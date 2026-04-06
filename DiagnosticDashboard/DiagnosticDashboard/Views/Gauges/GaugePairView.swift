import SwiftUI

struct GaugePairView: View {
    let era: Era

    var body: some View {
        HUDFrame(title: "System Diagnostics") {
            HStack(spacing: 24) {
                ArcGaugeView(
                    label: "System Stress (min)",
                    value: era.stressLevel.gaugeValue,
                    statusText: era.stressLevel.label,
                    color: era.stressLevel.color,
                    shouldPulse: era.stressLevel.shouldPulse
                )
                Spacer()
                ArcGaugeView(
                    label: "Capital (max)",
                    value: era.capitalLevel.gaugeValue,
                    statusText: era.capitalLevel.label,
                    color: era.capitalLevel.color,
                    shouldPulse: era.capitalLevel.shouldPulse
                )
            }
            .padding(.top, 4)

            // Descriptions
            VStack(alignment: .leading, spacing: 6) {
                HStack(alignment: .top, spacing: 6) {
                    Text("min:")
                        .foregroundStyle(era.stressLevel.color)
                    Text(era.stressDescription)
                        .foregroundStyle(Theme.textPrimary)
                }
                .font(Theme.monoCaption2)

                HStack(alignment: .top, spacing: 6) {
                    Text("max:")
                        .foregroundStyle(era.capitalLevel.color)
                    Text(era.capitalDescription)
                        .foregroundStyle(Theme.textPrimary)
                }
                .font(Theme.monoCaption2)
            }
            .padding(.top, 8)
        }
    }
}
