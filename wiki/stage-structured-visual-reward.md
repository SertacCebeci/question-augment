---
description: "Scoring a separate image-description tag by unique content, smoothed by tanh, makes an RL-trained VLM reason longer about the image, with uneven accuracy gains across puzzle types."
aliases: ["RSTRUCTURED", "multi-stage tag reward", "image-description tag reward", "unique-content stage reward"]
sources: ["arxiv-2601-00215", "doi-10-48550-arxiv-2604-01460"]
---
# Stage-structured visual reward

A reinforcement reward for a vision-language model can be built as a sum of terms, one per output tag, instead of one score on the final answer. In the variant studied here, the output is divided into an image description, a think block, a rethink block and an answer. Each non-answer tag earns credit for its presence and for "the amount of unique content generated within that tag."[^c1] Repetition is penalized and the counts are passed through a tanh function, "to prevent disproportionately large rewards."[^c2] The answer keeps the largest weight, since "answer correctness is assigned the highest weight in the composite to maintain factual accuracy."[^c3]

The mechanism is a shaping term that the policy can raise without a label for the image. The reward does not check whether the description is right. It pays for a description that is long, varied and placed before the reasoning, and GRPO then pushes the policy toward outputs that score well on those terms. The authors use it to test whether rewarding multi-stage structure "induces longer, more grounded reasoning trajectories without chain-of-thought supervision."[^c4]

The measured effects are these. Qwen-2.5-VL-7B trained with GRPO under this reward shows "long, structured reasoning with self-reflection and visual references," and the abstract reports "a 5.56-point gain over the base model."[^c5] Within the six variants compared, the stage-structured reward "achieves the highest average score (15.56), followed closely by" the outcome-only reward.[^c6] The behavioural change is the clearest result. Under the rewards that do not score the description, "the model produces minimal intermediate reasoning, often jumping directly to the answer with little explanation."[^c7] Under the stage-structured reward, the authors say the model "achieve[s] the intended behavior": it references and explains parts of the image before computing.[^c8]

The accuracy result is less clean. The outcome-only reward is "on par with or better than" the stage-structured one "in about half of the classes, especially" out of domain.[^c9] The authors take this as evidence that "long reasoning alone does not guarantee improved accuracy."[^c10]

## Limits

- One base model (Qwen-2.5-VL-7B) and one puzzle family (AlgoPuzzleVQA with generated training samples). The 5.56-point gain is on this family. The best model in the paper "achieves only 15.56% accuracy," so the gain is measured from a low base.[^c11]
- The reward counts unique content, not correct content. The paper's own error analysis shows trajectories that "proceed from an initial misreading of the image" and stay internally consistent.[^c12] A longer description that misreads the image earns the same credit as a correct one. The authors name the gap: a reward must "explicitly incentivize accurate visual grounding," which this variant does not do.[^c13]
- Accuracy and structure are not separated in the results. An accuracy-free reward, which scores only structure, also rises above the baseline: "the RPROCESS reward produces unexpected behavior."[^c14] So some of the gain may come from the structure term alone, and the paper does not settle how much.
- The trade-off runs against the accuracy term: "variants that achieve the largest in-domain gains tend to generalize less well, while variants with weaker accuracy signals" show more balanced out-of-domain results.[^c15] This is the reading of a few tables on one benchmark, with the authors' own hedge that it is "consistent with" overfitting.
- The helpful and harmful categories split by task type. The authors note that "encouraging more visual reasoning may distract the model from the algorithmic steps," on categories with simple images and complex algorithms.[^c16] No single reward was best everywhere: "no single reward function consistently dominates across all classes."[^c17] My inference is that a single stage weighting cannot be right for both kinds of task.
- Whether the tanh-smoothed repetition penalty stops reward hacking beyond the outputs the paper inspected is not tested. The paper does not run adversarial probes on the description tag.
- A different reward family scores a description against a reference. A video paper parses generated and reference captions into factual and temporal units and rewards their match, because "standard sentence-level rewards often prove too coarse to accurately localize specific grounding failures."[^c18] Unlike this variant, that reward can fail a description that is long but wrong; the two address different failures, which is my inference, and neither paper compares them. The audit that motivates that reward is in [[top-down-conditional-consistency-audit]].[^c19]

## Related

- [[perception-substitution-gap]] — measures how much of a model's error sits in perception; this reward tries to move the perception step, not to measure it
- [[visual-interrogation-reward]] — checks the content of a visual description by asking questions of the rendered output, where this reward only counts how much description there is
- [[counterfactual-image-grounding-audit]] — tests whether answers still depend on the image, the question this reward's gains leave open
- [[cot-hallucination-trap]] — a longer rationale is not a grounded one: fluent reasoning can detach from the image when its visual input is weak

[^c1]: arxiv-2601-00215 — "based on the amount of unique content generated within that tag"
[^c2]: arxiv-2601-00215 — "a tanh() smoothing function to prevent disproportionately large rewards"
[^c3]: arxiv-2601-00215 — "Answer correctness is assigned the highest weight in the"
[^c4]: arxiv-2601-00215 — "induces longer, more grounded reasoning"
[^c5]: arxiv-2601-00215 — "reward design induces long, structured reasoning with self-reflection and visual references"
[^c6]: arxiv-2601-00215 — "highest average score (15.56), followed closely by"
[^c7]: arxiv-2601-00215 — "the model produces minimal intermediate reasoning, often jumping directly to the answer with little explanation"
[^c8]: arxiv-2601-00215 — "achieve the intended behavior"
[^c9]: arxiv-2601-00215 — "in about half of the classes, especially"
[^c10]: arxiv-2601-00215 — "long reasoning alone does not guarantee improved accuracy"
[^c11]: arxiv-2601-00215 — "achieves only 15.56% accuracy"
[^c12]: arxiv-2601-00215 — "proceed from an initial misreading"
[^c13]: arxiv-2601-00215 — "signals that explicitly incentivize accurate visual"
[^c14]: arxiv-2601-00215 — "RPROCESS reward produces unexpected behavior"
[^c15]: arxiv-2601-00215 — "generalize less well, while variants with weaker accuracy signals"
[^c16]: arxiv-2601-00215 — "encouraging more visual reasoning may distract the"
[^c17]: arxiv-2601-00215 — "No single reward function consistently"
[^c18]: doi-10-48550-arxiv-2604-01460 — "standard sentence-level rewards often prove too coarse to accurately localize specific grounding failures"
[^c19]: doi-10-48550-arxiv-2604-01460 — "we parse generated and reference captions into structured factual and temporal units"
