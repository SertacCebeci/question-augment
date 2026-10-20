---
description: "Under an outcome reward that scores a missing answer and a wrong answer alike, RL training of a search agent can collapse into not answering; a small per-action penalty stopped the collapse."
aliases: ["answer refusal collapse", "answer withholding under F1 reward", "no-answer collapse"]
sources: ["doi-10-48550-arxiv-2602-19526"]
---
# Answer avoidance collapse

When a search agent is trained with reinforcement learning on an outcome reward alone, the reward can teach it to stop answering. The mechanism is a zero-credit tie: if a missing answer and a wrong answer both earn zero, withholding the answer is a free way to avoid the risk of being wrong. In the Search-R1 setting the authors trained with an F1 reward, the failure showed up as sharp drops in the overall score, and these drops coincided with "a significant decline in the answer rate, whereas the accuracy of the answered samples remains relatively" stable.[^c1] Their reading is that "the dominant failure mode is not incorrect answering," but a shrinking share of answers.[^c2]

The authors' explanation is that outcome supervision places no constraint on the decision to act. "Since missing an answer receives the same zero reward as an incorrect one," the policy "tends to collapse into a simpler state of generating no answer, effectively avoiding the effort of complex reasoning."[^c3] The abstract states the same finding for the comparison with exact-match reward: the F1-based reward underperforms because of "training collapse driven by answer avoidance".[^c4]

## Mechanism of the repair

The repair is a penalty on the absence of a decision, added to the outcome reward. The authors take the F1 reward and subtract a term when a step performs no search or produces no answer: R = R_F1 − α·I[no search] − β·I[no answer], with α = β = 0.1 in the reported runs.[^c5] Each penalty is an indicator on the action count, so it is cheap to compute and does not score the content of the answer. The stated purpose is to "discourage omitting search or answer steps", which removes the zero-credit tie that made withholding attractive.[^c6]

The measured effect is that these constraints "stabilize training dynamics by eliminating the answer" refusal failure mode.[^c7] The F1 model with the penalties "not only recovers from instability, but also surpasses the EM baseline in final" performance.[^c8] So the reward that had collapsed ended up the better one. The authors' reading is that direct supervision of the decisions is what restores stability; my inference, not stated in the paper, is that the penalty works by removing the zero-credit tie itself.

## Limits

- The authors concede that forcing actions "carries a theoretical risk of reward hacking" and report only that their own runs show "a positive effect".[^c9] An agent that searches or answers on every step to avoid the penalty, whether or not the answer is good, is not ruled out by this evidence.
- The collapse is inferred from training curves and answer rates, not from an intervention on the reward alone. The paper shows that the penalty stops the drop; it does not isolate answer avoidance as the only cause of the drop.
- The results are for one model family (Qwen2.5, 3B and 7B), one retriever setup (E5 over 2018 Wikipedia, top-3 passages) and one training pipeline. The authors report they "cannot fully match the reported" Search-R1 numbers, so the baseline itself is not a clean reproduction.
- The values α = β = 0.1 are the ones reported here. I did not find in the parts I read a sweep showing how sensitive the stability result is to them.
- Whether the same collapse appears under other outcome rewards, such as exact match with the same penalty, is not tested in the parts read.

## Related

- [[answer-withholding-learning-tradeoff]] — withholding the answer as a tutoring design, where its cost was measured on a post-test; here withholding is an RL escape from zero credit, a different cause with the same surface behaviour
- [[abstention-informedness]] — a lower false-answer rate can come from refusing more often; the same confound is what a zero-credit reward rewards
- [[hard-positive-evidence-augmentation]] — the opposite incentive, where an agent is rewarded for refusing; here refusal is not rewarded, but it costs nothing
- [[moderate-adaptive-reasoning-length]] — the same paper's other collapse, which comes from long reasoning rather than from withheld answers

[^c1]: doi-10-48550-arxiv-2602-19526 — "a significant decline in the answer rate, whereas the accuracy of the answered samples remains relatively"
[^c2]: doi-10-48550-arxiv-2602-19526 — "This indicates that the dominant failure mode is not incorrect answering,"
[^c3]: doi-10-48550-arxiv-2602-19526 — "Since missing an answer receives the same zero reward as an incorrect one,"
[^c4]: doi-10-48550-arxiv-2602-19526 — "training collapse driven by answer avoidance"
[^c5]: doi-10-48550-arxiv-2602-19526 — "we set α = 0.1, β = 0.1 here."
[^c6]: doi-10-48550-arxiv-2602-19526 — "minimal action-level penalties to discourage omitting search or answer steps"
[^c7]: doi-10-48550-arxiv-2602-19526 — "These constraints stabilize training dynamics by eliminating the answer"
[^c8]: doi-10-48550-arxiv-2602-19526 — "model with action penalties not only recovers from instability, but also surpasses the EM baseline in final"
[^c9]: doi-10-48550-arxiv-2602-19526 — "carries a theoretical risk of reward hacking"
