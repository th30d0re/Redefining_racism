//
//  BenefitHierarchyViewStyle.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Charts
import SwiftUI

struct BenefitHierarchyViewStyle {
    static func effectColor(_ effect: EffectDirection) -> Color {
        switch effect {
        case .benefit:
            return .green
        case .burden:
            return .red
        case .neutral:
            return .gray
        case .mixed:
            return .orange
        }
    }

    static func symbolShape(for effect: EffectDirection) -> BenefitSymbol {
        BenefitSymbol(effect: effect)
    }
}

struct BenefitSymbol: ChartSymbolShape {
    let effect: EffectDirection
    static var defaultSize: CGSize { CGSize(width: 14, height: 14) }
    var perceptualUnitRect: CGRect { CGRect(x: 0, y: 0, width: 1, height: 1) }

    func path(in rect: CGRect) -> Path {
        var path = Path()
        switch effect {
        case .benefit:
            let center = CGPoint(x: rect.midX, y: rect.midY)
            path.move(to: CGPoint(x: center.x, y: rect.minY))
            path.addLine(to: CGPoint(x: rect.maxX, y: center.y))
            path.addLine(to: CGPoint(x: center.x, y: rect.maxY))
            path.addLine(to: CGPoint(x: rect.minX, y: center.y))
            path.closeSubpath()
        case .burden:
            path.move(to: CGPoint(x: rect.midX, y: rect.minY))
            path.addLine(to: CGPoint(x: rect.maxX, y: rect.maxY))
            path.addLine(to: CGPoint(x: rect.minX, y: rect.maxY))
            path.closeSubpath()
        default:
            path.addEllipse(in: rect)
        }
        return path
    }
}
