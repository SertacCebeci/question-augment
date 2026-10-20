---
description: "In a maze study, a visual chain of thought needed about half the RL steps of a language chain yet reached no higher final accuracy, so training speed and performance ceiling come apart."
aliases: ["convergence versus ceiling", "speed-ceiling dissociation", "accelerates but does not lift the ceiling", "RL convergence speed versus asymptote"]
sources: ["arxiv-2511-22586"]
---
# Convergence-ceiling dissociation

After a supervised warm-up, reinforcement learning can be judged on two quantities that are easy to run together: how many steps a policy needs to reach high training accuracy, and where its accuracy levels off. A controlled maze study separates them. Visual chain of thought "yields the fastest RL convergence, requiring roughly half the training steps of language CoT".[^c1] Its final accuracy did not follow: visual CoT "does not surpass grounding CoT or language CoT in final accuracy".[^c2] The authors summarize that it "mainly accelerates optimization rather than expanding the model’s ultimate reasoning capacity".[^c3] In their abstract, the general form is that "visual and longer CoT mainly accelerate convergence but do not lift the final performance ceiling".[^c4]

The authors' explanation is that once RL has settled on an internal policy, extra visual steps have little left to add: "additional visual manipulation offers diminishing returns on" the asymptote.[^c5] In the same paper, the reason the short traces suffice is placed in grounding: "Once grounding is sufficiently reinforced, the model can perform effective reasoning" with brief traces.[^c6] On this reading the ceiling is set by the grounding the cold start instilled, not by how much explanation the trace carries.

Speed does not simply follow trace length. The shortest variant, the least-grounded path, converged faster than the grounding chain and "even surpass[ed] the efficiency of visual CoT".[^c7] So what accelerates the policy seems to be what the trace grounds, and the ceiling seems not to move with either. For a question-asker this distinction matters: a training run can look better because it reaches a plateau sooner, while the plateau itself is where the method's capacity lies. My inference is that the two should be reported separately whenever a trace format is compared.

## Limits

- The ceiling comparison sits near saturation. The SFT-initialized models "reach 100% accuracy on the training mazes".[^c8] Where every format reaches the same top value, "no higher ceiling" is weak evidence. The claim has more force on the held-out sizes than on the training set, and that comparison is only partly shown in the part read.
- The run length is finite. The authors "train for up to 1000 RL steps"[^c9] to address the question of where the ceiling lies. A plateau inside that window does not show the ceiling is fixed; longer runs were not tested in the passage read.
- The speed claim rests on one reported ratio ("roughly half") read from training curves. The passage read gives no interval or per-seed spread for it.
- One base model and one RL algorithm: the training is "Policy Optimization (GRPO) [32] to update the policy model".[^c10] Whether the plateau pattern holds under other RL objectives is not tested here.
- The mechanism is a hypothesis: "A plausible explanation is that visual CoT offers more" structured, spatially grounded supervision.[^c11] It is not measured.
- The result is about training a vision-language model on maze traces. Its transfer to a human asker or a text-only answerer is my inference, not something the study measures.

## Related

- [[least-grounded-trace-supervision]] — the same study's cross-size generalization result; that note carries the claim that the least-grounded format generalizes best, while this one carries the speed and ceiling claims
- [[thinking-stagnation]] — RL on general QA raises reward mostly through answer tokens while the thinking trace barely improves, another case where RL gains do not come from the trace
- [[initialization-bounded-exploration]] — cold-start SFT sets how deep the policy starts and RL refines rather than escapes that prior; a candidate reason a plateau appears early (my inference)
- [[rlvr-entropy-collapse]] — group-relative RL narrows the spread of sampled responses; a candidate mechanism for an early asymptote (my inference)

[^c1]: arxiv-2511-22586 — "roughly half the training steps of language CoT"
[^c2]: arxiv-2511-22586 — "does not surpass grounding CoT or language CoT in final accuracy"
[^c3]: arxiv-2511-22586 — "accelerates optimization rather than expanding the model’s ultimate reasoning capacity"
[^c4]: arxiv-2511-22586 — "visual and longer CoT mainly accelerate convergence but do not lift the final performance ceiling"
[^c5]: arxiv-2511-22586 — "additional visual manipulation offers diminishing returns on"
[^c6]: arxiv-2511-22586 — "Once grounding is sufficiently reinforced, the model can perform effective reasoning"
[^c7]: arxiv-2511-22586 — "even surpassing the efficiency of visual CoT"
[^c8]: arxiv-2511-22586 — "reach 100% accuracy on the training mazes"
[^c9]: arxiv-2511-22586 — "we train for up to 1000 RL steps"
[^c10]: arxiv-2511-22586 — "Policy Optimization (GRPO) [32] to update the policy model"
[^c11]: arxiv-2511-22586 — "A plausible explanation is that visual CoT offers more"
