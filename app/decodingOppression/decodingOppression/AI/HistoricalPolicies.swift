//
//  HistoricalPolicies.swift
//  decodingOppression
//
//  Single source of truth for expected COI of known historical policies.
//  Consumed by HistoricalBaselineTool (T4) and ValidationRunner (T8/T9).
//

import Foundation

nonisolated struct HistoricalPolicy: Sendable {
    let name: String
    let year: Int
    let clauses: [TierClassification]
    let expectedCOI: Double
}

nonisolated struct HistoricalPolicies {
    static let virginiaSlaveCodes = HistoricalPolicy(
        name: "Virginia Slave Codes (1705)",
        year: 1705,
        clauses: [
            makeClause(
                targetGroup: .outgroup,
                effectDirection: .burden,
                aar: 0.95,
                se: 0.9,
                ij: 0.85,
                rsc: 0.9,
                usesProxyVariables: false,
                proxyTerms: [],
                expandsOutgroup: true
            ),
            makeClause(
                targetGroup: .elite,
                effectDirection: .benefit,
                aar: 0.8,
                se: 0.7,
                ij: 0.75,
                rsc: 0.8,
                usesProxyVariables: false,
                proxyTerms: [],
                expandsOutgroup: false
            ),
            makeClause(
                targetGroup: .outgroup,
                effectDirection: .burden,
                aar: 0.9,
                se: 0.85,
                ij: 0.8,
                rsc: 0.95,
                usesProxyVariables: true,
                proxyTerms: ["property", "servitude"],
                expandsOutgroup: false
            ),
            makeClause(
                targetGroup: .ingroupNonElite,
                effectDirection: .benefit,
                aar: 0.6,
                se: 0.55,
                ij: 0.5,
                rsc: 0.6,
                usesProxyVariables: false,
                proxyTerms: [],
                expandsOutgroup: false
            ),
        ],
        expectedCOI: 0.93
    )

    static let thirteenthAmendment = HistoricalPolicy(
        name: "13th Amendment (1865)",
        year: 1865,
        clauses: [
            makeClause(
                targetGroup: .outgroup,
                effectDirection: .benefit,
                aar: 0.2,
                se: 0.25,
                ij: 0.15,
                rsc: 0.2,
                usesProxyVariables: false,
                proxyTerms: [],
                expandsOutgroup: false
            ),
            makeClause(
                targetGroup: .multiple,
                effectDirection: .neutral,
                aar: 0.1,
                se: 0.1,
                ij: 0.1,
                rsc: 0.1,
                usesProxyVariables: false,
                proxyTerms: [],
                expandsOutgroup: false
            ),
            makeClause(
                targetGroup: .elite,
                effectDirection: .burden,
                aar: 0.3,
                se: 0.2,
                ij: 0.2,
                rsc: 0.25,
                usesProxyVariables: false,
                proxyTerms: [],
                expandsOutgroup: false
            ),
        ],
        expectedCOI: 0.35
    )

    static let holcRedlining = HistoricalPolicy(
        name: "HOLC Redlining (1934)",
        year: 1934,
        clauses: [
            makeClause(
                targetGroup: .outgroup,
                effectDirection: .burden,
                aar: 0.85,
                se: 0.8,
                ij: 0.75,
                rsc: 0.9,
                usesProxyVariables: true,
                proxyTerms: ["risk", "neighborhood", "stability"],
                expandsOutgroup: true
            ),
            makeClause(
                targetGroup: .elite,
                effectDirection: .benefit,
                aar: 0.7,
                se: 0.6,
                ij: 0.65,
                rsc: 0.7,
                usesProxyVariables: false,
                proxyTerms: [],
                expandsOutgroup: false
            ),
            makeClause(
                targetGroup: .outgroup,
                effectDirection: .burden,
                aar: 0.8,
                se: 0.75,
                ij: 0.7,
                rsc: 0.85,
                usesProxyVariables: true,
                proxyTerms: ["credit", "property"],
                expandsOutgroup: false
            ),
            makeClause(
                targetGroup: .ingroupNonElite,
                effectDirection: .benefit,
                aar: 0.4,
                se: 0.45,
                ij: 0.4,
                rsc: 0.5,
                usesProxyVariables: false,
                proxyTerms: [],
                expandsOutgroup: false
            ),
        ],
        expectedCOI: 0.82
    )

    static let warOnDrugs = HistoricalPolicy(
        name: "War on Drugs (1971)",
        year: 1971,
        clauses: [
            makeClause(
                targetGroup: .outgroup,
                effectDirection: .burden,
                aar: 0.8,
                se: 0.7,
                ij: 0.75,
                rsc: 0.85,
                usesProxyVariables: true,
                proxyTerms: ["crime", "narcotics", "drug-free"],
                expandsOutgroup: true
            ),
            makeClause(
                targetGroup: .elite,
                effectDirection: .benefit,
                aar: 0.6,
                se: 0.55,
                ij: 0.6,
                rsc: 0.7,
                usesProxyVariables: false,
                proxyTerms: [],
                expandsOutgroup: false
            ),
            makeClause(
                targetGroup: .outgroup,
                effectDirection: .burden,
                aar: 0.75,
                se: 0.65,
                ij: 0.7,
                rsc: 0.8,
                usesProxyVariables: true,
                proxyTerms: ["gangs"],
                expandsOutgroup: false
            ),
            makeClause(
                targetGroup: .ingroupNonElite,
                effectDirection: .burden,
                aar: 0.45,
                se: 0.4,
                ij: 0.35,
                rsc: 0.5,
                usesProxyVariables: false,
                proxyTerms: [],
                expandsOutgroup: false
            ),
        ],
        expectedCOI: 0.78
    )

    static var chain: [HistoricalPolicy] {
        [virginiaSlaveCodes, thirteenthAmendment, holcRedlining, warOnDrugs]
    }

    /// Returns the expected COI (0-1) for a known historical policy name; 0.0 for unrecognised names.
    static func score(for policyName: String) -> Double {
        switch policyName {
        case "Virginia Slave Codes (1705)": return 0.93
        case "13th Amendment (1865)": return 0.35
        case "HOLC Redlining (1934)": return 0.82
        case "War on Drugs (1971)": return 0.78
        default: return 0.0
        }
    }

    private static func makeClause(
        targetGroup: TargetGroup,
        effectDirection: EffectDirection,
        aar: Double,
        se: Double,
        ij: Double,
        rsc: Double,
        usesProxyVariables: Bool,
        proxyTerms: [String],
        expandsOutgroup: Bool,
        confidence: Double = 0.88,
        tier: MLTier = .tier3
    ) -> TierClassification {
        TierClassification(
            targetGroup: targetGroup,
            effectDirection: effectDirection,
            architectureScores: ArchitectureScores(aar: aar, se: se, ij: ij, rsc: rsc),
            proxyDetection: ProxyDetection(
                usesProxyVariables: usesProxyVariables,
                proxyTerms: proxyTerms,
                expandsOutgroup: expandsOutgroup
            ),
            confidence: confidence,
            tier: tier,
            wasSafetyFallback: false
        )
    }
}
