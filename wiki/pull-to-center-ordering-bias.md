---
description: "In the newsvendor problem, orders fall short when margins are high and overshoot when they are low, pulled toward mean demand; three LLMs replicate this and exceed human levels."
aliases: ["Too Low/Too High effect", "pull-to-center effect", "newsvendor ordering bias", "mean-anchoring in ordering"]
sources: ["arxiv-2512-12552"]
---
# Pull-to-center ordering bias

In a newsvendor problem a decision maker orders stock before demand is known, and each unit left unsold or unmet costs money. The bias is a systematic departure from the optimal order in one direction: the order is pulled toward the middle of the demand range. The paper calls it the "Too Low/Too High" effect, "where decision makers tend to underorder in high-margin scenarios and overorder in low-margin scenarios."[^c1] The optimum is not a fixed number. It "varies significantly with the demand distribution," from 225 in the uniform high-margin case down to 165 for the lognormal.[^c2] The optimal order is a quantile of demand set by the margin (my inference from the standard newsvendor form). The bias is that the answer tracks the mean demand instead of the margin.

The paper reads its trajectories as showing that "mean-anchoring is a primary cognitive mechanism, as the models are persistently drawn to the center of the demand range."[^c3] That is the paper's reading of a plot in which the ordering paths cluster around the mean demand of 150. It is a description of where the orders go, and the word "primary" is the authors' own.

On the uniform and normal distributions, all three models (GPT-4, GPT-4o and LLaMA-8B) reproduced the pattern. They "exhibited significant underordering in high-margin scenarios" and overordering in low-margin ones, with mean deviations of −56.29 for the uniform case and +45.36 for the normal.[^c4] The paper's claim of amplification rests on one comparison: in the low-margin uniform condition, GPT-4's overordering "deviation (+100.25) exceeded the human benchmark (+59.06) by 70%."[^c5] The authors suggest the excess may come from training on human text, which "may reinforce and intensify heuristic tendencies."[^c6]

To quantify insufficient adjustment the paper defines a mean adjustment score. Its values are "often far from the optimal value of 1," and in low-margin scenarios they are negative, meaning the models moved away from the optimum.[^c7] The bias is therefore not only a shortfall of adjustment; in some conditions it grows.

The direction of the bias depends on the demand shape. Under the lognormal distribution the high-margin underordering disappears: the models "did not uniformly underorder in the high-margin scenarios," and GPT-4 and GPT-4o slightly overordered there.[^c8] The paper concludes that the direction and magnitude of the bias "are modulated by the skewness and properties of the demand distribution" rather than fixed.

The bias also survived the most direct remedy the paper tried. Its abstract reports that "these biases persist even when optimal formulas are provided," and from this it concludes they "stem from architectural constraints rather than knowledge gaps."[^c9] The next step, what that conclusion does and does not show, is in [[bias-persistence-under-cause-removal]] and [[definition-application-gap]].

For asking and answering, the transferable point is narrow. A quantity asked under asymmetric costs can be answered from a central reference even when the costs point the other way. That is my inference from the pattern, not a claim the paper makes about questions.

## Limits

- The direction is not universal. The lognormal case breaks the high-margin rule, so "too low when margins are high" holds only for the uniform and normal demands tested.[^c8]
- Three models, each run at temperature 1.0,[^c10] with ten independent repetitions per condition.[^c11] The human benchmark is the data of Schweitzer and Cachon (2000), experiment 1, not a new human sample.[^c12] The "70%" amplification is one cell of the design.
- "Mean-anchoring" as the cause is read from trajectories and rationales. The reading is plausible, and the paper does not report an experiment that moves the anchor and watches the orders follow (my inference from the sections read).
- The claim that training data drives the excess is a suggestion. The paper does not test it.
- The architectural conclusion comes from comparing three models of different sizes and vintages. Architecture was not varied, so "architectural" names the explanation the authors prefer, not a measured one.

## Related

- [[demand-chasing]] — the multi-round companion in the same experiments: the same models react to the latest demand realization rather than to the mean.
- [[bias-persistence-under-cause-removal]] — the risk-neutral control the paper applies to this bias, and what it does and does not separate.
- [[definition-application-gap]] — the same split: a formula supplied in the prompt does not guarantee that the answer follows it.
- [[conflicting-evidence-order-effect]] — another order sensitivity. The paper finds a presentation-order effect here too: which margin scenario comes first shifts the later orders.[^c13]
- [[diagnostic-anchoring-in-agentic-llms]] — anchoring in an LLM decision task of another kind, diagnosis rather than quantity.

[^c1]: arxiv-2512-12552 — "where decision makers tend to underorder in high-margin scenarios and overorder in low-margin scenarios"
[^c2]: arxiv-2512-12552 — "which itself varies significantly with the demand distribution"
[^c3]: arxiv-2512-12552 — "evidence that mean-anchoring is a primary cognitive mechanism, as the models are persistently drawn"
[^c4]: arxiv-2512-12552 — "They exhibited significant underordering in high-margin"
[^c5]: arxiv-2512-12552 — "deviation (+100.25) exceeded the human"
[^c6]: arxiv-2512-12552 — "suggesting that training on human-generated text may reinforce and"
[^c7]: arxiv-2512-12552 — "The scores, often far from the optimal value of 1"
[^c8]: arxiv-2512-12552 — "they did not uniformly underorder in the high-margin scenarios"
[^c9]: arxiv-2512-12552 — "Because these biases persist even when optimal formulas are provided,"
[^c10]: arxiv-2512-12552 — "set the temperature parameter to 1.0 for all models"
[^c11]: arxiv-2512-12552 — "Each experimental condition was conducted over 10 independent repetitions"
[^c12]: arxiv-2512-12552 — "Data source: Schweitzer and Cachon (2000), experiment 1."
[^c13]: arxiv-2512-12552 — "show the same basic pattern of presentation-order effect"
