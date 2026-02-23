//
//  ExportViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation
import UniformTypeIdentifiers

@Observable
@MainActor
final class ExportViewModel {
    var isGenerating: Bool = false
    var error: Error?
    var exportedItem: ExportedItem?

    func export(analysis: PolicyAnalysis, format: ExportFormat) {
        guard !isGenerating else { return }
        isGenerating = true
        error = nil
        exportedItem = nil

        Task { [weak self] in
            guard let self else { return }
            do {
                let exporter = ReportExporter()
                let data: Data
                switch format {
                case .pdf:
                    data = try exporter.exportPDF(analysis: analysis)
                case .json:
                    data = try exporter.exportJSON(analysis: analysis)
                }

                let filename = "\(analysis.policyName.replacingOccurrences(of: " ", with: "_"))_report.\(format.fileExtension)"
                let url = FileManager.default.temporaryDirectory.appendingPathComponent(filename)
                try data.write(to: url, options: [.atomic])

                exportedItem = ExportedItem(url: url, type: format.utType)
            } catch {
                self.error = error
            }
            isGenerating = false
        }
    }
}

struct ExportedItem: Identifiable {
    let id = UUID()
    let url: URL
    let type: UTType
}

enum ExportFormat: String, CaseIterable {
    case pdf
    case json

    var label: String {
        switch self {
        case .pdf: return "PDF Report"
        case .json: return "JSON Data"
        }
    }

    var utType: UTType {
        switch self {
        case .pdf: return .pdf
        case .json: return .json
        }
    }

    var fileExtension: String {
        switch self {
        case .pdf: return "pdf"
        case .json: return "json"
        }
    }
}
