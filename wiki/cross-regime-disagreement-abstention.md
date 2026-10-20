---
description: "Abstain when a model's direct answer conflicts with its answer under a task-equivalent decomposition; this catches fragile hallucinations via recall but misses errors stable across regimes."
aliases: ["Disagreement-Based Abstention", "DBA", "decomposition-based consistency probe"]
sources: ["arxiv-2602-04853"]
---
# Cross-regime disagreement abstention

The same closed-book multi-hop question is answered under two executions of one fixed, verified decomposition: Direct (one call, implicit reasoning), Assistive (all sub-questions given as context, one call) or Incremental (sub-questions answered one call at a time). Because the decomposition is the gold plan, a disagreement between regimes cannot be blamed on planning: it is read as an error in knowledge or in executing it.[^c1] The policy (DBA) is minimal: answer Direct, answer once more by decomposition, and say "I don't know" whenever the two final answers differ, with semantic equivalence judged by an LLM.[^c2]

## The premise

The authors' rationale is that stored knowledge is reproducible across reasoning paths while a hallucination is not: "Because factual knowledge is typically stable while hallucinations are stochastic".[^c3] Decomposition is therefore used as a probe, not a booster. Accuracy gains from it shrink with scale: non-frontier models gain, while frontier models show "diminishing or negative returns".[^c4] The authors describe a utility shift: scaffold for weak models, auditor for strong ones, in which cross-regime agreement becomes a stronger accuracy indicator.

## What it was measured to do

Across nine LLMs and six multi-hop QA sets, with errors in the Direct answer as the positive class, DBA beat the "Are you sure" (AYS) self-check baseline on F1 in 17 of 18 model-dataset pairs shown.[^c5] The gain comes mostly from recall: self-reported confidence misses hallucinations the model is confident about, whereas a hard veto on disagreement raises recall by 30 to 50 points on harder sets and open models (Llama-3.3-70B on Bamboogle: 37 to 90). AUROC stayed above chance, from the mid-0.60s to low 0.90s, which the authors take as showing DBA is not merely abstaining more.[^c6] It needs no training and no retrieval, and relies on exhibited behavior rather than stated confidence, at the price of extra model calls (Table 4 reports the call and token multipliers).

## Where it fails and what complements it

When a frontier model's errors are consistent, no disagreement appears: "such as CRAG, frontier models can produce stable" wrong answers, and DBA recall drops.[^c7] When accuracy is already high (Mintaka), errors are rare and the signal sparse, so AYS stays competitive. The two detectors fail on opposite cases: AYS catches stable-but-uncertain errors, DBA catches confident-but-fragile ones. On GPT-5.1 and CRAG, AYS beat DBA-A alone (66 vs 53 F1) yet "their union achieves" 75 F1.[^c8] My inference: agreement is evidence of a reproducible belief, not of a true one, so this signal only bounds fragile error.

## Limits

- The decomposition is gold and manually verified. In deployment a model must plan itself, and then planning errors would also create disagreement; the paper does not test this.
- Only closed-book multi-hop factual QA, with an LLM judge deciding equivalence; judge error is not separated out.
- Error detection is scored against the Direct answer only. Cost is roughly several calls per question versus one for single-call baselines.
- Consistent errors (common in frontier models on hard sets) are invisible by construction.
- The "factual knowledge is stable" premise is an assumption motivating the method, not independently tested here.

## Related

- [[selective-abstraction]] — the abstain-or-answer framework this policy instantiates.
- [[stepwise-self-qa-scaffold]] — sub-question scaffolding, here repurposed as a probe.
- [[inconsistency-penalized-confidence]] — another self-inconsistency signal; it fixes level, not ranking.
- [[self-consistency-difficulty-score]] — agreement across samples as a difficulty signal.

[^c1]: arxiv-2602-04853 — "Cross-regime"
[^c2]: arxiv-2602-04853 — "the two final answers are conflicting"
[^c3]: arxiv-2602-04853 — "Because factual knowledge is typically stable while hallucinations are stochastic"
[^c4]: arxiv-2602-04853 — "diminishing or negative returns"
[^c5]: arxiv-2602-04853 — "DBA outperforms the AYS baseline"
[^c6]: arxiv-2602-04853 — "showing that it effectively separates incorrect answers from correct ones."
[^c7]: arxiv-2602-04853 — "such as CRAG, frontier models can produce stable"
[^c8]: arxiv-2602-04853 — "their union achieves"
