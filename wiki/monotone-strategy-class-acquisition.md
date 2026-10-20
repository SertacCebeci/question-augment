---
description: "Learners are sorted by the response strategy their choices reveal; a monotone transition chain over four strategy classes models acquisition as a one-way climb to the successful class."
aliases: ["strategy class transition model", "strategy-class mixture model"]
sources: ["doi-10-48550-arxiv-2107-06994"]
---
# Monotone strategy-class acquisition

Learning a new puzzle skill can be read off the responses themselves, if each response is coded by the role its digit plays in the puzzle. In the hidden single task every puzzle has one target digit, one distractor, four absent digits and three in-house digits, so a choice falls into one of four categories: target, distractor, absent, or in-house.[^m1] Four strategy classes predict which categories a learner produces. An uninformed guess picks from all nine digits. Avoid-direct-contradictions picks among the digits not already in the house. Prevalent-digits picks between target and distractor with equal probability. The successful class "consistently selects" the target. Ignoring errors, the classes are expected to be correct 11.1%, 16.7%, 50% and 100% of the time.[^m2]

The aggregate of many learners is then fitted as a mixture. A weight is kept for each class at each trial. An emission matrix gives the probability that each class produces each response category. An error matrix lets a class fall back onto weaker classes. A transition matrix X moves weight between classes from trial to trial.[^m3] The key assumption is that the transition probability from a superior class to an inferior one is set to zero, because participants "would use the best strategy available to them and not regress to a worse strategy with a lower expected accuracy."[^m4] The chain is therefore upper-triangular: weight can climb from guessing toward the successful class but cannot fall back. Once the successful class holds weight, the fitted curve gives how fast it takes over the population.

The measured pattern is fast takeover in those who learn. "50% of solvers demonstrating consistently high accuracy starting from the 3rd trial and 90% by the 10th" is the paper's summary.[^m5] Most of the learners who did not reach the criterion instead settled on a class worth 50%, the prevalent-digit class, and kept it through the test phase.[^m6] The long tail matters for the model. About 20 participants first classed as non-solvers became high-accuracy late-solvers, and some of them were at or below 50% during practice, which a one-way chain fitted to the early trials does not describe.[^m7]

What the coding changes for asking and answering is the unit of measurement. A learner at 50% accuracy is not a stable low-skill learner by this account. Its accuracy can be the signature of a class that a later class will replace, or of one that never will. Accuracy averaged over a block hides which of these holds.

## Limits

- Solver status is a threshold, not a measured class. Participants were classed as solvers if a logistic fit to their practice accuracy predicted more than 0.8 on the 25th trial. The authors call this criterion "conservative," since it excluded some participants who later reached high accuracy.[^m8]
- The no-regression assumption is set by the modellers, not tested. The data are aggregate, so the model says nothing about whether an individual's path is monotone.
- The classes are a convenience. The paper admits that "other strategies and heuristics may be possible," and a learner who always picks the numerically larger of two prevalent digits is assigned to the same class as one who guesses between them.[^m9]
- One task, one target cell, one house, 88 of 271 participants recruited on Mechanical Turk. The mixture was fitted to this task's category counts (one, one, four, three); other tasks have other counts, and the emission probabilities would change with them.
- The fit covers acquisition during 25 practice trials. It is silent on what happens after the test phase.

## Related

- strategy-articulation-transfer — the same learners, sorted by whether they can state the strategy they now use
- [[feature-specific-transfer-cost]] — which changes to the puzzle the acquired class survives
- [[zpd-window-mastery-update]] — a simulated learner that gains only from explanations within a difficulty window; a different account of why learning comes in steps

[^m1]: doi-10-48550-arxiv-2107-06994 — "Each puzzle contains one, one, four, and three digits in each category"
[^m2]: doi-10-48550-arxiv-2107-06994 — "the four strategy classes are expected to produce correct responses with probabilities 11.1%,"
[^m3]: doi-10-48550-arxiv-2107-06994 — "we define a response emission matrix R"
[^m4]: doi-10-48550-arxiv-2107-06994 — "would use the best strategy available to them and not regress to a worse strategy with a lower expected accuracy"
[^m5]: doi-10-48550-arxiv-2107-06994 — "The successful strategies were acquired rapidly, with 50% of solvers demonstrating consistently"
[^m6]: doi-10-48550-arxiv-2107-06994 — "most non-solvers appeared to have adopted a strategy they continued to employ throughout the test phase"
[^m7]: doi-10-48550-arxiv-2107-06994 — "the distribution does appear to have a long tail that we have not captured in our study"
[^m8]: doi-10-48550-arxiv-2107-06994 — "This criterion may have been conservative in that it"
[^m9]: doi-10-48550-arxiv-2107-06994 — "other strategies and heuristics may be possible"
