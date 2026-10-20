---
description: "A reward that checks reply type (clarify, hedge, refuse) on deliberately underspecified prompts, not only correctness, reduces premature answering and lifts multi-turn math accuracy."
aliases: ["ICPO", "illocution-calibrated policy optimization", "calibrated humility reward"]
sources: ["arxiv-2601-15330"]
---
# Illocution-conditioned reward

Standard RLVR gives reward 1 for a correct final answer and 0 otherwise. Wang et al. report that this pushes models to answer confidently even when the question is missing information, which hurts later turns: "Overconfidence in Standard RLVR" is the paper's name for it.[^c1] ICPO changes the reward in two steps. First an expert model removes one or two conditions from a training question, making it unsolvable.[^c2] Then a judge model labels each sampled response with one of seven types (Answer attempt, Clarification, Interrogation, Discussion, Hedging, Refusal, Missing).[^c3] On the underspecified variant, reward is 1 if the type is in {Clarification, Interrogation, Discussion, Hedging, Refusal}, else 0; on ordinary questions the usual correctness reward applies.[^c4] Optimization is GRPO with group-normalized advantages.[^c5]

## Why early answering is the target

In the paper's analysis of Qwen2.5-Instruct models, conversations whose first answer attempt came later scored higher for all models.[^c6] The authors' reading is that a conversation opened with an underspecified query gives the least information, so a first attempt is least likely to be right and can plant a flawed assumption that persists.[^c7] Fig. 1 shows RLVR-trained models answering directly more often than the base model, while ICPO raises non-answer types.

## What was measured

- Multi-turn accuracy (GSM8K-derived, user reveals conditions gradually): for Qwen2.5-7B-Instruct the base model scores 35.4, standard RLVR 47.2 and ICPO 55.4; for the 1.5B model, 17.0, 26.1 and 32.8.[^c8] The abstract's "75%" average gain is stated against the RLVR baseline.[^c9]
- Single-turn math benchmarks stayed level or slightly better (e.g. 7B average 37.8 vs 38.2).[^c8]
- Entropy: ICPO kept policy entropy around 0.3, while standard RLVR fell to about 0.1.[^c10]
- Control against generic anti-collapse methods (Clip-higher, Clip-Cov, KL-Cov, RL-PLUS): these reached 47.7 to 51.6 on multi-turn accuracy versus 55.4 for ICPO, which the authors take to show the gain is not just preserved entropy.[^c11]

## Limits

- Only math (GSM8K-style, competition sets), two Qwen2.5 sizes in the main table; no non-verifiable or open-domain asks.
- The reward is type-only: any hedge or refusal on an underspecified prompt earns 1, whether or not it names the missing piece. Quality of the clarifying question is not scored, and nothing in the text penalizes over-asking on answerable prompts beyond the correctness reward there.
- Ambiguity is synthetic (condition deletion by an LLM); real vague requests may differ. Both the simulator and the judge are one model (DeepSeek-V3), whose labeling accuracy is not reported in the text I read.
- The overconfidence mechanism (entropy collapse) is the authors' interpretation; the entropy comparison is correlational.
- The mix ratio of standard to simulated prompts was not found in the slices read, so interaction with abstention base rate is unknown.

## Related

- [[underspecified-question-eager-answering]] — the same eager-answer failure measured in a benchmark, without training
- [[abstention-base-rate-sensitivity-in-rl]] — a reward that favors abstaining is sensitive to how often it is correct; ICPO's mix is subject to the same worry (my inference)
- [[initial-exploration-problem]] — early commitment hurting later progress

[^c1]: arxiv-2601-15330 — "Overconfidence in Standard RLVR."
[^c2]: arxiv-2601-15330 — "prompt the expert model to randomly remove one or two conditions from the"
[^c3]: arxiv-2601-15330 — "we similarly define seven response categories: Answer attempt,"
[^c4]: arxiv-2601-15330 — "If the model’s response type belongs to the expected type set T , a"
[^c5]: arxiv-2601-15330 — "We use Group Relative Policy Optimization (GRPO) [20] as our"
[^c6]: arxiv-2601-15330 — "for all models, conversations with"
[^c7]: arxiv-2601-15330 — "an early attempt at a"
[^c8]: arxiv-2601-15330 — "Table 1: Performance of the Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct models on six competition-level math benchmarks, along with"
[^c9]: arxiv-2601-15330 — "boasting an average improvement"
[^c10]: arxiv-2601-15330 — "and high policy entropy, fluctuating around 0.3."
[^c11]: arxiv-2601-15330 — "than indiscriminate"
