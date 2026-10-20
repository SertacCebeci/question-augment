---
description: "Reasoning, for evaluation, is a search whose step choice and halting time depend on intermediate states; correct answers can come from memorization or comprehension instead."
aliases: ["reasoning as adaptive multi-step computation", "memorization-comprehension-reasoning taxonomy"]
sources: ["doi-10-48550-arxiv-2605-02442"]
---
# Reasoning as input-dependent search

A correct answer does not say which process produced it. Nwadike et al. separate three regimes that can all yield the same correct output. Memorization is token-exact retrieval of a previously seen sequence. Comprehension is token-level association that survives paraphrase, i.e. pattern completion without an explicit step-by-step deductive search.[^c1] Reasoning is the remaining regime, defined as search through a chain of intermediate concepts between input concepts A and output concepts B until a connection is established.[^c2]

## The formal criterion

The search is a sequence of states s1 = f1(x), s2 = f2(s1), ..., sk = fk(s_{k-1}). At each step the system picks the next transition from the previous state, and halts when a predicate H(x, s_k) first holds. The defining feature is not that there are several steps but that both the next step and the stopping time depend on intermediate states.[^c3] The authors' reading is that a question such as a LogiQA item cannot be answered by recall or association alone, so it needs this adaptive form.[^c4]

## Why a single forward pass falls short

Their argument is that a fixed-depth threshold circuit (transformers, Mamba-like state-space models) is not expected to generalizably compute things whose depth grows with input length, such as recursion and search. Intermediate decoding such as chain-of-thought lets the model record partial state and condition on it, giving instance-adaptive step counts.[^c5] This is why they treat externalized traces as the evaluation interface: the distinction is between reasoning itself and access to the process by which it unfolds.[^c6]

## Same item, different regime

Which regime a benchmark item tests depends on exposure. With contamination, the 10,001st GSM8K-style question may collapse into comprehension-level pattern completion where the 4th still needed multi-step reasoning.[^c7] The consequence for question design is that the same wording can test reasoning for one model and recall for another; accuracy alone cannot say which. (My inference: an asker who wants to elicit reasoning should check whether the item is answerable by recall or association before reading success as reasoning.)

## Limits

- The definition is explicitly evaluation-oriented and a position-paper stance; the paper does not measure how often benchmark items fall into each regime.
- The TC0 limit concerns generalizable single-pass computation; it is cited from prior theory, not tested here, and says nothing about what models do in practice with traces.
- The regime boundaries (e.g. grokking treated as comprehension) are definitional choices, not empirically separated categories.
- Externalized traces may not be faithful to internal computation; the paper's own call is to evaluate that, not assume it.

## Related

- [[benchmark-contamination-convergent-audit]] — contamination is the route by which reasoning items collapse to recall
- [[accuracy-masks-unstable-reasoning]] — another case of accuracy failing to reveal the process
- [[reasoning-faithfulness-observer-effect]] — whether the externalized trace reflects the process
- [[supported-faithfulness-score]] — a trace-level faithfulness measure

[^c1]: doi-10-48550-arxiv-2605-02442 — "Token-level factual associations, supported by representational mapping, that are"
[^c2]: doi-10-48550-arxiv-2605-02442 — "proceeding through a chain of intermediate"
[^c3]: doi-10-48550-arxiv-2605-02442 — "The defining feature"
[^c4]: doi-10-48550-arxiv-2605-02442 — "This question cannot be answered through memorization"
[^c5]: doi-10-48550-arxiv-2605-02442 — "enabling instance-adaptive step counts"
[^c6]: doi-10-48550-arxiv-2605-02442 — "meaningful evaluation requires some substrate for measurement"
[^c7]: doi-10-48550-arxiv-2605-02442 — "solving the 10,001st can collapse into comprehension-level"
