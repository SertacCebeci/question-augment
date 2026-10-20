---
description: "A signal carries usable information only if its target concept is parseable given the receiver's acquired prerequisites; otherwise it collapses to a null observation, so informativeness is relative."
aliases: ["relativity of randomness", "prerequisite-gated parsing", "learner-side bottleneck"]
sources: ["arxiv-2603-19349"]
---
# Prerequisite-gated decodability

Whether an answer or explanation informs is not a property of the text alone. In Taşkesen's model a learner (a "mind") holds an acquired concept set and a prerequisite structure. A raw signal targets one concept. It is passed through a parsing map: if the targeted concept is not currently parseable, the learner observes a constant null symbol instead.[^c1] The effective channel from the teacher's latent target to the learner therefore changes as the learner's knowledge changes, unlike a Shannon channel with a fixed input-output relation.[^c2]

## The dichotomy

The paper's theorem on the "relativity of randomness" states an eventwise split. On rounds where the targeted concept is unparseable, the learner gets zero additional mutual information about the target from the signal. On parseable rounds, if the raw signal is informative, the transfer is strictly positive.[^c3] The same broadcast can therefore transmit to one learner and be erased for another.[^c4] The paper notes that the occurrence of unparseability can itself still be informative.

## Acquisition refines the experiment

Acquiring prerequisites does more than add facts. The paper shows that the parsed experiment induced by a larger acquired state Blackwell-dominates the one induced by a smaller state (see [[blackwell-informativeness]]).[^c5] For asking and answering, an answer that is correct but uses concepts the asker lacks yields no information. Choosing what to say needs a model of what the listener can currently decode, not only of what is true.

## Two separate bottlenecks

Identification needs the full initial uncertainty about the target to be paid for in usable information.[^c6] Before that, the learner must walk a prerequisite path to the target. These are different obstacles, and the paper's own summary says the structural one can dominate.[^c7] See [[prerequisite-depth-teaching-threshold]].

## Limits

- It is a stylized model: one concept added per round, a deterministic gate, and no forgetting, analogy, abstraction or semantic interpretation (the paper excludes these).
- The erasure result assumes a known, exact parsing map. Real listeners parse partially, and the model does not measure this.
- No experiment with humans or LLMs was read here. The claim that the model covers neural networks is the paper's own assertion, not tested in the slices read.
- The mapping of "prerequisite" to real conceptual dependencies in natural-language questions is my inference and is not established.

## Related

- [[blackwell-informativeness]] — the order the paper uses to compare the parsed experiments of larger and smaller acquired states
- [[prerequisite-depth-teaching-threshold]] — the structural limits that follow from the gate
- [[curriculum-sequencing-policy]] — a practical policy over a prerequisite graph of subtopics
- [[dependency-aware-subquestion-scheduling]] — ordering questions by dependencies

[^c1]: arxiv-2603-19349 — "usable only when its"
[^c2]: arxiv-2603-19349 — "Shannon’s information theory [Shannon, 1948] studies channels whose inputoutput relationship is fixed. In our framework, by contrast, the learner’s parsing"
[^c3]: arxiv-2603-19349 — "Theorem 3.13 (Relativity of randomness). Let Ct+1 = tgt(Zt+1 ) be the targeted"
[^c4]: arxiv-2603-19349 — "state dependent. In particular, the same raw broadcast may transmit usable"
[^c5]: arxiv-2603-19349 — "parsed experiment induced by a larger acquired state Blackwell-dominates the"
[^c6]: arxiv-2603-19349 — "Lemma 4.9 says that identification must pay for the full initial uncertainty of"
[^c7]: arxiv-2603-19349 — "The structural barrier can be dominant, but"
