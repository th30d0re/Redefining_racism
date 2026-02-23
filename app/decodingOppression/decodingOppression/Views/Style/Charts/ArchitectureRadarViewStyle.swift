//
//  ArchitectureRadarViewStyle.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct ArchitectureRadarViewStyle {
    static func axisStrokeStyle(index: Int, differentiateWithoutColor: Bool) -> StrokeStyle {
        guard differentiateWithoutColor else {
            return StrokeStyle(lineWidth: 1)
        }
        let patterns: [[CGFloat]] = [
            [],
            [6, 3],
            [2, 3],
            [8, 2, 2, 2]
        ]
        return StrokeStyle(lineWidth: 1, dash: patterns[index % patterns.count])
    }

    static func polygonStrokeStyle(differentiateWithoutColor: Bool) -> StrokeStyle {
        StrokeStyle(lineWidth: 2, lineJoin: .round)
    }
}
