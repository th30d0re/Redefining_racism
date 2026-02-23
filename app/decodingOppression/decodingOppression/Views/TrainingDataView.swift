//
//  TrainingDataView.swift
//  decodingOppression
//
//  macOS-only: clause table + editor for training data (T8).
//

#if os(macOS)

import SwiftUI

struct TrainingDataView: View {
    @State var viewModel: TrainingDataViewModel
    @EnvironmentObject private var deps: AppDependencies

    private var selectionBinding: Binding<Set<UUID>> {
        Binding(
            get: { viewModel.selectedClauseID.map { [$0] } ?? [] },
            set: {
                viewModel.selectedClauseID = $0.first
                viewModel.selectedClause = $0.first.flatMap { id in viewModel.clauses.first { $0.id == id } }
                viewModel.editingClause = viewModel.selectedClause.map { copyClause($0) }
                viewModel.hasUnsavedChanges = false
            }
        )
    }

    var body: some View {
        HSplitView {
            leftPanel
            rightPanel
        }
        .alert("Unsaved Changes", isPresented: $viewModel.showUnsavedChangesAlert) {
            Button("Discard", role: .destructive) {
                viewModel.pendingAction?()
                viewModel.pendingAction = nil
            }
            Button("Cancel", role: .cancel) {
                viewModel.pendingAction = nil
            }
        } message: {
            Text("You have unsaved changes. Discard them?")
        }
        .task {
            try? await viewModel.load(store: deps.trainingDataStore)
        }
        .onChange(of: viewModel.selectedClauseID) { _, newId in
            if let id = newId, let clause = viewModel.clauses.first(where: { $0.id == id }) {
                viewModel.editingClause = copyClause(clause)
            } else {
                viewModel.editingClause = nil
            }
        }
    }

    private var leftPanel: some View {
        VStack(alignment: .leading, spacing: 0) {
            toolbar
            Table(viewModel.clauses, selection: selectionBinding) {
                TableColumn("Clause Text") { clause in
                    Text(String(clause.text.prefix(80)) + (clause.text.count > 80 ? "…" : ""))
                        .lineLimit(1)
                }
                TableColumn("Source Policy") { clause in
                    Text(clause.sourcePolicy)
                }
                TableColumn("Target Group") { clause in
                    Text(clause.targetGroup.rawValue)
                }
                TableColumn("Effect Direction") { clause in
                    Text(clause.effectDirection.rawValue)
                }
            }
        }
        .frame(minWidth: 400)
    }

    private var toolbar: some View {
        HStack(spacing: 12) {
            Picker("Policy", selection: $viewModel.filterPolicy) {
                Text("All").tag(Optional<String>.none)
                ForEach(Array(Set(viewModel.allClauses.map(\.sourcePolicy))).filter { !$0.isEmpty }.sorted(), id: \.self) { p in
                    Text(p).tag(Optional(p))
                }
            }
            .frame(width: 160)
            .onChange(of: viewModel.filterPolicy) { _, _ in viewModel.applyFilters() }
            Picker("Target Group", selection: $viewModel.filterTargetGroup) {
                Text("All").tag(Optional<TargetGroup>.none)
                ForEach([TargetGroup.outgroup, .ingroupNonElite, .elite, .multiple], id: \.self) { tg in
                    Text(tg.rawValue).tag(Optional(tg))
                }
            }
            .frame(width: 140)
            .onChange(of: viewModel.filterTargetGroup) { _, _ in viewModel.applyFilters() }
            Button("Add Clause") {
                Task { await viewModel.addNew(store: deps.trainingDataStore) }
            }
            Button("Export JSONL") {
                Task { try? await viewModel.exportJSONL(store: deps.trainingDataStore) }
            }
            .overlay(alignment: .topTrailing) {
                Circle()
                    .fill(Color.orange)
                    .frame(width: 8, height: 8)
                    .opacity(TrainingDataViewStyle.unsavedDotOpacity(hasChanges: viewModel.hasUnsavedChanges))
                    .offset(x: 4, y: -4)
            }
            Spacer()
        }
        .padding(8)
    }

    @ViewBuilder
    private var rightPanel: some View {
        if let editing = viewModel.editingClause {
            List {
                SwiftUI.Section("Clause") {
                    TextEditor(text: Binding(
                        get: { editing.text },
                        set: { var e = editing; e.text = $0; viewModel.editingClause = e; viewModel.markEditingAsChanged() }
                    ))
                    .frame(minHeight: 80)
                }
                SwiftUI.Section("Classification") {
                    Picker("Target Group", selection: Binding(
                        get: { editing.targetGroup },
                        set: { var e = editing; e.targetGroup = $0; viewModel.editingClause = e; viewModel.markEditingAsChanged() }
                    )) {
                        ForEach([TargetGroup.outgroup, .ingroupNonElite, .elite, .multiple], id: \.self) { tg in
                            Text(tg.rawValue).tag(tg)
                        }
                    }
                    Picker("Effect Direction", selection: Binding(
                        get: { editing.effectDirection },
                        set: { var e = editing; e.effectDirection = $0; viewModel.editingClause = e; viewModel.markEditingAsChanged() }
                    )) {
                        ForEach([EffectDirection.burden, .benefit, .neutral, .mixed], id: \.self) { ed in
                            Text(ed.rawValue).tag(ed)
                        }
                    }
                }
                SwiftUI.Section("Architecture scores (0–1)") {
                    HStack {
                        Text("AAR")
                        Slider(value: Binding(get: { editing.architectureScores.aar }, set: { var e = editing; e.architectureScores.aar = $0; viewModel.editingClause = e; viewModel.markEditingAsChanged() }), in: 0...1)
                        Text(TrainingDataViewStyle.sliderLabel(editing.architectureScores.aar))
                    }
                    HStack {
                        Text("SE")
                        Slider(value: Binding(get: { editing.architectureScores.se }, set: { var e = editing; e.architectureScores.se = $0; viewModel.editingClause = e; viewModel.markEditingAsChanged() }), in: 0...1)
                        Text(TrainingDataViewStyle.sliderLabel(editing.architectureScores.se))
                    }
                    HStack {
                        Text("IJ")
                        Slider(value: Binding(get: { editing.architectureScores.ij }, set: { var e = editing; e.architectureScores.ij = $0; viewModel.editingClause = e; viewModel.markEditingAsChanged() }), in: 0...1)
                        Text(TrainingDataViewStyle.sliderLabel(editing.architectureScores.ij))
                    }
                    HStack {
                        Text("RSC")
                        Slider(value: Binding(get: { editing.architectureScores.rsc }, set: { var e = editing; e.architectureScores.rsc = $0; viewModel.editingClause = e; viewModel.markEditingAsChanged() }), in: 0...1)
                        Text(TrainingDataViewStyle.sliderLabel(editing.architectureScores.rsc))
                    }
                }
                SwiftUI.Section("Proxy") {
                    Toggle("Uses Proxy Variables", isOn: Binding(
                        get: { editing.usesProxyVariables },
                        set: { var e = editing; e.usesProxyVariables = $0; viewModel.editingClause = e; viewModel.markEditingAsChanged() }
                    ))
                    TextField("Proxy terms (comma-separated)", text: Binding(
                        get: { editing.proxyVariables.joined(separator: ", ") },
                        set: { var e = editing; e.proxyVariables = $0.split(separator: ",").map { String($0.trimmingCharacters(in: .whitespaces)) }; viewModel.editingClause = e; viewModel.markEditingAsChanged() }
                    ))
                }
                HStack {
                    Button("Save") {
                        Task { try? await viewModel.saveEditing(store: deps.trainingDataStore) }
                    }
                    if let clause = viewModel.selectedClause {
                        Button("Delete", role: .destructive) {
                            Task { try? await viewModel.delete(clause, store: deps.trainingDataStore) }
                        }
                    }
                }
            }
            .frame(minWidth: 320)
        } else {
            ContentUnavailableView(
                "Select a Clause",
                systemImage: "doc.text",
                description: Text("Choose a clause from the table to edit.")
            )
            .frame(minWidth: 320)
        }
    }

    private func copyClause(_ c: TrainingClause) -> TrainingClause {
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
}

#endif
