//
//  AnalysisPipeline.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/22/26.
//

import Foundation

actor AnalysisPipeline {
    private let tier1: Tier1EngineProtocol
    private let resolver: TierResolving
    private let scorer: PolicyScorer

    init(tier1: Tier1EngineProtocol, resolver: TierResolving, scorer: PolicyScorer) {
        self.tier1 = tier1
        self.resolver = resolver
        self.scorer = scorer
    }

    init(tier1: Tier1Engine, resolver: TierResolver, scorer: PolicyScorer) {
        self.tier1 = tier1
        self.resolver = resolver
        self.scorer = scorer
    }

    func analyze(pdfURL: URL) -> AsyncStream<AnalysisProgress> {
        let tier1 = tier1
        let resolver = resolver
        let scorer = scorer

        return AsyncStream<AnalysisProgress> { continuation in
            let task = Task {
                continuation.yield(.extracting)

                let clauses: [Clause]
                do {
                    clauses = try await tier1.extractAndPreprocess(pdf: pdfURL)
                } catch {
                    continuation.yield(.failed(error))
                    continuation.finish()
                    return
                }

                var classified: [TierClassification] = []
                let total = clauses.count

                for (index, clause) in clauses.enumerated() {
                    do {
                        try Task.checkCancellation()
                    } catch is CancellationError {
                        continuation.finish()
                        return
                    } catch {
                        continuation.finish()
                        return
                    }

                    let classification = await resolver.classify(clause: clause)
                    classified.append(classification)
                    let partialScores = scorer.score(clauses: classified)
                    continuation.yield(
                        .classifying(
                            clauseIndex: index,
                            total: total,
                            partialScores: partialScores,
                            clause: clause,
                            classification: classification
                        )
                    )
                }

                let finalScore = scorer.score(clauses: classified)
                continuation.yield(.complete(finalScore))
                continuation.finish()
            }

            continuation.onTermination = { _ in
                task.cancel()
            }
        }
    }
}
