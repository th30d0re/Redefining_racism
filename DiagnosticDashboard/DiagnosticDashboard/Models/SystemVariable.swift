import SwiftUI

enum SystemVariable: String, CaseIterable, Identifiable, Hashable {
    case E
    case O_racialized
    case I
    case I_buffer
    case F_enforce
    case F_enforce_proto
    case P_uppet
    case psi
    case QI
    case P_criminal
    case P_spatial
    case P_retroactive

    var id: String { rawValue }

    var displaySymbol: String {
        switch self {
        case .E: return "E"
        case .O_racialized: return "O_rac"
        case .I: return "I"
        case .I_buffer: return "I_buf"
        case .F_enforce: return "F_enf"
        case .F_enforce_proto: return "F_enf\u{00B0}"
        case .P_uppet: return "P_up"
        case .psi: return "\u{03C8}"
        case .QI: return "QI"
        case .P_criminal: return "P_crim"
        case .P_spatial: return "P_spat"
        case .P_retroactive: return "P_retro"
        }
    }

    var fullName: String {
        switch self {
        case .E: return "Elite Class"
        case .O_racialized: return "Racialized Out-group"
        case .I: return "In-group"
        case .I_buffer: return "Buffer Class"
        case .F_enforce: return "Enforcement Class"
        case .F_enforce_proto: return "Proto-Enforcement"
        case .P_uppet: return "Puppet Class"
        case .psi: return "Psychological Wage"
        case .QI: return "Qualified Immunity"
        case .P_criminal: return "Criminal Proxy"
        case .P_spatial: return "Spatial Proxy"
        case .P_retroactive: return "Retroactive Proxy"
        }
    }

    var category: VariableCategory {
        switch self {
        case .E, .I, .O_racialized:
            return .structural
        case .I_buffer:
            return .buffer
        case .F_enforce, .F_enforce_proto:
            return .enforcement
        case .P_uppet:
            return .puppet
        case .psi, .QI:
            return .mechanism
        case .P_criminal, .P_spatial, .P_retroactive:
            return .proxy
        }
    }

    /// Canonical display variables (excluding proto for the main grid)
    static var gridVariables: [SystemVariable] {
        [.E, .O_racialized, .I, .I_buffer, .F_enforce, .P_uppet, .psi, .QI, .P_criminal, .P_spatial, .P_retroactive]
    }
}

enum VariableCategory {
    case structural, buffer, enforcement, puppet, mechanism, proxy

    var color: Color {
        switch self {
        case .structural: return Theme.accentCyan
        case .buffer: return Theme.accentBlue
        case .enforcement: return Theme.accentRed
        case .puppet: return Theme.accentPurple
        case .mechanism: return Theme.accentAmber
        case .proxy: return Color(red: 1.0, green: 0.5, blue: 0.2)
        }
    }
}
