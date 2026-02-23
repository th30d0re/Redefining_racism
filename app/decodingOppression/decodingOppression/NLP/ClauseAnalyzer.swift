//
//  ClauseAnalyzer.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/22/26.
//

import Foundation

actor ClauseAnalyzer {
    private let keywordEngine: KeywordEngine

    init(keywordEngine: KeywordEngine) {
        self.keywordEngine = keywordEngine
    }

    func analyze(clause: Clause) async -> TierClassification {
        let vector = await keywordEngine.analyze(clause: clause)

        let targetGroup = resolveTargetGroup(using: vector)
        let effectDirection = resolveEffectDirection(using: vector)

        let architectureScores = ArchitectureScores(
            aar: vector.outgroupBurdenScore,
            se: max(0, vector.ingroupBenefitScore - vector.outgroupBurdenScore),
            ij: vector.proxyTermsFound.isEmpty
                ? 0.0
                : 0.5 + 0.1 * Double(min(5, vector.proxyTermsFound.count)),
            rsc: 0.1
        )

        let proxyDetection = ProxyDetection(
            usesProxyVariables: !vector.proxyTermsFound.isEmpty,
            proxyTerms: vector.proxyTermsFound,
            expandsOutgroup: vector.outgroupBurdenScore > 0.5 && !vector.proxyTermsFound.isEmpty
        )

        return TierClassification(
            targetGroup: targetGroup,
            effectDirection: effectDirection,
            architectureScores: architectureScores,
            proxyDetection: proxyDetection,
            confidence: vector.confidence,
            tier: .tier1,
            wasSafetyFallback: false
        )
    }

    private func resolveTargetGroup(using vector: KeywordFeatureVector) -> TargetGroup {
        let scoredGroups: [(TargetGroup, Double)] = [
            (.outgroup, vector.outgroupBurdenScore),
            (.ingroupNonElite, vector.ingroupBenefitScore),
            (.elite, vector.eliteExtractionScore)
        ]

        let sorted = scoredGroups.sorted { $0.1 > $1.1 }
        guard let top = sorted.first, let runnerUp = sorted.dropFirst().first else {
            return .multiple
        }

        return (top.1 - runnerUp.1) >= 0.1 ? top.0 : .multiple
    }

    private func resolveEffectDirection(using vector: KeywordFeatureVector) -> EffectDirection {
        let burdenScore = vector.outgroupBurdenScore
        let ingroupScore = vector.ingroupBenefitScore
        let eliteScore = vector.eliteExtractionScore
        let benefitScore = max(ingroupScore, eliteScore)

        if burdenScore > 0.3 && benefitScore > 0.3 {
            return .mixed
        }

        if burdenScore > 0.3 && burdenScore > benefitScore {
            return .burden
        }

        if (ingroupScore > 0.3 || eliteScore > 0.3) && benefitScore > burdenScore {
            return .benefit
        }

        if burdenScore < 0.3 && ingroupScore < 0.3 && eliteScore < 0.3 {
            return .neutral
        }

        return .neutral
    }
}
