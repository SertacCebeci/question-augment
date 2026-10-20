---
description: "A multi-part specification (pre/post-conditions, invariants, intent) given to an LLM in place of prose let strong models regenerate all 45 modules; a few-shot baseline reached 81.8%."
aliases: ["specification-guided code generation", "specification-driven generation", "formal-methods-guided generation", "generative file system specification"]
sources: ["arxiv-2512-13047"]
---
# Structured specification as the generation request

Where the request to an LLM is a natural-language prompt, this work writes it as a multi-part specification and asks the generator for an implementation that satisfies that specification. The premise is that prose cannot carry the constraints a system needs: "one cannot simply instruct an LLM to" avoid race conditions and expect a correct outcome.[^c1] The replacement keeps natural language but fixes its form: specifications are "expressed in structured natural language augmented with type annotations rather than pure mathematical logic", organised into functionality, modularity and concurrency sections.[^c2] The authors write that these designs "significantly limit the potential for misinterpretation."[^c3] Repairing the prompt by asking before generation is a different route ([[clarify-before-generate-specification-repair]]); here the precise form is written by the developer up front.

Each part does a different job. Functionality uses pre- and post-conditions: "we adapt the classic Hoare logic formalism of" {P}C{Q}, so each function states the state it requires and the state it guarantees.[^c4] Invariants hold across all states; a root-existence invariant lets generated code omit null checks on the root. Modularity uses rely-guarantee contracts so modules can be developed separately, and concurrency states the locking protocol explicitly. Pre- and post-conditions say what a function must do but not how, and the authors note that "an LLM could correctly generate a bubble sort" as easily as a quicksort.[^c5] So a system algorithm, or a lighter natural-language intent, carries the how; the authors report that "a high-level intent is often" sufficient for simpler functions and that "the necessary level of detail scales with complexity."[^c6]

The authors do not call the result formal. "While not strictly formal, these specifications provide a sufficiently precise blueprint" for the generator.[^c7] An LLM "enforces adherence to this logic during code generation", in the role a theorem prover would play in full verification.[^c8] The precision is therefore a property of the request, and the check on the answer is a separate step.

## What was measured

The test system is SpecFS, a userspace in-memory file system in C, re-implemented from the design of AtomFS as 45 modules. A generated module counts as correct only if it passes the functional tests and "is deemed logically equivalent to the groundtruth through manual inspection."[^c9] Two baselines are few-shot prompts to the same models: a normal one with a description and the dependency APIs, and an oracle one that also includes the dependency code. With the same specification, the stronger models generated the full set: Gemini-2.5-Pro and DeepSeek-V3.1 reach 100%, "completely generating all functional modules of" SpecFS.[^c10] The oracle baseline, which also gets the ground-truth code of its dependencies, reached 81.8% with the most capable model.[^c11]

The ablation in the paper's Table 3 is reported in the text only in summary. The functionality specification "alone is insufficient for correctly generating complex file system" code, mainly because of interface mismatch; adding the modularity specification supports the concurrency-agnostic modules; "that is not enough to accurately produce thread-safe modules," which the concurrency specification and agent self-validation address.[^c12][^c13] The headline comparison is with naive prompting, where the paper reports correctness gains for complex operations "prompting (up to 34.4%)."[^c14]

Evolution is handled as a change to the request. "A developer writes a patch containing either new specifications or modifications to an old one," and the toolchain regenerates the implementation so the change propagates.[^c15] The authors report integrating ten Ext4 features this way.[^c16] Accuracy on those features was higher than on the from-scratch modules, which the authors attribute to features "implemented primarily through modifications to existing specifications."[^c17]

The request is also checked by a second agent. A separate SpecEval agent "reviews the output against the specification", and its failures return as feedback into a retry loop.[^c18] The argument is that "verifying a solution against a set of rules is a simpler cognitive task than" generating it.[^c19] That is an argument from the authors' experience; it is not measured in the sections read here, and it is the same pattern as [[generate-then-verify-candidate-pipeline]].

The cost is on the asking side: "this paradigm usually demands a greater upfront investment in design."[^c20]

## My reading

From the asker's side the specification is a set of slots. A precondition names what the caller must supply, a postcondition names what the answer must make true, and an invariant names what may never change. The answer is then checked slot by slot. This is close to what [[answer-structure-specification]] does for the shape of an answer, applied here to the constraints on its content. (My inference: the paper does not describe its specification this way.)

## Limits

- One system and one domain. The specification was written by the authors, who know the design they are reproducing. The paper does not test a specification written by someone outside the design, or a deliberately underspecified one.
- The comparison is against few-shot prompting of the same models. Those baselines do not get the two-phase generation or the SpecEval retry loop, so "specification versus prose" is confounded with the rest of the toolchain. The 34.4% figure's configuration was not read in full.
- The claim that the structure limits misinterpretation is asserted, not measured in the sections read. No run was read that counts ambiguity in a prose request against the same request written as a specification.
- Correctness rests on functional tests plus manual equivalence. The system fails 64 of 754 test cases, which the authors attribute to unimplemented functionality.[^c21] The manual step is a judgment, not a blind check.
- Nothing is proved. The guarantee is the generator's reliability plus the reviewer's, not a formal verifier's.
- Transfer is untested. Nothing here tests specification-style requests to people, to retrieval, or to answers that are not code.

## Related

- [[clarify-before-generate-specification-repair]] — the same upstream repair of a request before generation, done there by a clarifying agent that asks the user; here no question is asked and the developer writes the precise form.
- [[answer-structure-specification]] — fixes the shape of the answer in the query; here the constraints on the content are fixed in the request.
- [[test-weakening-task-specification]] — also replaces a prose task with a checkable form, an executable test instead of a specification.
- [[generate-then-verify-candidate-pipeline]] — the SpecEval reviewer and retry loop are a generate-then-verify loop.
- [[ambiguity-taxonomy]] — the kinds of underspecification a specification is meant to close.

[^c1]: arxiv-2512-13047 — "one cannot simply instruct an LLM to"
[^c2]: arxiv-2512-13047 — "expressed in structured natural language augmented with type annotations rather than pure mathematical logic"
[^c3]: arxiv-2512-13047 — "significantly limit the potential for misinterpretation"
[^c4]: arxiv-2512-13047 — "we adapt the classic Hoare logic formalism of"
[^c5]: arxiv-2512-13047 — "an LLM could correctly generate a bubble sort"
[^c6]: arxiv-2512-13047 — "the necessary level of detail scales with complexity"
[^c7]: arxiv-2512-13047 — "While not strictly formal, these specifications provide a sufficiently precise blueprint"
[^c8]: arxiv-2512-13047 — "replacing the role of a formal theorem prover"
[^c9]: arxiv-2512-13047 — "is deemed logically equivalent to the groundtruth through manual inspection"
[^c10]: arxiv-2512-13047 — "completely generating all functional modules of"
[^c11]: arxiv-2512-13047 — "generation using the most capable Gemini-2.5-Pro is 81.8%"
[^c12]: arxiv-2512-13047 — "the functionality specification alone is insufficient for correctly generating complex file system"
[^c13]: arxiv-2512-13047 — "that is not enough to accurately produce thread-safe modules"
[^c14]: arxiv-2512-13047 — "prompting (up to 34.4%)"
[^c15]: arxiv-2512-13047 — "a developer writes a patch containing either new specifications or modifications to an old one"
[^c16]: arxiv-2512-13047 — "seamlessly integrating 10 real-world features from Ext4"
[^c17]: arxiv-2512-13047 — "implemented primarily through modifications to existing specifications"
[^c18]: arxiv-2512-13047 — "reviews the output against the specification"
[^c19]: arxiv-2512-13047 — "verifying a solution against a set of rules is a simpler cognitive task than"
[^c20]: arxiv-2512-13047 — "usually demands a greater upfront investment in design"
[^c21]: arxiv-2512-13047 — "failing only 64 out of 754 test"
