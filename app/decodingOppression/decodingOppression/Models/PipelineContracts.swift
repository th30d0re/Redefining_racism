//
//  PipelineContracts.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/19/26.
//

import Foundation
#if canImport(FoundationModels)
import FoundationModels
#endif

// MARK: - Architecture scores (Codable for pipeline and training)

struct ArchitectureScores: Codable, Sendable {
    var aar: Double  // asymmetric autonomy restriction
    var se: Double   // selective empathy
    var ij: Double   // ideological justification
    var rsc: Double  // resistance to structural critique
}

// MARK: - Analysis progress

enum AnalysisProgress {
    case extracting
    case classifying(
        clauseIndex: Int,
        total: Int,
        partialScores: ScoreResult,
        clause: Clause,
        classification: TierClassification
    )
    case complete(ScoreResult)
    case failed(Error)
}

// MARK: - Proxy detection

#if canImport(FoundationModels)
@Generable(description: "Detection of proxy variables or dog-whistle language")
#endif
struct ProxyDetection: Codable, Sendable {
    #if canImport(FoundationModels)
    @Guide(description: "Whether the clause uses proxy variables for outgroup targeting")
    #endif
    var usesProxyVariables: Bool

    #if canImport(FoundationModels)
    @Guide(description: "List of proxy terms found (up to 5 items)", .count(0...5))
    #endif
    var proxyTerms: [String]

    #if canImport(FoundationModels)
    @Guide(description: "Whether language expands the outgroup definition")
    #endif
    var expandsOutgroup: Bool
}

// MARK: - Tier classification result

struct TierClassification: Sendable {
    var targetGroup: TargetGroup
    var effectDirection: EffectDirection
    var architectureScores: ArchitectureScores
    var proxyDetection: ProxyDetection
    var confidence: Double
    var tier: MLTier
    var wasSafetyFallback: Bool
}