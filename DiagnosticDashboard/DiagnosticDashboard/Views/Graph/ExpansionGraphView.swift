import SwiftUI

struct ExpansionGraphView: View {
    let eras: [Era]
    let selectedIndex: Int

    var body: some View {
        HUDFrame(title: "O Expansion / I_buffer Contraction") {
            GeometryReader { geometry in
                let w = geometry.size.width
                let h = geometry.size.height
                let count = eras.count
                let stepX = w / CGFloat(max(count - 1, 1))

                ZStack(alignment: .topLeading) {
                    // Grid lines
                    ForEach(0..<5) { i in
                        let y = h * CGFloat(i) / 4.0
                        Path { path in
                            path.move(to: CGPoint(x: 0, y: y))
                            path.addLine(to: CGPoint(x: w, y: y))
                        }
                        .stroke(Theme.cardBorder.opacity(0.4), style: StrokeStyle(lineWidth: 0.5, dash: [4, 4]))
                    }

                    // Selected era vertical line
                    let selectedX = CGFloat(selectedIndex) * stepX
                    Path { path in
                        path.move(to: CGPoint(x: selectedX, y: 0))
                        path.addLine(to: CGPoint(x: selectedX, y: h))
                    }
                    .stroke(Theme.textSecondary.opacity(0.5), style: StrokeStyle(lineWidth: 1, dash: [3, 3]))

                    // O expansion line (red, rising)
                    linePath(data: eras.map(\.outgroupExpansion), width: w, height: h, stepX: stepX)
                        .stroke(Theme.accentRed, style: StrokeStyle(lineWidth: 2, lineCap: .round, lineJoin: .round))

                    // O expansion area fill
                    areaPath(data: eras.map(\.outgroupExpansion), width: w, height: h, stepX: stepX)
                        .fill(Theme.accentRed.opacity(0.08))

                    // I_buffer contraction line (blue, falling)
                    linePath(data: eras.map(\.bufferContraction), width: w, height: h, stepX: stepX)
                        .stroke(Theme.accentBlue, style: StrokeStyle(lineWidth: 2, lineCap: .round, lineJoin: .round))

                    // I_buffer area fill
                    areaPath(data: eras.map(\.bufferContraction), width: w, height: h, stepX: stepX)
                        .fill(Theme.accentBlue.opacity(0.08))

                    // Data points
                    ForEach(0..<count, id: \.self) { i in
                        let x = CGFloat(i) * stepX
                        // O point
                        Circle()
                            .fill(i == selectedIndex ? Theme.accentRed : Theme.accentRed.opacity(0.5))
                            .frame(width: i == selectedIndex ? 8 : 5, height: i == selectedIndex ? 8 : 5)
                            .position(x: x, y: h * (1.0 - eras[i].outgroupExpansion))

                        // I_buffer point
                        Circle()
                            .fill(i == selectedIndex ? Theme.accentBlue : Theme.accentBlue.opacity(0.5))
                            .frame(width: i == selectedIndex ? 8 : 5, height: i == selectedIndex ? 8 : 5)
                            .position(x: x, y: h * (1.0 - eras[i].bufferContraction))
                    }
                }
            }
            .frame(height: 120)

            // Legend
            HStack(spacing: 16) {
                HStack(spacing: 4) {
                    RoundedRectangle(cornerRadius: 1)
                        .fill(Theme.accentRed)
                        .frame(width: 16, height: 2)
                    Text("O (expanding)")
                        .font(.system(size: 8, design: .monospaced))
                        .foregroundStyle(Theme.accentRed)
                }
                HStack(spacing: 4) {
                    RoundedRectangle(cornerRadius: 1)
                        .fill(Theme.accentBlue)
                        .frame(width: 16, height: 2)
                    Text("I_buf (contracting)")
                        .font(.system(size: 8, design: .monospaced))
                        .foregroundStyle(Theme.accentBlue)
                }
            }
            .padding(.top, 4)
        }
    }

    private func linePath(data: [Double], width: CGFloat, height: CGFloat, stepX: CGFloat) -> Path {
        Path { path in
            for (i, value) in data.enumerated() {
                let point = CGPoint(x: CGFloat(i) * stepX, y: height * (1.0 - value))
                if i == 0 {
                    path.move(to: point)
                } else {
                    path.addLine(to: point)
                }
            }
        }
    }

    private func areaPath(data: [Double], width: CGFloat, height: CGFloat, stepX: CGFloat) -> Path {
        var path = linePath(data: data, width: width, height: height, stepX: stepX)
        path.addLine(to: CGPoint(x: CGFloat(data.count - 1) * stepX, y: height))
        path.addLine(to: CGPoint(x: 0, y: height))
        path.closeSubpath()
        return path
    }
}
