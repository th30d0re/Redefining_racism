//
//  HistoricalComparisonView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Charts
import SwiftUI

struct HistoricalComparisonView: View {
    @State private var viewModel: HistoricalComparisonViewModel
    init(analysis: PolicyAnalysis) {
        _viewModel = State(initialValue: HistoricalComparisonViewModel(analysis: analysis))
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("Historical Comparison")
                .font(.title2.weight(.semibold))
                .accessibilityHeading(.h2)

            Chart(viewModel.entries) { entry in
                BarMark(
                    x: .value("Policy", entry.name),
                    y: .value("COI", entry.coi)
                )
                .foregroundStyle(HistoricalComparisonViewStyle.barColor(isCurrent: entry.isCurrent))
            }
            .chartYAxis {
                AxisMarks(position: .leading) {
                    AxisGridLine()
                    AxisValueLabel()
                }
            }
            .accessibilityElement(children: .contain)
            .accessibilityRotor("Policies") {
                ForEach(viewModel.entries) { entry in
                    AccessibilityRotorEntry(entry.name, id: entry.id)
                }
            }
        }
        .padding(24)
        .accessibilityRotor("Historical Policies") {
            ForEach(viewModel.entries) { entry in
                AccessibilityRotorEntry(entry.name, id: entry.id)
            }
        }
        .accessibilitySortPriority(1)
    }

    private func accessibilityValue(for entry: HistoricalComparisonEntry) -> String {
        let score = entry.coi.formatted(.number.precision(.fractionLength(2)))
        if entry.isCurrent {
            return "\(score), current policy"
        }
        return score
    }
}

#Preview {
    HistoricalComparisonView(analysis: PolicyAnalysis(policyName: "Sample", sourceFilename: "sample.pdf", dateAnalyzed: .now))
}
