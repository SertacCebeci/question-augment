---
description: "Solution Multiplicity is the mean number of distinct correct solutions per problem; the paper reports that it tracks whether an entropy bonus or an entropy penalty helps a task."
aliases: ["solution multiplicity", "correct-solution multiplicity", "unique correct solutions per problem"]
sources: ["arxiv-2511-19942"]
---
# Solution multiplicity

Two tasks can have the same success rate and still differ in how many distinct correct answers they admit. Solution Multiplicity names that second quantity. The paper defines it as "defining a Solution Multiplicity metric, defined as the average number of unique correct solutions per problem." Over a set X of problems it is the mean of A(x), the number of correct solutions for problem x.[^s1]

The count matters because it decides the sign of a global entropy term. An entropy bonus pushes the policy toward spreading its mass; an entropy penalty pushes it toward a few answers. The paper measured this on four tasks, sampling 200 problems each, by correlating Solution Multiplicity with the change in Pass@8 from adding an entropy bonus.[^s2] The result it reports is that the gain from the bonus grows with the count: "so does the performance gain (Pass@8) of an entropy bonus over vanilla GRPO."[^s3] The table in the text is garbled, so I read it as follows (my reading): Knights-and-Knaves sits at multiplicity 1.5 with an entropy effect of -9.0% on Pass@8, and Countdown at 15.7 with +3.4%.[^s4] The paper's guiding principle follows: for high multiplicity the bonus helps, and for low multiplicity the penalty does.

The mechanism the paper gives is a trade between two kinds of error. When many distinct correct solutions exist, spreading probability over them costs little single-answer correctness, so a diversity-raising term pays. When there is one correct solution, the useful direction is to sharpen onto it. The paper's words are "for tasks with a larger solution space, the benefits of enhanced diversity outweigh the potential trade-offs in single-solution correctness."[^s5] It proposes the count as a pre-training check: "Solution Multiplicity as a practical metric for guiding the decision of whether to increase or decrease entropy for a given task."[^s6]

## Limits

- The relation rests on four tasks, so it is a pattern in the paper's data, not a fitted law. Four points cannot show the shape of the relation or where the sign changes (my inference).
- The count is estimated, not enumerated. The paper says: "To estimate Solution Multiplicity, we query the GPT-5-Think model on 200 randomly selected samples."[^s7] Whether that judge's notion of two solutions being "unique" matches a human's is not checked in the parts I read.
- A count needs two things the paper supplies for its tasks: a verifier that says which answers are correct, and a rule for when two correct solutions are the same. Neither is defined for open-ended questions, so the measure does not carry over to them as stated.
- The count ignores weight. A problem with fifteen correct solutions, where one of them holds most of the probability, has high multiplicity and a sharp distribution at once. The count does not see the distribution; the selection and reinforcement biases concern the distribution over the same correct set (my inference).
- The measure predicts which sign of a global entropy term helps. It does not measure Pass@K, and it says nothing about the differential alternative, which the paper argues does not need the choice of sign.

## Related

- [[rlvr-entropy-collapse]] — the entropy fall that a bonus is meant to counter; the multiplicity decides whether countering it is worth its cost in correctness
- [[effective-diversity]] — also a distinct count, but over generated items that pass a utility check, not over correct solutions to one problem
- [[predictive-multiplicity]] — "multiplicity" in another sense: disagreement among equally accurate models, not among correct answers to one problem

[^s1]: arxiv-2511-19942 — "defining a Solution Multiplicity metric, defined as the average number"
[^s2]: arxiv-2511-19942 — "We measured this metric across four tasks (sampling 200 problems each)"
[^s3]: arxiv-2511-19942 — "so does the performance gain (Pass@8) of an entropy bonus over vanilla GRPO"
[^s4]: arxiv-2511-19942 — "Entropy Effect (for Pass@8) -9.0%"
[^s5]: arxiv-2511-19942 — "for tasks with a larger solution space, the benefits of enhanced diversity outweigh the potential trade-offs in single-solution correctness"
[^s6]: arxiv-2511-19942 — "Solution Multiplicity as a practical metric for guiding the decision of whether to increase or decrease"
[^s7]: arxiv-2511-19942 — "To estimate Solution Multiplicity, we query the GPT-5-Think model on 200 randomly selected samples"
