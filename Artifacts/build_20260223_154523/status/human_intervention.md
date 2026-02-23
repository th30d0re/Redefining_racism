# Human Intervention Required

## Summary
Build Agent failed after 5 repair attempts.

## Timestamp
2026-02-23T21:08:30Z

## Configuration
- Scheme: decodingOppression
- Configuration: Debug
- Target: id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19

## Input
I have the following verification comments after thorough review and exploration of the codebase. Implement the comments by following the instructions in the comments verbatim.

---
## Comment 1: HistoricalPolicyValidationTests.swift not compiled: test target Sources phase is empty so the suite never builds or runs

Open \`decodingOppression.xcodeproj/project.pbxproj\` and add \`HistoricalPolicyValidationTests.swift\` to the \`PBXSourcesBuildPhase\` of target \`decodingOppressionTests\` (ID \`1487AD9F2F47B280009460B8\`). Ensure the build phase \`files\` array includes the \`PBXBuildFile\` entry \`FF60718293A1B2C3D4E5F609\` that references \`HistoricalPolicyValidationTests.swift\`. Then verify the file is marked as a member of the \`decodingOppressionTests\` target in Xcode.

### Referred Files
- /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj/project.pbxproj
---
## Comment 2: Test resources missing from test bundle; Bundle(for:) will not find validation_clauses.jsonl

In \`decodingOppression.xcodeproj/project.pbxproj\`, add \`validation_clauses.jsonl\` (and any other fixtures it depends on) to the \`PBXResourcesBuildPhase\` of target \`decodingOppressionTests\` (ID \`1487ADA12F47B280009460B8\`). Ensure the \`files\` array references the existing \`PBXBuildFile\` for \`validation_clauses.jsonl\` or create one if missing. Confirm in Xcode that the file is included in the test target’s Copy Bundle Resources.

### Referred Files
- /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj/project.pbxproj
- /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppressionTests/HistoricalPolicyValidationTests.swift
---
## Comment 3: withKnownIssue used around async/throwing calls without await; this block will not compile

In \`decodingOppressionTests/HistoricalPolicyValidationTests.swift\`, remove the \`withKnownIssue\` wrapper or replace it with an async-aware pattern. For example, gate the entire test with an availability check and \`throw XCTSkip\`/\`issue.record\` semantics, or use \`await withKnownIssue(...) { ... }\` if using a variant that supports async. Ensure the async \`session.classifyClause\`, \`detectArchitecture\`, and \`detectProxy\` calls are awaited directly so the test compiles and executes.

### Referred Files
- /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppressionTests/HistoricalPolicyValidationTests.swift
---
## Comment 4: Training/validation datasets far smaller than planned stratified set, leaving T9 goals unmet

Expand \`decodingOppression/Data/historical_clauses.jsonl\` to at least the planned stratified counts (~40/10 Virginia Slave Codes, 24/6 13th Amendment, 32/8 HOLC, 24/6 War on Drugs). Populate \`decodingOppression/Data/validation_clauses.jsonl\` with the 20% held-out clauses corresponding to the full dataset. Keep schema consistent with \`TrainingClause\` and ensure IDs are unique.

### Referred Files
- /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Data/historical_clauses.jsonl
- /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Data/validation_clauses.jsonl
---
...

## Error History

### error_attempt_1.log
```
================================================================================
BUILD AGENT ERROR LOG
================================================================================
Timestamp: 2026-02-23T20:47:10Z
Exit Code: 10
Error: Xcode build failed
================================================================================

CONFIGURATION:
  Scheme: decodingOppression
  Configuration: Debug
  Destination: id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19
  Project: /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj
  Workspace: <not set>

FAILING COMMAND:
  xcodebuild -project "/Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj" -scheme "decodingOppression" -configuration "Debug" -destination "id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19" -skipMacroValidation build

ERROR DETAILS:
Command line invocation:
    /Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild -project /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj -scheme decodingOppression -configuration Debug -destination id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19 -skipMacroValidation build

Resolve Package Graph


Resolved source packages:
  swift-collections: https://github.com/apple/swift-collections.git @ 1.3.0
  swift-numerics: https://github.com/apple/swift-numerics @ 1.1.1
  mlx-swift: https://github.com/ml-explore/mlx-swift @ 0.29.1
  Jinja: https://github.com/huggingface/swift-jinja.git @ 2.3.2
  mlx-swift-lm: https://github.com/ml-explore/mlx-swift-lm @ 2.29.3
  swift-transformers: https://github.com/huggingface/swift-transformers @ 1.1.6

ComputePackagePrebuildTargetDependencyGraph

Prepare packages

CreateBuildRequest

SendProjectDescription

CreateBuildOperation

ComputeTargetDependencyGraph
note: Building targets in dependency order
note: Target dependency graph (37 targets)
    Target 'decodingOppression' in project 'decodingOppression'
        ➜ Explicit dependency on target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
    Target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
    Target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
    Target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Models' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Models' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'swift-transformers_Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'InternalCollectionsUtilities' in project 'swift-collections'
    Target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'InternalCollectionsUtilities' in project 'swift-collections'
    Target 'InternalCollectionsUtilities' in project 'swift-collections' (no dependencies)
    Target 'swift-transformers_Hub' in project 'swift-transformers' (no dependencies)
    Target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target 'ComplexModule' in project 'swift-numerics'
    Target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target 'ComplexModule' in project 'swift-numerics'
    Target 'ComplexModule' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
    Target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
    Target '_NumericsShims' in project 'swift-numerics' (no dependencies)
    Target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'mlx-swift_Cmlx' in project 'mlx-swift'
    Target 'mlx-swift_Cmlx' in project 'mlx-swift' (no dependencies)

GatherProvisioningInputs

CreateBuildDescription

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swiftc --version

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x objective-c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c++ -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld -version_details

ReadFileContents /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/share/docc/features.json

Build description signature: 73b15091628e28b95987efe9fe395b4e
Build description path: /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/XCBuildData/73b15091628e28b95987efe9fe395b4e.xcbuilddata
ClangStatCache /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang-stat-cache /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang-stat-cache /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle/Info.plist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/mlx-swift_Cmlx.build/empty-mlx-swift_Cmlx.plist (in target 'mlx-swift_Cmlx' from project 'mlx-swift')
    cd /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/mlx-swift
    builtin-infoPlistUtility /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/mlx-swift_Cmlx.build/empty-mlx-swift_Cmlx.plist -producttype com.apple.product-type.bundle -expandbuildsettings -format binary -platform iphonesimulator -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle/Info.plist

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle/Info.plist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/swift-transformers_Hub.build/empty-swift-transformers_Hub.plist (in target 'swift-transformers_Hub' from project 'swift-transformers')
    cd /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/swift-transformers
    builtin-infoPlistUtility /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/swift-transformers_Hub.build/empty-swift-transformers_Hub.plist -producttype com.apple.product-type.bundle -expandbuildsettings -format binary -platform iphonesimulator -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle/Info.plist

WriteAuxiliaryFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-generated-files.hmap (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    write-file /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-generated-files.hmap

WriteAuxiliaryFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.SwiftConstValuesFileList (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    write-file /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.SwiftConstValuesFileList

WriteAuxiliaryFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.SwiftFileList (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    write-file /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.SwiftFileList

WriteAuxiliaryFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.LinkFileList (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    write-file /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.LinkFileList

WriteAuxiliaryFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-OutputFileMap.json (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    write-file /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-OutputFileMap.json

ProcessProductPackaging "" /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    
    Entitlements:
    
    {
    "application-identifier" = "PSSP6VP63G.tech.eocon.decodingOppression";
}
    
    builtin-productPackagingUtility -entitlements -format xml -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent

ProcessProductPackagingDER /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent.der (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    /usr/bin/derq query -f xml -i /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent.der --raw

SwiftDriver decodingOppression normal arm64 com.apple.xcode.tools.swift.compiler (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-SwiftDriver -- /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swiftc -module-name decodingOppression -Onone -enforce-exclusivity\=checked @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.SwiftFileList -DDEBUG -default-isolation\=MainActor -enable-bare-slash-regex -enable-upcoming-feature DisableOutwardActorInference -enable-upcoming-feature InferSendableFromCaptures -enable-upcoming-feature GlobalActorIsolatedTypesUsability -enable-upcoming-feature MemberImportVisibility -enable-upcoming-feature InferIsolatedConformances -enable-upcoming-feature NonisolatedNonsendingByDefault -enable-experimental-feature DebugDescriptionMacro -sdk /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -target arm64-apple-ios26.2-simulator -g -module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex -Xfrontend -serialize-debugging-options -profile-coverage-mapping -profile-generate -enable-testing -index-store-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Index.noindex/DataStore -Xcc -D_LIBCPP_HARDENING_MODE\=_LIBCPP_HARDENING_MODE_DEBUG -swift-version 5 -I /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -emit-localized-strings -emit-localized-strings-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64 -c -j10 -enable-batch-mode -incremental -Xcc -ivfsstatcache -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache -output-file-map /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-OutputFileMap.json -use-frontend-parseable-output -save-temps -no-color-diagnostics -explicit-module-build -module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/SwiftExplicitPrecompiledModules -clang-scanner-module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex -sdk-module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex -serialize-diagnostics -emit-dependencies -emit-module -emit-module-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftmodule -validate-clang-modules-once -clang-build-session-file /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex/Session.modulevalidation -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/swift-overrides.hmap -emit-const-values -Xfrontend -const-gather-protocols-file -Xfrontend /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_const_extract_protocols.json -Xcc -iquote -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-generated-files.hmap -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-own-target-headers.hmap -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-all-non-framework-target-headers.hmap -Xcc -ivfsoverlay -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression-92f70843e4a2cfdead6817d9c21f0c6f-VFS-iphonesimulator/all-product-headers.yaml -Xcc -iquote -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-project-headers.hmap -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/swift-numerics/Sources/_NumericsShims/include -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/mlx-swift/Source/Cmlx/include -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/include -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources-normal/arm64 -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources/arm64 -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources -Xcc -DDEBUG\=1 -emit-objc-header -emit-objc-header-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-Swift.h -working-directory /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression -experimental-emit-module-separately -disable-cmo

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/Info.plist /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Info.plist (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-infoPlistUtility /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Info.plist -producttype com.apple.product-type.application -genpkginfo /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/PkgInfo -expandbuildsettings -format binary -platform iphonesimulator -scanforprivacyfile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/mlx-swift_Cmlx.bundle -scanforprivacyfile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/swift-transformers_Hub.bundle -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/Info.plist

SwiftEmitModule normal arm64 Emitting\ module\ for\ decodingOppression (in target 'decodingOppression' from project 'decodingOppression')

EmitSwiftModule normal arm64 (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 Compiling\ TrainingDataViewModel.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/ViewModels/TrainingDataViewModel.swift (in target 'decodingOppression' from project 'decodingOppression')
SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/ViewModels/TrainingDataViewModel.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 Compiling\ ValidationViewStyle.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/Style/ValidationViewStyle.swift (in target 'decodingOppression' from project 'decodingOppression')
SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/Style/ValidationViewStyle.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 Compiling\ ValidationRunner.swift,\ TrainingManager.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/AI/ValidationRunner.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/MLX/TrainingManager.swift (in target 'decodingOppression' from project 'decodingOppression')
SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/AI/ValidationRunner.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/MLX/TrainingManager.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 Compiling\ TrainingViewModel.swift,\ ValidationViewModel.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/ViewModels/TrainingViewModel.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/ViewModels/ValidationViewModel.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/ViewModels/TrainingViewModel.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/ViewModels/ValidationViewModel.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 Compiling\ TrainingView.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/TrainingView.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/TrainingView.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 Compiling\ TrainingModels.swift,\ TrainingDataStore.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Models/TrainingModels.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Data/TrainingDataStore.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Models/TrainingModels.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Data/TrainingDataStore.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 Compiling\ TrainingViewStyle.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/Style/TrainingViewStyle.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/Style/TrainingViewStyle.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 Compiling\ TrainingDataView.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/TrainingDataView.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/TrainingDataView.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 Compiling\ ValidationView.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/ValidationView.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/ValidationView.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftCompile normal arm64 Compiling\ TrainingDataViewStyle.swift /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/Style/TrainingDataViewStyle.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftCompile normal arm64 /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Views/Style/TrainingDataViewStyle.swift (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    

SwiftDriverJobDiscovery normal arm64 Emitting module for decodingOppression (in target 'decodingOppression' from project 'decodingOppression')

SwiftDriver\ Compilation\ Requirements decodingOppression normal arm64 com.apple.xcode.tools.swift.compiler (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-Swift-Compilation-Requirements -- /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swiftc -module-name decodingOppression -Onone -enforce-exclusivity\=checked @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.SwiftFileList -DDEBUG -default-isolation\=MainActor -enable-bare-slash-regex -enable-upcoming-feature DisableOutwardActorInference -enable-upcoming-feature InferSendableFromCaptures -enable-upcoming-feature GlobalActorIsolatedTypesUsability -enable-upcoming-feature MemberImportVisibility -enable-upcoming-feature InferIsolatedConformances -enable-upcoming-feature NonisolatedNonsendingByDefault -enable-experimental-feature DebugDescriptionMacro -sdk /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -target arm64-apple-ios26.2-simulator -g -module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex -Xfrontend -serialize-debugging-options -profile-coverage-mapping -profile-generate -enable-testing -index-store-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Index.noindex/DataStore -Xcc -D_LIBCPP_HARDENING_MODE\=_LIBCPP_HARDENING_MODE_DEBUG -swift-version 5 -I /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -emit-localized-strings -emit-localized-strings-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64 -c -j10 -enable-batch-mode -incremental -Xcc -ivfsstatcache -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache -output-file-map /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-OutputFileMap.json -use-frontend-parseable-output -save-temps -no-color-diagnostics -explicit-module-build -module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/SwiftExplicitPrecompiledModules -clang-scanner-module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex -sdk-module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex -serialize-diagnostics -emit-dependencies -emit-module -emit-module-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftmodule -validate-clang-modules-once -clang-build-session-file /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex/Session.modulevalidation -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/swift-overrides.hmap -emit-const-values -Xfrontend -const-gather-protocols-file -Xfrontend /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_const_extract_protocols.json -Xcc -iquote -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-generated-files.hmap -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-own-target-headers.hmap -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-all-non-framework-target-headers.hmap -Xcc -ivfsoverlay -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression-92f70843e4a2cfdead6817d9c21f0c6f-VFS-iphonesimulator/all-product-headers.yaml -Xcc -iquote -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-project-headers.hmap -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/swift-numerics/Sources/_NumericsShims/include -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/mlx-swift/Source/Cmlx/include -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/include -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources-normal/arm64 -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources/arm64 -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources -Xcc -DDEBUG\=1 -emit-objc-header -emit-objc-header-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-Swift.h -working-directory /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression -experimental-emit-module-separately -disable-cmo

SwiftDriverJobDiscovery normal arm64 Compiling TrainingViewStyle.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftDriverJobDiscovery normal arm64 Compiling TrainingDataView.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftDriverJobDiscovery normal arm64 Compiling TrainingDataViewModel.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftDriverJobDiscovery normal arm64 Compiling ValidationViewStyle.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftMergeGeneratedHeaders /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources/decodingOppression-Swift.h /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-Swift.h (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-swiftHeaderTool -arch arm64 /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-Swift.h -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources/decodingOppression-Swift.h

SwiftDriverJobDiscovery normal arm64 Compiling ValidationView.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftDriverJobDiscovery normal arm64 Compiling TrainingViewModel.swift, ValidationViewModel.swift (in target 'decodingOppression' from project 'decodingOppression')

Copy /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.swiftmodule/arm64-apple-ios-simulator.swiftdoc /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftdoc (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-copy -exclude .DS_Store -exclude CVS -exclude .svn -exclude .git -exclude .hg -resolve-src-symlinks -rename /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftdoc /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.swiftmodule/arm64-apple-ios-simulator.swiftdoc

Copy /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.swiftmodule/arm64-apple-ios-simulator.swiftmodule /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftmodule (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-copy -exclude .DS_Store -exclude CVS -exclude .svn -exclude .git -exclude .hg -resolve-src-symlinks -rename /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftmodule /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.swiftmodule/arm64-apple-ios-simulator.swiftmodule

Copy /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.swiftmodule/Project/arm64-apple-ios-simulator.swiftsourceinfo /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftsourceinfo (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-copy -exclude .DS_Store -exclude CVS -exclude .svn -exclude .git -exclude .hg -resolve-src-symlinks -rename /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftsourceinfo /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.swiftmodule/Project/arm64-apple-ios-simulator.swiftsourceinfo

Copy /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.swiftmodule/arm64-apple-ios-simulator.abi.json /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.abi.json (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-copy -exclude .DS_Store -exclude CVS -exclude .svn -exclude .git -exclude .hg -resolve-src-symlinks -rename /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.abi.json /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.swiftmodule/arm64-apple-ios-simulator.abi.json

SwiftDriverJobDiscovery normal arm64 Compiling TrainingView.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftDriverJobDiscovery normal arm64 Compiling TrainingModels.swift, TrainingDataStore.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftDriverJobDiscovery normal arm64 Compiling ValidationRunner.swift, TrainingManager.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftDriverJobDiscovery normal arm64 Compiling TrainingDataViewStyle.swift (in target 'decodingOppression' from project 'decodingOppression')

SwiftDriver\ Compilation decodingOppression normal arm64 com.apple.xcode.tools.swift.compiler (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-Swift-Compilation -- /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swiftc -module-name decodingOppression -Onone -enforce-exclusivity\=checked @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.SwiftFileList -DDEBUG -default-isolation\=MainActor -enable-bare-slash-regex -enable-upcoming-feature DisableOutwardActorInference -enable-upcoming-feature InferSendableFromCaptures -enable-upcoming-feature GlobalActorIsolatedTypesUsability -enable-upcoming-feature MemberImportVisibility -enable-upcoming-feature InferIsolatedConformances -enable-upcoming-feature NonisolatedNonsendingByDefault -enable-experimental-feature DebugDescriptionMacro -sdk /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -target arm64-apple-ios26.2-simulator -g -module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex -Xfrontend -serialize-debugging-options -profile-coverage-mapping -profile-generate -enable-testing -index-store-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Index.noindex/DataStore -Xcc -D_LIBCPP_HARDENING_MODE\=_LIBCPP_HARDENING_MODE_DEBUG -swift-version 5 -I /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -emit-localized-strings -emit-localized-strings-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64 -c -j10 -enable-batch-mode -incremental -Xcc -ivfsstatcache -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache -output-file-map /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-OutputFileMap.json -use-frontend-parseable-output -save-temps -no-color-diagnostics -explicit-module-build -module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/SwiftExplicitPrecompiledModules -clang-scanner-module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex -sdk-module-cache-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex -serialize-diagnostics -emit-dependencies -emit-module -emit-module-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftmodule -validate-clang-modules-once -clang-build-session-file /Users/emmanuel/Library/Developer/Xcode/DerivedData/ModuleCache.noindex/Session.modulevalidation -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/swift-overrides.hmap -emit-const-values -Xfrontend -const-gather-protocols-file -Xfrontend /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_const_extract_protocols.json -Xcc -iquote -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-generated-files.hmap -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-own-target-headers.hmap -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-all-non-framework-target-headers.hmap -Xcc -ivfsoverlay -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression-92f70843e4a2cfdead6817d9c21f0c6f-VFS-iphonesimulator/all-product-headers.yaml -Xcc -iquote -Xcc /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression-project-headers.hmap -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/swift-numerics/Sources/_NumericsShims/include -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/mlx-swift/Source/Cmlx/include -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/include -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources-normal/arm64 -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources/arm64 -Xcc -I/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources -Xcc -DDEBUG\=1 -emit-objc-header -emit-objc-header-path /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-Swift.h -working-directory /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression -experimental-emit-module-separately -disable-cmo

Ld /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib normal (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -Xlinker -reproducible -target arm64-apple-ios26.2-simulator -dynamiclib -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -O0 -L/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/EagerLinkingTBDs/Debug-iphonesimulator -L/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/EagerLinkingTBDs/Debug-iphonesimulator -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -filelist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.LinkFileList -install_name @rpath/decodingOppression.debug.dylib -Xlinker -rpath -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -Xlinker -rpath -Xlinker @executable_path/Frameworks -dead_strip -Xlinker -object_path_lto -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_lto.o -rdynamic -Xlinker -no_deduplicate -Xlinker -objc_abi_version -Xlinker 2 -Xlinker -debug_variant -Xlinker -dependency_info -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_dependency_info.dat -fobjc-link-runtime -fprofile-instr-generate -L/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/iphonesimulator -L/usr/lib/swift -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-linker-args.resp -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -lc++ -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -framework Foundation -framework Metal -framework Accelerate -Xlinker -alias -Xlinker _main -Xlinker ___debug_main_executable_dylib_entry_point -Xlinker -no_adhoc_codesign -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLLM.build/Objects-normal/arm64/MLXLLM.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLLM.build/Objects-normal/arm64/MLXLLM-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLX.build/Objects-normal/arm64/MLX.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLX.build/Objects-normal/arm64/MLX-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/Numerics.build/Objects-normal/arm64/Numerics.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/Numerics.build/Objects-normal/arm64/Numerics-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/RealModule.build/Objects-normal/arm64/RealModule.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/RealModule.build/Objects-normal/arm64/RealModule-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/ComplexModule.build/Objects-normal/arm64/ComplexModule.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/ComplexModule.build/Objects-normal/arm64/ComplexModule-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXNN.build/Objects-normal/arm64/MLXNN.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXNN.build/Objects-normal/arm64/MLXNN-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXRandom.build/Objects-normal/arm64/MLXRandom.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXRandom.build/Objects-normal/arm64/MLXRandom-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXFast.build/Objects-normal/arm64/MLXFast.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXFast.build/Objects-normal/arm64/MLXFast-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXOptimizers.build/Objects-normal/arm64/MLXOptimizers.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXOptimizers.build/Objects-normal/arm64/MLXOptimizers-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXLinalg.build/Objects-normal/arm64/MLXLinalg.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXLinalg.build/Objects-normal/arm64/MLXLinalg-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Tokenizers.build/Objects-normal/arm64/Tokenizers.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Tokenizers.build/Objects-normal/arm64/Tokenizers-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Generation.build/Objects-normal/arm64/Generation.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Generation.build/Objects-normal/arm64/Generation-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Models.build/Objects-normal/arm64/Models.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Models.build/Objects-normal/arm64/Models-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/Jinja.build/Debug-iphonesimulator/Jinja.build/Objects-normal/arm64/Jinja.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/Jinja.build/Debug-iphonesimulator/Jinja.build/Objects-normal/arm64/Jinja-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/OrderedCollections.build/Objects-normal/arm64/OrderedCollections.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/OrderedCollections.build/Objects-normal/arm64/OrderedCollections-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/InternalCollectionsUtilities.build/Objects-normal/arm64/InternalCollectionsUtilities.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/InternalCollectionsUtilities.build/Objects-normal/arm64/InternalCollectionsUtilities-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Hub.build/Objects-normal/arm64/Hub.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Hub.build/Objects-normal/arm64/Hub-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLMCommon.build/Objects-normal/arm64/MLXLMCommon.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLMCommon.build/Objects-normal/arm64/MLXLMCommon-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXEmbedders.build/Objects-normal/arm64/MLXEmbedders.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXEmbedders.build/Objects-normal/arm64/MLXEmbedders-linker-args.resp
ld: warning: Could not find or use auto-linked framework 'CoreAudioTypes': framework 'CoreAudioTypes' not found
Undefined symbols for architecture arm64:
  "_main", referenced from:
      ___debug_main_executable_dylib_entry_point in command-line-aliases-file
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources/GeneratedAssetSymbols-Index.plist'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources/GeneratedAssetSymbols.h'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/DerivedSources/GeneratedAssetSymbols.swift'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisPipeline.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisPipeline.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisPipeline.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalysisViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalyzedClause.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalyzedClause.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/AnalyzedClause.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureDetector.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureDetector.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureDetector.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureRadarView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureRadarView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureRadarView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureRadarViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureRadarViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureRadarViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureRadarViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureRadarViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ArchitectureRadarViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/BenefitHierarchyView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/BenefitHierarchyView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/BenefitHierarchyView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/BenefitHierarchyViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/BenefitHierarchyViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/BenefitHierarchyViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/BenefitHierarchyViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/BenefitHierarchyViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/BenefitHierarchyViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseAnalyzer.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseAnalyzer.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseAnalyzer.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseClassificationPipeline.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseClassificationPipeline.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseClassificationPipeline.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseListView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseListView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseListView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseListViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseListViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseListViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseListViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseListViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ClauseListViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingCalculator.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingCalculator.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingCalculator.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingTrajectoryView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingTrajectoryView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingTrajectoryView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingTrajectoryViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingTrajectoryViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingTrajectoryViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingTrajectoryViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingTrajectoryViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/CompoundingTrajectoryViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ContentView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ContentView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ContentView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/DifferentialImpactScorer.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/DifferentialImpactScorer.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/DifferentialImpactScorer.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestDetailView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestDetailView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestDetailView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestDetailViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestDetailViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestDetailViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestDetailViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestDetailViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestDetailViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestScorer.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestScorer.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/EliteInterestScorer.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ExportView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ExportView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ExportView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ExportViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ExportViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ExportViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ExportViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ExportViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ExportViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/GenerableTypes.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/GenerableTypes.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/GenerableTypes.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/GeneratedAssetSymbols.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/GeneratedAssetSymbols.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/GeneratedAssetSymbols.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalBaselineTool-408b15cfc1fbda0eb7fdd4244f249e7a.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalBaselineTool-408b15cfc1fbda0eb7fdd4244f249e7a.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalBaselineTool.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalComparisonView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalComparisonView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalComparisonView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalComparisonViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalComparisonViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalComparisonViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalComparisonViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalComparisonViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalComparisonViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalPolicies-8a958e2202a4fbe4f130a42dab2f9e53.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalPolicies-8a958e2202a4fbe4f130a42dab2f9e53.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/HistoricalPolicies.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/KeywordEngine.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/KeywordEngine.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/KeywordEngine.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/MLXClauseClassifier-f05220ca911fb28f07924587188d50b2.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/MLXClauseClassifier-f05220ca911fb28f07924587188d50b2.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/MLXClauseClassifier.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/MLXEmbeddingEngine-3287d1d5d48193b5cf8c56d351c007fd.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/MLXEmbeddingEngine-3287d1d5d48193b5cf8c56d351c007fd.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/MLXEmbeddingEngine.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/MLXError-b218d96e5d4a711b20ebc745f6ddc1c5.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/MLXError-b218d96e5d4a711b20ebc745f6ddc1c5.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/MLXError.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ModelDownloadManager-9d9292d3cf202cd0dd538f832aebd9a7.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ModelDownloadManager-9d9292d3cf202cd0dd538f832aebd9a7.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ModelDownloadManager.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupAnalyzer.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupAnalyzer.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupAnalyzer.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupExpansionView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupExpansionView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupExpansionView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupExpansionViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupExpansionViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupExpansionViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupExpansionViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupExpansionViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/OutgroupExpansionViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PDFExtractor.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PDFExtractor.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PDFExtractor.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PipelineContracts.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PipelineContracts.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PipelineContracts.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Policy.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Policy.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Policy.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyAnalysis.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyAnalysis.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyAnalysis.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyAnalysisSession-57ed1e6f1c8593b8b9262ca46e86930e.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyAnalysisSession-57ed1e6f1c8593b8b9262ca46e86930e.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyAnalysisSession.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyHistoryView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyHistoryView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyHistoryView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyHistoryViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyHistoryViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyHistoryViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyHistoryViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyHistoryViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyHistoryViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyScorer.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyScorer.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/PolicyScorer.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ReportExporter.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ReportExporter.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ReportExporter.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreCardView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreCardView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreCardView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreCardViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreCardViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreCardViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreCardViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreCardViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreCardViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreResult.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreResult.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/ScoreResult.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/TextPreprocessor.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/TextPreprocessor.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/TextPreprocessor.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier1Engine.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier1Engine.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier1Engine.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier2Engine-abe82b2ee2137f293b2cae425dd7aa7c.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier2Engine-abe82b2ee2137f293b2cae425dd7aa7c.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier2Engine.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier2EngineHolder-60e99d0514fdae213f8e8ea95a9d3171.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier2EngineHolder-60e99d0514fdae213f8e8ea95a9d3171.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier2EngineHolder.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier3Engine-f6821d35c7cbe3923d06e30fd493a6ed.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier3Engine-f6821d35c7cbe3923d06e30fd493a6ed.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier3Engine.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier3Error-22ed320e5c4d2eee6138ed6301cc26a1.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier3Error-22ed320e5c4d2eee6138ed6301cc26a1.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/Tier3Error.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/TierResolver.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/TierResolver.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/TierResolver.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/WelcomeView.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/WelcomeView.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/WelcomeView.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/WelcomeViewModel.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/WelcomeViewModel.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/WelcomeViewModel.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/WelcomeViewStyle.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/WelcomeViewStyle.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/WelcomeViewStyle.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppressionApp.o'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppressionApp.stringsdata'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppressionApp.swiftconstvalues'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/assetcatalog_dependencies_thinned'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/assetcatalog_generated_info.plist'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/assetcatalog_generated_info.plist_thinned'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/assetcatalog_output/thinned'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/assetcatalog_output/unthinned'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/assetcatalog_signature'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/KeywordTaxonomies.json'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/adapter_config.json'

note: Removed stale file '/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/adapters.safetensors'

note: Disabling hardened runtime with ad-hoc codesigning. (in target 'decodingOppression' from project 'decodingOppression')
** BUILD FAILED **


The following build commands failed:
	Ld /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib normal (in target 'decodingOppression' from project 'decodingOppression')
	Building project decodingOppression with scheme decodingOppression and configuration Debug
(2 failures)
================================================================================
```

### error_attempt_2.log
```
================================================================================
BUILD AGENT ERROR LOG
================================================================================
Timestamp: 2026-02-23T20:49:25Z
Exit Code: 10
Error: Xcode build failed
================================================================================

CONFIGURATION:
  Scheme: decodingOppression
  Configuration: Debug
  Destination: id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19
  Project: /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj
  Workspace: <not set>

FAILING COMMAND:
  xcodebuild -project "/Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj" -scheme "decodingOppression" -configuration "Debug" -destination "id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19" -skipMacroValidation build

ERROR DETAILS:
Command line invocation:
    /Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild -project /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj -scheme decodingOppression -configuration Debug -destination id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19 -skipMacroValidation build

Resolve Package Graph


Resolved source packages:
  swift-transformers: https://github.com/huggingface/swift-transformers @ 1.1.6
  Jinja: https://github.com/huggingface/swift-jinja.git @ 2.3.2
  mlx-swift: https://github.com/ml-explore/mlx-swift @ 0.29.1
  swift-numerics: https://github.com/apple/swift-numerics @ 1.1.1
  mlx-swift-lm: https://github.com/ml-explore/mlx-swift-lm @ 2.29.3
  swift-collections: https://github.com/apple/swift-collections.git @ 1.3.0

ComputePackagePrebuildTargetDependencyGraph

Prepare packages

CreateBuildRequest

SendProjectDescription

CreateBuildOperation

ComputeTargetDependencyGraph
note: Building targets in dependency order
note: Target dependency graph (37 targets)
    Target 'decodingOppression' in project 'decodingOppression'
        ➜ Explicit dependency on target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
    Target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
    Target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
    Target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Models' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Models' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'swift-transformers_Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'InternalCollectionsUtilities' in project 'swift-collections'
    Target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'InternalCollectionsUtilities' in project 'swift-collections'
    Target 'InternalCollectionsUtilities' in project 'swift-collections' (no dependencies)
    Target 'swift-transformers_Hub' in project 'swift-transformers' (no dependencies)
    Target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target 'ComplexModule' in project 'swift-numerics'
    Target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target 'ComplexModule' in project 'swift-numerics'
    Target 'ComplexModule' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
    Target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
    Target '_NumericsShims' in project 'swift-numerics' (no dependencies)
    Target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'mlx-swift_Cmlx' in project 'mlx-swift'
    Target 'mlx-swift_Cmlx' in project 'mlx-swift' (no dependencies)

GatherProvisioningInputs

CreateBuildDescription

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swiftc --version

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x objective-c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c++ -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld -version_details

ReadFileContents /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/share/docc/features.json

Build description signature: 61caf27d55a30f4b739e6103e625462e
Build description path: /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/XCBuildData/61caf27d55a30f4b739e6103e625462e.xcbuilddata
ClangStatCache /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang-stat-cache /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang-stat-cache /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle/Info.plist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/swift-transformers_Hub.build/empty-swift-transformers_Hub.plist (in target 'swift-transformers_Hub' from project 'swift-transformers')
    cd /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/swift-transformers
    builtin-infoPlistUtility /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/swift-transformers_Hub.build/empty-swift-transformers_Hub.plist -producttype com.apple.product-type.bundle -expandbuildsettings -format binary -platform iphonesimulator -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle/Info.plist

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle/Info.plist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/mlx-swift_Cmlx.build/empty-mlx-swift_Cmlx.plist (in target 'mlx-swift_Cmlx' from project 'mlx-swift')
    cd /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/mlx-swift
    builtin-infoPlistUtility /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/mlx-swift_Cmlx.build/empty-mlx-swift_Cmlx.plist -producttype com.apple.product-type.bundle -expandbuildsettings -format binary -platform iphonesimulator -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle/Info.plist

note: Disabling hardened runtime with ad-hoc codesigning. (in target 'decodingOppression' from project 'decodingOppression')
ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/Info.plist /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Info.plist (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-infoPlistUtility /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Info.plist -producttype com.apple.product-type.application -genpkginfo /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/PkgInfo -expandbuildsettings -format binary -platform iphonesimulator -scanforprivacyfile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/mlx-swift_Cmlx.bundle -scanforprivacyfile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/swift-transformers_Hub.bundle -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/Info.plist

Ld /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib normal (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -Xlinker -reproducible -target arm64-apple-ios26.2-simulator -dynamiclib -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -O0 -L/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/EagerLinkingTBDs/Debug-iphonesimulator -L/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/EagerLinkingTBDs/Debug-iphonesimulator -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -filelist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.LinkFileList -install_name @rpath/decodingOppression.debug.dylib -Xlinker -rpath -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -Xlinker -rpath -Xlinker @executable_path/Frameworks -dead_strip -Xlinker -object_path_lto -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_lto.o -rdynamic -Xlinker -no_deduplicate -Xlinker -objc_abi_version -Xlinker 2 -Xlinker -debug_variant -Xlinker -dependency_info -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_dependency_info.dat -fobjc-link-runtime -fprofile-instr-generate -L/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/iphonesimulator -L/usr/lib/swift -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-linker-args.resp -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -lc++ -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -framework Foundation -framework Metal -framework Accelerate -Xlinker -alias -Xlinker _main -Xlinker ___debug_main_executable_dylib_entry_point -Xlinker -no_adhoc_codesign -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLLM.build/Objects-normal/arm64/MLXLLM.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLLM.build/Objects-normal/arm64/MLXLLM-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLX.build/Objects-normal/arm64/MLX.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLX.build/Objects-normal/arm64/MLX-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/Numerics.build/Objects-normal/arm64/Numerics.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/Numerics.build/Objects-normal/arm64/Numerics-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/RealModule.build/Objects-normal/arm64/RealModule.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/RealModule.build/Objects-normal/arm64/RealModule-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/ComplexModule.build/Objects-normal/arm64/ComplexModule.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/ComplexModule.build/Objects-normal/arm64/ComplexModule-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXNN.build/Objects-normal/arm64/MLXNN.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXNN.build/Objects-normal/arm64/MLXNN-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXRandom.build/Objects-normal/arm64/MLXRandom.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXRandom.build/Objects-normal/arm64/MLXRandom-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXFast.build/Objects-normal/arm64/MLXFast.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXFast.build/Objects-normal/arm64/MLXFast-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXOptimizers.build/Objects-normal/arm64/MLXOptimizers.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXOptimizers.build/Objects-normal/arm64/MLXOptimizers-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXLinalg.build/Objects-normal/arm64/MLXLinalg.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXLinalg.build/Objects-normal/arm64/MLXLinalg-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Tokenizers.build/Objects-normal/arm64/Tokenizers.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Tokenizers.build/Objects-normal/arm64/Tokenizers-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Generation.build/Objects-normal/arm64/Generation.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Generation.build/Objects-normal/arm64/Generation-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Models.build/Objects-normal/arm64/Models.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Models.build/Objects-normal/arm64/Models-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/Jinja.build/Debug-iphonesimulator/Jinja.build/Objects-normal/arm64/Jinja.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/Jinja.build/Debug-iphonesimulator/Jinja.build/Objects-normal/arm64/Jinja-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/OrderedCollections.build/Objects-normal/arm64/OrderedCollections.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/OrderedCollections.build/Objects-normal/arm64/OrderedCollections-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/InternalCollectionsUtilities.build/Objects-normal/arm64/InternalCollectionsUtilities.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/InternalCollectionsUtilities.build/Objects-normal/arm64/InternalCollectionsUtilities-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Hub.build/Objects-normal/arm64/Hub.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Hub.build/Objects-normal/arm64/Hub-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLMCommon.build/Objects-normal/arm64/MLXLMCommon.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLMCommon.build/Objects-normal/arm64/MLXLMCommon-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXEmbedders.build/Objects-normal/arm64/MLXEmbedders.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXEmbedders.build/Objects-normal/arm64/MLXEmbedders-linker-args.resp
ld: warning: Could not find or use auto-linked framework 'CoreAudioTypes': framework 'CoreAudioTypes' not found
Undefined symbols for architecture arm64:
  "_main", referenced from:
      ___debug_main_executable_dylib_entry_point in command-line-aliases-file
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)

** BUILD FAILED **


The following build commands failed:
	Ld /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib normal (in target 'decodingOppression' from project 'decodingOppression')
	Building project decodingOppression with scheme decodingOppression and configuration Debug
(2 failures)
================================================================================
```

### error_attempt_3.log
```
================================================================================
BUILD AGENT ERROR LOG
================================================================================
Timestamp: 2026-02-23T20:59:28Z
Exit Code: 10
Error: Xcode build failed
================================================================================

CONFIGURATION:
  Scheme: decodingOppression
  Configuration: Debug
  Destination: id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19
  Project: /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj
  Workspace: <not set>

FAILING COMMAND:
  xcodebuild -project "/Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj" -scheme "decodingOppression" -configuration "Debug" -destination "id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19" -skipMacroValidation build

ERROR DETAILS:
Command line invocation:
    /Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild -project /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj -scheme decodingOppression -configuration Debug -destination id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19 -skipMacroValidation build

Resolve Package Graph


Resolved source packages:
  mlx-swift-lm: https://github.com/ml-explore/mlx-swift-lm @ 2.29.3
  mlx-swift: https://github.com/ml-explore/mlx-swift @ 0.29.1
  swift-numerics: https://github.com/apple/swift-numerics @ 1.1.1
  Jinja: https://github.com/huggingface/swift-jinja.git @ 2.3.2
  swift-transformers: https://github.com/huggingface/swift-transformers @ 1.1.6
  swift-collections: https://github.com/apple/swift-collections.git @ 1.3.0

ComputePackagePrebuildTargetDependencyGraph

Prepare packages

CreateBuildRequest

SendProjectDescription

CreateBuildOperation

ComputeTargetDependencyGraph
note: Building targets in dependency order
note: Target dependency graph (37 targets)
    Target 'decodingOppression' in project 'decodingOppression'
        ➜ Explicit dependency on target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
    Target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
    Target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
    Target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Models' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Models' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'swift-transformers_Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'InternalCollectionsUtilities' in project 'swift-collections'
    Target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'InternalCollectionsUtilities' in project 'swift-collections'
    Target 'InternalCollectionsUtilities' in project 'swift-collections' (no dependencies)
    Target 'swift-transformers_Hub' in project 'swift-transformers' (no dependencies)
    Target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target 'ComplexModule' in project 'swift-numerics'
    Target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target 'ComplexModule' in project 'swift-numerics'
    Target 'ComplexModule' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
    Target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
    Target '_NumericsShims' in project 'swift-numerics' (no dependencies)
    Target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'mlx-swift_Cmlx' in project 'mlx-swift'
    Target 'mlx-swift_Cmlx' in project 'mlx-swift' (no dependencies)

GatherProvisioningInputs

CreateBuildDescription

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swiftc --version

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x objective-c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c++ -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld -version_details

ReadFileContents /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/share/docc/features.json

Build description signature: 373648c9c40ed296d6b0052f255146d1
Build description path: /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/XCBuildData/373648c9c40ed296d6b0052f255146d1.xcbuilddata
ClangStatCache /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang-stat-cache /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang-stat-cache /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle/Info.plist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/mlx-swift_Cmlx.build/empty-mlx-swift_Cmlx.plist (in target 'mlx-swift_Cmlx' from project 'mlx-swift')
    cd /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/mlx-swift
    builtin-infoPlistUtility /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/mlx-swift_Cmlx.build/empty-mlx-swift_Cmlx.plist -producttype com.apple.product-type.bundle -expandbuildsettings -format binary -platform iphonesimulator -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle/Info.plist

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle/Info.plist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/swift-transformers_Hub.build/empty-swift-transformers_Hub.plist (in target 'swift-transformers_Hub' from project 'swift-transformers')
    cd /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/swift-transformers
    builtin-infoPlistUtility /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/swift-transformers_Hub.build/empty-swift-transformers_Hub.plist -producttype com.apple.product-type.bundle -expandbuildsettings -format binary -platform iphonesimulator -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle/Info.plist

note: Disabling hardened runtime with ad-hoc codesigning. (in target 'decodingOppression' from project 'decodingOppression')
ProcessProductPackaging "" /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    
    Entitlements:
    
    {
    "application-identifier" = "PSSP6VP63G.tech.eocon.decodingOppression";
}
    
    builtin-productPackagingUtility -entitlements -format xml -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent

ProcessProductPackagingDER /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent.der (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    /usr/bin/derq query -f xml -i /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent.der --raw

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/Info.plist /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Info.plist (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-infoPlistUtility /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Info.plist -producttype com.apple.product-type.application -genpkginfo /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/PkgInfo -expandbuildsettings -format binary -platform iphonesimulator -scanforprivacyfile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/mlx-swift_Cmlx.bundle -scanforprivacyfile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/swift-transformers_Hub.bundle -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/Info.plist

Ld /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib normal (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -Xlinker -reproducible -target arm64-apple-ios26.2-simulator -dynamiclib -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -O0 -L/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/EagerLinkingTBDs/Debug-iphonesimulator -L/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/EagerLinkingTBDs/Debug-iphonesimulator -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -filelist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.LinkFileList -install_name @rpath/decodingOppression.debug.dylib -Xlinker -rpath -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -Xlinker -rpath -Xlinker @executable_path/Frameworks -dead_strip -Xlinker -object_path_lto -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_lto.o -rdynamic -Xlinker -no_deduplicate -Xlinker -objc_abi_version -Xlinker 2 -Xlinker -debug_variant -Xlinker -dependency_info -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_dependency_info.dat -fobjc-link-runtime -fprofile-instr-generate -L/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/iphonesimulator -L/usr/lib/swift -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-linker-args.resp -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -lc++ -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -framework Foundation -framework Metal -framework Accelerate -Xlinker -alias -Xlinker _main -Xlinker ___debug_main_executable_dylib_entry_point -Xlinker -no_adhoc_codesign -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLLM.build/Objects-normal/arm64/MLXLLM.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLLM.build/Objects-normal/arm64/MLXLLM-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLX.build/Objects-normal/arm64/MLX.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLX.build/Objects-normal/arm64/MLX-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/Numerics.build/Objects-normal/arm64/Numerics.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/Numerics.build/Objects-normal/arm64/Numerics-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/RealModule.build/Objects-normal/arm64/RealModule.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/RealModule.build/Objects-normal/arm64/RealModule-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/ComplexModule.build/Objects-normal/arm64/ComplexModule.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/ComplexModule.build/Objects-normal/arm64/ComplexModule-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXNN.build/Objects-normal/arm64/MLXNN.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXNN.build/Objects-normal/arm64/MLXNN-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXRandom.build/Objects-normal/arm64/MLXRandom.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXRandom.build/Objects-normal/arm64/MLXRandom-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXFast.build/Objects-normal/arm64/MLXFast.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXFast.build/Objects-normal/arm64/MLXFast-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXOptimizers.build/Objects-normal/arm64/MLXOptimizers.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXOptimizers.build/Objects-normal/arm64/MLXOptimizers-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXLinalg.build/Objects-normal/arm64/MLXLinalg.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXLinalg.build/Objects-normal/arm64/MLXLinalg-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Tokenizers.build/Objects-normal/arm64/Tokenizers.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Tokenizers.build/Objects-normal/arm64/Tokenizers-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Generation.build/Objects-normal/arm64/Generation.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Generation.build/Objects-normal/arm64/Generation-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Models.build/Objects-normal/arm64/Models.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Models.build/Objects-normal/arm64/Models-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/Jinja.build/Debug-iphonesimulator/Jinja.build/Objects-normal/arm64/Jinja.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/Jinja.build/Debug-iphonesimulator/Jinja.build/Objects-normal/arm64/Jinja-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/OrderedCollections.build/Objects-normal/arm64/OrderedCollections.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/OrderedCollections.build/Objects-normal/arm64/OrderedCollections-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/InternalCollectionsUtilities.build/Objects-normal/arm64/InternalCollectionsUtilities.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/InternalCollectionsUtilities.build/Objects-normal/arm64/InternalCollectionsUtilities-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Hub.build/Objects-normal/arm64/Hub.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Hub.build/Objects-normal/arm64/Hub-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLMCommon.build/Objects-normal/arm64/MLXLMCommon.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLMCommon.build/Objects-normal/arm64/MLXLMCommon-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXEmbedders.build/Objects-normal/arm64/MLXEmbedders.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXEmbedders.build/Objects-normal/arm64/MLXEmbedders-linker-args.resp
ld: warning: Could not find or use auto-linked framework 'CoreAudioTypes': framework 'CoreAudioTypes' not found
Undefined symbols for architecture arm64:
  "_main", referenced from:
      ___debug_main_executable_dylib_entry_point in command-line-aliases-file
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)

** BUILD FAILED **


The following build commands failed:
	Ld /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib normal (in target 'decodingOppression' from project 'decodingOppression')
	Building project decodingOppression with scheme decodingOppression and configuration Debug
(2 failures)
================================================================================
```

### error_attempt_4.log
```
================================================================================
BUILD AGENT ERROR LOG
================================================================================
Timestamp: 2026-02-23T21:06:53Z
Exit Code: 10
Error: Xcode build failed
================================================================================

CONFIGURATION:
  Scheme: decodingOppression
  Configuration: Debug
  Destination: id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19
  Project: /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj
  Workspace: <not set>

FAILING COMMAND:
  xcodebuild -project "/Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj" -scheme "decodingOppression" -configuration "Debug" -destination "id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19" -skipMacroValidation build

ERROR DETAILS:
Command line invocation:
    /Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild -project /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj -scheme decodingOppression -configuration Debug -destination id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19 -skipMacroValidation build

Resolve Package Graph


Resolved source packages:
  mlx-swift-lm: https://github.com/ml-explore/mlx-swift-lm @ 2.29.3
  swift-transformers: https://github.com/huggingface/swift-transformers @ 1.1.6
  swift-numerics: https://github.com/apple/swift-numerics @ 1.1.1
  swift-collections: https://github.com/apple/swift-collections.git @ 1.3.0
  mlx-swift: https://github.com/ml-explore/mlx-swift @ 0.29.1
  Jinja: https://github.com/huggingface/swift-jinja.git @ 2.3.2

ComputePackagePrebuildTargetDependencyGraph

Prepare packages

CreateBuildRequest

SendProjectDescription

CreateBuildOperation

ComputeTargetDependencyGraph
note: Building targets in dependency order
note: Target dependency graph (37 targets)
    Target 'decodingOppression' in project 'decodingOppression'
        ➜ Explicit dependency on target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
    Target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
    Target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
    Target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Models' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Models' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'swift-transformers_Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'InternalCollectionsUtilities' in project 'swift-collections'
    Target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'InternalCollectionsUtilities' in project 'swift-collections'
    Target 'InternalCollectionsUtilities' in project 'swift-collections' (no dependencies)
    Target 'swift-transformers_Hub' in project 'swift-transformers' (no dependencies)
    Target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target 'ComplexModule' in project 'swift-numerics'
    Target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target 'ComplexModule' in project 'swift-numerics'
    Target 'ComplexModule' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
    Target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
    Target '_NumericsShims' in project 'swift-numerics' (no dependencies)
    Target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'mlx-swift_Cmlx' in project 'mlx-swift'
    Target 'mlx-swift_Cmlx' in project 'mlx-swift' (no dependencies)

GatherProvisioningInputs

CreateBuildDescription

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swiftc --version

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x objective-c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c++ -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld -version_details

ReadFileContents /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/share/docc/features.json

Build description signature: 2b60c091db20225a74c36a740b636f86
Build description path: /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/XCBuildData/2b60c091db20225a74c36a740b636f86.xcbuilddata
ClangStatCache /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang-stat-cache /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang-stat-cache /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle/Info.plist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/mlx-swift_Cmlx.build/empty-mlx-swift_Cmlx.plist (in target 'mlx-swift_Cmlx' from project 'mlx-swift')
    cd /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/mlx-swift
    builtin-infoPlistUtility /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/mlx-swift_Cmlx.build/empty-mlx-swift_Cmlx.plist -producttype com.apple.product-type.bundle -expandbuildsettings -format binary -platform iphonesimulator -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle/Info.plist

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle/Info.plist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/swift-transformers_Hub.build/empty-swift-transformers_Hub.plist (in target 'swift-transformers_Hub' from project 'swift-transformers')
    cd /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/swift-transformers
    builtin-infoPlistUtility /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/swift-transformers_Hub.build/empty-swift-transformers_Hub.plist -producttype com.apple.product-type.bundle -expandbuildsettings -format binary -platform iphonesimulator -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle/Info.plist

note: Disabling hardened runtime with ad-hoc codesigning. (in target 'decodingOppression' from project 'decodingOppression')
ProcessProductPackaging "" /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    
    Entitlements:
    
    {
    "application-identifier" = "PSSP6VP63G.tech.eocon.decodingOppression";
}
    
    builtin-productPackagingUtility -entitlements -format xml -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent

ProcessProductPackagingDER /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent.der (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    /usr/bin/derq query -f xml -i /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/decodingOppression.app-Simulated.xcent.der --raw

Copy /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/swift-transformers_Hub.bundle /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-copy -exclude .DS_Store -exclude CVS -exclude .svn -exclude .git -exclude .hg -resolve-src-symlinks /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app

Ld /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib normal (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -Xlinker -reproducible -target arm64-apple-ios26.2-simulator -dynamiclib -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -O0 -L/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/EagerLinkingTBDs/Debug-iphonesimulator -L/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/EagerLinkingTBDs/Debug-iphonesimulator -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -filelist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.LinkFileList -install_name @rpath/decodingOppression.debug.dylib -Xlinker -rpath -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -Xlinker -rpath -Xlinker @executable_path/Frameworks -dead_strip -Xlinker -object_path_lto -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_lto.o -rdynamic -Xlinker -no_deduplicate -Xlinker -objc_abi_version -Xlinker 2 -Xlinker -debug_variant -Xlinker -dependency_info -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_dependency_info.dat -fobjc-link-runtime -fprofile-instr-generate -L/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/iphonesimulator -L/usr/lib/swift -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-linker-args.resp -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -lc++ -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -framework Foundation -framework Metal -framework Accelerate -Xlinker -alias -Xlinker _main -Xlinker ___debug_main_executable_dylib_entry_point -Xlinker -no_adhoc_codesign -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLLM.build/Objects-normal/arm64/MLXLLM.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLLM.build/Objects-normal/arm64/MLXLLM-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLX.build/Objects-normal/arm64/MLX.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLX.build/Objects-normal/arm64/MLX-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/Numerics.build/Objects-normal/arm64/Numerics.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/Numerics.build/Objects-normal/arm64/Numerics-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/RealModule.build/Objects-normal/arm64/RealModule.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/RealModule.build/Objects-normal/arm64/RealModule-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/ComplexModule.build/Objects-normal/arm64/ComplexModule.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/ComplexModule.build/Objects-normal/arm64/ComplexModule-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXNN.build/Objects-normal/arm64/MLXNN.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXNN.build/Objects-normal/arm64/MLXNN-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXRandom.build/Objects-normal/arm64/MLXRandom.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXRandom.build/Objects-normal/arm64/MLXRandom-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXFast.build/Objects-normal/arm64/MLXFast.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXFast.build/Objects-normal/arm64/MLXFast-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXOptimizers.build/Objects-normal/arm64/MLXOptimizers.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXOptimizers.build/Objects-normal/arm64/MLXOptimizers-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXLinalg.build/Objects-normal/arm64/MLXLinalg.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXLinalg.build/Objects-normal/arm64/MLXLinalg-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Tokenizers.build/Objects-normal/arm64/Tokenizers.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Tokenizers.build/Objects-normal/arm64/Tokenizers-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Generation.build/Objects-normal/arm64/Generation.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Generation.build/Objects-normal/arm64/Generation-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Models.build/Objects-normal/arm64/Models.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Models.build/Objects-normal/arm64/Models-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/Jinja.build/Debug-iphonesimulator/Jinja.build/Objects-normal/arm64/Jinja.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/Jinja.build/Debug-iphonesimulator/Jinja.build/Objects-normal/arm64/Jinja-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/OrderedCollections.build/Objects-normal/arm64/OrderedCollections.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/OrderedCollections.build/Objects-normal/arm64/OrderedCollections-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/InternalCollectionsUtilities.build/Objects-normal/arm64/InternalCollectionsUtilities.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/InternalCollectionsUtilities.build/Objects-normal/arm64/InternalCollectionsUtilities-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Hub.build/Objects-normal/arm64/Hub.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Hub.build/Objects-normal/arm64/Hub-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLMCommon.build/Objects-normal/arm64/MLXLMCommon.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLMCommon.build/Objects-normal/arm64/MLXLMCommon-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXEmbedders.build/Objects-normal/arm64/MLXEmbedders.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXEmbedders.build/Objects-normal/arm64/MLXEmbedders-linker-args.resp
ld: warning: Could not find or use auto-linked framework 'CoreAudioTypes': framework 'CoreAudioTypes' not found
Undefined symbols for architecture arm64:
  "_main", referenced from:
      ___debug_main_executable_dylib_entry_point in command-line-aliases-file
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)

Copy /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/mlx-swift_Cmlx.bundle /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-copy -exclude .DS_Store -exclude CVS -exclude .svn -exclude .git -exclude .hg -resolve-src-symlinks /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/Info.plist /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Info.plist (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-infoPlistUtility /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Info.plist -producttype com.apple.product-type.application -genpkginfo /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/PkgInfo -expandbuildsettings -format binary -platform iphonesimulator -scanforprivacyfile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/mlx-swift_Cmlx.bundle -scanforprivacyfile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/swift-transformers_Hub.bundle -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/Info.plist

** BUILD FAILED **


The following build commands failed:
	Ld /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib normal (in target 'decodingOppression' from project 'decodingOppression')
	Building project decodingOppression with scheme decodingOppression and configuration Debug
(2 failures)
================================================================================
```

### error_attempt_5.log
```
================================================================================
BUILD AGENT ERROR LOG
================================================================================
Timestamp: 2026-02-23T21:08:30Z
Exit Code: 10
Error: Xcode build failed
================================================================================

CONFIGURATION:
  Scheme: decodingOppression
  Configuration: Debug
  Destination: id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19
  Project: /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj
  Workspace: <not set>

FAILING COMMAND:
  xcodebuild -project "/Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj" -scheme "decodingOppression" -configuration "Debug" -destination "id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19" -skipMacroValidation build

ERROR DETAILS:
Command line invocation:
    /Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild -project /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj -scheme decodingOppression -configuration Debug -destination id=91DB2C2E-AE60-410B-BDDF-03BAC36F9A19 -skipMacroValidation build

Resolve Package Graph


Resolved source packages:
  swift-transformers: https://github.com/huggingface/swift-transformers @ 1.1.6
  swift-numerics: https://github.com/apple/swift-numerics @ 1.1.1
  mlx-swift: https://github.com/ml-explore/mlx-swift @ 0.29.1
  Jinja: https://github.com/huggingface/swift-jinja.git @ 2.3.2
  swift-collections: https://github.com/apple/swift-collections.git @ 1.3.0
  mlx-swift-lm: https://github.com/ml-explore/mlx-swift-lm @ 2.29.3

ComputePackagePrebuildTargetDependencyGraph

Prepare packages

CreateBuildRequest

SendProjectDescription

CreateBuildOperation

ComputeTargetDependencyGraph
note: Building targets in dependency order
note: Target dependency graph (37 targets)
    Target 'decodingOppression' in project 'decodingOppression'
        ➜ Explicit dependency on target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
    Target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
    Target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXEmbedders' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXLLM' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
    Target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXLMCommon' in project 'mlx-swift-lm'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Transformers' in project 'swift-transformers'
    Target 'Transformers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Models' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Models' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Generation' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Tokenizers' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'swift-transformers_Hub' in project 'swift-transformers'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'Jinja' in project 'Jinja'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
    Target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'InternalCollectionsUtilities' in project 'swift-collections'
    Target 'OrderedCollections' in project 'swift-collections'
        ➜ Explicit dependency on target 'InternalCollectionsUtilities' in project 'swift-collections'
    Target 'InternalCollectionsUtilities' in project 'swift-collections' (no dependencies)
    Target 'swift-transformers_Hub' in project 'swift-transformers' (no dependencies)
    Target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXLinalg' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXOptimizers' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXNN' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXFast' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLXRandom' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'MLX' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
    Target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target 'ComplexModule' in project 'swift-numerics'
    Target 'Numerics' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target 'ComplexModule' in project 'swift-numerics'
    Target 'ComplexModule' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
        ➜ Explicit dependency on target 'RealModule' in project 'swift-numerics'
    Target 'RealModule' in project 'swift-numerics'
        ➜ Explicit dependency on target '_NumericsShims' in project 'swift-numerics'
    Target '_NumericsShims' in project 'swift-numerics' (no dependencies)
    Target 'Cmlx' in project 'mlx-swift'
        ➜ Explicit dependency on target 'mlx-swift_Cmlx' in project 'mlx-swift'
    Target 'mlx-swift_Cmlx' in project 'mlx-swift' (no dependencies)

GatherProvisioningInputs

CreateBuildDescription

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swiftc --version

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x objective-c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -x c++ -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld -version_details

ReadFileContents /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/share/docc/features.json

Build description signature: c8788297832861ae5c1ce459c8e8feb9
Build description path: /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/XCBuildData/c8788297832861ae5c1ce459c8e8feb9.xcbuilddata
ClangStatCache /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang-stat-cache /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression.xcodeproj
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang-stat-cache /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/SDKStatCaches.noindex/iphonesimulator26.2-23C57-e8867d0c40613ffc63e0238af232dc507d00a8b37fbd7999ea79df8ebc024bf0.sdkstatcache

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle/Info.plist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/swift-transformers_Hub.build/empty-swift-transformers_Hub.plist (in target 'swift-transformers_Hub' from project 'swift-transformers')
    cd /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/swift-transformers
    builtin-infoPlistUtility /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/swift-transformers_Hub.build/empty-swift-transformers_Hub.plist -producttype com.apple.product-type.bundle -expandbuildsettings -format binary -platform iphonesimulator -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/swift-transformers_Hub.bundle/Info.plist

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle/Info.plist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/mlx-swift_Cmlx.build/empty-mlx-swift_Cmlx.plist (in target 'mlx-swift_Cmlx' from project 'mlx-swift')
    cd /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/SourcePackages/checkouts/mlx-swift
    builtin-infoPlistUtility /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/mlx-swift_Cmlx.build/empty-mlx-swift_Cmlx.plist -producttype com.apple.product-type.bundle -expandbuildsettings -format binary -platform iphonesimulator -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/mlx-swift_Cmlx.bundle/Info.plist

note: Disabling hardened runtime with ad-hoc codesigning. (in target 'decodingOppression' from project 'decodingOppression')
Ld /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib normal (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -Xlinker -reproducible -target arm64-apple-ios26.2-simulator -dynamiclib -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.2.sdk -O0 -L/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/EagerLinkingTBDs/Debug-iphonesimulator -L/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/EagerLinkingTBDs/Debug-iphonesimulator -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -F/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator -filelist /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.LinkFileList -install_name @rpath/decodingOppression.debug.dylib -Xlinker -rpath -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/PackageFrameworks -Xlinker -rpath -Xlinker @executable_path/Frameworks -dead_strip -Xlinker -object_path_lto -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_lto.o -rdynamic -Xlinker -no_deduplicate -Xlinker -objc_abi_version -Xlinker 2 -Xlinker -debug_variant -Xlinker -dependency_info -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression_dependency_info.dat -fobjc-link-runtime -fprofile-instr-generate -L/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/iphonesimulator -L/usr/lib/swift -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/decodingOppression.build/Debug-iphonesimulator/decodingOppression.build/Objects-normal/arm64/decodingOppression-linker-args.resp -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -lc++ -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -Wl,-no_warn_duplicate_libraries -framework Foundation -framework Metal -framework Accelerate -Xlinker -alias -Xlinker _main -Xlinker ___debug_main_executable_dylib_entry_point -Xlinker -no_adhoc_codesign -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLLM.build/Objects-normal/arm64/MLXLLM.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLLM.build/Objects-normal/arm64/MLXLLM-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLX.build/Objects-normal/arm64/MLX.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLX.build/Objects-normal/arm64/MLX-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/Numerics.build/Objects-normal/arm64/Numerics.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/Numerics.build/Objects-normal/arm64/Numerics-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/RealModule.build/Objects-normal/arm64/RealModule.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/RealModule.build/Objects-normal/arm64/RealModule-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/ComplexModule.build/Objects-normal/arm64/ComplexModule.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-numerics.build/Debug-iphonesimulator/ComplexModule.build/Objects-normal/arm64/ComplexModule-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXNN.build/Objects-normal/arm64/MLXNN.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXNN.build/Objects-normal/arm64/MLXNN-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXRandom.build/Objects-normal/arm64/MLXRandom.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXRandom.build/Objects-normal/arm64/MLXRandom-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXFast.build/Objects-normal/arm64/MLXFast.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXFast.build/Objects-normal/arm64/MLXFast-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXOptimizers.build/Objects-normal/arm64/MLXOptimizers.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXOptimizers.build/Objects-normal/arm64/MLXOptimizers-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXLinalg.build/Objects-normal/arm64/MLXLinalg.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift.build/Debug-iphonesimulator/MLXLinalg.build/Objects-normal/arm64/MLXLinalg-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Tokenizers.build/Objects-normal/arm64/Tokenizers.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Tokenizers.build/Objects-normal/arm64/Tokenizers-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Generation.build/Objects-normal/arm64/Generation.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Generation.build/Objects-normal/arm64/Generation-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Models.build/Objects-normal/arm64/Models.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Models.build/Objects-normal/arm64/Models-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/Jinja.build/Debug-iphonesimulator/Jinja.build/Objects-normal/arm64/Jinja.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/Jinja.build/Debug-iphonesimulator/Jinja.build/Objects-normal/arm64/Jinja-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/OrderedCollections.build/Objects-normal/arm64/OrderedCollections.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/OrderedCollections.build/Objects-normal/arm64/OrderedCollections-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/InternalCollectionsUtilities.build/Objects-normal/arm64/InternalCollectionsUtilities.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-collections.build/Debug-iphonesimulator/InternalCollectionsUtilities.build/Objects-normal/arm64/InternalCollectionsUtilities-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Hub.build/Objects-normal/arm64/Hub.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/swift-transformers.build/Debug-iphonesimulator/Hub.build/Objects-normal/arm64/Hub-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLMCommon.build/Objects-normal/arm64/MLXLMCommon.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXLMCommon.build/Objects-normal/arm64/MLXLMCommon-linker-args.resp -Xlinker -add_ast_path -Xlinker /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXEmbedders.build/Objects-normal/arm64/MLXEmbedders.swiftmodule @/Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Intermediates.noindex/mlx-swift-lm.build/Debug-iphonesimulator/MLXEmbedders.build/Objects-normal/arm64/MLXEmbedders-linker-args.resp
ld: warning: Could not find or use auto-linked framework 'CoreAudioTypes': framework 'CoreAudioTypes' not found
Undefined symbols for architecture arm64:
  "_main", referenced from:
      ___debug_main_executable_dylib_entry_point in command-line-aliases-file
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)

ProcessInfoPlistFile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/Info.plist /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Info.plist (in target 'decodingOppression' from project 'decodingOppression')
    cd /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression
    builtin-infoPlistUtility /Users/emmanuel/Documents/Theory/Redefining_racism/app/decodingOppression/decodingOppression/Info.plist -producttype com.apple.product-type.application -genpkginfo /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/PkgInfo -expandbuildsettings -format binary -platform iphonesimulator -scanforprivacyfile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/mlx-swift_Cmlx.bundle -scanforprivacyfile /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/swift-transformers_Hub.bundle -o /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/Info.plist

** BUILD FAILED **


The following build commands failed:
	Ld /Users/emmanuel/Library/Developer/Xcode/DerivedData/decodingOppression-cxwoggwjsgwizbfojlfnncihejwm/Build/Products/Debug-iphonesimulator/decodingOppression.app/decodingOppression.debug.dylib normal (in target 'decodingOppression' from project 'decodingOppression')
	Building project decodingOppression with scheme decodingOppression and configuration Debug
(2 failures)
================================================================================
```


## Recommendations
1. Review the error logs above
2. Check for missing dependencies or configuration issues
3. Manually fix the problematic code
4. Re-run the build agent after fixes

## Artifacts Location
`/Users/emmanuel/Documents/Theory/Redefining_racism/Artifacts/build_20260223_154523/logs`

---
*Generated by BuildAgent - Phase 5*
