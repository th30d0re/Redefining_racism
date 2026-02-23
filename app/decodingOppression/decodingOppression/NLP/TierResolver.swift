//
//  TierResolver.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/22/26.
//

import Foundation

protocol Tier1EngineProtocol: Sendable {
    func extractAndPreprocess(pdf url: URL) async throws -> [Clause]
    func classify(clause: Clause) async -> TierClassification
}

protocol Tier2EngineProtocol: Sendable {
    func classify(clause: Clause) async throws -> TierClassification?
}

protocol Tier3EngineProtocol: Sendable {
    func classify(clause: Clause) async throws -> TierClassification?
}

protocol TierResolving: Sendable {
    func classify(clause: Clause) async -> TierClassification
}

extension Tier1Engine: Tier1EngineProtocol {}
extension Tier2Engine: Tier2EngineProtocol {}
extension Tier3Engine: Tier3EngineProtocol {}

actor TierResolver: TierResolving {
    private let tier1: Tier1EngineProtocol
    private let tier2: Tier2EngineProtocol
    private let tier3: Tier3EngineProtocol

    init(tier1: Tier1EngineProtocol, tier2: Tier2EngineProtocol, tier3: Tier3EngineProtocol) {
        self.tier1 = tier1
        self.tier2 = tier2
        self.tier3 = tier3
    }

    init(tier1: Tier1Engine, tier2: Tier2Engine, tier3: Tier3Engine) {
        self.init(
            tier1: tier1 as Tier1EngineProtocol,
            tier2: tier2 as Tier2EngineProtocol,
            tier3: tier3 as Tier3EngineProtocol
        )
    }

    func classify(clause: Clause) async -> TierClassification {
        let tier1Result = await tier1.classify(clause: clause)
        if tier1Result.confidence >= 0.85 {
            return tier1Result
        }

        let tier2 = tier2
        let tier3 = tier3

        async let tier2Result: TierClassification? = {
            do {
                return try await tier2.classify(clause: clause)
            } catch {
                return nil
            }
        }()

        async let tier3Outcome: (TierClassification?, Bool) = {
            do {
                return (try await tier3.classify(clause: clause), false)
            } catch Tier3Error.safetyGuardrail {
                return (nil, true)
            } catch {
                return (nil, false)
            }
        }()

        let (t2, t3Outcome) = await (tier2Result, tier3Outcome)
        let (t3, wasSafetyFallback) = t3Outcome
        let candidates = [t2, t3].compactMap { $0 }
        if let best = candidates.max(by: { $0.confidence < $1.confidence }) {
            if wasSafetyFallback, best.tier == .tier2 {
                var fallback = best
                fallback.wasSafetyFallback = true
                return fallback
            }
            return best
        }

        return tier1Result
    }
}
