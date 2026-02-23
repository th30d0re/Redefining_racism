//
//  PolicyHistoryView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Observation
import SwiftData
import SwiftUI
import UniformTypeIdentifiers

struct PolicyHistoryView: View {
    @Environment(\.modelContext) private var modelContext
    @EnvironmentObject private var modelDownloadManager: ModelDownloadManager
    @Environment(\.accessibilityDifferentiateWithoutColor) private var differentiateWithoutColor
    @AppStorage("hasCompletedOnboarding") private var hasCompletedOnboarding: Bool = false
    @Query(sort: \PolicyAnalysis.dateAnalyzed, order: .reverse) private var analyses: [PolicyAnalysis]
    @State private var viewModel: PolicyHistoryViewModel
    @State private var analysisSelection: PDFSelection?

    init(viewModel: PolicyHistoryViewModel) {
        _viewModel = State(initialValue: viewModel)
    }

    var body: some View {
        @Bindable var viewModel = viewModel

        VStack(spacing: 0) {
            if shouldShowDownloadBanner {
                downloadBanner
                    .padding(.horizontal)
                    .padding(.top, 8)
            }

            if analyses.isEmpty {
                ContentUnavailableView(
                    "No Analyses",
                    systemImage: "doc.text.magnifyingglass",
                    description: Text("Analyze your first policy")
                )
            } else {
                List {
                    ForEach(analyses) { analysis in
                        analysisRow(analysis)
                    }
                }
            }
        }
        .navigationTitle("Analyses")
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                Button {
                    viewModel.isShowingFilePicker = true
                } label: {
                    Image(systemName: "plus")
                }
                .accessibilityLabel("Import PDF")
            }
        }
        .fileImporter(
            isPresented: $viewModel.isShowingFilePicker,
            allowedContentTypes: [.pdf]
        ) { result in
            switch result {
            case .success(let url):
                analysisSelection = PDFSelection(url: url)
            case .failure:
                break
            }
        }
        .navigationDestination(item: $analysisSelection) { selection in
            AnalysisView(pdfURL: selection.url)
        }
    }

    private var shouldShowDownloadBanner: Bool {
        guard hasCompletedOnboarding else { return false }
        switch modelDownloadManager.state {
        case .downloading, .unavailable:
            return true
        case .available(_):
            return false
        }
    }

    @ViewBuilder
    private var downloadBanner: some View {
        switch modelDownloadManager.state {
        case .downloading(let progress):
            HStack(spacing: 12) {
                ProgressView(value: progress)
                VStack(alignment: .leading, spacing: 2) {
                    Text("Downloading Tier2 model")
                        .font(.subheadline)
                    Text("\(Int(progress * 100))% complete")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                Spacer()
            }
            .padding(12)
            .background(.thinMaterial, in: RoundedRectangle(cornerRadius: 12))
        case .unavailable:
            HStack(spacing: 12) {
                Image(systemName: "exclamationmark.triangle")
                    .foregroundStyle(.orange)
                Text("Tier2 model unavailable. Analysis will use Tier1.")
                    .font(.subheadline)
                Spacer()
            }
            .padding(12)
            .background(.thinMaterial, in: RoundedRectangle(cornerRadius: 12))
        case .available(_):
            EmptyView()
        }
    }

    @ViewBuilder
    private func analysisRow(_ analysis: PolicyAnalysis) -> some View {
        let badge = PolicyHistoryViewStyle.coiBadgeColor(
            analysis.scoreResult.coi,
            differentiateWithoutColor: differentiateWithoutColor
        )
        let subtitle = "\(analysis.dateAnalyzed.formatted(date: .abbreviated, time: .shortened)) - \(analysis.clauses.count) clauses"
        let scoreText = analysis.scoreResult.coi.formatted(.number.precision(.fractionLength(2)))

        let rowContent = HStack(alignment: .top, spacing: 12) {
            VStack(alignment: .leading, spacing: 6) {
                Text(analysis.policyName)
                    .font(.headline)
                Text(subtitle)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
            Spacer()
            Label(scoreText, systemImage: badge.1)
                .font(.caption.weight(.semibold))
                .foregroundStyle(badge.0)
                .padding(.vertical, 4)
                .padding(.horizontal, 8)
                .background(badge.0.opacity(0.12), in: Capsule())
                .accessibilityLabel("Composite Oppression Index")
                .accessibilityValue(scoreText)
        }
        .contentShape(Rectangle())

        #if os(iOS)
        NavigationLink {
            ScoreCardView(analysis: analysis)
        } label: {
            rowContent
        }
        .swipeActions {
            Button(role: .destructive) {
                viewModel.delete(analysis, context: modelContext)
            } label: {
                Label("Delete", systemImage: "trash")
            }
        }
        #else
        Button {
            viewModel.selectedAnalysis = analysis
        } label: {
            rowContent
        }
        .buttonStyle(.plain)
        .contextMenu {
            Button("Delete", role: .destructive) {
                viewModel.delete(analysis, context: modelContext)
            }
        }
        .listRowBackground(
            viewModel.selectedAnalysis?.id == analysis.id ? Color.accentColor.opacity(0.15) : Color.clear
        )
        #endif
    }
}

private struct PDFSelection: Identifiable, Hashable {
    let id = UUID()
    let url: URL
}

#Preview {
    NavigationStack {
        PolicyHistoryView(viewModel: PolicyHistoryViewModel())
            .environmentObject(ModelDownloadManager.shared)
    }
}
