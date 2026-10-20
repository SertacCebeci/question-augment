---
description: "Showing a known outcome or candidate answers before the model reasons makes it rationalize them; committing to a scene-derived decision first and revealing options after restores faithful reasoning."
aliases: ["DEFT", "deferred exposure", "trajectory anchoring bias", "post-hoc rationalization of a revealed answer"]
sources: ["doi-10-48550-arxiv-2608-01755", "arxiv-2512-02456"]
---
# Deferred answer exposure

Information order changes what reasoning is. If a teacher or policy sees the answer (or a menu of answers) before it reasons, it works backward from the answer. Deferring the answer until the model has committed to a decision from evidence alone turns the answer into a check on that decision, not a premise of it.

## Mechanism

In autonomous-driving chain-of-thought annotation, the teacher is often shown the logged ground-truth future trajectory. The authors call the resulting failure trajectory anchoring bias: the revealed outcome "can act as an anchor, allowing teachers to reverse inference and construct a post hoc explanation of the revealed outcome".[^c1] The rationale then fits the action while failing to name the scene evidence that supports it. In their human-scored study, GT-conditioned CoTs got a quality score of 5.02 against 6.43 for causal-planning CoTs, and severe hallucination was 50% against 29% (read from the figure text, so the pairing of numbers is my reading).[^c2] The example given is an invented mandatory-turn sign.

Hiding the answer fixes this but makes the task open-ended. So the work turns planning into a multiple-choice selection among explicit candidate trajectories. That brings a second anchor: showing the candidates first "can simply replace the GT-trajectory anchor with a candidate-set anchor".[^c3]

The remedy is a two-turn protocol. Turn 1 sees only the scene context and must trace "how scene evidence leads to driving implications" and commit to a high-level decision. Turn 2 reveals the candidates, and the model grounds its decision in one of them. The candidates are "reserved for grounding an already formed scene-derived decision rather than shaping the decision itself".[^c4] The final choice has an exact verifiable reward, so the pipeline can be trained with RL on verifiable rewards.

Measured effect of order alone, with the same candidates: training-free deferred exposure raised accuracy from 28.1% to 56.6% on Qwen3-VL-8B and from 34.0% to 65.6% on Qwen3.5-4B over a joint-exposure baseline. Under the same correctness-only reward, the deferred version beat its matched joint-exposure ablation by 15.3 and 6.7 points.[^c5] In distillation with equal data, accuracy rose from 64.0% to 82.4%.[^c6] The authors attribute the gap to information order: with candidates visible during decision formation the policy "may organize the reasoning around a favored answer".[^c7]

The same mechanism appears in a self-training loop for vision-language models, outside driving. There the baseline gives the gold answer to items it answered wrongly and keeps the rationales that then reach it. The authors' objection is that "Because the gold answer is revealed, the model may generate superficially correct rationales",[^c8] and that this "enables the model to reach correct answers without true reasoning".[^c9] Their alternative keeps only answers reached without the gold answer in view. The parallel with deferred exposure is my own; the paper does not cite it. See correctness-filtered-self-training.

## Limits

- All evidence is from driving VLMs with trajectory candidates. Transfer to text question answering or clarification dialogues is my inference and was not tested.
- The anchoring study is human-scored on a limited sample; its details are in an appendix that I did not read.
- Deferral needs an answer set that can be checked after the decision. Open-ended answers lose the exact reward.
- The two-turn format also adds the grounding step as extra supervision, and the paper reports that it improves reasoning quality on its own. The effect of order is therefore not fully separated from the effect of the second turn.
- The link to anchoring in cognitive psychology is an analogy the authors draw, not something they test.

## Related

- [[diagnostic-anchoring-in-agentic-llms]] — anchoring on a first commitment; here the anchor is an outside revealed answer, there the model's own early guess
- [[root-query-anchoring]] — another anchoring effect on later reasoning
- [[verification-over-invention]] — checking a committed answer against a target instead of generating it open-ended
- correctness-filtered-self-training — the same risk in a rationale-training loop, where the gold answer is shown to items the model got wrong

[^c1]: doi-10-48550-arxiv-2608-01755 — "allowing teachers to reverse inference and construct a post hoc explanation"
[^c2]: doi-10-48550-arxiv-2608-01755 — "aggregate results show lower causal faithfulness and preference, with more severe hallucinations."
[^c3]: doi-10-48550-arxiv-2608-01755 — "can simply replace the GT-trajectory anchor with a candidate-set anchor"
[^c4]: doi-10-48550-arxiv-2608-01755 — "reserves candidate geometry for grounding an already formed scenederived decision rather than shaping the decision itself."
[^c5]: doi-10-48550-arxiv-2608-01755 — "DEFT raises ACC from 28.1% to 56.6% on Qwen3-VL-8B and from 34.0% to 65.6%"
[^c6]: doi-10-48550-arxiv-2608-01755 — "raising MCQ accuracy from 64.0% to 82.4%"
[^c7]: doi-10-48550-arxiv-2608-01755 — "the policy may organize the reasoning around a"
[^c8]: arxiv-2512-02456 — "Because the gold answer is revealed, the model may generate superficially correct rationales"
[^c9]: arxiv-2512-02456 — "This enables the model to reach correct answers without true reasoning"
