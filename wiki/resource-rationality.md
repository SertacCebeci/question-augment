---
description: "Resource rationality: choose a procedure by expected gain minus computation cost. An LLM study finds strategy shifts with task size and no cost reward; cost is never measured."
aliases: ["resource-rational analysis", "resource-rationality"]
sources: ["doi-10-48550-arxiv-2602-10329", "doi-10-7554-elife-81256"]
---
# Resource rationality

Resource rationality is the claim that a reasoner should pick its procedure by weighing what the procedure gains against what it costs to run. Lieder and Griffiths, as the LLM study reads them, "formalized reasoning as an optimization problem under cognitive constraints", in which agents "seek to maximize the difference between expected utility and the cost of computation".[^r1] Callaway et al. extend this to metacognitive control, where agents "flexibly adapt between strategies based on their relative reward and processing cost".[^r2] It is the formal successor of the satisficing picture in [[bounded-rationality]]: that note gives a threshold to stop at, while this one states the trade-off as an explicit objective.

The mechanism, as the paper frames it: a procedure that keeps more hypotheses in working memory pays a cost that grows with the hypothesis space, while a procedure that tests one hypothesis at a time pays less but may need more observations. Switching is worthwhile when the expected gain from pruning outweighs the cost of maintaining the pruned space. The paper's wording is that "the optimal choice shifts back to permutation" when the gain from pruning is smaller than the cost of elimination.[^r3] The concrete case is [[permutation-elimination-strategy-switch]].

The paper asks whether this kind of adaptation can arise in language models at all. Its abstract puts the open question as whether resource-rationality "can emerge from such scaling without explicit reward related to computational costs".[^r4] Its answer, on a causal-attribution task, is that both instruction-tuned and reasoning models change strategy with task size, and "this adaptation emerges without any explicit training objective that penalizes or rewards computational cost".[^r5] The mechanism it names is inference-time scaling ([[test-time-scaling]]): the reasoning tokens are where the strategy shows.

The authors also widen the notion from prescription to description. Resource rationality "may also serve as a descriptive lens for understanding how complex systems tend to behave when operating under finite capacity".[^r6]

## Limits

- The cost term is never measured. Cost enters only as an interpretation of the fitted landscape. What the data show is that strategy choice is consistent with a cost-utility boundary; it does not show that the chosen strategies maximize utility minus cost. Reading the fit as optimality is my inference, not the paper's claim.
- The human analogy is marked tentative by the authors: "we emphasize that this analogy remains tentative".[^r7] They also offer a competing account: "reasoning length reflects limitations in attention-based state maintenance rather than deliberate resource allocation".[^r8] The same behavior fits both readings.
- Effort is proxied by character count of the reasoning trace plus output, which is not compute or time. The authors present it as "a behavioral analog for human response time", "offering a predictive benchmark for future human study",[^r9][^r10] which is a proposal for a later study, not a validated one.
- One synthetic task, one family of Boolean rules, four models. Nothing here tests resource-rational adaptation on natural reasoning tasks.
- Simon's open problem carries over: resource rationality needs a cost measure before "good enough" becomes a rule. Without one, the framing names the trade-off and does not set the threshold.

## Related

- [[bounded-rationality]] — the older satisficing root; resource rationality states the trade-off as utility minus computation cost.
- [[permutation-elimination-strategy-switch]] — the measured strategy switch that this framing is applied to.
- [[test-time-scaling]] — the inference-time mechanism in which the reasoning-model behaviour is visible.
- [[forgetting-factor-beta-bernoulli]] — a case where the cost is a parameter: a precision cost with a weight fitted to each subject's predictions, so the cost is estimated from behaviour rather than only read into the fit.[^r11]

[^r1]: doi-10-48550-arxiv-2602-10329 — "formalized reasoning as an optimization problem under cognitive constraints"
[^r2]: doi-10-48550-arxiv-2602-10329 — "flexibly adapt between strategies based on their relative reward and processing cost"
[^r3]: doi-10-48550-arxiv-2602-10329 — "the optimal choice shifts back to permutation"
[^r4]: doi-10-48550-arxiv-2602-10329 — "without explicit reward related to computational costs"
[^r5]: doi-10-48550-arxiv-2602-10329 — "this adaptation emerges without any explicit training objective that penalizes or rewards computational cost"
[^r6]: doi-10-48550-arxiv-2602-10329 — "a descriptive lens for understanding how complex systems tend to behave"
[^r7]: doi-10-48550-arxiv-2602-10329 — "we emphasize that this analogy remains tentative"
[^r8]: doi-10-48550-arxiv-2602-10329 — "reasoning length reflects limitations in attention-based state maintenance rather than deliberate resource allocation"
[^r9]: doi-10-48550-arxiv-2602-10329 — "This result potentially serves as a behavioral analog for human response time"
[^r10]: doi-10-48550-arxiv-2602-10329 — "offering a predictive benchmark for future human study"
[^r11]: doi-10-7554-elife-81256 — "of each subject, by maximizing their likelihoods"
