---
description: "Rank candidate clarification questions by the expected completeness gain of the post over a distribution of likely answers; learned jointly, it beat answer-aware baselines without the sum."
aliases: ["neural EVPI question ranking", "EVPI clarification ranking", "expected utility over answers"]
sources: ["rao-2018"]
---
# Expected answer utility ranking

A question is scored not by how it reads but by what its answers would do to the text that prompted it. Rao and Daumé (2018) borrow the expected value of perfect information ([[value-of-information]]) and write the value of a candidate question as the sum, over possible answers, of the answer's probability times the utility of the post once that answer is added.[^c1] Here the post is the asker's incomplete text, the utility measures "how much more complete p would be if it were augmented with answer aj", and the probability is that of getting the answer given the post and the question.[^c2] Two things must therefore be modelled: the answer distribution and the utility.

## Mechanism

**Candidates from neighbours.** Questions are not generated. For a post, the ten most similar posts are retrieved with a TF-IDF engine; their questions become the candidate questions and the edits their askers made in reply become the candidate answers. The original post is always its own nearest neighbour, so the true question and answer are always among the candidates.[^c3]

**Answer model.** An answer representation is computed from post and question, and the likelihood of a candidate answer is an exponentiated negative cosine distance to it, multiplied by the similarity between the asked question and the question that candidate answer was paired with.[^c4] The training loss pulls the representation toward the true answer and also toward the answers of questions similar to the true one, reflecting that one question can be phrased many ways and have many valid answers (the paper's example: "Ubuntu 14.04 LTS", "Ubuntu 12.0", "Ubuntu 9.0").[^c5]

**Utility calculator.** A classifier scores the triple (post, question, answer); the original triple is a positive, the other nine candidate pairs are negatives. The authors note this labelling is noisy, because a question not paired with the post can still be a good one.[^c6] The authors find the utility works better when the question paired with the answer is an input, though in theory post and answer should suffice, which they attribute to the question carrying information about whether an answer completes the post.[^c7]

**Joint training and ranking.** Both parts are trained end to end, so that an answer with more potential to raise the post's utility gets higher probability; at test time the candidates are ranked by the expected utility.

## What was measured

Against expert human annotations of "best" and "valid" questions, the EVPI model beat the neural baseline that sees the same post, question and answer with the same parameter count. The difference is that EVPI uses alternate question and answer candidates in its loss, and the authors read this as showing that summing the utilities of questions similar to the original gives a boost.[^c8] Baselines that use answers beat the one that sees only post and question, so the answer is informative about which question to ask.[^c9] When the original question was excluded from the candidates, the neural models beat non-neural baselines but differences among the neural models were statistically insignificant.[^c10]

## Limits

- The claimed edge over the answer-aware baseline vanishes when the true question is removed from the candidate set; the authors call the in-set evaluation "overly optimistic".[^c11]
- The "utility" is a learned proxy trained to separate the original triple from neighbours' triples, not a decision-theoretic value over actions. It shares [[value-of-information]]'s name only: no action set, no baseline decision, no net-of-cost term. That reading is mine.
- Candidates are drawn from questions already asked on similar posts, so a question unlike any in the corpus cannot be ranked; this is ranking, not generation (compare [[self-supervised-clarification-question-generation]]).
- Utility is completeness of a text, in one forum domain; it is not shown to carry over to a task where the answer changes a downstream decision.
- The paper did not test whether asking the highest-ranked question helps a human answerer more than the others.

## Related

- [[value-of-information]] — the decision-analytic quantity this model imitates; here the utility is learned, not defined by actions
- [[clarification-utility]] — what makes a clarification question worth asking
- [[tool-call-evpi-question-selection]] — a later use of the same EVPI scoring idea
- [[expected-information-gain]] — the information-only alternative that ignores utility
- [[clarification-request]] — the act whose candidates are being ranked

[^c1]: rao-2018 — "The value of this question qi is the expected utility, over all possible answers:"
[^c2]: rao-2018 — "U(p + aj ) is a utility"
[^c3]: rao-2018 — "We consider the questions"
[^c4]: rao-2018 — "The likelihood of an answer candidate aj being"
[^c5]: rao-2018 — "a question can be asked in several"
[^c6]: rao-2018 — "It should be noted that this is a noisy"
[^c7]: rao-2018 — "we find that our neural EVPI model performs better when the candidate question"
[^c8]: rao-2018 — "This shows that when the candidate set consists"
[^c9]: rao-2018 — "showing that answer helps in selecting the right"
[^c10]: rao-2018 — "However, the differences between all the neural models are statistically insignificant."
[^c11]: rao-2018 — "it is overly optimistic."
