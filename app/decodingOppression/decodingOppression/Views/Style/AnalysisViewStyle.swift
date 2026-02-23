//
//  AnalysisViewStyle.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct AnalysisViewStyle {
    static func gaugeAnimation(reduceMotion: Bool) -> Animation? {
        reduceMotion ? nil : .spring(duration: 0.6)
    }

    static func scoreColor(_ score: Double, differentiateWithoutColor: Bool) -> (Color, String) {
        if score < 0 {
            return (.blue, "arrow.down")
        }
        switch score {
        case 0.6...:
            return (.red, "exclamationmark.triangle")
        case 0.3..<0.6:
            return (.orange, "minus.circle")
        default:
            return (.green, "checkmark.shield")
        }
    }
}
