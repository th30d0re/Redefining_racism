#!/bin/bash
SRC="Redefining_Racism_BACKUP_pre_restructure.tex"
OUT="Redefining_Racism.tex"

extract() { sed -n "${1},${2}p" "$SRC"; }

{
# === PREAMBLE (unchanged) ===
extract 1 99

# === CHAPTER 1: INTRODUCTION (current Ch 1, lines 101-293) ===
# Keep as-is for now; Phase 2 will rewrite forward refs
extract 101 293

# === CHAPTER 2: THE SOURCE CODE — PORTUGUESE ORIGINS (1450s) ===
cat << 'CHAP2'

\chapter{The Source Code: Portuguese Origins and the First Two Variables (1450s)}

Having established the architectural thesis, we now begin the chronological construction of the extraction algorithm. Rather than presenting the full mathematical framework in the abstract, we will introduce each formal variable at the exact historical moment the Elite were forced to invent it. The reader will watch the system being built, tier by tier, as the Elite iteratively patched their security vulnerabilities.

CHAP2

# 2.1 Portuguese Class Dynamics (current 296-310)
echo '\section{Portuguese Class Dynamics and the Elite'\''s Dilemma}'
echo ''
extract 298 310

# 2.2 Invention of Race (current 312-318)
extract 312 318

# 2.3 Implicit Contract + Slave Capitalism (current 320-461)
extract 320 461

# NEW: Introducing E and O (placeholder for Phase 2)
cat << 'INTRO_EO'

\section{Introducing the First Two Variables: The Elite ($E$) and the Out-group ($O_{\text{racialized}}$)}

% === PHASE 2 PLACEHOLDER: Write fresh transition introducing E and O ===
% Extract and adapt from current Ch 3 lines 737-753 (just E and O definitions)
% Present the embryonic 2-variable inequality: Benefit(E) >> Benefit(O)
% Introduce the concept of the Predatory Min-Max Function in its simplest form
% Include the Scope and Specificity note (current line 817)

The historical narrative of this chapter has demonstrated the system's two foundational actors in operation. We now formalize them mathematically.

Utilizing set theory, let us define the first two variables of the extraction algorithm as they emerged from the Portuguese innovation:

\begin{enumerate}
    \item \textbf{The True Elite ($E$):} The hyper-concentrated capital class (representing approximately 0.002\% of the population). They do not govern; they \textit{own}. Their primary function is dictating the core parameters of the extraction system. They are entirely insulated from the physical consequences of the system.

    \item \textbf{The Out-group ($O_{\text{racialized}}$):} The primary extraction pool---those subjected to racialization, initially African peoples and their descendants---systematically stripped of accumulated capacity ($O_t^{\text{capacity}}$) through compounding historic and modern policies.
\end{enumerate}

The foundational inequality of this embryonic system is therefore two-tiered:
\[
\text{Benefit}(E) \gg \text{Benefit}(O_{\text{racialized}})
\]

As the historical timeline will demonstrate, this simple two-variable system proved insufficient. The Elite were forced to invent additional tiers---each one a patch for a specific security flaw---until the full architecture was complete. We will introduce each tier at the moment of its invention.

\textbf{A Note on Scope and Specificity}: This model is specifically designed to analyze racism as a unique system rooted in the 15th century racialization of African peoples for the purposes of enslavement and colonial exploitation. The notation $O_{\text{racialized}}$ reflects this historical specificity. While the mathematical architecture may share structural similarities with other systems of oppression, this paper focuses on racism's particular genealogy and mechanisms. The subscript ``racialized'' anchors the mathematical formalism to the historical narrative, ensuring that the model captures the unique features of racism rather than generic intergroup conflict.

INTRO_EO

# 2.x Global Replication (current 463-491)
extract 463 491

# 2.x Institutional Legitimation (current 493-596)
extract 493 596

# === CHAPTER 3: THE APPLICATION — BACON'S REBELLION AND THE BUFFER CLASS (1676-1787) ===
cat << 'CHAP3'

\chapter{The Application: Bacon's Rebellion, the Buffer Class, and the Constitutional Patch (1676--1787)}

The two-variable system ($E$ and $O_{\text{racialized}}$) proved fatally unstable. In the American colonies, the Elite initially failed to implement the Portuguese code strictly. The result was the most dangerous event in Elite history: a unified working class that nearly destroyed them. This chapter traces the system's emergency response---the invention of the Buffer Class---and the subsequent constitutional patch that separated the Elite's front-end from their back-end.

CHAP3

# 3.1 Bacon's Rebellion (current 1145-1153)
extract 1145 1153

# 3.2 Invention of Whiteness (current 1154-1167)
extract 1154 1167

# NEW: Introducing the Buffer Class (placeholder for Phase 2)
cat << 'INTRO_BUFFER'

\section{Introducing the Third Variable: The Buffer Class ($I_{\text{buffer}}$) and the Psychological Wage ($\psi$)}

% === PHASE 2 PLACEHOLDER: Write fresh transition introducing I_buffer ===
% Extract and adapt Buffer Class definition from current Ch 3 line 750
% Formally define psi here
% Upgrade inequality to 3-tier: Benefit(E) >> Benefit(I_buffer) > Benefit(O)

The invention of ``Whiteness'' in 1705 was not merely a legal act; it was the creation of an entirely new mathematical variable in the extraction algorithm. We now formalize this third tier.

\begin{enumerate}
    \setcounter{enumi}{2}
    \item \textbf{The Buffer Class ($I_{\text{buffer}}$):} The remaining working-class In-group. They produce the economic reserves and provide the ideological cover required to legitimize the state, pacified by the psychological wages of racism ($\psi$) and the illusion of democratic agency. Following W.E.B.\ Du~Bois \cite{dubois}, we formalize the \textbf{psychological wage} $\psi$ as the non-material benefit (social status, legal privilege, racial solidarity with elites) offered to $I_{\text{buffer}}$ in exchange for policing the racial boundary rather than pursuing cross-racial class solidarity with $O_{\text{racialized}}$.
\end{enumerate}

The foundational inequality of the system upgrades to three tiers:
\[
\text{Benefit}(E) \gg \text{Benefit}(I_{\text{buffer}}) > \text{Benefit}(O_{\text{racialized}})
\]
where $\text{Benefit}(I_{\text{buffer}})$ consists primarily of $\psi$ (psychological wages) rather than material extraction, and $\text{Benefit}(E)$ reflects the material wealth extracted from all tiers below.

The psychological wage $\psi$ is not merely a side effect of the system; it is a \textit{designed feature}. The Elite ($E$) invest in $\psi$ precisely because it is cheaper than material concession: granting $I_{\text{buffer}}$ racial status, legal privileges over $O_{\text{racialized}}$, and the right to police the racial boundary costs the Elite far less than sharing material wealth. This makes $\psi$ the key variable in the system's minimization of class resistance. The system thus produces a paradox: $I_{\text{buffer}}$ defends a hierarchy that materially harms them, because the psychological wage creates the \textit{perception} of shared interest with $E$ and the \textit{perception} of threat from $O_{\text{racialized}}$. Both perceptions serve $E$'s extraction objectives.

INTRO_BUFFER

# 3.x Johnson Theorem (current 1021-1049)
extract 1021 1049

# 3.x Constitutional Trojan Horse (current 604-733)
extract 604 733

# NEW: The Prototype Puppet Class (placeholder for Phase 2)
cat << 'PROTO_PUPPET'

\section{The Second Crash and the Constitutional Patch: The Prototype Puppet Class (1787)}

% === PHASE 2 PLACEHOLDER: Write fresh section on Constitutional Convention as front-end/back-end separation ===
% Shays' Rebellion as second crash report
% The Elite realize direct rule makes them the target
% They separate front-end (representative government) from back-end (capital management)
% The Constitution deploys the Puppet Class in beta form
% Initial algorithmic filter: only white male property owners vote/hold office

The invention of the Buffer Class in 1705 solved the immediate crisis of cross-racial solidarity, but it did not solve the Elite's deeper vulnerability: \textit{visibility}. As long as the Elite ruled directly---as kings, royal governors, and landed aristocracy---they remained the obvious target whenever the system produced suffering. If the Buffer Class starved, they knew exactly whose mansion to burn.

Shays' Rebellion (1786--1787) served as the second ``crash report'' in the Elite's operating system. Barely a decade after independence, armed farmers in Massachusetts---members of the very Buffer Class that was supposed to be pacified---rose up against debt collectors and courts. The rebellion terrified the Elite precisely because it demonstrated that the Buffer Class, despite their psychological wages, could still identify the economic source of their suffering.

The Elite's solution was architectural: \textbf{separate the front-end from the back-end}. Rather than ruling directly, they would engineer a system of representative government---a political \textit{interface}---that the Buffer Class and Out-group would interact with, vote for, direct their grievances toward, and ultimately blame when the system failed. Meanwhile, the Elite would retreat to the back-end: managing the capital, the land, the central banks, and the true levers of power, entirely insulated from democratic accountability.

The Constitutional Convention of 1787 was this architectural separation made concrete. The ``Prototype Puppet Class'' ($P_{\text{uppet}}^{\text{v1.0}}$) was deployed: a Representative Republic where elected officials served as the visible face of governance while the true parameters of the system---property law, commerce, monetary policy---remained under Elite control.

The initial ``Algorithmic Filter'' was crude but effective: only white male property owners were legally permitted to vote or hold office. This ensured that the first generation of the Puppet Class was drawn almost entirely from the Elite themselves or their direct proxies. But the architecture was designed to scale. The system did not require the Elite to personally occupy every seat of power; it merely required that whoever occupied those seats remained tethered to Elite capital.

This constitutional patch created the illusion of self-governance while mathematically guaranteeing that the extraction kernel remained untouchable. The Elite no longer wore crowns; they funded representatives. And when the people grew angry, they directed their fury at the representatives---the front-end---while the back-end continued to extract, undisturbed.

PROTO_PUPPET

# 3.x Haitian Catalyst (current 1168-1175)
extract 1168 1175

# 3.x Haitian Contagion / Lockdown (current 1176-1192)
extract 1176 1192

# 3.x Sovereign Ransom / Haiti debt (current 1125-1132)
extract 1125 1132

# === CHAPTER 4: THE ENFORCEMENT ENGINE (1704-1865) ===
cat << 'CHAP4'

\chapter{The Enforcement Engine: Slave Patrols, the 13th Amendment, and the Compounding Model (1704--1865)}

With the Buffer Class pacified and the Puppet Class deployed as the system's political interface, the Elite required one more critical component: a physical enforcement apparatus. This chapter traces the invention of the Enforcement Class and the mathematical proof that the system's harm compounds multiplicatively over time.

CHAP4

# 4.1 Slave Patrols (current 598-603)
extract 598 603

# NEW: Introducing the Enforcement Class (placeholder for Phase 2)
cat << 'INTRO_ENFORCE'

\section{Introducing the Fourth Variable: The Enforcement Class ($F_{\text{enforce}}$)}

% === PHASE 2 PLACEHOLDER: Write fresh transition introducing F_enforce ===
% Extract and adapt from current Ch 3 line 744
% Define Qualified Immunity (QI)
% Introduce the Lethal Autonomy gradient
% Upgrade inequality to 4-tier

The slave patrol system reveals the structural necessity for a dedicated enforcement tier. The Elite ($E$) cannot personally actuate their extraction; doing so would expose them to the physical dangers of direct rule. The Buffer Class ($I_{\text{buffer}}$) provides ideological cover but lacks institutional authority. The system therefore required a specialized kinetic arm---recruited from the lower classes but compensated with unique privileges---to physically enforce the extraction algorithm.

\begin{enumerate}
    \setcounter{enumi}{2}
    \item \textbf{The Enforcement Class ($F_{\text{enforce}}$):} The kinetic arm of the algorithm ($F_{\text{enforce}} \subset I \cup O$). Comprising the military, domestic police forces, and carceral agents, they physically actuate the extraction. Crucially, $E$ recruits $F_{\text{enforce}}$ almost entirely from the lower classes. To ensure their compliance in inflicting brutality upon their own socioeconomic peers, $E$ compensates $F_{\text{enforce}}$ with a unique variable: \textbf{Qualified Immunity} ($QI$)---the judicial doctrine that shields state agents from civil liability for constitutional violations unless the victim can cite a prior case with nearly identical facts. The asymmetry of $QI$ is most starkly visible in the distribution of lethal autonomy. Under the Law Enforcement Officers Safety Act (LEOSA), active and retired members of $F_{\text{enforce}}$ are granted the statutory right to carry concealed firearms in all 50 states, superseding every state and local restriction. The Second Amendment thus operates on a strict gradient:
    \[
    \text{Lethal Autonomy}(F_{\text{enforce}}) \gg \text{Lethal Autonomy}(I_{\text{buffer}}) \gg \text{Lethal Autonomy}(O) = 0
    \]
    This gradient is not incidental; it is the physical enforcement of the hierarchy. $F_{\text{enforce}}$ is granted superior armament precisely because they must be capable of overwhelming both the classes below them. However, their status is strictly conditional; once a member of $F_{\text{enforce}}$ is no longer physically useful, their $QI$ is revoked, and they are discarded back into the Buffer Class or the Out-group.
\end{enumerate}

The foundational inequality now extends to four tiers:
\[
\text{Benefit}(E) \gg \text{Benefit}(F_{\text{enforce}}) > \text{Benefit}(I_{\text{buffer}}) > \text{Benefit}(O_{\text{racialized}})
\]
where $\text{Benefit}(F_{\text{enforce}})$ consists of Qualified Immunity ($QI$) and enhanced lethal autonomy.

INTRO_ENFORCE

# 4.x Second Amendment / Lethal Autonomy (current 1194-1229)
extract 1194 1229

# 4.x 13th Amendment Loophole (current 1230-1266)
extract 1230 1266

# 4.x Compounding Model + figures (current 819-1011)
cat << 'COMPOUND_HEADER'

\section{The Compounding Model: From Summation to Multiplication}

With the enforcement apparatus in place and the 13th Amendment providing the legal kernel for perpetual extraction, we can now formalize a critical mathematical property of the system: its harm does not merely add up---it \textbf{compounds}.

COMPOUND_HEADER
extract 821 1011

# 4.x Imperial Enforcement / 1915 Haiti (current 1267-1274)
extract 1267 1274

# === CHAPTER 5: THE CONTAINMENT (1870s-Present) ===
cat << 'CHAP5'

\chapter{The Containment: Gilded Age, Redlining, and the Scaling of the Puppet Class (1870s--1960s)}

The four-tier system ($E$, $F_{\text{enforce}}$, $I_{\text{buffer}}$, $O_{\text{racialized}}$) now required one final upgrade. As the franchise expanded---non-landowners, minorities, and women winning the right to vote---the crude Algorithmic Filter of the Constitutional era (``only property owners vote'') became untenable. The Elite needed to scale the Puppet Class into a fully industrialized democratic illusion. This chapter traces that upgrade and introduces the fifth and final tier.

CHAP5

# 5.1 Redlining (current 1275-1279)
extract 1275 1279

# 5.2 Civil Rights Capture (current 1280-1291)
extract 1280 1291

# NEW: Scaling the Puppet Class + Tweedism
cat << 'PUPPET_SCALE'

\section{Introducing the Fifth Variable: The Puppet Class ($P_{\text{uppet}}$) and the Tweedism Filter}

% === PHASE 2 PLACEHOLDER: Write fresh transition about Gilded Age franchise expansion ===
% The Elite can no longer use "only landowners vote"
% They upgrade the Puppet Class using Tweedism
% The filter becomes corporate lobbying, two-party duopoly, machine politics

The expansion of the franchise in the 19th and early 20th centuries presented an existential threat to Elite control. Non-landowners, and eventually minorities and women, won the right to vote. The system was flooded with Out-group and Buffer Class users who technically possessed the power to vote away the Elite's wealth.

The Elite could not revert to the old rule of ``only landowners vote.'' Instead, they radically upgraded the Puppet Class from its Constitutional-era prototype into a fully industrialized tier of the extraction hierarchy, deploying what we term \textbf{Tweedism}.

\begin{enumerate}
    \setcounter{enumi}{1}
    \item \textbf{The Puppet Class ($P_{\text{uppet}}$):} The political, judicial, and executive shield ($P_{\text{uppet}} \subset I$). This class writes the laws, sets the agenda, and acts as the ``Interface'' for the system. They provide the illusion of democratic control to the Buffer Class, but their survival and power are strictly tethered to the capital of $E$.
\end{enumerate}

PUPPET_SCALE

# Tweedism content (current 1051-1078)
extract 1051 1078

# 5.x Gilens-Page (current 1013-1019)
extract 1013 1019

# 5.x Agenda-Setter Trap (current 1719-1725)
extract 1719 1725

# 5.x Class Solidarity (current 1727-1731)
extract 1727 1731

# 5.x Conditional Mobility / New Money (current 1079-1124)
extract 1079 1124

# 5.x Algorithmic Corrections (current 1768-1775)
extract 1768 1775

# === CHAPTER 6: THE COMPLETE ALGORITHM (1968-Present) ===
cat << 'CHAP6'

\chapter{The Complete Algorithm: From the War on Drugs to Cannibalization (1968--Present)}

The reader has now watched the extraction algorithm being built, tier by tier, across four centuries: the Elite ($E$) and Out-group ($O_{\text{racialized}}$) in 15th-century Portugal, the Buffer Class ($I_{\text{buffer}}$) after Bacon's Rebellion, the Puppet Class ($P_{\text{uppet}}$) at the Constitutional Convention and its Gilded Age upgrade, and the Enforcement Class ($F_{\text{enforce}}$) through the slave patrol genealogy. This chapter traces the algorithm's modern execution---and reveals the complete 5-Tier architecture for the first time.

CHAP6

# 6.1 War on Drugs (current 1292-1363)
extract 1292 1363

# 6.2 Demographic Paradox (current 1364-1381)
extract 1364 1381

# 6.3 Modern Security Patch / Disarmament (current 1382-1449)
extract 1382 1449

# 6.4 Mental Gun Control (current 1451-1502)
extract 1451 1502

# 6.5 Universal Latent Criminality (current 1776-1783)
extract 1776 1783

# NEW: THE FULL 5-TIER REVEAL
cat << 'REVEAL_HEADER'

\section{The Full Reveal: The Complete 5-Tier Set-Theoretic Hierarchy}

% === PHASE 2 PLACEHOLDER: Write the structural climax ===
% "We have now introduced each tier at its historical point of invention.
% For the first time, we can present the complete architecture..."

We have now traced the construction of each tier through its historical moment of invention:

\begin{itemize}
    \item \textbf{The Elite ($E$)} and \textbf{the Out-group ($O_{\text{racialized}}$)}: invented in 15th-century Portugal to break the moral community and create an extractable labor class (Chapter~2).
    \item \textbf{The Buffer Class ($I_{\text{buffer}}$)}: invented after Bacon's Rebellion (1676) to partition the working class and deploy the psychological wage $\psi$ (Chapter~3).
    \item \textbf{The Puppet Class ($P_{\text{uppet}}$)}: prototyped at the Constitutional Convention (1787), then industrialized through Tweedism in the Gilded Age, to separate the political front-end from the capital back-end (Chapters~3 and~5).
    \item \textbf{The Enforcement Class ($F_{\text{enforce}}$)}: evolved from slave patrols (1704) through the Fugitive Slave Act to modern policing, compensated with Qualified Immunity ($QI$) (Chapter~4).
\end{itemize}

For the first time, we can present the complete architecture as a unified hierarchy. The system is governed by what we term the \textbf{Predatory Min-Max Function}:

\begin{enumerate}
    \item \textbf{Maximize ($Max$):} The extraction of capital, labor, and autonomy from the labor force---primarily from $O_{\text{racialized}}$, but eventually from $I_{\text{buffer}}$ as well.
    \item \textbf{Minimize ($Min$):} The risk of a unified class revolution against the Elite ($E$), achieved by deploying $\psi$ to keep $I_{\text{buffer}}$ invested in racial hierarchy rather than class solidarity, $F_{\text{enforce}}$ invested through $QI$, and $P_{\text{uppet}}$ tethered through capital dependency.
\end{enumerate}

\[
\text{Objective:} \quad \frac{\text{Max}(\text{Extraction})}{\text{Min}(\text{Resistance}_{\text{class}})} \rightarrow \text{System Stability}
\]

The complete five-tiered inequality:
\[
\text{Benefit}(E) \gg \text{Benefit}(P_{\text{uppet}}) > \text{Benefit}(F_{\text{enforce}}) > \text{Benefit}(I_{\text{buffer}}) > \text{Benefit}(O_{\text{racialized}})
\]
where $\text{Benefit}(I_{\text{buffer}})$ consists primarily of $\psi$ (psychological wages), $\text{Benefit}(F_{\text{enforce}})$ consists of Qualified Immunity ($QI$), $\text{Benefit}(P_{\text{uppet}})$ consists of delegated political power tethered to $E$'s capital, and $\text{Benefit}(E)$ reflects the material wealth extracted from all tiers below.

REVEAL_HEADER

# Insert the 5-tier pyramid figure (current 763-815)
extract 763 815

# 6.x Collapse / Cannibalization (current 1504-1515)
extract 1504 1515

# 6.x Biological Degradation (current 1516-1536)
extract 1516 1536

# 6.x Cannibalization of Buffer Class + extraction zone figure (current 1537-1635)
extract 1537 1635

# 6.x Min Variable failure / Disarmament Panic (current 1784-1815)
extract 1784 1815

# 6.x 922(g)(3) Crisis (current 1816-1827)
extract 1816 1827

# 6.x Geopolitical Override (current 1828-1848)
extract 1828 1848

# === CHAPTER 7: POLICY IMPLICATIONS ===
cat << 'CHAP7'

\chapter{From Diagnosis to Prescription: Policy Implications}

The preceding chapters have traced an unbroken algorithmic thread: from the Portuguese invention of racial hierarchy, through the constitutional embedding of extraction via the 13th Amendment, to the modern deployment of proxy variables that now cannibalize the very Buffer Class the system created to protect itself. Each phase of the Elite's optimization reveals a system that adapts its \textit{interface} while preserving its \textit{kernel}: the Predatory Min-Max Function that maximizes extraction while minimizing class resistance.

If this diagnostic is correct, it constrains the space of effective prescriptions. Interventions that target only the system's \textit{interface}---its current legal language, its present-day proxies---will be absorbed and neutralized, as every previous reform movement has been. Effective policy must target the kernel itself: the Predatory Min-Max Function and the economic architecture that sustains it.

CHAP7

# Policy content (current 1643-1718)
extract 1643 1718

# === CHAPTER 8: DISCUSSION ===
extract 1733 1766

# === CHAPTER 9: CONCLUSION ===
extract 1850 1876

# === BIBLIOGRAPHY ===
extract 1877 2070

} > "$OUT"

echo "Restructured file written to $OUT"
echo "Line count: $(wc -l < "$OUT")"
