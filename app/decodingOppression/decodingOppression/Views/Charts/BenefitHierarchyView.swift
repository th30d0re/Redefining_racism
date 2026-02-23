//
//  BenefitHierarchyView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Charts
import SwiftUI

struct BenefitHierarchyView: View {
    @Environment(\.accessibilityDifferentiateWithoutColor) private var differentiateWithoutColor
    @State private var viewModel: BenefitHierarchyViewModel

    init(analysis: PolicyAnalysis) {
        _viewModel = State(initialValue: BenefitHierarchyViewModel(analysis: analysis))
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("Benefit Hierarchy")
                .font(.title2.weight(.semibold))
                .accessibilityHeading(.h2)

            Group {
                if differentiateWithoutColor {
                    Chart(viewModel.dataPoints) { datum in
                        BarMark(
                            x: .value("Group", datum.groupLabel),
                            y: .value("Percent", datum.percent)
                        )
                        .foregroundStyle(by: .value("Effect", datum.effectLabel))
                        .symbol(by: .value("Effect", datum.effectLabel))
                    }
                    .chartForegroundStyleScale([
                        "Benefit": AnyShapeStyle(ImagePaint(image: Image(systemName: "circle.fill"), scale: 0.15)),
                        "Burden": AnyShapeStyle(ImagePaint(image: Image(systemName: "line.diagonal"), scale: 0.15))
                    ])
                    .chartSymbolScale([
                        "Benefit": BenefitHierarchyViewStyle.symbolShape(for: .benefit),
                        "Burden": BenefitHierarchyViewStyle.symbolShape(for: .burden)
                    ])
                    .chartYAxis {
                        AxisMarks(position: .leading) {
                            AxisGridLine()
                            AxisValueLabel(format: FloatingPointFormatStyle<Double>.Percent())
                        }
                    }
                } else {
                    Chart(viewModel.dataPoints) { datum in
                        BarMark(
                            x: .value("Group", datum.groupLabel),
                            y: .value("Percent", datum.percent)
                        )
                        .foregroundStyle(by: .value("Effect", datum.effectLabel))
                    }
                    .chartYAxis {
                        AxisMarks(position: .leading) {
                            AxisGridLine()
                            AxisValueLabel(format: FloatingPointFormatStyle<Double>.Percent())
                        }
                    }
                }
            }
            .accessibilityChartDescriptor(BenefitChartDescriptor(dataPoints: viewModel.dataPoints))
            .accessibilityLabel("Benefit Hierarchy Chart")
            .accessibilityValue(viewModel.accessibilitySummary)
        }
        .padding(24)
        .accessibilitySortPriority(2)
    }
}

struct BenefitChartDescriptor: AXChartDescriptorRepresentable {
    let dataPoints: [BenefitHierarchyDatum]

    func makeChartDescriptor() -> AXChartDescriptor {
        let groups = ["Elite", "In-Group", "Outgroup"]
        let xAxis = AXCategoricalDataAxisDescriptor(title: "Target Group", categoryOrder: groups)
        let yAxis = AXNumericDataAxisDescriptor(
            title: "Percentage",
            range: 0...1,
            gridlinePositions: [],
            valueDescriptionProvider: { value in
                value.formatted(.percent)
            }
        )

        let benefitSeries = AXDataSeriesDescriptor(
            name: "Benefit",
            isContinuous: false,
            dataPoints: groups.map { group in
                let value = dataPoints.first { $0.groupLabel == group && $0.effect == .benefit }?.percent ?? 0
                return AXDataPoint(x: group, y: value)
            }
        )

        let burdenSeries = AXDataSeriesDescriptor(
            name: "Burden",
            isContinuous: false,
            dataPoints: groups.map { group in
                let value = dataPoints.first { $0.groupLabel == group && $0.effect == .burden }?.percent ?? 0
                return AXDataPoint(x: group, y: value)
            }
        )

        return AXChartDescriptor(
            title: "Benefit Hierarchy",
            summary: "Relative benefits and burdens by target group",
            xAxis: xAxis,
            yAxis: yAxis,
            series: [benefitSeries, burdenSeries]
        )
    }
}

#Preview {
    BenefitHierarchyView(analysis: PolicyAnalysis(policyName: "Sample", sourceFilename: "sample.pdf", dateAnalyzed: .now))
}
