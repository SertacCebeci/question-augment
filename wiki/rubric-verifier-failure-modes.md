---
description: "Rubric verifiers that RL exploits fail in three structural ways: they credit part of a compound criterion, treat unstated content as stated, or match at the wrong level of specificity."
aliases: ["partial-compound failure", "implicit-as-explicit failure", "imprecise verification", "verifier failure taxonomy"]
sources: ["doi-10-48550-arxiv-2605-12474"]
---
# Rubric verifier failure modes

When a rubric verifier is wrong in a way that RL can exploit, the errors are not random. The paper takes every criterion-level incorrect credit, asks a strong model to write one sentence on the structural reason the failure happened, and clusters those sentences. The clusters fall into three families.[^c1]

**A. Partial compound.** The criterion asks for several elements, and the verifier is satisfied by some of them. Two sub-cases: a missing conjunct, where the criterion "requires A and B" and the verifier is satisfied by only one; and an incomplete enumeration, where the criterion requires N items and the verifier accepts fewer.[^c2] Both are the same error: a conjunction or a count is read as a disjunction or a lower bound.

**B. Implicit as explicit.** The verifier treats something absent or unstated as if the criterion were met.[^c3] Sub-cases: inferred content, where "the required claim was never stated" and the verifier infers it from context; and a missing supporting element, where "the main claim is present but the required rationale, contrast, or qualifier is" absent.[^c4]

**C. Imprecise verification.** The verifier matches at the wrong level of specificity. Concept substitution accepts "a related but distinct concept as equivalent"; topical alignment checks "only broad topic relevance rather than the precise claim."[^c5]

The paper counts 53,447 criterion-level incorrect credits across the four main runs, and reports that the proportions of these modes are nearly the same for the weak and strong verifier.[^c6] Its reading is that the patterns "reflect fundamental limitations of rubric verification rather than blind spots specific to a particular model."[^c7] This is what makes the taxonomy useful beyond one verifier: the same kinds of error recur, so a grader that is sound on one failure family may still fail on the others (my inference, not tested in the work).

## Limits

- The categories are the paper's clustering of one-sentence explanations written by one model (GPT-5.4), each conditioned on the rubric and on the verifier's and panel's own explanations. Another clustering could split or merge them. The full definitions and examples are in the paper's appendix, which I did not read.
- The taxonomy describes which credits were wrong, not how often a given criterion type appears in the rubrics. The paper reports proportions in a figure whose values are not recoverable from the text I read, so I do not state them.
- The "same across verifiers" claim is about mode proportions in two medical and science runs with one policy family (Qwen2.5). It is not tested on other rubric types or on human graders.
- The paper does not test a fix that targets a given family. Its own conclusion is that "making rubric-based RL robust will require not only better verifiers, but also reward design that more directly accounts for undesirable behavior" — that is a claim about reward design, not about any one failure family.
- Whether a conjunct-checking or specificity-checking grader would reduce the corresponding failure is my inference; the work does not run one.

## Related

- [[verifier-exploitation-rate]] — the measurement that finds these incorrect credits; the taxonomy is what the paper does with them
- [[judge-master-key-false-positives]] — a different reference-judge failure: content-free openers accepted as correct
- [[judge-coverage-overestimation]] — judges rate incomplete reasoning as complete, which is the same kind of error as a partial compound credit at the level of a whole chain
- [[violation-enumerated-rubric-verdict]] — a grading format that checks for violations rather than presence; a candidate defence against implicit-as-explicit errors, untested against these modes
- [[rubric-formation-gap]] — the criteria themselves can be missing or wrong, a source of error that sits upstream of any verifier

[^c1]: doi-10-48550-arxiv-2605-12474 — "a single sentence describing the structural reason the failure happened"
[^c2]: doi-10-48550-arxiv-2605-12474 — "criterion requires A and B; verifier is satisfied by only one"
[^c3]: doi-10-48550-arxiv-2605-12474 — "treats something absent or unstated as if the criterion"
[^c4]: doi-10-48550-arxiv-2605-12474 — "the main claim is present but the required rationale, contrast, or qualifier is"
[^c5]: doi-10-48550-arxiv-2605-12474 — "checks only broad topic relevance rather than the precise claim"
[^c6]: doi-10-48550-arxiv-2605-12474 — "the mode proportions are nearly identical"
[^c7]: doi-10-48550-arxiv-2605-12474 — "fundamental limitations of rubric verification rather than blind spots specific to a particular model"
