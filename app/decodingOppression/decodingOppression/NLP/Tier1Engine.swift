//
//  Tier1Engine.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/22/26.
//

import Foundation

actor Tier1Engine {
    private let clauseAnalyzer: ClauseAnalyzer

    init() throws {
        let keywordEngine = try KeywordEngine()
        self.clauseAnalyzer = ClauseAnalyzer(keywordEngine: keywordEngine)
    }

    func extractAndPreprocess(pdf url: URL) async throws -> [Clause] {
        let rawText = try PDFExtractor.extract(from: url)
        return TextPreprocessor.preprocess(text: rawText)
    }

    func classify(clause: Clause) async -> TierClassification {
        return await clauseAnalyzer.analyze(clause: clause)
    }
}
