---
description: "In multi-agent debate, broadcasting only the most mutually disagreeing responses, chosen by index so text stays verbatim, beats full broadcast and confidence filtering and cuts messages up to 32%."
aliases: ["Diversity-Aware Retention", "DAR", "diversity-aware message retention"]
sources: ["arxiv-2603-20640"]
---
# Disagreement retention in debate

Before each debate round, a filter LLM sees the previous round's N responses and the last vote, and returns only agent IDs: the subset that maximally disagrees with each other and with the majority. The retained responses form the next round's context; if the subset is empty the round falls back to the full broadcast.[^c1] Returning IDs rather than rewritten text keeps messages unmodified, so retained disagreement stays authentic.[^c2]

## Why it should work

The paper models responses as noisy estimators with common variance and pairwise correlation ρ. The average then has variance σ²/N_eff with N_eff = N/(1+(N−1)ρ).[^c3] When ρ approaches 1, adding agents buys almost nothing; the gain depends on response diversity, not N alone (see [[effective-independent-votes]] for the same quantity measured on judge panels).[^c4] This is a simplified homogeneous model (equal variance, exchangeable); the link from it to the filter is the authors' argument, not a test of ρ before and after filtering.

## What was measured

- Illustrative case: with answers (A, A, B), agents holding A see only B; the agent holding B falls back to the full context, so majority answers are not discarded globally.[^c5]
- Retained responses had the highest average pairwise embedding distance among the retention strategies compared.[^c6]
- Message count fell up to 32% (Qwen2.5-3B, Arithmetics), more at N=8; latency rose 3–14%.[^c7]
- Ablations: a hard distinct-answer filter lost more than removing the uncertainty score or soft vote; text-based retention (LLM re-emits messages) degraded sharply from format inconsistencies, versus index selection.[^c8]
- Variants retaining only certain or only similar answers improved modestly over Society of Mind but stayed below DAR.[^c9]
- In longer debates most methods saturate early; DAR stayed best.[^c10]

## Limits

- Experiments use small open models (Qwen2.5-1.5B/3B) on a few reasoning and QA benchmarks; ablations only on Arithmetics and Formal Logic.
- Disagreement is not correctness: if the minority is wrong, retaining it can propagate error; the paper shows a recovered-majority-error example, not a failure analysis.
- The filter is itself an LLM, so its selection quality is unverified beyond downstream accuracy.
- Debate can induce agreement-seeking regardless of content; see [[debate-elicits-sycophancy]].

## Related

- [[effective-independent-votes]] — same N_eff correlation arithmetic, measured on judge panels
- [[debate-elicits-sycophancy]] — failure of debate that retention does not address
- [[questioning-diversity]] — diversity as a quantity worth preserving
- [[query-by-committee]] — disagreement as the selection signal

[^c1]: arxiv-2603-20640 — "selects the subset of agent responses that maximally disagree with each other and with the majority vote before broadcasting"
[^c2]: arxiv-2603-20640 — "Importantly, F outputs only agent IDs, ensuring that retained content remains unchanged"
[^c3]: arxiv-2603-20640 — "denotes the effective number of independent responses that would yield the same variance."
[^c4]: arxiv-2603-20640 — "This implies that the gain from increasing the number of agents is not determined by N alone,"
[^c5]: arxiv-2603-20640 — "Importantly, majority responses are not discarded globally, ensuring performance is not degraded when the majority is correct."
[^c6]: arxiv-2603-20640 — "Across datasets, DAR consistently achieves the highest retained diversity, contributing"
[^c7]: arxiv-2603-20640 — "achieving up to a 32% reduction (Qwen2.5-3B on Arithmetics)."
[^c8]: arxiv-2603-20640 — "significantly degrades performance due to formatting inconsistencies, leading to information loss"
[^c9]: arxiv-2603-20640 — "these variants offer modest improvements over Society of Mind, yet"
[^c10]: arxiv-2603-20640 — "remaining the best-performing method across longer debates"
