---
description: "Schema validity and field-level value accuracy are separate measures: frontier MLLMs pass schema validation above 95%, yet no model exceeds 20% on fully matched structured outputs."
aliases: ["schema adherence", "structural fidelity", "field match accuracy", "full structure match", "schema validity versus value accuracy"]
sources: ["arxiv-2511-21750"]
---
# Schema adherence versus field accuracy

A structured output can fail in two places. It can break the schema: a required key is missing, a type is wrong, the nesting does not match. Or it can conform to the schema and still put a wrong value in a field. SO-Bench, a benchmark of visual structured output, splits performance along this line into "schema adherence, structural fidelity, and value-level accuracy".[^c1] The task itself is defined in two parts: the output must "(1) conforms syntactically to S and (2) semantically reflects the information extracted from I and X".[^c2] The two parts are scored separately, which is what makes the split a measurement rather than a description.

## What is measured

The paper reports three numbers. Schema validation accuracy is the share of outputs valid against the schema. Field matching accuracy is a per-field score: the fraction of ground-truth fields that have a matching predicted field, exact or fuzzy, with nested structures matching when their subfields do. Full structure matching accuracy is the share of outputs in which every ground-truth field matches.[^c3]

The matching step is itself a choice. Each primitive field gets a label of exact, fuzzy or ignore, produced by a proprietary model from the image, schema, intent and reference answer, and then the score is computed under that label.[^c4] A fuzzy match is a judgement that a string is close enough, not that it is the same fact.

## What the split shows

At the frontier the two halves come apart. Gemini-2.5-Pro reaches schema validation near 98%, "demonstrating strong schema adherence capabilities."[^c5] On the value side, "no model achieves above 20% on Full Match (fuzzy)."[^c6] The authors trace much of the gap between field match and full match to outputs that are "semantically correct answers for certain fields, which is beyond what fuzzy match can capture."[^c7] So part of the low full-match figure is the metric, and part is the models; the paper does not separate the two.

Depth moves both halves. Across schema depths "both metrics consistently degrade for all models."[^c8] Small models are the sharp case: Intern3.5-VL (4B) shows "substantial performance drops by around 40%" in schema validation at the deepest levels.[^c9]

Enforced decoding shifts the split. The paper evaluates structured output APIs on a subset of about 1.2K samples, "restricted to JSON schemas supported by both OpenAI ... and Gemini ... APIs."[^c10] The authors write that "APIs enforce schema compliance more reliably," but that "they may sometimes constrain content generation, leading to less accurate field-level value predictions."[^c11] In their Table 3, field matching under the API sits below instruction prompting for all six models. My reading of the extracted table, with the column order inferred rather than confirmed, is that schema validation favours the API only for the two GPT-4o models; for the GPT-5 pair and both Gemini models the instruction prompt scores higher on validity too. The paper's sentence is therefore true for the GPT-4o pair and not uniform.

Training moved both halves. Supervised finetuning and RLVR on the same labelling pipeline raised "schema validation and field matching accuracy up to 20% and 13%," respectively.[^c12] The value half is not fixed by the model's tier alone.

Set against [[output-accuracy-format-gap]], the picture changes with the model. There, 7-9B models reached 77-85% task accuracy and 0% output accuracy, so the format half was the bottleneck. Here the frontier models have a near-saturated validity half and the value half binds. My inference, not the papers': which half limits a reply depends on the model's tier and on how the value is matched, so a single "format accuracy" figure hides which one is failing.

## Limits

- The ground truth is machine-made. The authors "rely on frontier models to automatically generate the initial benchmark labels," and despite human and critic review, "there could still be some label errors which cap a model’s performance."[^c13]
- Some fields have more than one correct answer: "correct ground truths for some examples and our current annotation only captures one of them."[^c14] Models may be scored low for correct answers the labels do not contain.
- The field metrics "mainly capture the recall rates of a prediction."[^c15] Extra fields are not penalised: "which predicts many additional fields not existed in ground truth labels could still achieve high FMA or FSMA scores."[^c16]
- The API comparison covers one subset and a few models, and the paper does not say how the API enforces the schema. The phrase "its behavior under constrained decoding" describes the evaluation setting, not a verified mechanism.[^c17] Whether these APIs are token-level masks, as [[constrained-decoding]] describes, is not established here.
- The correlations with other benchmarks are taken over a handful of models, so they show association, not what drives it.

## Related

- [[structured-output]] — the four ways of getting a schema-shaped reply; this note measures what the reply contains once it parses.
- [[output-accuracy-format-gap]] — the product of correctness and parseability; there the format half binds for small models, here the value half binds for frontier ones.
- [[capacity-dependent-format-tax]] — the same depth and complexity gradient, read there as a cost to reasoning; SO-Bench measures it as a drop in validity and value accuracy with no reasoning task.
- [[constrained-decoding]] — the mechanism that guarantees validity by construction; the API result above is the nearest measure of its content cost.
- [[format-restriction-effect]] — the broader question of what requiring a format does to answer quality.

[^c1]: arxiv-2511-21750 — "schema adherence, structural fidelity, and value-level accuracy"
[^c2]: arxiv-2511-21750 — "(1) conforms syntactically to S and (2) semantically reflects the information extracted from I and X"
[^c3]: arxiv-2511-21750 — "We report the following three metrics in our experiments."
[^c4]: arxiv-2511-21750 — "one of {exact, fuzzy, ignore}"
[^c5]: arxiv-2511-21750 — "demonstrating strong schema adherence capabilities"
[^c6]: arxiv-2511-21750 — "no model achieves above 20% on Full Match (fuzzy)"
[^c7]: arxiv-2511-21750 — "semantically correct answers for certain fields, which is beyond what fuzzy match can capture"
[^c8]: arxiv-2511-21750 — "both metrics consistently degrade for all models"
[^c9]: arxiv-2511-21750 — "substantial performance drops by around 40%"
[^c10]: arxiv-2511-21750 — "restricted to JSON schemas supported by both OpenAI"
[^c11]: arxiv-2511-21750 — "APIs enforce schema compliance more reliably"
[^c12]: arxiv-2511-21750 — "schema validation and field matching accuracy up to 20% and 13%"
[^c13]: arxiv-2511-21750 — "there could still be some label errors which cap a model’s performance"
[^c14]: arxiv-2511-21750 — "correct ground truths for some examples and our current annotation only captures one of them"
[^c15]: arxiv-2511-21750 — "mainly capture the recall rates of a prediction"
[^c16]: arxiv-2511-21750 — "which predicts many additional fields not existed in ground truth labels could still achieve high FMA or"
[^c17]: arxiv-2511-21750 — "its behavior under constrained decoding"
