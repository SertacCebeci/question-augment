---
description: "A deviation that survives removing its usual cause, here risk aversion in a risk-neutral newsvendor, points to another source; LLM ordering errors survive that removal."
aliases: ["risk-neutral control", "bias persistence in risk-neutral setting", "persistence under removed cause"]
sources: ["arxiv-2512-12552"]
---
# Bias persistence under cause removal

When a decision deviates from the optimum, the usual textbook explanation for human deviations is a preference: the decision maker is risk averse, or overconfident, or loss averse. A diagnostic follows from that. If the deviation comes from preferences over risk, it "may diminish in risk-neutral contexts"; if it comes from something more basic, it persists.[^e1] The paper applies this in a newsvendor setting where every possible order yields a positive profit, so no risk-averse answer is forced. A bias that stays under that condition has lost its usual explanation and needs another one.

The result is that the ordering deviations survived. The paper says its results "robustly support Hypothesis 2, demonstrating that ordering deviations in risk-neutral" settings persist.[^e2] The three models differed in how, and the paper gives a different source for each:

- LLaMA-8B shows deviations even though profit is guaranteed. The paper calls these "manifestations of computational limits preventing accurate calculation of the optimal" order, and says its evidence is "that biases can exist independent of risk."[^e3][^e4]
- GPT-4 computes the optimum and then moves away from it. The paper says it shows "biases even when correctly calculating the optimal" solution, and that "post-calculation adjustments" follow, which it calls "overthinking."[^e5] Its rationales invoke risk in a setting where there is none, which the paper reads through a semantic-interference mechanism: narrative framing overriding the arithmetic.
- GPT-4o is near the optimum. The paper reports that it "achieves near-perfect normative rationality," with deviations between −0.05% and +0.11%.[^e6]

So the same control separates three things: a computation that fails, a correct computation that is then edited, and no deviation. The mechanism labels come from the rationales the models wrote, read by the authors. The control itself only shows that the deviation is not the risk-preference kind, which is the question it was designed to answer.

The transferable structure is a logic for reading a bias. Removing the cause a theory would name, and watching the deviation, is a test that can fail. The deviation's surviving tells the reader to look for another source. It does not name that source.

For a question or an answer, that matters because the stated reason for an answer can be absent while the answer keeps its shape. A model asked to justify an order in a risk-neutral setting still reaches for risk, and the paper reads that as the framing carrying over. This is the same kind of surface cue that [[option-matching-shortcut]] describes, here an economic frame rather than a list of options (my inference from the two papers' rationales).

## Limits

- The control removes one cause and does not establish that the remaining cause is architectural. The paper's conclusion that the biases "stem from architectural constraints rather than knowledge gaps" is drawn from three models and is not tested by varying architecture.[^e7] The authors themselves present the four mechanisms as "a structured framework" for interpretation.[^e8]
- The lognormal condition is excluded from the risk-neutral analysis "due to nondeterministic outputs."[^e9] The control is therefore tested on two of three demand distributions.
- The source labels for GPT-4 and LLaMA-8B rest on qualitative reading of rationales. A rationale can describe a computation the model did not perform, and the paper does not check that against the arithmetic beyond the sampled answers (my inference).
- Persistence in a risk-neutral setting shows that risk is not the only source. It does not show that humans deviate for the same reason, since the human comparison is a separate benchmark.
- "More sophisticated, more irrational" rests on comparing three models. It is a pattern in this sample, not a law of model scale.

## Related

- [[pull-to-center-ordering-bias]] — the deviation this control is applied to, and the level at which it is measured.
- [[demand-chasing]] — the multi-round companion; its explanation is recency rather than framing, so the control here does not test it.
- [[definition-application-gap]] — a stated rule that does not govern the answer; the risk-neutral control and that gap both ask whether the stated reason is the operative one.
- [[option-matching-shortcut]] — another case where a surface cue shapes reasoning, there the option list rather than the economic frame.

[^e1]: arxiv-2512-12552 — "if deviations stem from preferences over risk, they may diminish in risk-neutral contexts"
[^e2]: arxiv-2512-12552 — "demonstrating that ordering deviations in risk-neutral"
[^e3]: arxiv-2512-12552 — "manifestations of computational limits preventing accurate calculation of the optimal"
[^e4]: arxiv-2512-12552 — "LLaMA-8B provides the clearest evidence that biases can exist independent of risk"
[^e5]: arxiv-2512-12552 — "showing biases even when correctly calculating the optimal"
[^e6]: arxiv-2512-12552 — "achieves near-perfect normative rationality"
[^e7]: arxiv-2512-12552 — "we conclude they stem from architectural constraints rather than knowledge gaps"
[^e8]: arxiv-2512-12552 — "we propose four explanatory mechanisms that offer a structured framework"
[^e9]: arxiv-2512-12552 — "Lognormal data was excluded due to nondeterministic outputs"
