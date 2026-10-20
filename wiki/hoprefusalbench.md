---
description: "Across ten frontier search agents, correct halting on unanswerable multi-hop questions tops out at 43%, and search capability destabilizes correct refusals more than it rescues wrong ones."
aliases: ["HopRefusalBench", "Target-Aware Correct Halting Rate", "TCHR"]
sources: ["xie-2026"]
---
# HopRefusalBench

> Giving a search agent the ability to keep retrieving does not move it
> monotonically toward the right stopping decision: across ten frontier
> models, extra search more often turns a correct refusal into a wrong
> answer than it turns a wrong refusal into a correct one.

## Definition / Mechanism

Xie, Sun & Chen (2026) build 889 unanswerable multi-hop
questions from KILT entity paths, crossing three causes of unanswerability
— Answer Unknown, False Premise, Underspecified Context — with three
positions of the defect in an otherwise valid reasoning chain: Root (defect
first, masked by a plausible continuation), Middle (a broken bridge between
a valid prefix and a dependent suffix), and Terminal (defect only after all
prior hops resolve). "We introduce HopRefusalBench, the first controlled
benchmark of refusal within multihop search, comprising 889 unanswerable
questions constructed from KILT-grounded entity paths."[^c1]

Each model's final trajectory is scored into one of four behavioral
outcomes: "we classify each model's final behavior as Correct Refusal,
Pseudo-refusal, or Hallucination. Search-augmented evaluation adds Search
Exhaustion for trajectories that consume the full search budget without
producing a final response." Correct Refusal (TACH) requires naming the
gold reason (the false premise, the missing context, the unknowable
target); Pseudo-refusal (PPH/WRH/URH) is an [[abstention]] for the wrong or a
vague reason; Hallucination (SHD) answers past the defect. The headline
metric, TCHR, is the share of trajectories reaching TACH.[^c2]

Across ten proprietary and open-weight models in search-augmented mode:
"the best model achieves a target-aware correct halting rate (TCHR) of
only 42.9%." Most models score far lower, and the deficit is not evenly
distributed: "all ten models perform best on FP (17.1–59.0% TCHR), followed
by AU (11.0–27.4%), and worst on UC (1.2–11.6%)," and "Every model handles
Terminal items more reliably than Root or Middle items."[^c3]

The paper's central process finding compares each model with and without
search on the same questions: "Across models, search overturns 20.4–67.3%
of initially correct refusals but rescues only 4.2–16.9% of initially
non-target-aware outcomes."[^c4]

Pooled across categories, "84.7–98.4% of each model's explicit
refusal-like responses identify the correct rationale, localizing the main
bottleneck to committing to an appropriate non-answer; failed trajectories
instead diverge into hallucination or search-budget exhaustion."[^c5]

## Why it matters

For stall 2, this reframes "keep asking or stop" as a decision with a
measured downside: a search-augmented agent's own capacity to issue more
queries is not a free option on its halting decision — it is biased toward
overturning a correct refusal rather than repairing a wrong one. An agent
architecture that lets a generic policy decide whether to search again
after it has already recognized the right non-answer is, on this evidence,
more likely to talk itself out of that recognition than into it.

## Limits

Behavioral labels come from an LLM judge (GLM-5.1) with 87.2% agreement
against human raters on the four-way outcome and 95.3% on the existence of
a sufficient-evidence point — the per-trajectory numbers carry that noise
floor. The corpus is English, KILT/Wikipedia-2018-grounded, with explicit
thinking modes disabled on every model and an eight-search-call budget;
neither the 42.9% ceiling nor the override/rescue asymmetry has been shown
to hold with reasoning-mode models, other retrieval corpora, or a larger
search budget.

## Related
[[abstention]] · [[verification-aware-stopping]] · [[recognition-refusal-dissociation]] · [[sage-abstention-evaluation]]

[^c1]: xie-2026 — "We introduce HopRefusalBench, the first controlled benchmark of refusal within multihop search, comprising 889 unanswerable questions constructed from KILT-grounded entity paths."
[^c2]: xie-2026
[^c3]: xie-2026 — "the best model achieves a target-aware correct halting rate (TCHR) of only 42.9%."
[^c4]: xie-2026
[^c5]: xie-2026
