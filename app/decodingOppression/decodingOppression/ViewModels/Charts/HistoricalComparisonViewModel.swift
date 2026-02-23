//
//  HistoricalComparisonViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation

@Observable
@MainActor
final class HistoricalComparisonViewModel {
    var analysis: PolicyAnalysis

    init(analysis: PolicyAnalysis) {
        self.analysis = analysis
    }

    var entries: [HistoricalComparisonEntry] {
        var items = HistoricalPolicies.chain.map {
            HistoricalComparisonEntry(
                name: $0.name,
                coi: $0.expectedCOI,
                isCurrent: false
            )
        }
        items.append(
            HistoricalComparisonEntry(
                name: analysis.policyName,
                coi: analysis.scoreResult.coi,
                isCurrent: true
            )
        )
        return items
    }
}

struct HistoricalComparisonEntry: Identifiable {
    let id = UUID()
    let name: String
    let coi: Double
    let isCurrent: Bool
}
