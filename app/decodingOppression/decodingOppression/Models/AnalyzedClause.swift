//
//  AnalyzedClause.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/19/26.
//

import Foundation
import SwiftData

@Model
final class AnalyzedClause {
    var id: UUID
    var text: String
    var sectionType: SectionType
    var targetGroup: TargetGroup
    var effectDirection: EffectDirection
    var confidence: Double
    var tierUsed: MLTier
    @Attribute(.externalStorage)
    private var architectureScoresData: Data
    var proxyTerms: [String]
    var expandsOutgroup: Bool
    var wasSafetyFallback: Bool
    @Relationship(inverse: \PolicyAnalysis.clauses)
    var analysis: PolicyAnalysis?

    var architectureScores: ArchitectureScores {
        get {
            (try? JSONDecoder().decode(ArchitectureScores.self, from: architectureScoresData))
                ?? ArchitectureScores(aar: 0, se: 0, ij: 0, rsc: 0)
        }
        set {
            architectureScoresData = (try? JSONEncoder().encode(newValue)) ?? Data()
        }
    }

    init(
        id: UUID = UUID(),
        text: String,
        sectionType: SectionType,
        targetGroup: TargetGroup,
        effectDirection: EffectDirection,
        confidence: Double,
        tierUsed: MLTier,
        architectureScores: ArchitectureScores = ArchitectureScores(aar: 0, se: 0, ij: 0, rsc: 0),
        proxyTerms: [String] = [],
        expandsOutgroup: Bool = false,
        wasSafetyFallback: Bool = false,
        analysis: PolicyAnalysis? = nil
    ) {
        self.id = id
        self.text = text
        self.sectionType = sectionType
        self.targetGroup = targetGroup
        self.effectDirection = effectDirection
        self.confidence = confidence
        self.tierUsed = tierUsed
        self.architectureScoresData = (try? JSONEncoder().encode(architectureScores)) ?? Data()
        self.proxyTerms = proxyTerms
        self.expandsOutgroup = expandsOutgroup
        self.wasSafetyFallback = wasSafetyFallback
        self.analysis = analysis
    }
}
