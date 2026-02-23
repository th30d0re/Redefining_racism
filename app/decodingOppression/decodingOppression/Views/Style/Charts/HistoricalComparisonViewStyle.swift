//
//  HistoricalComparisonViewStyle.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct HistoricalComparisonViewStyle {
    static func barColor(isCurrent: Bool) -> Color {
        isCurrent ? .accentColor : .secondary
    }
}
