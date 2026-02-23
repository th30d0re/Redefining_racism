//
//  ScoreResult.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/19/26.
//

import Foundation

nonisolated struct ScoreResult: Codable, Sendable {
    var dis: Double
    var ads: Double
    var eis: Double
    var cis: Double
    var oes: Double
    var coi: Double

    static var zero: ScoreResult {
        ScoreResult(dis: 0, ads: 0, eis: 0, cis: 0, oes: 0, coi: 0)
    }
}
