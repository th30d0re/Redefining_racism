//
//  Tier3Engine.swift
//  decodingOppression
//
//  Facade mirroring Tier2Engine; gates Foundation Models classification behind availability.
//

import Foundation

#if canImport(FoundationModels)
import FoundationModels

actor Tier3Engine {
    private let session = PolicyAnalysisSession()

    private func checkAvailability() throws {
        switch SystemLanguageModel.default.availability {
        case .available:
            return
        case .unavailable(let reason):
            switch reason {
            case .deviceNotEligible:
                throw Tier3Error.unavailable
            case .appleIntelligenceNotEnabled:
                throw Tier3Error.unavailable
            case .modelNotReady:
                throw Tier3Error.unavailable
            @unknown default:
                throw Tier3Error.unavailable
            }
        }
    }

    func isAvailable() -> Bool {
        if case .available = SystemLanguageModel.default.availability { return true }
        return false
    }

    func classify(clause: Clause) async throws -> TierClassification? {
        do {
            try checkAvailability()
        } catch Tier3Error.unavailable {
            return nil
        }

        do {
            async let classification = session.classifyClause(clause)
            async let architecture = session.detectArchitecture(clause)
            async let proxy = session.detectProxy(clause)
            let (c, a, p) = try await (classification, architecture, proxy)

            let targetGroup: TargetGroup
            switch c.targetGroup {
            case .outgroup: targetGroup = .outgroup
            case .ingroupNonElite: targetGroup = .ingroupNonElite
            case .elite: targetGroup = .elite
            case .multiple: targetGroup = .multiple
            }

            let effectDirection: EffectDirection
            switch c.effectDirection {
            case .burden: effectDirection = .burden
            case .benefit: effectDirection = .benefit
            case .neutral: effectDirection = .neutral
            case .mixed: effectDirection = .mixed
            }

            let scores = ArchitectureScores(
                aar: a.asymmetricAutonomyRestriction,
                se: a.selectiveEmpathy,
                ij: a.ideologicalJustification,
                rsc: a.resistanceToStructuralCritique
            )

            return TierClassification(
                targetGroup: targetGroup,
                effectDirection: effectDirection,
                architectureScores: scores,
                proxyDetection: p,
                confidence: c.confidence,
                tier: .tier3,
                wasSafetyFallback: false
            )
        } catch Tier3Error.safetyGuardrail {
            print("[Tier3] Safety guardrail triggered for clause \(clause.id)")
            throw Tier3Error.safetyGuardrail
        } catch Tier3Error.contextWindowExceeded {
            print("[Tier3] Context window exceeded for clause \(clause.id)")
            return nil
        } catch Tier3Error.sessionFailed(let error) {
            print("[Tier3] Session failed for clause \(clause.id): \(error)")
            return nil
        }
    }

    func streamClassify(clause: Clause) -> AsyncThrowingStream<ArchitectureDetection.PartiallyGenerated, Error> {
        do {
            try checkAvailability()
        } catch Tier3Error.unavailable {
            return AsyncThrowingStream { $0.finish() }
        } catch {
            return AsyncThrowingStream { $0.finish(throwing: error) }
        }

        return AsyncThrowingStream { continuation in
            Task {
                do {
                    let stream = await session.streamArchitecture(clause)
                    for try await partial in stream {
                        continuation.yield(partial)
                    }
                    continuation.finish()
                } catch Tier3Error.safetyGuardrail {
                    print("[Tier3] Safety guardrail triggered (stream) for clause \(clause.id)")
                    continuation.finish()
                } catch Tier3Error.contextWindowExceeded {
                    print("[Tier3] Context window exceeded (stream) for clause \(clause.id)")
                    continuation.finish()
                } catch Tier3Error.sessionFailed(let error) {
                    print("[Tier3] Session failed (stream) for clause \(clause.id): \(error)")
                    continuation.finish()
                } catch {
                    continuation.finish(throwing: error)
                }
            }
        }
    }

}

#else

actor Tier3Engine {
    func isAvailable() -> Bool { false }

    func classify(clause: Clause) async throws -> TierClassification? {
        throw Tier3Error.unavailable
    }

    func streamClassify(clause: Clause) -> AsyncThrowingStream<ArchitectureDetection.PartiallyGenerated, Error> {
        AsyncThrowingStream { $0.finish(throwing: Tier3Error.unavailable) }
    }
}

#endif
