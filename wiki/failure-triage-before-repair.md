---
description: "Validation errors after supervised training mix noisy triples, misaligned questions and real gaps; repairing all of them reinforces noise, so only audited gaps get targeted training."
aliases: ["adaptive triple repair", "history-aware repair", "missing-knowledge repair", "LLM-judged repair with quarantine", "error triage before targeted fine-tuning"]
sources: ["doi-10-48550-arxiv-2609-12230"]
---
# Failure triage before repair

After supervised fine-tuning a model still answers some held-out items wrongly. The default reading is that a wrong answer marks something not yet learned, so train more on it. The paper argues that one wrong answer can come from several sources. "the source triple may be noisy, the validation question" may be misaligned with the fact it tests, or the model may really lack the knowledge.[^r1] Training on all of them is the risk: "on every incorrect validation item risks reinforcing noisy or unsupported supervision."[^r2] The idea is to sort the failures first and to give targeted training only to those that survive the sorting. The sorting is what separates this from plain retraining on errors.

The procedure, as the paper describes it, has a diagnosis, a repair and a review. A judge model first does "first diagnosing the source of each failure".[^r3] The repair stage then covers "failure categorization, targeted QA item generation, regression".[^r4] Items judged to be real gaps receive new questions built from the same source triple, and "These examples provide multiple alternative phrasings" of the same fact.[^r5] A second judge reviews what was set aside, the quarantine.

"History-aware" means the training set of each round depends on the record of each item, not only on the current round: the set is "determined by the error history of individual triple IDs (path_idx)".[^r6] The amount of repair also varies with the kind of error: "we do not use the same number of repair" examples for every failed triple.[^r7] The history matters because repair itself can break items. "New-error triples are usually recent repair-induced failures".[^r8] Each round is followed by a fresh evaluation, so a repair that creates new failures shows up as a regression rather than being hidden.

The reported outcome is that the repair brings the one-hop foundation to a perfect score. "This repair stage enables the models to reach 100% accuracy on the cleaned retained one-hop" validation sets.[^r9] The reason the paper gives for caring about one-hop errors is that a longer chain is built from them: "composed of multiple lower-hop factual links, unresolved 1-hop errors can" carry into the longer reasoning.[^r10] The downstream effect on reinforcement learning is reported separately; see [[atomic-sufficiency-for-rl-synthesis]].

## Limits

- The 100% is measured after quarantine. The abstract's wording, "the cleaned retained" set, means the items judged noisy were removed before scoring. A score on the retained set is not comparable to the accuracy on the full set before repair. This is my reading of the wording; the sections read do not give the full-set number next to it.
- The judges are language models, and they share a family with the model being trained. "Judge 1 uses Qwen3.6-27B for" the failure audit and Judge 2 is Qwen3-32B, while the trained model is Qwen3-14B.[^r11] The paper says the design "reduces the need for repeated manual inspection, but judge decisions may still" carry "model-specific biases".[^r12] My inference: a diagnosis from a model of the same family may share the trained model's blind spots, which the diagnosis is meant to catch. The text does not test this.
- No run in the sections read trains on all failures and compares the result with the triaged version. The claim that blind training "risks" reinforcing noise is stated as a risk, not measured against the alternative in those sections.
- The synthetic items are the same kind of data as in the context study. "the datasets are synthetic, some residual ambiguity or generation noise may remain".[^r13] A triage step that relies on synthetic items inherits any defect the generator puts into them.
- The repair targets one-hop items. Whether repairing one-hop errors helps 3- to 5-hop answers is shown only through the later RL step, not through the repair alone, in the parts read.

## Related

- [[same-chunk-context-supervision]] — the SFT stage whose one-hop failures this triage sorts.
- [[atomic-sufficiency-for-rl-synthesis]] — RL needs a base that already has the atomic parts; here the repaired checkpoint is the base condition for RL.
- [[reference-answer-defect-audit]] — the same question, whether a failure belongs to the model or to the item, asked of benchmarks rather than training data (my reading from its alias list).

[^r1]: doi-10-48550-arxiv-2609-12230 — "the source triple may be noisy, the validation question"
[^r2]: doi-10-48550-arxiv-2609-12230 — "on every incorrect validation item risks reinforcing noisy or unsupported supervision"
[^r3]: doi-10-48550-arxiv-2609-12230 — "first diagnosing the source of each failure"
[^r4]: doi-10-48550-arxiv-2609-12230 — "failure categorization, targeted QA item generation, regression"
[^r5]: doi-10-48550-arxiv-2609-12230 — "These examples provide multiple alternative phrasings"
[^r6]: doi-10-48550-arxiv-2609-12230 — "error history of individual triple IDs (path_idx)"
[^r7]: doi-10-48550-arxiv-2609-12230 — "we do not use the same number of repair"
[^r8]: doi-10-48550-arxiv-2609-12230 — "New-error triples are usually recent repair-induced failures"
[^r9]: doi-10-48550-arxiv-2609-12230 — "This repair stage enables the models to reach 100% accuracy on the cleaned retained one-hop"
[^r10]: doi-10-48550-arxiv-2609-12230 — "composed of multiple lower-hop factual links, unresolved 1-hop errors can"
[^r11]: doi-10-48550-arxiv-2609-12230 — "Judge 1 uses Qwen3.6-27B for"
[^r12]: doi-10-48550-arxiv-2609-12230 — "scalable failure diagnosis and reduces the need for repeated manual inspection, but judge decisions may still"
[^r13]: doi-10-48550-arxiv-2609-12230 — "the datasets are synthetic, some residual ambiguity or generation noise may remain"
