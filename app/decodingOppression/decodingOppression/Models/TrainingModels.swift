//
//  TrainingModels.swift
//  decodingOppression
//
//  macOS-only training and validation data types (T8).
//

#if os(macOS)

import Foundation

// MARK: - LoRA configuration

struct LoRAConfig: Codable, Sendable {
    var epochs: Int
    var learningRate: Double
    var loraRank: Int
    var alpha: Int

    static let `default` = LoRAConfig(
        epochs: 3,
        learningRate: 0.0001,
        loraRank: 8,
        alpha: 16
    )
}

// MARK: - Training clause (one line in historical_clauses.jsonl)

struct TrainingClause: Codable, Sendable, Identifiable {
    var id: UUID
    var text: String
    var sourcePolicy: String
    var targetGroup: TargetGroup
    var effectDirection: EffectDirection
    var architectureScores: ArchitectureScores
    var proxyVariables: [String]
    var usesProxyVariables: Bool
}

// MARK: - Validation result (one historical policy)

struct ValidationResult: Codable, Sendable {
    var policyName: String
    var year: Int
    var expectedCOI: Double
    var actualCOI: Double
    var delta: Double
    var passed: Bool

    init(policyName: String, year: Int, expectedCOI: Double, actualCOI: Double) {
        self.policyName = policyName
        self.year = year
        self.expectedCOI = expectedCOI
        self.actualCOI = actualCOI
        self.delta = actualCOI - expectedCOI
        self.passed = abs(delta) <= 0.10
    }
}

// MARK: - Adapter metadata (saved alongside LoRA adapter)

struct LoRAAdapterMetadata: Codable, Sendable {
    var id: UUID
    var name: String
    var timestamp: Date
    var trainingConfig: LoRAConfig
    var validationResults: [ValidationResult]?
    var isActive: Bool
}

// MARK: - Training progress (streamed to UI)

enum TrainingProgress: Sendable {
    case epoch(current: Int, total: Int, trainLoss: Double, valLoss: Double)
    case complete(adapterPath: URL, metadata: LoRAAdapterMetadata)
    case failed(Error)
}

#endif
