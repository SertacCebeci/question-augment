---
description: "In judge banks, higher accuracy tends to come with more correlated errors: frontier judges from different providers share mistakes, so accuracy alone does not buy independent evidence."
aliases: ["accuracy-dependence coupling", "capability-correlated judge errors", "frontier judges share errors"]
sources: ["doi-10-48550-arxiv-2609-22512", "doi-10-48550-arxiv-2609-33221"]
---
# Accuracy and error correlation in judge banks

The intuition that a more accurate judge adds more to a panel assumes that its mistakes are its own. The measurements in this work run the other way for the banks tested: the more accurate judges also made more correlated errors. "We show that higher judge accuracy does not guarantee more independent errors."[^c1] "Higher accuracy comes with stronger error correlation."[^c2]

The numbers are on identical RewardBench calibration pairs. A three-judge bank of GPT, Claude and Grok models reached mean per-judge accuracy 0.92, mean pairwise error correlation 0.56 (95% interval 0.42 to 0.68), and an effective ensemble size of 1.41 judges. The five open-weight pairwise judges reached accuracy 0.66 with correlation 0.20 and effective size 2.77. A three-judge Gemini bank sat between them, at accuracy 0.87 and correlation 0.42.[^c3]

The sharing does not stop at provider lines. "Errors are shared across providers."[^c4] Frontier judges from different providers had mean pairwise error correlation 0.42 on RewardBench, close to the 0.40 among the Gemini judges. A pair of one frontier judge and one open-weight pairwise judge had 0.07. So the frontier group is correlated internally, and the cross-tier pairs are nearly independent. That asymmetry is what makes mixing tiers useful: "Mixing capability tiers adds independent evidence."[^c5] Adding the five open-weight pairwise judges to the six frontier judges raised the effective size of the mixed bank from 1.88 to 3.83 on RewardBench.[^c6]

The mechanism is not identified. The work tests one candidate, preference optimization: a controlled comparison "does not support preference optimization alone as the explanation for" the stronger dependence. Switching six judges to GRPO training moved the mean correlation by only −0.021.[^c7] For the frontier pattern the paper offers a suggestion, not a cause: "stronger shared errors among similarly capable frontier judges, but the experiment does not identify" the reason.[^c8] (My reading: the observation is that a judge's skill and its error set can rise together, so skill is no guarantee of a separate error set.)

## Limits

- The frontier result rests on three judges per bank, one benchmark pair set of 400 and one of 300. The interval on the frontier correlation is wide, and the bank size is small.[^c9]
- The pattern is not uniform across datasets. On PKU-SafeRLHF the Gemini bank's correlation (0.32) is close to the open-weight pairwise judges' (0.29), so the high-accuracy-high-correlation pattern is clearest on RewardBench.[^c10]
- The measured correlation is not the whole account. Two bank structures with the same average can fail in different shapes, so the level of correlation does not say which judges share the mistake.[^c11]
- The experiment does not say the high-accuracy correlation is inevitable. The banks are the models the authors could evaluate; the introduction names shared pretraining data and post-training as candidate sources, and those sources are not isolated here.[^c12]

## Related

- [[shared-error-pattern]] — the level of correlation is not the whole account; which judges err together, and on which items, changes what a consensus rule should do.
- [[effective-independent-votes]] — the effective-size arithmetic behind the bank-level numbers above.
- [[cross-provider-judge-ensemble]] — a two-provider judge ensemble; the cross-provider result here says errors from different providers can still correlate, so that ensemble's independence is a question its own measurements would have to answer.
- [[common-mode-judge-error]] — the shared-residual account of why a panel's judges agree beyond their common quality.
- dependence-penalized-reward-boosting — a training-time remedy aimed at the same dependence: reward models penalized for kernel dependence on their margins, so a boosted aggregator has complementary errors to correct.[^c13]

[^c1]: doi-10-48550-arxiv-2609-22512 — "We show that higher judge accuracy does not guarantee more independent errors."
[^c2]: doi-10-48550-arxiv-2609-22512 — "Higher accuracy comes with stronger error correlation."
[^c3]: doi-10-48550-arxiv-2609-22512
[^c4]: doi-10-48550-arxiv-2609-22512 — "Errors are shared across providers."
[^c5]: doi-10-48550-arxiv-2609-22512 — "Mixing capability tiers adds independent evidence."
[^c6]: doi-10-48550-arxiv-2609-22512
[^c7]: doi-10-48550-arxiv-2609-22512 — "does not support preference optimization alone as the explanation for"
[^c8]: doi-10-48550-arxiv-2609-22512 — "stronger shared errors among similarly capable frontier judges, but the experiment does not identify"
[^c9]: doi-10-48550-arxiv-2609-22512
[^c10]: doi-10-48550-arxiv-2609-22512
[^c11]: doi-10-48550-arxiv-2609-22512 — "Thus, the pattern of shared errors matters, not only their overall correlation."
[^c12]: doi-10-48550-arxiv-2609-22512
[^c13]: doi-10-48550-arxiv-2609-33221 — "redundancy among reward models is often nonlinear"
