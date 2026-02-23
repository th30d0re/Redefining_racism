//
//  DifferentialImpactScorer.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation

nonisolated struct DifferentialImpactScorer: Sendable {
    func score(clauses: [TierClassification]) -> Double {
        guard !clauses.isEmpty else { return 0.0 }

        var benefitElite = 0
        var benefitIngroupNonElite = 0
        var benefitOutgroup = 0
        var burdenOutgroup = 0
        var burdenIngroupNonElite = 0
        var burdenElite = 0

        for clause in clauses {
            switch clause.effectDirection {
            case .benefit:
                switch clause.targetGroup {
                case .elite:
                    benefitElite += 1
                case .ingroupNonElite:
                    benefitIngroupNonElite += 1
                case .outgroup:
                    benefitOutgroup += 1
                case .multiple:
                    break
                }
            case .burden:
                switch clause.targetGroup {
                case .outgroup:
                    burdenOutgroup += 1
                case .ingroupNonElite:
                    burdenIngroupNonElite += 1
                case .elite:
                    burdenElite += 1
                case .multiple:
                    break
                }
            case .neutral, .mixed:
                break
            }
        }

        let denominator = Double(max(clauses.count, 1))
        let rawScore = Double(benefitElite - benefitOutgroup + burdenOutgroup - burdenElite) / denominator
        return clamp(rawScore)
    }

    private func clamp(_ value: Double) -> Double {
        min(max(value, -1.0), 1.0)
    }
}
