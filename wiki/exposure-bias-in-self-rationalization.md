---
description: "A model trained to explain gold labels is later asked to explain its own answers; conditioning the explanation on predicted labels under a schedule narrows that train-test gap."
aliases: ["self-rationalization exposure bias", "task-level scheduled sampling", "label-conditioned rationale exposure bias"]
sources: ["arxiv-2512-20074", "doi-10-48550-arxiv-2201-06206"]
---
# Exposure bias in self-rationalization

A model that explains its own answer is trained on one context and used on another. In training, the explanation is generated from the gold answer, so the model learns to justify the right label. At use, it must justify the label it has just produced, which may be wrong. The paper calls this exposure bias in self-rationalization: the explanation is never trained on the conditioning it actually receives.[^c1]

The fix moves scheduled sampling from tokens to the task. Ordinary scheduled sampling replaces reference tokens inside a sequence with the model's own. Here the conditioning context itself is switched: "we apply it at the task level by switching the conditioning context".[^c2] Reason2Decide runs one T5 model in two stages. It first predicts a label, then generates a rationale given a label that is the gold label with probability 1 − π_t and the model's own greedy prediction with probability π_t. The schedule is zero during warm-up, rises linearly over a transition phase, and is then held at 0.9.[^c3] The authors state the ceiling is deliberate: it stops the model "from fully relying on self-generated" labels, so that errors are not amplified.[^c4]

At inference the order is fixed: the model predicts the label greedily, then generates the rationale "conditioned on that prediction".[^c5] The schedule therefore ends where deployment begins, which is the stated point of the mechanism.

What the mechanism did in the authors' ablation is narrower than the framing. They say its "primary purpose" is rationale alignment through exposure-bias mitigation.[^c6] The prediction gain is the secondary result: on Clinical Triage, removing it lowered F1 from 59.92 to 57.28, and the text says it "improves prediction on complex, multi-class datasets".[^c7] BERT and BLEU scores were equal or higher with the mechanism on.

Transfer. The concept carries beyond T5 rationales to any setting where an answer is committed and then justified. The justification is trained on the answer the model would give, not only on the correct one. What does not carry over is the specific schedule. Its phase fractions were chosen by search over "a few sets of predefined tuples".[^c8]

The same gap appears in knowledge-graph reasoning, where a Transformer writes a reasoning path token by token. Training feeds the ground-truth history, and "during inference the history is generated" by the model itself.[^c13] The remedy there grows the training set rather than switching the conditioning context. The authors "propose iterative training that iteratively aggregates" the paths the model predicts, "adapting the model to the distribution of history tokens it induces".[^c14] They take the name from language modeling, where it is "a common challenge faced in autoregressive models".[^c15] The measured effect is on link prediction, not on rationales. Iterative training and rule-enhanced learning are both reported as "beneficial to the overall performance of SQUIRE", and the two "play a more important role on FB15K237 than on NELL995".[^c16][^c17] The transfer is of the remedy's shape, that the model's own outputs enter training. The paths themselves are a different object, see [[generated-path-completion]].

## Limits

- The ablation is reported for one base model. The table caption reads "Ablation results on Clinical Triage and BioASQ (Base model)".[^c9] Whether the gain holds for the small or large variants is not shown in the text I read.
- Each ablation row is a single number. I saw no spread across seeds, so a 2-point F1 gap is not shown to exceed run-to-run noise (my reading of the table).
- The hyperparameters were chosen heuristically, and the authors say a finer search "may lead to" further gains.[^c10]
- "Rationale fidelity" here means agreement with reference rationales by BERTScore, BLEU and an LLM judge.[^c11] The paper says "Finally, our rationale evaluation lacks" human oversight.[^c12] None of these measures whether the explanation reflects the computation that produced the label. That is a separate question, and the mechanism does not address it.
- The schedule uses greedy decoding for the training-time predictions. Whether the effect holds under sampled predictions is not tested (my inference).
- Exposure bias here is a training-time mismatch. The concept says nothing about an answerer who never trained on its own outputs, such as one prompted at inference only (my inference).

## Related

- [[answer-reasoning-consistency-reward]] — the RL-side version of the same worry, that a final answer may not follow from its trace; there the fix is a reward, here it is the conditioning used in training
- [[trace-conditioned-answer-consistency]] — re-eliciting an answer from its own trace at test time, a cousin of conditioning the explanation on the model's own prediction
- [[hint-adherence-without-acknowledgement]] — an explanation can present an answer as derived when another cue drove it; the mechanism above does not measure that gap
- [[generated-path-completion]] — the same train-on-ground-truth, generate-at-inference gap in a graph-path model, where the remedy is training on the model's own predicted paths

[^c1]: arxiv-2512-20074 — "models are trained to generate explanations conditioned on gold labels but at inference time must"
[^c2]: arxiv-2512-20074 — "we apply it at the task level by switching the conditioning context"
[^c3]: arxiv-2512-20074 — "where πt follows a linear schedule"
[^c4]: arxiv-2512-20074 — "The ceiling of 0.9 was a design choice to prevent the model from fully relying on self-generated"
[^c5]: arxiv-2512-20074 — "and then generate the rationale, via greedy decoding, conditioned on that prediction"
[^c6]: arxiv-2512-20074 — "The primary purpose of scheduled sampling is rationale alignment via exposure-bias mitigation"
[^c7]: arxiv-2512-20074 — "it improves prediction on complex, multi-class datasets"
[^c8]: arxiv-2512-20074 — "The hyperparameters (0.05 and 0.6) were determined through"
[^c9]: arxiv-2512-20074 — "Ablation results on Clinical Triage and"
[^c10]: arxiv-2512-20074 — "Our approach involved several hyperparameters that were chosen heuristically"
[^c11]: arxiv-2512-20074 — "rationale fidelity (BERTScore, BLEU, LLM-as-a-Judge)"
[^c12]: arxiv-2512-20074 — "Finally, our rationale evaluation lacks"
[^c13]: doi-10-48550-arxiv-2201-06206 — "during inference the history is generated"
[^c14]: doi-10-48550-arxiv-2201-06206 — "we propose iterative training that iteratively aggregates"
[^c15]: doi-10-48550-arxiv-2201-06206 — "a common challenge faced in autoregressive models"
[^c16]: doi-10-48550-arxiv-2201-06206 — "beneficial to the overall performance of SQUIRE"
[^c17]: doi-10-48550-arxiv-2201-06206 — "a more important role on FB15K237 than on NELL995"
