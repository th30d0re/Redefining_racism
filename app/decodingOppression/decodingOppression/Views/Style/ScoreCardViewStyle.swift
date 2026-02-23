//
//  ScoreCardViewStyle.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct ScoreCardViewStyle {
    static func scoreRevealAnimation(reduceMotion: Bool) -> Animation? {
        reduceMotion ? nil : .easeOut(duration: 0.5)
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

    static func backgroundMaterial(reduceTransparency: Bool) -> Material {
        reduceTransparency ? .regular : .ultraThin
    }

    static func scoreFont(dynamicTypeSize: DynamicTypeSize, legibilityWeight: LegibilityWeight?) -> Font {
        let baseSize: CGFloat = dynamicTypeSize.isAccessibilitySize ? 48 : 36
        let weight: Font.Weight = legibilityWeight == .bold ? .bold : .semibold
        return .system(size: baseSize, weight: weight, design: .rounded)
    }
}
