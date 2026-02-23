//
//  ValidationView.swift
//  decodingOppression
//
//  macOS-only: historical policy validation dashboard (T8).
//

#if os(macOS)

import SwiftUI

struct ValidationView: View {
    @State var viewModel: ValidationViewModel
    @EnvironmentObject private var deps: AppDependencies
    @Environment(\.accessibilityDifferentiateWithoutColor) private var differentiateWithoutColor

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            headerRow
            if let summary = viewModel.summaryText {
                Text(summary)
                    .font(.subheadline)
                    .padding(8)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(ValidationViewStyle.bannerBackground(allPassed: viewModel.results.allSatisfy(\.passed)), in: RoundedRectangle(cornerRadius: 8))
            }
            testCards
        }
        .padding()
    }

    private var headerRow: some View {
        HStack {
            VStack(alignment: .leading, spacing: 4) {
                Text("Validation")
                    .font(.title2.weight(.semibold))
                Text("Compare scorer output to expected COI for historical policies.")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
            Spacer()
            Button("Run All Tests") {
                Task {
                    await viewModel.runAll(runner: deps.validationRunner, scorer: DefaultPolicyScorer())
                }
            }
        }
    }

    private var testCards: some View {
        ForEach(HistoricalPolicies.chain, id: \.name) { policy in
            testCard(policy: policy)
        }
    }

    private func testCard(policy: HistoricalPolicy) -> some View {
        let result = viewModel.results.first { $0.policyName == policy.name }
        let passed = result?.passed ?? false
        let (color, icon) = result.map { ValidationViewStyle.resultColor(passed: $0.passed, differentiateWithoutColor: differentiateWithoutColor) } ?? (Color.primary, "circle")
        let resultDescription = result.map { "Expected \($0.expectedCOI.formatted(.percent.precision(.fractionLength(2)))), actual \($0.actualCOI.formatted(.percent.precision(.fractionLength(2)))), delta \($0.delta.formatted(.number.precision(.fractionLength(2))))" } ?? "Not run"

        return HStack(alignment: .top, spacing: 16) {
            VStack(alignment: .leading, spacing: 4) {
                Text(policy.name)
                    .font(.headline)
                Text("\(policy.year) · expected COI \(policy.expectedCOI.formatted(.percent.precision(.fractionLength(2))))")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
            Spacer()
            if viewModel.runningPolicyNames.contains(policy.name) {
                ProgressView()
            } else if let r = result {
                VStack(alignment: .trailing, spacing: 4) {
                    Label(r.passed ? "Passed" : "Failed", systemImage: icon)
                        .foregroundStyle(color)
                    Text("Actual: \(r.actualCOI.formatted(.number.precision(.fractionLength(2))))")
                    Text("Delta: \(r.delta.formatted(.number.precision(.fractionLength(2))))")
                        .font(.caption)
                }
            }
            Button("Run") {
                Task {
                    await viewModel.run(policy: policy, runner: deps.validationRunner, scorer: DefaultPolicyScorer())
                }
            }
        }
        .padding()
        .overlay(
            RoundedRectangle(cornerRadius: 10)
                .stroke(ValidationViewStyle.cardBorderColor(passed: result?.passed ?? true), lineWidth: 2)
        )
        .accessibilityLabel("\(policy.name), \(policy.year)")
        .accessibilityValue(resultDescription)
    }
}

#endif
