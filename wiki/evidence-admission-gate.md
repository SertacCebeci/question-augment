---
description: "Abstention applied one step before the answer — whether retrieved evidence is admitted into an agent's context at all — under a reward that penalizes wrong admission more than it rewards missed reuse."
aliases: ["memory-injection abstention", "pre-answer evidence gate", "risk-sensitive memory control"]
sources: ["arxiv-2604-27283"]
---
# Evidence-admission gate

> The failure is not always a wrong answer — sometimes it is a piece of
> evidence let in.

## Definition / Mechanism

Iscan (2026) studies an LLM coding agent that retrieves
a past debugging memory before answering, and asks not "should the agent
answer" but "should this retrieved memory be allowed into the context the
agent will then read": "This paper reframes issue-memory use as a
selective, risk-sensitive control problem rather than a pure top-k
retrieval problem." Its controller (RSCB-MC) chooses among seven
actions — no memory, inject top result, summarize several candidates,
retrieve high-precision or high-recall, abstain, or ask for feedback —
scored by a risk-regularized objective that subtracts an estimated
false-positive probability and a cost term from an expected-reward term,
then applies a safety override that can force abstention or no-memory
regardless of the raw score.

The reward that trains this score is built asymmetric by construction:
"γ>α>β is a design invariant. A false-positive memory injection is more
harmful than a successful accepted reuse is beneficial." From this the
paper derives, as an algebraic (not probabilistic) consequence of the
reward's own definition, the condition under which withholding dominates
injecting: "For a fixed context zt, a non-injection action aA has greater
expected reward than an injection action aI exactly when" the weighted sum
of the false-positive, rejection and correct-abstention terms exceeds the
weighted sum of the verified- and accepted-reuse terms — so a moderate
false-positive probability, under the invariant γ>α>β, is already enough
to flip the optimal action to abstention or no-memory.[^c3]

What makes the gate a distinct object from an answer-time abstention rule
is where it sits in the pipeline: "We borrow the core idea but move the
decision boundary one step earlier... The controller is not deciding
whether the LLM should answer; it is deciding whether a retrieved memory
should be inserted into the prompt that the LLM will then read."[^c4]

## Why it matters

An answer-time abstention gate ([[gated-answerability-rule]],
[[abstention]]) protects the last step of a pipeline: whatever evidence
the answerer already holds, it decides whether to commit. The
evidence-admission gate protects an earlier step: it decides whether a
candidate piece of evidence is even allowed to become part of what the
answerer holds. The two are not the same failure surface — a wrong final
answer is visible and can be flagged or rolled back, but a wrongly
admitted piece of evidence is invisible and biases every reasoning step
downstream of it. The paper's ablation makes the earlier gate's
contribution measurable: removing abstention and forcing the controller
to commit on every ambiguous case raised the false-positive rate from
0.0% to 17.5% and collapsed cumulative reward from −31.740 to −87.800.[^c5]

## Limits

- The "decision boundary" derivations are explicitly not theorems: the
  paper itself labels them algebraic consequences of a chosen reward
  function, not proofs of policy optimality over a full task trajectory.
- Reported results (62.5% non-oracle success, 0.0% false positives) come
  from deterministic, local, smoke-scale replay and proxy metadata rather
  than live user feedback or a causal online deployment — [?].
- On the 56-case abstention benchmark the gate is over-conservative:
  under the reported threshold it wrongly abstains on 42.9% of cases even
  while correctly abstaining on 57.1% — the asymmetric penalty that
  eliminates false positives also eliminates some true positives, and the
  paper names calibration of the boundary, not removal of the gate, as
  the fix.
- The false-positive judgment itself is supplied by replay/proxy metadata
  in the reported artifacts, not by an independent verifier — unverified.

## Related

[[abstention]] · [[gated-answerability-rule]] · [[dynamic-value-thresholding]] · [[precondition-risk-gate]] · [[conformal-abstention-floor]]

[^c3]: arxiv-2604-27283 — "For a fixed context zt , a non-injection action aA has greater expected reward than an injection action aI exactly when"
[^c4]: arxiv-2604-27283 — "We borrow the core idea but move the decision boundary one step earlier in the pipeline. The controller is not deciding whether the LLM should answer; it is deciding whether a retrieved memory should be inserted into the prompt that the LLM will then read."
[^c5]: arxiv-2604-27283 — "the false-positive rate jumps from 0.0% to 17.5% and cumulative reward collapses from -31.740 to -87.800."
