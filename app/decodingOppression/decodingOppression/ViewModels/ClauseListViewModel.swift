//
//  ClauseListViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation

@Observable
@MainActor
final class ClauseListViewModel {
    var analysis: PolicyAnalysis

    init(analysis: PolicyAnalysis) {
        self.analysis = analysis
    }

    var oppressiveClauses: [ClauseScore] {
        clauseScores.filter { $0.score >= 0.3 }
    }

    var liberatoryClauses: [ClauseScore] {
        clauseScores.filter { $0.score <= -0.3 }
    }

    private var clauseScores: [ClauseScore] {
        analysis.clauses.map { clause in
            let architectureAvg = (
                clause.architectureScores.aar +
                clause.architectureScores.se +
                clause.architectureScores.ij +
                clause.architectureScores.rsc
            ) / 4

            let directionMultiplier: Double
            switch clause.effectDirection {
            case .burden:
                directionMultiplier = 1
            case .benefit:
                directionMultiplier = -1
            case .mixed:
                directionMultiplier = 0.5
            case .neutral:
                directionMultiplier = 0
            }

            let score = architectureAvg * directionMultiplier
            return ClauseScore(clause: clause, score: score)
        }
    }
}

struct ClauseScore: Identifiable {
    let id = UUID()
    let clause: AnalyzedClause
    let score: Double
}
