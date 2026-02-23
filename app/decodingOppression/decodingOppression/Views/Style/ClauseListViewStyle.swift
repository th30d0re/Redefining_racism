//
//  ClauseListViewStyle.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct ClauseListViewStyle {
    static func scoreColor(_ score: Double) -> Color {
        if score >= 0.3 { return .red }
        if score <= -0.3 { return .green }
        return .secondary
    }
}
