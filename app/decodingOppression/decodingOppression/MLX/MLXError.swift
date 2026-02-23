//
//  MLXError.swift
//  decodingOppression
//
//  MLX component error types.
//

import Foundation

enum MLXError: Error {
    /// Thrown when running on simulator (MLX unsupported).
    case simulatorNotSupported
    /// Thrown when ModelDownloadManager.state is not .available.
    case modelUnavailable
    /// Thrown when loadModel() has not been called yet.
    case modelNotLoaded
    /// Thrown when the bundled LoRA adapter cannot be located in the bundle.
    case adapterNotFound
}
