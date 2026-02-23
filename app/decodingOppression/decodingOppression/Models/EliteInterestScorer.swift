//
//  EliteInterestScorer.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation

nonisolated struct EliteInterestScorer: Sendable {
    func score(clauses: [TierClassification]) -> Double {
        guard !clauses.isEmpty else { return 0.0 }

        var extractionCount = 0
        var divisionCount = 0
        var rscSum: Double = 0

        for clause in clauses {
            let isExtraction = (clause.targetGroup == .elite && clause.effectDirection == .benefit)
                || (clause.targetGroup == .outgroup && clause.effectDirection == .burden)
            if isExtraction {
                extractionCount += 1
            }

            if clause.proxyDetection.usesProxyVariables || clause.proxyDetection.expandsOutgroup {
                divisionCount += 1
            }

            rscSum += clause.architectureScores.rsc
        }

        let count = Double(clauses.count)
        let extraction = Double(extractionCount) / count
        let resistanceSuppression = rscSum / count
        let divisionMaintenance = Double(divisionCount) / count

        let eis = 0.4 * extraction + 0.3 * resistanceSuppression + 0.3 * divisionMaintenance
        let mapped = 2 * eis - 1
        return clamp(mapped)
    }

    private func clamp(_ value: Double) -> Double {
        min(max(value, -1.0), 1.0)
    }
}
