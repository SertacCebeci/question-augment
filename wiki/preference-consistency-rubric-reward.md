---
description: "A rubric generator can be trained by rewarding whether its rubric ranks the human-preferred report above the rejected one; format and judge-quality rewards act only as auxiliaries."
aliases: ["preference-grounded rubric generation", "learned query-specific rubrics"]
sources: ["arxiv-2602-03619", "doi-10-48550-arxiv-2605-03871"]
---
# Preference-consistency rubric reward

Query-specific rubrics are usually written by experts (costly) or prompted from an LLM (generic, weakly tied to what people prefer). The alternative here is to train the rubric writer itself on human pairwise judgments. A policy samples a group of rubrics for a query; each rubric is a weighted list of items with title, description and importance weight.[^c1]

A report is scored under a rubric as the weighted mean of judge-assigned item scores, S = sum(w_k v_k) / sum(w_k), each v_k a 1-10 Likert rating normalized to [0, 1].[^c2] The rubric's reward is +1 if it scores the human-accepted report above the rejected one for the same query, and -1 otherwise.[^c3] A rubric is thus rewarded for being discriminative in the direction humans chose, not for looking thorough.

Two auxiliary terms complete the hybrid: a hard format penalty of -1 for rubrics that fail the JSON schema the downstream pipeline needs, and an LLM-judge score of the rubric's coherence, coverage and relevance.[^c4] The total is a weighted sum, trained with GRPO.

What was measured: learned rubrics separated preferred from rejected reports better than generic, prompted or SFT-derived rubrics. Prompting and SFT gave some accuracy gains but a small paired Cohen's d, "indicating limited alignment with human preference margins."[^c5] RL with preference rewards raised the effect size markedly, and hybrid reward gave the best accuracy while preference-only RL was close and had the largest effect size on one backbone, so the authors read the human-preference reward as the primary signal and the others as constraints.[^c6] Used as the reward inside agentic RL for report generation, the RL-trained rubric generator beat human-defined general rubrics, GPT-5-generated rubrics and the SFT generator on DeepResearch Bench.[^c7]

A later paper gives the same reward a latent-variable reading. EvoLM treats the rubric as a latent variable that explains an observed preference: "This motivates treating the rubric as a latent variable that explains observed preferences."[^c8] The likelihood of a preference is a sigmoid of the judge's score gap under that rubric, and the rubric generator is trained toward it with a KL term back to the base model's prior over rubrics.[^c9] In practice the reward is a margin on the score gap, "where α = 0.7," combined with a format term.[^c10] The explanatory framing answers the limit below: the rubric is asked to explain the preference, not only to agree with it. The preference pairs differ, though. EvoLM's pairs are not human labels; they come from the policy's own outputs over training (see [[temporal-contrast-preference-pairs]]), so the explanation covers the policy's own drift, not human judgment (my inference).

## Limits

- The preference label is coarse (one binary choice per report pair); the rubric is only required to agree with it, not to explain it. Whether items reflect real quality dimensions versus judge quirks is not tested here (my inference).
- The reward depends on a judge LLM scoring items, so judge biases pass into the learned rubric.
- Hybrid versus preference-only differences are small; the auxiliary rewards' contribution is not cleanly established.
- Evidence is for long-form DeepResearch reports and one benchmark protocol; transfer to other asking or answering tasks is untested.

## Related

- [[pretraining-grounded-rubric-self-play]] — another route to learned query-specific rubrics, grounded in reference text rather than human preferences
- [[rubric-formation-gap]] — why rubric quality, not just judging, limits reward signals
- [[llm-judge-biases]] — biases of the judge that scores items under the rubric

[^c1]: arxiv-2602-03619 — "forming a weighted list of assessment dimensions (e.g., in JSON format)."
[^c2]: arxiv-2602-03619 — "Each vk is rated on a"
[^c3]: arxiv-2602-03619 — "determined by whether the rubric correctly ranks"
[^c4]: arxiv-2602-03619 — "Candidates that fail"
[^c5]: arxiv-2602-03619 — "indicating limited alignment with human preference margins."
[^c6]: arxiv-2602-03619 — "RL with hybrid rewards achieves the best preference accuracy, while"
[^c7]: arxiv-2602-03619 — "It outperforms humandefined general rubrics, GPT5-generated rubrics,"
[^c8]: doi-10-48550-arxiv-2605-03871 — "This motivates treating the rubric as a latent variable that explains observed preferences."
[^c9]: doi-10-48550-arxiv-2605-03871 — "we maximize the evidence lower bound (ELBO)"
[^c10]: doi-10-48550-arxiv-2605-03871 — "The margin provides continuous signal proportional to the score gap"
