---
description: "Multi-hop QA's retrieve-reason loop decides plan, index, next step and stop over time; a four-axis schema makes those choices comparable across systems instead of hidden heuristics."
aliases: ["retrieval–reasoning process", "retrieval–reasoning loop", "four-axis design framework", "execution procedure as unit of analysis"]
sources: ["arxiv-2601-00536"]
---
# Retrieval-reasoning procedure as the unit of analysis

In multi-hop question answering, the paper takes the execution procedure, not the architecture around it, as the object of analysis.[^c1] The procedure is the sequence of retrieval calls, intermediate hypotheses and stopping decisions a system runs before it answers. Its stated importance is that it is "often the main lever that changes both accuracy and failure modes": when to retrieve, how to form the next query, what evidence to keep under budgets, and when to stop.[^c2] IRCoT ([[chain-of-thought-interleaved-retrieval]]) is the paper's example: it improves multi-step QA by changing the retrieval-reasoning interaction, "rather than only scaling the reader".[^c3]

The paper's schema has four axes. Axis A is the overall execution plan. Interleaved plans, for instance, "alternate between reasoning steps and retrieval calls", where retrieve-then-read fetches a fixed set once.[^c4] Axis B is the index structure; hierarchical summary trees, for example, reduce context length on long-document QA by retrieving summaries and then drilling down.[^c5] Axis C is next-step control, covering both the strategy (rule-based, learned policy, search) and the trigger that decides the next move. Axis D is the stop/continue criterion.[^c6]

The axes are meant to be read together. Retrieval, reasoning, control and stopping "are interleaved over time, rather than discussed as separable components".[^c7] That is the argument for the framing: a choice such as a controller trigger or a stop signal, which papers "often present as method-specific heuristics", becomes a position on a shared axis, so that two systems can be laid side by side on the same choice.[^c8] The schema was applied to a corpus of 104 systems, and the paper reports the distribution on each axis; for Axis C, "over half of the systems employ a learned global control policy".[^c9]

## Limits

The framework is a taxonomy, and the authors disclaim more than that. The aim is to make procedural choices "explicit and comparable across systems rather than to claim causal superiority".[^c10] The empirical tendencies are a "pattern-mining synthesis of empirical findings as reported in the original papers".[^c11] Results come from "heterogeneous retrievers, LLMs, prompts, and budgets", so cross-paper comparisons are "suggestive rather than definitive".[^c12][^c13]

My reading is that the text reports no system re-run under a shared setup, so the effect of any single axis is not isolated here. That is my inference, not a claim of the paper. The corpus is also partial, since "our selection is necessarily incomplete", and it centres on English, text-based benchmarks.[^c14][^c15]

Finally, the axes are not yet linked to one another. The authors name the missing "principled mapping between structure and plan" as an open problem.[^c16] Reading the four axes as independent knobs would go beyond the text.

## Related

- [[stop-continue-criteria-in-retrieval-loops]] — axis D in detail: budget, confidence and verifier stops, and how common each is.
- [[chain-of-thought-interleaved-retrieval]] — IRCoT, the paper's example of an interleaved plan (axis A).
- [[self-ask-decomposition]] — a prompt format for the same interleaved loop, with explicit follow-up questions.
- [[uncertainty-guided-retrieval-triggering]] — a trigger on axis C, deciding whether to retrieve at all.
- [[coverage-driven-retrieval-control]] — a control that chooses to stop from element coverage, touching axes C and D.
- [[stopping-rules]] — a different object: error-controlled stopping of a sequence of tests, not of a retrieval loop.

[^c1]: arxiv-2601-00536 — "This survey takes the execution procedure as the unit of analysis"
[^c2]: arxiv-2601-00536 — "is often the main lever that changes both accuracy and failure modes"
[^c3]: arxiv-2601-00536 — "rather than only scaling the reader"
[^c4]: arxiv-2601-00536 — "Interleaved plans alternate between reasoning steps and retrieval calls"
[^c5]: arxiv-2601-00536 — "Hierarchical or summary-tree structures such as RAPTOR reduce context length"
[^c6]: arxiv-2601-00536 — "(C) next-step control (strategies and triggers), and (D) stop/continue criteria"
[^c7]: arxiv-2601-00536 — "are interleaved over time, rather than discussed as separable components"
[^c8]: arxiv-2601-00536 — "often presented as method-specific heuristics"
[^c9]: arxiv-2601-00536 — "For Axis C (next-step execute plan), over half"
[^c10]: arxiv-2601-00536 — "rather than to claim causal superiority"
[^c11]: arxiv-2601-00536 — "pattern-mining synthesis of empirical findings as reported in the original papers"
[^c12]: arxiv-2601-00536 — "heterogeneous retrievers, LLMs, prompts, and budgets"
[^c13]: arxiv-2601-00536 — "we treat cross-paper comparisons as suggestive rather than definitive"
[^c14]: arxiv-2601-00536 — "our selection is necessarily incomplete"
[^c15]: arxiv-2601-00536 — "we focus primarily on English, text-based benchmarks"
[^c16]: arxiv-2601-00536 — "A principled mapping between structure and plan is still missing"
