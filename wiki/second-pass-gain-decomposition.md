---
description: "A second-pass reviewer's gain splits into re-solving, scaffold and draft-content effects via four matched conditions; which dominates depends on task type and who is stronger."
aliases: ["re-solving vs revision", "revision gain accounting", "re-solving scaffold content decomposition"]
sources: ["arxiv-2604-01029"]
---
# Second-pass gain decomposition

When one model reviews and improves another's draft, the end-to-end gain is usually credited to the draft's information. A four-condition design separates three counterfactual transitions: x1 the generator alone; x2 the reviewer given question plus draft; x3 the reviewer given only the question (re-solving control); x4 the reviewer given question plus a semantically null, format-matched draft (scaffold control).[^c1] The total gain x2 − x1 is the sum of a re-solving effect (x3 − x1, the capability difference under direct answering), a scaffold effect (x4 − x3, the review framing and template) and a content effect (x2 − x4, the marginal value of the real draft over a null one).[^c2]

## What was measured

Two heterogeneous model pairs were run on GPQA Diamond, HLE and LiveCodeBench, in a primary (weak generator, strong reviewer) and a supplementary (roles swapped) setting.[^c3]

- On MCQ, weak-to-strong, most gain is re-solving, scaffold is negligible and content near zero; for example re-solving contributes +56.6 pp on GPQA Pair 2.[^c4] The stronger reviewer can discard a weak rationale and rebuild the answer from its own knowledge, so helpful and harmful draft influences mostly cancel.[^c5]
- On code, weak-to-strong, the null scaffold beats standard revision in both pairs and the content effect is significantly negative: the weak draft pulls the reviewer into a bad intermediate artifact.[^c6]
- Role-reversed, re-solving turns negative (the second pass is by the weaker model) and content becomes the compensating term; the authors read this as a threshold: weak drafts add little beyond what a strong reviewer can do, strong drafts can transfer capability to a weak reviewer.[^c7]

The design does not assume the three effects are independent; interactions show up as changes in marginal contributions across tasks, pairs and directions rather than as a residual.[^c8] The draft's identity is never revealed in any prompt, and the null draft avoids using another question's real output because that could carry latent transfer signal.[^c9]

## Why it matters for asking and answering

A gain from passing an intermediate artifact is not evidence that the artifact's content was used. The controls distinguish information transfer from downstream recomputation and interface effects; the authors suggest they bear on routing, resource allocation and graph design in cascades.[^c10] Inference (mine): where re-solving dominates, sending the question straight to the stronger model replaces the review step; where scaffold dominates, a fixed template may be the useful part.

## Limits

- Two model pairs, three benchmarks, one review prompt; the sign patterns may not hold for other prompts, larger capability gaps or open-ended tasks.
- The null draft is one design of "no content"; scaffold and content are defined relative to it, so a different null would shift the split.
- The additive split is an accounting of three counterfactuals, not a causal proof of independent mechanisms.
- Draft-quality threshold is read from few pairs (one weak result at 18.0% generator accuracy); no threshold was estimated.
- I read the abstract, method, MCQ and start of code results, not the diagnostic case analysis or appendices.

## Related

- [[peer-as-verifier]] — another case of one model checking another's output
- [[solve-verify-detection-gap]] — separates solving from checking ability
- [[generative-verification]] — verification as a distinct capability from generation
- [[chain-of-inquiry-scaffolding-effect]] — structure itself as a source of gain

[^c1]: arxiv-2604-01029 — "x3 : Re-solving control. The reviewer receives only the question and answers it directly,"
[^c2]: arxiv-2604-01029 — "The scaffold effect captures"
[^c3]: arxiv-2604-01029 — "each in a Primary setting"
[^c4]: arxiv-2604-01029 — "re-solving contributes +56.6 pp and +30.4 pp, respectively"
[^c5]: arxiv-2604-01029 — "its helpful and harmful influences mostly"
[^c6]: arxiv-2604-01029 — "the content effect is significantly negative"
[^c7]: arxiv-2604-01029 — "Weak drafts add"
[^c8]: arxiv-2604-01029 — "than as an unassigned residual"
[^c9]: arxiv-2604-01029 — "No prompt in any condition reveals the identity of the model that produced the draft."
[^c10]: arxiv-2604-01029 — "They distinguish information transfer from downstream"
