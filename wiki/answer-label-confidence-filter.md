---
description: "A generated multiple-choice item is kept only if its generator's next-token probabilities over the option labels peak above a high threshold; a flat spread marks an ambiguous item."
aliases: ["option-label probability filter", "answer-confidence filter for generated MCQs", "choice-probability validation"]
sources: ["arxiv-2512-10110"]
---
# Answer-label confidence filter

A multiple-choice item can be checked by the model that wrote it. Put the stem and its options into an answer prompt that ends in "Answer:", and the most likely next token is one of the option labels. When the weights are open, the probabilities over those labels can be read directly: "we can extract the next-token probabilities for these labels", and a softmax over them gives a distribution the model holds over its own answer.[^c1] The filter keeps the items whose distribution is peaked: "we prefer questions whose choice distribution has an outstanding peak".[^c2] Concretely, an item survives only if its most probable option is above a high threshold, 0.9 in the paper, and is not the added "none of the above" option.[^c3]

Two steps make that reading usable. The options are shuffled first, "to mitigate the position bias where Phi-2 may unevenly choose a particular position", a bias the same kind of model shows when it writes a key (see [[mcq-answer-position-bias]]).[^c4] A "none of the above" option is added for this step only, "to allow Phi-2 to indicate that none of the answer choices provided is correct".[^c5] A flat distribution is then read as a sign of ambiguity: the model "is equally confident about all choices", so the item may have no single key, or "all of the above" as its key.[^c6]

The threshold is a volume trade. The retained count "steadily decreased from 6,043 at the baseline (Version A) to about 2,856 at the 95% threshold",[^c7] while the agreement between the model and a second judge on the keyed answer "improved from 0.67 at the baseline to 0.91 at the 95% threshold".[^c8] The second judge there is Gemini, not a person. The one comparison with people is on 64 items: "The pairwise agreement between Phi-2 and human judges was higher than that between human judges".[^c9] The 0.9 threshold was first set by intuition; the authors write that "we did not have empirical evidence to support this intuition" before the ablation.[^c10]

What this filter measures is answerability: whether the generator settles on one key. It is one forward pass with no sampling, unlike the vote share over sampled solver answers in [[double-confidence-filtering]]. It is also a probability read from tokens, not a confidence the model states in words, unlike [[log-score-verbalized-confidence-reward]]. Within a generate-then-validate pipeline it is the answer-side check on a candidate list that is cut down, not extended (see [[generate-then-verify-candidate-pipeline]]).

## Limits

- One generator (Phi-2, "a 2.7B-parameter SLM"),[^c11] one prompt template, and one domain: the human study used eight AP environmental science objectives. Nothing here shows the filter transfers to other generators, item formats or subjects, and the threshold curve is for one model.
- The ablation's agreement is between two models, Phi-2 and Gemini. Two judges can agree on a wrong key. The paper does not measure how often a confident, consistent wrong key passes; a peaked distribution is confidence, not truth (my inference).
- The filter's cost is the discard: "it seems wasteful to generate so many questions initially, only to discard a large portion of them".[^c12] The authors argue the trade is worth it. The token cost per kept item is not reported in the text read.
- The shuffle and the added "none of the above" option are design choices. Their separate effect on the peak is not isolated in the text read.

## Related

- [[generate-then-verify-candidate-pipeline]] — the same generate-then-check shape; here the checker is the generator's own label probabilities, not a second model's verdict.
- [[double-confidence-filtering]] — keeps items by the vote share over sampled solver answers, a relative test; this filter reads one forward pass.
- [[log-score-verbalized-confidence-reward]] — confidence the model states in words, trained with a scoring rule; this one reads token probabilities and is not trained.
- [[mcq-answer-position-bias]] — the position skew that the shuffle is there to remove.

[^c1]: arxiv-2512-10110 — "we can extract the next-token probabilities for these labels"
[^c2]: arxiv-2512-10110 — "we prefer questions whose choice distribution has an outstanding peak"
[^c3]: arxiv-2512-10110 — "we only select questions whose most probable choice has a probability greater than a high threshold (e.g., 90%)"
[^c4]: arxiv-2512-10110 — "to mitigate the position bias where Phi-2 may unevenly choose a particular position"
[^c5]: arxiv-2512-10110 — "to allow Phi-2 to indicate that none of the answer choices provided is correct"
[^c6]: arxiv-2512-10110 — "since Phi-2 is equally confident about all choices"
[^c7]: arxiv-2512-10110 — "steadily decreased from 6,043 at the baseline (Version A) to about 2,856 at the 95% threshold"
[^c8]: arxiv-2512-10110 — "improved from 0.67 at the baseline to 0.91 at the 95% threshold"
[^c9]: arxiv-2512-10110 — "The pairwise agreement between Phi-2 and human judges was higher than that between human judges"
[^c10]: arxiv-2512-10110 — "we did not have empirical evidence to support this intuition"
[^c11]: arxiv-2512-10110 — "a 2.7B-parameter SLM"
[^c12]: arxiv-2512-10110 — "it seems wasteful to generate so many questions initially, only to discard a large portion of them"
