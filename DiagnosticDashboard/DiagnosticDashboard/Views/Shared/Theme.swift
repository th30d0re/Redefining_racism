import SwiftUI

enum Theme {
    // Backgrounds
    static let background = Color(red: 0.04, green: 0.04, blue: 0.07)
    static let cardBackground = Color(red: 0.07, green: 0.09, blue: 0.11)
    static let cardBorder = Color(red: 0.15, green: 0.25, blue: 0.3)

    // Accents
    static let accentGreen = Color(red: 0.0, green: 0.9, blue: 0.4)
    static let accentRed = Color(red: 1.0, green: 0.2, blue: 0.2)
    static let accentAmber = Color(red: 1.0, green: 0.75, blue: 0.0)
    static let accentCyan = Color(red: 0.0, green: 0.85, blue: 0.95)
    static let accentBlue = Color(red: 0.3, green: 0.5, blue: 1.0)
    static let accentPurple = Color(red: 0.6, green: 0.3, blue: 0.9)

    // Text
    static let textPrimary = Color(red: 0.85, green: 0.9, blue: 0.85)
    static let textSecondary = Color(red: 0.55, green: 0.6, blue: 0.55)
    static let textDim = Color(red: 0.35, green: 0.38, blue: 0.35)

    // Fonts
    static let mono = Font.system(.body, design: .monospaced)
    static let monoSmall = Font.system(.caption, design: .monospaced)
    static let monoCaption2 = Font.system(.caption2, design: .monospaced)
    static let monoTitle = Font.system(.title2, design: .monospaced).weight(.bold)
    static let monoTitle3 = Font.system(.title3, design: .monospaced).weight(.semibold)
    static let monoHeadline = Font.system(.headline, design: .monospaced)
    static let monoSubheadline = Font.system(.subheadline, design: .monospaced)

    // Spacing
    static let cardPadding: CGFloat = 14
    static let sectionSpacing: CGFloat = 16
    static let cornerRadius: CGFloat = 8
}
