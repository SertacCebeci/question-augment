---
description: "The accuracy change a prompting strategy brings can flip sign across tasks and models, so the same structured prompt can help one stage of a workflow and hurt another."
aliases: ["task-dependent prompt gain", "prompt effect heterogeneity", "no one-size-fits-all prompting", "prompt benefit depends on task"]
sources: ["arxiv-2512-22966", "arxiv-2512-12042", "arxiv-2512-03818", "arxiv-2511-22832"]
---
# Task-conditional prompt gain

A prompting strategy is not a property of the strategy alone. What it does is the difference between the model's accuracy with the added structure and without it, and that difference is measured per task and per model. In a benchmark of three LLMs (ChatGPT-4o, Gemini 2.5 Flash, Llama 3.3 70B) on 36 clinical vignettes, the same MedPrompt-style package (self-generated chain-of-thought, few-shot exemplars, and an answer-shuffling ensemble) raised one task and lowered another. On relevant diagnostic testing it helped: "the accuracy of ChatGPT 4o for relevant diagnostic testing surged from 30.8% to 50.7%" with exemplars chosen by similarity.[^t1] On differential diagnosis and treatment recommendation it hurt for all or most models: "MedPrompt with KNN dynamic few-shot prompting led to a sharp decline in ChatGPT 4o" on differential diagnosis, from 71.1% to 56.0%.[^t2] The authors summarise the pattern as "the effect of prompt engineering was strongly task- and model-dependent."[^t3]

The gain was largest where the unprompted baseline was weakest. Relevant diagnostic testing was "the most challenging task" out of the box for all three models, and the prompt helped it most.[^t4] The authors read this as a headroom effect: "when a model lacks a robust internal strategy for a high-uncertainty task, the explicit structure of a prompt could be highly beneficial."[^t5] The same reading explains why final diagnosis was dropped from the prompting analysis: baseline accuracy was near-complete, "which left little room for further improvement."[^t6] Within this study, then, the ordering of tasks by baseline difficulty predicts where structure is likely to help. The study does not test that prediction beyond four tasks.

The same moderator shows up when the task is judging a recommendation rather than diagnosing. In a benchmark of LLM judges for in-car restaurant recommendations, "a negligible effect is observed" for reasoning models, while for non-reasoning models "the best improvement is identified" under advanced prompting.[^t8][^t12] The largest gains were for small non-reasoning models, "in particular, when applying multi-agent prompting."[^t9] For reasoning models the order reverses: single-model prompting such as CoT-3 or SC-5 "outperformed all prompting techniques."[^t10] The authors also call multi-agent results unstable: they "yields inconsistent results, particularly for reasoning models, performing similarly or even worse than single-agent-based prompting."[^t11] The headroom reading from the clinical study fits this pattern, since reasoning judges start high and have less room for structure to add. The judge paper does not test that reading; it is mine.

The mechanism that makes the sign flip is only partly resolved. The authors offer a conjecture: "a plausible explanation is that prompt length and context-window competition may lead to distraction from core task-relevant signals."[^t7] This is not tested in the benchmark; it is the authors' reading of why long, multi-example prompts lost ground on some tasks. For a question-writer or answerer the transferable point is narrower. A prompt is a fixed intervention, and its effect has to be read off the task and the model it is applied to, not carried over from a benchmark where it worked.

My reading is that the same shape recurs under other moderators in neighbouring notes: query length decides which expansion prompt wins, the best reasoning pattern varies per problem, and a prompted style that helps one assistant task does not help another. These are links to the wiki's own notes, not claims tested here (see Related).

A third setting shows a small gain from add-ons once a baseline is strong. In a study of LLM classification of psychological constructs in expressive writing, persona, chain-of-thought and explanation prompts were layered on prompts already chosen by a search. The authors report that the additive techniques "offer only small and inconsistent" gains,[^t13] and that in most cases they "offer little or no benefit beyond the baseline prompt."[^t14] The difference from the weaker baseline "is never statistically significant."[^t15] This is consistent with the headroom reading above, since the baseline here had already been tuned. The study did not vary baseline difficulty as a moderator, so the fit is my inference, not the authors' claim. See [[combinatorial-empirical-prompting]] for the baseline search.

A fourth setting is entity matching, the decision whether two records name the same real-world object. The paper compares a three-step prompt with a plain prompt on six public benchmark tasks; the staged method "first identifies matched and unmatched tokens between two records, then determines the attributes most influential to the matching decision".[^t16] In zero-shot use the staged reasoning did better on some tasks and worse on others: the authors report that "reasoning based methods achieve better performance in 4 out of 6 tasks".[^t17] With two in-context examples the standing weakens, and the authors guess that the examples supply signals, so that "therefore the insights brought by the reasoning strategy become less important".[^t18][^t19] The gain is also paid for in tokens, since "the LLM cost is much heavier since each step requires seperate input and output tokens".[^t20] Every number comes from one model, reached through the OpenAI API.[^t21] So the moderators here are the exemplars in the prompt and the dataset together, and the paper does not separate them from the model. This is a pattern across cells, not a tested interaction (my reading).

## Limits

- The sample is small and uneven: 36 vignettes, with 10 for essential immediate steps. The authors say the sample sizes "reduce statistical power for task-specific comparisons," so many task-by-model contrasts are directional.
- Most pairwise comparisons were not significant. Only "a small number of pairwise comparisons were statistically significant," so the sign flips are a pattern across cells, not a tested interaction effect.
- Only two MedPrompt variants (KNN-chosen and randomly chosen exemplars) were tested, with a fixed three exemplars per question. Other prompt strategies were not evaluated, so the claim is about this package, not prompting in general.
- The difficulty-gated reading is an observation over four tasks. It has no independent measure of baseline difficulty beyond the models' own accuracy.
- The benchmark is closed-form multiple choice, drawn from textbook-style vignettes. Whether the flip holds for open-ended clinical text is not shown.
- The mechanism (context competition, distraction) is the authors' conjecture and is not separated from alternatives.

## Related

- [[query-length-dependent-expansion-prompting]] — the same pattern with query length as the moderator: which prompt wins depends on the input
- [[per-problem-reasoning-pattern-selection]] — the best reasoning pattern varies per problem, so no fixed pattern is optimal
- [[capability-dilution]] — an added objective hurts most where the task is already demanding, the opposite direction from the headroom reading here
- [[assistant-personality-style]] — no single prompted style wins across tasks, a parallel finding for style rather than reasoning structure
- [[instruction-dilution-of-structured-reasoning]] — one concrete way added structure can cancel a reasoning scaffold inside a long prompt
- [[compact-exemplar-scaffold-over-verbose-reasoning]] — the compact-scaffold advantage in moral prompting, where this clinical study found structure sometimes counterproductive
- [[context-constraint-judge]] — the same moderator, model class, on an LLM judge of in-car recommendations

[^t1]: arxiv-2512-22966 — "the accuracy of ChatGPT 4o for relevant diagnostic testing surged from 30.8% to 50.7%"
[^t2]: arxiv-2512-22966 — "led to a sharp decline in ChatGPT 4o"
[^t3]: arxiv-2512-22966 — "was strongly task- and model-dependent"
[^t4]: arxiv-2512-22966 — "the most challenging task in out-of-the-box evaluation across all three models"
[^t5]: arxiv-2512-22966 — "when a model lacks a robust internal strategy for a high-uncertainty task"
[^t6]: arxiv-2512-22966 — "which left little room for"
[^t7]: arxiv-2512-22966 — "a plausible explanation is that prompt length and context-window competition may lead to"
[^t8]: arxiv-2512-12042 — "a negligible effect is observed"
[^t9]: arxiv-2512-12042 — "in particular, when applying multi-agent prompting."
[^t10]: arxiv-2512-12042 — "or SC-5 outperformed all prompting techniques."
[^t11]: arxiv-2512-12042 — "yields inconsistent results, particularly for reasoning models, performing similarly or even worse than single-agent-based prompting."
[^t12]: arxiv-2512-12042 — "for non-reasoning models, the best improvement is identified"
[^t13]: arxiv-2512-03818 — "additive techniques offer only small and inconsistent"
[^t14]: arxiv-2512-03818 — "additive techniques offer little or no benefit beyond the baseline prompt"
[^t15]: arxiv-2512-03818 — "is never statistically significant"
[^t16]: arxiv-2511-22832 — "first identifies matched and unmatched tokens between two records, then determines the attributes most influential to the matching decision"
[^t17]: arxiv-2511-22832 — "reasoning based methods achieve better performance in 4 out of 6 tasks"
[^t18]: arxiv-2511-22832 — "the relative performance of reasoning based methods are not as good as that under zero-shot settings"
[^t19]: arxiv-2511-22832 — "therefore the insights brought by the reasoning strategy become less important"
[^t20]: arxiv-2511-22832 — "the LLM cost is much heavier since each step requires seperate input and output tokens"
[^t21]: arxiv-2511-22832 — "we use the official OpenAI APIs of GPT-5.1-mini"
