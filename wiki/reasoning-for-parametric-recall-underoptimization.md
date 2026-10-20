---
description: "Reasoning models under-reason on closed-book recall: a think-step-by-step cue helps recall but not math, and answer-correctness RL on TriviaQA improves recall across QA sets."
aliases: ["parametric knowledge access reasoning", "knowledge-recall reasoning gap", "closed-book reasoning under-optimization"]
sources: ["arxiv-2602-22193"]
---
# Reasoning for parametric recall is under-optimized

Reasoning models are trained with verifiable rewards mostly on mathematics and code. Ma and Hewitt ask whether the reasoning they emit also serves recall of facts stored in their own weights (closed-book question answering). Their answer is that it does not by default, and that this is cheap to fix.

## The default is not the best

Four reasoning models (R1-Distill-Qwen-1.5B, Olmo-3-7B-Think, GPT-OSS-20B, GPT-5.2) were run on TriviaQA and Natural Questions with and without an added "think step-by-step" cue. The cue raised extracted-answer recall on average by 0.8 points across datasets and models.[^c1] For GPT-OSS-20B the gains were +1.1 and +1.3 points. On MATH the cue did not help, and accuracy degraded across three models.[^c2] The authors read the contrast as: models already reason well on math, thanks to RLVR, but "do not know to do their best knowledge access reasoning by default."[^c3] Forcing an empty reasoning span cost 6.9% on average, so reasoning does help recall; it is just not saturated.[^c4]

## Training the reasoning with answer correctness

The same paper trains GPT-OSS-20B with online GRPO-style RL on TriviaQA. The reward depends only on the final answer, with exact match weighted over contained-answer recall plus a format term, and does not supervise the trace.[^c5] After training, TriviaQA exact match rose from 36.5 to 63.6, Natural Questions from 6.0 to 18.2, and HotpotQA from 7.5 to 17.0; StrategyQA rose from 71.5 to 74.5. SimpleQA moved little (1.8 to 3.3).[^c6] An offline baseline, supervised tuning on the model's own correct traces, gave only small gains, so the on-policy adaptation of the reasoning carries the improvement.[^c7]

## What the reasoning becomes

Traces grew only modestly (94 to 107 tokens average), and the post-RL model "seems to sometimes just guess more accurately after brief reasoning."[^c8] In cases fixed by training, the model often states the correct answer earlier in the trace rather than reasoning more deeply.[^c9] The authors' stance is that for recall the useful reasoning is whatever elicits the memory, so it need not be deductive or human-interpretable.[^c10] The intended "spreading activation" style (walking through related concepts) was not shown to emerge.

## Limits

- One training model (GPT-OSS-20B) and one training set (TriviaQA); the cue study covers four models but only two recall datasets.
- Gains on SimpleQA are small, and several gains are in exact match rather than the relaxed extracted-recall; EM gains are larger partly because format and answer-span behavior can improve, which the paper does not separate (my reading).
- The paper does not show that the trace, rather than better answer calibration or shorter answering, causes the gain; the authors say the two lie on a spectrum.[^c9]
- Even after RL the cue still adds gains, so the headroom is not closed. The spreading-activation motivation is untested here.
- Whether these effects bear on how a user's question should be phrased is not studied; the cue is a system-side prompt.

## Related

- [[rlvr-answering-bias]] — RLVR shapes when a model answers versus abstains; here it shapes what it recalls.
- [[parametric-knowledge-gates-retrieval-noise-damage]] — another account of what the model's own stored knowledge does for answering.
- [[stepwise-self-qa-scaffold]] — prompted intermediate steps as a scaffold for answering.
- [[thinking-stagnation]] — a different limit on what reasoning tokens buy.

[^c1]: arxiv-2602-22193 — "models, we observe an average increase of 0.8%"
[^c2]: arxiv-2602-22193 — "but does not help on MATH"
[^c3]: arxiv-2602-22193 — "This shows that reasoning language models do not know to do their best knowledge access reasoning by default."
[^c4]: arxiv-2602-22193 — "We find that models perform 6.9%"
[^c5]: arxiv-2602-22193 — "that depends only on the final answer and does not"
[^c6]: arxiv-2602-22193 — "Table 2: GPT-OSS-20B performance before and after RL training on knowledge recall tasks."
[^c7]: arxiv-2602-22193 — "RL training contributes beyond what supervised fine-tuning"
[^c8]: arxiv-2602-22193 — "seems to sometimes just guess more accurately after brief reasoning."
[^c9]: arxiv-2602-22193 — "answer earlier in the reasoning trace rather than"
[^c10]: arxiv-2602-22193 — "elicits the memory from the model, so reasoning"
