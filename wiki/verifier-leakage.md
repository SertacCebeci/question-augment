---
description: "A verifier whose probes or predicates encode the hidden target can make an exact optimizer look effective; the leaked evidence forces the answer, so a solver comparison becomes vacuous."
aliases: ["verifier leakage", "answer leakage in verifiers", "probe leakage", "non-revealing verification", "vacuous solver comparison"]
sources: ["openalex-org-w7219155344"]
---
# Verifier leakage

An evaluation can reveal its own answer. In closed-loop agent debugging, a verifier turns aggregate observations into conflicts, and a downstream optimizer picks a low-cost set of components that intersects every conflict. The optimizer is then scored on that result. The failure is that the verifier can settle the answer before the optimizer runs, so the score measures the verifier and not the solver. "A verifier can nevertheless make a solver comparison vacuous" is how the paper states it.[^c1]

The mechanism has two parts that each look innocent. A predicate scoped to one named component is one channel. A hard probe that counterfactually intervenes on that same component is the second: "The hard probe intervenes on exactly that component."[^c2] The local response to the probe becomes a singleton conflict naming the planted component. Once singleton propagation runs, every solver inherits the same forced choice. In the development audit, exact minimum hitting set and a propagation-aware greedy method "returned identical supports in 12/12 development cases," and after the explicit anchor predicates were removed, "hard-probe singleton pairs nevertheless matched the planted pair in 9/9".[^c3] The paper's summary: "The optimizer was correct, but the verifier had already disclosed the answer."[^c4]

The general point is that the leak is not one rule that can be deleted. "Removing an explicit anchor rule does not remove this second channel."[^c5] An intervention "may encode its target in the response," so a benchmark that injects faults or exposes privileged state has to document which role each probe plays.[^c6] Passive measurement and counterfactual intervention are different objects for a verifier, and only the second can leak through its own mechanics.

The practical test the paper proposes runs after forced facts are removed: the verifier should report "whether a nontrivial decision remains." If the residual candidate family is empty or singleton in every case, "a solver benchmark cannot support claims about optimizer" quality.[^c7] A stronger audit asks this question, not only whether the solver returns a minimum-cost set. A conventional audit can pass on both solvers and still leave "the scientific comparison" empty.[^c8]

## Limits

- The evidence is small and local. The development audit has 12 plus 9 cases in one simulator with one fitted closed-loop policy. The fault is a deterministic shift of a subset of cells, "A fault shifts a deterministic subset of direction-changeable" cells by one action bucket, so the leak was found for this probe family only.[^c9]
- The leak was found in two channels, and the paper removes both. Finding two does not show there is no third. The paper says the upstream transformations must be red-teamed, "Red-teaming should therefore include target-swapping," together with scope-mismatch and residual-ambiguity tests, but it does not run them on other verifiers.[^c10] Whether those tests catch a channel nobody has named is my inference, not a result.
- The heldout does not compare solvers, so the paper does not show which optimizer is better on a non-leaking verifier: "does not establish localization accuracy."[^c11] The note records the failure of a comparison, not the winner of one.
- The mechanism is shown in one domain (aggregate-trace diagnosis of a decision agent). The transfer to LLM benchmarks is my inference: a judge or rubric that names the expected answer is the same shape of channel, and the paper does not test it there.

## Related

- [[answer-string-leakage]] — the same failure located in the question text: the answer written into a generated question. Here the answer is written into the evaluation's own intervention.
- [[split-order-leakage]] — another evaluation leak that inflates a score through what the evaluator is allowed to see.
- [[rubric-conditioned-contrast]] — a rubric that states the expected answer rewards itself; the same channel from the rubric side.
- [[evidence-eligibility-gate]] — the complementary check. A leak test asks whether the verifier reveals the answer; an eligibility gate asks whether the evidence exists at all. The paper's argument is that both must pass before an optimizer comparison means anything.

[^c1]: openalex-org-w7219155344 — "A verifier can nevertheless make a solver comparison vacuous"
[^c2]: openalex-org-w7219155344 — "The hard probe intervenes on exactly that component."
[^c3]: openalex-org-w7219155344 — "identical supports in 12/12 development cases"
[^c12]: openalex-org-w7219155344 — "hard-probe singleton pairs nevertheless matched the planted pair in 9/9"
[^c4]: openalex-org-w7219155344 — "The optimizer was correct, but the verifier had already disclosed the answer."
[^c5]: openalex-org-w7219155344 — "Removing an explicit anchor rule does not remove this second channel."
[^c6]: openalex-org-w7219155344 — "may encode its target in the response"
[^c7]: openalex-org-w7219155344 — "a solver benchmark cannot support claims about optimizer"
[^c8]: openalex-org-w7219155344 — "pass while the scientific comparison remains empty."
[^c9]: openalex-org-w7219155344 — "A fault shifts a deterministic subset of direction-changeable"
[^c10]: openalex-org-w7219155344 — "Red-teaming should therefore include target-swapping,"
[^c11]: openalex-org-w7219155344 — "does not establish localization accuracy"
