//
//  HistoricalBaselineTool.swift
//  decodingOppression
//
//  Tool returning the COI of a known historical policy for model comparison.
//

import Foundation

#if canImport(FoundationModels)
import FoundationModels

struct HistoricalBaselineTool: Tool {
    let name = "getHistoricalBaseline"
    let description = "Returns the COI of a known historical policy for comparison."

    @Generable
    struct Arguments {
        @Guide(description: "Historical policy name", .anyOf([
            "Virginia Slave Codes (1705)",
            "13th Amendment (1865)",
            "HOLC Redlining (1934)",
            "War on Drugs (1971)"
        ]))
        var policyName: String
    }

    func call(arguments: Arguments) async throws -> String {
        let coi = HistoricalPolicies.score(for: arguments.policyName)
        return "Historical COI for \(arguments.policyName): \(coi)"
    }
}

#else

struct HistoricalBaselineTool {
    let name = "getHistoricalBaseline"
    let description = "Returns the COI of a known historical policy for comparison."
}

#endif
