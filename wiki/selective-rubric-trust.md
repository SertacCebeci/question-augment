---
description: "A verifier given a rubric follows it only when it judges the rubric helpful, and otherwise reverts to rubric-free judging; the work reports this stays robust when most rubrics mislead."
aliases: ["critical verifier", "selective inference with rubrics", "rubric rejection at inference", "conditional rubric use"]
sources: ["openalex-org-w7154789980"]
---
# Selective rubric trust

A verifier handed a rubric has two options: follow it or judge without it. The work gives the verifier a third step that makes the choice on each rubric. It is a "critical verifier to assess rubric validity before making its judgment, following only rubrics it deems helpful at inference time."[^c1] Put plainly, the verifier reads the rubric, decides whether to trust it, and if it does not, "reverts to rubric-free" evaluation.[^c2]

The trust judgment is part of the verifier's own reasoning, not a separate filter. The verifier is trained with reinforcement learning "to reason about which response is better and whether to trust the rubric."[^c3] Its training data includes examples where the rubric helps and examples where it misleads, so the verifier learns both to follow a useful rubric and to drop a misleading one. The work's test of this is the case where most of the rubrics given at inference are wrong: "selective inference maintains robustness even when most input rubrics" are misleading.[^c4]

The point for the two-sided effect (see [[two-sided-rubric-influence]]) is that a rubric's average effect no longer has to set the verifier's accuracy. If the verifier can refuse the bad rubrics, the low-quality tail costs less. The work also describes a fallback: "the retry mechanism may invoke a second rubric-free inference when rubrics are flagged as misleading."[^c5] The trust decision therefore has a direct cost in a second inference, which the paper counts against its method.

Training matters for this to work. In the ablations, the variant without misleading examples "trains both components without misleading rubrics", and the text reports that "Removing misleading rubrics causes" a measurable drop in the ablation results.[^c6][^c7] The claim is that the verifier must see rubrics it should reject in order to learn to reject them. A verifier trained only on helpful rubrics has no example of the failure it is meant to catch.

## Limits

- The robustness result is for the paper's own trained verifier and its own rubric generator. The note has not seen a test of a general-purpose verifier that reads the same rubrics without this training.
- The trust judgment depends on the base model's reasoning. The paper warns that "weaker models may struggle to reliably distinguish helpful from misleading" rubrics, "leading to unnecessary rejection of useful" guidance.[^c8][^c9] Below some capability, the filter throws away good rubrics as well as bad ones.
- The gain is not free. Rubric generation and a possible second rubric-free inference both add compute; the paper lists this as a limitation. Its conclusion says the gains stem from the design, not from extra compute, and that selective inference keeps the verifier robust.[^c10] The note has not checked that analysis itself.
- No formal guarantee is given that the verifier rejects every misleading rubric. The robustness is an empirical result on the benchmarks used.
- Whether the same selective behaviour appears when the rubrics come from humans, rather than from the paper's generator, is not established in the parts read.

## Related

- [[two-sided-rubric-influence]] — the effect this trust decision is meant to filter
- [[shift-labelled-rubric-contrast]] — the measured labels that train the trust judgment
- [[prover-verifier-deliberation]] — a verifier that challenges a proposed answer before accepting it; a different setting with the same question of when a verifier should accept guidance
- [[conversational-maxims]] — Grice's cooperative principle, the human-communication theory the work cites as its inspiration

[^c1]: openalex-org-w7154789980 — "a critical verifier to assess rubric validity before making its judgment"
[^c2]: openalex-org-w7154789980 — "rubrics it deems helpful and reverts to rubric-free"
[^c3]: openalex-org-w7154789980 — "to reason about which response is better and whether"
[^c4]: openalex-org-w7154789980 — "selective inference maintains robustness even when most input rubrics"
[^c5]: openalex-org-w7154789980 — "the retry mechanism may invoke a second rubric-free inference"
[^c6]: openalex-org-w7154789980 — "w/o Negative Rubrics trains both components without misleading rubrics"
[^c7]: openalex-org-w7154789980 — "Removing misleading rubrics causes"
[^c8]: openalex-org-w7154789980 — "weaker models may struggle to reliably distinguish helpful from misleading"
[^c9]: openalex-org-w7154789980 — "leading to unnecessary rejection of useful"
[^c10]: openalex-org-w7154789980 — "than increased compute, and selective inference"
