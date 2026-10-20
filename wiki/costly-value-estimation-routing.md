---
description: "Routing needs each specialist's expected return, but precise estimates are costly; pricing each refinement against its value, as Pandora's Box does, queries the expensive estimator far less."
aliases: ["routing with costly value estimation", "Pandora's Router", "Pandora's Bidder", "cost of value estimation in routing"]
sources: ["doi-10-48550-arxiv-2608-20316"]
---
# Costly value estimation in routing

A heterogeneous AI system, built from several models, architectures, harnesses or inference-time settings, can improve quality and cost by sending each query to the specialist that answers it best at the lowest price.[^r1] Routing requires an estimate of each specialist's expected return on the input, and that estimate has a price. "Cheap estimators (e.g., embedding-based predictors) are fast but noisy", while accurate ones, such as fine-tuned models given retrieval results or partial reasoning traces, are expensive.[^r2]

The mechanism is a two-tier estimate. The router always holds a cheap estimate $f_m(x)$ for each specialist and may pay $c_m$ to open a costlier, more accurate estimate $g_m(x)$. Treating each specialist as a box in [[pandora-box-reservation-price]] turns the choice into a search: compute reservation prices from the cheap estimates, "inspect specialists ... in reservation-price order, stopping when no remaining query is worth its cost", then choose the specialist with the largest observed estimate.[^r3] The search is the centralized policy, which the paper calls Pandora's Router. Under a Gaussian model of how the cheap estimates predict the costly one, "the reservation prices and the associated value-of-information expressions have closed forms", so the decision to refine an estimate is computed rather than tuned.[^r4]

The measured claim is from the abstract: across three domains (a multi-LLM benchmark, retrieval-augmented factoid QA, and inference-time reasoning on mathematics), the router "matches the routing quality of exhaustive estimation, while querying the expensive estimator far less often".[^r5][^r6]

The decentralized version, Pandora's Bidder, moves the decision to the specialists. Each one "faces a posted price", the current best competing offer, and "must decide whether to invest in a more accurate self-assessment before claiming the query".[^r7] The motive is that the specialist often knows more about its own value than the router does: a retrieval-augmented specialist "has access to its own corpus, and can measure how relevant it is to the query".[^r8] The abstract reports that value-of-information reasoning "improves allocative efficiency when competing estimates are accurate", but when competing estimates are noisy, "it can increase the strategic specialist" utility at the expense of others.[^r9][^r10]

What survives the move from a router to a bidder is the pricing: an estimate is worth buying only when its expected effect on the decision exceeds what it costs, and the cost is a term in that comparison, not an afterthought.

## Limits

- The cost ratios are design choices. In the mathematics domain, the authors set the price of the large model "so that it is beneficial to route to Gemini only when confident" that it can answer correctly.[^r11] The cost-accuracy tradeoff is, in their words, "rather than an objectively-measurable property of the domain or method".[^r12] Other prices would move the result.
- The Gaussian signal model is an approximation, as in [[pandora-box-reservation-price]]. Where specialists' values are correlated, the paper "propose[s] a heuristic approximation" that recomputes prices after each inspection, with no optimality claim.[^r13]
- The learned costly estimator is "a learned plug-in approximation to this posterior decision value", not the realized reward.[^r14] The router optimizes a proxy, and the proxy's error is not separated out in the text read here.
- The costly estimator was built by the authors: "by fine-tuning a small language model encoder to predict the reward" from a domain-specific context.[^r15] Whether a deployed router could obtain such estimates at the stated cost is not tested.
- The decentralized result is mixed by the abstract's own account. Under noisy competing estimates, reasoning about information can benefit the strategic specialist at others' expense, so no efficiency claim holds in general.
- This pass read the abstract and the method through the setup of the experiments, not the result tables. The "far less often" claim is reported from the abstract and has not been checked against figures here.

## Related

- [[pandora-box-reservation-price]] — the search rule the router applies to the costly estimates.
- [[value-of-information]] — the refine-or-not decision is a net value-minus-cost rule, here applied to estimators rather than to questions.
- [[voi-per-cost-modality-selection]] — also picks the next action by expected gain per cost, but over action modalities rather than the precision of a specialist's estimate.
- [[model-orchestration]] — routes between models by hand; this note is the automated, estimate-cost side of the same routing question.
- [[routing-ceiling]] — a headroom bound on what per-query routing can gain at all. (This note's reading: where that bound is near zero, refining the estimates has little to buy.)

[^r1]: doi-10-48550-arxiv-2608-20316 — "by routing queries to the specialist who can answer most"
[^r2]: doi-10-48550-arxiv-2608-20316 — "Cheap estimators (e.g., embedding-based predictors) are fast but noisy"
[^r3]: doi-10-48550-arxiv-2608-20316 — "in reservation-price order, stopping when no remaining"
[^r4]: doi-10-48550-arxiv-2608-20316 — "value-of-information expressions have closed forms"
[^r5]: doi-10-48550-arxiv-2608-20316 — "matches the routing quality of exhaustive estimation, while"
[^r6]: doi-10-48550-arxiv-2608-20316 — "querying the expensive estimator far less often"
[^r7]: doi-10-48550-arxiv-2608-20316 — "must decide whether to invest in a more accurate self-assessment before claiming the query"
[^r8]: doi-10-48550-arxiv-2608-20316 — "has access to its own corpus, and can measure how relevant it is to the query"
[^r9]: doi-10-48550-arxiv-2608-20316 — "reasoning improves allocative efficiency when competing estimates are accurate"
[^r10]: doi-10-48550-arxiv-2608-20316 — "it can increase the strategic specialist"
[^r11]: doi-10-48550-arxiv-2608-20316 — "This high cost is chosen so that it is beneficial to route to Gemini only when confident"
[^r12]: doi-10-48550-arxiv-2608-20316 — "rather than an objectively-measurable property of the domain or method"
[^r13]: doi-10-48550-arxiv-2608-20316 — "we propose a heuristic approximation"
[^r14]: doi-10-48550-arxiv-2608-20316 — "a learned plug-in approximation to this posterior decision value"
[^r15]: doi-10-48550-arxiv-2608-20316 — "by fine-tuning a small language model encoder to predict the reward"
