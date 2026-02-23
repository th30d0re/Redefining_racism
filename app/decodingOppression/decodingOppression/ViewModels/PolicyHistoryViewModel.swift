//
//  PolicyHistoryViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation
import SwiftData

@Observable
@MainActor
final class PolicyHistoryViewModel {
    var isShowingFilePicker: Bool = false
    var selectedAnalysis: PolicyAnalysis?

    func delete(_ analysis: PolicyAnalysis, context: ModelContext) {
        context.delete(analysis)
    }
}
