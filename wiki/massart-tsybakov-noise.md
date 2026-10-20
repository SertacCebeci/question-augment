---
description: "Massart and Tsybakov noise limit how often a label is close to a coin flip; under them active learning saves labels, while in high noise a classical lower bound says it may not."
aliases: ["Massart noise", "Tsybakov noise", "low-noise conditions for active learning", "margin condition"]
sources: ["arxiv-2512-23924"]
---
# Massart and Tsybakov noise conditions

Active learning saves labels only when the labelling noise has a certain shape. Two standard conditions describe that shape. Both concern the conditional probability η(x) = P(y = 1 | x) and how often it lies near the decision boundary 1/2. Massart noise forbids ambiguity altogether: for some constant τ0 > 0, no point may have η(x) within τ0 of 1/2.[^m1] Tsybakov noise is a softer condition, with a parameter β ≥ 0 that governs how much probability mass can sit near 1/2.[^m2] This reading did not read the full formal definition of the Tsybakov parameter.

The payoff under Massart noise is a sharp count. In the single-point case, η(x) stays at least τ0 away from 1/2, so a learner needs only a number of labels governed by τ0 and log(1/δ), with no dependence on the target accuracy ε, "no matter how small ε is".[^m3] The dissertation extends this to a general finite class of regression functions: there is an algorithm whose label complexity, measured in terms of the eluder dimension of the class and log(|F|/δ), divided by τ0², is "independent of" 1/ε.[^m4]

The reason these conditions are a focus is the reverse regime. The chapter says a classical lower bound shows that, in high-noise regimes, active learning gives no improvement over passive learning.[^m5] Massart and Tsybakov noise are the assumptions under which the known savings hold; outside them the advantage of querying is not guaranteed. The chapter's own aim is to remove the dependence on these assumptions, which it does with an abstention option (see [[abstention]]).

The transferable point for asking is that the noise regime, not only the model class, decides whether a querying rule can pay off. The dependence is on the shape of the noise near the boundary: a region where answers are nearly random behaves differently from one where they are reliable.

## Limits

- The conditions are stated for binary classification with a labelling oracle that returns y drawn from a conditional distribution. η(x) is a probability an open-ended answerer does not expose, so the conditions do not map directly onto free-text answers.
- The margin τ0 and the exponent β are parameters of the distribution. The text does not estimate them for any real task, and nothing here says how a learner would find out which regime it is in.
- The constant-label-complexity result is stated informally in the text and holds for a finite or bounded-complexity class; it is not a claim about arbitrary model families.
- The "classical lower bound" for high-noise regimes is cited in the chapter, not proved in the portion read here.
- Under Chow's excess error the chapter states a comparable constant label complexity "without any low noise assumptions", so these conditions are not the only route to small label counts; the claim is only that the standard route needs them.[^m6]

## Related

- [[noise-seeking-uncertainty-sampling]] — the noise-seeking conditions generalise these, and there uncertainty-based querying is shown to waste labels
- [[abstention]] — the reject option with a named cost is the chapter's route around the high-noise barrier
- [[label-complexity-as-noisy-lossy-compression]] — a finite-blocklength lower bound on the labels a noisy pool needs, from a different angle

[^m1]: arxiv-2512-23924 — "which assumes that no data point has conditional expectation close to the decision boundary"
[^m2]: arxiv-2512-23924 — "the Tsybakov noise condition with parameter"
[^m3]: arxiv-2512-23924 — "no matter how small"
[^m4]: arxiv-2512-23924 — "which is independent of"
[^m5]: arxiv-2512-23924 — "is a classical lower bound showing that, in high-noise regimes, active"
[^m6]: arxiv-2512-23924 — "without any low noise assumptions"
