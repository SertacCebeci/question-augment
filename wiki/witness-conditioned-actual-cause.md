---
description: "A is an actual cause of B if, given a background formula C true in the actual world, not-A would bring not-B; the admissible C decides which factors count."
aliases: ["abstract actual causality", "conditional but-for cause", "witness-relative actual cause", "Halpern-Pass actual cause"]
sources: ["arxiv-2511-21260"]
---
# Witness-conditioned actual cause

The most prominent definition of actual causality is the Halpern-Pearl one, and it is defined on causal models with structural equations.[^c1] Halpern and Pass strip the definition down to its features so that it applies to any model in which counterfactuals are defined. The intuition they start from is "the classic notion of but-for causality used in the law literature".[^c2] A but-for test alone is too weak, so the definition conditions it on a background: A is a cause of B if, conditional on some suitable C, A is a but-for cause of B.

The three conditions are these. A and B both hold in the true state. There is a formula C that holds in the true state and such that, if not-A together with C held, not-B would hold. And A is minimal, so no weaker formula that implies A also satisfies the second condition.[^c3] The paper's own wording is that "our notion says that A is an actual cause of B with respect to a language L". The C is required only to be true where the world actually is: "we just require C to be a formula that is true (in the current state of the world)."[^c4]

The background is what does the work. Take two rocks thrown at a bottle, where Suzy's arrives first. Suzy's throw is not a but-for cause of the shattering, since Billy's rock would have shattered the bottle anyway. It is a cause once Billy's rock is held at the fact that it did not hit the intact bottle: "We can think of ST = 1 as a but-for cause of BS = 1, conditional on BH = 0."[^c5] The same event is a cause relative to one background and not relative to another. The authors make this explicit: "the set of possible witnesses is a parameter".[^c6]

**What survives the transfer.** When the admissible backgrounds are conjunctions of primitive events, the definition reduces to the Halpern-Pearl one: "our definition collapses down to the HP definition of causality (see Theorem 4.2)."[^c7] Allowing a quite restricted form of disjunction in the background recovers the causal-model answers in recursive counterfactual structures.[^c8] What the transfer does not keep is the causal-model reading of negation. In counterfactual structures a formula "not X = x" is evaluated at the closest state where it holds, which need not match the causal-model reading when X is not binary.[^c14]

**The choice is where the answer lives.** Unrestricted disjunction in the background makes the definition empty: "then any formula would become a cause".[^c9] The paper's example is a man in a room with a ticking bomb, defused by a secret combination. Whether running away is a cause of the explosion "would depend on what number combination Bob would enter in the closest world where he does not run away".[^c10] So the verdict is fixed by the background world the question is asked against. A question "was A the cause of B?" is not settled until that background is supplied. That reading is mine, not the paper's, and the paper does not claim people supply it.

## Limits

- The text is a theory. It proves the reductions and gives examples. It does not measure how anyone chooses the background, and it does not claim that people do so in any particular way.
- Whether the short-combination case goes the other way is left open: "if the number combination is short (say, 1 digit), then arguably the HP definition would give the right answer" under the restricted background.[^c11] The authors' own verdicts are hedged with "arguably".
- The counterfactual translation is admitted to be ad hoc: "This definition seems somewhat ad hoc".[^c12] The authors say the framework is applicable to other definitions of causality, but "we have not checked details".[^c13]
- The text gives no general rule for choosing C. The examples are chosen by the authors.

## Related

- [[causal-model-of-explanation]] — Lipton's account gives causes as explanations; this note gives a formal test for which events are causes, which Lipton's abstract does not supply.
- [[realistic-scm-extension-failure]] — the causal-model definition runs on structural counterfactuals; my inference is that the abstract form needs only a model in which counterfactuals are defined, so it is not blocked by the same extension problem.
- [[backtracking-counterfactual]] — the background set also decides whether a causal claim lets upstream variables change; the same choice, seen from the upstream side.
- [[knowledge-relative-explanation]] — the same authors extend the definition from causes to explanations, where what the agent knows fixes which cause counts as an explanation.

[^c1]: arxiv-2511-21260 — "Perhaps the most prominent current definition of (actual) causality is due to Halpern and Pearl"
[^c2]: arxiv-2511-21260 — "the classic notion of but-for causality used in the law literature"
[^c3]: arxiv-2511-21260 — "There is a formula C ∈ L such that C holds (in the true state of the world)"
[^c4]: arxiv-2511-21260 — "we just require C to be a formula that is true (in the current state of the world)"
[^c5]: arxiv-2511-21260 — "We can think of ST = 1 as a but-for cause of BS = 1, conditional on BH = 0."
[^c6]: arxiv-2511-21260 — "the set of possible witnesses is a parameter"
[^c7]: arxiv-2511-21260 — "our definition collapses down to the HP definition of causality (see Theorem 4.2)"
[^c8]: arxiv-2511-21260 — "(a quite restricted form of) disjunctions"
[^c9]: arxiv-2511-21260 — "then any formula would become a cause"
[^c10]: arxiv-2511-21260 — "combination Bob would enter in the closest world where he does not run away"
[^c11]: arxiv-2511-21260 — "then arguably the HP definition would give the right answer"
[^c12]: arxiv-2511-21260 — "This definition seems somewhat ad hoc"
[^c13]: arxiv-2511-21260 — "but we have not checked details"
[^c14]: arxiv-2511-21260 — "But if X is not binary, the two approaches may not agree."
