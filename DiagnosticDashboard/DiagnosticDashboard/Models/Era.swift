import Foundation

struct PolicyEntry: Identifiable {
    let id = UUID()
    let name: String
    let year: Int
    let description: String
}

struct Era: Identifiable {
    let id: Int
    let version: String
    let title: String
    let subtitle: String
    let dateRange: String
    let location: String

    let stressLevel: StressLevel
    let stressDescription: String
    let capitalLevel: CapitalLevel
    let capitalDescription: String

    let activePatch: String
    let variablesLoaded: [SystemVariable]
    let variablesDeployed: [SystemVariable]
    let executingFunction: String
    let policies: [PolicyEntry]
    let result: String
    let warning: String?

    // Graph data points (normalized 0.0...1.0)
    let outgroupExpansion: Double
    let bufferContraction: Double
}
