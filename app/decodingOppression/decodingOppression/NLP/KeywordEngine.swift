//
//  KeywordEngine.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/22/26.
//

import Foundation
import NaturalLanguage

nonisolated struct KeywordFeatureVector: Sendable {
    let outgroupBurdenScore: Double
    let ingroupBenefitScore: Double
    let eliteExtractionScore: Double
    let proxyTermsFound: [String]
    let confidence: Double
}

actor KeywordEngine {
    private struct KeywordTaxonomies: Decodable {
        let outgroupBurden: [String]
        let ingroupBenefit: [String]
        let eliteExtraction: [String]
        let dogWhistleProxies: [String]
    }

    enum KeywordEngineError: Error {
        case missingTaxonomies
        case decodingFailed(Error)
    }

    private let taxonomies: KeywordTaxonomies
    private let embedding: NLEmbedding?
    private let gazetteer: NLGazetteer

    init() throws {
        let bundle = Bundle.main
        let url = bundle.url(forResource: "KeywordTaxonomies", withExtension: "json")
            ?? bundle.url(forResource: "KeywordTaxonomies", withExtension: "json", subdirectory: "Data")

        guard let url else {
            throw KeywordEngineError.missingTaxonomies
        }

        do {
            let data = try Data(contentsOf: url)
            self.taxonomies = try JSONDecoder().decode(KeywordTaxonomies.self, from: data)
        } catch {
            throw KeywordEngineError.decodingFailed(error)
        }

        self.gazetteer = try NLGazetteer(
            dictionary: ["proxy": taxonomies.dogWhistleProxies],
            language: .english
        )
        self.embedding = NLEmbedding.wordEmbedding(for: .english)
    }

    func analyze(clause: Clause) -> KeywordFeatureVector {
        let tagger = NLTagger(tagSchemes: [.lemma, .nameType, .lexicalClass])
        tagger.string = clause.text
        tagger.setGazetteers([gazetteer], for: .nameType)

        var outgroupTokenScores: [Double] = []
        var ingroupTokenScores: [Double] = []
        var eliteTokenScores: [Double] = []
        var proxyTerms: [String] = []

        let text = clause.text
        let options: NLTagger.Options = [.omitWhitespace, .omitPunctuation]

        tagger.enumerateTags(in: text.startIndex..<text.endIndex, unit: .word, scheme: .lexicalClass, options: options) { _, tokenRange in
            let token = String(text[tokenRange])
            let (lemmaTag, _) = tagger.tag(at: tokenRange.lowerBound, unit: .word, scheme: .lemma)
            let lemma = lemmaTag?.rawValue ?? token

            let (nameTag, _) = tagger.tag(at: tokenRange.lowerBound, unit: .word, scheme: .nameType)
            if nameTag?.rawValue == "proxy" {
                proxyTerms.append(token)
            }

            outgroupTokenScores.append(bestSimilarity(for: lemma, terms: taxonomies.outgroupBurden))
            ingroupTokenScores.append(bestSimilarity(for: lemma, terms: taxonomies.ingroupBenefit))
            eliteTokenScores.append(bestSimilarity(for: lemma, terms: taxonomies.eliteExtraction))

            return true
        }

        let outgroupScore = averageTop3(outgroupTokenScores)
        let ingroupScore = averageTop3(ingroupTokenScores)
        let eliteScore = averageTop3(eliteTokenScores)

        let sortedScores = [outgroupScore, ingroupScore, eliteScore].sorted(by: >)
        let topScore = sortedScores.first ?? 0
        let secondScore = sortedScores.dropFirst().first ?? 0
        let separationGap = max(0, topScore - secondScore)
        let confidence = min(0.95, topScore + 0.15 * separationGap)

        return KeywordFeatureVector(
            outgroupBurdenScore: outgroupScore,
            ingroupBenefitScore: ingroupScore,
            eliteExtractionScore: eliteScore,
            proxyTermsFound: proxyTerms,
            confidence: confidence
        )
    }

    private func bestSimilarity(for lemma: String, terms: [String]) -> Double {
        guard let embedding else { return 0 }
        guard embedding.contains(lemma) else { return 0 }

        var best: Double = 0
        for term in terms {
            guard embedding.contains(term) else { continue }
            let distance = embedding.distance(between: lemma, and: term, distanceType: .cosine)
            let similarity = max(0, 1 - distance)
            if similarity > best {
                best = similarity
            }
        }
        return best
    }

    private func averageTop3(_ scores: [Double]) -> Double {
        let topScores = scores.sorted(by: >).prefix(3)
        guard !topScores.isEmpty else { return 0 }
        let sum = topScores.reduce(0, +)
        return sum / Double(topScores.count)
    }
}
