//
//  ValidationViewModel.swift
//  decodingOppression
//
//  macOS-only: state for ValidationView (T8).
//

#if os(macOS)

import Foundation

@Observable
@MainActor
final class ValidationViewModel {
    var results: [ValidationResult] = []
    var runningPolicyNames: Set<String> = []
    var summaryText: String?

    func runAll(runner: ValidationRunner, scorer: PolicyScorer) async {
        let policies = HistoricalPolicies.chain
        for policy in policies {
            runningPolicyNames.insert(policy.name)
        }
        let allResults = runner.runAll(scorer: scorer)
        runningPolicyNames.removeAll()
        results = allResults
        let passed = allResults.filter(\.passed).count
        let total = allResults.count
        summaryText = "\(passed) of \(total) tests passed"
    }

    func run(policy: HistoricalPolicy, runner: ValidationRunner, scorer: PolicyScorer) async {
        runningPolicyNames.insert(policy.name)
        let result = runner.run(policy: policy, scorer: scorer)
        runningPolicyNames.remove(policy.name)
        if let i = results.firstIndex(where: { $0.policyName == policy.name }) {
            results[i] = result
        } else {
            results.append(result)
        }
    }
}

#endif
