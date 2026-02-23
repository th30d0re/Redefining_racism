//
//  ValidationRunner.swift
//  decodingOppression
//
//  macOS-only stateless runner: compares scorer output to HistoricalPolicies expected COI (T8).
//

#if os(macOS)

import Foundation

struct ValidationRunner: Sendable {
    /// Runs one policy and returns a ValidationResult. COI from scorer is already in [0,1]; no remapping needed.
    func run(policy: HistoricalPolicy, scorer: PolicyScorer) -> ValidationResult {
        let result = scorer.score(clauses: policy.clauses)
        return ValidationResult(
            policyName: policy.name,
            year: policy.year,
            expectedCOI: policy.expectedCOI,
            actualCOI: result.coi
        )
    }

    /// Runs all policies in HistoricalPolicies.chain.
    func runAll(scorer: PolicyScorer) -> [ValidationResult] {
        HistoricalPolicies.chain.map { run(policy: $0, scorer: scorer) }
    }
}

#endif