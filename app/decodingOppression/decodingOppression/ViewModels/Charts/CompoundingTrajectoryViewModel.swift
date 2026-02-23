//
//  CompoundingTrajectoryViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation

@Observable
@MainActor
final class CompoundingTrajectoryViewModel {
    var analysis: PolicyAnalysis

    init(analysis: PolicyAnalysis) {
        self.analysis = analysis
    }

    var points: [CompoundingPoint] {
        let alpha = 0.1
        var baseline = 1.0
        var results: [CompoundingPoint] = []

        for policy in HistoricalPolicies.chain {
            baseline *= (1 - alpha * policy.expectedCOI)
            results.append(CompoundingPoint(year: policy.year, capacity: baseline, name: policy.name, isCurrent: false))
        }

        let currentYear = Calendar.current.component(.year, from: analysis.dateAnalyzed)
        baseline *= (1 - alpha * analysis.scoreResult.coi)
        results.append(CompoundingPoint(year: currentYear, capacity: baseline, name: analysis.policyName, isCurrent: true))

        return results
    }

    var summary: String {
        let values = points.map { "\($0.year): \($0.capacity.formatted(.percent))" }
        return values.joined(separator: ", ")
    }
}

struct CompoundingPoint: Identifiable {
    let id = UUID()
    let year: Int
    let capacity: Double
    let name: String
    let isCurrent: Bool
}
