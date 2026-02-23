//
//  EliteInterestDetailViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation

@Observable
@MainActor
final class EliteInterestDetailViewModel {
    var analysis: PolicyAnalysis

    init(analysis: PolicyAnalysis) {
        self.analysis = analysis
    }

    var eliteClauseRate: Double {
        rate { $0.targetGroup == .elite }
    }

    var eliteBenefitRate: Double {
        rate { $0.targetGroup == .elite && $0.effectDirection == .benefit }
    }

    var eliteBurdenRate: Double {
        rate { $0.targetGroup == .elite && $0.effectDirection == .burden }
    }

    var eliteAverageConfidence: Double {
        let eliteClauses = analysis.clauses.filter { $0.targetGroup == .elite }
        guard !eliteClauses.isEmpty else { return 0 }
        let total = eliteClauses.reduce(0.0) { $0 + $1.confidence }
        return total / Double(eliteClauses.count)
    }

    private func rate(where predicate: (AnalyzedClause) -> Bool) -> Double {
        guard !analysis.clauses.isEmpty else { return 0 }
        let count = analysis.clauses.filter(predicate).count
        return Double(count) / Double(analysis.clauses.count)
    }
}
