---
description: "Self-repair of code is capped by the accuracy of the model's own diagnosis of its failure; a stronger model's or a human's explanation of the bug lifts the repair pass rate."
aliases: ["feedback bottleneck in self-repair", "diagnosis bottleneck", "explanation quality in self-repair"]
sources: ["doi-10-48550-arxiv-2306-09896", "arxiv-2511-21380"]
---
# Feedback quality bottleneck

In a self-repair loop a sampled program is run against the task's unit tests. If it fails, "the error message and the faulty program are given to a feedback generation model, which outputs a short explanation of why the code failed," and a repair is then sampled conditioned on that explanation.[^c1] The explanation is the step where the model has to diagnose its own mistake. The claim examined here is that this diagnosis, not the code writing, is what limits the loop.

The evidence comes from two interventions that change only the explanation. In the first, the code model is held fixed and its feedback is produced by a stronger model. "Artificially boosting the quality of the feedback significantly improves the efficacy of self-repair."[^c2] The paper reads this as showing that "This suggests that the textual feedback stage itself is of crucial importance."[^c3] On APPS both weaker models then beat their own no-repair baselines, and on HumanEval the gain Code Llama receives "increases further with the strength of the feedback model."[^c17]

In the second, GPT-4 is the repairer and the explanations are either its own or written by expert programmers. Each failing program received two human explanations, and 25 repair candidates were sampled per (feedback, program) pair and run against the tests. "The overall success rate is increased by 1.58× when we replace GPT-4’s own feedback" with the human explanations.[^c4] The paper's table puts the overall pass rate at 33.30% with GPT-4's explanations and 52.60% with human ones.[^c16] The gap widens with difficulty: on the introductory tier the rates are 42.64% and 62.21%, on the competition tier 3.67% and 14.67%.[^c16] "Perhaps unsurprisingly, the relative difference increases as the" problems get harder.[^c5]

The explanations differ in kind, not only in correctness. GPT-4's explanations were judged inaccurate far more often: "GPT-4’s feedback is much more likely to be inaccurate (32/80 vs. 7/80 for the human feedback)."[^c6] Human explanations also expressed doubt: "Our human participants sometimes express uncertainty (7/80); GPT-4 never does (0/80)."[^c7] The human explanations were also more willing to propose high-level changes in the paper's count, a second factor the authors list alongside accuracy.[^c18]

The paper's summary is that current models are held back by "their inability to reliably produce accurate and useful feedback on why the code is wrong."[^c8]

What transfers: a repair can only be as good as the diagnosis it is conditioned on. My inference, not the paper's test, is that a wrong explanation sends the repair samples toward a wrong fix, so extra repair samples cannot recover what the explanation removed.

## Limits

- The bottleneck is a hypothesis the paper states as one: "We hypothesize that this is because self-repair is bottlenecked by"[^c13] the model's ability to give feedback on its own code. The same paper finds that generation and repair success "trend together," and that "factors influence which one will overpower the other on any given domain."[^c14]
- The human study is small: "a small-scale study in which we provide GPT-4"[^c15] with feedback from people. It used 16 participants, with two explanations for each of 40 failing programs.[^c9] The accuracy and category counts come from the authors' manual reading of those explanations; the text read reports no second rater and no larger sample.
- Effort is not priced: "our study on human data did not track how much time the participants took to debug the"[^c12] programs. The comparison is of explanation quality, and says nothing about whether a human-in-the-loop approach is worth its cost.
- The repair comparison holds the repair count fixed at 25 per pair, so the cost of repair, which the paper's headline is about, is not part of the human result (my inference from that fixed count).[^c10]
- The stronger-model feedback experiment reports pass rates. In the sections read, the accuracy of the stronger model's explanations is not measured, so "better feedback" is established only as "feedback from a stronger model" (my inference that this means more accurate).
- Scope: "our experiments focus on self-contained Python programming tasks with executable unit"[^c11] tests. The paper notes that real software specifications are often incomplete and tests are scarce, where the diagnosis step may behave differently.
- Raw output is not a diagnosis. A study of a multi-agent coding system adapting research artifacts to new datasets gives the agent raw terminal tracebacks with no model-written explanation.[^c20] The abstract names execution error messages, with reference code, as the interventions that help most.[^c19] That setting is repository adaptation, not unit-tested function generation, and the paper does not separate error messages from reference code, so it does not test the explanation stage. A placebo-controlled study finds raw execution feedback adds nothing over a placebo (see [[placebo-controlled-retry-evaluation]]). The two results point in different directions and are not reconciled here (my inference).

## Related

- [[self-repair-anchoring]] — conditioning a small code model on its own failed attempt cost accuracy against blind resampling; a feedback bottleneck predicts that better explanations help, while anchoring predicts a cost from conditioning at all, so both can hold.
- [[placebo-controlled-retry-evaluation]] — separates the value of retrying from the value of feedback content; its feedback is raw execution output, not a model-written diagnosis, so its finding that execution feedback adds nothing over a placebo does not directly test the explanation stage studied here.
- [[specific-actionable-self-feedback]] — a self-critique helps when it names the problem and the fix, and wrong critique is the main failure; the same weakness, located in the explanation stage.
- [[reference-code-guided-repair]] — repair toward a hidden target by showing sibling solutions from the same repository; the feedback there is a reference, not a diagnosis.

[^c1]: doi-10-48550-arxiv-2306-09896 — "the error message and the faulty program are given to a feedback generation model, which outputs a short"
[^c2]: doi-10-48550-arxiv-2306-09896 — "Artificially boosting the quality of the feedback significantly improves the efficacy of self-repair."
[^c3]: doi-10-48550-arxiv-2306-09896 — "This suggests that the textual feedback stage itself is of crucial importance"
[^c4]: doi-10-48550-arxiv-2306-09896 — "the overall success rate is increased by 1.58× when we replace GPT-4’s own feedback"
[^c5]: doi-10-48550-arxiv-2306-09896 — "Perhaps unsurprisingly, the relative difference increases as the"
[^c6]: doi-10-48550-arxiv-2306-09896 — "GPT-4’s feedback is much more likely to be inaccurate (32/80 vs. 7/80 for the human feedback)."
[^c7]: doi-10-48550-arxiv-2306-09896 — "Our human participants sometimes express uncertainty (7/80); GPT-4 never does (0/80)."
[^c8]: doi-10-48550-arxiv-2306-09896 — "their inability to reliably produce accurate and useful feedback on why the code is wrong"
[^c9]: doi-10-48550-arxiv-2306-09896 — "We recruit 16 participants and collect a total of 2 human-written"
[^c10]: doi-10-48550-arxiv-2306-09896 — "we sample 25 repair candidates for each (feedback, program)-pair from GPT-4"
[^c11]: doi-10-48550-arxiv-2306-09896 — "our experiments focus on self-contained Python programming tasks with executable unit"
[^c12]: doi-10-48550-arxiv-2306-09896 — "our study on human data did not track how much time the participants took to debug the"
[^c13]: doi-10-48550-arxiv-2306-09896 — "We hypothesize that this is because self-repair is bottlenecked by"
[^c14]: doi-10-48550-arxiv-2306-09896 — "factors influence which one will overpower the other on any given domain."
[^c15]: doi-10-48550-arxiv-2306-09896 — "a small-scale study in which we provide GPT-4"
[^c16]: doi-10-48550-arxiv-2306-09896
[^c17]: doi-10-48550-arxiv-2306-09896 — "increases further with the strength of the feedback model"
[^c18]: doi-10-48550-arxiv-2306-09896 — "while human participants show a slightly greater tendency to suggest high-level changes (23/80 vs."
[^c19]: arxiv-2511-21380 — "Prompt-level interventions, especially providing execution error messages and reference code, substantially improve structural similarity to ground truth (from 7.25% to 67.14%)"
[^c20]: arxiv-2511-21380 — "the agent receives raw error outputs copied directly from the terminal (e.g., Python tracebacks)"
