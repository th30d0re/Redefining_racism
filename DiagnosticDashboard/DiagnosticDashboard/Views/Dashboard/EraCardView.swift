import SwiftUI

struct EraCardView: View {
    let era: Era

    var body: some View {
        HUDFrame(title: "Runtime Log: \(era.dateRange) (\(era.location))") {
            VStack(alignment: .leading, spacing: 8) {
                // Active patch
                HStack(spacing: 6) {
                    Text(">")
                        .foregroundStyle(Theme.accentGreen)
                    Text("Active Patch:")
                        .foregroundStyle(Theme.accentAmber)
                    Text(era.activePatch)
                        .foregroundStyle(Theme.textPrimary)
                }
                .font(Theme.monoCaption2)

                // Executing function
                HStack(alignment: .top, spacing: 6) {
                    Text(">")
                        .foregroundStyle(Theme.accentGreen)
                    Text("Executing:")
                        .foregroundStyle(Theme.accentAmber)
                    Text(era.executingFunction)
                        .foregroundStyle(Theme.textPrimary)
                }
                .font(Theme.monoCaption2)

                Divider().overlay(Theme.cardBorder)

                // Result
                HStack(alignment: .top, spacing: 6) {
                    Text(">")
                        .foregroundStyle(Theme.accentGreen)
                    Text("Result:")
                        .foregroundStyle(Theme.accentGreen)
                    Text(era.result)
                        .foregroundStyle(Theme.textPrimary)
                }
                .font(Theme.monoCaption2)

                // Warning
                if let warning = era.warning {
                    HStack(alignment: .top, spacing: 6) {
                        Text("!")
                            .foregroundStyle(Theme.accentRed)
                            .fontWeight(.bold)
                        Text("WARNING:")
                            .foregroundStyle(Theme.accentRed)
                            .fontWeight(.bold)
                        Text(warning)
                            .foregroundStyle(Theme.accentRed)
                    }
                    .font(Theme.monoCaption2)
                    .glow(Theme.accentRed, active: true)
                }
            }
        }
    }
}
