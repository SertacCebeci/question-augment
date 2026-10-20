---
description: "Wrapping each candidate finding in numbered tags inside the report text lifted an 8B model's zero-shot macro-F1 above tag-free 1- and 5-shot prompts, mainly through precision."
aliases: ["lesion tagging", "inline candidate markers", "tagged-span input"]
sources: ["arxiv-2512-05537"]
---
# Candidate-span tagging in the input

A clinical report can repeat the same word in several places, and only some of those places are the finding a question is about. The incidentaloma pipeline handles this by changing the input rather than the model: each candidate lesion span is wrapped in a numbered XML-style tag, and the surrounding text is left intact.[^c1] The candidates come from an upstream extractor, so the model is handed a marked set of spans instead of having to find them in the prose.

The authors give the motive directly: "Without tags, it can be difficult to identify the lesion of interest."[^c2] The concern is specific. A term such as "nodule" can recur in several contexts within one report, and the tag fixes which occurrence the decision concerns.

What was measured is an ablation on one model. For Llama 3.1-8B Instruct, a zero-shot prompt with tags scored higher macro-F1 "than all 0-shot, 1-shot and 5-shot settings" run without tags.[^c3] From this the authors conclude that "structural cues can be more beneficial than additional examples."[^c4] The gain is attributed to precision: "The improvement was primarily driven by higher precision with comparable recall."[^c5] They read this as "the tags helped models focus on the correct lesion spans."[^c6]

Mechanism, in my reading: a tag is a localisation signal. It adds no fact the model lacks; it removes the need to resolve which mention is meant. That would lower false positives on mentions outside the candidate set while leaving recall where it was, which is the pattern the authors report. The same numbering also serves review: "Numbered lesion tags support detailed error analysis."[^c7] This reading fits the precision result but the paper does not test it separately.

## Limits

- The ablation uses one model, Llama 3.1-8B Instruct, and one task: "Our ablation study using the Llama 3.1-8B Instruct model".[^c8] I found no untagged ablation for the GPT models in the text I read, so the tag effect is not shown for them.
- Tag quality is extractor quality. The lesion spans came from PL-Marker++, whose anatomy inference "was sometimes limited."[^c9] A candidate the extractor misses is simply untagged, and the ablation does not separate the tagging effect from extraction quality.
- The precision and recall figures behind "comparable recall" are not in the passages I read, so the size of the precision change is unknown here.
- Whether tags help when the candidate spans are ones the model would find unaided is untested.

## Related

- [[attribute-pinning-in-prompt]] — the next step on the same tagged input: each tag is bound to an attribute.
- [[memory-induced-unawareness]] — a structural marker in the prompt, there for what remains unfilled rather than for which span is the target; the same lever applied to a different object.

[^c1]: arxiv-2512-05537 — "were enclosed with XML-format tags using lesion information extracted by PL-Marker++"
[^c2]: arxiv-2512-05537 — "Without tags, it can be difficult to identify the lesion of interest"
[^c3]: arxiv-2512-05537 — "inputs with lesion tags achieved higher macro F1-score than all 0-shot, 1-shot and 5-shot settings"
[^c4]: arxiv-2512-05537 — "structural cues can be more beneficial than additional examples"
[^c5]: arxiv-2512-05537 — "The improvement was primarily driven by higher precision with comparable recall"
[^c6]: arxiv-2512-05537 — "the tags helped models focus on the correct lesion spans"
[^c7]: arxiv-2512-05537 — "Numbered lesion tags support detailed error analysis"
[^c8]: arxiv-2512-05537 — "Our ablation study using the Llama 3.1-8B Instruct model"
[^c9]: arxiv-2512-05537 — "its inference was sometimes limited"
