---
description: "A smaller student is fine-tuned on reviewer-corrected reasoning chains and then reasons without the reviewer; the evidence offered for this is benchmark accuracy alone."
aliases: ["corrected-CoT fine-tuning", "internalizing corrected reasoning", "student distillation of self-corrected chains"]
sources: ["arxiv-2512-22627"]
---
# Corrected-trace distillation

The chains produced by a correction loop are kept as training targets. In the paper's design they are used to fine-tune a smaller student model, which is then the model that answers. The reviewer is needed only while the corrected chains are being made. "After fine-tuning, the student LLM is able to produce logically consistent multi-step reasoning without relying on the reviewer and is used as the final model for TSQA."[^d1] The corrections are thus moved from the reviewer into the student's parameters, which is what the paper means by "internalizing" the reasoning.[^d2]

The training is ordinary supervised learning on sequences. The student is conditioned on the question, the time series and the corrected chain, and "is trained to autoregressively predict the next token in the CoT given the preceding reasoning context."[^d3] The objective adds a chain loss and an answer loss, L = Lcot + Lans, with the answer predicted after the completed reasoning.[^d4] The paper's stated result of the process is that the student "becomes capable of independently generating consistent reasoning for TSQA."[^d5] The student is fine-tuned "using LoRA."[^d6]

Mechanically, this is distillation from a process that had information the student does not have. The reviewer saw the reference answer when it corrected the chain, so the student learns a chain that was shaped by that answer. (This reading is mine; it is the same structure as distilling a teacher with extra context into a student without it, see [[knowledge-boundary-aware-self-distillation]].)

The reported evidence is that the resulting student "achieves state-of-the-art performance" over LLM-based baselines on the two benchmarks.[^d7] Those baselines share the same backbone and include chain-of-thought without correction, so the comparison is between training regimes on the same base, not between reasoning methods at inference.

## Limits

The text reports accuracy on two benchmarks, CTQA and TMQA, and in both "the associated time series information appears in the texts."[^d8] Whether the distillation works where the input cannot be checked against the chain is not tested; the verifiability argument for the reviewer is made for time series specifically.[^d9]

The benefit of distillation is not isolated. The only direct comparison to a no-correction baseline is at one correction round, and the student is compared with baselines as a whole. Correction and distillation are confounded in the reported numbers, so the text does not show how much of the gain belongs to the student's training rather than to the corrected chains it was trained on.

The student's quality is bounded by the chains it learns from. The paper reports that when the initial chain is wrong, the correction "is unable to stop the" student "from learning erroneous CoTs."[^d10] The selection of the best corrected chain also uses the reference answer, as noted for the loop itself, so the training targets carry label information.[^d11]

The paper does not measure whether the student's chains are faithful to the time series, only whether its answers score higher. "Internalizing" is the paper's term for a claim about parameters that the benchmark accuracy does not check. Whether the student's reasoning is more consistent with the input, rather than just more often correct, is an open question in this text.

## Related

- [[earliest-error-truncation-correction]] — the loop that produces the corrected chains this note distills.
- [[knowledge-boundary-aware-self-distillation]] — a teacher with extra context distilled into a hint-free student; the same structure, applied to a search agent's trust and retrieval decisions.
- [[socraticpo]] — a teacher's corrective guidance during RL, with the reward decayed so that guidance is not a free path to reward; a contrast to distilling corrections once, offline.

[^d1]: arxiv-2512-22627 — "reasoning without relying on the reviewer and is"
[^d2]: arxiv-2512-22627 — "the student model internalizes the multi-step reasoning structure"
[^d3]: arxiv-2512-22627 — "The student model is trained to autoregressively predict the next token in the CoT given the preceding"
[^d4]: arxiv-2512-22627 — "The overall training objective of"
[^d5]: arxiv-2512-22627 — "becomes capable of independently generating consistent reasoning for TSQA."
[^d6]: arxiv-2512-22627 — "fine-tune the student LLM using LoRA"
[^d7]: arxiv-2512-22627 — "T3LLM achieves state-of-the-art performance"
[^d8]: arxiv-2512-22627 — "in which the associated time series information appears in the texts."
[^d9]: arxiv-2512-22627 — "time series data are inherently verifiable, enabling consistency checking between"
[^d10]: arxiv-2512-22627 — "the later correction process is unable to stop the"
[^d11]: arxiv-2512-22627 — "answer correctness or proximity to the golden standard answer."
