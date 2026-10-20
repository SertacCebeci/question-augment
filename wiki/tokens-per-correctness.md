---
description: "Tokens Per Correctness divides total weighted compute (generated, input, search-call cost) by the count of correct answers-or-abstentions, so search that adds cost without correctness raises it."
aliases: ["TPC", "cost per correct response"]
sources: ["arxiv-2601-05503", "doi-10-48550-arxiv-2607-13920"]
---
# Tokens Per Correctness

Tokens Per Correctness (TPC) is the expected compute cost per correct response, lower being better: total cost over a dataset divided by the number of correct responses.[^c1] Cost for a query is generated tokens plus a weighted count of input tokens (prompt and all retrieved context) plus a weighted count of search calls. The paper fixes the input weight at 0.25 and the per-search cost at 500 tokens-equivalent, from typical production LLM and search-API pricing, so systems are comparable.[^c2]

A response counts as correct if the model answers an answerable query correctly or abstains on an unanswerable one. This makes the denominator sensitive to both accuracy and abstention; a system that searches more but abstains less can see TPC rise even when answer accuracy is flat. If nothing is correct, TPC is defined as infinity.[^c3]

The abstention rule bites hardest where every question stays answerable and only the evidence degrades. DeepStress runs search agents that way: when document quality falls, a withheld answer on an answerable question is not correct, so its cost is paid without adding to the count of correct answers. Average TPC rises from 18.1k at full document quality to 75.7k at 0% quality, "because it normalizes cost only by correct answers."[^c6] Its cost-normalised companion CoPRAS divides the same cost by a reliability-aware sum that credits withholding under unreliable evidence (see [[reliability-discounted-abstention-credit]]), so it rises less, from 18.1k to 36.8k.[^c7] The ranking changes with it: at 0% quality "AutoRefine has the best TPC due to its very low cost", while the best CoPRAS values went to systems "combining low cost with high RAS."[^c8][^c9]

## Why it is useful

Over-searching is hard to spot instance by instance, since a model may be right for the wrong reason or flip between states as retrieval adds noise. The paper therefore studies aggregate correctness against cost: when marginal correctness stops improving while cost accumulates, TPC rises.[^c4] In the o4-mini reasoning-effort runs, TPC went 517.1, 1002.7, 1492.2 for low, medium, high effort while overall accuracy stayed near 60%.[^c5]

## Limits

The coefficients are one pricing snapshot; the ranking of systems could change with other weights (the paper compares against other metrics in an appendix not read here). It is defined for search tools; extension to other tools is asserted, not tested. It collapses answering and abstaining into one correctness bit, hiding the trade-off between them, which is why the paper also reports both accuracies.

## Related

- [[search-induced-abstention-degradation]] — the phenomenon TPC was built to expose
- [[search-decision-boundary-misalignment]] — over-search as wasted cost at the decision threshold
- [[recall-gated-conversion-rate]] — another efficiency-style ratio for retrieval use

[^c1]: arxiv-2601-05503 — "defined as the expected compute cost per correct response (lower is better)"
[^c2]: arxiv-2601-05503 — "We set λ = 0.25 for the input-token cost and µ = 500 for the per-search-call cost"
[^c3]: arxiv-2601-05503 — "we define TPC(D) = +∞."
[^c4]: arxiv-2601-05503 — "When additional search does not improve"
[^c5]: arxiv-2601-05503 — "TPC increases monotonically with reasoning effort."
[^c6]: doi-10-48550-arxiv-2607-13920 — "because it normalizes cost only by correct answers"
[^c7]: doi-10-48550-arxiv-2607-13920 — "CoPRAS also increases, but less severely"
[^c8]: doi-10-48550-arxiv-2607-13920 — "AutoRefine has the best TPC due to its very low cost"
[^c9]: doi-10-48550-arxiv-2607-13920 — "combining low cost with high RAS"
