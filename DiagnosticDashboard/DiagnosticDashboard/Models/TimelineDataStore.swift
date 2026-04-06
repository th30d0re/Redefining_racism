import Foundation

enum TimelineDataStore {
    static let eras: [Era] = [
        // CHAPTER 2: Portugal
        Era(
            id: 2,
            version: "1.0",
            title: "Initializing the Vector",
            subtitle: "15th-Century Portugal",
            dateRange: "1452–1486",
            location: "LISBON, PORTUGAL",
            stressLevel: .high,
            stressDescription: "Domestic labor shortage threatening agricultural capital. Existing moral framework constrains exploitation of Christians.",
            capitalLevel: .stagnant,
            capitalDescription: "Sugar trade demands labor the current moral economy cannot supply.",
            activePatch: "Compiling Version 1.0...",
            variablesLoaded: [],
            variablesDeployed: [.E, .O_racialized, .I],
            executingFunction: "The Implicit Contract (Issuing the Psychological Wage).",
            policies: [
                PolicyEntry(name: "Dum Diversas", year: 1452, description: "Papal authorization for unlimited exploitation of non-Christians"),
                PolicyEntry(name: "Romanus Pontifex", year: 1455, description: "Grants Portugal monopoly on African slave trade"),
                PolicyEntry(name: "Casa dos Escravos", year: 1486, description: "State customs house institutionalizes managed extraction")
            ],
            result: "Extraction Algorithm initialized. Vector established.",
            warning: nil,
            outgroupExpansion: 0.15,
            bufferContraction: 1.0
        ),

        // CHAPTER 3: Bacon's Rebellion → Constitution
        Era(
            id: 3,
            version: "2.0",
            title: "Emergency Patch",
            subtitle: "Bacon's Rebellion → Constitutional Convention",
            dateRange: "1676–1787",
            location: "VIRGINIA COLONY → PHILADELPHIA",
            stressLevel: .critical,
            stressDescription: "Cross-racial labor solidarity detected. Jamestown burning.",
            capitalLevel: .atRisk,
            capitalDescription: "Plantation economy destabilized by unified revolt.",
            activePatch: "Emergency recompile. Partitioning the poor...",
            variablesLoaded: [.E, .O_racialized, .I],
            variablesDeployed: [.I_buffer, .F_enforce_proto, .P_uppet, .psi],
            executingFunction: "Codify \"Whiteness.\" Weaponize the Implicit Contract into explicit law. Draft constitutional front-end.",
            policies: [
                PolicyEntry(name: "Virginia Slave Codes", year: 1705, description: "Partition working class; deputize I_buffer as racial enforcers"),
                PolicyEntry(name: "Three-Fifths Compromise", year: 1787, description: "Embed extraction into federal architecture"),
                PolicyEntry(name: "Constitutional Convention", year: 1787, description: "Prototype Puppet Class; front-end/back-end separation")
            ],
            result: "Working class partitioned. Constitutional front-end deployed. min variable temporarily stabilized.",
            warning: nil,
            outgroupExpansion: 0.2,
            bufferContraction: 0.95
        ),

        // CHAPTER 4: Enforcement Engine
        Era(
            id: 4,
            version: "3.0",
            title: "The Enforcement Engine",
            subtitle: "Slave Patrols → 13th Amendment",
            dateRange: "1704–1865",
            location: "AMERICAN SOUTH",
            stressLevel: .moderate,
            stressDescription: "Buffer Class pacified by \u{03C8}. Racial partition holding. Physical enforcement of extraction requires dedicated apparatus.",
            capitalLevel: .expanding,
            capitalDescription: "Slave capitalism scaling. Human bodies classified as mortgageable assets. Cotton economy driving global markets.",
            activePatch: "Deploying dedicated enforcement tier...",
            variablesLoaded: [.E, .O_racialized, .I, .I_buffer, .P_uppet],
            variablesDeployed: [.F_enforce, .QI],
            executingFunction: "Deploy physical enforcement tier. Convert slave patrols into permanent state apparatus. Embed extraction loophole into 13th Amendment.",
            policies: [
                PolicyEntry(name: "Fugitive Slave Act", year: 1850, description: "Merges Northern/Southern enforcement tracks"),
                PolicyEntry(name: "13th Amendment", year: 1865, description: "Loophole: O_incarcerated → forced labor. Extraction survives abolition")
            ],
            result: "Four-tier hierarchy operational. Extraction survives abolition via carceral loophole. max secured indefinitely.",
            warning: nil,
            outgroupExpansion: 0.25,
            bufferContraction: 0.9
        ),

        // CHAPTER 5: Containment
        Era(
            id: 5,
            version: "4.0",
            title: "The Containment",
            subtitle: "Reconstruction → Civil Rights Era",
            dateRange: "1870s–1960s",
            location: "RECONSTRUCTION → CIVIL RIGHTS ERA",
            stressLevel: .high,
            stressDescription: "13th Amendment reclassified O as citizens with voting rights. Demographic pressure building. Civil Rights Movement breaching the interface.",
            capitalLevel: .restructuring,
            capitalDescription: "Direct slavery terminated. System transitioning to indirect extraction via convict leasing, sharecropping, and spatial containment.",
            activePatch: "Building containment field. Scaling Puppet Class...",
            variablesLoaded: [.E, .O_racialized, .I, .I_buffer, .F_enforce],
            variablesDeployed: [.P_uppet, .P_spatial],
            executingFunction: "Build containment field (Redlining). Scale Puppet Class into two-party front-end. Execute voter capture of O to neutralize Civil Rights gains.",
            policies: [
                PolicyEntry(name: "National Housing Act / HOLC Redlining", year: 1934, description: "Concentrates O for targeted extraction"),
                PolicyEntry(name: "Civil Rights Act", year: 1964, description: "Dismantles legal interface — but not the kernel"),
                PolicyEntry(name: "Voting Rights Act", year: 1965, description: "Capture Variable absorbs O into two-party system")
            ],
            result: "Five-tier hierarchy complete. Democratic interface fully operational. min restored through spatial and political containment.",
            warning: nil,
            outgroupExpansion: 0.3,
            bufferContraction: 0.85
        ),

        // CHAPTER 6: Complete Algorithm
        Era(
            id: 6,
            version: "5.0",
            title: "The Complete Algorithm",
            subtitle: "War on Drugs → Cannibalization",
            dateRange: "1968–Present",
            location: "NATIONAL",
            stressLevel: .critical,
            stressDescription: "Civil Rights Movement breached the legal interface. Demographic Paradox emerging: O shrinking, extraction demand unchanged.",
            capitalLevel: .peak,
            capitalDescription: "Carceral state fully industrialized. 13th Amendment loophole generating maximum throughput. War on Drugs providing unlimited proxy criminalization.",
            activePatch: "Full algorithm running. Variable Swap masking racial targeting...",
            variablesLoaded: [.E, .P_uppet, .F_enforce, .I_buffer, .O_racialized],
            variablesDeployed: [.P_criminal, .P_spatial, .P_retroactive],
            executingFunction: "Demographic deficit forcing cannibalization of I_buffer. Universal Latent Criminality deployed.",
            policies: [
                PolicyEntry(name: "Anti-Drug Abuse Act", year: 1986, description: "100:1 crack/powder ratio"),
                PolicyEntry(name: "Three Strikes Laws", year: 1994, description: "Mandatory sentencing expansion"),
                PolicyEntry(name: "Assault Weapon Bans", year: 1994, description: "Spatial proxy / hardware restriction"),
                PolicyEntry(name: "NFA Tax Increases", year: 2026, description: "$4,709 transfer tax proposal"),
                PolicyEntry(name: "Sensitive Place Expansions", year: 2022, description: "Post-Bruen spatial felony traps")
            ],
            result: "All proxy variables deployed. I_buffer being consumed. O expanding beyond O_racialized.",
            warning: "min VARIABLE FAILING. Buffer Class detecting contract breach. Kinetic calculus unfavorable. System entering terminal phase.",
            outgroupExpansion: 0.7,
            bufferContraction: 0.5
        ),

        // CHAPTER 7: Policy Implications
        Era(
            id: 7,
            version: "5.1",
            title: "Diagnostic Complete",
            subtitle: "Compiling Prescriptions",
            dateRange: "PRESENT",
            location: "DIAGNOSTIC MODE",
            stressLevel: .failing,
            stressDescription: "I_buffer awakening to contract breach. Kinetic capacity of civilian population exceeds F_enforce. Cross-racial solidarity vectors reappearing.",
            capitalLevel: .terminal,
            capitalDescription: "Extraction zone expanded beyond O into I_buffer. Opioid crisis, affordability trap, and universal latent criminality consuming the system's own defenders.",
            activePatch: "Switching from diagnostic to prescriptive mode...",
            variablesLoaded: [.E, .P_uppet, .F_enforce, .I_buffer, .O_racialized, .psi, .QI, .P_criminal, .P_spatial, .P_retroactive],
            variablesDeployed: [],
            executingFunction: "Identify interventions targeting the kernel (Predatory Min-Max Function), not merely the interface.",
            policies: [],
            result: "Algorithm fully mapped. Prescriptions targeting kernel compiled.",
            warning: nil,
            outgroupExpansion: 0.85,
            bufferContraction: 0.3
        ),

        // CHAPTER 8: Discussion
        Era(
            id: 8,
            version: "5.2",
            title: "Post-Diagnostic Analysis",
            subtitle: "Framework Evaluation",
            dateRange: "ANALYSIS",
            location: "POST-DIAGNOSTIC",
            stressLevel: .high,
            stressDescription: "Historically variable. Each system crash (Bacon's Rebellion, Civil War, Civil Rights) temporarily spiked min, forcing emergency patches.",
            capitalLevel: .expanding,
            capitalDescription: "Monotonically increasing across five centuries. Interface changes; kernel persists.",
            activePatch: "Evaluating framework against counter-arguments...",
            variablesLoaded: [.E, .P_uppet, .F_enforce, .I_buffer, .O_racialized, .psi, .QI, .P_criminal, .P_spatial, .P_retroactive],
            variablesDeployed: [],
            executingFunction: "Testing model against counter-arguments and boundary conditions.",
            policies: [],
            result: "Framework validated. Counter-arguments resolved within model parameters.",
            warning: nil,
            outgroupExpansion: 0.85,
            bufferContraction: 0.3
        ),

        // CHAPTER 9: Conclusion
        Era(
            id: 9,
            version: "FINAL",
            title: "Final Output",
            subtitle: "return R_acism",
            dateRange: "OUTPUT",
            location: "TERMINAL",
            stressLevel: .failing,
            stressDescription: "Most reforms targeted the interface; the kernel recompiled. Civil rights legal strategy did breach the kernel — but the system adapted. Only source-code attacks work at scale.",
            capitalLevel: .terminal,
            capitalDescription: "Algorithm continues to extract. O expands. I_buffer shrinks. O_racialized remains at the bottom of a growing extraction pool.",
            activePatch: "Consolidating revised definition...",
            variablesLoaded: [.E, .P_uppet, .F_enforce, .I_buffer, .O_racialized, .psi, .QI, .P_criminal, .P_spatial, .P_retroactive],
            variablesDeployed: [],
            executingFunction: "Outputting the vector equation of racism.",
            policies: [],
            result: "Target the kernel. Forget the interface. Remove d_state and the vector collapses to a scalar: prejudice without power.",
            warning: "return R_acism = M_agnitude * d_state",
            outgroupExpansion: 0.95,
            bufferContraction: 0.15
        )
    ]
}
