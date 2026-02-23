//
//  TrainingDataViewStyle.swift
//  decodingOppression
//
//  macOS-only style for TrainingDataView (T8).
//

#if os(macOS)

import SwiftUI

struct TrainingDataViewStyle {
    static func unsavedDotOpacity(hasChanges: Bool) -> Double {
        hasChanges ? 1.0 : 0.0
    }

    static func sliderLabel(_ value: Double) -> String {
        String(format: "%.2f", value)
    }
}

#endif
