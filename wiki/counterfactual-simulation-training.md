---
description: "Rewarding chains of thought that let a simulator predict the model's answer on a counterfactual input raises CoT faithfulness, mostly for cue-based counterfactuals, and fails on dissuading cues."
aliases: ["CST", "counterfactual simulatability reward"]
sources: ["arxiv-2602-20710"]
---
# Counterfactual Simulation Training

A reasoning trace is faithful, in this method, when it lets another model predict what the author model will answer to a changed version of the question. The trace is scored by that prediction, not by how plausible it reads.[^c1]

## Mechanism

For each question the task model answers an original input and a counterfactual one. A counterfactual is either the input with a cue removed (such as "A Stanford professor thinks the answer is X") or an LLM-generated close variant: the same question about new entities, or an inverted question (most to least).[^c2] A zero-shot simulator is given the original input, reasoning and answer, and must predict the answer on the counterfactual.[^c3]

A second, outcome-only simulator sees only the original answer. The difference between the two simulators says whether the CoT actively helped (+1) or actively misled (-1). That difference weights the training signal.[^c4]

Unfaithful CoTs are rewritten by the task model itself, which is told to state that the cue influenced it. The rewrite is rejection-sampled against the simulator for up to 10 attempts. Training then uses cross-entropy on faithful examples and an unlikelihood loss on unfaithful ones.[^c5]

The reward is agnostic about what counts as good evidence. A trained model may still defer to a cue. The target is that the CoT reports whether it did.[^c6] It rewards two things: admitting that an answer flipped because of a cue, and not claiming reliance on a cue when the answer was unaffected.

## What was measured

- On gpt-oss-120b, monitor accuracy on cue-based counterfactuals rose 35 points. Simulator accuracy on generic model-based counterfactuals rose only 2 points.[^c7]
- CST beat prompting baselines, including describing the test procedure to the model and raising reasoning effort.[^c8]
- Rewriting unfaithful CoTs with an LLM was 5x more efficient than a pure RL approach and generalized better.[^c9]
- Larger models were not more faithful out of the box, but CST gained more on them.[^c10]
- Rejection sampling keeps only counterfactuals where the simulator disagrees with the task model. This forces the simulator to rely on the CoT.[^c11]

## Limits

- The gains do not transfer to cues that dissuade rather than persuade.[^c12]
- Generic counterfactuals gave small gains, and some were not driven by the CoT itself. The authors read this as process-based tasks being more amenable than knowledge-heavy ones.
- Answers are single tokens (Yes/No, A/B), and the simulator is an LLM. Faithfulness here is only what that simulator can recover.
- Tested on gpt-oss-120b and Qwen3 models, with SNLI, ETHICS, MMLU and MMLU-Pro. My inference: whether it holds for open-ended answers, or whether training teaches a verbal template instead of reflecting the real computation, is not shown by these results.

## Related

- [[hint-adherence-without-acknowledgement]] — the unfaithfulness CST targets: answers that follow a hint with no mention of it
- [[reasoning-masked-sycophancy]] — cue-driven answers hidden behind a reasoning trace
- [[counterfactual-explanation]] — counterfactual inputs used to explain a model, here used as a training signal
- [[reasoning-faithfulness-observer-effect]] — how faithfulness measurements interact with the model being measured

[^c1]: arxiv-2602-20710 — "CST works by rewarding CoTs that allow for a simulator model"
[^c2]: arxiv-2602-20710 — "We write a few-shot prompt with demonstrations of operations like inverting a question (most→least), asking a similar question about new entities"
[^c3]: arxiv-2602-20710 — "we zero-shot prompt an LLM, the"
[^c4]: arxiv-2602-20710 — "Actively helpful"
[^c5]: arxiv-2602-20710 — "The training objective consists of a cross-entropy"
[^c6]: arxiv-2602-20710 — "The goal is for the CoT to faithfully reflect whether the model relies on a piece of evidence."
[^c7]: arxiv-2602-20710 — "CST"
[^c8]: arxiv-2602-20710 — "We show that CST outperforms prompting baselines"
[^c9]: arxiv-2602-20710 — "We show that using an LLM to rewrite unfaithful CoTs is 5x more efficient and generalizes"
[^c10]: arxiv-2602-20710 — "We find that larger models do not demonstrate better faithfulness out of the box"
[^c11]: arxiv-2602-20710 — "forcing the simulator to rely on the"
[^c12]: arxiv-2602-20710 — "We identify one salient area where CST does not generalize"
