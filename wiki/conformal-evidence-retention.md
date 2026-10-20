---
description: "A cut calibrated on the scores of known-relevant snippets keeps a stated share of relevant evidence in a RAG context, while top-k and fixed cosine cutoffs give no coverage control."
aliases: ["conformal context filtering", "coverage-controlled context filtering", "conformal snippet retention", "conformal context engineering"]
sources: ["arxiv-2511-17908"]
---
# Conformal evidence retention

A retrieval filter that keeps snippets by score can be given a coverage
target. Each retrieved snippet gets a nonconformity score, lower meaning more
relevant: here one minus the cosine between query and snippet embedding, or
one minus an LLM's relevance rating. A labelled calibration set of queries
then sets the cut. The threshold is the (1−α) empirical quantile of the scores
of the snippets labelled relevant, not of all snippets, and at test time a
snippet is kept when its score is at or below that threshold.[^c1][^c2]
Under exchangeability between calibration and test data, the share of relevant
snippets kept is guaranteed at least 1−α. The guarantee is marginal, a
property of the pooled relevant snippets rather than of each query.[^c3][^c4]

The construction is the split conformal recipe of [[conformal-prediction]],
with one change of object. A prediction set asks which labels a model cannot
rule out. A retention rule keeps the items that look relevant, and its
calibration uses only the positives, so the guarantee is a recall guarantee
on evidence and the size of the retained context is what the rule leaves
behind. The authors place the filter "immediately after retrieval," so that
the generator never sees the discarded snippets.[^c5] That placement is the
part of the design that distinguishes it from the post-generation calibration
the paper contrasts it with.

## Why a calibrated cut and not a fixed one

The mechanism that makes this useful is the comparison with the baselines the
paper runs on the same collection. Per-query top-k pruning "yields uncontrolled
coverage," and "Fixed cosine thresholds provide no coverage control and vary
widely across queries."[^c6][^c7] The problem is not that the cut is wrong on
average; it is that its coverage is unknown, and it changes from query to
query. A cut calibrated against labelled positives at a chosen α gives a single
number the operator can read off and move.

On the paper's NeuCLIR and RAGTIME runs, the two scoring functions (embedding
similarity, and a GPT-4o rating) "meet or slightly exceed theoretical coverage
guarantees" across the α range tested.[^c8] The paper reports that conformal
filtering "achieves target coverage while reducing context size," and that the
LLM score removes more context, though its removal rate moves in steps that
the authors tie to quantized ratings.[^c9][^c10]

The downstream claim is narrower. On NeuCLIR, ARGUE F1 with the unfiltered
baseline at 0.69 is improved by the strict filters and "remain[s]
indistinguishable from the baseline" at α = 0.20.[^c11][^c12] The authors read
this as evidence that "most discarded material is redundant or irrelevant,"
and conclude that "more than half of retrieved snippets can be pruned."[^c13][^c14]
The reading that fits the mechanism is that the generator, given less noise,
stops operating far from "its effective attention limit."[^c15]
See [[effective-context-length]].

## Limits

- The relevance labels are not human. They come from Llama 3.3-70B using a
  rubric prompt, and "A 10% subsample was manually reviewed to" check
  consistency.[^c16] The paper states that its guarantees "are conditional on
  label consistency across calibration and test topics."[^c17] A label
  drift between topics voids the guarantee the note describes.
- Exchangeability is assumed through topic splits: the calibration and test
  topics are disjoint, "using disjoint query topics for" the purpose of
  preserving it.[^c18] The paper names this as its open problem: future work is
  to "relax the exchangeability assumption."[^c19] Under topic or domain shift
  the threshold is not shown to hold.
- The nugget-based downstream measure exists only for NeuCLIR. For RAGTIME
  the paper says it is "evaluated only for coverage and removal behavior."[^c20]
  So the factual-quality result rests on one collection, one generator
  ("provided to the same Llama 3.3-70B generator"[^c21]), and one metric.
- The gains are small. The authors say "Although absolute gains are modest,"[^c22]
  and the significance they report comes from a paired bootstrap on one
  collection; no wider sweep of queries or generators is reported.
- The guarantee bounds the miss rate on relevant snippets, not the size of
  what is kept. How much context is removed is an output of how well the score
  separates the classes, and the note has no bound on it. The rate is also
  not conditional on a query, so a single hard query can lose all its evidence
  while the average holds.
- What is not tested here: whether the retained snippets are enough to answer
  the question. Coverage is about labelled snippets, and the answer quality
  is measured only through one downstream F1.

## Related

- [[conformal-prediction]] — the base construction; this note changes the set the quantile is taken over, from labels to positives only
- [[candidate-set-restriction-conformal-prediction]] — the other place where the size of a conformal set is set by the candidate space, not by the model's confidence
- [[adaptive-conformal-inference]] — the online recalibration that would answer the topic-shift limit; the paper only names it as future work
- [[effective-context-length]] — the attention limit the paper uses to motivate pruning
- [[context-recall-precision-tradeoff]] — the same trade between keeping evidence and keeping the context small; in this note the trade is a single calibrated knob (my reading)

[^c1]: arxiv-2511-17908 — "At test time, a snippet s is retained iff"
[^c2]: arxiv-2511-17908 — "the positive calibration"
[^c3]: arxiv-2511-17908 — "marginal coverage"
[^c4]: arxiv-2511-17908 — "assumption between calibration and test splits"
[^c5]: arxiv-2511-17908 — "applies conformal prediction immediately after retrieval"
[^c6]: arxiv-2511-17908 — "per-query top-k snippet pruning yields uncontrolled coverage"
[^c7]: arxiv-2511-17908 — "Fixed cosine thresholds provide no coverage control and vary widely across queries"
[^c8]: arxiv-2511-17908 — "meet or slightly exceed theoretical coverage guarantees"
[^c9]: arxiv-2511-17908 — "conformal filtering achieves target coverage while reducing context size"
[^c10]: arxiv-2511-17908 — "exhibits discrete jumps in removal rate due to its quantized confidence ratings"
[^c11]: arxiv-2511-17908 — "The unfiltered baseline achieves 0.69 F1"
[^c12]: arxiv-2511-17908 — "remain indistinguishable from the baseline at"
[^c13]: arxiv-2511-17908 — "most discarded material is redundant or irrelevant"
[^c14]: arxiv-2511-17908 — "indicating that more than half of retrieved snippets can be pruned"
[^c15]: arxiv-2511-17908 — "near its effective attention limit"
[^c16]: arxiv-2511-17908 — "A 10% subsample was manually reviewed to"
[^c17]: arxiv-2511-17908 — "guarantees are conditional on label consistency across calibration and test topics"
[^c18]: arxiv-2511-17908 — "using disjoint query topics for"
[^c19]: arxiv-2511-17908 — "to relax the exchangeability assumption"
[^c20]: arxiv-2511-17908 — "it is therefore evaluated only for coverage and removal behavior"
[^c21]: arxiv-2511-17908 — "provided to the same Llama 3.3-70B generator"
[^c22]: arxiv-2511-17908 — "Although absolute gains are modest"
