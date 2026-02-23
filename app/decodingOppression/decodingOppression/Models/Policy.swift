//
//  Policy.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/19/26.
//

import Foundation
#if canImport(FoundationModels)
import FoundationModels
#endif

// MARK: - Section type and targeting

enum SectionType: String, Codable, CaseIterable, Sendable {
    case title
    case definitions
    case operativeClauses
    case penalties
    case exceptions
}

#if canImport(FoundationModels)
@Generable
#endif
enum TargetGroup: String, Codable, CaseIterable, Sendable {
    case outgroup
    case ingroupNonElite
    case elite
    case multiple
}

#if canImport(FoundationModels)
@Generable
#endif
enum EffectDirection: String, Codable, CaseIterable, Sendable {
    case burden
    case benefit
    case neutral
    case mixed
}

enum MLTier: String, Codable, Sendable {
    case tier1
    case tier2
    case tier3
}

// MARK: - Policy value types

struct Section: Identifiable, Codable {
    var id: UUID
    var type: SectionType
    var rawText: String
}

struct Clause: Identifiable, Codable {
    var id: UUID
    var text: String
    var sectionType: SectionType
    var targetGroup: TargetGroup?
    var effectDirection: EffectDirection?
}

struct Policy: Identifiable, Codable {
    var id: UUID
    var name: String
    var year: Int
    var sections: [Section]
    var clauses: [Clause]
}
