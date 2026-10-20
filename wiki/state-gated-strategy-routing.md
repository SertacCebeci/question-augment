---
description: "A diagnose-then-route tutor architecture that adaptively selects between two non-answering question strategies, audited to show no reliable quality gain over picking one strategy fixed."
aliases: ["ExplainRoute"]
sources: ["gai-2026"]
---
# State-gated strategy routing

> A programming tutor that first diagnoses a learner's explanation state and
> then routes to one of two bounded question strategies performs the
> routing safely, but a pre-deployment audit found no reliable quality
> advantage over simply picking one strategy and holding it fixed.

## Definition / Mechanism

Gai, Zhang & Huang (2026) build ExplainRoute, a two-role
teaching-assistant agent for Java code lines. A diagnostic role classifies a
learner's free-text explanation into one of four states and recommends a
strategy; a separate tutor role reads the code, the explanation and that
diagnostic record and selects exactly one bounded action: "Feynman-style
open self-explanation: ask the learner to reconstruct code behavior or
explain a small change in their own words" or "[[staged-socratic-hint-policy|Socratic]] scaffold: ask one
bounded question targeting the likely missing relation without stating the
answer." The tutor is informed by the diagnostic recommendation but not
bound to it, which is what lets the audit measure routing agreement rather
than merely enforcing it.[^c1]

A deterministic verifier checks each response's structural fields — state,
strategy, answer polarity, cited code, leakage risk — before it is accepted,
with no repair loop after verification: "the tutor role, implemented with
xhang_llm_qwen3-235b-a22b, receives the code, learner explanation, and
diagnostic record. It selects exactly one strategy."[^c2]

## Findings

Adaptive routing was audited offline against fixed-Open, fixed-Socratic, a
direct-answer baseline, and a no-state ablation on 443 held-out
explanation-code pairs. Its independent-judge quality score placed it above
the no-state ablation but not above either fixed strategy: "An independent
language-model judge rates adaptive responses 4.516/5 on a composite
rubric, above the no-state ablation (2.819/5) but slightly below fixed
open self-explanation (4.598/5) and Socratic scaffolding (4.658/5)." A
blinded human-rater replication of the same comparison found Adaptive
statistically tied with the fixed strategies rather than below them, but
"both evaluators therefore agree there is no reliable adaptive gain over
the fixed strategies."[^c3]

The routing decision itself tracked a frozen, score-derived reference rule
only weakly: "adaptive routing agrees with the frozen score-based
reference rule on 60.5% of records. Its state macro-F1 is 0.238, falling
between the two fixed strategies (Open 0.229; Socratic 0.246)" — the
diagnostic role systematically softened low-coverage explanations toward
"partial" or "adequate" instead of preserving the distinction the
reference rule needs.[^c4]

Routing was not free: "Operationally, Adaptive costs one additional
diagnostic call: its mean latency is 6.14 seconds, compared with 4.31
seconds for Direct, 3.89 seconds for Open, 3.63 seconds for Socratic, and
3.35 seconds for No-State." Adaptive selected Socratic for 336/443 records
(75.8%) and Open for 107/443 (24.2%), a lopsided split rather than a
finely calibrated per-item choice.[^c5]

## Why it matters

This is a controlled, negative result on the exact question this stall
asks: does estimating the respondent's state and adaptively picking a
question strategy from it beat committing to one strategy in advance? Here
the answer is no — not because adaptation is unsafe (contract validity was
100% in every condition) but because the state estimator was not accurate
enough to route better than a strategy fixed at design time, while still
costing an extra model call per turn.

## Transfer

| | |
|---|---|
| **Home field** | Software-engineering formal methods: a deterministic contract/verifier checks an output's structural fields against a schema and fails closed, with no post-hoc repair. |
| **Here** | Every tutor response — across all five audited conditions — is checked against a shared schema (state, strategy, answer polarity, cited code, leakage risk) before being counted; a malformed or answer-leaking output is rejected rather than corrected. |
| **What survives** | Full, fail-closed structural enforcement travels intact: contract validity reached 100% for both fixed and adaptive conditions, and every violation is retained rather than silently repaired. |
| **What does not** | The contract verifies structural polarity only — it "does not inspect cited-code locality or semantic leakage, which are measured as separate post-generation endpoints" — so it cannot certify that a routing decision was pedagogically good, only that it was well-formed. |

[^c6]

## Limits

- The paper states its own scope explicitly: "a validated audit protocol
  and a boundary finding, not a claim of improved learning, retention, or
  causal instructional effectiveness." The comparisons are offline proxy
  scores, not a classroom trial.[^c7]
- The state estimator's weak macro-F1 (0.238) means the "no reliable
  adaptive advantage" finding may reflect this particular diagnostic
  role's [[calibration]], not a ceiling on diagnose-then-route architectures
  in general — the authors themselves frame it as motivating future
  calibration work, not as a closed question.
- One domain (Java code-line explanations, the SelfCode corpus), one model
  pairing (a Qwen3-235B tutor with a separate diagnostic model); the
  four-valued [[possible-worlds|state space]] is inherited from the corpus's similarity
  labels, not a general learner model.
- The independent LLM judge and the three human teaching-assistant raters
  agreed on ranking but only "fair" on the full composite (quadratic-
  weighted κ = 0.32), with better agreement confined to the two
  dimensions that actually varied (actionability κ = 0.71, diagnosis
  κ = 0.57).

## Related

[[uncertainty-aware-multi-agent-scaffold]] · [[gated-socratic-scaffolding]] · [[non-advisory-dialogue]] · [[value-of-information]]

[^c1]: gai-2026
[^c2]: gai-2026
[^c3]: gai-2026 — "An independent language-model judge rates adaptive responses 4.516/5 on a composite rubric, above the no-state ablation (2.819/5) but slightly below fixed open self-explanation (4.598/5) and Socratic scaffolding (4.658/5)."
[^c4]: gai-2026 — "adaptive routing agrees with the frozen score-based reference rule on 60.5% of records. Its state macro-F1 is 0.238, falling between the two fixed strategies (Open 0.229; Socratic 0.246)"
[^c5]: gai-2026 — "Operationally, Adaptive costs one additional diagnostic call: its mean latency is 6.14 seconds, compared with 4.31 seconds for Direct, 3.89 seconds for Open, 3.63 seconds for Socratic, and 3.35 seconds for No-State."
[^c6]: gai-2026
[^c7]: gai-2026 — "a validated audit protocol and a boundary finding, not a claim of improved learning, retention, or causal instructional effectiveness."
