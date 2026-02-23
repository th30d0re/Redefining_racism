//
//  TextPreprocessor.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/22/26.
//

import Foundation
import NaturalLanguage

nonisolated struct TextPreprocessor {
    static func preprocess(text: String) -> [Clause] {
        let sectionRanges = detectSectionRanges(in: text)
        let tokenizer = NLTokenizer(unit: .sentence)
        tokenizer.string = text

        var clauses: [Clause] = []
        let fullRange = text.startIndex..<text.endIndex

        tokenizer.enumerateTokens(in: fullRange) { tokenRange, _ in
            let sentenceText = String(text[tokenRange])
            let sectionType = sectionType(for: tokenRange.lowerBound, in: sectionRanges)
            let clause = Clause(
                id: UUID(),
                text: sentenceText,
                sectionType: sectionType,
                targetGroup: nil,
                effectDirection: nil
            )
            clauses.append(clause)
            return true
        }

        return clauses
    }

    private static func detectSectionRanges(in text: String) -> [(range: Range<String.Index>, sectionType: SectionType)] {
        let patternDefinitions: [(String, SectionType)] = [
            ("(?i)\\bTITLE\\b", .title),
            ("(?i)\\bDEFINITIONS?\\b", .definitions),
            ("(?i)\\bSECTION\\s+\\d+\\b", .operativeClauses),
            ("(?i)\\bPENALTIES\\b", .penalties),
            ("(?i)\\bEXCEPTIONS?\\b", .exceptions)
        ]

        let compiledPatterns: [(NSRegularExpression, SectionType)] = patternDefinitions.compactMap { pattern, sectionType in
            do {
                return (try NSRegularExpression(pattern: pattern), sectionType)
            } catch {
                assertionFailure("Invalid section header regex: \(pattern)")
                return nil
            }
        }

        var ranges: [(range: Range<String.Index>, sectionType: SectionType)] = []
        var currentSection: SectionType = .operativeClauses

        text.enumerateSubstrings(in: text.startIndex..<text.endIndex, options: .byLines) { line, range, _, _ in
            guard let line = line else { return }
            if let matchedSection = compiledPatterns.first(where: { regex, _ in
                let nsRange = NSRange(line.startIndex..<line.endIndex, in: line)
                return regex.firstMatch(in: line, range: nsRange) != nil
            })?.1 {
                currentSection = matchedSection
            }
            ranges.append((range: range, sectionType: currentSection))
        }

        return ranges
    }

    private static func sectionType(
        for index: String.Index,
        in ranges: [(range: Range<String.Index>, sectionType: SectionType)]
    ) -> SectionType {
        for entry in ranges where entry.range.contains(index) {
            return entry.sectionType
        }
        return .operativeClauses
    }
}
