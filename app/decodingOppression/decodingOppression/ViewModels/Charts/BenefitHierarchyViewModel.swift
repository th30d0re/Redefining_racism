//
//  BenefitHierarchyViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation

@Observable
@MainActor
final class BenefitHierarchyViewModel {
    var analysis: PolicyAnalysis

    init(analysis: PolicyAnalysis) {
        self.analysis = analysis
    }

    var dataPoints: [BenefitHierarchyDatum] {
        let groups: [TargetGroup] = [.elite, .ingroupNonElite, .outgroup]
        var results: [BenefitHierarchyDatum] = []

        for group in groups {
            let clauses = analysis.clauses.filter { $0.targetGroup == group }
            let benefitCount = clauses.filter { $0.effectDirection == .benefit }.count
            let burdenCount = clauses.filter { $0.effectDirection == .burden }.count
            let mixedCount = clauses.filter { $0.effectDirection == .mixed }.count

            let total = max(benefitCount + burdenCount + mixedCount * 2, 1)
            let benefit = benefitCount + mixedCount
            let burden = burdenCount + mixedCount

            let benefitPercent = Double(benefit) / Double(total)
            let burdenPercent = Double(burden) / Double(total)

            results.append(BenefitHierarchyDatum(group: group, effect: .benefit, percent: benefitPercent))
            results.append(BenefitHierarchyDatum(group: group, effect: .burden, percent: burdenPercent))
        }

        return results
    }

    var accessibilitySummary: String {
        let groups: [TargetGroup] = [.elite, .ingroupNonElite, .outgroup]
        let summaries = groups.map { group -> String in
            let benefit = dataPoints.first { $0.group == group && $0.effect == .benefit }?.percent ?? 0
            let burden = dataPoints.first { $0.group == group && $0.effect == .burden }?.percent ?? 0
            let benefitText = benefit.formatted(.percent.precision(.fractionLength(0)))
            let burdenText = burden.formatted(.percent.precision(.fractionLength(0)))
            return "\(group.displayName): \(benefitText) benefit, \(burdenText) burden"
        }
        return summaries.joined(separator: "; ")
    }
}

struct BenefitHierarchyDatum: Identifiable {
    let id = UUID()
    let group: TargetGroup
    let effect: EffectDirection
    let percent: Double

    var groupLabel: String { group.displayName }
    var effectLabel: String {
        switch effect {
        case .benefit: return "Benefit"
        case .burden: return "Burden"
        case .neutral: return "Neutral"
        case .mixed: return "Mixed"
        }
    }
}

private extension TargetGroup {
    var displayName: String {
        switch self {
        case .elite: return "Elite"
        case .ingroupNonElite: return "In-Group"
        case .outgroup: return "Outgroup"
        case .multiple: return "Multiple"
        }
    }
}
