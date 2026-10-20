---
description: "In multi-turn code refinement, a later request that edits the same component overwrites earlier features; an agent that re-checks prior instructions cut the forgetting rate to nearly zero."
aliases: ["multi-turn forgetting", "cross-turn feature overwrite"]
sources: ["arxiv-2601-04203"]
---
# Cross-turn requirement overwrite

In a multi-turn build, every turn adds to an artifact that earlier turns already shaped. The FronTalk paper calls the resulting loss "forgetting": "features implemented in earlier turns are often overwritten in later turns."[^c1] The mechanism it reports is specific. The failure appears when turns "request modifications to the same component of code (e.g., adding different buttons to the same section)," and the model does not integrate the new request with what is there: it will "overwrite the previous implementation rather than integrate the new feature."[^c2] Both requests may be valid together; the model simply replaces the earlier code.

The paper measures this with a forgetting rate. It is the share of functionality that was correct at an earlier turn and is lost in the final output: the metric counts "how much functionality correctly implemented in prior turns (t < T)" is lost.[^c3] Across the models tested the rate runs "from 4.3% to 44.6%".[^c4] The authors state that "this issue consistently occurs across all leading models"[^c5], and that it is distinct from the long-context degradation that affects only some models.[^c6]

The paper's remedy follows from the mechanism. After each turn a web agent explores the built site and verifies it against both current and past instructions, not only the newest one.[^c7] The identified errors are fed back into the code: "The identified coding errors or oversights are then used to rewrite the code."[^c8] The reported effect is that the forgetting rate falls "to nearly zero," with the final pass rate up by "up to 9.3% with textual instructions."[^c9] An ablation separates the two parts of the check: a variant that critiques only the current turn "improves the pass rate but fails to meaningfully reduce the forgetting rate."[^c10] So the gain comes from re-verifying old requirements, not from a more careful reading of the new one.

The same failure has an answerer-side reading that the paper does not make. A reply can satisfy the latest request while silently dropping an earlier one that is still binding. My inference: this is the mirror of [[user-side-implicit-conflict]], where the user's new turn conflicts with an old requirement and the model fails to notice; here the model's own new edit is the conflicting act.

## Limits

- One benchmark: 100 dialogues of ten turns each, with a fixed turn count. The rate depends on the test cases, which GPT-4o generated and humans then edited. The authors edited 2,783 of the test cases by hand, 73.4% of the total,[^c12] so the measured loss is partly a property of the curated checks.
- The rate is conditional on earlier success. A model that passes little early on has little to forget, so a low rate does not mean the model retains requirements well. My inference from the definition.
- The "nearly zero" figure comes from a critic that is itself an LLM web agent. The evaluation that scores these results reaches moderate to substantial agreement with human annotators, with higher alignment on implementation correctness than on usability,[^c13] so a violation the check does not test can pass unnoticed.
- The single-turn baseline has no forgetting at all: "the single-turn setting eliminates forgetting and long-context degradation."[^c11] The multi-turn setting is the one in which the problem exists, and the paper does not test whether a single-turn restatement of all prior requirements closes the gap in a way that survives long dialogues.
- Only code generation was tested. Whether the same overwrite pattern and the same verifier-based cure hold for prose, plans or other artifacts was not measured.

## Related

- [[user-side-implicit-conflict]] — the user-side version: a new utterance inconsistent with a still-valid requirement, with no revision signal.
- [[contextual-inertia]] — the model copies its previous reply; here it overwrites earlier work. Both are carry-over failures across turns, measured differently.
- [[last-turn-flattening]] — a harness that gives the answerer only the last turn cannot see the earlier requirements at all.
- [[evidence-forgetting-rate]] — shares the word "forgetting" but measures retrieved evidence that is not used, not code that is overwritten. The two should not be merged.

[^c1]: arxiv-2601-04203 — "in earlier turns are often overwritten in later turns"
[^c2]: arxiv-2601-04203 — "overwrite the previous implementation rather than integrating the new feature"
[^c3]: arxiv-2601-04203 — "how much functionality correctly implemented in prior turns (t < T)"
[^c4]: arxiv-2601-04203 — "from 4.3% to 44.6%"
[^c5]: arxiv-2601-04203 — "This issue consistently occurs across all leading models"
[^c6]: arxiv-2601-04203 — "this issue differs from the commonly discussed long-context"
[^c7]: arxiv-2601-04203 — "verify alignment with both current and past instructions"
[^c8]: arxiv-2601-04203 — "The identified coding errors or oversights are then used to rewrite the code"
[^c9]: arxiv-2601-04203 — "to nearly zero, improves the final performance by up to 9.3% with textual instructions"
[^c10]: arxiv-2601-04203 — "fails to meaningfully reduce the forgetting rate"
[^c11]: arxiv-2601-04203 — "the single-turn setting eliminates forgetting and long-context degradation"
[^c12]: arxiv-2601-04203 — "and the editing of 2,783"
[^c13]: arxiv-2601-04203 — "agreement with human annotators, with higher alignment on implementation correctness"
