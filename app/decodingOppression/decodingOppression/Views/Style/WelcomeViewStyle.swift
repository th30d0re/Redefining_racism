//
//  WelcomeViewStyle.swift
//  decodingOppression
//
//  Created by Emmanuel Theodore on 2/23/26.
//

import SwiftUI

struct WelcomeViewStyle {
    let reduceMotion: Bool
    let dynamicTypeSize: DynamicTypeSize

    static func progressAnimation(reduceMotion: Bool) -> Animation? {
        reduceMotion ? nil : .easeInOut(duration: 0.4)
    }
}
