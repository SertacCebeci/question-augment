---
description: "A group-testing-inspired wrapper that evaluates a per-query confidence estimator on cluster medoids, propagates scores to lookalike queries, then rescues only the highest-disagreement cases."
aliases: ["POOL", "Propagated Uncertainty Over Lookalikes", "group-testing confidence estimation"]
sources: ["sharma-2026"]
---
# POOL (Propagated Uncertainty Over Lookalikes)

> Confidence estimation over a whole query batch does not need one full
> estimator call per query when the batch is not a set of unrelated
> questions — a group test on the cluster is often enough.

## Definition / Mechanism

Given any per-query black-box confidence estimator $M$ with cost $g_M$
generations per call, POOL wraps it in two tiers. Tier 1 clusters query
stems in an embedding space with overlaps allowed, picks one medoid per
cluster, and calls $M$ only on the $K$ medoids ($K g_M$ generations —
"the Tier-1 floor cost"); every other query's score is a softmax-weighted
average $\mu_i$ of the medoid scores within a similarity threshold, with
weights $w_k(i)$ that also yield a free per-query disagreement statistic
$d_i$ (the weighted standard deviation of the medoid scores feeding
$\mu_i$), computed with no extra generations.[^c1]

Tier 2 spends a user-set rescue
fraction $q$: the top $\lceil qN\rceil$ non-medoid queries by $d_i$ are
evaluated directly with $M$ and their score overwritten. Expected cost per
query is $(c+q)\,g_M$ with $c=K/N$; at $q=0$ only the Tier-1 floor is paid,
at $q=1-c$ the unpooled estimator is recovered exactly.[^c2]

The method is explicitly adapted from Dorfman's classical group testing —
"expensive tests can be shared across groups and followed by targeted
tests only where needed" — applied to confidence estimation for the first
time, per the authors.[^c3]

Instantiated with a hybrid base estimator
[[hy-hybrid-confidence-estimator|HY@5]], POOL retains 93.4–97.9% of the
unpooled estimator's AUROC while saving 19.3–39.3% of generations across
six domains, three benchmarks and five black-box LLMs; on paraphrase-dense
workloads the savings rise to 73–76%.[^c4]

## Why it matters

This is a mechanism for the cost side of the deferral decision: an agent
that must decide whether to abstain, route to a stronger model, or send a
case to human review (stall 10) needs a confidence score for every item in
a batch, and sampling-based scores are the most discriminative but scale
linearly per query. POOL turns semantic redundancy in the query batch — a
property of real workloads (benchmarks, tutoring systems, support logs)
that per-query treatment discards — into a cost reduction that does not
touch which base estimator is used, so it composes with whatever scoring
rule stall 10 already uses. It also bears on stall 7 (is $|W|$ small
enough) and stall 4 (who answers next): the disagreement statistic $d_i$
is a free, per-query signal for exactly the queries where routing to a
stronger source is worth the extra cost, at zero marginal generations
until Tier 2 triggers.[^c5]

## Transfer

| | |
|---|---|
| **Home field** | classical group testing (Dorfman, 1943): a population of items, one property (defective/not) per item, tests are pooled to find defectives with fewer tests than items |
| **Here** | queries in an embedding space, no binary defective label — a continuous confidence score approximated by cluster medoids and refined by disagreement |
| **What survives** | the amortization principle itself (share one expensive test across a group; test only where the group result is unreliable) and the two-tier structure (a cheap floor pass, a targeted rescue pass) |
| **What does not** | group testing's combinatorial guarantee of exact [[recovery-postulate|recovery]] from pooled binary outcomes — POOL's medoid score is a soft, weighted approximation with no recovery guarantee, and the rescue trigger ($d_i$) is an empirical heuristic, not a proven bound on estimation error |

## Limits

- Reported gains are relative to each method's own unpooled base estimator,
  averaged across cells; the rescue fraction $q$ and cluster cutoff $\tau$
  are stated as "not tuned" deployment knobs, so the AUROC-vs-savings curve
  is what these fixed settings produce, not a swept optimum.[^c6]
- Evaluated only on confidence-as-ranking (AUROC), not on calibrated
  probabilities — the paper states this explicitly.[^c7]
- The compression ratio $K/N$ depends on how much genuine semantic
  redundancy the query batch has; the large savings on paraphrase-dense
  workloads do not generalize to batches of genuinely unrelated queries.

## Related

[[abstention]] · [[semantic-entropy]] · [[sequence-likelihood-confidence]] · [[hy-hybrid-confidence-estimator]]

[^c1]: sharma-2026 — "Base evaluation on medoids. We invoke M once per medoid, sk = M (xmk ), consuming KgM generations — the Tier-1 floor cost."
[^c2]: sharma-2026
[^c3]: sharma-2026 — "Classical group testing exploits a related principle: when items are structured, expensive tests can be shared across groups and followed by targeted tests only where needed (Dorfman, 1943)."
[^c4]: sharma-2026 — "With H Y @5 as the base estimator, POOL retains 93.5–97.9% of unpooled AUROC while saving 39.3%, 29.3%, and 19.3% of confidence-estimation generations as the rescue budget increases."
[^c5]: sharma-2026 — "No extra compute is required, di reuses the values already in Eqs. 3–4."
[^c6]: sharma-2026
[^c7]: sharma-2026 — "We study confidence estimation as a ranking problem, that is, the goal is to assign scores that separate likely-correct from likely-incorrect outputs, not to produce calibrated probabilities."
