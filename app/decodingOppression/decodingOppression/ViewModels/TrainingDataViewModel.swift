//
//  TrainingDataViewModel.swift
//  decodingOppression
//
//  macOS-only: state for TrainingDataView (T8).
//

#if os(macOS)

import Foundation
import AppKit
import UniformTypeIdentifiers

@Observable
@MainActor
final class TrainingDataViewModel {
    var clauses: [TrainingClause] = []
    var allClauses: [TrainingClause] = []
    var selectedClause: TrainingClause?
    var selectedClauseID: UUID?
    var editingClause: TrainingClause?
    var filterPolicy: String?
    var filterTargetGroup: TargetGroup?
    var hasUnsavedChanges: Bool = false
    var showUnsavedChangesAlert: Bool = false
    var pendingAction: (() -> Void)?

    var selectedClauseForTable: TrainingClause? {
        get { selectedClause }
        set {
            selectedClause = newValue
            selectedClauseID = newValue?.id
            if let clause = newValue {
                editingClause = copy(clause)
                hasUnsavedChanges = false
            } else {
                editingClause = nil
                hasUnsavedChanges = false
            }
        }
    }

    private func copy(_ c: TrainingClause) -> TrainingClause {
        TrainingClause(
            id: c.id,
            text: c.text,
            sourcePolicy: c.sourcePolicy,
            targetGroup: c.targetGroup,
            effectDirection: c.effectDirection,
            architectureScores: c.architectureScores,
            proxyVariables: c.proxyVariables,
            usesProxyVariables: c.usesProxyVariables
        )
    }

    func markEditingAsChanged() {
        hasUnsavedChanges = true
    }

    func load(store: TrainingDataStore) async throws {
        try await store.load()
        allClauses = await store.allClauses()
        applyFilters()
        hasUnsavedChanges = await store.hasUnsavedChanges
    }

    func applyFilters() {
        clauses = allClauses.filter { clause in
            let matchPolicy = filterPolicy == nil || filterPolicy!.isEmpty || clause.sourcePolicy == filterPolicy
            let matchGroup = filterTargetGroup == nil || clause.targetGroup == filterTargetGroup
            return matchPolicy && matchGroup
        }
    }

    func saveEditing(store: TrainingDataStore) async throws {
        guard let edited = editingClause else { return }
        await store.update(edited)
        try await store.save()
        if let i = allClauses.firstIndex(where: { $0.id == edited.id }) {
            allClauses[i] = edited
        }
        applyFilters()
        selectedClause = edited
        editingClause = copy(edited)
        hasUnsavedChanges = await store.hasUnsavedChanges
    }

    func addNew(store: TrainingDataStore) async {
        let newClause = TrainingClause(
            id: UUID(),
            text: "",
            sourcePolicy: "",
            targetGroup: .outgroup,
            effectDirection: .neutral,
            architectureScores: ArchitectureScores(aar: 0.5, se: 0.5, ij: 0.5, rsc: 0.5),
            proxyVariables: [],
            usesProxyVariables: false
        )
        await store.add(newClause)
        allClauses.append(newClause)
        applyFilters()
        selectedClause = newClause
        selectedClauseID = newClause.id
        editingClause = copy(newClause)
        hasUnsavedChanges = await store.hasUnsavedChanges
    }

    func delete(_ clause: TrainingClause, store: TrainingDataStore) async throws {
        await store.delete(id: clause.id)
        try await store.save()
        allClauses.removeAll { $0.id == clause.id }
        applyFilters()
        if selectedClauseID == clause.id {
            selectedClause = nil
            selectedClauseID = nil
            editingClause = nil
        }
        hasUnsavedChanges = await store.hasUnsavedChanges
    }

    func exportJSONL(store: TrainingDataStore) async throws {
        try await store.save()
        let panel = NSSavePanel()
        panel.allowedContentTypes = [.plainText]
        panel.nameFieldStringValue = "historical_clauses.jsonl"
        guard panel.runModal() == .OK, let url = panel.url else { return }
        let clauses = await store.allClauses()
        let encoder = JSONEncoder()
        let lines = try clauses.map { try String(data: encoder.encode($0), encoding: .utf8) ?? "" }
        try lines.joined(separator: "\n").write(to: url, atomically: true, encoding: .utf8)
    }

    func requestNavigation(action: @escaping () -> Void) {
        if hasUnsavedChanges {
            pendingAction = action
            showUnsavedChangesAlert = true
        } else {
            action()
        }
    }
}

#endif
