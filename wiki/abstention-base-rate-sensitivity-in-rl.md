---
description: "In RL with an abstention reward, the share of unanswerable questions in training decides the outcome: too few and the model never abstains, balanced to 50% and it collapses into always abstaining."
aliases: ["unanswerable-ratio sensitivity in abstention RL", "always-abstain collapse", "abstention data-ratio effect"]
sources: ["arxiv-2602-04755"]
---
# Abstention base-rate sensitivity in RL

When a model is trained with reinforcement learning to answer or say "No Answer", the reward is a rule: 1.0 for "No Answer" on an unanswerable question, ROUGE-L plus exact match for a correct answer on an answerable one, and 0 otherwise.[^c1] Under such a reward, the fraction of unanswerable items in the training set acts as a hidden control on behavior. Zhou et al. (arxiv-2602-04755) tested this on TimeQA-Easy, where unanswerable questions are only 12.4% of training data.

## What happens at each base rate

- **Natural distribution (about 12% unanswerable).** The model "largely ignores abstention", because unanswerable cases are too rare to move the reward.[^c2]
- **Balanced to 50%.** The problem flips: abstention becomes a trivial shortcut with a much simpler action space that is optimized faster, and the model collapses into "always abstain".[^c2]

The authors conclude that robust abstention needs both reward design and control of the data distribution and training dynamics.[^c3] Their reward ablations support the "reward is delicate" half. ROUGE alone hurts on the Hard split, where lexical overlap fails to capture temporal reasoning, and swapping exact match for BERTScore lowers Easy accuracy, because semantic similarity can reward plausible but wrong answers.[^c4]

## Why it matters for asking and answering

The point is that "abstain when you should" is not one skill to be rewarded in isolation. It is a decision whose payoff depends on how often abstention is correct in the training stream. Too sparse a signal gives no learning, and too dense a signal gives a cheap policy that beats the harder one. My inference, not measured in the paper: the same would hold for any trained ask-or-answer decision, such as clarification, where the base rate of "needs a question" shapes whether the policy learns discrimination or a constant.

## Related behaviors reported alongside

- Supervised fine-tuning shifted models from over-cautious to over-confident: fewer false positives, but also fewer true positives and more false negatives.[^c5]
- After RL, abstention improved on TimeQA-Easy but reversed on TimeQA-Hard, where the model avoided abstention and false negatives rose sharply.[^c6]
- Adding more knowledge-graph facts to the prompt made the model abstain less, a trade-off between answer accuracy and abstention.[^c7]
- Abstention learned on temporal QA did not generalize to out-of-distribution tasks.[^c8]

## Limits

- One dataset family (TimeQA), one small base model (Qwen2.5-1.5B-Instruct) for the ratio experiment, and only two ratios (12.4% and 50%); no intermediate mix was reported, so the location of the transition between "ignores" and "always abstains" is unknown.
- The explanation (abstention as a simpler action space optimized faster) is the authors' reading, not tested by intervention.
- The reward was a single hand-made rule; whether a reward that penalizes constant policies would remove the collapse was not shown.
- The generality claim in the last section is my inference.

## Related

- [[refusal-shortcut-learning]] — a refusal bound to cheap cues rather than to intent; here the cheap cue is the label base rate
- [[informed-abstention-framework]] — when abstention is warranted at all
- [[accuracy-masks-selective-reliability]] — accuracy alone hides the abstention behavior
- [[selective-abstraction]] — the answer-or-abstain trade-off this training tries to learn

[^c1]: arxiv-2602-04755 — "where we set the reward to 1.0 for encouraging the model to be honest if it generates “No Answer”"
[^c2]: arxiv-2602-04755 — "In the natural distribution, the model largely ignores abstention because unanswerable cases are too rare to impact reward maximization."
[^c3]: arxiv-2602-04755 — "achieving robust abstention requires not only carefully adjusting the reward design but also controlling the data distribution and training dynamics."
[^c4]: arxiv-2602-04755 — "Replacing EM with BERTScore lowers"
[^c5]: arxiv-2602-04755 — "SFT shifts models from over-cautious"
[^c6]: arxiv-2602-04755 — "the model avoids abstention and sharply increases false"
[^c7]: arxiv-2602-04755 — "With more KGs, the model abstains less frequently."
[^c8]: arxiv-2602-04755 — "All experiments illustrate that abstention"
