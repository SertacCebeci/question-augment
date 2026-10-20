---
description: "Judges sharing a residual beyond the common factor bias an anchored estimate: a residual shared uniformly is credited as quality, and one shared by model family can be blocked out."
aliases: ["shared judge residual", "common-mode error", "correlated judge residuals", "panel-wide judge bias"]
sources: ["doi-10-48550-arxiv-2609-08826"]
---
# Common-mode judge error

Two judges can agree for two reasons: both track the quality being judged, or both carry an error they share. The second part is the common mode. In a single-common-factor model the shared error is one latent factor c, and the judges' own residuals are assumed to be uncorrelated: "all shared judge variation is carried by the single common-mode factor c."[^c1] The paper names this residual assumption separately because it is "the empirically fragile part." LLM judges built on a shared base model, prompt template, or preference-tuning lineage "plausibly share residual correlation beyond c."[^c2]

The mechanism is what happens when that assumption fails. A residual shared by every judge at the same strength (a homogeneous residual) is not a difference between judges. It adds a common variance term to the judges' covariance, and the closed form reads that term as part of quality or of the common mode. The paper's Proposition 1 gives the clean case: "A second common factor loading uniformly across judges and anchors is observationally equivalent to inflating" the quality variance, and it leaves the contamination correlation unbiased. Only asymmetric loading biases the estimate. The other side of the same fact is that a shared bias of the symmetric shape "would be silently credited as quality."[^c3]

For a homogeneous judge residual the direction of the bias depends on the anchors. With at least one clean anchor "the effect is pure attenuation": the estimated contamination shrinks toward zero, so a contaminated anchor is reported as nearly clean. With both anchors contaminated, the paper finds attenuation in a moderate regime and inflation near the identification boundary, so the sign is configuration-dependent.[^c4] The panel-wide case is the hard one. The test designed for this (a judge-covariance dispersion test) is blind to a uniform residual, and a second test, over-identification across anchors, has little power at realistic sizes: "0.6 is 0.06 at N =500 (its own false-positive rate), 0.16 at N =2000" for a residual of strength 0.6.[^c5]

The paper's partial remedy uses judge metadata. If judges are grouped by model family, cross-family covariances carry no family-level residual: "cross-family judge covariances equal σt2 +σc2 exactly (the residual cancels)." So the closed form can be computed from cross-family pairs only, and the gap between within-family and cross-family covariance estimates the family residual's variance. In the paper's simulation the naive estimate drifts toward "clean" as the family residual grows, while the family-blocked estimate stays near the truth.[^c6]

## Limits

- The remedy covers only family-level residuals, and only when the panel spans at least two families with one family holding two or more judges. The paper's own words: "the panel-wide case remains open."[^c7]
- A panel-wide cause, such as one shared prompt template that every judge sees, "no within-panel statistic can separate from the common mode."[^c8] Within the panel the shared bias looks like quality, and the paper advises that single-family panels should treat a small estimate "as unverified, not as clearance."
- The power figures come from simulation at fixed residual strength and sample size; they are a profile of the test, not a measurement on any real panel.
- My inference: the family-blocked fix assumes the family is the unit of shared lineage. A shared bias that crosses families (a common preference-tuning recipe, for example) is not separated by it. The paper does not test this.

## Related

- [[anchor-contamination]] — the anchor-side half of the same shared variation: the reference set may carry the common mode too, and the closed form is the one tool that uses both sides.
- [[effective-independent-votes]] — measures the same judge co-variation as an intraclass correlation and reads it as a shared prior; this note says what the decomposition does with that co-variation.
- [[pessimistic-min-judge-aggregation]] — a min over judges relies on partly independent blind spots; a shared residual of the kind described here is what breaks that reliance (my inference).
- [[llm-judge-biases]] — position and verbosity biases are per-judge effects; the shared residual is the case where many judges carry the same bias, which per-judge correction does not remove.

[^c1]: doi-10-48550-arxiv-2609-08826 — "all shared judge variation is carried by the single common-mode factor c."
[^c2]: doi-10-48550-arxiv-2609-08826 — "plausibly share residual correlation beyond c"
[^c3]: doi-10-48550-arxiv-2609-08826 — "A genuinely shared bias of exactly this symmetric shape would be silently credited as quality"
[^c4]: doi-10-48550-arxiv-2609-08826 — "with at least one clean anchor the effect is pure attenuation"
[^c5]: doi-10-48550-arxiv-2609-08826 — "0.6 is 0.06 at N =500 (its own false-positive rate), 0.16 at N =2000"
[^c6]: doi-10-48550-arxiv-2609-08826 — "cross-family judge covariances equal σt2 +σc2 exactly (the residual cancels)"
[^c7]: doi-10-48550-arxiv-2609-08826 — "the panel-wide case remains open."
[^c8]: doi-10-48550-arxiv-2609-08826 — "which no within-panel statistic can separate from the common mode"
