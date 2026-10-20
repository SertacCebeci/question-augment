---
description: "Restricting conformal candidates to tokens that can be correct shrinks 847-token sets to about 4, but validity holds only while the true token stays inside the restricted set."
aliases: ["vocabulary-aware conformal prediction", "VACP", "vocabulary masking for conformal prediction", "candidate-space restriction"]
sources: ["arxiv-2512-22682"]
---
# Candidate-set restriction in conformal prediction

A conformal set is built from a candidate space: every candidate whose score
passes a threshold calibrated on held-out data is kept. The paper's point is
that for next-token prediction the candidate space is the vocabulary, and its
size alone can make the set uninformative even when the guarantee holds.
Under the adaptive variant (APS), a token is scored by the cumulative
probability of the tokens ranked at or above it, and tokens are included until
the calibrated threshold is crossed.[^c2] On Gemma-2B with a vocabulary of
256,000 tokens and α = 0.1, standard APS reached 91.2% empirical coverage, but
its mean set held 847 tokens.[^c1] The mechanism the authors give is the tail:
"including tokens until cumulative probability mass exceeds a calibrated
threshold."[^c3] Thousands of near-zero-probability tokens add up in the
cumulative sum, so the set grows with the vocabulary rather than with the
model's doubt.[^c4]

## What the restriction does

The method, VACP, shrinks the candidate space in two steps. A structural
filter removes tokens that cannot occur as natural-language continuations
(control, reserved and non-printable tokens, 1,847 in this tokenizer). An
empirical filter, run on a separate validation split, removes tokens that never
receive probability above 10⁻⁵; this step removes 198,432 tokens.[^c10] The
authors then renormalize over the remaining vocabulary and apply a temperature
to the logits. Temperature preserves token order, so the rank of the true token
does not change; only the renormalized masses do.[^c7]

The ablation separates the two pieces. The mask alone brought the mean set to
142 tokens at 90.8% coverage, which the authors call "substantial improvement
but still yields sets too large for practical use."[^c5] Temperature alone on
the full vocabulary gave a mean of 3.1 tokens, but at 76.4% coverage.[^c6][^c18]
Both together gave 4.3 tokens at 89.7% coverage.[^c18] So neither piece alone
is the result: the mask removes the tail, and the temperature makes the
remaining mass concentrated enough for the threshold to bite.

## Validity condition

The argument for why restriction is safe is a bound rather than an equality.
If the true label lies in a restricted set V* with probability p, conformalizing
over V* at error α gives coverage at least (1 − α)·p over the full vocabulary.[^c8]
With p = 1 the full (1 − α) guarantee is recovered. The paper's p = 1 is not
derived; it is checked on a validation split, where all ground-truth tokens fell
inside V*.[^c11] Section 4.2 then says the vocabulary is "provably" complete for the
evaluation domain; in my reading that word rests on the empirical check alone.[^c12]

What survives the transfer, in my reading and not a tested claim: a set's size
depends on the candidate space it is drawn from, not only on the model's
confidence. Two systems with the same score and the same coverage can give very
different set sizes if one of them ranges over a much larger space. The price is
that the guarantee now depends on a property of the space (here, that the truth
is in it), which calibration does not check on its own.

## Limits

- The authors name the central assumption themselves: "The primary limitation
  is the assumption that ground-truth".[^c17] The assumption is that the true
  token lies in V* with probability 1.[^c13] Domain shift breaks it, and the
  authors say "extreme domain shifts (e.g., code generation, non-English text)
  would" need domain-specific vocabularies.[^c14]
- The bound (1 − α)·p is loose by construction: it multiplies the coverage
  down by p even where the truth is almost always inside V*. The proof also
  takes the APS guarantee to hold conditionally on Y ∈ V*. The text does not
  justify that the calibration exchangeability carries over to that conditioned
  event. This is my reading of the proof, not a result the paper flags.
- Temperature is a free parameter, and coverage is sensitive to it. In the
  paper's sweep, τ = 0.05 gives 72.3% coverage and τ = 0.1 gives 89.7%.[^c18]
  The guarantee is stated for a fixed score; the text does not explain why a
  calibrated temperature drops coverage below target. The authors say the
  range "should be validated on a held-out calibration set for new
  applications."
- Coverage is marginal. In the confidence-stratified check, the low-confidence
  stratum covered 88.1% with mean set size 7.2.[^c15] The conditional coverage
  of single inputs is not established.
- One model (Gemma-2B), two datasets (SQuAD, WikiText-103), and token-level
  prediction only. The paper names sequence-level extension as future work.[^c17]
  On transfer, the SQuAD mask and temperature applied to WikiText gave 88.4%
  coverage with mean set 6.7; recalibrating on WikiText gave 90.1% with 5.9.[^c16][^c18]
  No open-ended answer or multi-token response was scored.
- The implementation is said to be released, but the text gives only a
  placeholder URL; the claim is not checked here.

## Related

- [[conformal-prediction]] — the base framework; this note changes the candidate space the guarantee ranges over, not the guarantee itself
- [[conformal-set-size-calibration-tradeoff]] — set size tied there to calibration quality; here to the size of the candidate space
- [[mondrian-conformal-prediction]] — class-conditional coverage, the other route to a per-group guarantee
- [[sequence-level-conformal-prediction]] — the multi-token extension the paper names as future work
- [[conformal-candidate-prompting]] — the same kind of restriction over classes chosen by a cheap classifier, used to shape an LLM prompt and to skip the call when the set is a singleton

[^c1]: arxiv-2512-22682 — "naive conformal prediction achieves valid coverage but produces prediction sets"
[^c2]: arxiv-2512-22682 — "including all labels y in C(Xn+1) for which s(Xn+1, y)"
[^c3]: arxiv-2512-22682 — "including tokens until cumulative probability mass exceeds a calibrated threshold."
[^c4]: arxiv-2512-22682 — "model produces prediction sets containing hundreds or thousands of tokens"
[^c5]: arxiv-2512-22682 — "substantial improvement but still yields sets too large for practical use."
[^c6]: arxiv-2512-22682 — "adjustment (row 3) applied to the full vocabulary achieves small sets but fails to maintain"
[^c7]: arxiv-2512-22682 — "temperature scaling preserves the ranking of tokens"
[^c8]: arxiv-2512-22682 — "the resulting prediction sets achieve marginal coverage at least"
[^c10]: arxiv-2512-22682 — "The resulting effective vocabulary V* contains 55,721 tokens"
[^c11]: arxiv-2512-22682 — "This holds for 100% of samples, confirming p = 1 for our setting."
[^c12]: arxiv-2512-22682 — "provably containing all ground-truth labels in our evaluation"
[^c13]: arxiv-2512-22682 — "Our approach assumes the ground-truth token lies in V* with probability 1."
[^c14]: arxiv-2512-22682 — "extreme domain shifts (e.g., code generation, non-English text) would"
[^c15]: arxiv-2512-22682 — "Coverage is consistent across confidence strata, demonstrating that VACP does not"
[^c16]: arxiv-2512-22682 — "The method maintains valid coverage on WikiText-103 despite being calibrated on SQuAD."
[^c17]: arxiv-2512-22682 — "The primary limitation is the assumption that ground-truth"
[^c18]: arxiv-2512-22682
