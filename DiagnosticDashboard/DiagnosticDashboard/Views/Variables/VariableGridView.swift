import SwiftUI

struct VariableGridView: View {
    let era: Era

    private let columns = Array(repeating: GridItem(.flexible(), spacing: 6), count: 5)

    var body: some View {
        HUDFrame(title: "Variable State") {
            LazyVGrid(columns: columns, spacing: 6) {
                ForEach(SystemVariable.gridVariables) { variable in
                    VariableChipView(
                        variable: variable,
                        state: variableState(for: variable)
                    )
                    .animation(.easeInOut(duration: 0.4), value: variableState(for: variable) == .deployed)
                }
            }

            // Legend
            HStack(spacing: 12) {
                legendItem(color: Theme.textDim.opacity(0.4), label: "Inactive")
                legendItem(color: Theme.accentCyan.opacity(0.7), label: "Loaded")
                legendItem(color: Theme.accentGreen, label: "Deployed")
            }
            .padding(.top, 8)
        }
    }

    private func variableState(for variable: SystemVariable) -> VariableState {
        // Map F_enforce_proto to F_enforce for display
        let deployed = era.variablesDeployed
        let loaded = era.variablesLoaded

        if deployed.contains(variable) { return .deployed }
        // Check proto mapping
        if variable == .F_enforce && deployed.contains(.F_enforce_proto) { return .deployed }
        if loaded.contains(variable) { return .loaded }
        // Check if deployed in any previous era
        let currentIndex = TimelineDataStore.eras.firstIndex(where: { $0.id == era.id }) ?? 0
        for i in 0..<currentIndex {
            let prev = TimelineDataStore.eras[i]
            if prev.variablesDeployed.contains(variable) { return .loaded }
            if variable == .F_enforce && prev.variablesDeployed.contains(.F_enforce_proto) { return .loaded }
        }
        return .hidden
    }

    private func legendItem(color: Color, label: String) -> some View {
        HStack(spacing: 4) {
            RoundedRectangle(cornerRadius: 2)
                .fill(color)
                .frame(width: 8, height: 8)
            Text(label)
                .font(.system(size: 8, design: .monospaced))
                .foregroundStyle(Theme.textDim)
        }
    }
}
