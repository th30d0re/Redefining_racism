import SwiftUI

enum StressLevel: Int, Comparable, CaseIterable {
    case moderate = 1
    case high = 2
    case critical = 3
    case failing = 4

    static func < (lhs: StressLevel, rhs: StressLevel) -> Bool {
        lhs.rawValue < rhs.rawValue
    }

    var label: String {
        switch self {
        case .moderate: return "MODERATE"
        case .high: return "HIGH"
        case .critical: return "CRITICAL"
        case .failing: return "FAILING"
        }
    }

    var color: Color {
        switch self {
        case .moderate: return .yellow
        case .high: return .orange
        case .critical: return Theme.accentRed
        case .failing: return Theme.accentRed
        }
    }

    var gaugeValue: Double {
        switch self {
        case .moderate: return 0.35
        case .high: return 0.55
        case .critical: return 0.8
        case .failing: return 0.95
        }
    }

    var shouldPulse: Bool {
        self == .critical || self == .failing
    }
}

enum CapitalLevel: Int, Comparable, CaseIterable {
    case stagnant = 1
    case atRisk = 2
    case restructuring = 3
    case expanding = 4
    case peak = 5
    case terminal = 6

    static func < (lhs: CapitalLevel, rhs: CapitalLevel) -> Bool {
        lhs.rawValue < rhs.rawValue
    }

    var label: String {
        switch self {
        case .stagnant: return "STAGNANT"
        case .atRisk: return "AT RISK"
        case .restructuring: return "RESTRUCTURING"
        case .expanding: return "EXPANDING"
        case .peak: return "PEAK"
        case .terminal: return "TERMINAL"
        }
    }

    var color: Color {
        switch self {
        case .stagnant: return .gray
        case .atRisk: return .orange
        case .restructuring: return .yellow
        case .expanding: return Theme.accentGreen
        case .peak: return Theme.accentCyan
        case .terminal: return Theme.accentRed
        }
    }

    var gaugeValue: Double {
        Double(rawValue) / 6.0
    }

    var shouldPulse: Bool {
        self == .terminal
    }
}
