---
description: "A single LLM writes a justification and a binary correctness label after each reasoning step, in one generation, so per-step verdicts need no separate verifier model."
aliases: ["Stepwise Think-Critique", "STC", "interleaved self-critique", "inline step verdict", "full-mode critique"]
sources: ["arxiv-2512-15662"]
---
# Inline step critique

A reasoning trace can carry its own verdicts. In Stepwise Think-Critique (STC), a single LLM "emits a structured, step-level critique inline with each reasoning step".[^c1] Each critique has two parts: a justification in natural language, and a binary label that says whether the step is correct.[^c2] The critique is produced in the same generation as the step, so the verdict is written as the trace is written, not by a second model after it.

The motivation is set against post-hoc checking. Most models either "generate reasoning without explicit selfchecking or rely on external verifiers to detect" errors.[^c3] A process reward model (PRM), the external scorer studied in [[process-reward-model-hackability]], runs after a policy has produced its steps. The authors' objection is timing and plumbing: "the post-hoc nature (i.e., the separation of reasoning and verification) prevents timely feedback".[^c4] Keeping a policy and a verifier apart also has a deployment cost: "passing trajectories between models requires additional scheduling, memory management, and fault".[^c19]

The paper defines two modes. "Compact mode: reasoning only, omitting critiques to save tokens."[^c5] "Full mode: reasoning and critique are interleaved,"[^c6] which gives a step-level judgment and error localization. The interleaving is not only a display choice. The authors write that "Considering the critiques would influence the next step reasoning",[^c7] so a verdict written at step n is part of the context for step n+1. The format is enforced: "we require that each reasoning step is followed by a well-formed critique".[^c8] Without that requirement the verdicts could be skipped, and a step with no verdict would count as no judgment at all.

The reported effect is on two measures. On five mathematical benchmarks, "STC improves Pass@1 by" 7.2% over the 1.5B base model, and it reaches "67.4% step-level critique F1, surpassing seven" external PRMs.[^c9] The F1 is a balanced one, "the harmonic mean of correct accuracy and error" accuracy.[^c10] Each step gets one binary prediction, so no threshold has to be chosen. A PRM gives a continuous score, which has to be cut at a threshold; the paper gives each PRM its per-dataset best cut, an oracle that needs labels to pick.

What transfers from the PRM literature is the scoring frame: a per-step verdict evaluated against step labels with F1. What does not transfer cleanly is the object being scored. The verdict is written by the policy that wrote the step, so, in my reading, the critic and the policy can share their errors unless training separates them. The paper's answer to that is the critique reward, see [[critique-consistency-reward]]. Whether a same-model verdict is less biased than an external one is not settled by the sections I read.

## Limits

- One base model (DS-Qwen-1.5B) and one seed: "multi-seed experiments were not run due to compute cost".[^c11]
- Mathematics only, English text: "We do not evaluate STC on code",[^c12] and the authors narrow their "critical thinking" claim to step-level error detection in math chain-of-thought.
- The step labels are a judge's, not ground truth. The authors "use GPT-5-mini as the judge",[^c13] and when the reference is swapped to Claude, balanced F1 "differs by only 0.4%" on AIME24 while Corr. and Err. move in opposite directions.[^c14]
- The granularity differs. STC steps are blank-line-delimited and finer than most PRMs' paragraphs, so the comparison runs at different base rates: "should be read as evidence that STC reaches a" calibration-free operating point, "not as a direct step-by-step claim".[^c15]
- Critic reliability is uneven: it is "where critic reliability is weakest" on Minerva.[^c16]
- Reward hacking was checked by inspection, not by a test: "we did not observe evidence of" it.[^c17] An absence seen on inspection is a weaker claim than a probe like those in [[process-reward-model-hackability]] (my reading).
- Cost: "The full mode interleaves critiques with reasoning", which adds tokens at inference time.[^c18] The appendix's own advice is the compact default: "We recommend defaulting to compact mode and enabling" full mode only when interpretability is required,[^c20] so the verdict is not free.

## Related

- [[critique-consistency-reward]] — the reward that trains these verdicts from final-answer correctness, with no step labels
- [[process-outcome-consistency-verification]] — a verifier that checks a whole derivation against its outcome, the non-stepwise counterpart
- [[same-model-self-verification-conditional-confidence]] — a same-model self-check at answer level, without per-step labels
- [[stage-level-hallucination-loss-masking]] — stage labels on self-verification traces, used to mask the loss rather than to score at inference

[^c1]: arxiv-2512-15662 — "LLM emits a structured, step-level critique inline with each reasoning step"
[^c2]: arxiv-2512-15662 — "where jn is a natural-language justification and"
[^c3]: arxiv-2512-15662 — "generate reasoning without explicit selfchecking or rely on external verifiers to detect"
[^c4]: arxiv-2512-15662 — "the post-hoc nature (i.e., the separation of reasoning and verification) prevents timely feedback"
[^c5]: arxiv-2512-15662 — "Compact mode: reasoning only, omitting critiques to save tokens."
[^c6]: arxiv-2512-15662 — "Full mode: reasoning and critique are interleaved,"
[^c7]: arxiv-2512-15662 — "Considering the critiques would influence the"
[^c8]: arxiv-2512-15662 — "we require that each reasoning step is followed by a well-formed critique"
[^c9]: arxiv-2512-15662 — "STC improves Pass@1 by"
[^c10]: arxiv-2512-15662 — "the harmonic mean of correct accuracy and error"
[^c11]: arxiv-2512-15662 — "multi-seed experiments were not run due to compute cost"
[^c12]: arxiv-2512-15662 — "We do not evaluate STC on code"
[^c13]: arxiv-2512-15662 — "we use GPT-5-mini as the judge"
[^c14]: arxiv-2512-15662 — "differs by only 0.4%"
[^c15]: arxiv-2512-15662 — "should be read as evidence that STC reaches a"
[^c16]: arxiv-2512-15662 — "where critic reliability is weakest"
[^c17]: arxiv-2512-15662 — "we did not observe evidence of"
[^c18]: arxiv-2512-15662 — "The full mode interleaves critiques with reasoning"
[^c19]: arxiv-2512-15662 — "passing trajectories between models requires additional scheduling, memory management, and fault"
[^c20]: arxiv-2512-15662 — "We recommend defaulting to compact mode and enabling"
