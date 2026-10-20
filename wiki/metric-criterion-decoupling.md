---
description: "NLG papers pick metrics and quality criteria independently, each by popularity; task-distinctive metrics and criteria are rarely paired, so a score cannot be tied to what it measures."
aliases: ["metric-criteria mapping problem", "metric inertia"]
sources: ["arxiv-2601-07648", "arxiv-2511-18739"]
---
# Metric-criterion decoupling

In 3,334 NLG papers (2020-2025), the authors computed, per task, how strongly each metric co-occurs with each named quality criterion inside the same paper, separately for LaaJ and human-evaluation subsets. Significant pairings concentrate almost exclusively among frequent metrics and frequent criteria: in dialogue generation and text summarization, BLEU, ROUGE, BERTScore and Meteor pair with coherence, fluency and relevance, a default set shared across tasks.[^c1] The quadrant of task-distinctive metrics by task-distinctive criteria has no significant cells, and question answering shows no significant pairings under either method.[^c2]

Exceptions exist: in summarization FactCC pairs near-exclusively with factual truth, consistent with its design.[^c3] The authors read the general pattern as papers choosing "their metric and criterion largely independently", a construct-validity concern.[^c4]

Related is **metric inertia**: lexical-overlap metrics persist alongside semantic ones. The authors attribute part of it to legacy datasets with a single gold reference that make overlap fast and deterministic, though modern models paraphrase freely.[^c5] The consequence for asking about quality: a reported metric used as a generic proxy for "quality" cannot show which property drove an improvement. The checklist asks that each metric be explicitly tied to a named criterion and that overlap metrics not support claims about coherence or factuality.[^c6]

The same mismatch appears outside NLG. A taxonomy of time series anomaly detection metrics finds that existing ones "group metrics by mathematical form", which gives no guidance on which metric fits an evaluation objective.[^c7] Organised by objective instead, the authors find that "many evaluation inconsistencies originate from mismatched design intentions rather than mathematical deficiencies."[^c8] The decoupling is the same: a metric picked by its form is not tied to the criterion it is meant to test. One measured instance is [[random-score-inflation]], where a metric scores uninformed predictions close to real detectors.

## Limits

- The evidence is co-occurrence in papers, not whether a metric validly measures a criterion; a decoupled pair could still be well chosen.
- The explanation (tradition, single references) is the authors' argument, not tested.
- Criteria were mapped to a taxonomy from the criterion name alone, without context.
- Tasks are coarse (for example "dialogue generation"), hiding subtask-specific pairing.
- Four tasks only; extraction by LLM.

## Related

- [[llm-judge-validation-gap]] — the same paper's finding on judges
- [[llm-judge-biases]] — judge scores likewise need a named construct to be interpretable
- [[random-score-inflation]] — a time series detection metric that a random predictor can pass; the objective-to-metric mismatch made measurable

[^c1]: arxiv-2601-07648 — "indicating a default evaluation set shared across"
[^c2]: arxiv-2601-07648 — "The distinctiveness × distinctiveness quadrant contains no significant cells"
[^c3]: arxiv-2601-07648 — "FactCC pairs near-exclusively with Factual Truth,"
[^c4]: arxiv-2601-07648 — "their metric and criterion largely independently,"
[^c5]: arxiv-2601-07648 — "Researchers default to"
[^c6]: arxiv-2601-07648 — "Is the target construct explicitly named?"
[^c7]: arxiv-2511-18739 — "group metrics by mathematical form"
[^c8]: arxiv-2511-18739 — "many evaluation inconsistencies originate from mismatched design intentions rather than mathematical deficiencies"
