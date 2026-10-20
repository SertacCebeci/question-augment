---
description: "A named social role (mother, principal) in a terse system prompt, plus role-based critics, induces both values and context-reading schemas and beat principle lists on safety benchmarks."
aliases: ["role conditioning for alignment", "role-based critics", "guardianship role assignment"]
sources: ["arxiv-2602-00061"]
---
# Role-conditioned value and cognition induction

The claim is that a principle list supplies only values, while answering well in context also needs a belief or cognition model that says when a value applies. A role is proposed as a compact carrier of both: "mother" or "judge" implicitly encodes care or fairness and the schema for applying it.[^c1] The authors model an aligned response as drawn from P(y | x, v*, c*), and treat the role as a latent variable that induces both v and c, whereas a fixed principle set fixes only v.[^c2] Their argument is that for an ideal role the role-induced distribution equals the target one, so it dominates a principle list; this is an ideal-case argument, not a measured result.

## The pipeline

A generator gets a one-line system prompt naming the roles ("On your private side, you are also {role1}, {role2}..."). One critic per role then judges the full response strictly from that role's values and professional ethics, returning Agree or Disagree plus a suggestion. The generator revises until all critics agree or the iteration limit is hit.[^c3] The roles are given by name only, to isolate role assignment from prompt optimization.[^c4]

## What was measured

- Selection on SafeEdit: single roles with system prompt alone raised safety from 54.0% to 78.5%. The best were guardians of children and students, in line with the intuition that content is safe if it is "safe for children".[^c5]
- Concrete beat abstract: "mother" outperformed "parent". The authors read this as concrete terms giving better value understanding.[^c6]
- Number of roles (Qwen3-8B, SafeEdit): the largest gain is from one role (83.7%) to two (85.8%); five roles give 86.6%. Which roles are chosen still moves results.[^c7]
- Critic iterations: most of the benefit arrives with the first iteration, modest gains through the third, then a plateau.[^c8]
- The abstract reports WildJailbreak unsafe outputs falling from 81.4% to 3.6% with DeepSeek-V3, across five model families.[^c9]
- Agentic safety (GPT-4.1, system prompt only): blackmail rate fell from 65% to 11% in the affair scenario, and the best role set depended on the scenario (principal plus mother cut the bribery rate from 36% to 8%).[^c10]
- Combining with URIAL raised its performance, but the combination still underperformed the role method alone.[^c11]

## Limits

- The dominance claim holds only for an "appropriate role r*"; no method for finding r* is given beyond screening roles on a benchmark, and the same SafeEdit benchmark was used to choose the roles that are then reported.
- Ablations used only Qwen3-8B on SafeEdit for computational reasons.[^c12]
- The method depends on the model genuinely understanding the concrete role; the authors caution about roles whose characteristics are poorly represented.[^c13]
- Guardian roles may bias toward refusal; over-refusal cost on benign queries was not something I verified in the slices read. This is my caveat.
- Baselines (ShieldGemma principles, URIAL, CoT examples built from AdvBench) are particular choices; a stronger principle prompt was not shown to lose.

## Related

- [[expert-persona-confidence-amplification]] — another persona effect, which the authors read as changing commitment rather than knowledge
- [[llm-red-teaming]] — the jailbreak benchmarks on which unsafe output is measured
- [[dialectic-red-team]] — adversarial role-based critique as a refinement signal

[^c1]: arxiv-2602-00061 — "Roles like “mother” or “judge” implicitly encode the relevant values (care, fairness)"
[^c2]: arxiv-2602-00061 — "where the role r induces both values vir and cognition cri given any context naturally."
[^c3]: arxiv-2602-00061 — "The generator iteratively refines its output based on this feedback until all critics approve or the maximum iteration"
[^c4]: arxiv-2602-00061 — "Note that we intentionally keep the information about the roles to be just their names to isolate the effect of our rolebased approach from factors like prompt optimization."
[^c5]: arxiv-2602-00061 — "The safety rate improves from the base"
[^c6]: arxiv-2602-00061 — "that concrete terminology generally yields better"
[^c7]: arxiv-2602-00061 — "the most significant gain occurs when expanding from"
[^c8]: arxiv-2602-00061 — "performance substantially improves with the first iteration, shows modest gains through the third iteration, and then plateaus."
[^c9]: arxiv-2602-00061 — "it reduces unsafe outputs on the WildJailbreak benchmark from 81.4% to 3.6% with"
[^c10]: arxiv-2602-00061 — "the combined principal + mother” role proved most"
[^c11]: arxiv-2602-00061 — "Despite these gains, the combined approach still underperformed compared to"
[^c12]: arxiv-2602-00061 — "Due to computational constraints, all ablation experiments were conducted"
[^c13]: arxiv-2602-00061 — "Our method relies on LLMs’ genuine “understanding” of concrete roles we listed."
