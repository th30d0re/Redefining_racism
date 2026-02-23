//
//  PolicyAnalysisSession.swift
//  decodingOppression
//
//  One session per clause (4k token constraint); academic framing and tool injection.
//

import Foundation

#if canImport(FoundationModels)
import FoundationModels

actor PolicyAnalysisSession {
    private let academicFramingPrefix = "You are an academic policy analyst. Provide precise, evidence-based analysis of each clause for research."
    private let retryCharacterLimit = 500

    func classifyClause(_ clause: Clause, options: GenerationOptions? = nil) async throws -> ClauseClassification {
        try await runWithRetry(clause: clause) { session, text in
            if let opts = options {
                let response = try await session.respond(to: text, generating: ClauseClassification.self, options: opts)
                return response.content
            } else {
                let response = try await session.respond(to: text, generating: ClauseClassification.self)
                return response.content
            }
        }
    }

    func detectArchitecture(_ clause: Clause, options: GenerationOptions? = nil) async throws -> ArchitectureDetection {
        try await runWithRetry(clause: clause) { session, text in
            if let opts = options {
                let response = try await session.respond(to: text, generating: ArchitectureDetection.self, options: opts)
                return response.content
            } else {
                let response = try await session.respond(to: text, generating: ArchitectureDetection.self)
                return response.content
            }
        }
    }

    func detectProxy(_ clause: Clause, options: GenerationOptions? = nil) async throws -> ProxyDetection {
        try await runWithRetry(clause: clause) { session, text in
            if let opts = options {
                let response = try await session.respond(to: text, generating: ProxyDetection.self, options: opts)
                return response.content
            } else {
                let response = try await session.respond(to: text, generating: ProxyDetection.self)
                return response.content
            }
        }
    }

    func streamArchitecture(_ clause: Clause) -> AsyncThrowingStream<ArchitectureDetection.PartiallyGenerated, Error> {
        AsyncThrowingStream { continuation in
            Task {
                do {
                    _ = try await detectArchitecture(clause)
                    continuation.finish()
                } catch {
                    continuation.finish(throwing: error)
                }
            }
        }
    }

    private func makeSession() -> LanguageModelSession {
        LanguageModelSession(tools: [HistoricalBaselineTool()], instructions: academicFramingPrefix)
    }

    private func runWithRetry<T>(
        clause: Clause,
        body: (LanguageModelSession, String) async throws -> T
    ) async throws -> T {
        do {
            return try await body(makeSession(), clause.text)
        } catch let error as LanguageModelSession.GenerationError {
            switch error {
            case .exceededContextWindowSize(_):
                let truncated = String(clause.text.prefix(retryCharacterLimit))
                do {
                    return try await body(makeSession(), truncated)
                } catch let retryError as LanguageModelSession.GenerationError {
                    switch retryError {
                    case .exceededContextWindowSize(_):
                        throw Tier3Error.contextWindowExceeded
                    case .guardrailViolation(_), .refusal(_, _):
                        logSafetyGuardrail(for: clause.id)
                        throw Tier3Error.safetyGuardrail
                    default:
                        throw Tier3Error.sessionFailed(retryError)
                    }
                } catch {
                    throw Tier3Error.sessionFailed(error)
                }
            case .guardrailViolation(_), .refusal(_, _):
                logSafetyGuardrail(for: clause.id)
                throw Tier3Error.safetyGuardrail
            default:
                throw Tier3Error.sessionFailed(error)
            }
        } catch {
            throw Tier3Error.sessionFailed(error)
        }
    }

    private func streamWithRetry(
        clause: Clause,
        body: (LanguageModelSession, String) async throws -> Void
    ) async throws {
        do {
            try await body(makeSession(), clause.text)
        } catch let error as LanguageModelSession.GenerationError {
            switch error {
            case .exceededContextWindowSize(_):
                let truncated = String(clause.text.prefix(retryCharacterLimit))
                do {
                    try await body(makeSession(), truncated)
                } catch let retryError as LanguageModelSession.GenerationError {
                    switch retryError {
                    case .exceededContextWindowSize(_):
                        throw Tier3Error.contextWindowExceeded
                    case .guardrailViolation(_), .refusal(_, _):
                        logSafetyGuardrail(for: clause.id)
                        throw Tier3Error.safetyGuardrail
                    default:
                        throw Tier3Error.sessionFailed(retryError)
                    }
                } catch {
                    throw Tier3Error.sessionFailed(error)
                }
            case .guardrailViolation(_), .refusal(_, _):
                logSafetyGuardrail(for: clause.id)
                throw Tier3Error.safetyGuardrail
            default:
                throw Tier3Error.sessionFailed(error)
            }
        } catch {
            throw Tier3Error.sessionFailed(error)
        }
    }

    private func logSafetyGuardrail(for clauseID: UUID) {
        print("[Tier3] Safety guardrail triggered for clause \(clauseID)")
    }
}

#else

actor PolicyAnalysisSession {
    func classifyClause(_ clause: Clause, options: GenerationOptions? = nil) async throws -> ClauseClassification {
        throw Tier3Error.unavailable
    }

    func detectArchitecture(_ clause: Clause, options: GenerationOptions? = nil) async throws -> ArchitectureDetection {
        throw Tier3Error.unavailable
    }

    func detectProxy(_ clause: Clause, options: GenerationOptions? = nil) async throws -> ProxyDetection {
        throw Tier3Error.unavailable
    }

    func streamArchitecture(_ clause: Clause) -> AsyncThrowingStream<ArchitectureDetection.PartiallyGenerated, Error> {
        AsyncThrowingStream { $0.finish(throwing: Tier3Error.unavailable) }
    }
}

#endif
