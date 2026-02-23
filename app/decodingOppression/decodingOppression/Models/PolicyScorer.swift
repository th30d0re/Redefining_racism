//
//  PolicyScorer.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/22/26.
//

import Foundation

nonisolated protocol PolicyScorer: Sendable {
    func score(clauses: [TierClassification]) -> ScoreResult
}

nonisolated struct StubPolicyScorer: PolicyScorer {
    func score(clauses: [TierClassification]) -> ScoreResult {
        .zero
    }
}

nonisolated struct DefaultPolicyScorer: PolicyScorer {
    private let dis: DifferentialImpactScorer
    private let ads: ArchitectureDetector
    private let eis: EliteInterestScorer
    private let cis: CompoundingCalculator
    private let oes: OutgroupAnalyzer

    init(
        dis: DifferentialImpactScorer = DifferentialImpactScorer(),
        ads: ArchitectureDetector = ArchitectureDetector(),
        eis: EliteInterestScorer = EliteInterestScorer(),
        cis: CompoundingCalculator = CompoundingCalculator(),
        oes: OutgroupAnalyzer = OutgroupAnalyzer()
    ) {
        self.dis = dis
        self.ads = ads
        self.eis = eis
        self.cis = cis
        self.oes = oes
    }

    func score(clauses: [TierClassification]) -> ScoreResult {
        let disScore = clamp(dis.score(clauses: clauses))
        let adsScore = clamp(ads.score(clauses: clauses))
        let eisScore = clamp(eis.score(clauses: clauses))
        let cisScore = clamp(cis.score(clauses: clauses))
        let oesScore = clamp(oes.score(clauses: clauses))

        let coi = 0.25 * disScore + 0.25 * adsScore + 0.20 * eisScore + 0.15 * cisScore + 0.15 * oesScore
        let coiScore = clamp(coi)

        return ScoreResult(
            dis: disScore,
            ads: adsScore,
            eis: eisScore,
            cis: cisScore,
            oes: oesScore,
            coi: coiScore
        )
    }

    private func clamp(_ value: Double) -> Double {
        min(max(value, 0.0), 1.0)
    }
}
