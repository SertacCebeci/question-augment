---
description: "Time-bearing facts are rewritten as relation(subject, object, start, end) predicates and kept only if their interval overlaps the question's; a language model then reasons over those predicates."
aliases: ["normalized temporal predicates", "temporal predicate encoding", "symbolic temporal facts"]
sources: ["arxiv-2512-07218"]
---
# Symbolic temporal representation

Temporal information in natural language is hard to reason over because it is implicit and varied. A date can be spelled several ways, and a period can be stated in one sentence and inferred from another. The mechanism described in NeSTR works on that input before any inference happens. It is "converting raw temporal context into structured symbolic representations."[^s1] Each fact becomes a quadruple, relation(subject, object, start, end), with start and end as normalized numeric timestamps. The worked example turns "From 1946 to 1949, Jaroslav Pelikan worked at Valparaiso University" into works_for(Jaroslav Pelikan, Valparaiso University, 1946, 1949). The paper's claim for this step is that it "preserves temporal boundaries in a normalized format."[^s2]

The second part is a deterministic filter. Given a question with its own interval, a fact is kept when the two intervals overlap. The paper states the rule as a condition on the start and end points, so a fact is relevant when its start is no later than the question's end and its end is no earlier than the question's start.[^s3] A further filter keeps only facts whose subject matches the subject named in the question, which is written as "To further constrain inference to the correct subject."[^s4] Both filters act on the timestamps, not on the wording of the sentence, so once the predicates exist the selection of facts does not depend on how the model reads the prose.

Only after this filter does a language model reason. The paper says the model operates "not over raw contexts but directly over the aforementioned" symbols.[^s5] The predicates are the reasoning space: the model matches and compares them, and the paper describes the symbols as a "constrained and interpretable reasoning space."[^s15]

What the ablation measures. The variant "w/o Symbol" removes the representation and "replaces symbolic reasoning with purely" natural-language inference.[^s16] On TimeQA-Hard the paper reports that "EM drops from 81.7 to 74.2."[^s6] The symbolic-only variant, which drops the neural layer, reaches "achieving 88.2 EM" on TimeQA-Hard,[^s14] but on the multi-hop TempReason-L2 its EM falls from 80.8 to 70.5, and the paper concludes that "neural components are essential for generalization and deeper compositional reasoning."[^s7] So the two parts of the mechanism show different strengths: the symbolic layer carries direct, single-fact lookups, and the neural layer carries chains longer than one fact.

The format of the symbols matters less than their presence. The paper reports that "introducing structured symbolic inputs" helps "regardless of format."[^s8] It also compares first-order logic with Python-style dictionaries, and finds that "FOL yields stronger performance on" TimeQA-Hard while the dictionary format does slightly better on TempReason-L3.[^s9] The transfer claim is therefore about structure, not notation.

## Limits

- The ablation is reported "using gpt-4o-mini."[^s10] The other variants are not shown on other models in the slices read, so the size of the symbolic effect on open models is not established here.
- The setting is zero-shot: "Our work specifically targets the zero-shot setting."[^s11] No fine-tuned variant of the symbolic step was tested.
- The predicates are produced from text, and the paper names the hard part as "accurately extracting and interpreting temporal expressions in natural language."[^s12] The slices read do not measure extraction error separately, so an error made while writing the predicate is not separated from an error made while reasoning over it. (My inference.)
- The paper calls its algorithm "a simplified pseudocode illustration" and points to the full prompt on GitHub.[^s13] The exact conversion rules were not read, so the claim is about the described design, not the prompt.
- The paper's own numbers show the symbolic-only variant above the full model on TimeQA-Hard (88.2 EM against 81.7). The paper does not reconcile that with its claim that the symbolic layer is key. (My inference from the quoted figures.)
- Open intervals, unstated end dates and overlapping but contradictory facts are not discussed in the slices read; whether the overlap rule handles them is untested here.

## Related

- [[neurosymbolic-text-to-logic-retrieval]] — the same text-to-logic translation step, used there for image retrieval rather than for time; both name the translation as the point where errors enter.
- [[temporal-constraint-taxonomy]] — enumerates the pairwise relations between intervals; the overlap test used here is one of the relations such a taxonomy has to cover.
- [[symbolic-grounded-depth-gap]] — a different symbolic-to-text loss: there, a graph path fails to survive realization in prose, while here the symbolic layer is what the multi-hop chains lack.

[^s1]: arxiv-2512-07218 — "converting raw temporal context into structured symbolic"
[^s2]: arxiv-2512-07218 — "preserves temporal boundaries in a normalized format"
[^s3]: arxiv-2512-07218 — "identifies whether a fact fi is relevant to a query based on interval overlap"
[^s4]: arxiv-2512-07218 — "To further constrain inference to the correct subject"
[^s5]: arxiv-2512-07218 — "not over raw contexts but directly over the aforementioned"
[^s6]: arxiv-2512-07218 — "EM drops from 81.7 to 74.2"
[^s7]: arxiv-2512-07218 — "neural components are essential for generalization and deeper compositional reasoning"
[^s8]: arxiv-2512-07218 — "regardless of format"
[^s9]: arxiv-2512-07218 — "FOL yields stronger performance on"
[^s10]: arxiv-2512-07218 — "Ablation results on four temporal QA benchmarks using gpt-4o-mini"
[^s11]: arxiv-2512-07218 — "Our work specifically targets the zero-shot setting"
[^s12]: arxiv-2512-07218 — "accurately extracting and interpreting temporal expressions in natural language"
[^s13]: arxiv-2512-07218 — "This is a simplified pseudocode illustration"
[^s14]: arxiv-2512-07218 — "achieving 88.2 EM"
[^s15]: arxiv-2512-07218 — "constrained and interpretable reasoning space"
[^s16]: arxiv-2512-07218 — "replaces symbolic reasoning with purely"
