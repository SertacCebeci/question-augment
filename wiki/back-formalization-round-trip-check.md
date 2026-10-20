---
description: "Before a formal statement is trusted, it is compiled, then translated back to prose and judged equivalent to the original step; only steps that survive both checks go on to proof."
aliases: ["back-formalization", "round-trip formalization check", "back-translation check", "formalization equivalence check"]
sources: ["arxiv-2511-18760"]
---
# Back-formalization round-trip check

A formal statement can compile and still say something other than what the informal step said. The check described in HERMES is a second test on the translation itself, separate from whether a proof is found. The formal statement is first compiled; the validated code is then rendered back into informal language, and a language model judges whether that back-translation is equivalent to the original step.[^c1] Only a statement that passes both tests is forwarded to the prover; otherwise the formalizer is run again.[^c2]

The two tests answer different questions. Compilation asks whether the statement is well-formed: it "guarantees that the prover module is provided with valid code" and with well-defined premises and goals.[^c3] The round trip asks whether the well-formed statement means what the step meant. A compiled theorem can be the wrong theorem, and a prover will prove whatever it is handed. My inference, not the paper's claim: the round trip is the only check in the pipeline aimed at that gap, which is why it is worth naming as its own concept.

## The retry budget

Both tests draw on one budget. The paper says "the number of attempts to obtain a valid formalization is controlled by the parameter" Kf, the formalization budget.[^c4] Since a statement is forwarded only when the round trip accepts it, "valid formalization" here includes the equivalence judgement, not just compilation (my reading of the paragraph). The sensitivity run reports that "increasing Kf from 1 to 4 yields a massive" gain on the hardest benchmark, a figure the authors attribute to "mitigating formalization errors."[^c5] That gain is for the formalizer as a whole, so it does not isolate the round trip.

## What was measured about faithfulness

The paper does not report the round trip's own error rate. Its faithfulness evidence is about the formalizer's output. A human-led audit labelled 100 steps, half where the prover succeeded and half where it failed, and defined translation accuracy as the share of steps where "human experts verified the formalization as semantically faithful to the original statement."[^c6] Separately, the authors say "qualitative inspection" of the formalizer's output shows that "over 80% of these steps are faithfully translated into Lean."[^c7] These are two different instruments with different denominators, and the paper reports both without reconciling them.

Coverage is a third quantity. It is the share of formalized steps for which the prover found a proof, and it is reported as "our 75% coverage rate."[^c8] A step can be faithfully translated and still unproved, and an unproved step is not evidence of a bad translation.

## Limits

- The round trip is not ablated. The paper removes the memory buffer and the prover, and states that "The formalization and feedback modules are not ablated."[^c9] Whether the equivalence check changes final accuracy is therefore not measured.
- The judge is a language model. The equivalence decision is made by an LLM, the kind of evaluator the paper's introduction distrusts for reward signals. No error rate for the back-translation judgement is reported.
- A shared misreading survives. If the formalizer and the back-translator make the same mistake, the two informal texts agree and the check passes. This is my inference; the paper does not test it.
- The faithfulness figures are for DeepSeek-V3.2 outputs and for mathematics in Lean 4. The authors claim the design "remains relevant for non-mathematical applications," and they add "verification environments beyond Lean4," but that is untested.[^c10]
- Transfer to questions is my inference, not a result. One could write a question's constraints as a formal specification, render it back into prose, and compare it with the original. The paper offers no evidence for this, and natural questions rarely have a formal target to round-trip into.

## Related

- [[soft-unification-premise-surfacing]] — the same pipeline shape in another paper: the step is rewritten to carry its unstated premises before the prover sees it; the round trip here tests the translation after it is made.
- [[selective-symbolic-translation]] — a structural and a semantic check that reverts a rejected translation; the closest relative of the round trip.
- [[formalizability-routing]] — decides which claims can be formalized at all, before any translation is attempted.
- [[tool-grounded-self-verification]] — a verdict grounded in a tool run; there the tool re-checks a reasoning step, here a compiler and an LLM check the translation of the step.

[^c1]: arxiv-2511-18760 — "the validated Lean code is backformalized into informal language, and the LLM evaluates"
[^c2]: arxiv-2511-18760 — "If the two are deemed equivalent, the formalization module forwards the Lean statement to the prover"
[^c3]: arxiv-2511-18760 — "This verification guarantees that the prover module is provided with valid code"
[^c4]: arxiv-2511-18760 — "The number of attempts to obtain a valid formalization is controlled by the parameter"
[^c5]: arxiv-2511-18760 — "increasing Kf from 1 to 4 yields a massive"
[^c6]: arxiv-2511-18760 — "human experts verified the formalization as semantically"
[^c7]: arxiv-2511-18760 — "over 80% of these steps are faithfully translated into Lean"
[^c8]: arxiv-2511-18760 — "our 75% coverage rate"
[^c9]: arxiv-2511-18760 — "The formalization and feedback modules are not ablated"
[^c10]: arxiv-2511-18760 — "This flexibility ensures the design remains relevant for non-mathematical applications"
