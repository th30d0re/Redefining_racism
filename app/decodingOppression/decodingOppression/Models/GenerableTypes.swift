//
//  GenerableTypes.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/19/26.
//

import Foundation

#if canImport(FoundationModels)
import FoundationModels

// MARK: - Clause classification (classification-first order for constrained decoding)

@Generable(description: "Classification of a policy clause by target group and effect direction")
struct ClauseClassification {

    @Guide(description: "Which group the clause primarily targets")
    var targetGroup: TargetGroup

    @Guide(description: "Whether the clause imposes burden, confers benefit, or is neutral/mixed")
    var effectDirection: EffectDirection

    @Guide(description: "Confidence score 0-1", .range(0.0...1.0))
    var confidence: Double

    @Guide(description: "Brief rationale for the classification")
    var rationale: String
}

// MARK: - Architecture detection scores

@Generable(description: "Architectural bias scores for a clause (0-1 each)")
struct ArchitectureDetection: Codable {
    @Guide(description: "Asymmetric autonomy restriction", .range(0.0...1.0))
    var asymmetricAutonomyRestriction: Double

    @Guide(description: "Selective empathy", .range(0.0...1.0))
    var selectiveEmpathy: Double

    @Guide(description: "Ideological justification", .range(0.0...1.0))
    var ideologicalJustification: Double

    @Guide(description: "Resistance to structural critique", .range(0.0...1.0))
    var resistanceToStructuralCritique: Double
}

#endif

