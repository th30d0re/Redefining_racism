export interface TimelineEvent {
  year: number;
  event: string;
  outgroup: string[];
}

export interface VennDiagramData {
  inGroup: { label: string; members: string[] };
  outGroup: { label: string; members: string[] };
  elite?: { label: string; members: string[] };
}

export interface ExpansionData {
  periods: Array<{ year: number; size: number; groups: string[] }>;
}

export interface StoryChapter {
  title: string;
  content: string[];
  visualization?: 'venn' | 'timeline' | 'expansion' | 'compounding';
  visualizationData?: VennDiagramData | TimelineEvent[] | ExpansionData;
  keyConcepts?: Array<{ term: string; definition: string }>;
}

export const storyChapters: StoryChapter[] = [
  {
    title: "Introduction: A Pattern Emerges",
    content: [
      "Imagine you could see oppression not as random acts of cruelty, but as a predictable system with mathematical properties. This is the story of how systems of domination operate—across history, across contexts, and even in our most intimate relationships.",
      "Through the lens of set theory and historical analysis, we'll discover that oppression isn't chaos. It follows patterns. It has architecture. And understanding that architecture is the first step toward dismantling it.",
      "This journey will take us from 1619 Virginia to modern mass incarceration, revealing a shocking truth: the group targeted by oppression doesn't shrink over time—it expands."
    ],
    keyConcepts: [
      { term: "Oppressive System (S)", definition: "A social structure that systematically restricts autonomy for some while preserving it for others" },
      { term: "Set Theory", definition: "A branch of mathematics dealing with collections of objects, used here to formalize social dynamics" }
    ]
  },
  {
    title: "The Four Pillars of Oppression",
    content: [
      "Every oppressive system, regardless of context, rests on four architectural components:",
      "First: Asymmetric Autonomy Restriction. The In-group (I) enjoys freedoms that are systematically denied to the Out-group (O). This isn't individual prejudice—it's structural.",
      "Second: Selective Empathy. In-group suffering demands immediate response. Out-group suffering is dismissed, minimized, or blamed on the victims themselves.",
      "Third: Ideological Justification. The system generates spurious claims to explain why inequality is natural, necessary, or deserved.",
      "Fourth: Resistance to Critique. The system actively suppresses attempts to examine or challenge its structure."
    ],
    visualization: 'venn',
    visualizationData: {
      inGroup: { label: 'In-group (I)', members: ['Full autonomy', 'Empathy received', 'Justified actions'] },
      outGroup: { label: 'Out-group (O)', members: ['Restricted autonomy', 'Empathy denied', 'Actions criminalized'] },
      elite: { label: 'Elite (E ⊂ I)', members: ['Extract value', 'Maintain division', 'Control narrative'] }
    },
    keyConcepts: [
      { term: "In-group (I)", definition: "The privileged class with full autonomy and systemic protection" },
      { term: "Out-group (O)", definition: "The oppressed class with restricted autonomy and systemic harm" },
      { term: "Elite (E ⊂ I)", definition: "A subset of the In-group that truly benefits from the oppressive system" }
    ]
  },
  {
    title: "1619-1705: The Birth of Racial Capitalism",
    content: [
      "In 1619, the first enslaved Africans arrived in Virginia. But the story of American racism doesn't begin with Black and white—it begins with class.",
      "Poor whites and enslaved Africans initially found common cause. In 1676, Bacon's Rebellion united them against the colonial elite. The plantation owners faced a terrifying prospect: solidarity across racial lines.",
      "The solution? The Virginia Slave Codes of 1705. By granting poor whites symbolic privileges—the right to own guns, beat slaves, and claim racial superiority—the elite fractured working-class unity.",
      "This is the origin story of American racism: not ancient tribal hatred, but a calculated engineering solution to a labor problem."
    ],
    visualization: 'timeline',
    visualizationData: [
      { year: 1619, event: 'First enslaved Africans arrive', outgroup: ['Africans'] },
      { year: 1676, event: 'Bacon\'s Rebellion - Cross-racial solidarity', outgroup: ['Africans', 'Poor Whites'] },
      { year: 1705, event: 'Virginia Slave Codes - Racial division formalized', outgroup: ['Black people'] }
    ]
  },
  {
    title: "1865-1968: Reconstruction and the Expansion Begins",
    content: [
      "The Civil War ended slavery. The elite needed a new system. Enter convict leasing.",
      "By criminalizing activities predominantly performed by newly freed Black Americans—loitering, vagrancy, 'inflammatory speech'—the South created a pipeline from freedom to forced labor.",
      "But here's where the pattern reveals itself: poor whites were also caught in this net. The Out-group was expanding.",
      "By the Jim Crow era, the mathematical formula was clear: O₁₉₀₀ = {Black Americans} ∪ {Poor Whites} ∪ {The 'Undesirable'}"
    ],
    keyConcepts: [
      { term: "Convict Leasing", definition: "System where prisoners were leased to private businesses, creating economic incentives for incarceration" },
      { term: "Out-group Expansion", definition: "The tendency of oppressive systems to progressively include more groups in the oppressed class" }
    ]
  },
  {
    title: "1971-Present: The War on Drugs",
    content: [
      "In 1971, President Nixon declared the War on Drugs. His advisor John Ehrlichman later confessed:",
      "'We knew we were lying about the drugs. But by getting the public to associate hippies with marijuana and Black people with heroin, we could disrupt those communities, arrest their leaders, and vilify them.'",
      "The result? The United States, with 5% of the world's population, now holds 25% of the world's prisoners.",
      "And the Out-group? It now includes: Black Americans, poor people of all races, drug users, immigrants, and increasingly, middle-class whites caught in mandatory minimums.",
      "The pattern is undeniable: |O(t)| increases over time."
    ],
    visualization: 'expansion',
    visualizationData: {
      periods: [
        { year: 1619, size: 1, groups: ['Enslaved Africans'] },
        { year: 1865, size: 2, groups: ['Black Americans', 'Poor Whites'] },
        { year: 1971, size: 4, groups: ['Black Americans', 'Poor People', 'Drug Users', 'Anti-war Left'] },
        { year: 2020, size: 6, groups: ['Black Americans', 'Poor People', 'Drug Users', 'Immigrants', 'Debtors', 'The Incarcerated'] }
      ]
    }
  },
  {
    title: "The Elite Extraction Model",
    content: [
      "Here's the crucial insight: who actually benefits from this system?",
      "Not the nominal In-group. Poor whites aren't getting richer. Middle-class whites see their children also caught in the carceral system.",
      "The beneficiaries are a tiny Elite class (E ⊂ I): prison corporations, pharmaceutical companies profiting from the opioid crisis, politicians using fear to win elections.",
      "The mathematical model reveals: E uses division to prevent solidarity. As long as the In-group and Out-group fight each other, they can't challenge E.",
      "This is why the Out-group must expand: the system requires an ever-growing supply of people to extract value from."
    ],
    keyConcepts: [
      { term: "Elite Class (E)", definition: "The small subset of the In-group that profits from maintaining oppression" },
      { term: "Extraction", definition: "The process by which the Elite class derives economic and political value from the oppressed" }
    ]
  },
  {
    title: "The Same Pattern, Different Scale",
    content: [
      "This mathematical architecture isn't limited to racial systems. It appears in abusive relationships, toxic workplaces, and authoritarian regimes.",
      "An abusive partner restricts their victim's autonomy (pillar 1), dismisses their suffering (pillar 2), claims the abuse is justified or provoked (pillar 3), and punishes attempts to seek help (pillar 4).",
      "The transferability of this pattern across scales suggests something profound: oppression operates through recognizable, formalizable structures.",
      "And if we can formalize it, we can identify it. If we can identify it, we can resist it."
    ]
  },
  {
    title: "What Comes Next",
    content: [
      "You've completed the story. You understand the architecture of oppression.",
      "The question now is: what do we do with this knowledge?",
      "The dashboard you're about to enter contains tools to explore this framework in depth—timelines, visualizations, and the full mathematical model.",
      "But more importantly, it contains the patterns you need to recognize oppression when you encounter it—whether in policy debates, workplace dynamics, or your own relationships.",
      "Knowledge is the first step. Solidarity is the solution. When we recognize that the system benefits only a tiny Elite by dividing the rest of us, we can begin to build something better.",
      "Welcome to the dashboard. Let's explore."
    ]
  }
];
