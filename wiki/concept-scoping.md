---
description: "Before borderline cases are shown, a composite subjective concept is split into at most three unit concepts, whose candidate positive and negative subconcepts the user keeps or drops."
aliases: ["concept decomposition", "subconcept scoping", "scoping stage"]
sources: ["arxiv-2512-10821"]
---
# Concept scoping

Before anyone looks at borderline cases, a subjective concept is scoped: it is split into its visual parts, and each part gets candidate positive and negative subconcepts. The work makes this the first stage of concept deliberation, in which "the system decomposes the user's initial concept description into a hierarchy of subconcepts".[^c1] The aim is a structure the user can then check cases against, rather than one undivided phrase.

The mechanism has three steps. A composite concept is first rewritten as a formula over unit concepts, and the authors keep the count small: "We keep M small because too many unit concepts" are "harder to reason about".[^c2] The formula is "a formula over conjunctions and disjunctions", so a concept such as healthy food becomes a few simpler dimensions joined by logic.[^c9] For each unit concept, the system generates candidate positive and negative subconcepts, each with retrieved representative images.[^c10] Then "Users then decide which subconcept should be included".[^c3] The result, "an initial structured definition", is what instantiates the first classifier and seeds the later rounds of iteration.[^c4]

The stage rests on what practitioners were seen to do. In the authors' coding of 20 professional concept definitions, "practitioners typically begin by scoping their concept definitions and then" refine them by reflecting on borderline images.[^c5] The decomposition itself was run by a model: "We use Gemini-Pro 2.5 for the concept decomposition component".[^c6]

## Limits

- The stage is not measured on its own. The authors' evaluation "does not isolate the contributions of individual components", and scoping is not separated from the iteration that follows it.[^c7]
- The comparison with an automated decomposer does not isolate scoping either. The paper reports a 7.5% advantage over "methods that automatically decompose subjective concepts using LLMs", but that comparison also differs in the deliberation stage that follows.[^c8]
- The cap of three unit concepts is justified by a sentence, not tested against other caps. Its only support is that more units are harder to reason about.[^c2]
- The unit concepts are chosen by a model and then accepted by a user. The paper does not check them against a human decomposition of the same concept. This is my inference, not a finding.
- Figure 2 shows a decomposition for one participant on healthy food, and its effect is shown only by example. No aggregate measure of the scoping output is reported.

## Related

- [[concept-deliberation]] — the parent process; scoping is its first stage, and the iteration stage depends on the structure it yields.
- [[semantic-borderline-selection]] — the stage that uses the scoped definition to pick the borderline cases shown to the user.
- [[ambiguity-taxonomy]] — a vague term admits borderline cases; scoping gives those cases named parts to fall between. This link is my inference, not the paper's.

[^c1]: arxiv-2512-10821 — "into a hierarchy of subconcepts"
[^c2]: arxiv-2512-10821 — "We keep M small because too many unit concepts"
[^c3]: arxiv-2512-10821 — "Users then decide which subconcept should be included"
[^c4]: arxiv-2512-10821 — "The result of Stage 1 is an initial structured definition"
[^c5]: arxiv-2512-10821 — "typically begin by scoping their concept definitions and then"
[^c6]: arxiv-2512-10821 — "We use Gemini-Pro 2.5 for the concept decomposition component"
[^c7]: arxiv-2512-10821 — "Our evaluation does not isolate the contributions of individual components"
[^c8]: arxiv-2512-10821 — "methods that automatically decompose subjective concepts using LLMs"
[^c9]: arxiv-2512-10821 — "is a formula over conjunctions and disjunctions"
[^c10]: arxiv-2512-10821 — "retrieved representative images"
