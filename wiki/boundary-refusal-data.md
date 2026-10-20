---
description: "Refusals that are safe but sit near the edge of harmful topics can erode a student's safety when fine-tuned on; dropping them reversed the safety loss for two of three models tested."
aliases: ["boundary refusals", "boundary data", "near-edge safe refusals", "boundary examples in safety fine-tuning"]
sources: ["arxiv-2602-11157"]
---
# Boundary refusal data

A boundary refusal is a reply that is safe but lies near the edge of harmful content. The paper's examples are multiple-choice questions that set safe against unsafe responses, controversial historical material, and careful navigation of unsafe roleplay scenarios. Its definition is data "that is technically safe but exists near the edge of harmful concepts."[^b1] The claim is that such data, used as a fine-tuning target, can wear down the refusals the model already has. The mechanism the paper proposes is that fine-tuning on this kind of material "can erode a model’s guardrails by confusing its internal safety classifiers."[^b2] That account is taken from a cited work; the paper does not probe the classifiers itself, so the mechanism is its hypothesis.

The setting is response-based distillation. A teacher, OpenAI o1-mini, answers jailbreak prompts in ten languages, and student models are fine-tuned on the teacher's refusals with LoRA. Standard fine-tuning on those "safe" refusals increased jailbreak success in all three students, "up to 16.6 percentage points."[^b3] To see how much of the refusal set is boundary material, the paper used Gemma-3-12B-IT as a judge. It "graded 33.1% of o1-mini’s 28,190 refusal responses as ‘boundary’ examples,” and 57.2% as simple refusals.[^b4]

The test that links boundary data to the damage is a data intervention. In a preliminary run, the authors fine-tuned on a revised set that excluded the boundary refusals. Their own summary is that removing this data "mitigates or even reverses the safety failure."[^b5] In the table the paper reports, "Qwen3-8B and Meta-Llama-3-8B-Instruct showed a reversal," with JSR falling below baseline, while "Gemma-2-2B-IT achieved a positive but considerably smaller JSR increase of +6.98%."[^b6] So the intervention helped two of the three students and did not remove the harm for the third.

The paper does not treat boundary data as the only cause. It names three factors, boundary data, the amplification of teacher vulnerabilities, and catastrophic forgetting, and says they "are not mutually exclusive"; "our analysis suggests a compounding effect."[^b7] The purification is the only test in the text that isolates the boundary factor. The other two are argued from the teacher's 3.1% baseline and from a drop in math reasoning, and are not separately measured.

## Limits

- **The boundary label is one judge's reading.** Gemma-3-12B-IT assigned the labels. The paper's human check covers its evaluation judge, GPT-4o, on a 300-prompt sample; the text read does not check the labelling judge against human raters. The 33.1% share is that judge's count, not a measured property of the data.
- **The removal experiment is preliminary.** The paper's own term is "preliminary data purification."[^b8] It was run once, on one dataset, and the table reports one representative run. The text read does not show a control that removes an equal number of randomly chosen refusals, so it is not shown that the effect is specific to boundary content rather than to the smaller or different set.
- **It does not restore reasoning.** Models trained on simple refusals still lost accuracy on GSM8K. The paper concludes that "the reasoning degradation is a separate roadblock."[^b9]
- **It does not fix every model.** Gemma-2-2B-IT still rose after purification, and the paper's size ablation reports that "The Gemma model family, again, saw disproportionately high JSR increases."[^b10] The benefit is model-dependent.
- **Causal share is open.** Because the paper's three factors are "not mutually exclusive," the purification gain cannot be assigned to boundary data alone. The paper itself calls the result a route, writing that "our results reveal a data-centric solution to the safety erosion."[^b11]
- **Languages are mixed in.** The distillation set spans ten languages, and the boundary share was computed over all of them. Whether the boundary share differs by language is not reported in the text read.

## Related

- [[knowledge-distillation]] — the response-based, hard-label form in which these refusals are the training target.
- [[zero-alignment-distillation]] — the opposite case: distilling only benign completions, with no refusals, also loses safety; here refusals are present and safety still falls.
- [[multilingual-safety-divide]] — the gap between high- and low-resource languages that this distillation was meant to narrow.
- [[refusal-signal-dimensionality]] — how a refusal is carried inside the model, which bears on whether training on refusal text can move it.

[^b1]: arxiv-2602-11157 — "that is technically safe but exists near the edge of harmful concepts"
[^b2]: arxiv-2602-11157 — "can erode a model’s guardrails by confusing its internal safety classifiers"
[^b3]: arxiv-2602-11157 — "up to 16.6 percentage points"
[^b4]: arxiv-2602-11157 — "graded 33.1% of o1-mini’s 28,190 refusal responses as ‘boundary’ examples and 57.2% as"
[^b5]: arxiv-2602-11157 — "mitigates or even reverses the safety failure"
[^b6]: arxiv-2602-11157 — "Qwen3-8B and Meta-Llama-3-8B-Instruct showed a reversal,"
[^b7]: arxiv-2602-11157 — "our analysis suggests a compounding effect."
[^b8]: arxiv-2602-11157 — "Through a preliminary data purification experiment"
[^b9]: arxiv-2602-11157 — "the reasoning degradation is a separate roadblock"
[^b10]: arxiv-2602-11157 — "The Gemma model family, again, saw disproportionately high JSR increases"
[^b11]: arxiv-2602-11157 — "our results reveal a data-centric solution to the safety erosion"
