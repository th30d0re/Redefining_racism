//
//  CompoundingCalculator.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation

nonisolated struct CompoundingCalculator: Sendable {
    let alpha: Double
    let historicalChain: [HistoricalPolicy]

    init(alpha: Double = 0.1, historicalChain: [HistoricalPolicy] = HistoricalPolicies.chain) {
        self.alpha = alpha
        self.historicalChain = historicalChain
    }

    func score(clauses: [TierClassification]) -> Double {
        guard !clauses.isEmpty else { return 0.0 }

        let count = Double(clauses.count)
        let pNew = clauses.reduce(0.0) { partial, clause in
            let intensity = (clause.architectureScores.aar + clause.architectureScores.rsc) / 2
            return partial + intensity
        } / count

        var baseline = 1.0
        for policy in historicalChain {
            baseline *= (1 - alpha * policy.expectedCOI)
        }

        let final = baseline * (1 - alpha * pNew)
        let reduction = baseline - final
        guard alpha > 0 else { return 0.0 }

        let normalizedValue = reduction / alpha
        let clamped = Swift.min(Swift.max(normalizedValue, 0.0), 1.0)
        return clamped
    }

    private func clamp(_ value: Double) -> Double {
        Swift.min(Swift.max(value, 0.0), 1.0)
    }
}
