//
//  TrainingDataStore.swift
//  decodingOppression
//
//  macOS-only actor for loading/saving training clauses (T8).
//

#if os(macOS)

import Foundation

actor TrainingDataStore {
    static let shared = TrainingDataStore()

    private var clauses: [TrainingClause] = []
    private(set) var hasUnsavedChanges: Bool = false

    private let fileName = "historical_clauses.jsonl"
    private var appSupportURL: URL {
        let dir = FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask).first!
        let sub = dir.appendingPathComponent("decodingOppression", isDirectory: true)
        try? FileManager.default.createDirectory(at: sub, withIntermediateDirectories: true)
        return sub.appendingPathComponent(fileName, isDirectory: false)
    }

    private var bundledURL: URL? {
        Bundle.main.url(forResource: "historical_clauses", withExtension: "jsonl", subdirectory: "Data")
    }

    func load() async throws {
        let decoder = JSONDecoder()
        let data: Data
        let url: URL

        if FileManager.default.fileExists(atPath: appSupportURL.path) {
            url = appSupportURL
            data = try Data(contentsOf: url)
        } else if let bundled = bundledURL, FileManager.default.fileExists(atPath: bundled.path) {
            data = try Data(contentsOf: bundled)
            url = appSupportURL
        } else {
            clauses = []
            hasUnsavedChanges = false
            return
        }

        let lines = String(decoding: data, as: UTF8.self).split(separator: "\n").map(String.init)
        clauses = try lines.compactMap { line in
            guard !line.isEmpty, let d = line.data(using: .utf8) else { return nil }
            return try decoder.decode(TrainingClause.self, from: d)
        }
        hasUnsavedChanges = false
    }

    func save() async throws {
        let encoder = JSONEncoder()
        let lines = try clauses.map { clause in
            let d = try encoder.encode(clause)
            return String(data: d, encoding: .utf8) ?? ""
        }
        let content = lines.joined(separator: "\n")
        try content.write(to: appSupportURL, atomically: true, encoding: .utf8)
        hasUnsavedChanges = false
    }

    func allClauses() -> [TrainingClause] {
        clauses
    }

    func filtered(policy: String?, targetGroup: TargetGroup?) -> [TrainingClause] {
        var result = clauses
        if let p = policy, !p.isEmpty {
            result = result.filter { $0.sourcePolicy == p }
        }
        if let tg = targetGroup {
            result = result.filter { $0.targetGroup == tg }
        }
        return result
    }

    func add(_ clause: TrainingClause) {
        clauses.append(clause)
        hasUnsavedChanges = true
    }

    func update(_ clause: TrainingClause) {
        if let i = clauses.firstIndex(where: { $0.id == clause.id }) {
            clauses[i] = clause
            hasUnsavedChanges = true
        }
    }

    func delete(id: UUID) {
        clauses.removeAll { $0.id == id }
        hasUnsavedChanges = true
    }
}

#endif
