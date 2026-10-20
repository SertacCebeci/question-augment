---
description: "Placing a prompt's rubric in a base model's context raises its rubric score; that lift, measured forward-only, diagnoses how much rubric signal self-distillation can transfer."
aliases: ["rubric-conditioning gap", "rubric-conditioning lift", "rubric-in-prompt lift"]
sources: ["doi-10-48550-arxiv-2606-12507"]
---
# Rubric-conditioning gap

Give a base model the prompt-specific rubric in its context and its answers score higher against that rubric than its answers to the bare prompt. The paper measures the difference as rubric satisfaction on the same prompts, with and without the rubric, and calls it the rubric-conditioning gap: "The +rubric lift measures the rubric-conditioning gap."[^c1] On RubricHub-medical, Qwen-2.5-7B-Instruct rises from 33.0 to "78.0 (+45.0)" with the rubric in its prompt.[^c2] Across the four base models and both domains in the paper's Table 1 the lift runs from +31.0 (science, Qwen-2.5-3B, "62.0 (+31.0)") to +46.2 (medical, Qwen3-4B, "89.8 (+46.2)").[^c3][^c4]

The gap belongs to a base model and a prompt set, and it is read before any training run. The authors use it as a diagnostic, not as an outcome: "We use this gap as a diagnostic for how much signal" the unconditioned student can take up.[^c5] The teacher that makes this a plausible budget is the same base model with the rubric added, "a frozen copy of the base model conditioned on the prompt and rubric provides" next-token targets on the student's own rollouts.[^c6] Read this way, the gap is the room the distillation has to carry across (my inference). Whether a fixed share of it is recovered is an analysis the paper places in its Section 5, "the recovered fraction"; I did not read that section in this pass.[^c7]

The check is cheap. The paper calls the gap a "cheap diagnostic before training, since it can be measured with a forward-only validation pass rather than a full GRPO run."[^c8] Nothing is trained to read it, which is the property that makes it useful as a go or no-go before a self-distillation run.

It is not the same quantity as the log-probability version in [[self-internalization-gap]], which reads how far a rubric in context moves the policy's log-probabilities and uses that shift as a verifier-free stopping signal. Both place the rubric in context of the same model, but one reads a graded score and the other a log-probability shift. The RGSD paper does not compare them, so treating them as two measurements is my inference.

## Limits

- The gap is not shown to predict the gain. On RubricHub-medical the lifts run from +43.1 to +46.2, yet the model with the largest lift, Qwen3-4B, gets the smallest RGSD gain, "42.0 (+7.5)."[^c10] The largest RGSD gain, "37.0 (+11.9)" for Qwen-2.5-7B, comes from the second-largest lift.[^c11] With four models and one domain, this is two tables set side by side, not a fit (my inference).
- The gap is measured with the same kind of LLM judge that grades the trained models, and the authors say "the absolute scores may still inherit judge-specific biases."[^c12] The size of the gap is therefore relative to a judge.
- The text does not say how large a gap counts as "meaningful." The paper says RGSD "is most useful when the base model has a meaningful rubric-conditioning response" and gives no threshold below which to skip the run.[^c13]
- One rubric-in-prompt format was used per dataset. Whether a shorter rubric, a rubric written by someone else, or different wording changes the lift is not measured here.
- For thinking models the rubric-conditioned trace can name criteria, so part of the lift may pass through text the student never sees (see [[rubric-aware-on-policy-self-distillation]]). How much of the lift takes that route was not measured.

## Related

- [[rubric-aware-on-policy-self-distillation]] — the method whose rubric-conditioned teacher this gap describes; the gap is the signal that method moves into the student.
- [[self-internalization-gap]] — the log-probability version of putting a rubric in context, used as a verifier-free stopping signal; a different measurement.
- [[soft-versus-hard-privileged-information]] — why a rubric conditions the teacher more per token than a reference does, on the student's own rollouts.

[^c1]: doi-10-48550-arxiv-2606-12507 — "The +rubric lift measures the rubric-conditioning gap"
[^c2]: doi-10-48550-arxiv-2606-12507 — "78.0 (+45.0)"
[^c3]: doi-10-48550-arxiv-2606-12507 — "62.0 (+31.0)"
[^c4]: doi-10-48550-arxiv-2606-12507 — "89.8 (+46.2)"
[^c5]: doi-10-48550-arxiv-2606-12507 — "We use this gap as a diagnostic for how much signal"
[^c6]: doi-10-48550-arxiv-2606-12507 — "a frozen copy of the base model conditioned on the prompt and rubric provides"
[^c7]: doi-10-48550-arxiv-2606-12507 — "Section 5 analyzes the recovered fraction empirically."
[^c8]: doi-10-48550-arxiv-2606-12507 — "cheap diagnostic before training, since it can be measured with a forward-only validation pass"
[^c10]: doi-10-48550-arxiv-2606-12507 — "42.0 (+7.5)"
[^c11]: doi-10-48550-arxiv-2606-12507 — "37.0 (+11.9)"
[^c12]: doi-10-48550-arxiv-2606-12507 — "but the absolute scores may still inherit judge-specific biases."
[^c13]: doi-10-48550-arxiv-2606-12507 — "RGSD is most useful when the base model has a meaningful rubric-conditioning response."
