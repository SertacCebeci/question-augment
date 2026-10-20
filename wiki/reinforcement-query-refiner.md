---
description: "An RL-trained frontend rewrites a query into explicit structured logic before a frozen LLM sees it, trained against a difficulty-matched solver pool so one refiner generalizes to unseen models."
aliases: ["ReQueR", "Adaptive Solver Hierarchy", "ASH"]
sources: ["arxiv-2604-25444"]
---
# Reinforcement query refiner

> The rewrite is not learned against one model's quirks; it is learned against a moving pool of models kept at the refiner's own frontier of competence — so the rewrite that results generalizes to models neither ever saw.

## Definition / Mechanism

A refiner policy $\pi_\theta(x'|x)$ rewrites a raw query $x$ into a structured query $x'$ before a frozen downstream Solver LLM answers it; training treats the Solver as the environment and reinforces the refiner on whether the Solver's answer to $x'$ is correct.[^c1]

Because no Solver parameters are touched, one refiner trained against a small set of Solvers can be applied at inference time to Solvers it never trained against, with no per-model tuning — the paper calls this $O(1)$ alignment against $O(N)$ per-model fine-tuning.[^c2]

Training a rewriting policy this way hits reward sparsity: a Solver too weak fails regardless of query quality, one too strong succeeds on a poor rewrite, and either way the gradient carries no signal about whether the rewrite helped. The Adaptive Solver Hierarchy (ASH) fixes this per training sample rather than per training run: each sample carries its own difficulty index into a capability-ranked Solver pool, and after a group of rewrite attempts on it, the index escalates to a stronger Solver if every attempt failed and de-escalates to a weaker one if every attempt succeeded, keeping the assigned Solver at the sample's current pass/fail boundary. This is a Zone-of-Proximal-Development argument applied to the *rewrite*, not to a learner's knowledge: the wording a policy should produce next is calibrated to what an evaluator just barely fails or just barely succeeds at resolving, sample by sample, rather than to a fixed curriculum schedule shared across samples (contrast [[reformulation-pattern-library|a fixed pattern selected once per query]]).[^c3]

A second failure mode is specific to training a rewriter against a reward it does not fully control: the refiner can raise the accuracy score by leaking the answer into the rewritten query instead of eliciting reasoning for it. The paper detects this without a generative judge, by comparing a judge model's conditional perplexity of the ground-truth answer given the query before and after refinement — a large drop signals the rewrite handed the answer away rather than structured the problem — and penalizes the reward when the drop exceeds a threshold.[^c4]

Ablating ASH is the single largest driver of the reported gains, and removing it destabilizes training outright.[^c5]

## Why it matters

What the trained rewriter converges on gives a working taxonomy of what "explicit, structured logic" means for a wording change to a math or reasoning query, distinct from a fixed pattern library selected before generation: symbolic parameterization (turn a narrative word problem into named variables and equations), contextual de-noising (drop factual detail irrelevant to the computation), linguistic disambiguation (replace a vague phrase with an explicit operator or set), and conceptual reduction (decompose a named high-level concept into primitive operations and constraints).
[^c6.1][^c6.2][^c6.3][^c6.4]

Across benchmarks and Solver architectures, Zhou et al. (2026) report consistent absolute gains over zero-shot prompting the raw query, 1.7–7.2 points depending on benchmark and Solver, beating other rewriting baselines by 2.1 points on average.[^c7]

## Limits

Evaluated only on reasoning tasks with a verifiable ground-truth
answer (math and general-reasoning benchmarks); the leak-penalty
mechanism assumes a judge model whose conditional perplexity is a
faithful signal of leakage, and the main ASH ordering is built from
one model family (Qwen3 at three sizes), with a cross-family variant
shown only to match it rather than to improve on it substantially. In
a real-time deployment the refiner adds a second generation pass
before the Solver runs, an overhead the paper argues but does not
fully net out against the shorter Solver responses it also reports.

## Related

Retrieval-side counterpart: rewrite-retrieve-read trains a small rewriter against a frozen reader's answer too, but with a web search between rewrite and reader, and it is measured by retrieval hits as well as answers.

[[reformulation-pattern-library]] · [[elicitation-transform-types]] · [[question-rewriting-schema-scaling]] · [[specification-channel-redundancy]] · [[format-restriction-effect]]

[^c1]: arxiv-2604-25444 — "we propose ReQueR (Reinforcement Query Refinement), a modular framework that treats reasoning elicitation as an inference-time alignment task. We train a specialized Refiner policy via Reinforcement Learning to rewrite raw queries into explicit logical decompositions, treating frozen LLMs as the environment."
[^c2]: arxiv-2604-25444
[^c3]: arxiv-2604-25444 — "By escalating Solver difficulty upon consistent failure and de-escalating when success becomes trivial, ASH ensures the Refiner evolves within its optimal growth zone, maintaining a dense reward signal"
[^c4]: arxiv-2604-25444
[^c5]: arxiv-2604-25444 — "removing ASH degrades performance significantly, confirming that balancing task difficulty with current competence is essential for stable optimization"
[^c6.1]: arxiv-2604-25444 — "Strategy 1: Symbolic Parameterization Description: Transforms narrative word problems into formal symbolic models comprising variables and equations."
[^c6.2]: arxiv-2604-25444 — "Strategy 2: Contextual De-noising Description: Filters out factual but computationally irrelevant narrative noise from the problem description."
[^c6.3]: arxiv-2604-25444 — "Strategy 3: Linguistic Disambiguation Description: Resolves semantic ambiguity by replacing vague natural language with formal operators or explicit sets."
[^c6.4]: arxiv-2604-25444 — "Strategy 4: Conceptual Reduction Description: Decomposes high-level math concepts into primitive algebraic operations and decision constraints."
[^c7]: arxiv-2604-25444 — "ReQueR yields consistent absolute gains of 1.7%–7.2% across diverse architectures and benchmarks, outperforming strong baselines by 2.1% on average."
