---
description: "Having a multimodal model commit to its intent and slot labels before writing the rationale raised label accuracy on a visual SLU benchmark; reasoning generated first was read as hurting them."
aliases: ["predict-then-explain order", "labels-first rationale", "LR-Instruct ordering", "reasoning-after-label template"]
sources: ["arxiv-2511-19005"]
---
# Label-before-rationale order

A model that writes its reasoning before its answer makes the answer a function of that reasoning. The VRSLU paper treats this as a live risk for label prediction. Its reasoning-first baseline, Qwen2.5-VL-7B, "performs worse than its counterpart without reasoning (w/o R)", and the authors read this as "reasoning generation may hinder model performance".[^l1] The proposed template reverses the order. It "first prompts the model to predict labels before generating the reasoning process".[^l2] The stated mechanism is that "proposed LR-Instruct mitigates this issue by first predicting" the labels and only then generates reasoning, which the authors say "enhances the model's ability to discriminate between intent and slot categories". The discrimination claim is supported in the paper by a per-category figure, not by a separate test.[^l3]

The order is the only thing LR-Instruct changes in the answer format. The reasoning is still produced, in the same output, after the labels. The paper's evidence that the order matters is comparative. Across several multimodal models, "LR-Instruct consistently improves intent Acc, slot F1, and overall Acc performance", and it also raises the reasoning metrics (BLEU-1, BLEU-4 and cosine similarity).[^l4] Both the template and the baselines are trained the same way: "both the proposed LR-Instruct and all baselines are fine-tuned using LoRA".[^l5]

The paper does not read reasoning as useless. Removing the reasoning target from LR-Instruct lowers accuracy, and the authors conclude that "requiring reasoning helps the model better understand the utterance".[^l6] So the claim is not that reasoning hurts. It is that the position of the reasoning relative to the label decides whether reasoning helps or hurts the label.

## Limits

- One dataset. VRSLU has GPT-4o-drafted reasoning, refined by annotators. The paper also shows that the uncorrected reasoning lowers accuracy, and reads this as showing that GPT-4o's output "still benefits from human refinement".[^l7] The order effect is therefore not separated from the quality of the reasoning text.
- The template is a training format. Every model in the comparison is LoRA fine-tuned, so the text does not show that a label-first instruction in a frozen model's prompt gives the same gain.
- The claim that reasoning-first hurts rests on comparing a model with reasoning to the same model without it, across settings in the paper's tables. It is not a controlled swap of order on a single model with the same training.
- Nothing in the text tests what happens when the label is wrong. Label-first means the reasoning cannot correct the label; whether it then rationalizes the error, as the reasoning-first ordering might, is not measured.
- The domain is spoken-language intent and slot labels. Transfer to open-ended answers, where a label cannot be fixed before the reasoning, is my inference and was not tested.

## Related

- [[deferred-answer-exposure]] — the same ordering problem from the other side: there a shown answer makes the reasoning rationalize it; here the reasoning, placed before the label, may steer the label.
- [[pre-committed-answer-before-cot]] — the answer is sometimes fixed before the chain is written. Label-first makes that commitment explicit and places it on purpose.
- [[perception-first-rationale-template]] — orders a rationale differently: describe the input first, then reason, then conclude. Both are rationale templates whose value depends on what comes first.

[^l1]: arxiv-2511-19005 — "performs worse than its counterpart without reasoning (w/o R)"
[^l2]: arxiv-2511-19005 — "a method that first prompts the model to predict labels before generating the reasoning process"
[^l3]: arxiv-2511-19005 — "proposed LR-Instruct mitigates this issue by first predicting"
[^l4]: arxiv-2511-19005 — "LR-Instruct consistently improves intent Acc, slot F1, and"
[^l5]: arxiv-2511-19005 — "both the proposed LR-Instruct and all baselines are fine-tuned using LoRA"
[^l6]: arxiv-2511-19005 — "requiring reasoning helps the model better understand the utterance"
[^l7]: arxiv-2511-19005 — "still benefits from human refinement"
