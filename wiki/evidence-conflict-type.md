---
description: "Sources that disagree differ in kind, not only in content: complementary, opinion, outdated and false sources each call for a different answer shape, so the kind has to be named first."
aliases: ["conflict type taxonomy", "CONFLICTS conflict types", "Dragged into Conflicts taxonomy", "evidence conflict typology", "source conflict type"]
sources: ["arxiv-2512-16795"]
---
# Evidence conflict type

When retrieved sources disagree, the disagreement has a kind, and the kind fixes what a good answer looks like. Cattan et al. introduced "a taxonomy of conflict types and defining expected model behaviors for each conflict type."[^c1] The paper read here works with five classes, each paired with an expected answer. The pairing is the substance. The class is not a label for error analysis; it is a rule for the shape of the response. For sources that agree, the expected answer is "a unified and concise answer that synthesizes all content accurately."[^c3] For complementary sources the answer integrates: "Integrate all valid details to produce a richer," a fuller response.[^c4] For disagreement over viewpoints, experimental results or interpretations, the answer presents the sides, "Present each viewpoint clearly, describe the" nature of the disagreement, and does not pick one "a side unless supported by strong evidence."[^c5][^c6] For outdated sources the answer prefers the newer material and says so, "explicitly noting that certain sources are outdated."[^c7] For misinformation the answer corrects it: "Reject or correct the misinformation, provide" verified facts and explain the error.[^c8]

The class belongs to the set of retrieved sources, not to any one of them. The pipeline first gives each snippet a "verdict {supports, partially supports, irrelevant}"[^c9] and then "aggregates all micro-level judgments and provides a reason" to name the overall type.[^c10] My reading: two documents can each be sound and still disagree in a way that only the pair or the group exhibits, so the type is a property of the evidence as a whole. The paper does not test that reading separately.

The type is meant to govern the output. The generation step is instructed to "ensure that the final output adheres to the expected behavior associated with the given conflict" type.[^c11]

What the paper measures about the type is modest. Giving base models the gold type, in the oracle setting, moved behavioural adherence only a little: "Mistral improves from 0.630 to 0.648, and Qwen" went from 0.074 to 0.296 in the end-to-end contrast, and the authors read it this way: "the gains remain modest, indicating that" base models do not turn explicit conflict structure into behaviour without training.[^c12][^c13] Inferring the type is the harder half. Baseline models "have an even stronger bias, usually defaulting to" no conflict, and "Conflicting opinions" is "the hardest category to identify."[^c14][^c15]

## Limits

- The five classes and their expected behaviours are inherited from the CONFLICTS data: "No additional classification is performed."[^c16] The paper tests whether models match these behaviours, not whether the behaviours are the right ones for a user. Adherence is agreement with a rubric.
- The training labels were produced by an LLM and then reviewed by people. "on human-verified annotations introduces a degree of subjectivity in verdict interpretation and"[^c17] the authors say, so the rubric's own judgements are part of the result.
- The scale is small: 539 queries, and "only 54 queries are available in" the test split.[^c18] Two 7B models and one dataset were tested. Nothing here shows the classes transfer to open web retrieval, where the type is itself a prediction and is the weak link.
- The refusal side is near ceiling (F1-GR = 1.000 after fine-tuning), but the authors warn that the test split has few refusal cases: "required instances, which likely amplifies the observed ceiling performance."[^c19]
- Adherence is scored by an LLM judge against the type's template, and the paper concedes the judge "inherits the biases and inconsistencies of the judging model" it runs on.[^c20]
- The earlier list in the paper's introduction names the classes differently, "temporal, debatable, misinformation, and complementary".[^c2] My reading is that "temporal" and "debatable" correspond to the later "outdated" and "conflicting opinions", but the paper does not say the mapping is exact.

## Related

- [[context-grounded-vs-reconciled-reasoning]] — the two reasoning modes over retrieved context; that note is about the sources against the model's own knowledge, this one is about the sources against each other.
- [[source-credibility-hierarchy-in-knowledge-conflicts]] — which of two conflicting contexts a model trusts; here the type, not a credibility ranking, is what sets the answer.
- [[parametric-suppression]] — a conflict between retrieved evidence and what the model memorised, a different conflict pair from the one typed here.
- [[behavioral-evaluation-without-correctness]] — judging an answer by its traceable behaviour when correctness is not checkable; the paper's adherence score is a behaviour check against a type-specific template.
- [[ambiguity-taxonomy]] — the same move on the question side: naming the kind of ambiguity fixes the shape of the question; here the kind sits in the sources.
- [[abstention]] — refusal as a third output; the paper's refusal trigger is evidence-based, not a confidence threshold.

[^c1]: arxiv-2512-16795 — "conflict types and defining expected model behaviors for each conflict type."
[^c2]: arxiv-2512-16795 — "proposed a taxonomy of conflict types, including temporal, debatable, misinformation, and"
[^c3]: arxiv-2512-16795 — "Return a unified and concise answer that synthesizes all content accurately."
[^c4]: arxiv-2512-16795 — "Integrate all valid details to produce a richer,"
[^c5]: arxiv-2512-16795 — "Present each viewpoint clearly, describe the"
[^c6]: arxiv-2512-16795 — "a side unless supported by strong evidence."
[^c7]: arxiv-2512-16795 — "explicitly noting that certain sources are outdated."
[^c8]: arxiv-2512-16795 — "Reject or correct the misinformation, provide"
[^c9]: arxiv-2512-16795 — "verdict {supports, partially supports, irrelevant}"
[^c10]: arxiv-2512-16795 — "all micro-level judgments and provides a reason"
[^c11]: arxiv-2512-16795 — "ensure that the final output adheres to the expected behavior associated with the given conflict"
[^c12]: arxiv-2512-16795 — "Mistral improves from 0.630 to 0.648, and Qwen"
[^c13]: arxiv-2512-16795 — "the gains remain modest, indicating that"
[^c14]: arxiv-2512-16795 — "have an even stronger bias, usually defaulting to"
[^c15]: arxiv-2512-16795 — "the hardest category to identify."
[^c16]: arxiv-2512-16795 — "No additional classification is performed."
[^c17]: arxiv-2512-16795 — "on human-verified annotations introduces a degree of subjectivity in verdict interpretation and"
[^c18]: arxiv-2512-16795 — "only 54 queries are available in"
[^c19]: arxiv-2512-16795 — "required instances, which likely amplifies the observed ceiling performance."
[^c20]: arxiv-2512-16795 — "biases and inconsistencies of the judging model"
