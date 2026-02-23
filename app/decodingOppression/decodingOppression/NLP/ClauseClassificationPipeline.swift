//
//  ClauseClassificationPipeline.swift
//  decodingOppression
//
//  Routes clause classification through Tier2 when available, falling back to Tier1.
//

import Foundation

actor ClauseClassificationPipeline {
    private let tier1Engine: Tier1Engine
    private let tier2Engine: Tier2Engine

    init(tier2Engine: Tier2Engine) throws {
        self.tier1Engine = try Tier1Engine()
        self.tier2Engine = tier2Engine
    }

    func extractAndPreprocess(pdf url: URL) async throws -> [Clause] {
        try await tier1Engine.extractAndPreprocess(pdf: url)
    }

    func classify(clause: Clause) async -> TierClassification {
        if let classification = (try? await tier2Engine.classify(clause: clause)) ?? nil {
            return classification
        }
        return await tier1Engine.classify(clause: clause)
    }

    func similarity(clause: String, taxonomyTerm: String) async throws -> Double {
        try await tier2Engine.similarity(clause: clause, taxonomyTerm: taxonomyTerm)
    }

    func embed(_ text: String) async throws -> [Float] {
        try await tier2Engine.embed(text)
    }
}
