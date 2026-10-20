---
description: "The share of correctly answered samples whose reasoning block concludes the same option as the final answer tag; high scores can coexist with low accuracy, so it is a second axis."
aliases: ["TAC", "think-answer agreement", "reasoning-answer consistency rate", "Think–Answer Consistency"]
sources: ["arxiv-2511-23478"]
---
# Think–answer consistency

A reasoning model writes a reasoning block and then an answer tag. Nothing in the format forces the two to agree: the reasoning can conclude one option while the tag reports another. Video-R2 turns this into a measured quantity, Think–Answer Consistency (TAC). For a model and a dataset, TAC is the fraction of samples whose reasoning-block conclusion equals the final answer, and the paper states it is computed only over the samples the model answered correctly.[^c1][^c2] A reasoning block that argues for A under a tag reading E is counted as a failure of the link, even when E is the right answer.

The measure is a rate over outputs. By my reading of the formula it needs only the two extracted answers, not a gold label for the consistency itself; the paper reads its complement as the share of correct answers reached for unclear or contradictory reasons: "The value of (1 − TAC) indicates the proportion of" such correctness.[^c8] The restriction to correct samples is a design choice the authors give: consistency among wrong answers would "convey a false sense of better performance," so they leave those out.[^c3]

The paper's figures show the measure moving with training stage, and not in the direction accuracy moves. Timestamp-aware supervised fine-tuning raised TAC from 55.5 to 96.8 over the chain-of-thought baseline, with accuracy rising only slightly.[^c4] Adding GRPO on the final answer then raised accuracy while TAC fell, "(96.8 → 76.8)", because "the GRPO reward is only applied to the final answer", and the authors read this as policy optimization exploiting "answerlevel shortcuts rather than improve actual reasoning behavior".[^c5][^c6] The authors call the high-TAC, low-accuracy end of this the SFT consistency paradox: a model can be almost perfectly coherent and still often wrong. This is why TAC is a second axis: a reward that scores only the answer can raise accuracy while moving TAC the other way (my reading of the paper's pairing of the two results).

The paper also uses TAC as a gate on training. The temporal reward is multiplied by an indicator that the reasoning conclusion matches the answer, and "the gating ensures that temporally precise reasoning is rewarded" only where the two agree; the authors report overall TAC rising from 77.5 to 81.6 with the gate on.[^c9] The consistency check thus moves from a diagnostic into a reward term. That use is treated in [[answer-reasoning-consistency-reward]], which scores agreement differently.

## Limits

- The text I read gives the definition, not the extraction rule. How the "conclusion" of a free-form reasoning block is read off, and how the match is judged for open answers, is not described in the parts I read. For multiple choice the rule is an equality of letters (my reading of the formula).
- Agreement is not derivation. TAC says the conclusion in the block and the tag match; it does not show the tag was computed from the block. A post-hoc rationale can be consistent (my inference).
- TAC is conditioned on correctness. It says nothing about consistency on wrong answers, which the authors exclude by design.
- High TAC is not high accuracy, and the paper's own data show the two trading off under its training. A TAC gain is not evidence of a better model on its own.
- Visual dependence is a separate axis. TAC does not measure whether the reasoning used the video, which is why the paper pairs it with [[claimed-visual-reliance-score]].
- One paper, one model family, one set of 11 video benchmarks; the human check of the training data (500 samples) concerns data quality, not whether TAC tracks anything outside this setup.

## Related

- [[answer-reasoning-consistency-reward]] — the reward that trains the link TAC measures; its score is a probability lift on the gold answer, not a match of two extracted answers
- [[process-outcome-consistency-verification]] — a verifier that accepts an answer only when its derivation agrees with it, the same link checked by a model rather than by string match
- [[outcome-induced-process-verification]] — outcome-only RL can make a verifier check its own steps, the opposite drift from the answer-only shortcut reported here
- [[cot-hallucination-trap]] — a fluent rationale not tied to the image, which a consistency rate would not catch
- [[reasoning-path-fidelity]] — coverage of expert checkpoints, a separate measure of reasoning quality
- [[claimed-visual-reliance-score]] — the visual-reliance axis Video-R2 pairs with TAC

[^c1]: arxiv-2511-23478 — "A high TAC value indicates coherent reasoning, where the model concludes the same output in both"
[^c2]: arxiv-2511-23478 — "TAC ∈ [0, 1] thus represents the fraction of correct samples"
[^c3]: arxiv-2511-23478 — "only for the subset containing correctly answered samples,"
[^c4]: arxiv-2511-23478 — "with TAC increasing from 55.5 to 96.8 and VAS from 44.3 to 69.7"
[^c5]: arxiv-2511-23478 — "the GRPO reward is only applied to the final answer"
[^c6]: arxiv-2511-23478 — "policy optimization tends to exploit answerlevel shortcuts rather than improve actual reasoning behavior"
[^c7]: arxiv-2511-23478 — "underscoring an open tradeoff between interpretability and performance"
[^c8]: arxiv-2511-23478 — "The value of (1 − TAC) indicates the proportion of"
[^c9]: arxiv-2511-23478 — "The gating ensures that temporally precise reasoning is rewarded"
