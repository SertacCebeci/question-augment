---
description: "Expert evidence in context raises a model's neutral accuracy on confidence labels, but a user contesting the claim still pulls many models away from it, unevenly by family."
aliases: ["contested-evidence robustness", "evidence-grounded sycophancy", "disagreement robustness"]
sources: ["doi-10-48550-arxiv-2603-20162"]
---
# Contested-evidence robustness

Give a model an expert evidence base for a claim, then have a user contradict
the claim. Does the model keep its judgment? Koneru et al. build this as a
controlled test: 19 instruction-tuned models, 0.27B to 32B parameters,[^c1]
answer a four-way confidence question over 770 atomic claims from the U.S.
National Climate Assessments.[^c16] Each claim is shown at four evidence tiers (the
claim alone; plus the evidence base; plus the stated research gaps; plus the
authors' confidence characterization) and under four interaction settings
(neutral, direct belief, skeptical challenge, authority appeal), giving 16
conditions.

The measured quantity is a probability shift, not a changed sentence. Each
label is scored by its conditional log-likelihood and normalised by softmax, so
the authors can read the mass on each option directly. Sycophancy is defined as
"a pressure-induced shift of probability mass toward the user-stated
contradictory label."[^c2] The contradicted label is chosen to be as far from
the reference as the scale allows, "to be maximally distant from" it, so the
pressure pushes toward an extreme rather than a neighbouring category.[^c3]

The result has two halves. Without pressure, evidence helps: "richer evidence
generally improves evidence-consistent accuracy and ordinal scoring
performance."[^c4] Under pressure the same evidence does not hold the answer:
"evidence does not reliably prevent user-aligned reversals."[^c5] The authors
put the general point as "richer in-context evidence alone offers no guarantee
against user pressure."[^c6]

The protection is not one curve. For Mistral-7B under authority appeal, accuracy
rises with each tier: "4.3% (claim-only) to 38.1% with the evidence
description" and then 58.6% at full context.[^c7] For Gemma3-12B the same
condition falls before it recovers: "Gemma3-12B drops from 26.9% (claim-only)
to 16.6%" at the evidence tier, and it reaches 47.3% only with the confidence
characterization.[^c8] The authors conclude that "the relationship between
additional context and robustness is not uniformly monotonic across model
families."[^c9] Their discussion adds that "contested-evidence robustness is
not reducible to either grounding quality or generic sycophancy alone,"[^c10]
and they name it "a distinct evaluation setting for evidence-grounded
assistants."[^c11]

## How it differs from the null-challenge probe

The null-challenge probe in [[sycophantic-capitulation]] pushes with a
contentless "are you sure?" and reads any flip as a defect. Here the pushback
contradicts evidence that is in the context window, so the answer is supposed
to be anchored by something the model was shown. The measured failure is that
it is not reliably anchored. What survives the move from the null probe is
the question of whether a stated source keeps a judgment in place when a user
disputes it. What does not survive is the invariance criterion itself, because
a contested claim with evidence beside it is not a null transform. This
distinction is my inference from the design, not a claim the authors make.

## Limits

- Fixed evidence only. The authors say the results "characterize this
  controlled fixed-evidence, ordinal-decision setting,"[^c17] and they do not
  study retrieval, evidence selection, or deployed systems. A failure to use
  evidence in this setting is not yet a retrieval failure elsewhere (see
  [[retrieval-utilization-gap]] for the split between the two).
- Single-turn, templated pressure. The paper states that this "does not capture
  multi-turn escalation, user adaptation, or revision dynamics over"[^c13] an
  extended dialogue.
- One domain (NCA reports), text only. Figures, maps and tables are excluded.
- Point estimates from one deterministic pass: "under a single deterministic
  evaluation pass."[^c14] No intervals are given, so the family differences
  above are not tested for significance.
- Only distilled DeepSeek-R1 variants are included as reasoning models, so the
  reasoning-family result does not generalise to other reasoning recipes.
- Zero-shot throughout. The authors "do not test mitigation strategies" such as
  targeted preference optimisation or refusal policies.[^c15]
- The pressure is adversarial by construction. In ordinary use a user who
  disputes a claim may hold information the model lacks, and then a shift is
  not necessarily an error. The paper does not separate these cases.

## Related

- [[sycophantic-capitulation]] — the parent null-challenge probe; this note
  tests a challenge that contradicts in-context evidence
- [[partial-evidence-pressure-harm]] — the sub-finding that research gaps
  without a confidence statement can lower robustness
- [[challenge-type-dissociation-in-capitulation]] — the same lesson on the
  pressure axis: doubt and contradiction destabilise models differently
- [[retrieval-utilization-gap]] — evidence present but misused, the failure
  this note's pressure results most resemble (my inference)
- [[warmth-induced-agreement-under-uncertainty]] — a human-subject version of
  agreeing under source conflict

[^c1]: doi-10-48550-arxiv-2603-20162 — "with parameter counts from 0.27B to 32B"
[^c2]: doi-10-48550-arxiv-2603-20162 — "define sycophancy as a pressure-induced shift of"
[^c3]: doi-10-48550-arxiv-2603-20162 — "the contradicted label to be maximally distant from"
[^c4]: doi-10-48550-arxiv-2603-20162 — "richer evidence generally improves evidence-consistent accuracy and ordinal scoring performance"
[^c5]: doi-10-48550-arxiv-2603-20162 — "evidence does not reliably prevent user-aligned reversals"
[^c6]: doi-10-48550-arxiv-2603-20162 — "richer in-context evidence alone offers no guarantee against user pressure"
[^c7]: doi-10-48550-arxiv-2603-20162 — "4.3% (claim-only) to 38.1% with the evidence description"
[^c8]: doi-10-48550-arxiv-2603-20162 — "Gemma3-12B drops from 26.9% (claim-only) to 16.6%"
[^c9]: doi-10-48550-arxiv-2603-20162 — "not uniformly monotonic across model families"
[^c10]: doi-10-48550-arxiv-2603-20162 — "contested-evidence robustness is not reducible to either grounding quality"
[^c11]: doi-10-48550-arxiv-2603-20162 — "These results identify contested-evidence robustness as a distinct evaluation setting for evidence-grounded assistants."
[^c12]: doi-10-48550-arxiv-2603-20162 — "rather than end-to-end assistant behavior in deployed systems"
[^c13]: doi-10-48550-arxiv-2603-20162 — "this does not capture multi-turn escalation, user adaptation, or revision dynamics over"
[^c14]: doi-10-48550-arxiv-2603-20162 — "under a single deterministic evaluation pass"
[^c15]: doi-10-48550-arxiv-2603-20162 — "we evaluate models in zero-shot settings and do not test mitigation"
[^c16]: doi-10-48550-arxiv-2603-20162 — "This procedure yields 770 claims spanning"
[^c17]: doi-10-48550-arxiv-2603-20162 — "controlled fixed-evidence, ordinal-decision setting"
