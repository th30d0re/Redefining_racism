//
//  ScoreCardView.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Observation
import SwiftUI

struct ScoreCardView: View {
    @Environment(\.accessibilityDifferentiateWithoutColor) private var differentiateWithoutColor
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @Environment(\.accessibilityReduceTransparency) private var reduceTransparency
    @Environment(\.dynamicTypeSize) private var dynamicTypeSize
    @Environment(\.legibilityWeight) private var legibilityWeight
    @State private var viewModel: ScoreCardViewModel
    @State private var animatedCOI: Double = 0
    @State private var selectedDrillDown: DrillDown?
    @Namespace private var rotorNamespace
    @Namespace private var linkedNamespace

    private let disKey = AccessibilityCustomContentKey("DIS")
    private let adsKey = AccessibilityCustomContentKey("ADS")
    private let eisKey = AccessibilityCustomContentKey("EIS")
    private let cisKey = AccessibilityCustomContentKey("CIS")
    private let oesKey = AccessibilityCustomContentKey("OES")

    init(analysis: PolicyAnalysis) {
        _viewModel = State(initialValue: ScoreCardViewModel(analysis: analysis))
    }

    var body: some View {
        @Bindable var viewModel = viewModel
        let content = Group {
            #if os(macOS)
            HSplitView {
                ScrollView {
                    scoreCardContent
                        .padding(24)
                }
                detailPanel
                    .frame(minWidth: 320)
            }
            .toolbar { exportToolbar }
            .popover(isPresented: $viewModel.isShowingExport, attachmentAnchor: .rect(.bounds), arrowEdge: .top) {
                ExportView(analysis: viewModel.analysis)
                    .frame(width: 360)
            }
            #else
            ScrollView {
                scoreCardContent
                    .padding(24)
            }
            .toolbar { exportToolbar }
            .sheet(isPresented: $viewModel.isShowingExport) {
                ExportView(analysis: viewModel.analysis)
            }
            #endif
        }

        return content
            .accessibilityRotor("Scores") {
                AccessibilityRotorEntry("Composite Oppression Index", id: "coi", in: rotorNamespace)
                AccessibilityRotorEntry("Differential Impact Score", id: "dis", in: rotorNamespace)
                AccessibilityRotorEntry("Architecture Detection Score", id: "ads", in: rotorNamespace)
                AccessibilityRotorEntry("Elite Interest Score", id: "eis", in: rotorNamespace)
                AccessibilityRotorEntry("Compounding Impact Score", id: "cis", in: rotorNamespace)
                AccessibilityRotorEntry("Outgroup Expansion Score", id: "oes", in: rotorNamespace)
            }
            .accessibilitySortPriority(5)
            .onAppear {
                let animation = ScoreCardViewStyle.scoreRevealAnimation(reduceMotion: reduceMotion)
                let target = max(0, min(1, viewModel.analysis.scoreResult.coi))
                if let animation {
                    withAnimation(animation) {
                        animatedCOI = target
                    }
                } else {
                    animatedCOI = target
                }
            }
            .onChange(of: viewModel.analysis.scoreResult.coi) { _, newValue in
                let animation = ScoreCardViewStyle.scoreRevealAnimation(reduceMotion: reduceMotion)
                let target = max(0, min(1, newValue))
                if let animation {
                    withAnimation(animation) {
                        animatedCOI = target
                    }
                } else {
                    animatedCOI = target
                }
            }
    }

    private var exportToolbar: some ToolbarContent {
        ToolbarItem(placement: .primaryAction) {
            Button("Export") {
                viewModel.isShowingExport = true
            }
        }
    }

    private var scoreCardContent: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("Policy Analysis Results")
                .font(.title.bold())
                .accessibilityHeading(.h1)

            gaugeBlock

            Text(viewModel.interpretation)
                .font(.headline)
                .foregroundStyle(.secondary)

            Text("Scores")
                .font(.headline)
                .accessibilityHeading(.h2)

            scoreLinkRow(
                label: "DIS",
                description: "Differential Impact",
                value: viewModel.analysis.scoreResult.dis,
                drillDown: .benefitHierarchy
            )

            scoreLinkRow(
                label: "ADS",
                description: "Architecture Detection",
                value: viewModel.analysis.scoreResult.ads,
                drillDown: .architectureRadar
            )

            scoreLinkRow(
                label: "EIS",
                description: "Elite Interest",
                value: viewModel.analysis.scoreResult.eis,
                drillDown: .eliteInterest
            )

            scoreLinkRow(
                label: "CIS",
                description: "Compounding Impact",
                value: viewModel.analysis.scoreResult.cis,
                drillDown: .compoundingTrajectory
            )

            scoreLinkRow(
                label: "OES",
                description: "Outgroup Expansion",
                value: viewModel.analysis.scoreResult.oes,
                drillDown: .outgroupExpansion
            )

            Text("Context")
                .font(.headline)
                .accessibilityHeading(.h2)

            navigationRow(title: "Historical Comparison", drillDown: .historicalComparison)
            navigationRow(title: "Clauses", drillDown: .clauses)
        }
    }

    private var gaugeBlock: some View {
        let score = viewModel.analysis.scoreResult.coi
        let scoreText = score.formatted(.number.precision(.fractionLength(2)))
        let badge = ScoreCardViewStyle.scoreColor(score, differentiateWithoutColor: differentiateWithoutColor)

        return VStack(alignment: .leading, spacing: 16) {
            ZStack {
                Circle()
                    .stroke(.secondary.opacity(0.2), lineWidth: 20)
                Circle()
                    .trim(from: 0, to: CGFloat(animatedCOI))
                    .stroke(badge.0, style: StrokeStyle(lineWidth: 20, lineCap: .round))
                    .rotationEffect(.degrees(-90))
                VStack(spacing: 8) {
                    #if os(iOS)
                    Text(scoreText)
                        .font(ScoreCardViewStyle.scoreFont(dynamicTypeSize: dynamicTypeSize, legibilityWeight: legibilityWeight))
                        .foregroundStyle(badge.0)
                        .accessibilityShowsLargeContentViewer()
                        .speechAdjustedPitch(-0.1)
                        .speechSpellsOutCharacters(false)
                    #else
                    Text(scoreText)
                        .font(ScoreCardViewStyle.scoreFont(dynamicTypeSize: dynamicTypeSize, legibilityWeight: legibilityWeight))
                        .foregroundStyle(badge.0)
                        .speechAdjustedPitch(-0.1)
                        .speechSpellsOutCharacters(false)
                    #endif
                    Text("COI")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            }
            .frame(width: 220, height: 220)
        }
        .accessibilityElement(children: .combine)
        .accessibilityLabel("Composite Oppression Index")
        .accessibilityValue("\(scoreText), \(viewModel.interpretation)")
        .accessibilityCustomContent(disKey, Text(viewModel.analysis.scoreResult.dis.formatted(.number.precision(.fractionLength(2)))))
        .accessibilityCustomContent(adsKey, Text(viewModel.analysis.scoreResult.ads.formatted(.number.precision(.fractionLength(2)))))
        .accessibilityCustomContent(eisKey, Text(viewModel.analysis.scoreResult.eis.formatted(.number.precision(.fractionLength(2)))))
        .accessibilityCustomContent(cisKey, Text(viewModel.analysis.scoreResult.cis.formatted(.number.precision(.fractionLength(2)))))
        .accessibilityCustomContent(oesKey, Text(viewModel.analysis.scoreResult.oes.formatted(.number.precision(.fractionLength(2)))))
        .accessibilityRotorEntry(id: "coi", in: rotorNamespace)
    }

    @ViewBuilder
    private func scoreLinkRow(label: String, description: String, value: Double, drillDown: DrillDown) -> some View {
        let scoreText = value.formatted(.number.precision(.fractionLength(2)))
        let badge = ScoreCardViewStyle.scoreColor(value, differentiateWithoutColor: differentiateWithoutColor)

        let rowContent = HStack {
            VStack(alignment: .leading, spacing: 4) {
                Text(label)
                    .font(.subheadline.weight(.semibold))
                Text(description)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
            Spacer()
            HStack(spacing: 6) {
                Image(systemName: badge.1)
                Text(scoreText)
                    .font(.subheadline.monospacedDigit())
                    .speechAdjustedPitch(-0.1)
                    .speechSpellsOutCharacters(false)
            }
            .foregroundStyle(badge.0)
        }
        .padding(.vertical, 6)
        .accessibilityRotorEntry(id: label.lowercased(), in: rotorNamespace)
        .accessibilityLinkedGroup(id: label.lowercased(), in: linkedNamespace)

        #if os(macOS)
        Button {
            selectedDrillDown = drillDown
        } label: {
            rowContent
        }
        .buttonStyle(.plain)
        #else
        NavigationLink {
            drillDownDestination(drillDown)
                .accessibilityLinkedGroup(id: label.lowercased(), in: linkedNamespace)
        } label: {
            rowContent
        }
        #endif
    }

    @ViewBuilder
    private func navigationRow(title: String, drillDown: DrillDown) -> some View {
        #if os(macOS)
        Button {
            selectedDrillDown = drillDown
        } label: {
            Text(title)
                .font(.subheadline.weight(.semibold))
                .padding(.vertical, 4)
        }
        .buttonStyle(.plain)
        #else
        NavigationLink {
            drillDownDestination(drillDown)
        } label: {
            Text(title)
                .font(.subheadline.weight(.semibold))
                .padding(.vertical, 4)
        }
        #endif
    }

    @ViewBuilder
    private func drillDownDestination(_ drillDown: DrillDown) -> some View {
        switch drillDown {
        case .benefitHierarchy:
            BenefitHierarchyView(analysis: viewModel.analysis)
                .accessibilitySortPriority(2)
                .accessibilityLinkedGroup(id: "dis", in: linkedNamespace)
        case .architectureRadar:
            ArchitectureRadarView(analysis: viewModel.analysis)
                .accessibilitySortPriority(4)
                .accessibilityLinkedGroup(id: "ads", in: linkedNamespace)
        case .eliteInterest:
            EliteInterestDetailView(analysis: viewModel.analysis)
                .accessibilityLinkedGroup(id: "eis", in: linkedNamespace)
        case .compoundingTrajectory:
            CompoundingTrajectoryView(analysis: viewModel.analysis)
                .accessibilitySortPriority(3)
                .accessibilityLinkedGroup(id: "cis", in: linkedNamespace)
        case .outgroupExpansion:
            OutgroupExpansionView(analysis: viewModel.analysis)
                .accessibilityLinkedGroup(id: "oes", in: linkedNamespace)
        case .historicalComparison:
            HistoricalComparisonView(analysis: viewModel.analysis)
                .accessibilitySortPriority(1)
        case .clauses:
            ClauseListView(analysis: viewModel.analysis)
        }
    }

    @ViewBuilder
    private var detailPanel: some View {
        let panel = Group {
            if let drillDown = selectedDrillDown {
                drillDownDestination(drillDown)
            } else {
                ContentUnavailableView(
                    "Select a Detail",
                    systemImage: "chart.bar",
                    description: Text("Choose a score to explore the analysis.")
                )
            }
        }

        panel
            .padding(24)
            .background(ScoreCardViewStyle.backgroundMaterial(reduceTransparency: reduceTransparency))
    }

    private enum DrillDown: Hashable {
        case benefitHierarchy
        case architectureRadar
        case eliteInterest
        case compoundingTrajectory
        case outgroupExpansion
        case historicalComparison
        case clauses
    }
}

#Preview {
    NavigationStack {
        ScoreCardView(analysis: PolicyAnalysis(policyName: "Sample", sourceFilename: "sample.pdf", dateAnalyzed: .now))
    }
}
