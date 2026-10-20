---
description: "Adapting only the query projections over one cached prefill raises the target-distractor margin with keys and values fixed, a cheaper use of inference compute than extra thinking tokens."
aliases: ["qTTT", "query-only TTT", "query-only test-time adaptation"]
sources: ["arxiv-2512-13898"]
---
# Query-only test-time training

Test-time training (TTT) adapts a model's weights to the input it is given, at inference. On long contexts the full version is too costly, because each update needs a forward and backward pass over the whole context. The query-only variant avoids that. It runs one prefill to store each layer's keys and values, then takes a few gradient steps on the query projection matrices alone, on short contiguous spans of the context. The "few lightweight gradient updates exclusively on the query projection matrices in the attention layers" leave "all other parameters fixed and reusing the key-value cache."[^q1]

The mechanism is what the update does to attention. For a loss equal to the negative log of the target's attention weight, with keys fixed, the gradient with respect to the query is a scaled attention-weighted average of the keys minus the target key. A descent step therefore moves the query toward the target key and away from that average.[^q2] The margin between the target logit and the rest rises with each step, and the gain is proportional to the squared distance between the target key and the attention-weighted mean. The paper's conclusion is that "Improvements are therefore largest precisely when attention is most diffuse," which is the regime where score dilution is severe.[^q3] The first-order statement holds for small step sizes; the higher-order terms are dropped.

The compute comparison is the reason the paper frames this as reallocating inference budget. Extra thinking tokens grow the cache by thousands of positions without changing attention, whereas query updates "keep the cache length fixed at T" and spend the same FLOPs reshaping queries against the existing keys and values.[^q4] The paper gives a rule of thumb that, for long contexts, the thinking-token count is roughly twice the number of query updates times the span length, and it uses that to match budgets in its experiments.[^q4]

On the benchmarks, the abstract reports "qTTT leads to massive 12.6% and 14.1% points improvements" for Qwen3-4B on average across subsets of LongBench-v2 and ZeroScrolls, against in-context decoding and compute-matched thinking.[^q5] The gains are largest on tasks where evidence is spread out: on Long Dialogue History and Multi-Document QA the paper reports wide margins over both baselines.[^q6] On summarization-style tasks the gain is small, and the paper's reading is that "reweighting attention yields limited returns" when generation, not retrieval, is the bottleneck.[^q7]

What transfers and what does not: the transferable part is the claim that access to the evidence, not the length of the reasoning written after it, limits retrieval. The intervention itself needs gradient access to the model's query weights and so is not something a prompt writer can perform. A question-asker's counterpart would be a change in how the question is represented relative to the evidence; the paper does not test that, and I do not claim it.

## Limits

- The compute matching is against thinking tokens only. The paper says "extending to self-consistency and best-of-n within the same framework is future work."[^q8]
- The gains are task-dependent, and the paper gives no rule for when to prefer query updates over decoding-based scaling; it lists developing such predictors as a next step.[^q9]
- The evaluation covers Qwen3 models from 1.7B to 8B and two long-context benchmark suites, plus the authors' synthetic tasks. Other architectures and model families are not tested in this text.
- The margin mechanism is shown on single-head analysis and on attention mass for synthetic targets. That the benchmark gains come from margin increase is the authors' inference from the attention-mass measurement, not a direct test on the benchmarks.
- Wall-clock and latency comparisons are reported in an appendix this note did not read, so the claim about practical cost rests only on the FLOP-matching argument.
- The paper evaluates a single point on the trade-off between span size and number of steps, so the best setting is not established.[^q10]

## Related

- [[score-dilution]] — the mechanism this update is derived to counteract; the margin requirement the query update tries to meet.
- [[cot-token-complexity-lower-bound]] — a separate bound on what generated chain-of-thought tokens can do, which the compute comparison here sits beside.

[^q1]: arxiv-2512-13898 — "projection matrices in the attention layers, keeping all other parameters fixed and reusing the key-value cache"
[^q2]: arxiv-2512-13898 — "explicitly counteracting dilution"
[^q3]: arxiv-2512-13898 — "Improvements are therefore largest precisely when attention is most diffuse"
[^q4]: arxiv-2512-13898 — "keeps the cache length fixed at T"
[^q5]: arxiv-2512-13898 — "qTTT leads to massive 12.6% and 14.1% points improvements"
[^q6]: arxiv-2512-13898 — "On Long Dialogue History and Multi-Document QA, where evidence is most diffuse, qTTT outperforms standard in-context and thinking by wide margins"
[^q7]: arxiv-2512-13898 — "reweighting attention yields limited returns"
[^q8]: arxiv-2512-13898 — "extending to self-consistency and best-of-n within the same framework is future work"
[^q9]: arxiv-2512-13898 — "developing simple predictors for when to prefer qTTT"
[^q10]: arxiv-2512-13898 — "We evaluate a single point on the"
