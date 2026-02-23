//
//  ValidationViewStyle.swift
//  decodingOppression
//
//  macOS-only style for ValidationView (T8).
//

#if os(macOS)

import SwiftUI

struct ValidationViewStyle {
    static func resultColor(passed: Bool, differentiateWithoutColor: Bool) -> (Color, String) {
        if differentiateWithoutColor {
            return passed ? (.primary, "checkmark.circle") : (.primary, "xmark.circle")
        }
        return passed ? (.green, "checkmark.circle") : (.red, "xmark.circle")
    }

    static func cardBorderColor(passed: Bool) -> Color {
        passed ? Color.green.opacity(0.5) : Color.red.opacity(0.5)
    }

    static func bannerBackground(allPassed: Bool) -> Color {
        allPassed ? Color.green.opacity(0.15) : Color.red.opacity(0.15)
    }
}

#endif
