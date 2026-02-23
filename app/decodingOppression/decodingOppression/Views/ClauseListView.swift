//
//  ClauseListView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct ClauseListView: View {
    @State private var viewModel: ClauseListViewModel
    @Namespace private var rotorNamespace

    init(analysis: PolicyAnalysis) {
        _viewModel = State(initialValue: ClauseListViewModel(analysis: analysis))
    }

    var body: some View {
        List {
            SwiftUI.Section("Oppressive Clauses") {
                if viewModel.oppressiveClauses.isEmpty {
                    Text("None identified")
                        .foregroundStyle(.secondary)
                } else {
                    ForEach(viewModel.oppressiveClauses) { item in
                        ClauseRow(item: item)
                            .accessibilityRotorEntry(id: item.id, in: rotorNamespace)
                    }
                }
            }

            SwiftUI.Section("Liberatory Clauses") {
                if viewModel.liberatoryClauses.isEmpty {
                    Text("None identified")
                        .foregroundStyle(.secondary)
                } else {
                    ForEach(viewModel.liberatoryClauses) { item in
                        ClauseRow(item: item)
                            .accessibilityRotorEntry(id: item.id, in: rotorNamespace)
                    }
                }
            }
        }
        .navigationTitle("Clauses")
        .accessibilityRotor("Oppressive Clauses") {
            ForEach(viewModel.oppressiveClauses) { item in
                AccessibilityRotorEntry(Text(item.clause.text), id: item.id, in: rotorNamespace)
            }
        }
        .accessibilityRotor("Liberatory Clauses") {
            ForEach(viewModel.liberatoryClauses) { item in
                AccessibilityRotorEntry(Text(item.clause.text), id: item.id, in: rotorNamespace)
            }
        }
    }
}

private struct ClauseRow: View {
    let item: ClauseScore

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(item.clause.text)
                .font(.subheadline)
            Text("Score \(item.score.formatted(.number.precision(.fractionLength(2))))")
                .font(.caption)
                .foregroundStyle(ClauseListViewStyle.scoreColor(item.score))
        }
    }
}

#Preview {
    ClauseListView(analysis: PolicyAnalysis(policyName: "Sample", sourceFilename: "sample.pdf", dateAnalyzed: .now))
}
