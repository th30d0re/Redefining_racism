//
//  ArchitectureRadarView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct ArchitectureRadarView: View {
    @Environment(\.accessibilityDifferentiateWithoutColor) private var differentiateWithoutColor
    @State private var viewModel: ArchitectureRadarViewModel
    @State private var selectedIndex: Int = 0

    init(analysis: PolicyAnalysis) {
        _viewModel = State(initialValue: ArchitectureRadarViewModel(analysis: analysis))
    }

    var body: some View {
        let components = viewModel.components
        VStack(alignment: .leading, spacing: 16) {
            Text("Architecture Detection Radar")
                .font(.title2.weight(.semibold))
                .accessibilityHeading(.h2)

            GeometryReader { proxy in
                Canvas { context, size in
                    let center = CGPoint(x: size.width / 2, y: size.height / 2)
                    let radius = min(size.width, size.height) * 0.35
                    let count = components.count
                    let angleStep = (2 * Double.pi) / Double(count)

                    for index in 0..<count {
                        let angle = -Double.pi / 2 + Double(index) * angleStep
                        let axisPoint = CGPoint(
                            x: center.x + CGFloat(cos(angle)) * radius,
                            y: center.y + CGFloat(sin(angle)) * radius
                        )

                        var axisPath = Path()
                        axisPath.move(to: center)
                        axisPath.addLine(to: axisPoint)
                        context.stroke(
                            axisPath,
                            with: .color(.secondary),
                            style: ArchitectureRadarViewStyle.axisStrokeStyle(index: index, differentiateWithoutColor: differentiateWithoutColor)
                        )

                        let labelPoint = CGPoint(
                            x: center.x + CGFloat(cos(angle)) * (radius + 18),
                            y: center.y + CGFloat(sin(angle)) * (radius + 18)
                        )
                        context.draw(Text(components[index].name).font(.caption2), at: labelPoint)
                    }

                    var polygon = Path()
                    for index in 0..<count {
                        let angle = -Double.pi / 2 + Double(index) * angleStep
                        let scoreRadius = radius * CGFloat(max(0, min(1, components[index].score)))
                        let point = CGPoint(
                            x: center.x + CGFloat(cos(angle)) * scoreRadius,
                            y: center.y + CGFloat(sin(angle)) * scoreRadius
                        )
                        if index == 0 {
                            polygon.move(to: point)
                        } else {
                            polygon.addLine(to: point)
                        }
                    }
                    polygon.closeSubpath()

                    context.fill(polygon, with: .color(.accentColor.opacity(0.2)))
                    context.stroke(polygon, with: .color(.accentColor), style: ArchitectureRadarViewStyle.polygonStrokeStyle(differentiateWithoutColor: differentiateWithoutColor))
                }
            }
            .frame(height: 280)
            .accessibilityLabel("Architecture Detection Radar Chart")
            .accessibilityValue(accessibilityValue(for: components))
            .accessibilityAdjustableAction { direction in
                switch direction {
                case .increment:
                    selectedIndex = min(selectedIndex + 1, components.count - 1)
                case .decrement:
                    selectedIndex = max(selectedIndex - 1, 0)
                default:
                    break
                }
            }
            .accessibilityRepresentation {
                VStack(alignment: .leading, spacing: 6) {
                    ForEach(components) { component in
                        Text("\(component.name): \(component.score, format: .percent)")
                    }
                }
            }
        }
        .padding(24)
        .accessibilitySortPriority(4)
    }

    private func accessibilityValue(for components: [ArchitectureComponent]) -> Text {
        guard components.indices.contains(selectedIndex) else { return Text("") }
        let component = components[selectedIndex]
        return Text("\(component.name): \(component.score, format: .percent)")
    }
}

#Preview {
    ArchitectureRadarView(analysis: PolicyAnalysis(policyName: "Sample", sourceFilename: "sample.pdf", dateAnalyzed: .now))
}
