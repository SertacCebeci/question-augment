---
description: "Before a theorem prover checks a reasoning step, the LLM writes in the valid but unstated assumptions it leans on; without them, steps that read as valid fail for lack of a premise."
aliases: ["soft unification", "autoformalization with soft unification", "implicit-assumption surfacing before formal check"]
sources: ["arxiv-2512-18196"]
---
# Soft unification before formal checking

A symbolic checker judges an inference only against the premises it is handed, and natural language routinely leaves a bridge unsaid. The paper's example is that "humans recognize Dad and Father as equivalent," while a symbolic system treats them as distinct predicates, so a step a human reads as valid is rejected as a formal error.[^c1]

The mechanism is a prompt placed before formalization. The LLM is asked to "supplement valid but implicit assumptions within each reasoning step that are not stated in Pr," and the premises, with these assumptions added, are then parsed into an event-semantics form and converted into an Isabelle theory.[^c2][^c3] The paper's reading is that natural language "often omits implicit information or assumptions that humans can easily interpret but symbolic systems cannot."[^c4] Its reported effect is at two levels: more traces pass the syntax check, and this "allows more reasoning traces to be verified by the Theorem Prover."[^c5]

Where a step still fails, the paper iterates. The LLM is prompted to "refine the Soft Unification in the reasoning step using the error messages" until the prover accepts the step or an iteration limit is reached.[^c6] On the synthetic refined subset the mean average reward is reported to rise from 0.47 to 0.6.[^c7]

The distinction that matters for asking and answering is this. A formal verdict of "invalid" conflates two cases: a bad inference, and a good inference whose bridge was never written down. The paper's own diagnosis separates them, since some inferences "appear valid but are judged invalid due to missing information, such as unstated assumptions."[^c8] Soft unification handles the second case by making the bridge an explicit premise, so the check runs on what the answer actually relies on. That the move transfers beyond logic is my inference, not a result of the paper; the related notes below show the same move, naming what is left unsaid, in other settings.

## Limits

- The added assumptions are written by the same LLM whose step is being checked. The paper asks for assumptions that are "valid," but the text I read reports no check of them beyond the prover's acceptance of the augmented theory (my reading). A step can pass because it brought its own bridge.
- Refinement rewrites the bridge against the prover's error messages until the step passes. The paper does not report how often refinement added an assumption the original text did not contain, so part of the 0.47 to 0.6 rise may measure the prover accepting rewritten assumptions (my inference).
- The authors say the process is still imperfect: "the auto-formalization process is still imperfect." Their proposed remedy is to ask rather than assume: "pipelines that proactively ask clarification questions to resolve these ambiguities."[^c9][^c10] Soft unification itself resolves ambiguity silently, and the paper does not compare the two.
- The method is tested on NLI and logical-reasoning benchmarks with a fixed premise set. Open-ended questions, where no premise set exists to be surfaced against, are not tested.

## Related

- [[refutation-based-entailment-check]] — the prover check that the surfaced premises feed; the paper's Logic Validity is a check of this family.
- [[implicit-requirement-recovery-bottleneck]] — recovering unstated requirements of a whole task; here the unstated item is one bridge inside a single inference.
- [[implicit-subject-resolution-injection]] — another route that writes down what the prompt leaves unnamed.
- [[process-outcome-consistency-verification]] — the lucky-guess failure that step checking is meant to expose.

[^c1]: arxiv-2512-18196 — "humans recognize Dad and Father as equivalent"
[^c2]: arxiv-2512-18196 — "supplement valid but implicit assumptions within each reasoning step that are not stated in Pr"
[^c3]: arxiv-2512-18196 — "we parse the Pr with Soft Unification"
[^c4]: arxiv-2512-18196 — "natural language often omits implicit information or assumptions that humans can easily interpret but symbolic systems cannot"
[^c5]: arxiv-2512-18196 — "This allows more reasoning traces to be verified by the Theorem Prover"
[^c6]: arxiv-2512-18196 — "refine the Soft Unification in the reasoning step using the error messages"
[^c7]: arxiv-2512-18196 — "which rises from 0.47 to 0.6"
[^c8]: arxiv-2512-18196 — "judged invalid due to missing information, such as unstated assumptions"
[^c9]: arxiv-2512-18196 — "the auto-formalization process is still imperfect"
[^c10]: arxiv-2512-18196 — "pipelines that proactively ask clarification questions to resolve these ambiguities"
