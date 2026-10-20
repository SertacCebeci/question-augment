---
description: "In Qwen3-4B, certainty is the transcoder network's default, carried by shared features; uncertainty is a sparse override, and overconfidence is what happens when it fails to fire."
aliases: ["sparse override", "certainty default mechanism"]
sources: ["mazzaccara-2026"]
---
# Certainty-default sparse override

> The model does not have a "certain" circuit and an "uncertain" circuit of
> equal weight; it has a default and an override, and overconfidence is what
> the default does whenever the override does not fire.

## Definition / Mechanism

Mazzaccara, Bertolazzi & Bernardi (2026) localize, in
Qwen3-4B's middle layers (20–29), the transcoder features that distinguish
certainty from uncertainty expression on controlled logical-inference
stories, separating **selectivity** (which features fire more for one
condition) from **causal contribution** (which features actually push the
next-token logit). The two diverge: "certainty-specific features contribute
almost nothing to the certainty token, whereas uncertainty-specific features
supply the bulk of the push to the uncertainty token. Certainty therefore
has no dedicated subnetwork reaching the logit; it is the network's default,
carried by a broad coalition of shared middle-layer features. Uncertainty is
its sparse override: a small, dedicated group of uncertainty-specific
features that takes over the push only when the prompt licenses it."[^c1]

Causal interventions confirm the asymmetry is not merely correlational.
Boosting the top-20 uncertainty features on 34 samples where the model
wrongly answered with certainty produces a graded rescue: "none at 1×, 23/34
at 1.5×, and ≈ 94% (32/34) from 2.5× on, with P(uncertain) rising from 0.11
to 0.95."[^c2]

The converse ablation is asymmetric in the direction the mechanism predicts:
"suppressing the same top-20 uncertainty-specific features on correct
uncertainty samples drives uncertainty expression from 99% correct down to
0%, whereas the symmetric suppression of the top-20 certainty-specific
features on certainty samples leaves certainty at 100%" — removing the
override collapses uncertainty; removing the (non-existent) certainty-specific
push changes nothing, because certainty was never routed through it.[^c3]

The same 20 features generalize outside the token-level setting they were
found in: boosted ×3 on committed-answer errors, "30 of the 82
committed-answer errors flip to 'I don't know', lifting [[abstention]] accuracy
from 72.7% to 82.7%" — the features encode uncertainty abstractly enough to
surface as abstention, not just as an epistemic marker.[^c4]

On a third, numeric confidence-score format the same boost is far weaker:
"at ×3 only 1 of the 241 overconfident errors crosses below 5 (19.7% →
20.0%)... The score-5 probability mass is already saturated (mean P(5) =
0.95 on the error cases), so the features cannot move the prediction."[^c5]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Interpretability (this paper) | sparse override | exact |
| Interpretability (this paper) | default certainty mechanism | exact |

[^c6]

## Transfer

| | |
|---|---|
| In its home field | mechanistic interpretability: contrastive selectivity (Cohen's d on transcoder feature activations) combined with causal attribution (direct logit attribution) to find and validate an intervention target, following AlKhamissi et al. (2025) |
| Here | a causal, not merely correlational, account of *why* an answerer overcommits on stall 10: overconfidence is the default path firing because a small override circuit failed to engage, not a general miscalibration |
| What survives | the asymmetry finding itself — that a rescue intervention on a small feature set generalizes across three different surface expressions (epistemic markers, abstention, modality task) and two languages, which licenses treating "hedge/abstain" as one abstract decision with several output channels rather than three separate ones |
| What does not | the numeric confidence-score channel — the mechanism transfers weakly to it (§ above), so a single override circuit does not explain overcommitment uniformly across every way an answerer can report uncertainty |

[^c7]

## Limits

- One model (Qwen3-4B, non-thinking mode) and one dataset family (Li et al.
  2025's controlled stories); the authors themselves flag model scale and
  chain-of-thought as untested moderators.[^c8]
- The causal-contribution scoring keeps only features whose selectivity and
  logit-push directions agree, which by the authors' own account
  underestimates the mechanism by excluding features that diverge on the
  two measures — this wiki's summary above therefore likely undercounts, not
  overcounts, the machinery involved.
- Interpreting transcoder features inherits the general limits of that
  method (cited by the authors to Hanna et al. 2025 and Lindsey et al.
  2025); this note does not independently establish that limitation.

## Related

[[abstention]] · [[calibration]] · [[knowledge-verbalization-dissociation]] · [[gated-activation-steering-for-abstention]]

[^c1]: mazzaccara-2026
[^c2]: mazzaccara-2026 — "Boosting the top-20 uncertainty features at generation time on the 34 uncertainty error samples produces a graded rescue: none at 1×, 23/34 at 1.5×, and ≈ 94% (32/34) from 2.5× on, with P (uncertain) rising from 0.11 to 0.95"
[^c3]: mazzaccara-2026
[^c4]: mazzaccara-2026 — "The same top-20 uncertainty features, boosted ×3 on error cases only, generalize to the abstention setting: 30 of the 82 committed-answer errors flip to “I don’t know”, lifting abstention accuracy from 72.7% to 82.7%"
[^c5]: mazzaccara-2026 — "at ×3 only 1 of the 241 overconfident errors crosses below 5 (19.7% → 20.0%, Fig. 2). The score-5 probability mass is already saturated (mean P (5) = 0.95 on the error cases), so the features cannot move the prediction."
[^c6]: mazzaccara-2026 — "Default Mechanism vs. sparse override"
[^c7]: mazzaccara-2026 — "On the numeric setting the same boost has a monotonic but negligible effect: the expected score drifts down monotonically with the multiplier, yet at ×3 only 1 of the 241 overconfident errors crosses below 5"
[^c8]: mazzaccara-2026 — "Our analysis is restricted to a single model, Qwen3-4B, and to its non-thinking mode. Recent studies demonstrate that either more parameters (Xiong et al., 2024; Li et al., 2025) and chain-of-thought reasoning (Podolak and Verma, 2025) mitigate overconfidence."
