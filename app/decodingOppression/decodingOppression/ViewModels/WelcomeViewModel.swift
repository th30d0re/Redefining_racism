//
//  WelcomeViewModel.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import Foundation
import Observation

@Observable
@MainActor
final class WelcomeViewModel {
    var isDownloadStarted: Bool = false

    func getStarted(deps: AppDependencies, hasCompletedOnboarding: inout Bool) {
        if !isDownloadStarted {
            isDownloadStarted = true
            Task { await deps.startTier2Download() }
        }
        hasCompletedOnboarding = true
    }
}
