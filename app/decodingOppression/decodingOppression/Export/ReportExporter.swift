//
//  ReportExporter.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
#if canImport(UIKit)
import UIKit
#endif
#if os(macOS)
import AppKit
#endif

nonisolated struct ReportExporter {
    struct TierUsageStats: Codable {
        let tier1Count: Int
        let tier2Count: Int
        let tier3Count: Int
    }

    struct AnalyzedClauseExport: Codable {
        let id: UUID
        let text: String
        let sectionType: SectionType
        let targetGroup: TargetGroup
        let effectDirection: EffectDirection
        let confidence: Double
        let tierUsed: MLTier
        let architectureScores: ArchitectureScores
        let proxyTerms: [String]
        let expandsOutgroup: Bool
        let wasSafetyFallback: Bool
    }

    struct PolicyAnalysisExport: Codable {
        let id: UUID
        let policyName: String
        let sourceFilename: String
        let dateAnalyzed: Date
        let scoreResult: ScoreResult
        let clauses: [AnalyzedClauseExport]
        let tierUsageStats: TierUsageStats
        let safetyFallbackCount: Int
    }

    enum ExportError: LocalizedError {
        case renderFailed

        var errorDescription: String? {
            switch self {
            case .renderFailed:
                return "Unable to render PDF"
            }
        }
    }

    func exportJSON(analysis: PolicyAnalysis) throws -> Data {
        var tier1 = 0
        var tier2 = 0
        var tier3 = 0
        var safetyFallbackCount = 0

        let clauses = analysis.clauses.map { clause in
            switch clause.tierUsed {
            case .tier1: tier1 += 1
            case .tier2: tier2 += 1
            case .tier3: tier3 += 1
            }
            if clause.wasSafetyFallback { safetyFallbackCount += 1 }

            return AnalyzedClauseExport(
                id: clause.id,
                text: clause.text,
                sectionType: clause.sectionType,
                targetGroup: clause.targetGroup,
                effectDirection: clause.effectDirection,
                confidence: clause.confidence,
                tierUsed: clause.tierUsed,
                architectureScores: clause.architectureScores,
                proxyTerms: clause.proxyTerms,
                expandsOutgroup: clause.expandsOutgroup,
                wasSafetyFallback: clause.wasSafetyFallback
            )
        }

        let export = PolicyAnalysisExport(
            id: analysis.id,
            policyName: analysis.policyName,
            sourceFilename: analysis.sourceFilename,
            dateAnalyzed: analysis.dateAnalyzed,
            scoreResult: analysis.scoreResult,
            clauses: clauses,
            tierUsageStats: TierUsageStats(tier1Count: tier1, tier2Count: tier2, tier3Count: tier3),
            safetyFallbackCount: safetyFallbackCount
        )

        let encoder = JSONEncoder()
        encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
        return try encoder.encode(export)
    }

    func exportPDF(analysis: PolicyAnalysis) throws -> Data {
        #if canImport(UIKit)
        return try exportPDFUIKit(analysis: analysis)
        #elseif os(macOS)
        return try exportPDFAppKit(analysis: analysis)
        #else
        throw ExportError.renderFailed
        #endif
    }

    #if canImport(UIKit)
    private func exportPDFUIKit(analysis: PolicyAnalysis) throws -> Data {
        let bounds = CGRect(x: 0, y: 0, width: 612, height: 792)
        let renderer = UIGraphicsPDFRenderer(bounds: bounds)

        let data = renderer.pdfData { context in
            context.beginPage()
            let margin: CGFloat = 40
            var y: CGFloat = margin

            func ensureSpace(_ height: CGFloat) {
                if y + height > bounds.height - margin {
                    context.beginPage()
                    y = margin
                }
            }

            func drawLine(_ text: String, font: UIFont, color: UIColor = .label) {
                ensureSpace(font.lineHeight + 6)
                let attributes: [NSAttributedString.Key: Any] = [
                    .font: font,
                    .foregroundColor: color
                ]
                let rect = CGRect(x: margin, y: y, width: bounds.width - margin * 2, height: font.lineHeight + 6)
                NSString(string: text).draw(in: rect, withAttributes: attributes)
                y += font.lineHeight + 8
            }

            func drawWrapped(_ text: String, font: UIFont) {
                let attributes: [NSAttributedString.Key: Any] = [
                    .font: font,
                    .foregroundColor: UIColor.label
                ]
                let width = bounds.width - margin * 2
                let bounding = NSString(string: text).boundingRect(
                    with: CGSize(width: width, height: .greatestFiniteMagnitude),
                    options: [.usesLineFragmentOrigin, .usesFontLeading],
                    attributes: attributes,
                    context: nil
                )
                ensureSpace(bounding.height + 6)
                let rect = CGRect(x: margin, y: y, width: width, height: bounding.height)
                NSString(string: text).draw(in: rect, withAttributes: attributes)
                y += bounding.height + 8
            }

            drawLine("Policy Analysis Report", font: .boldSystemFont(ofSize: 22))
            drawLine("Policy: \(analysis.policyName)", font: .systemFont(ofSize: 14))
            drawLine("Source: \(analysis.sourceFilename)", font: .systemFont(ofSize: 12), color: .secondaryLabel)
            drawLine("Date: \(analysis.dateAnalyzed.formatted(date: .long, time: .shortened))", font: .systemFont(ofSize: 12), color: .secondaryLabel)

            drawLine("COI: \(analysis.scoreResult.coi.formatted(.number.precision(.fractionLength(2))))", font: .boldSystemFont(ofSize: 16))

            drawLine("Sub-scores", font: .boldSystemFont(ofSize: 14))
            drawLine("DIS: \(analysis.scoreResult.dis.formatted(.number.precision(.fractionLength(2))))", font: .systemFont(ofSize: 12))
            drawLine("ADS: \(analysis.scoreResult.ads.formatted(.number.precision(.fractionLength(2))))", font: .systemFont(ofSize: 12))
            drawLine("EIS: \(analysis.scoreResult.eis.formatted(.number.precision(.fractionLength(2))))", font: .systemFont(ofSize: 12))
            drawLine("CIS: \(analysis.scoreResult.cis.formatted(.number.precision(.fractionLength(2))))", font: .systemFont(ofSize: 12))
            drawLine("OES: \(analysis.scoreResult.oes.formatted(.number.precision(.fractionLength(2))))", font: .systemFont(ofSize: 12))

            let stats = tierUsageStats(for: analysis)
            drawLine("Tier usage", font: .boldSystemFont(ofSize: 14))
            drawLine("Tier 1: \(stats.tier1Count)", font: .systemFont(ofSize: 12))
            drawLine("Tier 2: \(stats.tier2Count)", font: .systemFont(ofSize: 12))
            drawLine("Tier 3: \(stats.tier3Count)", font: .systemFont(ofSize: 12))
            drawLine("Safety fallbacks: \(stats.safetyFallbackCount)", font: .systemFont(ofSize: 12))

            drawLine("Clause breakdown", font: .boldSystemFont(ofSize: 14))
            for (index, clause) in analysis.clauses.enumerated() {
                let text = "\(index + 1). [\(clause.tierUsed.rawValue)] \(clause.targetGroup.rawValue) / \(clause.effectDirection.rawValue) - \(clause.text)"
                drawWrapped(text, font: .systemFont(ofSize: 10))
            }
        }

        return data
    }
    #endif

    #if os(macOS)
    private func exportPDFAppKit(analysis: PolicyAnalysis) throws -> Data {
        let data = NSMutableData()
        var mediaBox = CGRect(x: 0, y: 0, width: 612, height: 792)
        guard let consumer = CGDataConsumer(data: data as CFMutableData),
              let context = CGContext(consumer: consumer, mediaBox: &mediaBox, nil) else {
            throw ExportError.renderFailed
        }

        context.beginPDFPage(nil)
        let graphicsContext = NSGraphicsContext(cgContext: context, flipped: false)
        NSGraphicsContext.saveGraphicsState()
        NSGraphicsContext.current = graphicsContext

        let margin: CGFloat = 40
        var y: CGFloat = margin

        func ensureSpace(_ height: CGFloat) {
            if y + height > mediaBox.height - margin {
                context.endPDFPage()
                context.beginPDFPage(nil)
                y = margin
            }
        }

        func drawLine(_ text: String, font: NSFont, color: NSColor = .labelColor) {
            ensureSpace(font.pointSize + 8)
            let attributes: [NSAttributedString.Key: Any] = [
                .font: font,
                .foregroundColor: color
            ]
            let rect = CGRect(x: margin, y: y, width: mediaBox.width - margin * 2, height: font.pointSize + 6)
            NSAttributedString(string: text, attributes: attributes).draw(in: rect)
            y += font.pointSize + 10
        }

        func drawWrapped(_ text: String, font: NSFont) {
            let attributes: [NSAttributedString.Key: Any] = [
                .font: font,
                .foregroundColor: NSColor.labelColor
            ]
            let width = mediaBox.width - margin * 2
            let bounding = NSString(string: text).boundingRect(
                with: CGSize(width: width, height: .greatestFiniteMagnitude),
                options: [.usesLineFragmentOrigin, .usesFontLeading],
                attributes: attributes
            )
            ensureSpace(bounding.height + 6)
            let rect = CGRect(x: margin, y: y, width: width, height: bounding.height)
            NSAttributedString(string: text, attributes: attributes).draw(in: rect)
            y += bounding.height + 8
        }

        drawLine("Policy Analysis Report", font: .boldSystemFont(ofSize: 22))
        drawLine("Policy: \(analysis.policyName)", font: .systemFont(ofSize: 14))
        drawLine("Source: \(analysis.sourceFilename)", font: .systemFont(ofSize: 12), color: .secondaryLabelColor)
        drawLine("Date: \(analysis.dateAnalyzed.formatted(date: .long, time: .shortened))", font: .systemFont(ofSize: 12), color: .secondaryLabelColor)

        drawLine("COI: \(analysis.scoreResult.coi.formatted(.number.precision(.fractionLength(2))))", font: .boldSystemFont(ofSize: 16))

        drawLine("Sub-scores", font: .boldSystemFont(ofSize: 14))
        drawLine("DIS: \(analysis.scoreResult.dis.formatted(.number.precision(.fractionLength(2))))", font: .systemFont(ofSize: 12))
        drawLine("ADS: \(analysis.scoreResult.ads.formatted(.number.precision(.fractionLength(2))))", font: .systemFont(ofSize: 12))
        drawLine("EIS: \(analysis.scoreResult.eis.formatted(.number.precision(.fractionLength(2))))", font: .systemFont(ofSize: 12))
        drawLine("CIS: \(analysis.scoreResult.cis.formatted(.number.precision(.fractionLength(2))))", font: .systemFont(ofSize: 12))
        drawLine("OES: \(analysis.scoreResult.oes.formatted(.number.precision(.fractionLength(2))))", font: .systemFont(ofSize: 12))

        let stats = tierUsageStats(for: analysis)
        drawLine("Tier usage", font: .boldSystemFont(ofSize: 14))
        drawLine("Tier 1: \(stats.tier1Count)", font: .systemFont(ofSize: 12))
        drawLine("Tier 2: \(stats.tier2Count)", font: .systemFont(ofSize: 12))
        drawLine("Tier 3: \(stats.tier3Count)", font: .systemFont(ofSize: 12))
        drawLine("Safety fallbacks: \(stats.safetyFallbackCount)", font: .systemFont(ofSize: 12))

        drawLine("Clause breakdown", font: .boldSystemFont(ofSize: 14))
        for (index, clause) in analysis.clauses.enumerated() {
            let text = "\(index + 1). [\(clause.tierUsed.rawValue)] \(clause.targetGroup.rawValue) / \(clause.effectDirection.rawValue) - \(clause.text)"
            drawWrapped(text, font: .systemFont(ofSize: 10))
        }

        NSGraphicsContext.restoreGraphicsState()
        context.endPDFPage()
        context.closePDF()

        return data as Data
    }
    #endif

    private func tierUsageStats(for analysis: PolicyAnalysis) -> (tier1Count: Int, tier2Count: Int, tier3Count: Int, safetyFallbackCount: Int) {
        var tier1 = 0
        var tier2 = 0
        var tier3 = 0
        var safetyFallbackCount = 0

        for clause in analysis.clauses {
            switch clause.tierUsed {
            case .tier1: tier1 += 1
            case .tier2: tier2 += 1
            case .tier3: tier3 += 1
            }
            if clause.wasSafetyFallback { safetyFallbackCount += 1 }
        }

        return (tier1, tier2, tier3, safetyFallbackCount)
    }
}
