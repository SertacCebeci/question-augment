---
description: "A black-box's explanatory information kept as one persistent, updatable surrogate that matches every observation, from which stakeholder-specific answers are queried instead of recomputed."
aliases: ["scientific theory of a black box", "SToBB", "constructive-empiricist XAI"]
sources: ["arxiv-2602-02215"]
---
# Empirically adequate surrogate record

The problem it addresses: explanation methods are applied ad hoc, so answers to similar questions are recomputed and can disagree. The source says methods yield "isolated outputs that may need to be recomputed for similar questions and that can yield incompatible characterisations" of one model.[^c1] Its proposal is to keep one maintained record of the black box and to treat that record as a theory in van Fraassen's constructive-empiricist sense. It is "not itself an explanation, but a representational foundation from which diverse explanations can be derived."[^c2]

## Mechanism

The record has five parts: an extensible observation base (inputs, outputs, auxiliary measures), a traceable hypothesis class, algorithms to construct and update, a concrete surrogate, and documentation.[^c3] The central requirement is empirical adequacy. The surrogate must reproduce the black box on all available observations, with no tolerated approximation error. The source calls this "stricter than typical surrogate modelling in XAI" and looser than held-out testing, because the target is a fixed function and the aim is not generalisation beyond it.[^c4] Adequacy is binary. When a new observation conflicts with the surrogate, a documented update procedure must restore it; this is the "acceptance as commitment" obligation.[^c5]

Claims about the black box's hidden reasoning are not made. The source says there is "no claim that the relational substructures represent the true reasoning that is being executed by the black-box."[^c6] Trust therefore moves from one-off predictive performance to a continuous, checkable process.

Many surrogates can be adequate at once (the Rashomon effect). The remedy is to add auxiliary observables, such as feature-attribution scores, to the observation base. Adequacy is then demanded on a richer set, which shrinks the set of admissible surrogates without claiming access to real reasoning.[^c7] Choices of this kind (hypothesis class, compactness, auxiliary measures) are "pragmatic virtues", which pick among adequate theories by usefulness and not by truth.

Answering is separated from storing. An interface takes the current record and a query and returns an answer fitted to a stakeholder. Interfaces must not modify the record directly; an inconsistent new sample must go through the documented update. To avoid disagreement between outputs, an interface should keep traceability to the underlying observations and surrogate structure.[^c8]

## Proof of concept

The Constructive Box Theoriser (CoBoT) builds an axis-aligned box rule system online, using LIME attributions to restrict each rule to important dimensions. It was run on a 4x32 ReLU network for three-class Abalone, with validation accuracy 0.64. Across the stream, 187 observations triggered updates (4.5%), and the final system had fewer than 20 boxes.[^c9] Because adequacy is enforced, CoBoT fails explicitly when two observations are indistinguishable in the chosen subspace.

## Limits

- Only a demonstration on one small tabular model; no comparison with other surrogates, and no user study showing that stakeholders ask or answer better with the record.
- The black box is assumed fixed. A model that changes would need a different treatment, and the source defers this to its discussion.
- Adequacy covers observed points only and gives no guarantee on unobserved behaviour. Nothing here shows that the surrogate's rules reflect what the network actually computes.
- The link from stakeholder need to interface design is left to designers. Which questions a record should be able to answer is not derived.
- My inference, not the source's: the same split (a persistent store with update commitments, plus thin question-specific query layers) may suit question-and-answer systems more broadly. This was not tested.

## Related

- [[capability-auditability-tradeoff]] — both concern what is gained or lost when a system's behaviour is made auditable
- [[reasoning-faithfulness-observer-effect]] — a faithfulness question that this record sidesteps by claiming only observational adequacy

[^c1]: arxiv-2602-02215 — "producing isolated outputs that may need to be recomputed for similar questions and that can yield incompatible characterisations"
[^c2]: arxiv-2602-02215 — "Such a record is not itself an explanation, but a representational foundation from which diverse explanations can be derived."
[^c3]: arxiv-2602-02215 — "A SToBB consists of the following five components"
[^c4]: arxiv-2602-02215 — "This is stricter than typical surrogate modelling in XAI, where approximation error on observed data is tolerated"
[^c5]: arxiv-2602-02215 — "Adequacy is binary and"
[^c6]: arxiv-2602-02215 — "But there is no claim that the relational substructures represent the true"
[^c7]: arxiv-2602-02215 — "multiple surrogates can achieve perfect fidelity to the black-box while relying on different"
[^c8]: arxiv-2602-02215 — "interfaces must not directly modify the SToBB; instead, an update must"
[^c9]: arxiv-2602-02215 — "Across all observations, 187 updates were performed."
