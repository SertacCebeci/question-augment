---
description: "A conclusion is valid when premises plus its negation are unsatisfiable; a theorem prover can then label each reasoning step provable, refutable or unknown, not just the final answer."
aliases: ["entailment check by refutation", "proof-path validity", "logical validity by refutation", "step-level entailment verification"]
sources: ["arxiv-2512-23511", "arxiv-2512-18196"]
---
# Refutation-based entailment check

Validity here is a relation between premises and a conclusion, not a judgment of how plausible the conclusion sounds. A conclusion C follows from premises P when every interpretation that satisfies P also satisfies C. An automated theorem prover tests this by refutation: it looks for a derivation showing that P together with the negation of C is contradictory. "The prover mechanistically attempts to find a syntactic proof for the unsatisfiability of" P ∪ {¬C}.[^c1] Because first-order logic is sound and complete, a proof found this way settles the entailment: "finding such a proof provides a definitive confirmation of the original semantic entailment".[^c2]

The arXiv work arxiv-2512-23511 (the MATP framework) applies this check to reasoning chains rather than only to answers. Each intermediate statement is labelled provable, refutable, or indeterminate given the premises, and a search looks for a subset of the correct steps that together entail the conclusion or its negation.[^c3] If such a subset exists, "it indicates that the reasoning chain is logically sound."[^c4] The output is a graded classification of the chain, not a single accuracy bit.

Why this separates the route from the answer: in the paper's motivating example, two models reach the same correct conclusion, but one chain has "steps 3 and 7 introduce unsupported information while step 13 contradicts the premises," and the chain as a whole still fails to support the conclusion, "indicating that the answer might be coincidental."[^c5][^c6] The authors' summary is that "answer accuracy alone fails to capture reasoning strength."[^c7] This is the same failure that [[process-outcome-consistency-verification]] describes as lucky guessing, here checked by a prover instead of a learned verifier.

What transfers from logic and what does not. The criterion transfers: entailment from explicit premises is a precise, checkable standard, and refutation gives a yes-or-no answer where it terminates. What does not transfer is the setting the criterion needs. The premises must be explicit and fixed. The paper's own text says some mappings "require external knowledge not present in the premises," so an entailment that holds in common sense can fail the check for lack of a premise. The check is only as good as the translation that produces the formulas; see nl2fol-translation-bottleneck.

Used as a training reward. arxiv-2512-18196 (LogicReward) places a theorem-prover check of each step inside a training reward. The paper uses Isabelle to verify each inference from the premises it cites; the step's Logic Validity is 1 when the formal theory is syntactically and logically valid, 0 when it parses but the prover rejects it, and a token-probability confidence when the syntax fails.[^c12][^c13] Reasoning validity averages over the steps, and the final score averages it with a 0/1 outcome term at equal weights.[^c14] Among reward variants trained under equal settings, the authors report that the LogicReward-trained model "achieves the highest overall average performance (71.4)".[^c15] Whether a prover check of a step is the same family as the one above is my reading: both ask whether a step follows from its premises, but the paper's prover is Isabelle applied to a formalization the LLM produced.

## Limits

- The inputs are deductive by construction: each task gives premises and a candidate conclusion, and "by design, it is guaranteed to either logically follow from" the premises or contradict them.[^c8] The benchmark therefore never contains a conclusion the premises leave open, although the method has an "indeterminate" label for steps.
- Ground truth for the benchmark is a "manually annotated label", so the check's accuracy is measured against human labels on that data, not against an independent oracle.[^c9]
- The reported margin, "outperforms prompting-based baselines by more than 42 percentage points in macro F1-score," is the authors' comparison on their own benchmark of 10,830 instances from 10 LLMs.[^c10] I have not seen it replicated, and the baselines' strength is not described in the part of the text I read.
- Open-ended questions, where there is no premise set to refute against, are outside the method. The authors note that "supporting reverse reasoning could broaden applicability," which places reverse inference outside what is tested; open-domain tasks are not tested.[^c11]
- An "unknown" result is a real outcome, not a pass; it says the prover could not decide, which is different from the step being wrong.
- In the LogicReward reward the prover verdict is one input among several, and the fallback to token confidence means a step's score is not always a prover verdict. The authors name the cost: the labeling process is "relatively slower than approaches that only compare final outcomes."[^c16] The text I read does not report how often the fallback fires (my reading).

## Related

- nl2fol-translation-bottleneck — the formalization step this check depends on, and where most of its failures come from
- [[process-outcome-consistency-verification]] — the same lucky-guess failure, checked by a learned verifier on math derivations

[^c1]: arxiv-2512-23511 — "the prover mechanistically attempts to find a syntactic proof for the unsatisfiability of"
[^c2]: arxiv-2512-23511 — "finding such a proof provides a definitive confirmation of the original semantic entailment"
[^c3]: arxiv-2512-23511 — "refutable, or indeterminate based on the premises"
[^c4]: arxiv-2512-23511 — "exists, it indicates that the reasoning chain is logically sound."
[^c5]: arxiv-2512-23511 — "steps 3 and 7 introduce unsupported information while step 13 contradicts the premises"
[^c6]: arxiv-2512-23511 — "indicating that the answer might be coincidental"
[^c7]: arxiv-2512-23511 — "answer accuracy alone fails to capture reasoning strength"
[^c8]: arxiv-2512-23511 — "By design, it is guaranteed to either logically follow from"
[^c9]: arxiv-2512-23511 — "A manually annotated label"
[^c10]: arxiv-2512-23511 — "outperforms prompting-based baselines by more than 42 percentage points in macro F1-score"
[^c11]: arxiv-2512-23511 — "supporting reverse reasoning could broaden applicability"
[^c12]: arxiv-2512-18196 — "we use the theorem prover Isabelle"
[^c13]: arxiv-2512-18196 — "we fall back to the confidence"
[^c14]: arxiv-2512-18196 — "For simplicity, we set w1 = w2 = 0.5"
[^c15]: arxiv-2512-18196 — "achieves the highest overall average performance (71.4)"
[^c16]: arxiv-2512-18196 — "relatively slower than approaches that only compare final outcomes"
