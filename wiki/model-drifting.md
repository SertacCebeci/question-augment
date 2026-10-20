---
description: "Model drifting: a prompt tuned for one LLM can lose much of its accuracy on another, so the best prompt is a property of the model and task pair, not of the prompt alone."
aliases: ["model drifting", "prompt transfer gap", "source-optimal prompt transfer gap", "model-switch performance drift"]
sources: ["arxiv-2512-01420"]
---
# Model drifting

A prompt is tuned against a model, and the tuning does not travel. The PromptBridge paper names this Model Drifting and defines it as the performance change that follows a model substitution while the prompt stays fixed: "We refer to the performance drift induced by the model substitution as model drifting."[^m1] The mechanism is that the prompt which was best for the source model stops being best for the target: "the same prompt that was previously optimal for the source model often yields suboptimal" performance on the target.[^m2]

The paper writes the gap as a transfer gap. It is the target model's accuracy under the source-optimal prompt, minus its accuracy under its own optimal prompt, for the same task. The quantity is "the shortfall of the transferred" prompt relative to the target's optimum.[^m3] The gap is one-directional in a sense that matters: a prompt can be a poor transfer in one direction and a good one in the other. On HumanEval, the best GPT-5 prompt "reaches 99.39% on GPT-5 but yields 68.70% when transferred to" Llama-3.1-70B-Instruct, whose own optimal prompt scores 79.47%.[^m4] In the reverse direction the Llama-optimal prompt "attains 96.95% on GPT-5, below GPT-5" optimum, a much smaller shortfall.[^m5] The gap is therefore a property of the ordered pair, not a fixed penalty for any prompt.

The drift is not only across vendors. The paper reports the same pattern within one family at different scales, and says that "even closely related models do not share a stable" prompt optimum.[^m6] It gives a figure of "to 50–70% relative loss on xCodeEval" when a prompt optimized for a larger Llama or Qwen model is used on a smaller one.[^m7] The explanation offered is that vendors "train and align models with different corpora, tokenization" and differ in role tags and feedback criteria, which changes how the same instruction is read.[^m8]

The paper separates this from prompt sensitivity. Prompt sensitivity is a local effect of small wording changes; model drifting is described as "rather than a local perturbation effect, model drifting captures a systematic semantic shift" in how a new model reads the same instruction.[^m9] For the asker, the consequence I draw (my inference, not the paper's wording) is that a prompt is a probe calibrated to a particular reader, and a model swap changes the reader.

## Limits

The optimum being compared against is itself a search result. The paper's drift measurement depends on an optimizer that approximates the target's best prompt: "MAP-RPE supports both our drift measurement (by" approximating the optimum.[^m10] A weaker search would lower the target's ceiling and shrink the measured gap, so the size of the drift is only as good as the search. I did not find a sensitivity analysis of this in the text I read (my inference).

The measured tasks are accuracy on code, agentic and planning benchmarks (HumanEval, xCodeEval, SWE-Bench, Terminal-Bench). The paper's own scope is narrower than the general claim: it "currently focuses on optimizing instructions alone" and does not optimize exemplars.[^m11] Drift in open-ended tasks, in prompts with few-shot examples, or in human-judged outputs is not established by this text.

The causes are asserted with examples, not isolated. The text lists tokenization, role tags, corpora and alignment as candidates; it does not vary them one at a time. The paper says more about the phenomenon in an appendix section I did not read, so claims about its shape beyond the cited figures are not checked here.

Drift is shown across models and scales, not across time. The introduction speaks of a model that is "replaced or updated," but the measured cases are different models, not successive versions of one model (my inference from the figures).[^m12]

## Related

- [[model-prompt-matching-bias]] — the same prompt-model mismatch, measured there as a flip in per-prompt ranking between two vision-language backbones rather than as a gap to the target's optimum.
- [[calibration-anchored-prompt-transfer]] — the mapping that tries to close this gap from calibrated source and target prompt pairs on alignment tasks.
- [[prompt-content-over-surface-form]] — a separate account of prompt sensitivity, located in the prompt's content rather than in which model reads it; the paper contrasts drift with exactly this kind of local sensitivity.

[^m1]: arxiv-2512-01420 — "We refer to the performance drift induced by the model substitution as model drifting"
[^m2]: arxiv-2512-01420 — "the same prompt that was previously optimal for the source model often yields suboptimal"
[^m3]: arxiv-2512-01420 — "the shortfall of the transferred"
[^m4]: arxiv-2512-01420 — "reaches 99.39% on GPT-5 but yields 68.70% when transferred to"
[^m5]: arxiv-2512-01420 — "attains 96.95% on GPT-5, below GPT-5"
[^m6]: arxiv-2512-01420 — "even closely related models do not share a stable"
[^m7]: arxiv-2512-01420 — "to 50–70% relative loss on xCodeEval"
[^m8]: arxiv-2512-01420 — "Vendors train and align models with different corpora, tokenization"
[^m9]: arxiv-2512-01420 — "rather than a local perturbation effect, model drifting captures a systematic semantic shift"
[^m10]: arxiv-2512-01420 — "MAP-RPE supports both our drift measurement (by"
[^m11]: arxiv-2512-01420 — "PromptBridge currently focuses on optimizing instructions alone, omitting exemplar or"
[^m12]: arxiv-2512-01420 — "underlying LLM in a system is replaced or updated"
