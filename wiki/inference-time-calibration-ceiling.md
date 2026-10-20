---
description: "Three progressively stronger inference-time RAG pipelines all plateau near 35% commit/ask/abstain accuracy; supervised finetuning of the same base model clears the ceiling."
aliases: ["ceiling of inference-time interventions", "epistemic passivity through finetuning"]
sources: ["arxiv-2604-04565"]
---
# Inference-time calibration ceiling

> An answerer's decision to commit, ask or abstain does not improve by
> making its retrieval and reasoning pipeline smarter — only by retraining
> the model that makes the decision.

## Definition / Mechanism

Baidya (2026) evaluates three progressively more
sophisticated retrieval-augmented QA pipelines — a standard RAG baseline,
an enhanced version with semantic chunking, hybrid retrieval,
cross-encoder reranking and self-reflection, and a decision-aware version
(v3) adding a hard confidence/coverage gate — on a fixed three-way routing
task: Answer, Ask (clarify) or Abstain, given a query and a knowledge
base. "All three plateau at 34–38% decision accuracy and below 14%
Abstain recall, with a consistent failure mode: the model defaults to
Answer regardless of the information state."[^c1]

Improving retrieval quality alone does not help and can hurt: the
enhanced pipeline added five non-trivial improvements over the baseline
yet matched its accuracy and macro F1 exactly, while its hallucination
rate rose from 42.7% to 51.7% — "demonstrating that better retrieval
without a decision gate increases overconfident answering."
[^c5]

Adding an
explicit hard gate (v3) is the only inference-time change that moves any
metric, but even it tops out: "Even v3 achieves only 38% accuracy and
13.3% Abstain recall, establishing a clear upper bound on what can be
achieved without model-level adaptation."[^c2]

The same base model, LoRA-finetuned on 9,000 graph-grounded
reasoning-chain examples (supervised, not RL) to output the same
three-way decision explicitly, clears that ceiling: "The finetuned
planner achieves 55.6% macro F1 on the held-out test split, compared to
35.3% for the best inference-time architecture (v3). This 20.3 pp gain
confirms the central thesis: decision behaviour must be internalised at
training time."
[^c3]

The gain concentrates in the action inference-time
gating could not touch: Abstain recall "rises substantially from 13.3%
(v3) to 58.1%, confirming that the graph's empty-node signal is learnable
through training in a way that inference-time thresholds cannot
replicate."[^c4]

## Why it matters

This separates two families of fix for an answerer that over-commits: a
better retrieval or scoring pipeline wrapped around a fixed model, and a
change to the model's own weights. The paper's controlled comparison — same
base model, same test queries, only the intervention point differs — finds
the first family saturates well short of the second, specifically on the
hardest action (abstaining on an irrecoverably absent topic). A system
designer choosing where to spend effort on commitment behaviour gets a
concrete answer: past a point, more inference-time machinery is not the
lever.

## Limits

- One base model (Mistral-7B-Instruct), one architecture family (LoRA
  SFT vs. three RAG variants), one domain (multi-source QA over a built
  knowledge graph); whether the ceiling generalizes to larger models or
  other decision-gating designs is untested here.
- The finetuning result is reported as "a conservative lower bound rather
  than a ceiling" — 2 epochs over 9,000 of the available 34,000 training
  samples — so the true training-time ceiling is unmeasured, which
  weakens (in the paper's favor) but does not undercut the inference-time
  vs. training-time comparison itself.
- Single run per condition; no variance or significance test is reported
  for the accuracy and recall deltas — [?].

## Related

[[abstention]] · [[detection-to-abstention-gap]] · [[gated-answerability-rule]] · [[calibration-training]] · Commitment

[^c1]: arxiv-2604-04565 — "All three plateau at 34–38% decision accuracy and below 14% Abstain recall, with a consistent failure mode: the model defaults to Answer regardless of the information state"
[^c2]: arxiv-2604-04565 — "Even v3 achieves only 38% accuracy and 13.3% Abstain recall, establishing a clear upper bound on what can be achieved without model-level adaptation."
[^c3]: arxiv-2604-04565 — "The finetuned planner achieves 55.6% macro F1 on the held-out test split, compared to 35.3% for the best inference-time architecture (v3). This 20.3 pp gain confirms the central thesis: decision behaviour must be internalised at training time."
[^c4]: arxiv-2604-04565
[^c5]: arxiv-2604-04565
