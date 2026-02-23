//
//  ArchitectureRadarViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation

@Observable
@MainActor
final class ArchitectureRadarViewModel {
    var analysis: PolicyAnalysis

    init(analysis: PolicyAnalysis) {
        self.analysis = analysis
    }

    var components: [ArchitectureComponent] {
        let clauses = analysis.clauses
        guard !clauses.isEmpty else {
            return ArchitectureComponent.defaults
        }

        let count = Double(clauses.count)
        let aar = clauses.reduce(0.0) { $0 + $1.architectureScores.aar } / count
        let se = clauses.reduce(0.0) { $0 + $1.architectureScores.se } / count
        let ij = clauses.reduce(0.0) { $0 + $1.architectureScores.ij } / count
        let rsc = clauses.reduce(0.0) { $0 + $1.architectureScores.rsc } / count

        return [
            ArchitectureComponent(id: 0, name: "AAR", score: aar),
            ArchitectureComponent(id: 1, name: "SE", score: se),
            ArchitectureComponent(id: 2, name: "IJ", score: ij),
            ArchitectureComponent(id: 3, name: "RSC", score: rsc)
        ]
    }
}

struct ArchitectureComponent: Identifiable {
    let id: Int
    let name: String
    let score: Double

    static let defaults: [ArchitectureComponent] = [
        ArchitectureComponent(id: 0, name: "AAR", score: 0),
        ArchitectureComponent(id: 1, name: "SE", score: 0),
        ArchitectureComponent(id: 2, name: "IJ", score: 0),
        ArchitectureComponent(id: 3, name: "RSC", score: 0)
    ]
}
