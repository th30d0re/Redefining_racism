//
//  PDFExtractor.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/22/26.
//

import PDFKit

nonisolated struct PDFExtractor {
    enum PDFExtractorError: Error {
        case scannedImagePDF
        case unreadable
    }

    static func extract(from url: URL) throws -> String {
        guard let document = PDFDocument(url: url) else {
            throw PDFExtractorError.unreadable
        }

        var extractedPages: [String] = []
        var hasText = false

        for index in 0..<document.pageCount {
            guard let page = document.page(at: index) else { continue }
            guard let pageText = page.string, !pageText.isEmpty else { continue }
            hasText = true
            extractedPages.append(pageText)
        }

        guard hasText else {
            throw PDFExtractorError.scannedImagePDF
        }

        return extractedPages.joined(separator: "\n\n")
    }
}
