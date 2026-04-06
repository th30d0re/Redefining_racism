import SwiftUI

enum VariableState {
    case hidden
    case loaded
    case deployed
}

struct VariableChipView: View {
    let variable: SystemVariable
    let state: VariableState

    var body: some View {
        VStack(spacing: 2) {
            Text(variable.displaySymbol)
                .font(Theme.monoSmall)
                .fontWeight(state == .deployed ? .bold : .regular)
                .foregroundStyle(foregroundColor)

            Text(variable.fullName)
                .font(.system(size: 7, design: .monospaced))
                .foregroundStyle(state == .hidden ? Theme.textDim.opacity(0.3) : Theme.textDim)
                .lineLimit(1)
                .minimumScaleFactor(0.6)
        }
        .frame(width: 62, height: 46)
        .background(backgroundColor)
        .clipShape(RoundedRectangle(cornerRadius: 6))
        .overlay(
            RoundedRectangle(cornerRadius: 6)
                .stroke(borderColor, lineWidth: state == .deployed ? 1.5 : 0.5)
        )
        .glow(variable.category.color, active: state == .deployed)
        .opacity(state == .hidden ? 0.25 : 1.0)
    }

    private var foregroundColor: Color {
        switch state {
        case .hidden: return Theme.textDim.opacity(0.4)
        case .loaded: return variable.category.color.opacity(0.7)
        case .deployed: return variable.category.color
        }
    }

    private var backgroundColor: Color {
        switch state {
        case .hidden: return Theme.background
        case .loaded: return Theme.cardBackground
        case .deployed: return variable.category.color.opacity(0.1)
        }
    }

    private var borderColor: Color {
        switch state {
        case .hidden: return Theme.cardBorder.opacity(0.3)
        case .loaded: return variable.category.color.opacity(0.3)
        case .deployed: return variable.category.color
        }
    }
}
