---
description: "Splitting a hallucination rate by the verification stage that catches it (wrong entity vs. wrong facts about the right entity) shows whether a model lacks breadth or depth of knowledge."
aliases: ["HaluBOK and HaluDOK", "breadth of knowledge versus depth of knowledge hallucination rate"]
sources: ["arxiv-2602-19643"]
---
# Breadth-depth hallucination decomposition

A single hallucination rate says that a model is wrong, not why. Robertson et al. (2026) ask each question about one focal entity from a knowledge graph, with a compound question over three of its relations. They verify the long-form answer in two layers and report the hallucination rate by the layer that catches it.

## Mechanism

Layer one is an abstention filter plus an entity-level check of the response against the entity's description. A response failing it counts as a breadth failure. Layer two checks the remaining responses fact by fact against graph triples.[^c1]

HaluBOK is the share of non-abstained responses flagged at the entity level; a high value means the model lacks fundamental knowledge of the content, so limited breadth. HaluDOK is incorrect facts divided by the maximum attainable score, among responses that passed layer one; a high value means the model knows the entity but not the details asked.[^c2]

Measured on 25 models, HaluBOK fell from 54.75% (8-32B models) to 11.91% (larger proprietary models), while HaluDOK fell only about 24.59%. The authors read this as larger models being better at deciding what to discuss while still failing to retain precise details.[^c3] The single aggregate rate would have blended these two different failures.

Abstention is handled apart from both: two models with equal entity-level breadth differed in hallucination rate (30.00% vs 58.67%) because one abstained more, and some models declined about half the questions.[^c4]

## Limits

- The split is only as good as the filters: agreement with human judgment was 79.19% at entity level and 87.74% at fact level, so the breadth label is the noisier one.[^c5]
- "Breadth" here means recognizing one randomly drawn entity, not coverage across topics; reading a failure as missing knowledge rather than a retrieval slip is the authors' interpretation, not tested.
- The denominators differ (responses vs. attainable points), so the two rates are not directly comparable in size. That is my observation.
- Fact-level correctness depends on the graph's triples being complete and right.
- Tested on Wikidata/Wikipedia-style entities only.

## Related

- [[unnecessary-abstention-aware-recall]] — also scores abstention separately from correctness
- [[interpretation-breadth-depth-asymmetry]] — a different breadth/depth contrast, in interpretation
- [[post-cutoff-corpus-benchmark-isolation]] — another guard against stale static benchmarks

[^c1]: arxiv-2602-19643 — "an abstention filter to detect expressions of uncertainty, an initial entity-level filter to identify semantic misalignment with the entity, and a final fact-level check to verify correctness against grounded facts"
[^c2]: arxiv-2602-19643 — "A high rate indicates that the LLM lacks fundamental knowledge of the assessment content, suggesting limited breadth of knowledge."
[^c3]: arxiv-2602-19643 — "larger models excel at determining what to discuss but still struggle to retain the precise details of that topic"
[^c4]: arxiv-2602-19643 — "Llama-3.1-8B has a higher abstention rate, resulting in a significantly lower hallucination rate of 30.00%, compared to Gemma2-9B of 58.67%"
[^c5]: arxiv-2602-19643 — "achieving 79.19% and 87.74% agreement with human judgment, respectively"
