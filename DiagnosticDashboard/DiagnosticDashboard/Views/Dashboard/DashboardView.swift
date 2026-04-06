import SwiftUI

struct DashboardView: View {
    @State private var selectedIndex = 0
    private let eras = TimelineDataStore.eras

    var selectedEra: Era {
        eras[selectedIndex]
    }

    var body: some View {
        ZStack {
            Theme.background.ignoresSafeArea()

            VStack(spacing: 0) {
                // Header
                headerView
                    .padding(.horizontal, 16)
                    .padding(.top, 8)

                // Era title bar
                eraTitleBar
                    .padding(.horizontal, 16)
                    .padding(.top, 12)

                // Scrubber
                EraScrubberView(eras: eras, selectedIndex: $selectedIndex)
                    .padding(.top, 12)

                // Main content
                ScrollView(.vertical, showsIndicators: false) {
                    VStack(spacing: Theme.sectionSpacing) {
                        // Gauges
                        GaugePairView(era: selectedEra)

                        // Variable grid
                        VariableGridView(era: selectedEra)

                        // Runtime log card
                        EraCardView(era: selectedEra)

                        // Policy log
                        PolicyLogView(policies: selectedEra.policies)

                        // Expansion graph
                        ExpansionGraphView(eras: eras, selectedIndex: selectedIndex)
                    }
                    .padding(.horizontal, 16)
                    .padding(.vertical, 12)
                }
            }
        }
        .preferredColorScheme(.dark)
        .gesture(
            DragGesture(minimumDistance: 50)
                .onEnded { value in
                    if value.translation.width < -50 && selectedIndex < eras.count - 1 {
                        withAnimation(.spring(duration: 0.4)) { selectedIndex += 1 }
                    } else if value.translation.width > 50 && selectedIndex > 0 {
                        withAnimation(.spring(duration: 0.4)) { selectedIndex -= 1 }
                    }
                }
        )
    }

    private var headerView: some View {
        HStack {
            HStack(spacing: 8) {
                // Pulsing status dot
                Circle()
                    .fill(Theme.accentGreen)
                    .frame(width: 8, height: 8)
                    .glow(Theme.accentGreen, active: true)

                Text("EXTRACTION ALGORITHM")
                    .font(Theme.monoSubheadline)
                    .foregroundStyle(Theme.textPrimary)
            }

            Spacer()

            Text("RUNTIME DIAGNOSTIC")
                .font(Theme.monoCaption2)
                .foregroundStyle(Theme.textDim)
        }
    }

    private var eraTitleBar: some View {
        VStack(alignment: .leading, spacing: 2) {
            HStack {
                Text("CH \(selectedEra.id)")
                    .font(Theme.monoCaption2)
                    .foregroundStyle(selectedEra.stressLevel.color)
                    .padding(.horizontal, 6)
                    .padding(.vertical, 2)
                    .background(selectedEra.stressLevel.color.opacity(0.15))
                    .clipShape(RoundedRectangle(cornerRadius: 3))

                Text("//")
                    .foregroundStyle(Theme.textDim)

                Text("v\(selectedEra.version)")
                    .foregroundStyle(Theme.accentGreen)
            }
            .font(Theme.monoSmall)

            Text(selectedEra.title)
                .font(Theme.monoTitle3)
                .foregroundStyle(Theme.textPrimary)

            Text(selectedEra.subtitle)
                .font(Theme.monoSmall)
                .foregroundStyle(Theme.textSecondary)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .animation(.easeInOut(duration: 0.3), value: selectedIndex)
    }
}
