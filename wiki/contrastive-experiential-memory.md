---
description: "Textual experience is distilled by an LLM contrasting high-reward and low-reward reasoning trajectories, then placed in the training prompt as guidelines for tool use."
aliases: ["contrastive experience reasoning", "textual experiential memory", "experience bank from good and bad trajectories"]
sources: ["arxiv-2512-06653"]
---
# Contrastive experiential memory

Reinforcement learning for a search-using model produces many reasoning trajectories per query, each with a scalar reward. Contrastive experiential memory turns those rewards into text. The trajectories are split by reward: "where good trajectories achieve the most idealized outcome, i.e.," a reward of 1, and bad ones fall below a threshold.[^c2] Each trajectory is first annotated: "we first augment each trajectory with an explicit explanation of its" performance, together with its F1 score and its reward.[^c1] The annotated summaries of the good group and of the bad group are then compared by an LLM, and the comparison is written out as text. The paper says "The generated Experience takes the form of natural language" guidelines that describe effective reasoning patterns.[^c3] The mechanism's central step is that it "automatically transforms good implicit reasoning experiences into" explicit, interpretable text.[^c4]

The memory is not retrieved per query. It is one bank, refreshed as training goes on, and the paper says it is "maintaining a dynamic experiential memory bank."[^c5] In each training iteration, the paper states that "all experience from the experiential memory bank is integrated into the" model's input prompt.[^c6] That prompt also carries the task instructions, one randomly sampled high-reward trajectory as a few-shot example, and the query. The few-shot part is a separate component in the paper, so the memory proper is the textual guidance alone.

The guidelines change over training. In the paper's case study, early experiences are format rules, later ones are search strategies, and finally "they pivot toward optimizing model efficiency."[^c7] The evidence for this is a handful of excerpts, not a measurement of guideline quality.

What the memory does is shown by its ablation. The authors write that "Experiential Memory is the most critical component" of their framework.[^c8] Removing it lowers F1 "by 7.2% and LMJ score decreasing by 5.9%."[^c9] Tool calls fall to 1.18 in that variant, and the paper reads this as the model becoming "the model turns overly conservative and neglects to retrieve essential information as needed."[^c10] So in this paper the memory does not simply cut searching. It helps the policy search when a question needs it, and the efficiency gain is a separate claim carried by the reward.

## What transfers

The transferable part is the unit of learning: a contrast between trajectories of different outcome, rendered as a rule and then conditioned on in the prompt. The rule is drawn from many instances, not from one. That distinguishes it from [[experience-repository]], which stores past high-reward trajectories and prepends the most relevant ones to the context; a retrieved trajectory is one instance, while a contrast is a generalization over many. It also differs from [[judge-scored-reflection-memory]], which keeps the best judged reflection on one attempt. Here the summary is built from the whole batch of good and bad runs.

What does not obviously transfer is the writer. The paper's memory is composed by a language model and read back by the same policy. The text I read does not name the model that writes the Experience beyond the symbol "LLM", and it gives no prompt for that step. Whether a different writer, a different reward, or a retrieval-based bank would produce the same effect is not tested in the parts I read.

## Limits

- The good and bad split is made by the reward itself. The accuracy term is F1 against gold answers, so the split is only as good as that reward. A miscalibrated reward is written into the guidelines. Nothing in the parts read checks the guidelines against an independent measure of trajectory quality.
- The ablation is on one dataset and one base model: "HotpotQA dataset using Qwen2.5-7B-Instruct as the base model."[^c11] The four benchmarks in the abstract are not separated by component in the ablation.
- The authors themselves note that "LightSearcher is currently suited to controlled reasoning scenarios and demands additional computational" resources during RL training.[^c12] They also say the method is "validated on multi-hop QA"[^c13] and extension to other domains is future work.
- The memory is described as used during training. The paper has a section on inference with the memory, which I did not read in full, so no claim here covers whether a trained policy still needs the bank at test time.
- The phrase "experiential" is the paper's name for this mechanism. Its relation to other memory-of-experience methods is stated only by the paper's own related-work survey, which I did not check against the cited sources.

## Related

- [[experience-repository]] — stores past high-reward trajectories and retrieves them per query; this note stores no raw trajectory and writes one contrast into the prompt.
- [[judge-scored-reflection-memory]] — keeps the best judged reflection from a single attempt; this note aggregates many trajectories by their difference.
- [[correctness-gated-redundancy-penalty]] — the reward half of the same paper, which shapes the tool calls this memory is meant to guide.

[^c1]: arxiv-2512-06653 — "we first augment each trajectory with an explicit explanation of its"
[^c2]: arxiv-2512-06653 — "where good trajectories achieve the most idealized outcome, i.e.,"
[^c3]: arxiv-2512-06653 — "The generated Experience takes the form of natural language"
[^c4]: arxiv-2512-06653 — "it automatically transforms good implicit reasoning experiences into"
[^c5]: arxiv-2512-06653 — "maintaining a dynamic experiential memory bank"
[^c6]: arxiv-2512-06653 — "all experience from the experiential memory bank is integrated into the"
[^c7]: arxiv-2512-06653 — "they pivot toward optimizing model efficiency"
[^c8]: arxiv-2512-06653 — "Experiential Memory is the most critical component"
[^c9]: arxiv-2512-06653 — "by 7.2% and LMJ score decreasing by 5.9%"
[^c10]: arxiv-2512-06653 — "the model turns overly conservative and neglects to retrieve essential information as needed"
[^c11]: arxiv-2512-06653 — "HotpotQA dataset using Qwen2.5-7B-Instruct as the base model"
[^c12]: arxiv-2512-06653 — "LightSearcher is currently suited to controlled reasoning scenarios and demands additional computational"
[^c13]: arxiv-2512-06653 — "while validated on multi-hop QA"
