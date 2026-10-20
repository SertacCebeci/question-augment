---
description: "At first contact with an unfamiliar knowledge graph a lay user is in a pre-goal state of scope uncertainty, ontology opacity and query incapacity; question-asking tools presuppose what is missing."
aliases: ["IEP", "first-contact problem", "scope revelation gap", "entry-point problem"]
sources: ["arxiv-2602-21066"]
---
# Initial exploration problem

A conceptual proposal by McNamara et al. (2026, arxiv-2602-21066), not a measurement: before anyone can ask a good question of an unfamiliar knowledge graph (KG), they must be able to pick a starting point, and at first contact they cannot. The paper defines the problem as "a temporally bounded pre-goal state" that arises at first contact with an unfamiliar KG.[^c1]

## The three barriers

The state is the co-occurrence of three barriers:

- **Scope uncertainty** is "where to begin". It is epistemic, not technical: the user cannot reason about the knowledge space itself, and large KGs make it worse.
- **Ontology opacity** is the user's inability to map the schema onto a mental model, so they cannot anticipate which questions are meaningful.
- **Query incapacity** is the lack of a formal query language (SPARQL) skill.

The paper names scope uncertainty as dominant: "At first contact, scope uncertainty precedes query incapacity".[^c2] The barriers are interdependent, so fixing one leaves the others. The paper's example is that "providing users with a means of asking NLQs over a KG does not address" what to ask or how to structure it.[^c3]

## How it differs from neighbouring notions

The paper positions the problem against existing information-behaviour concepts. For Belkin's Anomalous State of Knowledge (ASK), "ASK presupposes a knowledge gap; the IEP precedes the ability to articulate such a gap."[^c4] This makes the problem close to, but distinct from, [[unknown-unknowns]]. There the asker lacks the axis along which to ask. Here the same lack is localised to the first moment of an interaction and tied to an interface.

In information foraging terms it is "a complete absence of scent".[^c5] Onboarding is a remedy rather than the same thing: "onboarding is a method of solution to the IEP, it does not articulate the problem."[^c6]

## Interaction primitives presuppose what is missing

The paper decomposes KG interfaces into primitives (search, facet selection, schema browsing, graph navigation, visual query building, natural-language question answering). Each carries an epistemic precondition. For example, "issuing a search query presupposes that the user has and can articulate a meaningful" information need.[^c7] Faceted browsers, visual tools and natural-language-to-SPARQL tools are therefore, on the paper's argument, effective only after the problem is overcome. This is a claim about temporal alignment, not about poor design.

## The missing primitive: scope revelation

The paper names a gap in the design space: no dominant primitive has the function of "scope revelation without user specification".[^c8] It must meet three conditions. It must not require the user to state a goal or query. It must not need ontology interpretation: "it must not rely on the user interpreting ontological structures or terminology".[^c9] It must also give a foothold from which exploration proceeds. Suggested forms are curated question-and-answer pairs, semantic preview panels and guided entity anchors. The idea in terms of asking and answering is that the system's answer side comes first and shows what questions are answerable, so that the user's question is formed rather than assumed.

## Limits

- The paper says of itself that it is "a conceptual and positioning contribution". It reports no user study, so the claim that the three barriers co-occur and that scope uncertainty dominates rests on a literature synthesis, not on measurement.
- The scope is lay users, complex KGs and, in its examples, digital humanities. Transfer to other first-contact settings (an unfamiliar database, a new domain expert, a chat assistant) is this note's inference, not shown.
- The paper's tables of primitives and preconditions are the authors' own classification, not tested.
- Whether scope-revealing primitives (their own CuQA, in ongoing work) actually help is not established here.

## Related

- [[unknown-unknowns]] — the general state of lacking the axis to ask along; this note is the interface-bound, first-contact case
- [[knowledge-graph-guided-clarification]] — uses a KG to shape questions, where this note concerns the user's questions of a KG
- [[information-need-reification]] — turning a vague need into an askable one, the step the problem blocks
- [[cold-start-value-of-information]] — another first-contact condition, for the system rather than the user

[^c1]: arxiv-2602-21066 — "First, it defines the Initial Exploration Problem (IEP) as a temporally bounded"
[^c2]: arxiv-2602-21066 — "At first contact, scope uncertainty precedes query incapacity"
[^c3]: arxiv-2602-21066 — "providing users with a means of asking NLQs over a KG does not address"
[^c4]: arxiv-2602-21066 — "ASK presupposes a knowledge gap; the IEP precedes the ability to articulate such a gap."
[^c5]: arxiv-2602-21066 — "The IEP represents a complete absence of scent"
[^c6]: arxiv-2602-21066 — "onboarding is a method of solution to the IEP, it does not articulate the problem."
[^c7]: arxiv-2602-21066 — "issuing a search query presupposes that the user has and can articulate a meaningful"
[^c8]: arxiv-2602-21066 — "scope revelation without user specification"
[^c9]: arxiv-2602-21066 — "it must not rely on the user interpreting ontological structures or terminology"
