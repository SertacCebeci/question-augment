---
description: "A tool-call reward judged from the tool's output and the question alone, asking whether the returned crop or result is evidence for the question, so the reward never reads the model's reasoning text."
aliases: ["evidence-checking tool reward", "output-only tool judge", "tool reward as evidence checking"]
sources: ["arxiv-2511-19661"]
---
# Tool-output evidence reward

A reward for a tool step can be computed from three things: the model's reasoning text, the model's own call or code, and what the tool returned. The CodeV paper uses only the last, together with the question. Its judge receives a tuple (Q, o_t, metadata): the question, the sandbox output (a cropped image or its description, coordinates, simple statistics), and nothing the policy wrote. The authors put the scope of this directly: "TAPO only inspects non-model-generated context".[^t1] The judge is asked "whether the current tool result provides any useful evidence for answering Q".[^t2]

The rubric is permissive on purpose. It rewards any crop that clearly contains a relevant object or region, and it does not require the crop to contain every relevant object. For multi-target questions, "one correct region is rewarded rather than penalized".[^t3] The reward is a step-level signal on each tool call, so an agent that spends a call on a useful crop is credited for that call and not only for the final answer. The paper's motivation is that outcome-only rewards are sparse: "early-stage rollouts on difficult tasks frequently receive zero rewards, which discourages the faithful use of tools with partially correct attempts".[^t4]

The reward is combined with answer correctness as R = λ_acc·r_acc + λ_tool·r_tool, where r_tool is a mean over the tool-call steps.[^t5] Advantages are then normalized within the rollout group, as in GRPO. The judge model is Qwen2.5-VL-32B.[^t6]

The choice to judge the output and not the reasoning is argued, not measured in the text read. The authors say that "directly judging the model's code and thoughts is both brittle and expensive" in early experiments, and that "the judge never sees the chain-of-thought or code and only answers" whether the evidence helps.[^t7] The stated alternative, IoU against ground-truth boxes, is rejected because "they require dense annotations and do not generalize to tasks without bounding boxes".[^t8] The authors also claim the design is "less susceptible to reward hacking".[^t9]

## Limits

- The text read reports the rubric and the judge but no ablation of this reward. The judge is said to have an ablation with GPT-5-nano, "with results shown in 5.4", which I did not read.[^t6]
- The judge sees only the question and the output. A crop that holds the right object while the reasoning uses it for a wrong step is rewarded by this signal. The check cannot tell whether the answer depends on the crop. This is my inference, not a tested failure.
- "Less susceptible to reward hacking" is the authors' claim. The paper's own motivation is that tool-use rewards invite hacking, and an output-only judge removes one channel for it. Whether it removes the hack or moves it into the judge is not tested here.
- The domain is visual search with crops. The authors write that the judge "can be reused for other task families with minimal changes",[^t10] which is an assertion; no second domain is reported in the text read.
- The training reward is judged by a model, and the paper's evaluation uses a different judge (GPT-4o) for the faithfulness rate. The two judges are not compared here.

## Related

- [[crop-label-consistency-reward]] — another crop-level process reward; it scores the crop against the model's own label, where this one scores the crop against the question
- [[grounding-answer-dual-axis-audit]] — the same evidence test used as a measurement and crossed with answer correctness, not as a training reward
- [[benefit-scaled-tool-reward]] — rewards a tool call by the accuracy gain it brings, not by whether its output holds evidence
- [[evidence-grounded-step-reward]] — step-level reward on reasoning steps by a generative judge; this note's judge reads tool outputs instead
- [[visual-evidence-scoring]] — grades the crops a reasoner cites against ground-truth boxes with a learned selector

[^t1]: arxiv-2511-19661 — "TAPO only inspects non-model-generated context"
[^t2]: arxiv-2511-19661 — "tool result provides any useful evidence for answering Q"
[^t3]: arxiv-2511-19661 — "one correct region is rewarded rather than penalized"
[^t4]: arxiv-2511-19661 — "which discourages the faithful use of tools"
[^t5]: arxiv-2511-19661 — "where racc measures answer quality and rtool evaluates tool"
[^t6]: arxiv-2511-19661 — "with ablation on GPT-5-nano with results shown in 5.4"
[^t7]: arxiv-2511-19661 — "is both brittle and expensive"
[^t8]: arxiv-2511-19661 — "dense annotations and do not generalize to tasks without"
[^t9]: arxiv-2511-19661 — "less susceptible to reward hacking"
[^t10]: arxiv-2511-19661 — "task families with minimal changes"
