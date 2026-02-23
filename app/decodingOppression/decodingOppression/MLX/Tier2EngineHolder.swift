//
//  Tier2EngineHolder.swift
//  decodingOppression
//
//  Deprecated: use Tier2Engine directly via AppDependencies.
//

import Combine
import Foundation

@available(*, deprecated, message: "Use Tier2Engine directly.")
@MainActor
final class Tier2EngineHolder: ObservableObject {
    let objectWillChange = ObservableObjectPublisher()
    private let engine: Tier2Engine

    init(downloadManager: ModelDownloadManager) {
        self.engine = Tier2Engine(downloadManager: downloadManager)
    }

    func classify(clause: Clause) async throws -> TierClassification? {
        try await engine.classify(clause: clause)
    }

    func similarity(clause: String, taxonomyTerm: String) async throws -> Double {
        try await engine.similarity(clause: clause, taxonomyTerm: taxonomyTerm)
    }

    func embed(_ text: String) async throws -> [Float] {
        try await engine.embed(text)
    }
}
