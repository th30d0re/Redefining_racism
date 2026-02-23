//
//  OutgroupAnalyzer.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation

nonisolated struct OutgroupAnalyzer: Sendable {
    func score(clauses: [TierClassification]) -> Double {
        guard !clauses.isEmpty else { return 0.0 }

        var expansionCount = 0
        var proxyCount = 0
        var proxyTermTotal = 0

        for clause in clauses {
            if clause.proxyDetection.expandsOutgroup {
                expansionCount += 1
            }
            if clause.proxyDetection.usesProxyVariables {
                proxyCount += 1
            }
            proxyTermTotal += clause.proxyDetection.proxyTerms.count
        }

        let count = Double(clauses.count)
        let expansionScore = Double(expansionCount) / count
        let proxyScore = Double(proxyCount) / count
        let proxyDensity = (Double(proxyTermTotal) / count) / 5.0

        let oes = (expansionScore + proxyScore + proxyDensity) / 3.0
        let mapped = 2 * oes - 1
        return clamp(mapped)
    }

    private func clamp(_ value: Double) -> Double {
        min(max(value, -1.0), 1.0)
    }
}
