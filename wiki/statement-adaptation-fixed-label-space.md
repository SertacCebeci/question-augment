---
description: "Recasting multiple-choice QA as a fixed True/False statement check, built on the runner-up option, makes uncertainty comparable across questions so unbiased test-item selection can run."
aliases: ["statement adaptation", "proxy statement verification", "natural language verification proxy", "RunnerUp proxy statement"]
sources: ["arxiv-2603-19264"]
---
# Statement adaptation to a fixed label space

Active selection of test items needs uncertainty scores that can be compared across items. Multiple-choice QA breaks this: the options change with every question, so confidence lives only inside one question's local context. Ramakrishnan et al. (2026) argue that unbiased risk estimation requires the task to "operate over a fixed, context-independent label".[^c1]

## Mechanism

An oracle model rewrites each question and one chosen option as a statement. The evaluated model then answers a binary Natural Language Verification task, True or False. Every item now shares the same two-class output space, so the entropy of the predicted distribution is comparable between items.[^c2] This is the precondition for the surrogate-based acquisition used in [[active-testing]].

Which option becomes the statement matters. Three strategies were compared: the top prediction (MostConf), the lowest-probability option (LeastConf) and the second most probable option (RunnerUp). The change in conditional AUROC among high-confidence items (confidence at least 0.7) varied widely for the first two. For example it fell by 49.9% for MostConf on one dataset (PubMedQA), a drop the authors tie to strong distractors and ambiguous "Maybe" options.[^c3] RunnerUp improved the metric on all three datasets. The authors read it as forcing the proxy to resolve the ambiguity that confuses the model most, which is margin sampling.[^c4] Statement adaptation also shrank the spread of output entropy compared with the raw QA task, which the authors call a more stable signal.[^c5]

The target is the high-confidence regime, where native uncertainty fails to separate correct answers from silent failures (hallucinations). The proxy is built to recover an error signal there.[^c6]

On top of the fixed label space the paper adds acquisition scores. They measure divergence from a uniform prior, optionally mixed with a surrogate model's belief. This is meant to down-weight items where the model is confidently wrong. The reported result is a roughly 40% reduction in estimation error against traditional sampling baselines, without task-specific training.[^c7]

## Limits

- Option choice is dataset-dependent. The RunnerUp recommendation was ablated with one main model (Llama 3.1 8B) and three datasets, and I did not see tests with other models.
- The statement rewrite uses a stronger external model (GPT-4o). My inference: rewriting errors, and the oracle's own bias, enter the proxy, and the cost of that step is not charged against the savings.
- The conditional AUROC subsets are small, a few hundred items each, and the gains in Table 2 are modest (a few AUROC points).
- Whether the proxy's uncertainty tracks the original QA error as well as the QA task's own confidence does is argued from AUROC and entropy spread. I did not find a direct risk-equivalence proof.
- The 40% figure is an average over settings. It is not uniform: for some main models and functions, random sampling was close or better.

## Related

- [[active-testing]] — the selection paradigm this adaptation makes applicable to generative QA
- [[surrogate-uncertainty-sharpness-for-query-selection]] — another case where the choice of surrogate uncertainty drives selection
- [[multi-choice-preference-query]] — multi-option questions whose options shape the answer

[^c1]: arxiv-2603-19264 — "operate over a fixed, context-independent label"
[^c2]: arxiv-2603-19264 — "(True/False) against which the model’s uncertainty"
[^c3]: arxiv-2603-19264 — "degradation in discrimination power (e.g. -49.9%"
[^c4]: arxiv-2603-19264 — "strategy forces the proxy task to resolve the specific ambiguity that confuses the model most, effectively acting as a margin-sampling technique"
[^c5]: arxiv-2603-19264 — "Compared to the QA task, the statement adapted task"
[^c6]: arxiv-2603-19264 — "targets the highconfidence regime"
[^c7]: arxiv-2603-19264 — "zero-shot acquisition functions reduce estimation error by"
