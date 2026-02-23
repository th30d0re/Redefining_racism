//
//  AnalysisView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftData
import SwiftUI

struct AnalysisView: View {
    let pdfURL: URL

    @EnvironmentObject private var deps: AppDependencies
    @EnvironmentObject private var modelDownloadManager: ModelDownloadManager
    @Environment(\.modelContext) private var modelContext
    @Environment(\.dismiss) private var dismiss
    @Environment(\.accessibilityDifferentiateWithoutColor) private var differentiateWithoutColor
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @AppStorage("hasCompletedOnboarding") private var hasCompletedOnboarding: Bool = false
    @State private var viewModel = AnalysisViewModel()
    @State private var animatedCOI: Double = 0
    @State private var shouldNavigate: Bool = false
    @AccessibilityFocusState private var gaugeFocused: Bool

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                if shouldShowDownloadBanner {
                    downloadBanner
                }

                Text(viewModel.stage)
                    .font(.headline)

                coiGauge

                clauseProgress

                scoreRows

                if viewModel.isComplete {
                    Button("View Full Results") {
                        shouldNavigate = true
                    }
                    .buttonStyle(.borderedProminent)
                }

                if let error = viewModel.error {
                    errorBanner(error)
                }
            }
            .padding(24)
        }
        .navigationTitle(pdfURL.deletingPathExtension().lastPathComponent)
        .navigationDestination(isPresented: $shouldNavigate) {
            if let analysis = viewModel.finalAnalysis {
                ScoreCardView(analysis: analysis)
            }
        }
        .onAppear {
            viewModel.startAnalysis(pdfURL: pdfURL, deps: deps, context: modelContext)
        }
        .onChange(of: viewModel.coiValue) { _, newValue in
            let clamped = max(0, min(1, newValue))
            if let animation = AnalysisViewStyle.gaugeAnimation(reduceMotion: reduceMotion) {
                withAnimation(animation) {
                    animatedCOI = clamped
                }
            } else {
                animatedCOI = clamped
            }
        }
        .onChange(of: viewModel.isComplete) { _, isComplete in
            if isComplete {
                gaugeFocused = true
                Task {
                    try? await Task.sleep(for: .seconds(1))
                    shouldNavigate = true
                }
            }
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

    private var coiGauge: some View {
        let badge = AnalysisViewStyle.scoreColor(viewModel.coiValue, differentiateWithoutColor: differentiateWithoutColor)
        let scoreText = viewModel.coiValue.formatted(.number.precision(.fractionLength(2)))

        return VStack(alignment: .leading, spacing: 12) {
            ZStack {
                Circle()
                    .stroke(.secondary.opacity(0.2), lineWidth: 16)
                Circle()
                    .trim(from: 0, to: CGFloat(animatedCOI))
                    .stroke(badge.0, style: StrokeStyle(lineWidth: 16, lineCap: .round))
                    .rotationEffect(.degrees(-90))
                VStack(spacing: 6) {
                    Text(scoreText)
                        .font(.system(size: 34, weight: .bold, design: .rounded))
                        .foregroundStyle(badge.0)
                    Text("COI")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            }
            .frame(width: 180, height: 180)
            .accessibilityFocused($gaugeFocused)
        }
    }

    private var clauseProgress: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Clauses \(viewModel.clauseIndex) of \(max(viewModel.totalClauses, 1))")
                .font(.subheadline)
            ProgressView(value: Double(viewModel.clauseIndex) / Double(max(viewModel.totalClauses, 1)))
        }
    }

    private var scoreRows: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text(viewModel.isComplete ? "Final Scores" : "Preliminary Scores")
                .font(.headline)

            ScoreRow(label: "DIS", value: viewModel.partialScores.dis, isReady: viewModel.clauseIndex > 0, isComplete: viewModel.isComplete)
            ScoreRow(label: "ADS", value: viewModel.partialScores.ads, isReady: viewModel.clauseIndex > 0, isComplete: viewModel.isComplete)
            ScoreRow(label: "EIS", value: viewModel.partialScores.eis, isReady: viewModel.clauseIndex > 0, isComplete: viewModel.isComplete)
            ScoreRow(label: "CIS", value: viewModel.partialScores.cis, isReady: viewModel.clauseIndex > 0, isComplete: viewModel.isComplete)
            ScoreRow(label: "OES", value: viewModel.partialScores.oes, isReady: viewModel.clauseIndex > 0, isComplete: viewModel.isComplete)
        }
    }

    @ViewBuilder
    private func errorBanner(_ error: Error) -> some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Analysis failed")
                .font(.headline)
            Text(error.localizedDescription)
                .font(.caption)
                .foregroundStyle(.secondary)
            Button("Go Back") {
                dismiss()
            }
            .buttonStyle(.bordered)
        }
        .padding(12)
        .background(.thinMaterial, in: RoundedRectangle(cornerRadius: 12))
    }
}

private struct ScoreRow: View {
    let label: String
    let value: Double
    let isReady: Bool
    let isComplete: Bool

    var body: some View {
        HStack {
            Text(label)
                .font(.subheadline.weight(.semibold))
            Spacer()
            if isReady {
                Text(value.formatted(.number.precision(.fractionLength(2))))
                    .font(.subheadline.monospacedDigit())
            } else {
                Text("-")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
            if !isComplete {
                Text("Preliminary")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
        }
    }
}

#Preview {
    NavigationStack {
        AnalysisView(pdfURL: URL(fileURLWithPath: "/tmp/sample.pdf"))
            .environmentObject(AppDependencies.shared)
            .environmentObject(ModelDownloadManager.shared)
    }
}
