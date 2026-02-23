//
//  PolicyAnalysis.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/19/26.
//

import Foundation
import SwiftData

@Model
final class PolicyAnalysis {
    var id: UUID
    var policyName: String
    var sourceFilename: String
    var dateAnalyzed: Date
    @Attribute(.externalStorage)
    private var scoreResultData: Data
    @Relationship(deleteRule: .cascade)
    var clauses: [AnalyzedClause]

    var scoreResult: ScoreResult {
        get {
            (try? JSONDecoder().decode(ScoreResult.self, from: scoreResultData)) ?? .zero
        }
        set {
            scoreResultData = (try? JSONEncoder().encode(newValue)) ?? Data()
        }
    }

    init(
        id: UUID = UUID(),
        policyName: String,
        sourceFilename: String,
        dateAnalyzed: Date,
        scoreResult: ScoreResult = .zero,
        clauses: [AnalyzedClause] = []
    ) {
        self.id = id
        self.policyName = policyName
        self.sourceFilename = sourceFilename
        self.dateAnalyzed = dateAnalyzed
        self.scoreResultData = (try? JSONEncoder().encode(scoreResult)) ?? Data()
        self.clauses = clauses
    }
}
