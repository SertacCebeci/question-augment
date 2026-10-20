---
description: "In repeated newsvendor rounds, orders chase the latest demand realization rather than the distribution; the three LLMs chase it more strongly, each in its own way."
aliases: ["demand chasing", "overreaction to recent demand", "chasing the latest demand"]
sources: ["arxiv-2512-12552"]
---
# Demand chasing

In a newsvendor task repeated over several rounds, the decision maker sees the demand realized in each round and adjusts the next order. Demand chasing is the tendency to overreact to that latest observation. The behavioral operations literature describes it for humans: decision makers overreact to the latest observed demand rather than weighing long-term distributional properties.[^d1] The paper's version of the test is simple. Each round's forecast error is sorted into magnitude quartiles, "from smallest to largest," and the adjustment is classed as "No Change," "Toward Demand," or "Away from Demand."[^d2] A rational corrector moves toward demand after large errors and leaves small ones alone. Chasing shows up as movement after small errors and as a rising share of "Toward Demand" with error size.

The measured pattern is strong. Under the uniform distribution with the low-margin scenario first, GPT-4o's "Toward Demand" rate rises from 82.5% in the smallest-error quartile to 100.0% in the largest. The paper contrasts this with human participants, "far exceeding human participants, who keep" "No Change" above 60% even with large errors.[^d3][^d4] The LLMs therefore react more to each new realization than the human benchmark does, which is the "amplified" claim of the paper's Hypothesis 4.

The three models differ in how they chase. GPT-4 "shows over-reactivity," correcting strongly for large errors but "overreacting to small ones, particularly in complex distributions."[^d5] GPT-4o is the consistent one: "GPT-4o is consistent, achieving near-perfect" movement toward demand under high error, with moderate and stable adjustment sizes.[^d6] LLaMA-8B is erratic. In some low-margin Q1 settings, "Away from Demand" responses dominate, and the paper says that reacting incorrectly to small, noisy signals "reflects architectural and representational limits."[^d7]

Chasing is not uniform across conditions. The high-margin uniform small-error cell is an exception for GPT-4o, where most adjustments went away from demand (83.3%), and the paper reads that as "that long-term anchoring can override short-term demand signals."[^d8] This is the same anchor that appears in [[pull-to-center-ordering-bias]], pulling the other way when the latest signal is small.

The paper's explanation is an attention account: transformers "prioritize early or recent inputs," so a recent demand signal weighs heavily.[^d9] It is offered as one of four "explanatory mechanisms," and the paper gives it as a framework rather than a tested account of attention.

The transferable structure is that a repeated decision mixes two reference points, the distribution and the latest outcome, and the answerer can weight the second too much. Whether a human-facing question should be asked in a way that separates them is not something this paper tests.

## Limits

- The quartile analysis is descriptive. It counts directions of adjustment; it does not fit a sensitivity coefficient to the error, so "over-reactivity to small errors" is a claim about proportions in four bins.
- The attention explanation was not tested with an attention analysis or an ablation. It is the authors' interpretation, offered among four mechanisms (my inference from the mechanism section).[^d9]
- The human comparison is quoted from earlier studies and from the paper's own table, not from a new human sample.
- One task, the newsvendor, with the same three models and the same demand families as the ordering experiments. Whether chasing appears in other repeated decisions is not tested.
- The results for each model depend on the demand shape and on the margin scenario shown first, so no single "LLM chasing rate" exists to quote.

## Related

- [[pull-to-center-ordering-bias]] — the level bias in the same experiments. The two are separable: one pulls the order toward the mean, the other toward the latest realization.
- [[outcome-feedback]] — the realized demand is the answerer's own outcome feedback; the paper asks whether that feedback is used in proportion to its information.
- [[bias-persistence-under-cause-removal]] — the control that tests whether a bias keeps its source when the textbook cause is removed.

[^d1]: arxiv-2512-12552 — "latest observed demand rather than considering long-term distributional properties"
[^d2]: arxiv-2512-12552 — "from smallest to largest, measuring proportions of"
[^d3]: arxiv-2512-12552 — "Under the uniform distribution (low-margin scenario first)"
[^d4]: arxiv-2512-12552 — "far exceeding human participants, who keep"
[^d5]: arxiv-2512-12552 — "strongly for large errors but overreacting to small ones, particularly in complex distributions"
[^d6]: arxiv-2512-12552 — "GPT-4o is consistent, achieving near-perfect"
[^d7]: arxiv-2512-12552 — "reflects architectural and representational limits"
[^d8]: arxiv-2512-12552 — "that long-term anchoring can override short-term demand signals"
[^d9]: arxiv-2512-12552 — "we propose four explanatory mechanisms that offer a structured framework"
