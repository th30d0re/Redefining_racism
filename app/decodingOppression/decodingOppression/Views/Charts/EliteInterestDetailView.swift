//
//  EliteInterestDetailView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct EliteInterestDetailView: View {
    @State private var viewModel: EliteInterestDetailViewModel

    init(analysis: PolicyAnalysis) {
        _viewModel = State(initialValue: EliteInterestDetailViewModel(analysis: analysis))
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("Elite Interest Detail")
                .font(.title2.weight(.semibold))
                .accessibilityHeading(.h2)

            MetricRow(title: "Elite clause share", value: viewModel.eliteClauseRate)
            MetricRow(title: "Elite benefit rate", value: viewModel.eliteBenefitRate)
            MetricRow(title: "Elite burden rate", value: viewModel.eliteBurdenRate)
            MetricRow(
                title: "Average confidence",
                value: viewModel.eliteAverageConfidence,
                formatter: { $0.formatted(.number.precision(.fractionLength(2))) }
            )
        }
        .padding(24)
        .accessibilityLabel("Elite Interest Detail")
    }
}

private struct MetricRow: View {
    let title: String
    let value: Double
    let formatter: (Double) -> String

    init(title: String, value: Double, formatter: @escaping (Double) -> String = { value in
        value.formatted(.percent.precision(.fractionLength(0)))
    }) {
        self.title = title
        self.value = value
        self.formatter = formatter
    }

    var body: some View {
        HStack {
            Text(title)
                .font(EliteInterestDetailViewStyle.metricFont)
            Spacer()
            Text(formatter(value))
                .font(.headline.monospacedDigit())
                .foregroundStyle(.primary)
        }
    }
}

#Preview {
    EliteInterestDetailView(analysis: PolicyAnalysis(policyName: "Sample", sourceFilename: "sample.pdf", dateAnalyzed: .now))
}
