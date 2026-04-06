import SwiftUI

struct HUDFrame<Content: View>: View {
    let title: String?
    @ViewBuilder let content: Content

    init(title: String? = nil, @ViewBuilder content: () -> Content) {
        self.title = title
        self.content = content()
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            if let title {
                HStack(spacing: 6) {
                    Circle()
                        .fill(Theme.accentGreen)
                        .frame(width: 6, height: 6)
                    Text(title)
                        .font(Theme.monoSmall)
                        .foregroundStyle(Theme.textSecondary)
                        .textCase(.uppercase)
                }
            }
            content
        }
        .padding(Theme.cardPadding)
        .background(Theme.cardBackground)
        .clipShape(RoundedRectangle(cornerRadius: Theme.cornerRadius))
        .overlay(
            RoundedRectangle(cornerRadius: Theme.cornerRadius)
                .stroke(Theme.cardBorder, lineWidth: 1)
        )
    }
}
