//
//  MLXEmbeddingEngine.swift
//  decodingOppression
//
//  Actor that loads BGE small embedder and provides similarity for taxonomy matching.
//

import Foundation
#if !targetEnvironment(simulator)
import MLX
import MLXEmbedders
import Tokenizers
#endif

actor MLXEmbeddingEngine {
#if !targetEnvironment(simulator)
    private var modelContainer: ModelContainer?

    func loadModel() async throws {
        if modelContainer != nil { return }
        modelContainer = try await loadModelContainer(
            configuration: .init(id: "mlx-community/bge-small-en-v1.5")
        )
    }

    func embed(_ text: String) async throws -> [Float] {
        guard let modelContainer else { throw MLXError.modelNotLoaded }
        return await modelContainer.perform { model, tokenizer, pooler in
            let tokens = tokenizer.encode(text: text, addSpecialTokens: true)
            let padId = tokenizer.eosTokenId ?? 0
            let maxLength = max(tokens.count, 1)
            let padded = tokens + Array(repeating: padId, count: maxLength - tokens.count)
            let input = MLXArray(padded)
            let inputs = stacked([input])
            let mask = (inputs .!= padId)
            let tokenTypes = MLXArray.zeros(like: inputs)
            let output = model(inputs, positionIds: nil, tokenTypeIds: tokenTypes, attentionMask: mask)
            let pooled = pooler(output, mask: mask, normalize: true, applyLayerNorm: true)
            pooled.eval()
            if pooled.shape.count == 2 {
                return pooled[0].asArray(Float.self)
            }
            return pooled.asArray(Float.self)
        }
    }

    nonisolated func cosineSimilarity(_ a: [Float], _ b: [Float]) -> Double {
        guard !a.isEmpty, !b.isEmpty, a.count == b.count else { return 0 }
        let dot = zip(a, b).reduce(0.0) { $0 + Double($1.0 * $1.1) }
        let na = sqrt(zip(a, a).reduce(0.0) { $0 + Double($1.0 * $1.1) })
        let nb = sqrt(zip(b, b).reduce(0.0) { $0 + Double($1.0 * $1.1) })
        guard na > 0, nb > 0 else { return 0 }
        return dot / (na * nb)
    }

    func similarity(clause: String, taxonomyTerm: String) async throws -> Double {
        let a = try await embed(clause)
        let b = try await embed(taxonomyTerm)
        return cosineSimilarity(a, b)
    }
#else
    func loadModel() async throws {
        throw MLXError.simulatorNotSupported
    }

    func embed(_ text: String) async throws -> [Float] {
        throw MLXError.simulatorNotSupported
    }

    nonisolated func cosineSimilarity(_ a: [Float], _ b: [Float]) -> Double {
        0
    }

    func similarity(clause: String, taxonomyTerm: String) async throws -> Double {
        throw MLXError.simulatorNotSupported
    }
#endif
}
