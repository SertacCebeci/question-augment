---
description: "A model's critique of its own output improves the next draft only when it names where the problem is and what to do; generic or missing critique recovers little, and wrong critique is the main failure"
aliases: ["Self-Refine", "self-feedback refinement loop", "actionable and specific feedback"]
sources: ["madaan-2023", "arxiv-2511-18714"]
---
# Specific, actionable self-feedback

In Self-Refine one model plays three roles: it drafts an answer, writes feedback on its own draft, then rewrites the draft given that feedback. The loop repeats until a stopping condition is met. The condition is either a fixed step count or a stop indicator the model emits inside the feedback.[^c1] The feedback prompt is shown input-output-feedback examples, and the model is told to write feedback that is "actionable and specific".[^c2] Actionable means the feedback "should contain a concrete action that would likely improve the output". Specific means it "should identify concrete phrases in the output to change".[^c3]

## What the feedback has to carry

The work's own contrast is between "Avoid repeated calculations in the for loop" (it pinpoints an issue and suggests an improvement) and "Improve the efficiency of the code" (it lacks that precision and direction).[^c4] The ablation scores form a gradient. In code optimization the score falls from 27.5 with full feedback to 26.0 with generic feedback and 24.8 with none.[^c5] In sentiment reversal, generic feedback drops the score from 43.2 to 31.2, and the task fails without feedback. In acronym generation, removing actionable feedback drops it from 56.4 to 48.0.[^c6] Generic feedback gives some benefit, so the loss is graded rather than all-or-nothing.

## Where it fails: the critic, not the rewriter

In a manual analysis of 35 successes and 35 failures (code optimization and math), unsuccessful cases were mostly erroneous feedback. 33% had feedback that mislocated the error and 61% had feedback proposing an inappropriate fix. Only 6% were a refiner mishandling good feedback.[^c7] So the quality of the question the model puts to its own draft ("what is wrong, where, and what would fix it") is the bottleneck.

Math shows the limit. Gains were modest because the model could not tell whether an error existed. A consistent-looking chain of reasoning led the critic to say everything looks good, and ChatGPT did so in 94% of instances.[^c8] When an external source flagged that the answer was wrong, gains grew to 5%+.[^c9] Self-critique is therefore weakest exactly where the error is subtle and the draft is fluent.

## Iteration

Quality tends to rise with iterations but with diminishing returns. Code optimization went from 22.0 to 28.8 after three iterations, and constrained generation from 29.0 to 49.7.[^c10] Improvement need not be monotonic when feedback covers several aspects. The method then scores each aspect numerically so the best output can be selected.[^c11] Each step conditions on the whole history of earlier outputs and feedback, so the model can avoid repeating mistakes.[^c12]

## Limits

- All results are with prompted GPT-3.5, ChatGPT and GPT-4, few-shot, over seven tasks. Nothing here concerns human askers or questions posed to other parties.
- The specificity ablation compares one generic-feedback prompt with one specific prompt per task. It does not isolate "specific" from "actionable".
- The 70-sample failure analysis covers only code optimization and math.
- The claim that specific feedback is the cause of the gain rests on three ablation tasks. Whether the effect holds for stronger or fine-tuned models is not tested in the passages read.
- The link between the 94% "everything looks good" rate and the gain from external error flags is the work's explanation, not an isolated test.
- A later multi-agent question generator puts a reflector between a validator and the rewriter, and describes it as one that "abstracts high-level revision cues"[^c13]. That is the opposite pull from the specificity requirement above: a cue abstracted to a high level may name no phrase to change. The paper reports whole-pipeline scores against single-pass models[^c14], so whether its reflector's cues were specific enough to help is not tested there; this is my reading, not a result of that paper.

## Related

- [[prompted-stopping-critic-robustness]] — the stop indicator in the loop is a critic judgement and can be fooled
- [[adversarial-metric-self-review]] — another self-critique-before-commit loop
- [[returns-per-token-spent]] — diminishing returns per added iteration
- [[reasoning-trap]] — fluent reasoning that hides an error

[^c1]: madaan-2023 — "The stopping condition stop(f bt , t) either stops at a specified timestep t,"
[^c2]: madaan-2023 — "We prompt the model to write feedback that is actionable and specific via f b(k) ."
[^c3]: madaan-2023 — "By ‘specific’, we mean the feedback should identify concrete phrases in the output to change."
[^c4]: madaan-2023 — "Generic feedback, like Improve the efficiency of the code,"
[^c5]: madaan-2023 — "performance slightly dips from 27.5 (S ELF -R EFINE feedback) to 26.0 (generic"
[^c6]: madaan-2023 — "performance drops from"
[^c7]: madaan-2023 — "61% were a result of feedback suggesting"
[^c8]: madaan-2023 — "think that “everything looks good” (e.g., ChatGPT feedback for 94% instances is ’everything looks"
[^c9]: madaan-2023 — "bigger (5%+) if an external source can identify if the current math answer is incorrect."
[^c10]: madaan-2023 — "which improves to 28.8 after"
[^c11]: madaan-2023 — "generates numerical scores"
[^c12]: madaan-2023 — "we retain the history of previous feedback and"
[^c13]: arxiv-2511-18714 — "abstracts high-level revision cues"
[^c14]: arxiv-2511-18714 — "Compared to GPT-4o, MAGMA-Edu improves the average textual metric from 57.01 to 92.31"
