import SwiftUI

struct ArcGaugeView: View {
    let label: String
    let value: Double
    let statusText: String
    let color: Color
    let shouldPulse: Bool

    @State private var animatedValue: Double = 0

    var body: some View {
        VStack(spacing: 10) {
            ZStack {
                // Background arc
                ArcShape(progress: 1.0)
                    .stroke(Theme.cardBorder, style: StrokeStyle(lineWidth: 8, lineCap: .round))
                    .frame(width: 120, height: 70)

                // Filled arc
                ArcShape(progress: animatedValue)
                    .stroke(color, style: StrokeStyle(lineWidth: 8, lineCap: .round))
                    .frame(width: 120, height: 70)
                    .glow(color, active: shouldPulse)

                // Value text
                Text(statusText)
                    .font(Theme.monoCaption2)
                    .foregroundStyle(color)
                    .offset(y: 20)
                    .glow(color, active: shouldPulse)
            }

            Text(label)
                .font(Theme.monoCaption2)
                .foregroundStyle(Theme.textSecondary)
                .textCase(.uppercase)
        }
        .onAppear {
            withAnimation(.spring(duration: 1.0, bounce: 0.3)) {
                animatedValue = value
            }
        }
        .onChange(of: value) { _, newValue in
            withAnimation(.spring(duration: 0.8, bounce: 0.2)) {
                animatedValue = newValue
            }
        }
    }
}

struct ArcShape: Shape {
    var progress: Double

    var animatableData: Double {
        get { progress }
        set { progress = newValue }
    }

    func path(in rect: CGRect) -> Path {
        var path = Path()
        let center = CGPoint(x: rect.midX, y: rect.maxY)
        let radius = min(rect.width, rect.height * 2) / 2
        let startAngle = Angle(degrees: 180)
        let endAngle = Angle(degrees: 180 + (180 * progress))
        path.addArc(center: center, radius: radius, startAngle: startAngle, endAngle: endAngle, clockwise: false)
        return path
    }
}
