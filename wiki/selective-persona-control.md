---
description: "A persona edit is selective only if it moves the target answer while non-target answers stay put; following the stated persona does not show that, a three-state test can."
aliases: ["selective control of persona attributes", "persona selectivity", "attribute-selective persona manipulation"]
sources: ["doi-10-48550-arxiv-2609-35036"]
---
# Selective persona control

Persona prompts are used to simulate users and to read a behavioural difference as the effect of one attribute. That reading needs the manipulation to be selective. The paper's wording is that "it must change the target attribute while preserving other" attributes intended to stay fixed.[^c1] A persona edit has two requirements: the target answer moves when the target attribute changes, and the answer on a non-target attribute stays stable when only the target changes, following that attribute's declared direction where one is given.

The distinction the paper draws is between persona following and selective persona control. Persona following is the first requirement with the stated persona as the reference: the model answers as the described user would. Selective control adds the second requirement, which following does not test. "A model can play the described user faithfully and still change more than the intended attribute."[^c2] A persona that is followed can still be a confounded manipulation.

The paper measures the second requirement with three quantities. Non-target sensitivity is the total variation distance between the non-target answer distributions at the two target levels, computed within each option order and label assignment and then averaged, so that opposite-sign effects do not cancel. A comparison counts as sensitive when that distance exceeds .15, and a prompt design preserves the non-target attribute when at most 5% of evaluation worlds contain a sensitive comparison.[^c3] Attribute fidelity is the distance from the non-target answer to its ground truth. Target efficacy is the movement toward the target-positive option when the target changes, which must stay above a prespecified floor relative to the bare prompt.[^c3]

Sensitivity alone is not enough. "A constant response that ignores Z is perfectly insensitive," so a model that ignores the non-target attribute passes the sensitivity measure while failing fidelity.[^c4] Selectivity therefore needs sensitivity to be low together with fidelity and efficacy.

The three-state diagnostic applies this to declarations. The non-target attribute is left unspecified, declared directional, or declared neutral. Directional tests measure persona following and target efficacy, and a model can pass them by following the stated direction. The neutral state is the one that exposes failures of selectivity: selective control requires non-target sensitivity within tolerance at every declared level, including the neutral one.[^c5] A neutral declaration needs no ground-truth answer for the non-target, only invariance to the target.[^c6] Where the neutral state fails, the failure is the [[neutrality-gap]].

## Limits

- The thresholds (a total variation of .15, a 5% share of worlds, a retention floor for target efficacy) are prespecified design choices. The paper does not show they are the right ones, and a different threshold would change which designs pass.
- Fidelity is defined only where a ground-truth non-target answer exists. Natural items fix no correct non-target answer, so the paper uses structured worlds built from a decision rule for that measure.[^c7]
- The prompt designs were chosen on validation worlds and tested once on held-out ones. The materials are English and text-only, so the diagnostic has not been shown on other languages or modalities.[^c8]
- The diagnostic detects a failure of selectivity; it does not name a unique cause. The paper's own statement is that the evidence "does not identify a unique inference algorithm" behind trait-conditioned completion.[^c9]

## Related

- [[neutrality-gap]] — the measured failure of the neutral state, where the diagnostic finds selectivity lacking
- [[persona-attribute-confounding]] — the same leakage described as a confound in persona-based measurement; this note states the requirement that the confound violates

[^c1]: doi-10-48550-arxiv-2609-35036 — "it must change the target attribute while preserving other"
[^c2]: doi-10-48550-arxiv-2609-35036 — "A model can play the described user faithfully and still change more than the intended attribute"
[^c3]: doi-10-48550-arxiv-2609-35036 — "A comparison is sensitive when its TV exceeds .15"
[^c4]: doi-10-48550-arxiv-2609-35036 — "a constant response that ignores Z is perfectly insensitive"
[^c5]: doi-10-48550-arxiv-2609-35036 — "selective persona control additionally requires non-target sensitivity"
[^c6]: doi-10-48550-arxiv-2609-35036 — "it needs only invariance to the target, not a ground-truth answer"
[^c7]: doi-10-48550-arxiv-2609-35036 — "Because natural items fix"
[^c8]: doi-10-48550-arxiv-2609-35036 — "Materials are English and text-only"
[^c9]: doi-10-48550-arxiv-2609-35036 — "does not identify a unique inference algorithm"
