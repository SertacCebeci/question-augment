---
description: "A generated reference that several models, or several replications of one model, produce independently is far more likely real; fabricated references are stochastic and rarely recur."
aliases: ["cross-model citation convergence", "citation agreement as verification"]
sources: ["arxiv-2603-03299"]
---
# Citation recurrence as an authenticity signal

When a model is asked to cite, a reference it invents has no external anchor, so it differs from run to run and from model to model. A real reference is anchored in training data and is reproduced. In an audit of 10 commercial LLMs, the share of unique title strings that matched the verification pipeline rose with the number of models producing them: 16.5% for titles cited by one model, 87.4% for two models, and 95.6% for three or more, a 5.8-fold gain.[^c1] The same holds inside one model across three replications: 28.6% matched when a citation appeared in one replication, 88.9% when it recurred in two or more.[^c2] The authors read both as one mechanism: hallucinated citations are stochastic and variable, real ones stable and convergent.[^c3]

For asking and answering, the point is that agreement across independent samples carries information about existence without any external lookup. An answerer can treat a reference (or, by my extension, any specific factual token string) that is not reproduced across samples as unsupported. A questioner can obtain this check by asking the same thing several times or of several models and comparing.

Family structure confounds the cross-model count. Pairwise Jaccard overlap of cited titles was mostly 0.15 to 0.25 but higher within families (0.540 for GPT-5-mini and GPT-5-nano), which the authors attribute to shared training.[^c4] Models from one family therefore do not count as independent witnesses.

## Limits

- The "real" label comes from the authors' own matching pipeline, which itself recovered 8 of 75 sampled "hallucinated" citations as real (10.7%), so the match rates are noisy.
- Recurrence of a wrong but popular reference (a systematic error) is not excluded; the data show a rise in match rate, not a guarantee.
- Cross-model counts mix independent and family-correlated models; the study does not separate them in the match rate.
- The classifier built from these signals (AUC 0.876 cross-validated, 0.834 leave-one-model-out) is reported in the abstract; I did not read its details, so I make no claim about it.[^c5]
- Tested on four academic domains and citation strings only.

## Related

- [[cross-model-answer-disagreement-entropy]] — disagreement across models as an uncertainty measure; the same idea in reverse
- [[self-consistency-difficulty-score]] — agreement across samples of one model
- [[cross-provider-judge-ensemble]] — independence across providers matters for ensembles
- [[phantombench]] — abstention on non-existent entities, a neighbouring fabrication measure

[^c1]: arxiv-2603-03299 — "For titles cited by two models, this rises to 87.4%."
[^c2]: arxiv-2603-03299 — "when the same citation recurs in two or more replications, the match rate rises to 88.9%"
[^c3]: arxiv-2603-03299 — "hallucinated citations are"
[^c4]: arxiv-2603-03299 — "GPT-5-mini and GPT-5-nano share a Jaccard index of 0.540"
[^c5]: arxiv-2603-03299 — "achieving AUC 0.876 in crossvalidation and 0.834 in leave-one-model-out generalization"
