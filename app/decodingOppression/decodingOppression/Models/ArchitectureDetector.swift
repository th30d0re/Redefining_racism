//
//  ArchitectureDetector.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation

nonisolated struct ArchitectureDetector: Sendable {
    func score(clauses: [TierClassification]) -> Double {
        guard !clauses.isEmpty else { return 0.0 }

        var aarSum: Double = 0
        var seSum: Double = 0
        var ijSum: Double = 0
        var rscSum: Double = 0

        for clause in clauses {
            let scores = clause.architectureScores
            aarSum += scores.aar
            seSum += scores.se
            ijSum += scores.ij
            rscSum += scores.rsc
        }

        let count = Double(clauses.count)
        let meanAAR = aarSum / count
        let meanSE = seSum / count
        let meanIJ = ijSum / count
        let meanRSC = rscSum / count

        let ads = 0.35 * meanAAR + 0.20 * meanSE + 0.20 * meanIJ + 0.25 * meanRSC
        let mapped = 2 * ads - 1
        return clamp(mapped)
    }

    private func clamp(_ value: Double) -> Double {
        min(max(value, -1.0), 1.0)
    }
}
