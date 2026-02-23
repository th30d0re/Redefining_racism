//
//  Tier3Error.swift
//  decodingOppression
//
//  Errors for Tier3 (Foundation Models) classification path.
//

import Foundation

#if canImport(FoundationModels)

enum Tier3Error: Error {
    /// Foundation Models not available on this device/configuration.
    case unavailable
    /// Prompt was rejected by the safety system (caught internally, never surfaced to callers).
    case safetyGuardrail
    /// exceededContextWindowSize persisted even after condensed-text retry.
    case contextWindowExceeded
    /// Wraps any other LanguageModelSession error for internal logging.
    case sessionFailed(Error)
}



#endif
