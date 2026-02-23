//
//  CompoundingTrajectoryView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Charts
import SwiftUI

struct CompoundingTrajectoryView: View {
    @State private var viewModel: CompoundingTrajectoryViewModel

    init(analysis: PolicyAnalysis) {
        _viewModel = State(initialValue: CompoundingTrajectoryViewModel(analysis: analysis))
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("Compounding Impact Trajectory")
                .font(.title2.weight(.semibold))
                .accessibilityHeading(.h2)

            Chart {
                ForEach(viewModel.points) { point in
                    LineMark(
                        x: .value("Year", point.year),
                        y: .value("Capacity", point.capacity)
                    )
                    .foregroundStyle(CompoundingTrajectoryViewStyle.lineColor)

                    if point.isCurrent {
                        PointMark(
                            x: .value("Year", point.year),
                            y: .value("Capacity", point.capacity)
                        )
                        .foregroundStyle(CompoundingTrajectoryViewStyle.currentPointColor)
                    }
                }
            }
            .chartYAxis {
                AxisMarks(position: .leading) {
                    AxisGridLine()
                    AxisValueLabel(format: FloatingPointFormatStyle<Double>.Percent())
                }
            }
            .accessibilityChartDescriptor(CompoundingChartDescriptor(points: viewModel.points))
            .accessibilityLabel("Compounding Impact Trajectory")
            .accessibilityHint("Tracks outgroup capacity over time")
        }
        .padding(24)
        .accessibilitySortPriority(3)
    }
}

struct CompoundingChartDescriptor: AXChartDescriptorRepresentable {
    let points: [CompoundingPoint]

    func makeChartDescriptor() -> AXChartDescriptor {
        let xAxis = AXNumericDataAxisDescriptor(
            title: "Year",
            range: Double((points.first?.year ?? 0))...Double((points.last?.year ?? 0)),
            gridlinePositions: [],
            valueDescriptionProvider: { value in
                String(Int(value))
            }
        )
        let yAxis = AXNumericDataAxisDescriptor(
            title: "Capacity",
            range: 0...1,
            gridlinePositions: [],
            valueDescriptionProvider: { value in
                value.formatted(.percent)
            }
        )

        let series = AXDataSeriesDescriptor(
            name: "Capacity",
            isContinuous: true,
            dataPoints: points.map { point in
                AXDataPoint(x: Double(point.year), y: point.capacity)
            }
        )

        return AXChartDescriptor(
            title: "Compounding Impact Trajectory",
            summary: "Outgroup capacity over time",
            xAxis: xAxis,
            yAxis: yAxis,
            series: [series]
        )
    }
}

#Preview {
    CompoundingTrajectoryView(analysis: PolicyAnalysis(policyName: "Sample", sourceFilename: "sample.pdf", dateAnalyzed: .now))
}
