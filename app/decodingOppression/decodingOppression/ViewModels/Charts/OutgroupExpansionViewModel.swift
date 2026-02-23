//
//  OutgroupExpansionViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation

@Observable
@MainActor
final class OutgroupExpansionViewModel {
    var analysis: PolicyAnalysis

    init(analysis: PolicyAnalysis) {
        self.analysis = analysis
    }

    var expansionRate: Double {
        guard !analysis.clauses.isEmpty else { return 0 }
        let count = analysis.clauses.filter { $0.expandsOutgroup }.count
        return Double(count) / Double(analysis.clauses.count)
    }

    var proxyUsageRate: Double {
        guard !analysis.clauses.isEmpty else { return 0 }
        let count = analysis.clauses.filter { !$0.proxyTerms.isEmpty }.count
        return Double(count) / Double(analysis.clauses.count)
    }

    var proxyDensity: Double {
        guard !analysis.clauses.isEmpty else { return 0 }
        let totalTerms = analysis.clauses.reduce(0) { $0 + $1.proxyTerms.count }
        return (Double(totalTerms) / Double(analysis.clauses.count)) / 5.0
    }

    var uniqueProxyTerms: [String] {
        let terms = analysis.clauses.flatMap { $0.proxyTerms }
        return Array(Set(terms)).sorted()
    }
}
