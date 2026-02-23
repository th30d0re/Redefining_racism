//
//  OutgroupExpansionView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct OutgroupExpansionView: View {
    @State private var viewModel: OutgroupExpansionViewModel

    init(analysis: PolicyAnalysis) {
        _viewModel = State(initialValue: OutgroupExpansionViewModel(analysis: analysis))
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("Outgroup Expansion")
                .font(.title2.weight(.semibold))
                .accessibilityHeading(.h2)

            MetricRow(title: "Expansion rate", value: viewModel.expansionRate)
            MetricRow(title: "Proxy usage rate", value: viewModel.proxyUsageRate)
            MetricRow(title: "Proxy density", value: viewModel.proxyDensity)

            if !viewModel.uniqueProxyTerms.isEmpty {
                Text("Proxy terms")
                    .font(.headline)
                LazyVGrid(columns: [GridItem(.adaptive(minimum: 80), spacing: 8)], alignment: .leading, spacing: 8) {
                    ForEach(viewModel.uniqueProxyTerms, id: \.self) { tag in
                        Text(tag)
                            .font(.caption)
                            .padding(.vertical, 4)
                            .padding(.horizontal, 8)
                            .background(.thinMaterial, in: Capsule())
                    }
                }
            }
        }
        .padding(24)
        .accessibilityLabel("Outgroup Expansion Score")
    }
}

private struct MetricRow: View {
    let title: String
    let value: Double

    var body: some View {
        HStack {
            Text(title)
                .font(OutgroupExpansionViewStyle.metricFont)
            Spacer()
            Text(value.formatted(.percent.precision(.fractionLength(0))))
                .font(.headline.monospacedDigit())
                .foregroundStyle(.primary)
        }
    }
}

#Preview {
    OutgroupExpansionView(analysis: PolicyAnalysis(policyName: "Sample", sourceFilename: "sample.pdf", dateAnalyzed: .now))
}
