---
description: "A risk score whose sum weights are constrained non-negative can only rise as risk evidence accumulates, so one detected item sets a floor that benign context cannot dilute."
aliases: ["monotone risk head", "fail-closed evidence aggregation", "monotonicity constraint on a probabilistic circuit", "non-negative weight constraint", "no-dilution risk score"]
sources: ["doi-10-48550-arxiv-2603-17292"]
---
# Monotone risk aggregation

A risk score is built from a list of indicators: which kinds of sensitive item
appear, how linkable they are, how confident the extractor was. Ordinarily
nothing fixes how the score responds to adding one more indicator. A neural
head can let benign context pull the score down. The SEAL-Tag paper proposes a
head where that cannot happen. The score is the output of a probabilistic
circuit, a decomposable sum-product network over a latent variable R (Safe or
Unsafe) and binary evidence indicators. Its sum nodes are convex mixtures
weighted by non-negative parameters, and the parameters are constrained so the
output is monotone in the risk indicators.[^c1][^c2]

The mechanism is the constraint on the weights. The paper writes that it
"constrain[s] the non-negative weights w of all sum nodes such that" the
computed polynomial is monotone with respect to the risk indicators.[^c3] The
stated consequence is that the score "increases monotonically with the
accumulation of risk evidence."[^c4] The paper then reads the consequence as a
floor: if an indicator x_HIPAA is set, the posterior P(Unsafe) "is strictly
lower-bounded by the risk of that feature alone", and this holds "regardless of
any benign context features" that might otherwise dilute the risk in a standard
neural head.[^c5] Continuous inputs such as extractor confidence are binned
into monotone bins so that their ordering is preserved.[^c6] Inference stays
exact and cheap because the circuit is decomposable and smooth, which the paper
says makes it "typically executing in microseconds."[^c7]

The paper's motivation is a contrast with neural heads. It says the circuit
lets it "enforce hard logical constraints (e.g., monotonicity and k-anonymity)
that neural networks cannot guarantee."[^c8] Its claim is that the circuit is
"mathematically interpretable and calibrated."[^c9]

The transfer beyond privacy is my inference, not the paper's. Any decision
that releases or withholds an answer on the basis of accumulated evidence could
use the same shape: a score that a benign addition cannot lower, so a single
disqualifying fact keeps its weight. The asker or answerer who needs this would
then have to decide which indicators are "risk" indices, since the guarantee
covers only those.

## Limits

- **The guarantee is about the score, not the system.** The indicators are
  filled in by an LLM. The paper says "the LLM is tasked solely with evidence
  extraction,"[^c10] so an entity the extractor misses is never an indicator,
  and monotonicity cannot protect it. The "cannot fail open" property holds
  only once the indicator is set.
- **Monotone in each indicator is not the same as capturing joint risk.** A
  monotone function can encode interactions, but the constraint does not force
  them. Mosaic-style risk, where two quasi-identifiers are dangerous together
  and neither alone is, must be built into the circuit's structure. The paper
  addresses this through its linkability fields, and I did not check how well
  that works. See [[compositional-inference-leakage]].
- **Fail-closed has a cost the constraint does not price.** The same property
  that stops benign context from diluting a risk also stops a false positive
  from being retracted by later evidence. The paper claims high utility, and
  its own table lists the utility of SEAL-Tag as "High," but that is the
  authors' claim. The evaluation sections were not read for this note, so no
  over-refusal figure is reported here.
- **Calibration and speed are the authors' claims.** The introduction states
  that the head "achieves perfect calibration and microsecond-scale inference."[^c11]
  No calibration measurement was read for this note.
- **Monotone is not a gate.** The floor is a lower bound on risk, not a veto.
  A compensating gain elsewhere still changes the score above the floor, so the
  head does not fix the reversal problem that
  [[compensatory-leakage]] describes for ordered criteria.

## Related

- [[compensatory-leakage]] — an ordered-criteria reversal, where lower-priority gains overturn a decision. A monotone floor gives a risk indicator a similar protection against dilution, but as a lower bound, not a priority.
- [[compositional-inference-leakage]] — the mosaic case that a per-indicator monotone score does not give for free.
- [[provenance-gated-assertion]] — caps a claim's voice by how it was obtained; the monotone head caps nothing and only refuses to let risk fall.
- [[monotone-recalibration-operating-point-shift]] — a different monotone: a map on the output that keeps ranking and moves thresholds. Here the monotonicity is in the inputs, and the output ranking is what the constraint protects.

[^c1]: doi-10-48550-arxiv-2603-17292 — "Probabilistic Circuit C encodes a joint probability distribution"
[^c2]: doi-10-48550-arxiv-2603-17292 — "Sum Nodes ( ): Represent a convex mixture of children"
[^c3]: doi-10-48550-arxiv-2603-17292 — "We constrain the non-negative weights w of all sum nodes such that"
[^c4]: doi-10-48550-arxiv-2603-17292 — "score increases monotonically with the accumulation of risk evidence"
[^c5]: doi-10-48550-arxiv-2603-17292 — "regardless of any benign context features"
[^c6]: doi-10-48550-arxiv-2603-17292 — "discretized into monotone bins to preserve ordinality"
[^c7]: doi-10-48550-arxiv-2603-17292 — "ensure that this inference is exact and tractable, typically executing in microseconds"
[^c8]: doi-10-48550-arxiv-2603-17292 — "that neural networks cannot guarantee"
[^c9]: doi-10-48550-arxiv-2603-17292 — "PCs are mathematically interpretable and calibrated"
[^c10]: doi-10-48550-arxiv-2603-17292 — "the LLM is tasked solely with evidence extraction"
[^c11]: doi-10-48550-arxiv-2603-17292 — "Our PC head achieves perfect calibration and microsecond-scale inference"
