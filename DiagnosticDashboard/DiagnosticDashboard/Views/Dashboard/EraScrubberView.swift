import SwiftUI

struct EraScrubberView: View {
    let eras: [Era]
    @Binding var selectedIndex: Int

    var body: some View {
        ScrollViewReader { proxy in
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 0) {
                    ForEach(Array(eras.enumerated()), id: \.element.id) { index, era in
                        Button {
                            withAnimation(.spring(duration: 0.4)) {
                                selectedIndex = index
                            }
                        } label: {
                            VStack(spacing: 4) {
                                // Version badge
                                Text("v\(era.version)")
                                    .font(.system(size: 9, design: .monospaced))
                                    .fontWeight(.bold)
                                    .foregroundStyle(isSelected(index) ? Theme.background : stressColor(era))
                                    .padding(.horizontal, 8)
                                    .padding(.vertical, 3)
                                    .background(isSelected(index) ? stressColor(era) : Theme.cardBackground)
                                    .clipShape(RoundedRectangle(cornerRadius: 4))
                                    .overlay(
                                        RoundedRectangle(cornerRadius: 4)
                                            .stroke(stressColor(era).opacity(isSelected(index) ? 1 : 0.4), lineWidth: 1)
                                    )

                                // Era title
                                Text(era.title)
                                    .font(.system(size: 7, design: .monospaced))
                                    .foregroundStyle(isSelected(index) ? Theme.textPrimary : Theme.textDim)
                                    .lineLimit(1)
                                    .frame(width: 72)

                                // Date
                                Text(era.dateRange)
                                    .font(.system(size: 6, design: .monospaced))
                                    .foregroundStyle(Theme.textDim)
                                    .lineLimit(1)
                            }
                            .padding(.vertical, 6)
                            .padding(.horizontal, 4)
                        }
                        .id(index)

                        // Connector line
                        if index < eras.count - 1 {
                            Rectangle()
                                .fill(connectorColor(index))
                                .frame(width: 16, height: 1)
                                .offset(y: -8)
                        }
                    }
                }
                .padding(.horizontal, 12)
            }
            .onChange(of: selectedIndex) { _, newValue in
                withAnimation {
                    proxy.scrollTo(newValue, anchor: .center)
                }
            }
        }
    }

    private func isSelected(_ index: Int) -> Bool {
        index == selectedIndex
    }

    private func stressColor(_ era: Era) -> Color {
        era.stressLevel.color
    }

    private func connectorColor(_ index: Int) -> Color {
        index < selectedIndex ? Theme.accentGreen.opacity(0.5) : Theme.cardBorder
    }
}
