---
description: "An estimand is the precise quantity an analysis sets out to estimate, fixed before the data are consulted; its population, contrast and follow-up decide what the same records can answer."
aliases: ["causal estimand", "target estimand", "target quantity of inference"]
sources: ["arxiv-2511-19735"]
---
# Estimand

An estimand is the quantity an analysis is built to estimate, written down in full before any data are analysed. The statistical roadmap for combining randomized trials, real-world data and AI/ML puts it first. Its starting point is the question, not the source or the method: the decision problem and causal estimand come before the data are touched, because the question is "but the question to be answered".[^e1]

Specifying the estimand means naming a fixed set of parts: the target population, the treatment strategies, the endpoint, how intercurrent events are handled, the follow-up horizon, and the causal contrast of interest.[^e2] The paper gives the reason. Many downstream problems come from the scientific question not being kept apart from what the data happen to support: "downstream problems arise when the scientific question is not clearly distinguished".[^e3]

Once the parts are fixed, each data source gets a role inside the question. In integrative settings the estimand says whether real-world data is used to "broaden the target population, extend follow-up, augment/supplement a control arm", to improve efficiency, or to support post-market surveillance.[^e4] The same records therefore answer different questions depending on what the estimand names.

The mechanism shows in the paper's worked cases. In AI-assisted recruitment, an algorithm selects the participants most likely to benefit, so the enriched group is not the population the question is about. The estimand "must specify the intended target population, not merely the enriched" subpopulation.[^e5] In target trial emulation the observational analysis is framed by a hypothetical protocol: the approach "requires explicit specification of a hypothetical trial" with its eligibility, strategies, follow-up, outcome and contrast.[^e6] The protocol is the question; the observational data are the material that may or may not answer it.

What transfers, in my reading and not the paper's words: a question that names its quantity, population and time frame before evidence is gathered gives the eventual answer something exact to be checked against. The estimand is also where a mismatch between question and data becomes visible. The interpretability note on [[rung-mismatch-in-interpretability-claims]] uses the same word for the target of a probe, which supports reading it as the named quantity a method is aimed at. The causal machinery does not carry over unchanged. Identification under assumptions is specific to causal contrasts, and the paper does not argue it for descriptive or predictive questions.

## Limits

- The paper is a Perspective, and it says so: "Rather than providing a comprehensive review of all recent developments".[^e7] No case in the text measures how often an unwritten estimand led to a wrong conclusion.
- The roadmap is described as operational, "intended to be operational",[^e8] but the text reports no study that tests it; its cases are argued from the framework.[^e9]
- The estimand here is a causal contrast. How the parts map onto non-causal questions is not worked out in this text.
- Writing an estimand does not establish that it is identifiable from the data. That is a separate step (see [[common-support-positivity]]).

## Related

- [[rung-mismatch-in-interpretability-claims]] — the same word for what a probe targets; there the named quantity decides which rung a claim needs
- [[predicted-outcome-substitution]] — a predicted value put in place of an observed outcome shifts the estimand itself
- [[data-fitness-for-purpose]] — once the estimand is fixed, whether a source can address it
- [[common-support-positivity]] — the overlap condition that an estimand can fail
- [[evidentiary-role-of-analysis]] — the closing statement of what the estimated quantity licenses

[^e1]: arxiv-2511-19735 — "but the question to be answered"
[^e2]: arxiv-2511-19735 — "target population, treatment strategies, endpoint, intercurrent event handling"
[^e3]: arxiv-2511-19735 — "downstream problems arise when the scientific question is not clearly distinguished"
[^e4]: arxiv-2511-19735 — "broaden the target population, extend follow-up, augment/supplement a control arm"
[^e5]: arxiv-2511-19735 — "must specify the intended target population, not merely the enriched"
[^e6]: arxiv-2511-19735 — "requires explicit specification of a hypothetical trial"
[^e7]: arxiv-2511-19735 — "Rather than providing a comprehensive review of all recent developments"
[^e8]: arxiv-2511-19735 — "The roadmap is intended to be operational"
[^e9]: arxiv-2511-19735 — "This Perspective is written from that statistical viewpoint."
