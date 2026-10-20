---
description: "Post-training that raises an answer-level metric can lower blind physician ratings of the same model's reasoning and feasibility; the paper calls the gap an alignment paradox."
aliases: ["alignment paradox", "algorithmic-clinical alignment gap", "accuracy-trust divergence after RL alignment"]
sources: ["arxiv-2511-18084"]
---
# Algorithmic–clinical alignment gap

A model can get better on the metric its training optimizes and worse on what experts read in its answers. The concept is the split between two measurements of the same outputs: an automatic score, and a blind expert rating of how the answer reasons and whether its plan can be carried out. Where those two move in opposite directions after post-training, the gain on the first does not buy trust on the second.

In a study of four post-training methods (supervised fine-tuning, SFT; direct preference optimization, DPO; group relative policy optimization, GRPO; in-context learning, ICL) on more than 8,000 infertility treatment records, the GRPO-trained model "achieves the highest algorithmic accuracy across multiple decision layers".[^c1] Yet in the physician panel the ordering reversed. Physicians rated the SFT model higher "on both reasoning capability (p = 0.033, adj. p = 0.048" and clinical feasibility (adj. p = 0.045), with no significant difference in diagnosis accuracy.[^c2][^c3] GRPO had the lower hallucination rate, 15.00% against 18.61%.[^c4] In blind pairwise comparisons, SFT won 51.2% of comparisons, against 26.2% for GRPO and 22.7% for the physicians' own original decisions.[^c5] The authors call this the alignment paradox: "algorithmic improvements do not necessarily translate into higher clinical trust".[^c6]

The mechanism the authors propose is about the reward, not about the method's name. Their GRPO reward is "an answer-centric reward in our implementation", and "the intermediate logical consistency is neither penalized nor rewarded during the alignment".[^c7][^c16] A model rewarded only for the final answer can converge on answers that are right but whose stepwise justification physicians expect, and the fields where the reward does not reach show no gain: "initial diagnosis is not covered by the custom reward function in GRPO", and diagnosis accuracy did not differ between the two models.[^c8] The authors add reward overoptimization, that "reinforcement learning can induce reward overoptimization", so the policy drifts from patterns learned in SFT.[^c9] They introduce both as "We hypothesize" explanations.[^c10]

The same shape shows up across fields. GRPO helped most where the answer space is discrete and the reward is clean, such as ART strategy and rare subtypes, and it fell where several answers are valid: for COS regimen "an answer-level reward can inadvertently penalize reasonable alternatives".[^c11] DPO collapsed on initial diagnosis, with partial and exact matches dropping "substantially (41.29% and 4.63%" against the SFT baseline.[^c12] The authors attribute this to long answers: "The key signals are diluted in long-form reasoning".[^c13] That is a mechanism they propose, not one they isolate.

What the split means for a reader of metrics: a leaderboard gain on an answer-level score says little about whether the reasoning was judged sound. Reporting both the automatic score and an expert rating of the reasoning is what made the gap visible here.

## Limits

- The gap is one study on one institution's records. "the EHRs were all collected from a single institution", and the ground truth is "single-center ground truth".
- Only small open-source models were tested: "our evaluation focuses on small open-source" models, and the authors say they "may underrepresent scaling effects", so whether larger models show the same gap is not established.
- The physician panel is small. It "includes 100 cases", and the authors concede this "may underpower the evaluation of subtle reasoning differences".[^c14]
- The reward explanation is untested in the text read. The authors' own next step is "clinically grounded reward engineering", and no process-aware reward is trained in the paper.[^c15]
- The effect sizes on the physician ratings are small (my reading of the reported Cohen's d values, about 0.2); the significance rests on adjusted p-values near 0.05.
- Whether the gap is caused by reinforcement learning or by the answer-level reward specifically is not separated: GRPO is the only reinforcement method whose reward was reported as answer-centric, so the two are confounded here (my inference).

## Related

- [[attitude-blind-quality-divergence]] — the same split between a blind-rated quality and a second measure, there a stated attitude toward the source
- [[rhetorical-pattern-preference-accuracy-divergence]] — stated preference against measured accuracy, outside training
- [[accuracy-masks-unstable-reasoning]] — a correct answer can hide unstable reasoning; an answer-level reward has the same blind spot
- [[outcome-induced-process-verification]] — the converse design, where an outcome reward is made to check the derivation
- [[solution-multiplicity]] — where several answers are valid, an answer-level reward can penalize the alternatives
- [[metric-criterion-decoupling]] — a score chosen without the criterion it is meant to test

[^c1]: arxiv-2511-18084 — "GRPO achieves the highest algorithmic accuracy across multiple decision layers"
[^c2]: arxiv-2511-18084 — "Physicians preferred more on the SFT model significantly"
[^c3]: arxiv-2511-18084 — "No significant differences observed in diagnosis accuracy between the two models"
[^c4]: arxiv-2511-18084 — "to have a lower rate (15.00%) compared to SFT (18.61%)"
[^c5]: arxiv-2511-18084 — "SFT attains the highest winning rate (51.2%), outperforming both GRPO (26.2%)"
[^c6]: arxiv-2511-18084 — "algorithmic improvements do not necessarily translate into higher clinical trust"
[^c7]: arxiv-2511-18084 — "answer-centric reward in our implementation"
[^c16]: arxiv-2511-18084 — "the intermediate logical consistency is neither penalized nor rewarded during the alignment"
[^c8]: arxiv-2511-18084 — "initial diagnosis is not covered by the custom reward function in GRPO"
[^c9]: arxiv-2511-18084 — "reinforcement learning can induce reward overoptimization"
[^c10]: arxiv-2511-18084 — "We hypothesize that this reverse pattern between superior benchmark scores and superior clinical"
[^c11]: arxiv-2511-18084 — "an answer-level reward can inadvertently penalize reasonable alternatives"
[^c12]: arxiv-2511-18084 — "both partial and exact matches drop substantially (41.29% and 4.63%"
[^c13]: arxiv-2511-18084 — "The key signals are diluted in long-form reasoning"
[^c14]: arxiv-2511-18084 — "may underpower the evaluation of subtle reasoning differences"
[^c15]: arxiv-2511-18084 — "Future work should prioritize developing clinically grounded reward engineering"
