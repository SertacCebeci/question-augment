---
description: "Regenerate a text-to-model-to-simulation pipeline N times per document; Shannon entropy over the resulting outcome distribution flags source-text ambiguity for human clarification."
aliases: ["entropy-based uncertainty detector", "entropy-based ambiguity detector"]
sources: ["arxiv-2604-07817"]
---
# Outcome-distribution entropy detector

> Ask "is this document ambiguous" not by looking at what the model said, but
> at what its regenerated pipeline *did* when run to completion many times.

## Definition / Mechanism

Menaka Sekar et al. (2026) convert a policy document
into an executable BPMN process M times independently per LLM backend, run
each candidate model against the same population of synthetic patients, and
tabulate the resulting key-performance-indicator (KPI) combination each run
produces. Normalized Shannon entropy over the empirical distribution of these
KPI combinations — $H_{norm} = -\frac{1}{\log K}\sum_i p_i \log p_i$, $K$ the
number of distinct combinations observed — is the ambiguity score: 0%
means every regeneration reached the same downstream outcome; values near
100% mean the regenerations disagree almost uniformly. The entropy is not
taken over model tokens, answer text, or a single model's resamples — it is
taken over the terminal effect of executing each candidate artifact against
real data. High scores route the document to a human reviewer for
clarification rather than triggering the agent to ask a question itself:
"The entropy score serves as an ambiguity detector : high entropy flags
documents whose natural-language descriptions admit multiple valid
interpretations, directing human reviewers to the specific policies that
require clarification."[^c1]

The same statistic separates two causes of disagreement that a flat entropy
number alone would conflate. Random generation failures cluster as one
dominant mode plus a single outlier; genuine source-text vagueness produces
several comparably-sized clusters, because each cluster corresponds to a
distinct, defensible reading of the document rather than noise around one
reading: "The detector also distinguishes between LLM noise (random
generation failures that produce all-zero KPIs) and genuine policy
vagueness (multiple non-trivial KPI clusters corresponding to distinct but
defensible readings of the source text) through the shape of the KPI
distribution: noise manifests as a single outlier cluster alongside a
dominant mode, whereas genuine vagueness produces multiple comparably-sized
clusters."[^c2]

The detector is validated against an independent measure computed on the
same models: per-patient decision agreement (Cohen's κ) between each
generated model and a human-designed reference. Across three municipal
policy documents of increasing textual ambiguity, the entropy score and κ
move together without being computed from each other — entropy rises as κ
collapses: "Across all three cities, the pattern is consistent: κ tracks
the entropy-based uncertainty scores. City 1 (low entropy) yields
near-perfect κ; City 2 (moderate entropy) yields moderate κ with
LLM-dependent variation; City 3 (high entropy) yields near-zero κ
universally."[^c3]

## Why it matters

The signal needs no ground-truth label, no human-annotated ambiguity
judgment, and no confidence score from the generating model itself — it is
read entirely off the variance of independently regenerated *executable
artifacts* once they are run. That makes it cheap to attach to any pipeline
that already produces something executable or simulatable from text:
regenerate, run, measure the spread of what happened, not what was said.
It also converts "should a human be asked" from a per-document editorial
judgment into a monotone, document-intrinsic statistic — the entropy gap
between documents dwarfs the gap between the three LLM backends applied to
the same document, so the signal tracks the source text rather than which
model produced it.

## Transfer

| | |
|---|---|
| Home field | Information theory — Shannon entropy over a discrete outcome distribution |
| Here | Entropy over the KPI-combination outcomes of M independently regenerated and *executed* candidate process models for one document, thresholded to route the document to a human reviewer |
| What survives | Low entropy = agreement = no ambiguity; high entropy = disagreement = ambiguity, and the cluster-shape distinction between noise and genuine multi-reading vagueness |
| What does not | Any claim that the score identifies *which phrase* in the document is ambiguous, or that it works without an executable/simulatable downstream artifact to run — the entropy is computed on execution outcomes, not on text or on a single model's token distribution |

## Limits

Demonstrated on three documents from one domain (diabetic-nephropathy
prevention policy) and a restricted BPMN construct palette that excludes
parallel gateways, timers, and sub-processes, so whether the outcome-entropy
signal generalizes to other executable-artifact pipelines is unverified.
The detector flags a document for human review; it does not itself ask a
question or propose what to clarify — the paper's own future work notes
that automated ambiguity correction for entropy-flagged documents remains
undone. The per-run cost (M full regenerations, each simulated against a
full synthetic population) is not compared against cheaper single-pass
uncertainty proxies.

## Related

[[cross-model-answer-disagreement-entropy]], [[entropy-threshold-clarification-trigger]],
[[self-consistency-difficulty-score]], [[entropy]], [[semantic-entropy]]

[^c1]: arxiv-2604-07817 — "The entropy score serves as an ambiguity detector : high entropy flags documents whose natural-language descriptions admit multiple valid interpretations, directing human reviewers to the specific policies that require clarification."
[^c2]: arxiv-2604-07817 — "The detector also distinguishes between LLM noise (random generation failures that produce all-zero KPIs) and genuine policy vagueness (multiple non-trivial KPI clusters corresponding to distinct but defensible readings of the source text) through the shape of the KPI distribution: noise manifests as a single outlier cluster alongside a dominant mode, whereas genuine vagueness produces multiple comparably-sized clusters."
[^c3]: arxiv-2604-07817 — "Across all three cities, the pattern is consistent: κ tracks the entropy-based uncertainty scores. City 1 (low entropy) yields near-perfect κ; City 2 (moderate entropy) yields moderate κ with LLM-dependent variation; City 3 (high entropy) yields near-zero κ universally."
