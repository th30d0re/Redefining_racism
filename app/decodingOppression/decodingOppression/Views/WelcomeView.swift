//
//  WelcomeView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct WelcomeView: View {
    @EnvironmentObject private var deps: AppDependencies
    @EnvironmentObject private var modelDownloadManager: ModelDownloadManager
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @Environment(\.dynamicTypeSize) private var dynamicTypeSize
    @Binding var hasCompletedOnboarding: Bool
    @State private var viewModel = WelcomeViewModel()
    @AccessibilityFocusState private var progressFocused: Bool

    var body: some View {
        let style = WelcomeViewStyle(reduceMotion: reduceMotion, dynamicTypeSize: dynamicTypeSize)

        ScrollView {
            VStack(spacing: 24) {
                VStack(spacing: 12) {
                    Image(systemName: "doc.text.magnifyingglass")
                        .font(.system(size: 64, weight: .semibold))
                        .foregroundStyle(.tint)
                    Text("Decoding Oppression")
                        .font(.title.bold())
                    Text("Analyze policies for structural bias and track historical impact.")
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                        .multilineTextAlignment(.center)
                }
                .padding(.top, 32)

                Button {
                    viewModel.getStarted(deps: deps, hasCompletedOnboarding: &hasCompletedOnboarding)
                    progressFocused = true
                } label: {
                    Text("Get Started")
                        .frame(maxWidth: .infinity)
                }
                .buttonStyle(.borderedProminent)
                .accessibilityHint("Starts the model download and opens the analysis list")

                downloadProgressSection(animation: WelcomeViewStyle.progressAnimation(reduceMotion: style.reduceMotion))

                if modelDownloadManager.downloadError != nil {
                    Button("Retry Download") {
                        Task { await deps.startTier2Download() }
                    }
                    .buttonStyle(.bordered)
                }
            }
            .padding(.horizontal, 24)
            .padding(.bottom, 32)
        }
    }

    @ViewBuilder
    private func downloadProgressSection(animation: Animation?) -> some View {
        switch modelDownloadManager.state {
        case .downloading(let progress):
            VStack(spacing: 12) {
                ProgressView(value: progress)
                    .accessibilityFocused($progressFocused)
                Text("Downloading model... \(Int(progress * 100))%")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                Button("Pause") {
                    modelDownloadManager.cancelDownload()
                }
                .buttonStyle(.bordered)
            }
            .animation(animation, value: progress)
        case .available(_):
            Label("Model ready", systemImage: "checkmark.circle.fill")
                .foregroundStyle(.green)
        case .unavailable:
            EmptyView()
        }
    }
}

#Preview {
    WelcomeView(hasCompletedOnboarding: .constant(false))
        .environmentObject(AppDependencies.shared)
        .environmentObject(ModelDownloadManager.shared)
}
