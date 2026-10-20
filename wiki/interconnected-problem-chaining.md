---
description: "When each stage takes the previous stage's output as input, a task becomes stateful; the paper argues this strains an LLM's multi-step reasoning and context more than independent parts."
aliases: ["interconnected assessment", "output-as-input chaining", "sequential dependency design", "stateful multi-stage problem"]
sources: ["arxiv-2512-10758"]
---
# Interconnected problem chaining

Two sets of sub-problems can contain the same parts and still differ in one structural respect: whether the solution to one part is an input to the next. The paper calls a set where "the output of one problem serves as the input for the next" an interconnected assessment, and sets it against a modular one whose problems are independent.[^c1]

The grounding is Cognitive Load Theory's notion of element interactivity. Intrinsic difficulty is set by how many interacting elements must be held together, since they "must be simultaneously processed in working memory".[^c2] A task whose parts can be handled one at a time is one that "can be broken down and solved piece by piece".[^c3] A chain is the case where the parts cannot be separated, because the later part depends on the earlier one.

The paper's proof follows the dependency. If the solution to one stage is an input to the next, "a generative AI model must therefore solve the entire sequence" to answer a later stage.[^c4] Two costs follow. The first is multi-step reasoning, where the cited weakness is that "performance degrades as the number of reasoning" steps grows.[^c5] The second is memory: "the cumulative context required to solve later problems in the sequence can exceed the" effective context window.[^c6] A modular problem is solved "in a separate, stateless" context, so it never accumulates this load.[^c7] The paper concludes that "design is inherently more resilient to trivial AI delegation",[^c8] and its premise is that current generative AI "struggles with high-interactivity problems".[^c9]

What the concept changes is how a question is built. In a chain, each sub-question's content depends on the answer to the one before, so no part can be lifted out and answered alone. My reading: this is the same logic as [[bridging-question-chaining]], where a multi-hop question is grown by linking an answer into the next question and the link is kept only if removing the bridge leaves the question unanswerable. The difference is what the link is. There the bridge is an entity in a question; here it is a learner's own output. The removal test that would show a link is needed is not run in this paper.

## Limits

- The resilience claim is argued, not measured on a model. The proof draws on cited results about LLM multi-step reasoning and context, and the paper does not run an assistant on the modular and chained versions. The empirical part is student grades: "For each course, we collected anonymized" student grade data for every assessment.[^c10]
- The drop comparison is weak on its own terms. Figure 2 says the chained project shows "a greater (though not statistically significant) drop and higher variability".[^c11]
- The two-offering comparison confounds design with cohort. The courses "shared identical syllabi and encouraged the use of AI tools",[^c12] but they ran in different terms with different students, and the paper does not control for that. My reading: the difference may reflect the cohort as much as the design.
- Higher variance is read as differentiation: "in dispersion is a desirable property".[^c13] My reading: a wider spread can also come from a harder or less well-specified task. The paper does not separate these readings.
- The optimal degree of interconnection is not established. The paper says it would "explore the optimal level of interconnectedness",[^c14] which means the level at which the effect holds, or stops helping, is open.

## Related

- [[bridging-question-chaining]] — the same output-as-input link, used to grow a multi-hop question and checked by removing the bridge.
- [[ai-score-inflation]] — the measured take-home versus proctored gap that this structure is proposed to reduce.
- [[solution-space-pinning]] — the paper's second proposition: it constrains which instance is solved, where chaining constrains the sequence.
- [[unsolicited-task-switching-cost]] — Cognitive Load Theory applied to AI-assisted work, where extraneous load, not intrinsic load, carries most of the cost.

[^c1]: arxiv-2512-10758 — "where the output of one problem serves as the input for the next"
[^c2]: arxiv-2512-10758 — "must be simultaneously processed in working memory"
[^c3]: arxiv-2512-10758 — "solved piece by piece"
[^c4]: arxiv-2512-10758 — "must therefore solve the entire sequence"
[^c5]: arxiv-2512-10758 — "performance degrades as the number of reasoning"
[^c6]: arxiv-2512-10758 — "the cumulative context required to solve later problems in the sequence can exceed the"
[^c7]: arxiv-2512-10758 — "allows each problem to be solved in a separate, stateless"
[^c8]: arxiv-2512-10758 — "design is inherently more resilient to trivial AI delegation"
[^c9]: arxiv-2512-10758 — "struggles with high-interactivity problems"
[^c10]: arxiv-2512-10758 — "For each course, we collected anonymized"
[^c11]: arxiv-2512-10758 — "statistically significant) drop and higher variability"
[^c12]: arxiv-2512-10758 — "shared identical syllabi and encouraged the use of AI tools"
[^c13]: arxiv-2512-10758 — "in dispersion is a desirable property"
[^c14]: arxiv-2512-10758 — "explore the optimal level of interconnectedness"
