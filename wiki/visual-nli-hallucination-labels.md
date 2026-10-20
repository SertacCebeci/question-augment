---
description: "Hallucination labels can come from a judge VLM that rates an answer against a gold reference as entailment, contradiction or uncertainty, with the judge discarded at inference time."
aliases: ["Visual-NLI labels", "model-driven hallucination supervision", "LLM-as-a-judge labels for VQA hallucination", "judge-derived hallucination labels"]
sources: ["arxiv-2601-00269"]
---
# Visual-NLI hallucination labels

Supervised hallucination detection needs labels, and labelling every answer by hand is costly. One route treats labelling as a visual natural-language inference problem. The premise is the image, the question and the reference answer; the hypothesis is the answer the target model actually gave. A pretrained vision-language judge then returns a three-way distribution over entailment, contradiction and uncertainty for that premise and hypothesis.[^c1] The paper presents this as a structured Visual-NLI protocol, and as extending the LLM-as-a-Judge paradigm to VQA.[^c2]

The mechanism is short. The judge is queried for R independent rounds, "we perform R independent judging rounds and average" the probabilities, which damps the judge's own sampling noise.[^c3] The hallucination probability is the averaged mass of the two non-entailment outcomes, contradiction plus uncertainty. The answer is labelled a hallucination when that mass exceeds the averaged entailment probability.[^c4] The paper counts uncertainty as a hallucination on purpose: "indicators of hallucination, as they reflect failures of visual" grounding or over-commitment beyond the evidence.[^c4]

What makes the labels "model-aware" is that the judge sees the answer the target model produced under low-temperature decoding, not a reference model's answer. The authors put it this way: the judge "is not a detached oracle; it evaluates answers in the context of the target model's reasoning".[^c5] The labels therefore mark the model's own failure modes, and they are model-dependent in the same way the detector is (see [[single-pass-internal-signal-detector]]).

The judge is a dataset-construction tool, not an inference component. "We emphasize that the judge model is only used during" dataset construction, and "at inference time, the proposed hallucination detector operates independently".[^c6] Once the detector is trained, the judge's cost is paid once, not per query.

How the labels were checked. The authors draw a small sample for human review, 100 instances per dataset, and treat it as "a quality control mechanism rather than" a label source.[^c7] Agreement between human and judge labels is reported as "achieving agreement scores in the range of 0.950–0.990", with Cohen's kappa and MCC "consistently high across datasets".[^c8] The text also says that items with ambiguous questions or problematic reference answers were marked and left out of the agreement analysis.[^c9]

## Limits

- The human check is small: 100 instances per dataset, drawn at low temperature from one model's answers. High agreement on that sample says the judge tracks human judgment there; it does not bound the label error on the training set.
- Labels depend on the reference answer. The premise is the gold answer, so a wrong or incomplete reference becomes a wrong label. The paper excludes flagged references in its check, not in its training labels, as far as the excerpt shows.
- Counting uncertainty as hallucination is a choice. A correct answer that the image cannot verify is labelled a hallucination. This is defensible for the paper's faithfulness target, but it is not the same object as factual error, and the label would shift if the choice were reversed.
- The judge's own biases carry into the labels (see [[llm-judge-biases]]). The paper's robustness step, repeated rounds, reduces stochastic variance in the judge; it does not remove systematic bias.
- The paper also describes a reliability score over labels, from repeated verification, stochastic generation and self-reflection, to weight training instances. I did not read that section (supplementary), so I make no claim about its effect.

## Related

- [[single-pass-internal-signal-detector]] — the detector trained on these labels; it never calls the judge
- [[llm-judge-validation-gap]] — the general question of whether judge verdicts track the thing they are meant to measure
- [[llm-judge-biases]] — systematic judge preferences that would pass into any label this way

[^c1]: arxiv-2601-00269 — "is then queried to assess the semantic relationship between the premise and the hypothesis"
[^c2]: arxiv-2601-00269 — "extending the LLM-as-a-Judge paradigm to VQA"
[^c3]: arxiv-2601-00269 — "we perform R independent judging rounds and average"
[^c4]: arxiv-2601-00269 — "indicators of hallucination, as they reflect failures of visual"
[^c5]: arxiv-2601-00269 — "not a detached oracle; it evaluates answers in the context of"
[^c6]: arxiv-2601-00269 — "We emphasize that the judge model is only used during"
[^c7]: arxiv-2601-00269 — "a quality control mechanism rather than"
[^c8]: arxiv-2601-00269 — "achieving agreement scores in the range of 0.950–0.990"
[^c9]: arxiv-2601-00269 — "problematic ground-truth references are explicitly marked and"
