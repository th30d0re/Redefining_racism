//
//  PolicyHistoryViewStyle.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct PolicyHistoryViewStyle {
    static func coiBadgeColor(_ coi: Double, differentiateWithoutColor: Bool) -> (Color, String) {
        switch coi {
        case 0.6...:
            return (.red, "exclamationmark.triangle")
        case 0.3..<0.6:
            return (.orange, "minus.circle")
        default:
            return (.green, "checkmark.shield")
        }
    }
}
