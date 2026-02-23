# Session Log - 2025-02-22 Tier3 AI Implementation

## What Was Wrong / What Was Requested

Implement a new `AI/` group in the decodingOppression Xcode target with five files: `Tier3Error`, `HistoricalPolicies`, `HistoricalBaselineTool`, `PolicyAnalysisSession`, and `Tier3Engine`. All gated behind `#if canImport(FoundationModels)` with stub fallbacks where needed. Tier3Engine mirrors Tier2Engine's public actor interface for TierResolver (T5). Register the new files in project.pbxproj.

## How I Fixed It / What I Did

1. Created `AI/Tier3Error.swift` with enum cases: unavailable, safetyGuardrail, contextWindowExceeded, sessionFailed(Error).
2. Created `AI/HistoricalPolicies.swift` with static `score(for policyName:)` returning COI for four ground-truth policies; 0.0 for unknown.
3. Created `AI/HistoricalBaselineTool.swift` (FoundationModels-gated) implementing `Tool` with `getHistoricalBaseline`, `Arguments` with `@Guide(.anyOf([...]))`, and `call(arguments:)` delegating to HistoricalPolicies.
4. Created `AI/PolicyAnalysisSession.swift` (FoundationModels-gated) actor with academic framing prefix, `classifyClause`, `detectArchitecture`, `detectProxy`, and `streamArchitecture`; session-per-call and error handling for context window (retry with truncated text) and safety guardrail (log and rethrow).
5. Created `AI/Tier3Engine.swift` with availability check via `SystemLanguageModel.default.availability`, `isAvailable()`, `classify(clause:)` (async let for three session calls, map to TierClassification, return nil on Tier3Error.unavailable/safetyGuardrail), and `streamClassify(clause:)`; stub `#else` throwing Tier3Error.unavailable.
6. Added `ArchitectureDetection.PartiallyGenerated` stub in GenerableTypes.swift `#else` for Tier3Engine stream return type when FoundationModels is unavailable.
7. Registered all five AI files in project.pbxproj (PBXFileSystemSynchronizedBuildFileExceptionSet membershipExceptions).

## Challenges Encountered

1. Project uses PBXFileSystemSynchronizedRootGroup; new files added via membershipExceptions rather than legacy PBXFileReference/PBXSourcesBuildPhase.
2. PipelineContracts.TierClassification and Policy.swift define TargetGroup, EffectDirection, MLTier; GenerableTypes defines ClauseClassification.TargetGroup/EffectDirection and ArchitectureDetection/ProxyDetection; mapping from Generable types to pipeline types required rawValue bridging.
3. FoundationModels API names (LanguageModelSession, SystemLanguageModel, Tool, GenerationError.exceededContextWindowSize) assumed from plan; PartiallyGenerated for streaming assumed on ArchitectureDetection.

## Next Ideas (6 Ideas)

1. Add unit tests for HistoricalPolicies.score(for:) and Tier3Engine stub behaviour when FoundationModels unavailable.
2. Add TierResolver (T5) integration that calls Tier3Engine.classify and falls back to Tier2 when nil.
3. ValidationRunner (T8/T9) consuming HistoricalPolicies for expected COI comparison.
4. Replace print() for safety guardrail logging with a proper logging or telemetry hook.
5. Consider sharing one LanguageModelSession across multiple short clauses if token budget allows, to reduce session churn.
6. Document FoundationModels SDK version and availability requirements in README or Docs.
