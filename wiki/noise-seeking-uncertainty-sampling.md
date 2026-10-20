---
description: "Uncertainty-based active learners can spend every label on points whose answer is a coin flip, harmless under excess error; a learner that may abstain avoids this trap."
aliases: ["noise-seeking", "noise-seeking conditions", "uncertainty-based active learner trap", "wasteful uncertainty sampling"]
sources: ["arxiv-2512-23924"]
---
# Noise-seeking: uncertainty-based querying spends labels on harmless points

An active learner chooses which unlabelled point to query next. The natural rule is to query where it is uncertain. The dissertation points out what that rule does when the conditional probability η(x) = P(y = 1 | x) sits close to 1/2 over a large part of the input space. There the label is close to a fair coin, and the prediction made at that point barely changes the excess error. The text calls such points "harmless": they are not harmless in the sense of being absent, only in the sense that a wrong guess there costs little.[^n1]

The trap is that an uncertainty-based learner cannot decide whether |η(x) − 1/2| is zero or merely small. In the text's words, it "requests the label for any point that is uncertain, i.e., the algorithm cannot decide if |η(x) − 1/2| is strictly greater than 0." So it keeps querying in exactly those regions, and the labels it buys there are spent on points where a mistake is cheap, while "other regions where erring could be much more harmful" are left under-sampled.[^n2]

The dissertation names the class of distributions that allow this: noise-seeking conditions, which strictly generalise the Massart and Tsybakov conditions by allowing abundant points with η(x) equal or close to 1/2.[^n3] Under them it states a lower bound. For any labelling budget B of the required order, there is a learning problem on which any uncertainty-based active learner has standard excess error at least of order 1/B, while the algorithm the chapter builds reaches standard excess error at most ε on that same problem.[^n4] The loss is therefore not a constant factor: the trap keeps the error of an uncertainty-based learner from falling below a rate set by its budget.

The mechanism, in one line and as my own reading rather than the text's claim: the querying rule scores points by how undecided the learner is about the sign of η − 1/2, and nothing in that score asks whether the answer changes what the learner would predict. Under excess error those two questions come apart. The chapter's remedy is to let the learner abstain at a named price, so that a point near 1/2 can be left unlabelled and marked as abstained instead of queried. The price is small by design: "The price of abstention is only marginally smaller than random" guessing.[^n5]

For the asker's side, the transferable point is about the score, not the model: a question chosen for uncertainty about the answer is not the same as a question chosen for what the answer would change. A selection rule that does not separate these two can spend its budget on questions whose answers are irrelevant to the decision that the asker actually faces.

## Limits

- The lower bound is for a constructed learning problem. This reading used the informal statement (Proposition 2.4 in the text) and did not read the formal version in Section 2.3.2, so the exact class of "uncertainty-based" learners is taken from the chapter's informal description only.
- It is a theorem about a worst-case instance. The text does not measure how often real uncertainty-sampling pipelines fall into this trap at practical sizes.
- The verdict "harmless" is relative to excess error. Under another loss a point with η near 1/2 may matter, and the note does not carry the verdict across losses.
- The remedy needs the cost of abstaining to be stated. Where no such cost is named, abstention has no price and the argument does not apply.
- The noise conditions that make the trap possible are the ones the chapter generalises. How much of the trap survives under the usual Massart condition is a separate question, handled in [[massart-tsybakov-noise]].

## Related

- [[abstention]] — abstention with a named cost is the chapter's remedy for the trap; the reject option itself predates it
- [[massart-tsybakov-noise]] — the low-noise conditions that the noise-seeking conditions generalise
- [[expected-information-gain]] — the information-maximising score that uncertainty sampling approximates; the trap concerns what such scores pick
- [[label-complexity-as-noisy-lossy-compression]] — a different lower bound on the labels a noisy pool needs

[^n1]: arxiv-2512-23924 — "can, however, cause troubles for any active learning algorithm that"
[^n2]: arxiv-2512-23924 — "ignoring other regions where erring could be much more harmful"
[^n3]: arxiv-2512-23924 — "the noise-seeking conditions allow abundant data points with"
[^n4]: arxiv-2512-23924 — "any uncertainty-based active learner suffers standard excess"
[^n5]: arxiv-2512-23924 — "The price of abstention is only marginally smaller than random"
