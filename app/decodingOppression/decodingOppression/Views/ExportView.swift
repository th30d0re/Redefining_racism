//
//  ExportView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct ExportView: View {
    let analysis: PolicyAnalysis

    @State private var viewModel = ExportViewModel()
    @State private var lastFormat: ExportFormat?

    var body: some View {
        VStack(alignment: .leading, spacing: ExportViewStyle.buttonSpacing) {
            Text("Export")
                .font(.title2.weight(.semibold))

            Button(ExportFormat.pdf.label) {
                lastFormat = .pdf
                viewModel.export(analysis: analysis, format: .pdf)
            }
            .buttonStyle(.borderedProminent)
            .accessibilityLabel("Export PDF report")
            .accessibilityHint("Creates a PDF report of the analysis")

            Button(ExportFormat.json.label) {
                lastFormat = .json
                viewModel.export(analysis: analysis, format: .json)
            }
            .buttonStyle(.bordered)
            .accessibilityLabel("Export JSON data")
            .accessibilityHint("Creates a JSON export with full analysis data")

            if viewModel.isGenerating {
                ProgressView("Generating...")
            }

            if let exportedItem = viewModel.exportedItem {
                ShareLink(item: exportedItem.url) {
                    Label("Share", systemImage: "square.and.arrow.up")
                }
            }

            if let error = viewModel.error {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Export failed")
                        .font(.headline)
                    Text(error.localizedDescription)
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    Button("Try Again") {
                        if let format = lastFormat {
                            viewModel.export(analysis: analysis, format: format)
                        }
                    }
                    .buttonStyle(.bordered)
                }
                .padding(12)
                .background(.thinMaterial, in: RoundedRectangle(cornerRadius: 12))
            }

            Spacer(minLength: 0)
        }
        .padding(ExportViewStyle.panelPadding)
    }
}

#Preview {
    ExportView(analysis: PolicyAnalysis(policyName: "Sample", sourceFilename: "sample.pdf", dateAnalyzed: .now))
}
