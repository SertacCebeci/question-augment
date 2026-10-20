---
description: "A vague subjective concept is settled by revising its definition against borderline cases, not fixed in advance; an 18-session study measured higher F1 than automated and manual deliberation."
aliases: ["agile deliberation", "subjective concept deliberation", "deliberative concept definition"]
sources: ["arxiv-2512-10821"]
---
# Concept deliberation

A subjective concept such as "healthy food" or "unsafe imagery" often has no settled definition when someone needs a classifier for it. The work's claim is that the definition is reached by working at it: people "must spend significant time exploring borderline cases and refining their definitions accordingly".[^c1] The authors name this practice concept deliberation and say they identified its strategies through "structured interviews with content moderation experts".[^c2]

The mechanism runs in two stages. In scoping, a composite concept is split into unit concepts, and each receives candidate positive and negative subconcepts that the user keeps or drops ([[concept-scoping]]). The output is a definition that is both a human-readable description and a prompt for a vision–language classifier: "a textual specification with explicit positive/negative subconcepts and edge cases".[^c3] In iteration, the system surfaces borderline images ([[semantic-borderline-selection]]). The user labels them and gives short reasons, and the system writes several rewritten definitions and keeps the one with the highest F1 on all labels collected so far: "We choose the best candidate via a greedy update".[^c4] The definition therefore changes as the user meets cases the current wording does not settle.

The measured result comes from 18 sessions. Nine participants, each without prior professional content moderation experience, ran one session with this system and one with manual deliberation, on different concepts, at about 90 minutes per session.[^c5] Each participant then labelled 200 held-out images to score the classifier that came out of the session. The introduction reports 7.5% "higher F1 scores than automated decomposition baselines" and "more than 3% higher than manual deliberation".[^c6] Participants also reported that they "exerted significantly less effort to" deliberate.[^c7] The definitions were optimised with one model (Gemini 2.5 Flash) and then used with smaller Qwen3-VL models. The authors report that the gains were largest on the more capable of those models, reading this as richer definitions whose advantages "become more visible as model reasoning ability improves".[^c8]

## Limits

- The sample is small. The authors concede that the study "may limit the statistical power and generalizability" of the findings.[^c9]
- The method came from interviews with experts, but it was tested on novices. Whether it helps people who already work in the field is not tested. The design was "informed by interviews with 5 content moderation experts".[^c10] This sentence is the paper's; the gap it leaves is my inference.
- The two systems were used on different concepts, so the comparison is not clean. The authors say that "the classification performances are not comparable" across participants, because each started from a different understanding of the same concept.[^c11]
- The paper does not separate the stages. "Our evaluation does not isolate the contributions of individual components within Agile Deliberation".[^c12] The authors argue the stages are coupled, that "borderline examples and refining definitions are tightly coupled activities in concept deliberation".[^c13] So the study supports the package, not the claim that either stage does the work.
- The two gain figures do not match. The introduction gives 7.5% over automated decomposition; the results section gives "10.5% and 7% on average" over the two automated baselines.[^c14] The text read here does not reconcile them.
- F1 is scored against each participant's own labels, which are the concept being deliberated. The measure is therefore agreement with the user's stated definition, not correctness against an outside truth. This is my inference from the design, not a claim the paper makes.

## Related

- [[concept-scoping]] — the first stage, which splits the concept before any borderline case is shown.
- [[semantic-borderline-selection]] — how the second stage picks the cases a user deliberates over.
- [[ambiguity-taxonomy]] — a vague term admits borderline cases and is inquiry resistant; deliberation works on those cases by example rather than by a single closing question.
- [[clara-visual-disambiguation]] — sorts visual candidates along interpretable ambiguity axes for one request; this work uses a similar axis to stress-test a standing definition.

[^c1]: arxiv-2512-10821 — "exploring borderline cases and refining their definitions accordingly"
[^c2]: arxiv-2512-10821 — "structured interviews with content moderation experts"
[^c3]: arxiv-2512-10821 — "a textual specification with explicit positive/negative subconcepts and edge"
[^c4]: arxiv-2512-10821 — "We choose the best candidate via a greedy update"
[^c5]: arxiv-2512-10821 — "nine participants without prior professional content moderation experience"
[^c6]: arxiv-2512-10821 — "more than 3% higher than manual deliberation"
[^c7]: arxiv-2512-10821 — "participants exerted significantly less effort to"
[^c8]: arxiv-2512-10821 — "become more visible as model reasoning ability improves"
[^c9]: arxiv-2512-10821 — "which may limit the statistical power and generalizability"
[^c10]: arxiv-2512-10821 — "Our design is informed by interviews with 5 content moderation experts"
[^c11]: arxiv-2512-10821 — "the classification performances are not comparable"
[^c12]: arxiv-2512-10821 — "Our evaluation does not isolate the contributions of individual components within Agile Deliberation"
[^c13]: arxiv-2512-10821 — "borderline examples and refining definitions are tightly coupled activities in concept deliberation"
[^c14]: arxiv-2512-10821 — "10.5% and 7% on average"
