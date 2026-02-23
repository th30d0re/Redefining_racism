//
//  TrainingViewStyle.swift
//  decodingOppression
//
//  macOS-only style for TrainingView (T8).
//

#if os(macOS)

import SwiftUI

struct TrainingViewStyle {
    static func trainButtonLabel(isTraining: Bool) -> String {
        isTraining ? "Cancel" : "Start Training"
    }

    static func progressAnimation(reduceMotion: Bool) -> Animation? {
        reduceMotion ? nil : .easeInOut(duration: 0.3)
    }

    static func lossLineColor(isTrain: Bool) -> Color {
        isTrain ? .blue : .orange
    }
}

#endif
