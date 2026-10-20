---
description: "Calibrates a per-query confidence signal into a probability of correctness, then thresholds it to choose closed-book answering, compact or full retrieval, or abstention."
aliases: ["calibrated retrieval-budget allocation", "graded retrieval-budget allocation", "adaptive RAG as calibrated allocation"]
sources: ["dong-2026-know"]
---
# Calibrated retrieval-budget allocation

> Retrieval-augmented generation usually retrieves a fixed number of
> passages for every query. Dong, Shah, Qin & Wang (2026)
> turn that fixed policy into a graded decision: given a query, answer
> closed-book, retrieve a compact context (k = 1), retrieve a full context
> (k = 5), or abstain.[^c1]

## Definition / Mechanism

For each query, a frozen reader is run once without retrieval and a scalar
uncertainty signal is computed (length-normalized sequence log-probability,
or a prefix-logit signal such as TARG [[entropy]]/margin). A logistic calibrator
maps that scalar to a probability of correctness: "Given a scalar signal
si, such as length-normalized sequence log-probability, we fit a logistic
calibrator" $p_i = \Pr(y_i^{(0)}=1\mid s_i)=\sigma(\alpha s_i+\beta)$.[^c2]

Thresholding that probability selects the action: "A binary policy skips
retrieval when pi ≥ τ and otherwise retrieves k = 5. A graded policy uses
two thresholds" — closed-book above τ₀, compact retrieval between τ₁ and
τ₀, full retrieval below τ₁ — with a fourth action, [[abstention]], added when
the confidence of the answer the system would actually give is too low.[^c3]

The paper's central distinction is between what grading improves and what
it does not: "Graded allocation improves full-context and passage-budget
frontiers, but not retrieval-call frontiers" — because "k = 1 is still a
retrieval call," so a graded policy saves passage tokens and full-context
usage without reducing how often the system contacts the retriever at all.[^c4]

Out-of-fold calibration is not cosmetic: "for sequence log-probability, ECE
drops from 0.275 to 0.062 on TriviaQA, 0.643 to 0.009 on NQ, and 0.711 to
0.031 on MS MARCO."[^c5]

Sorting by the confidence of the answer actually returned (closed-book
confidence if skipped, a separate calibration of the k = 5 answer if
retrieved) yields a risk-coverage curve for abstention: "At 80% coverage,
TriviaQA accuracy improves from 80.8% to 86.0%, and NQ from 66.9% to
75.0%."[^c6]

Retrieving more is not monotonically better: "k = 10 is worse than k = 5
for both Qwen3-8B and Qwen3-32B" and "roughly 8.5% of examples correct at
k = 5 become wrong at k = 10," so budget should be allocated, not
maximised.[^c7]

A measured two-stage cost model (the closed-book probe is an added
generation pass) shows gating is not universally cheaper: "a measured cost
model reveals that gating is not universally faster: it increases latency
by about 27% on Qwen3-8B but saves about 8% on Qwen3-32B."[^c8]

## Transfer

| | |
|---|---|
| **In its home field** | ML calibration and selective prediction: a logistic calibrator fit on held-out data, thresholds swept on a validation split, a risk–coverage curve for the reject option. |
| **Here** | an asker/answerer choosing which axis to act on first — closed-book vs. retrieve, and how much evidence to gather before committing to an answer. |
| **What survives** | the probability interface (a calibrated scalar usable across actions and thresholds); graded, multi-action allocation instead of a single retrieve/skip bit; treating "any retrieval call" and "how much was retrieved" as separate cost axes; a named break-even condition before deploying a gate. |
| **What does not** | any certified risk bound (unlike SGR-style selective classification) — thresholds here are diagnostic operating points, not guarantees; the thresholds and the cost-model break-even point are per-model, per-dataset and batch-1/hardware-specific, so neither transfers unchanged to a new reader or serving stack. |

## Limits

- This note's claims rest on short-answer QA with alias-based correctness
  (TriviaQA, Natural Questions, MS MARCO); the paper itself flags that
  long-form answers would need evidence attribution and human evaluation,
  which this method has not been shown to handle.[^c9]
- The measured latency numbers (the 27%/8% figures) are batch-1 and
  hardware-specific; the authors note production batching, async retrieval
  and KV-cache reuse may shift the break-even point, so the direction of
  the cost trade-off is not fixed by this note.[^c10]
- Calibration can drift under domain shift, and the thresholds are fit
  per reader model — the same limit [[calibration]] already states for
  probability estimates generally.

## Related

[[calibration]] · [[abstention]] · [[reasoning-gap-driven-retrieval]] · [[value-of-information]]

[^c1]: dong-2026-know — "given a query, decide whether to answer closed-book, retrieve a compact context (k = 1), retrieve a full context (k = 5), or abstain"
[^c2]: dong-2026-know
[^c3]: dong-2026-know — "A binary policy skips retrieval when pi ≥ τ and otherwise retrieves k = 5. A graded policy uses two thresholds"
[^c4]: dong-2026-know — "Graded allocation improves full-context and passage-budget frontiers, but not retrieval-call frontiers"
[^c5]: dong-2026-know — "for sequence log-probability, ECE drops from 0.275 to 0.062 on TriviaQA, 0.643 to 0.009 on NQ, and 0.711 to 0.031 on MS MARCO"
[^c6]: dong-2026-know — "At 80% coverage, TriviaQA accuracy improves from 80.8% to 86.0%, and NQ from 66.9% to 75.0%"
[^c7]: dong-2026-know — "k = 10 is worse than k = 5 for both Qwen3-8B and Qwen3-32B"
[^c8]: dong-2026-know — "a measured cost model reveals that gating is not universally faster: it increases latency by about 27% on Qwen3-8B but saves about 8% on Qwen3-32B"
[^c9]: dong-2026-know — "Most experiments are on short-answer QA, where correctness can be judged with aliases. Long-form answers require evidence attribution and human evaluation."
[^c10]: dong-2026-know — "The measured latency numbers are batch-1 and hardware-specific; production batching, asynchronous retrieval, and KV-cache reuse may shift the break-even point."
