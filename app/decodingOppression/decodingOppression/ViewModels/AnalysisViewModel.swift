//
//  AnalysisViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation
import SwiftData

@Observable
@MainActor
final class AnalysisViewModel {
    var stage: String = "Preparing analysis..."
    var coiValue: Double = 0
    var partialScores: ScoreResult = .zero
    var clauseIndex: Int = 0
    var totalClauses: Int = 0
    var isComplete: Bool = false
    var error: Error?
    var finalAnalysis: PolicyAnalysis?
    var classifiedClauses: [TierClassification] = []

    private var clauseSnapshots: [Clause] = []
    private var analysisTask: Task<Void, Never>?

    func startAnalysis(pdfURL: URL, deps: AppDependencies, context: ModelContext) {
        guard analysisTask == nil else { return }

        stage = "Preparing analysis..."
        coiValue = 0
        partialScores = .zero
        clauseIndex = 0
        totalClauses = 0
        isComplete = false
        error = nil
        finalAnalysis = nil
        classifiedClauses = []
        clauseSnapshots = []

        analysisTask = Task { [weak self] in
            guard let self else { return }
            do {
                let pipeline = try deps.makeAnalysisPipeline()
                let stream = await pipeline.analyze(pdfURL: pdfURL)
                for await progress in stream {
                    switch progress {
                    case .extracting:
                        stage = "Extracting text..."
                    case .classifying(let index, let total, let partial, let clause, let classification):
                        let displayIndex = index + 1
                        stage = "Classifying clause \(displayIndex) of \(total)..."
                        clauseIndex = displayIndex
                        totalClauses = total
                        coiValue = partial.coi
                        partialScores = partial
                        classifiedClauses.append(classification)
                        clauseSnapshots.append(clause)
                    case .complete(let scoreResult):
                        let analysis = PolicyAnalysis(
                            policyName: pdfURL.deletingPathExtension().lastPathComponent,
                            sourceFilename: pdfURL.lastPathComponent,
                            dateAnalyzed: Date(),
                            scoreResult: scoreResult,
                            clauses: []
                        )

                        let analyzedClauses = zip(clauseSnapshots, classifiedClauses).map { clause, classification in
                            AnalyzedClause(
                                text: clause.text,
                                sectionType: clause.sectionType,
                                targetGroup: classification.targetGroup,
                                effectDirection: classification.effectDirection,
                                confidence: classification.confidence,
                                tierUsed: classification.tier,
                                architectureScores: classification.architectureScores,
                                proxyTerms: classification.proxyDetection.proxyTerms,
                                expandsOutgroup: classification.proxyDetection.expandsOutgroup,
                                wasSafetyFallback: classification.wasSafetyFallback,
                                analysis: analysis
                            )
                        }

                        analysis.clauses = analyzedClauses
                        context.insert(analysis)
                        finalAnalysis = analysis
                        isComplete = true
                        stage = "Analysis complete"
                        coiValue = scoreResult.coi
                        partialScores = scoreResult
                    case .failed(let error):
                        self.error = error
                        stage = "Analysis failed"
                    }
                }
            } catch {
                self.error = error
                stage = "Analysis failed"
            }

            analysisTask = nil
        }
    }

    func cancel() {
        analysisTask?.cancel()
        analysisTask = nil
    }
}
