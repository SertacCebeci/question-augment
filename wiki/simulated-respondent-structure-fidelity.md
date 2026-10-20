---
description: "An LLM-simulated sample can reproduce a human scale's factor structure while missing its score distributions and variances, so structure and spread can come apart."
aliases: ["group-level structure fidelity", "factor structure of simulated samples", "structure-level validity of synthetic respondents"]
sources: ["arxiv-2512-02910"]
---
# Simulated-respondent structure fidelity

A factor structure is the pattern of which items move together, summarised by loadings from a factor model. The question here is whether a simulated sample carries that pattern from a human sample, and whether the same sample carries the rest of the human data with it. Cipriani and colleagues separate the two by testing both on the same simulated datasets.

The simulator was GPT-4o-mini. "The simulated data were generated using GPT4o-mini"[^c1] and "Each prompt was sent as a separate, independent API request"[^c2], so each simulated respondent is one request with no shared history. Each request asked the model to impersonate a UK respondent of a given age, sex and ethnicity and to answer a whole scale at once, returning "Give the answers as a single string of comma separated values."[^c12]

On the structure, the result is positive. "Except for Study 1, all simulated datasets successfully replicated the factor structure"[^c3] of their scale. Studies 1 and 2 fitted a confirmatory model to an existing scale. In Studies 3 and 4 the authors "developed entirely new scales"[^c4] by factor analysis on simulated data and then tested the structure on newly collected human samples.

On the rest of the data, the result is negative. The same paper reports that "While CFA yields reliably positive results, simulated samples fail to replicate" the pairwise correlations, the distributions and the variances of the real samples.[^c5] Its summary is "their score distributions differ significantly across all measured dimensions."[^c6] The authors conclude that group-level structures are good enough for early piloting but that "However, individual-level simulated data are not suitable for this purpose."[^c7]

The mechanism is not established. My inference, from which tests passed and which failed, is that a factor model reads the covariance pattern among items and not their levels or spread. A simulator can therefore reproduce co-movement among items while sitting at different means and with a narrower spread. The paper does not test this; it is the reading the two results suggest.

Two parts of the evidence are weaker than they look. The correlation test (H3) could not be run as a paired comparison: "obtain precise couples of real and simulated data for all studies except Study 2"[^c8] was not possible, so the correlation failure is not a clean measure of simulator error. The contrast that carries the claim is therefore structure against marginal distributions and variances, not structure against correlations.

The authors offer three untested reasons why Study 1 differs. The first is the rotation: "structure of this scale was determined using a different rotation (minres) than other scales."[^c9] The second is the response format: "uses a 5-point Likert scale for responses, while others use a 6-point"[^c10] scale. The third is the topic, since climate perception "is a politically contextualised topic"[^c11] and so may be over-represented in the training data. None of the three was varied in the study.

Batching may also matter. All items were sent in one completion, which is a known source of inflated cross-item correlation in synthetic data (see [[shared-completion-batching-distortion]]). If that holds here, the structure may replicate more readily than the human data would allow. That is my inference; the paper does not test it.

## Limits

- Only Likert-type scales were tested. "we only tested Likert-type scales"[^c13] and only survey data; behavioural measures were not examined.
- One population: "This limits the generalizability of our results for other languages and other sociocultural contexts."[^c14]
- One model: "For this research we only used a specific ChatGPT model."[^c15]
- Short scales: "the tested scales possess a relatively small number of items."[^c16] The largest had 30 draft items.
- The structure test rests on fit indices with cut-offs from Hu and Bentler (1999). The paper reports them, and this note does not re-derive them.
- Whether structure replication survives a change of prompt, temperature or model is untested.

## Related

- [[simulated-respondent-composite-fidelity]] — item-level agreement that fails at the level of a weighted total; a second place where a check on parts does not carry to the scale
- [[simulated-respondent-variance-deficit]] — the spread side of the same gap, measured in a different study
- [[measurement-invariance-ladder]] — the next test once a structure is found: whether the same instrument means the same thing across the simulated and human groups
- [[shared-completion-batching-distortion]] — batched generation can inflate cross-item correlation, a candidate reason structure replicates too easily (my inference)
- [[response-free-semantic-scale-reduction]] — factor-like item groups can be recovered from item wording alone, with no respondents at all

[^c1]: arxiv-2512-02910 — "The simulated data were generated using GPT4o-mini"
[^c2]: arxiv-2512-02910 — "Each prompt was sent as a separate, independent API request"
[^c3]: arxiv-2512-02910 — "Except for Study 1, all simulated datasets successfully replicated the factor structure"
[^c4]: arxiv-2512-02910 — "we developed entirely new scales"
[^c5]: arxiv-2512-02910 — "While CFA yields reliably positive results, simulated samples fail to replicate"
[^c6]: arxiv-2512-02910 — "their score distributions differ significantly across all measured dimensions"
[^c7]: arxiv-2512-02910 — "However, individual-level simulated data are not suitable for this purpose"
[^c8]: arxiv-2512-02910 — "obtain precise couples of real and simulated data for all studies except Study 2"
[^c9]: arxiv-2512-02910 — "structure of this scale was determined using a different rotation (minres) than other scales"
[^c10]: arxiv-2512-02910 — "uses a 5-point Likert scale for responses, while others use a 6-point"
[^c11]: arxiv-2512-02910 — "is a politically contextualised topic"
[^c12]: arxiv-2512-02910 — "Give the answers as a single string of comma separated values"
[^c13]: arxiv-2512-02910 — "we only tested Likert-type scales"
[^c14]: arxiv-2512-02910 — "This limits the generalizability of our results for other languages and other sociocultural contexts"
[^c15]: arxiv-2512-02910 — "For this research we only used a specific ChatGPT model"
[^c16]: arxiv-2512-02910 — "the tested scales possess a relatively small number of items"
