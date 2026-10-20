---
description: "Scoring an answer by one exact string penalizes equivalent names; dropping the alias set cut one multimodal editing model's all-hop accuracy on original images from 29.90% to 12.99%."
aliases: ["alias-aware scoring", "answer alias set", "valid-alias answer matching", "alias set evaluation"]
sources: ["arxiv-2512-00881"]
---
# Alias-tolerant answer matching

An evaluation that asks whether a model's answer equals one gold string treats two names of the same entity as two different answers. The benchmark in this work is built against that gap. Each gold answer is expanded with "all valid aliases of the ground-truth answer (e.g., Buenos Aires and Buenos Ayres), as retrieved from Wikidata".[^c1] The mechanism is a lookup, not a model: a prediction counts if it matches any member of the alias set, so the scorer no longer marks a spelling variant of the right entity as wrong.

The effect is measured by removing the alias set and rescoring. For LLaVA on original images, the all-hop accuracy (H-Acc) "drops significantly, from 29.90% and 26.16% to 12.99% and 9.98%, respectively" when alias handling is excluded, for original and rephrased images.[^c2] The authors state the general point as a limit of the usual protocol: "conventional VQA evaluation protocols, which rely on exact single-answer matching" can "fail to capture nuanced differences in model capabilities".[^c5] The alias set does more than shift one number. The authors report that the H-Acc gap between LLaVA and the other backbones narrows once aliases are removed, so the comparison between models changes too.[^c3]

The direction is the useful part. Alias handling raises measured accuracy, so an exact-match scorer under-reports the model. A method that scores better under exact match is not automatically the better one, because the ranking can depend on how the answer is spelled.

## Limits

- The measurement is one benchmark, MMQAKE, with factoid answers whose entities have Wikidata entries. The authors name "open-ended questions beyond factoid QA" as future work.[^c4] Alias matching says nothing about answers that are descriptions, lists or claims.
- The removal test is reported for the proposed method only, in an appendix table, not for every baseline.[^c2] Whether the alias gain would be the same for the baselines is not shown.
- An alias set is only as complete as its source. An answer whose valid name is missing from the knowledge base is still counted wrong. The paper does not measure how many gold answers lack aliases, or how often an alias expansion accepts a wrong entity. (My inference from the design; the paper does not report it.)

## Related

- [[exact-match-versus-weighted-agreement]] — exact match counts every error alike; alias matching is a separate way exact match misfires, by counting a right answer as wrong
- [[invariance-sensitivity-trade-off]] — invariance to equivalent rewrites, here applied to the answer side rather than the question side
- [[dependency-aware-checklist-scoring]] — another scorer that changes which intermediate answers count as correct, by checking prerequisites rather than spelling

[^c1]: arxiv-2512-00881 — "aliases of the ground-truth answer (e.g., Buenos Aires and"
[^c2]: arxiv-2512-00881 — "its H-Acc drops significantly, from 29.90% and 26.16% to 12.99% and 9.98%, respectively"
[^c3]: arxiv-2512-00881
[^c4]: arxiv-2512-00881 — "we aim to address open-ended questions beyond factoid QA and explore end-to-end multihop reasoning"
[^c5]: arxiv-2512-00881 — "conventional VQA evaluation protocols, which rely on exact single-answer matching"
