---
description: "A brief rationale before the answer is a mode video models already have; it cuts decoding cost, but trails direct answering and breaks under token compression."
aliases: ["concise reason decoding", "compact rationale before answer", "brief reasoning mode"]
sources: ["arxiv-2512-09616"]
---
# Concise reasoning mode

A multimodal model that answers a question can use one of three decoding modes. A **direct answer** emits only the final answer. A **chain-of-thought** (CoT) trace emits a long run of intermediate steps first. A **concise reasoning** response lies between them: it is a "reasoning response rather than a full CoT trace",[^c1] a short rationale before the answer. Its length is itself a training variable, as in [[reasoning-length-training-collapse]], but here the question is cost against accuracy at inference.

The reason the mode matters is where the cost sits. A model call has two parts, prefilling the input and decoding the output, and the decoding part "scales with the number of output tokens for reasoning".[^c2] A long chain therefore loads the expensive side, and each generated token attends to the whole input. In the authors' measurement the CoT model "spends around ten times" the inference runtime of the other modes.[^c3]

The mode is not something the authors add. They report that "Concise reasoning, learned from pretraining, can largely reduce decoding cost".[^c4] A pre-trained model already produces a short rationale, and no CoT annotation is needed to get it. Accuracy is the catch: before further training, "there is a clear performance gap between concise" reasoning and direct answering.[^c5] The long trace does not reliably pay for itself either. In their benchmark, adding CoT "yields only modest" gains over direct answering,[^c6] so on this evidence the short mode gives up accuracy for speed and the long mode gives up speed for little accuracy.

## Under token compression

The mode is most fragile when the input is reduced. Token compression lowers the number of visual tokens prefilled, and the authors find that it "can reduce prefilling overhead, but fails to well preserve the performance of concise reasoning".[^c7] In their Table 2 the caption reads "Concise reason is largely impacted by token compression".[^c8] The average column, as I read it, falls about -1.9 for direct answer, -2.4 for CoT and -4.3 for concise reasoning. The authors conjecture that the model "is not optimized to such decoding mode and thus" is more vulnerable to an input intervention it did not see in training.[^c9] The conjecture is theirs; the table only shows the gap.

Training changes the picture. Their method runs RL directly on the pre-trained model, with no CoT annotation and no supervised stage, and they report that "Direct GRPO training improves the compatibility of concise reasoning with token compression".[^c10] The drop under compression shrinks after that training: "concise reasoning can be further integrated with token compression after GRPO finetuning",[^c11] with the average drop going from -4.3 to -2.2 by the paper's numbers. Their account is that GRPO "strengthens" the concise behaviour, so the model is "more capable of operating effectively in this decoding mode".[^c12] The compression also frees input budget: the comparison "maintain[s] the same level of computation budget for prefilling",[^c13] so the final model reads more frames at the same prefilling cost. On that setup, the authors report that "our model achieves the best results on" the benchmarks they test.[^c14]

## Limits

- The evidence is empirical, and the authors say so: "Our work is grounded in empirical evidence rather than theoretical guarantees".[^c15] The conclusions are bounded by "the scope of current video benchmarks".[^c16]
- One model family is tested. The CoT model is "initialized from the pre-trained Qwen2.5-VL model",[^c17] and the concise and direct modes are read from that same base. Nothing here shows the mode on text-only reasoning, or on tasks whose answer needs a long derivation.
- The paper does not claim the new method is superior in general: "we do not claim algorithmic superiority over prior methods".[^c18]
- The filler claim, that the "pondering" phrases of CoT output "contribute little to reasoning",[^c19] is read from output text and is not tested by ablation. Whether those tokens are dead weight or carry some of the computation is not settled here.
- The compression fragility is shown for one training-free compression method. Whether other compression schemes break the mode in the same way is not measured.

## Related

- [[moderate-adaptive-reasoning-length]] — capping reasoning length helped on theory-of-mind tasks; a shorter-trace result in another setting
- [[distractor-similarity-reasoning-inflation]] — more reasoning tokens under noisy context did not raise accuracy, so extra length can cost without gain
- [[cot-token-complexity-lower-bound]] — a bound on how many chain tokens some tasks need; the video paper gives empirical comparisons, not a bound
- [[complexity-tiered-strategy-routing]] — a router picks a reasoning strategy per query by difficulty; the video paper proposes one mode for all queries and no routing

[^c1]: arxiv-2512-09616 — "reasoning response rather than a full CoT trace"
[^c2]: arxiv-2512-09616 — "scales with the number of output tokens for reasoning"
[^c3]: arxiv-2512-09616 — "CoT model spends around ten times"
[^c4]: arxiv-2512-09616 — "Concise reasoning, learned from pretraining, can largely reduce decoding cost"
[^c5]: arxiv-2512-09616 — "there is a clear performance gap between concise"
[^c6]: arxiv-2512-09616 — "adding CoT yields only modest"
[^c7]: arxiv-2512-09616 — "can reduce prefilling overhead, but fails to well preserve the performance of concise reasoning"
[^c8]: arxiv-2512-09616 — "Concise reason is largely impacted by token compression"
[^c9]: arxiv-2512-09616 — "the model is not optimized to such decoding mode and thus"
[^c10]: arxiv-2512-09616 — "Direct GRPO training improves the compatibility of concise reasoning with token compression"
[^c11]: arxiv-2512-09616 — "concise reasoning can be further integrated with token compression after GRPO finetuning"
[^c12]: arxiv-2512-09616 — "more capable of operating effectively in this decoding mode"
[^c13]: arxiv-2512-09616 — "we maintain the same level of computation budget for prefilling"
[^c14]: arxiv-2512-09616 — "our model achieves the best results on"
[^c15]: arxiv-2512-09616 — "Our work is grounded in empirical evidence rather than theoretical guarantees"
[^c16]: arxiv-2512-09616 — "the scope of current video benchmarks"
[^c17]: arxiv-2512-09616 — "It is initialized by the pre-trained Qwen2.5-VL model"
[^c18]: arxiv-2512-09616 — "we do not claim algorithmic superiority over prior methods"
[^c19]: arxiv-2512-09616 — "that contribute little to reasoning"
