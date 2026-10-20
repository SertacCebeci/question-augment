---
description: "Questions kept only when a panel of open-weight models all answer them wrong, closed-book, keeps a factoid benchmark hard for frontier models, but the filter measures the panel, not the target."
aliases: ["adversarial sampling with open-weight models", "proxy-model adversarial selection", "closed-book proxy filter", "open-model failure filter"]
sources: ["arxiv-2512-10791"]
---
# Proxy-panel hardness filter

A benchmark of factual questions goes stale when its questions stop being hard for the models it is meant to measure. One way to keep questions hard in advance is to select them by how a different set of models fares. In the FACTS Parametric construction the selection runs in stages. Questions first pass automatic LLM filters for the factoid criteria. They are then labelled with a preliminary "silver" answer from a strong search-enabled model, and kept only if that answer is backed by a Wikipedia URL in the search results.[^c1] The hardness step comes next. The authors "collect responses from five strong open-weight models," queried "in a closed-book setting, without access to external search tools," and "retain only the questions that none of these open-weight models answered correctly."[^c2]

The mechanism is a difficulty filter defined by failure of a proxy panel. A question survives when every panel member misses it, so the surviving set is by construction a set where the panel's closed-book recall is zero. The authors give the reason for choosing open weights: "to decouple the adversarial selection process from" the proprietary models that are later evaluated.[^c3] The filter's stated purpose is forward-looking: "a key goal is to ensure the benchmark remains challenging for frontier LLMs, avoiding saturation in the near future."[^c4]

The filter is one stage among several. Human verification follows, with three annotators per pair checking the answer against the web rather than the supplied URL.[^c5] So a question that every open model misses still has to be confirmed as correct before it stays. The panel decides which questions are hard; it does not decide which are true.

Read as a concept rather than a recipe: difficulty can be defined relative to a reference population of answerers, and a benchmark built this way is hard for that population by construction. Whether it is hard for the population that is actually being measured is a separate question, and my inference is that the answer depends on how far the panel's failures overlap with the target's. Nearby, the same paper's headline is the reason the filter exists: "the top performing model has an average accuracy of only 69%," and "existing benchmarks become saturated" as LLMs improve.[^c6]

## Limits

- The filter is a pass/fail on the panel. The text gives no measurement of how many questions it removed, nor of how the frontier accuracy on FACTS Parametric would look without it. The effect on difficulty is asserted in the design, not measured in the passages read.
- The "correct" used in the panel test is a match to the silver answer from a single search-enabled model, and the authors call these "preliminary filters; the final labels are determined later."[^c7] A question the panel misses because the silver label is wrong would be dropped for the wrong reason, and only the later human pass corrects labels.
- Difficulty for the panel is not difficulty in general. Hardness might come from obscure entities, from answer-format ambiguity, or from the panel's training data, and the authors name this as open: "studying what affects the hardness of questions."[^c8] The filter does not say which of these it is selecting for.
- Decoupling from proprietary evaluated models is a choice, not a proof of independence. Open models trained on overlapping web text can share the same blind spots as the frontier models; the text does not test for this.
- The filter is tied to a moment. A question kept as hard today can become easy as the panel improves, which is the drift problem the wiki records for fixed benchmarks ([[benchmark-drift]]). The paper does not describe a schedule for re-running the filter.

## Related

- [[benchmark-drift]] — a benchmark can look saturated while its judge no longer tracks what it measured; this filter addresses the saturation half of that problem at construction time.
- [[saturated-performance-measure]] — a ceiling in the measure itself; the filter here works on item selection, not on the metric.
- [[search-decision-f1]] — another construction that scores models against parametric-only knowledge, where the reference set depends on the evaluated model.
- [[question-asking-skill-transfer]] — a panel of open-weight solvers also defines which questions count as boundary cases, but there the panel sets a reward target rather than what is dropped.
- [[clean-accuracy-masks-adversarial-collapse]] — the word "adversarial" here means selection by failure, not an input perturbation; the two share only the idea that one accuracy number can hide what a model does under a chosen pressure.

[^c1]: arxiv-2512-10791 — "we filter this set to retain only the questions where the model"
[^c2]: arxiv-2512-10791 — "we retain only the questions that none of these open-weight models answered correctly"
[^c3]: arxiv-2512-10791 — "to decouple the adversarial selection process from"
[^c4]: arxiv-2512-10791 — "a key goal is to ensure the benchmark remains challenging for frontier LLMs"
[^c5]: arxiv-2512-10791 — "each question-answer (QA) pair was verified by three independent third-party human annotators"
[^c6]: arxiv-2512-10791 — "the top performing model has an average accuracy of only 69%"
[^c7]: arxiv-2512-10791 — "preliminary filters; the final labels are determined later"
[^c8]: arxiv-2512-10791 — "studying what affects the hardness of questions"
