import SwiftUI

struct PolicyLogView: View {
    let policies: [PolicyEntry]
    @State private var visibleCount = 0

    var body: some View {
        HUDFrame(title: "Policy Log") {
            if policies.isEmpty {
                Text("> No policies enacted this cycle.")
                    .font(Theme.monoCaption2)
                    .foregroundStyle(Theme.textDim)
            } else {
                VStack(alignment: .leading, spacing: 4) {
                    ForEach(Array(policies.enumerated()), id: \.element.id) { index, policy in
                        if index < visibleCount {
                            HStack(alignment: .top, spacing: 0) {
                                Text("[\(policy.year)] ")
                                    .foregroundStyle(Theme.accentAmber)
                                Text(policy.name)
                                    .foregroundStyle(Theme.accentGreen)
                                Text(" — ")
                                    .foregroundStyle(Theme.textDim)
                                Text(policy.description)
                                    .foregroundStyle(Theme.textPrimary)
                            }
                            .font(Theme.monoCaption2)
                            .transition(.opacity.combined(with: .move(edge: .leading)))
                        }
                    }
                }
            }
        }
        .onAppear { animatePolicies() }
        .onChange(of: policies.count) { _, _ in animatePolicies() }
    }

    private func animatePolicies() {
        visibleCount = 0
        for i in 0..<policies.count {
            DispatchQueue.main.asyncAfter(deadline: .now() + Double(i) * 0.15) {
                withAnimation(.easeOut(duration: 0.3)) {
                    visibleCount = i + 1
                }
            }
        }
    }
}
