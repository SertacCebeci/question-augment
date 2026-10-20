---
description: "Where to measure: rank candidate sites by the expected drop in epistemic (reducible) variance rather than total variance, which on one dataset favoured noisy regions over ambiguous ones."
aliases: ["expected reduction in epistemic uncertainty", "epistemic-driven sensor placement", "Δ_Ep acquisition", "reducible-variance acquisition"]
sources: ["arxiv-2511-22567"]
---
# Reducible-uncertainty acquisition

> Where to measure: score each candidate site by how much of the model's
> uncertainty a measurement there is expected to remove, counting only the
> part that more data can remove.

## Mechanism

Sensor placement chooses a few sites from a finite candidate set, and the
objective cannot be evaluated during placement because target labels are
not available.[^r1] So the choice runs through an acquisition function: a
score that stands in for the utility of a measurement at each site.[^r1]
Because the number of subsets explodes, placement is done greedily: pick
the best site, add it to the context, and score again.[^r2]

For a probabilistic surrogate the established score is the expected drop in
predictive variance over the target locations, computed after the candidate
is appended to the context: "after appending x to the context set C has
been proposed as an acquisition function".[^r3] The work changes which
variance is dropped. A mixture-density output head splits the predictive
variance into two parts. The disagreement between mixture components is
read as epistemic variance, and the spread inside each component as
aleatoric variance; the two sum to the predictive variance of the
mixture.[^r4] The acquisition then ranks sites by the expected reduction in
the epistemic part alone: "The key idea of our approach is to leverage
epistemic uncertainty estimates in ConvCNPs as a guiding criterion for
selecting new sensor locations."[^r5]

The reason given is the definitional one. The predictive uncertainty does
not separate "uncertainty arising from limited knowledge of the underlying
function" from "uncertainty arising from inherent noise in the" function.[^r6]
Only the first is the kind a sensor can buy down. On the Baltic Sea test the
authors observed that the estimated aleatoric term was often much larger
than the epistemic term, and that the total-variance score therefore
"tends to favor regions with high aleatoric uncertainty rather than
ambiguous regions for sensor" placement.[^r7] My inference: a site with
large noise looks informative under total variance, yet a sensor there can
settle only the mean, not the noise, so the score sends sensors where they
cannot reduce error. The paper's own argument supports this reading; it
does not measure it.

The mechanism is one forward pass. The authors chose the mixture head over
ensembles or MC-dropout because "MDNs model the predictive density directly
in a single forward pass."[^r8]

## Relation to information gain

[[expected-information-gain]] is mutual information indexed by a design and
maximised over it. The reducible-uncertainty score is not that quantity: it
is a variance-reduction proxy computed from the surrogate's own predictive
distribution, and the work computes no information quantity. What it shares
with EIG is the shape of the step: a candidate is scored before its label
exists, from the distribution of what the label could do to the model. What
it does not inherit is any guarantee that the ranking follows information.

## Limits

- Placement is not adaptive here. "our sensor placement setting assumes that
  measurements become available only after all sensors are deployed," so the
  score never sees an intermediate label, unlike iterative active
  learning.[^r9]
- One test day, 1 January 2022, with placements evaluated on that same day.
  "This represents a limited evaluation, as ideally, model performance should
  be assessed across multiple test days."[^r10] Sensors were also relocated
  daily, which the authors themselves call impractical.
- Ten sensors, one dataset, one variable (daily sea surface temperature).
  "Preliminary experiments with 10 sensors suggest better model error
  reduction with the new epistemic-driven strategy."[^r11] No significance
  test or spread across seeds for the acquisition is reported beyond three
  random-placement seeds.
- The epistemic estimate itself is unvalidated. The authors list as future
  work "quantitative validation of the epistemic uncertainty estimates" and
  whether "reductions in estimated epistemic uncertainty correlate with actual
  predictive performance."[^r12]
- The K=1 versus K=2 comparison changes the head, not only the uncertainty
  decomposition: the K=2 model adds about 17k parameters. The authors note
  that "the epistemic uncertainty may be underestimated when using a
  mixture"[^r13] and that "components may not fully capture epistemic
  uncertainty in all regions."[^r14]
- The score is computed from the predictive mean, so the quality of each
  acquisition value depends on the prior estimate: "since the expected
  reduction is computed using the predictive mean."[^r15]
- No ensemble or MC-dropout baseline was run; the comparison is against total
  variance only.

## Transfer

| | |
|---|---|
| **Home field** | a surrogate that predicts a field from sparse measurements, where sites are placed before any label is seen (sensor placement with neural processes) |
| **Here** | a question-asker has no fitted surrogate with a mixture head; the analogue would have to supply its own split of uncertainty into reducible and not |
| **What survives** | the rule that a candidate should be ranked by the part of the uncertainty that its answer can plausibly move, not by the total |
| **What does not** | the estimator: the epistemic/aleatoric split here is a property of a parametric output head, and nothing in the work shows that a language-model asker's uncertainty splits the same way |

## Related

- [[uncertainty-decomposition]] — the aleatoric/epistemic split this criterion depends on; the work gives a single-model estimator of that split for a parametric model
- [[expected-information-gain]] — the information-theoretic selection criterion this variance proxy resembles in shape and not in quantity

[^r1]: arxiv-2511-22567 — "can usually not be evaluated during sensor placement, as target labels are not available"
[^r2]: arxiv-2511-22567 — "via a greedy method, iteratively selecting sensor locations to add to S."
[^r3]: arxiv-2511-22567 — "after appending x to the context set C has been proposed as an acquisition function"
[^r4]: arxiv-2511-22567 — "disagreement between the mixture components and aleatoric uncertainty as the spread of each individual component"
[^r5]: arxiv-2511-22567 — "The key idea of our approach is to leverage epistemic uncertainty estimates in ConvCNPs as a guiding criterion for selecting new sensor locations."
[^r6]: arxiv-2511-22567 — "from limited knowledge of the underlying function and uncertainty arising from inherent noise in the"
[^r7]: arxiv-2511-22567 — "tends to favor regions with high aleatoric uncertainty rather than ambiguous regions for sensor"
[^r8]: arxiv-2511-22567 — "model the predictive density directly in a single forward pass"
[^r9]: arxiv-2511-22567 — "our sensor placement setting assumes that measurements become available"
[^r10]: arxiv-2511-22567 — "This represents a limited evaluation, as ideally, model performance should be"
[^r11]: arxiv-2511-22567 — "Preliminary experiments with 10 sensors suggest better model error reduction with the"
[^r12]: arxiv-2511-22567 — "how reductions in estimated epistemic uncertainty correlate with actual predictive performance"
[^r13]: arxiv-2511-22567 — "the epistemic uncertainty may be underestimated when using a mixture"
[^r14]: arxiv-2511-22567 — "components may not fully capture epistemic uncertainty in all regions"
[^r15]: arxiv-2511-22567 — "since the expected reduction is computed using the predictive mean"
