---
description: "BCEA turns a calibrated answer/abstain filter into answer/abstain/acquire, spending a bounded evidence budget on borderline claims while re-calibration keeps the hallucination-rate guarantee."
aliases: ["BCEA", "Budgeted Conformal Evidence Acquisition"]
sources: ["xu-2026-look"]
---
# Budgeted Conformal Evidence Acquisition (BCEA)

> A conformal filter that only ever answers or abstains pays for its
> guarantee in refusals; BCEA adds a third move — spend a fixed compute
> budget looking again — and shows that move must be *folded into the
> calibrated score itself*, not bolted on after, or the guarantee silently
> breaks.

## Definition / Mechanism

Xu, Wu, Zeng, Paisley & Zhao (2026) start from a baseline
selective predictor (ConfLVLM-style): a claim's grounding score is
conformally calibrated so that asserted claims carry a distribution-free
hallucination-rate bound. That baseline is expensive: "to hold it below 5%
on balanced object-existence claims, a conformal grounding filter must
abstain on over 80%."[^c1]

BCEA replaces the binary decision with a three-way one, realized by a
single gate: run the acquisition views (B zoomed crops, or a claim-type
intervention such as a horizontal flip) only when the base grounding score
falls in a pre-fixed borderline band; otherwise answer or abstain on the
base score directly — "so only borderline claims spend budget." The
resulting post-acquisition score, not the base score, is what gets
thresholded.[^c2]

The paper's central finding is that this folding is not optional:
"acquisition plugged naively into a calibrated filter breaks the
guarantee — it destroys the exchangeability conformal [[calibration]] relies
on — but folding the whole acquisition policy into the score and
re-calibrating restores the finite-sample guarantee while recovering
coverage." Calibrating a threshold on the pre-acquisition score and then
swapping in post-acquisition scores at test time (the "obvious" naive
approach) violates the risk guarantee on almost every split; the fix is to
treat the acquisition policy — crops, interventions and the gate together
— as part of the score function that gets calibrated.[^c3]

The validity of the fixed policy is a theorem, not an empirical claim:
"Exact BCEA is proven valid by Theorem 1, whose guarantee is the
false-certification probability ≤ δ," giving Pr[R(τ̂) > α] ≤ δ exactly
when the acquisition policy is fixed before the calibration sample is
observed.[^c4]

Certified (gated, Bonferroni-corrected) BCEA "clearly beats [[abstention]] at
α≥0.10 (0.32 vs. 0.23; 0.42 vs. 0.28), at ≈2 extra passes/claim," at the
cost of roughly two additional forward passes per borderline claim.[^c5]

## Known as

| Field | Name there | Match |
|---|---|---|
| The paper's own system name | BCEA | exact |
| Spelled out in the paper's title | Budgeted Conformal Evidence Acquisition | exact — same object |

[^c6]

## Why it matters

This is a stopping/acquisition rule for stall 2 (which evidence to seek
next) built on a distribution-free guarantee rather than a heuristic
threshold: instead of asking "is this good enough to answer?" once, it
asks "is this good enough to answer, good enough to acquire more evidence
for cheaply, or hopeless?" — and proves that only a specific recipe (fold
the acquisition action into the calibrated score before thresholding)
keeps that decision's risk certificate valid. Any asking pipeline that
adds an "acquire more evidence" action to a calibrated abstain filter — not
just vision-language claims — inherits the same exchangeability trap the
paper's Proposition 1 names.

## Transfer

| | |
|---|---|
| **In its home field** | [[crc-confident-error-control|Conformal risk control]] / selective prediction (Angelopoulos et al. 2024-line) certifies a fixed threshold on a fixed score; it says nothing about a decision (like acquisition) computed adaptively from the same data the score will be calibrated on |
| **Here** | Used as a bounded-budget rule for when to seek more evidence before answering or abstaining, with the guarantee stated as a [[stopping-rules|stopping condition]] on stall 2 |
| **What survives** | The requirement — any policy, however elaborate, that touches the score must be fixed *before* the calibration sample is observed and folded into the score function itself, or exchangeability between calibration and deployment breaks |
| **What does not** | The guarantee says nothing about which axis to acquire evidence on beyond the paper's fixed visual actions (crop, flip); per-claim budget allocation across claims is shown coverage-neutral here, not beneficial, so the theorem does not license adaptive budget spending as a source of gain |

## Limits

The certified ("exact") variant is validated on object-existence and
spatial-relation claims built from COCO annotations with two open VLM
backbones (LLaVA-1.5-7B main, Qwen3-VL-7B for generality); the "practical"
variant that reaches higher coverage is explicitly anti-conservative (up to
2× the target risk) and is not the guaranteed one. The theorem requires
the acquisition policy to be fixed before the calibration sample and
requires exchangeability between calibration and deployment claims — the
same assumption [[conformal-abstention-floor]] rests on and that is known
to fail under distribution shift. The source is an arXiv preprint not yet
peer-reviewed (v4, 2026-07-21) and is listed `unverified` pending the
wiki's source verification.

## Related

[[conformal-abstention-floor]] · [[abstention]] · [[question-conditioned-evidence-acquisition]] · [[calibration]] · [[value-of-information]]

[^c1]: xu-2026-look — "to hold it below 5% on balanced object-existence claims, a conformal grounding filter must abstain on over 80%"
[^c2]: xu-2026-look — "it runs the B acquisition views only when the base grounding s falls in the pre-fixed borderline band [τ − , τ + ] (a label-free, calibration-independent test), and answers/abstains on s directly otherwise—so only borderline claims spend budget."
[^c3]: xu-2026-look
[^c4]: xu-2026-look — "Exact BCEA is proven valid by Theorem 1, whose guarantee is the false-certification probability ≤ δ."
[^c5]: xu-2026-look — "clearly beats abstention at α≥0.10 (0.32 vs. 0.23; 0.42 vs. 0.28), at ≈ 2 extra passes/claim."
[^c6]: xu-2026-look — "Budgeted Conformal Evidence Acquisition (BCEA)"
