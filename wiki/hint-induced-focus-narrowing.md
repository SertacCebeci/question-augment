---
description: "Injecting rule-derived hints into an LLM judge's prompt raised detection of the hinted issues, yet the hinted judges rediscovered only 45–70% of the issues the unhinted judge found."
aliases: ["issue-rediscovery rate", "hint-induced narrowing", "analytic hint injection", "focus narrowing under cues"]
sources: ["arxiv-2512-16272", "arxiv-2511-18221"]
---
# Hint-induced focus narrowing

A hint is a cue placed in a judge's prompt that names an issue to look for. In the COBOL study the cue came from a rule-based checker, a pattern-matching tool that "encodes over 30 error types identified" by expert review and emits a short message for each issue it finds. The messages were injected into the judge's prompt, either appended to the end or with an instruction to address them in detail. The authors report that "introducing analytic hints led to consistent gains across all models."[^c1]

The gain is real on the issues the hints name, and it moves overall coverage. Native judges detected "roughly 45–63% of total issues, whereas hybrid judges" reached "48–74.1%, depending on model and prompt."[^c2][^c3] Most of the rise came from errors the checker found and the native judge missed, a point taken up in [[analytic-llm-detection-complementarity]].

The cost sits on the other side. The authors checked what each hinted judge still found among the issues the native judge had already reported, by matching the two sets of explanations. The hinted judges "reproduced approximately 45–70% of the issues originally identified by" their native counterparts.[^c4] They read the drop as the hints shifting the judge's attention, so that the judge "deprioritized unhinted aspects of the evaluation."[^c5] Their summary is that "injection improves targeted diagnostic precision but may narrow overall coverage."[^c6]

Two numbers therefore describe a hinted judge, and a gain on the hinted issues alone hides the second. One is detection of the named issues, which rises. The other is rediscovery of the unnamed ones, which falls. The authors propose the second as a diagnostic: "issue-rediscovery rate as an additional diagnostic metric for" judging evaluator reliability.[^c7] Rediscovery differed by model. "DeepSeek-v3 and gpt-oss-120b achieved the highest rediscovery rates," and the paper calls the spread a sign that some judges "preserved their original evaluative behavior more effectively than others" when given new guidance.[^c8]

The mechanism is my inference, not the paper's test. A judge reads a long program under a limited attention budget. A prompt that lists some issues to check spends part of that budget on them, and issues the judge would have raised unprompted get less of it. The paper shows the drop and its spread across judges; it does not isolate attention as the cause.

A second study places hints the same way, but on a different target: GPT-4o assessing undergraduate circuit-analysis homework. There the hints were written from error types seen earlier, and the paper lists them as appended to different prompting stages, each designed to address common errors.[^c16] The authors describe the aim as: "hints into the prompt, explicitly guiding GPT-4o to avoid" the errors.[^c12] Splitting the hints across steps was meant to keep prompts short: "steps, thereby avoiding overly lengthy prompts."[^c13] On the 13 examples where the earlier unhinted evaluation had erred, "responses contained errors, 11 were correctly addressed using" the enhanced prompts.[^c14] That result is a gain on the hinted error types only. The study does not report whether unhinted issues were still found, so the rediscovery cost described above is neither confirmed nor ruled out there. See [[aspect-separated-evaluation]] for the step structure the hints were placed in.

## Limits

- One task and a small set: the paper's own words are "limited to one task and a small dataset."[^c9] The dataset is 100 synthetic COBOL programs, and the text gives no spread across seeds or programs.
- The judges' evaluation prompt is not in the text: "(not disclosed due to proprietary constraints)."[^c10] Cue placement and wording therefore cannot be replayed, and the size of the narrowing under other prompts is unknown.
- Rediscovery is itself measured by a model. "This matching was conducted by" an issue-finder judge, so the diagnostic inherits a judge's errors.[^c11]
- Coverage is relative to an estimated total, because "the exact number of true issues is unknown." See [[analytic-llm-detection-complementarity]] for what that denominator does.
- Net coverage still rose in this study (the hybrid numbers above exceed the native ones), so the narrowing was a loss on unhinted issues, not a cancellation of the gain. Whether the loss can outweigh the gain with more hints, or with a judge that already covers much, is not tested.
- Only two injection schemes were compared. How hint length, count and placement change the trade-off is not measured.
- The circuit-homework hints were tested on the same error examples they were written from, and the gain was not separated from the step split and the added context. Whether those hints narrow coverage of unnamed errors is not reported.[^c15]

## Related

- [[rubric-blind-spot]] — a fixed criterion list finds only the errors it names in advance; an injected hint is the same limit applied per input
- [[explicit-cue-check-tradeoff]] — telling a model to check its question for hints raises acknowledgment and false reports; a different cue effect, on answering rather than judging
- [[hint-adherence-without-acknowledgement]] — a hint appended to an answer prompt is followed without being mentioned; here the hint is an input to the judge and its effect is on what the judge reports
- [[analytic-llm-detection-complementarity]] — the same hinted checker, seen from the side of what it adds to the judge
- [[rubric-presence-absence-asymmetry]] — the judge-side version of the omission problem: what is missing is harder to flag than what is present

[^c1]: arxiv-2512-16272 — "introducing analytic hints led to consistent gains across all models"
[^c2]: arxiv-2512-16272 — "roughly 45–63% of total issues, whereas hybrid judges"
[^c3]: arxiv-2512-16272 — "reached 48–74.1%, depending on model and prompt."
[^c4]: arxiv-2512-16272 — "the hint-augmented judges reproduced approximately 45–70% of the issues originally identified by"
[^c5]: arxiv-2512-16272 — "deprioritized unhinted aspects of the evaluation"
[^c6]: arxiv-2512-16272 — "injection improves targeted diagnostic precision but may narrow overall coverage"
[^c7]: arxiv-2512-16272 — "issue-rediscovery rate as an additional diagnostic metric for"
[^c8]: arxiv-2512-16272 — "DeepSeek-v3 and gpt-oss-120b achieved the highest rediscovery rates"
[^c9]: arxiv-2512-16272 — "limited to one task and a small dataset"
[^c10]: arxiv-2512-16272 — "(not disclosed due to proprietary constraints)"
[^c11]: arxiv-2512-16272 — "This matching was conducted by"
[^c12]: arxiv-2511-18221 — "hints into the prompt, explicitly guiding GPT-4o to avoid"
[^c13]: arxiv-2511-18221 — "steps, thereby avoiding overly lengthy prompts."
[^c14]: arxiv-2511-18221 — "responses contained errors, 11 were correctly addressed using"
[^c15]: arxiv-2511-18221 — "examples shown in TABLE II, which include cases where"
[^c16]: arxiv-2511-18221 — "lists the hints appended to different prompting stages, each"
