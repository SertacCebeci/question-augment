---
description: "Atomic claims from a diagnostic rationale are each labelled against retrieved knowledge-graph triplets and pooled by a sigmoid, so unsupported claims lower the score."
aliases: ["KAS", "Knowledge Attribution Score", "triplet-grounded claim attribution", "claim-to-triplet attribution score"]
sources: ["arxiv-2511-17947"]
---
# Knowledge attribution score

The score asks whether each claim in a model's reasoning is supported by a structured source, and it asks this of the reasoning, not of the final answer. The passage is first reduced to named entities, which are used to retrieve a set of triplets from a knowledge graph built from the disorder criteria. The passage is then split by an LLM into claims, and the paper's step is "decomposed into atomic, verifiable claims": a narrative becomes a list of items that can each be checked.[^c1]

Each claim gets two numbers. The first is a symbolic label from the retrieved triplets, a "Triplet-Based Attribution Classification" with four categories (attributable, extrapolatory, no attribution, contradictory) and a value that runs from −1 to 2 in the extracted layout.[^c2] The pairing of each label to its value is not clear from the text extraction, so I do not state it. The second is a triplets match score, a weighted sum of two terms: the cosine similarity between the claim and the retrieved triplets, and "the entity-level precision/recall between" the claim and the matched entities.[^c3] The weight between the two is set to 0.5, chosen by inspecting the score distributions and trying a set of configurations, not derived from a stated principle.[^c4] The claim's weight is the product of its label and its match score (my reading of the paper's Eq. 3), and the aggregate is a sigmoid of the sum over claims.[^c5] A rationale with many supported claims pushes the sum up, and a contradicted claim pushes it down.

What the aggregate is for is stated by the authors as a distinction between kinds of reasoning. The sigmoid "allows the KAS to effectively distinguish flawed" reasoning from valid justifications.[^c5] The contrast they draw is with claim verification that "usually treat claims in isolation", which the paper answers with a joint check of the reasoning chain.[^c6] In this design the knowledge attribution is the claim-level half of that joint check. The other half is a rule-based grade, described in [[criteria-conformance-score]].

On the paper's data, the combined score separates correct from incorrect outputs: "higher across prompting strategies, while incorrect cases receive" markedly lower values.[^c7] That figure is for the combined score, not for the knowledge attribution term alone, so it does not isolate this component.

## Limits

- The claim decomposition and the labelling are both done by LLMs. The sections read do not report how often these labels agree with a human's judgement of whether a claim is attributable. The score can only be as good as the decomposition, and that is my inference.
- The reference the score is compared with is not a clinician's label. The paper evaluates "on the D4 dataset with pseudo-labels", and the pseudo-labels come from a model: "silver-standard labels for the D4 dataset by applying DSM-5".[^c8] A high score tracks agreement with a model-made label as much as with the diagnosis.
- A claim the retrieved subgraph does not contain comes back as no attribution, whether the claim is false or only missing from the graph. The labels do not separate those two cases, which is my reading of the label set.
- The weights (0.5 on similarity, the sigmoid's sensitivity) were chosen on the paper's own data. The ablation on these parameters is in a part of the paper I did not read in full, so I do not report its effect.
- The retrieval step is a graph walk (WoolNet) over triplets extracted from DSM-5 text. How much of the criteria the graph actually covers is not reported in the sections read.
- The sections read do not test the score on claims about anything other than depression-related disorders.

## Related

- [[criteria-conformance-score]] — the rule-based half of the same combined score; it grades the procedure against the criteria, where this grades each claim against triplets.
- [[gap-claim-attribution-check]] — also checks a claim against a text, but asks whether a named gap is present in the passages, not whether a claim is supported by structured triplets.
- [[evidence-verified-identification]] — replays a final guess against the dialogue, the same verify-against-evidence move applied to an answer rather than to each claim.
- [[checklist-diagnostic-decomposition]] — also splits a judgement into independent factors answered by an LLM, but to classify, not to score a rationale.

[^c1]: arxiv-2511-17947 — "decomposed into atomic, verifiable claims"
[^c2]: arxiv-2511-17947 — "Triplet-Based Attribution Classification"
[^c3]: arxiv-2511-17947 — "the entity-level precision/recall between"
[^c4]: arxiv-2511-17947 — "we set it to 0.5"
[^c5]: arxiv-2511-17947 — "This allows the KAS to effectively distinguish flawed"
[^c6]: arxiv-2511-17947 — "While prior claim verification methods usually treat claims in isolation"
[^c7]: arxiv-2511-17947 — "higher across prompting strategies, while incorrect cases receive"
[^c8]: arxiv-2511-17947 — "silver-standard labels for the D4 dataset by applying DSM-5"
