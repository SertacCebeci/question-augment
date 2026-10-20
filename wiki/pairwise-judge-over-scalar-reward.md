---
description: "LM judges are weaker at scoring one output on a number than at picking the better of two; in one safety-training ablation the scoring judge was easier to exploit than the pairwise one."
aliases: ["pairwise preference judge", "binary preference judge", "pair-wise vs point-wise judge"]
sources: ["arxiv-2512-20806"]
---
# Pairwise judge over scalar reward

A reward for training a language model can come from a judge that gives each output a number, or from one that says which of two outputs is better. Paulus et al. choose the second. Their reason, taken from Lanchantin et al. (2025), is that "LM judges have difficulty providing accurate scalar scores, but perform better at"[^c1] "making a binary preference decision."[^c2] A pairwise judge therefore yields a winner and a loser for each pair, not a score.

**Mechanism, concretely.** The judge is applied to two responses to the same prompt (for the defender) or to two attack queries with their responses (for the attacker). Under the Bradley-Terry assumption, the probability that one output beats the other is a logistic function of a difference in implicit rewards: "these preferences can be related back to implicit rewards via"[^c3] a sigmoid of the reward difference. The training losses are DPO-style, so they use only the preference pairs; the paper notes that its DPO and IPO variants do "not actually use them during training as they only need" preference pairs, and computes reward only for logging.[^c4]

**The evidence in the paper.** In its ablation, replacing the pairwise judge with a point-wise one shows "a clear" loss, a "drop in both safety and utility performance."[^c5] The authors read this as a reward-hacking effect: a point-wise score is easier to push up without the behaviour being right. Their words: "to exploit the reward hacking. In contrast, it seems pair-wise"[^c6] judging "is more robust and less prone to such exploitation,"[^c7] which is why they use it.

**What transfers to answering (my inference).** A pairwise judge asks a simpler question per call: which of these two is better, not how good is this one on an absolute scale. That is the property the paper relies on, and it bears on answer evaluation as much as on training. The cost is that a set of n answers needs pairwise comparisons or a tournament to rank, and that position can bias a single comparison. Both are handled elsewhere in the wiki (see the Related notes), and neither is tested in this paper.

**What does not transfer.** The paper's judge is one language model under different templates, used inside adversarial safety training. The pairwise result is about that setting. The authors do not claim generality: "not claiming that this universally holds."[^c8]

## Limits

- One paper, one family of safety-training runs. The claim that pairwise judging resists exploitation is an observation from this ablation, not a theorem; the authors say better reward design "might (partially) address the problem" for point-wise scores too.
- The mechanism of the robustness is not explained in the text. "It seems" is the paper's own hedge.
- A pairwise judge is not a drop-in: in this paper it sits inside a faithfulness gate, and when neither attack is faithful the preference is a tie at one half (see [[faithfulness-gated-attack-reward]]). Ties need handling that a scalar score does not.
- Whether the pairwise advantage holds for grading open answers, rather than for the safety comparisons measured here, is not tested in the work.

## Related

- [[bradley-terry-preference-model]] — the model that turns a pairwise preference into a reward difference, used here.
- [[bidirectional-preference-entropy]] — a pairwise judge scored in both response orders, with the binary entropy of the averaged preference as an order-neutral uncertainty score; a route to the order-position problem named above.
- [[reward-overoptimization]] — the general failure in which a reward is pushed past what it measures, which the pairwise choice is meant to slow.
- [[non-zero-sum-attacker-reward]] — the attacker payoff that is built from these pairwise winners and losers.
- [[swiss-system-tournament-evaluation]] — tournament-style ranking from pairwise results, the cost side of replacing scores with comparisons.

[^c1]: arxiv-2512-20806 — "LM judges have difficulty providing accurate scalar scores, but perform better at"
[^c2]: arxiv-2512-20806 — "making a binary preference decision"
[^c3]: arxiv-2512-20806 — "these preferences can be related back to implicit rewards via"
[^c4]: arxiv-2512-20806 — "not actually use them during training as they only need"
[^c5]: arxiv-2512-20806 — "drop in both safety and utility performance"
[^c6]: arxiv-2512-20806 — "to exploit the reward hacking. In contrast, it seems pair-wise"
[^c7]: arxiv-2512-20806 — "judging is more robust and less prone to such exploitation,"
[^c8]: arxiv-2512-20806 — "not claiming that this universally holds"
