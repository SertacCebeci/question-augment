---
description: "Low confidence in a reasoning trace becomes a reflection trigger: generation pauses, a guided self-review is spliced into the partial trace, and decoding resumes instead of stopping."
aliases: ["Reflective Confidence", "ReflectiveConf", "confidence-triggered self-correction", "reflection trigger on low confidence"]
sources: ["arxiv-2512-18605", "arxiv-2511-19900"]
---
# Confidence-triggered reflection

A low-confidence reading during decoding can be used in two ways. Early
stopping reads it as a termination signal: the path is cut, and the tokens
already spent on it are lost. Confidence-triggered reflection reads the same
reading as a correction signal. The path is not abandoned: "it does not
abandon it."[^c1] The model is asked to look at what it has just written and
continue from a corrected point.

The mechanism, concretely. A token confidence is the log-likelihood averaged
over the top-k most probable next tokens, "computed as the log-likelihood
averaged" over that high-probability subset.[^c2] A group confidence is the
expectation of token confidence over a causal sliding window of the last n
steps, "defined as the expectation of token confidence over" that window.[^c3]
The window is a smoothing step. The paper describes the result as "yielding a stable, low-pass filtered signal that" detects sustained model uncertainty, the kind it links to profound errors, rather than single noisy tokens.[^c18] Its Figure 2 labels a window of 2048 tokens.[^c4]

The threshold is calibrated, not set by hand. A warmup set of traces gives "an
empirical distribution of minimum" group confidence reached in each trace, and
the threshold is a percentile of that distribution.[^c5] In the experiments the
threshold sits "at the 10th percentile of the lowest" group confidences of the
warmup traces.[^c6]

When the group confidence at step i* falls below that threshold, generation
pauses. The tokens up to i* become a partial path. A reflection prompt is then
built from the original question, the partial path, and an instruction to find
the error or uncertainty and give a corrected continuation, "tasking the model
with self-review."[^c7] The model's output for that prompt is a corrective
segment. It is concatenated to the partial path, and "Autoregressive generation
resumes from the end of this" corrected trajectory until completion.[^c8]

What the measurements show. All experiments use Qwen3-8B on AIME 2025, a set
of high-school-level competition math problems.[^c9] At K=32 paths, the paper
reports 83.3% accuracy for the method, against 73.3% for its reimplemented
DeepConf early-stopping baseline and 70.0% for Self-Consistency. The method's
token total in that setting is 18.0M, against 15.6M for DeepConf and 16.7M for
Self-Consistency (values read from Table 1). The authors describe the gain
over Self-Consistency as coming "with only a marginal increase in computational
cost."[^c10]

The paper also defines a salvage rate: "the percentage of intervened paths"
that end in a correct answer.[^c11] By my reading, a path that is discarded, as
DeepConf does it, is not in that count at all, so the rate measures only what the intervention recovers. The restart variant "salvages 35.4% of
failures," and the guided method reaches "a much higher 65.8% Salvage Rate."[^c12]

A verifier's confidence can play the same gating role. In Agent0-VL the trigger is not a decoder's token reading but the confidence a Verifier attaches to a finished step. The repair gate is a sigmoid of the gap between a threshold and that confidence: "The repair gate at step t is defined as" a sigmoid of the threshold minus the confidence, scaled by a temperature.[^c19] When the gate opens, the Verifier writes a repair instruction and the Solver regenerates that segment. The text does not say how the threshold is set, so it is not calibrated on warmup traces as here. The gate is also priced: the step reward subtracts a term that "penalizes unnecessary repairs."[^c20] The paper does not compare its trigger with a token-confidence trigger, so the contrast is one of mechanism, not a measured difference.

The intervention's content matters, not only its trigger. The restart variant
keeps the same trigger but, instead of a reflection prompt, "simply backtracks
to the last sentence" and regenerates from there.[^c13] It reaches 76.7%, against
83.3% for the guided method and 73.3% for discarding (Table 2). The authors
attribute the gain to "guided reflection mechanism over naive re-generation."[^c14]

## Limits

- One benchmark and one model. The experiments are on AIME 2025 with Qwen3-8B.
  The conclusion names code generation and scientific discovery as "potential
  applications in" those domains; the text does not test them.[^c15]
- Small differences in a small test. The reported accuracies are multiples of
  1/30 (for example 83.3 is 25 of 30), which is my reading and not stated in the
  text. A three-point gap is three problems. The text reports no variance,
  repeat runs or significance test.
- The efficiency claim is narrower than its caption. The Table 1 caption says
  "ReflectiveConf surpasses Self-Consistency in accuracy and efficiency."[^c16]
  At K=32 the table shows 18.0M tokens for the method and 16.7M for
  Self-Consistency, so the efficiency advantage is not visible in that row. The
  claim holds against early stopping's cost and at K=2, where the figures are
  0.89M and 0.87M (my reading).
- The threshold percentile (10th) and the window length were not varied in the
  text. Whether the calibrated threshold transfers to a different model or a
  different task depends on the warmup traces being representative; the text
  does not test that.
- The qualitative case is one problem. The authors say of the intervention
  there: "The subsequent reflection is not a perfect" solution.[^c17] Its success
  is one illustration, not a rate.
- The baselines were reimplemented by the authors, and the text does not say
  whether warmup tokens are counted in the token totals.
- The verifier-confidence gate in Agent0-VL is not tested against a token-confidence gate, and its threshold and repair cost are not varied in the slices read. The same shape can be built from either signal; which one better separates a wrong step from a right one is not established here.

## Related

- [[sequence-likelihood-confidence]] — the whole-sequence mean token probability, measured as a routing signal; this note's signal is windowed and used online, mid-trace
- [[confidence-gated-query-decomposition-tree]] — a confidence gate that splits a failing node instead of reflecting on it, the same discard-or-repair choice in retrieval
- [[earliest-error-truncation-correction]] — truncate-and-regenerate on a reviewer's finding of the first error, not on an online confidence reading
- [[self-repair-anchoring]] — a conflicting result: conditioning a code model on its own failed attempt cost accuracy against blind resampling, while here the guided variant beat a plain restart; the two differ in model, task and what is conditioned on, so neither settles the other
- [[sigma-triage-regenerate-or-abstain]] — the same threshold-then-regenerate shape, applied to a finished answer rather than to a trace in progress
- [[answer-first-confidence-gated-reasoning]] — token confidence also gates whether reasoning is generated, but decides before reasoning, not during it
- [[tool-grounded-self-verification]] — the same gated-repair shape, but the gating confidence belongs to a verifier that has already checked the step with tools, not to the decoder's own token readings

[^c1]: arxiv-2512-18605 — "it does not abandon it"
[^c2]: arxiv-2512-18605 — "computed as the log-likelihood averaged"
[^c3]: arxiv-2512-18605 — "defined as the expectation of token confidence over"
[^c4]: arxiv-2512-18605 — "Window Size: 2048 tokens"
[^c5]: arxiv-2512-18605 — "we derive an empirical distribution of minimum"
[^c6]: arxiv-2512-18605 — "The confidence threshold s is set at the 10th percentile of the lowest"
[^c7]: arxiv-2512-18605 — "tasking the model with self-review"
[^c8]: arxiv-2512-18605 — "Autoregressive generation resumes from the end of this"
[^c9]: arxiv-2512-18605 — "We conduct all experiments on the AIME 2025"
[^c10]: arxiv-2512-18605 — "with only a marginal increase in computational cost"
[^c11]: arxiv-2512-18605 — "the percentage of intervened paths"
[^c12]: arxiv-2512-18605 — "Conf-Restart salvages 35.4% of failures"
[^c13]: arxiv-2512-18605 — "simply backtracks to the last sentence"
[^c14]: arxiv-2512-18605 — "guided reflection mechanism over naive re-generation"
[^c15]: arxiv-2512-18605 — "with potential applications in"
[^c16]: arxiv-2512-18605 — "ReflectiveConf surpasses Self-Consistency in accuracy and efficiency"
[^c17]: arxiv-2512-18605 — "The subsequent reflection is not a perfect"
[^c18]: arxiv-2512-18605 — "yielding a stable, low-pass filtered signal that"
[^c19]: arxiv-2511-19900 — "The repair gate at step t is defined as"
[^c20]: arxiv-2511-19900 — "penalizes unnecessary repairs"
