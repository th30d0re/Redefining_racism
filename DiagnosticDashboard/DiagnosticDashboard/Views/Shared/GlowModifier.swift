import SwiftUI

struct GlowModifier: ViewModifier {
    let color: Color
    let active: Bool
    @State private var glowing = false

    func body(content: Content) -> some View {
        content
            .shadow(color: active ? color.opacity(glowing ? 0.8 : 0.3) : .clear, radius: active ? 8 : 0)
            .onAppear {
                guard active else { return }
                withAnimation(.easeInOut(duration: 1.0).repeatForever(autoreverses: true)) {
                    glowing = true
                }
            }
            .onChange(of: active) { _, newValue in
                if newValue {
                    withAnimation(.easeInOut(duration: 1.0).repeatForever(autoreverses: true)) {
                        glowing = true
                    }
                } else {
                    glowing = false
                }
            }
    }
}

extension View {
    func glow(_ color: Color, active: Bool = true) -> some View {
        modifier(GlowModifier(color: color, active: active))
    }
}
