---
description: "A turn-level reward counts how many hidden rubric items a clarification question targets and penalizes early answers; with a judge as verifier it lifted a 7B model's multi-turn accuracy and coverage."
aliases: ["rubric-guided RLVR", "AskBench checkpoint reward", "checkpoint-targeted questioning reward"]
sources: ["arxiv-2602-11199"]
---
# Rubric-targeted clarification reward

AskBench turns a QA pair into a degraded query (AskMind: key factors removed or blurred) paired with an itemized rubric of what is missing; the items are "explicit checkpoints that must be resolved before delivering a final answer".[^c1] A frozen judge model reads the dialogue plus the hidden original query and plays the user, revealing only what was explicitly asked for.[^c2] The same loop supplies the training signal.

## The reward

At each non-final turn the judge returns whether the latest message is a final answer (a_t) and which of the m rubric items it explicitly asked about (c_t of m). The intermediate reward is: answering early, -2.0; asking with c_t = 0, -0.8; targeting some but not all items, 0.8; targeting all, 1.0.[^c3] The terminal reward is +1.0 for a correct final answer, -1.0 for a wrong one and -2.0 for still asking on the last turn; the weights are hand-set and shared across tasks.[^c4] Optimization is GRPO with the judge as verifier; the authors argue that with checkpoints and ground-truth answers but no gold clarification trajectory, a judge is the way to couple coverage with correctness.[^c5]

The point of the structure is that the reward is defined over what the question contains (which missing item it names), not over whether the dialogue ended well, so it separates "asked something" from "asked the right thing".

## What was measured

On AskMind, a Qwen2.5-7B policy trained this way rose in accuracy from 0.332 to 0.615 and coverage from 0.214 to 0.679 over the base model, with strong general models (Gemini, GPT) showing coverage of only 0.124 and 0.118 because they answer without resolving the checkpoints.[^c6] A prompting baseline (FATA, a slate of supplementary questions) raised coverage to 0.503 but trailed in accuracy; the authors conclude "asking per se is insufficient" without a learning signal aligned to the task's checkpoints.[^c7] A supervised baseline improved asking metrics but hurt out-of-domain performance, while RLVR kept or raised single-turn QA scores.[^c8] The AskOverconfidence variant (confident false premises to be identified) was trained the same way; coverage rose from 0.188 to 0.894, but redundant follow-up (Unq.) was 0.463, so over-asking was not solved there.[^c9]

## Limits

- The reward needs a rubric of what is missing; it exists here because the benchmark constructs the degradation itself, so it is not available for naturally underspecified queries without a rubric.
- Reward values (-2.0, -0.8, 0.8, 1.0, -1.0) are hand-set; no ablation of them was read, so which term drives the gain is not established (my reading of the text, which describes no such ablation).
- Judge and user simulator are LLMs; the paper reports cross-judge checks in appendices that I did not read in detail.
- The authors state AskBench "remains an offline benchmark constructed from existing QA pairs", so the information space is bounded by the rubric.[^c10]
- One 7B base model; the SFT-versus-RLVR contrast is preliminary by the authors' own label.
- The 0.463 redundancy on AskOverconfidence shows the reward does not penalize unnecessary questions strongly.

## Related

- [[underspecified-question-eager-answering]] — the failure (answering from an assumed reading) this reward is trained against
- [[staged-clarification-reward-pipeline]] — another reward design for clarification training
- [[post-refusal-clarification-reward]] — a different reward trigger for asking back
- [[query-misalignment-framework]] — the missing-information and false-premise categories AskBench instantiates
- [[uncertainty-driven-synthetic-clarification-training]] — synthetic data route to clarification training

[^c1]: arxiv-2602-11199 — "We refer to the items"
[^c2]: arxiv-2602-11199 — "revealing only the information explicitly asked"
[^c3]: arxiv-2602-11199 — "we strongly penalize answering early"
[^c4]: arxiv-2602-11199 — "These hand-set weights are shared across"
[^c5]: arxiv-2602-11199 — "no single “gold” clarification trajectory, we rely"
[^c6]: arxiv-2602-11199 — "OursI improves Acc. from 0.332 to 0.615 and Cov. from"
[^c7]: arxiv-2602-11199 — "per se is insufficient without a learning signal that"
[^c8]: arxiv-2602-11199 — "This contrasts with an AskMind SFT baseline, which improves asking metrics but hurts outof-domain performance"
[^c9]: arxiv-2602-11199 — "higher Unq. (0.463), indicating that reducing redundant follow-up remains a challenge in this"
[^c10]: arxiv-2602-11199 — "AskBench remains an offline benchmark constructed from existing QA pairs, so its information"
