//
//  ScoreCardViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation

@Observable
@MainActor
final class ScoreCardViewModel {
    var analysis: PolicyAnalysis
    var isShowingExport: Bool = false

    init(analysis: PolicyAnalysis) {
        self.analysis = analysis
    }

    var interpretation: String {
        let coi = analysis.scoreResult.coi
        if coi >= 0.6 {
            return "Highly Oppressive"
        }
        if coi >= 0.3 {
            return "Moderately Oppressive"
        }
        if coi < 0 {
            return "Liberatory"
        }
        return "Low Oppression"
    }
}
