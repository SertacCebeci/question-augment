---
description: "A formal specification can typecheck and still be weak, vacuous or off-task; it carries information only if it separates correct implementations from plausible wrong ones."
aliases: ["specification nonvacuity", "semantic bite of a specification", "vacuous specification", "wrong implementation rejection", "specification discrimination"]
sources: ["arxiv-2511-21104"]
---
# Specification nonvacuity

A specification written for a proof assistant has to pass the elaborator, and passing says little about whether it means what was intended. The BRIDGE paper states the gap directly: "A specification that compiles is not necessarily meaningful."[^s1] Its list of failure modes is "It may be too weak, too strong, vacuous," and unrelated to the task.[^s1] Vacuity is the extreme case: a predicate that holds for every input, or for none, is well-formed and constrains nothing.

The paper's working test is about what the specification does, not how it is written. A specification has "semantic bite" when it can tell a correct implementation from a plausible wrong one. The authors ask "can they help distinguish correct implementations from reasonable wrong ones" and measure this separately from form.[^s2] Their battery for specifications is "elaboration, nonvacuity, correct implementation acceptance, wrong implementation rejection, and downstream usefulness."[^s3] The reason for the test is that a specification which compiles but accepts everything does no work: "a specification that typechecks but accepts both" correct and incorrect code is of little use to verification.[^s4]

The mechanism has two halves that a single check does not join. Nonvacuity asks whether the specification constrains anything at all. Discrimination asks whether what it constrains is the right thing. A specification can be non-vacuous and still accept a wrong program. It can also reject correct programs while being satisfied by no sensible one. The paper measures both and does not claim that one implies the other. In the paper's results, generated specifications "are often useful as discriminators," which the authors read as evidence that they are "not merely syntactically valid or vacuous."[^s5]

The test needs both kinds of implementation. Acceptance of the correct program means little unless wrong programs are rejected, and rejection of a wrong program means little if the specification rejects everything. This pairing is my reading of the two measured quantities; the paper lists them and does not write out the argument.

The same problem appears for theorem statements. "A theorem statement can elaborate while still being weak,"[^s6] and the paper applies the same kinds of check, nonvacuity and implementation relevance, to them. The specification side also has a practical yield. The authors report that specification reasoning helps code generation as well: "specification reasoning yields gains of up to 17.5 percentage points" in conventional Python generation.[^s7] A specification is therefore useful as a planning object before any proof exists, and the nonvacuity question applies to it in either role.

## Limits

The discriminator is only as strong as the wrong implementations it is tested against. The paper's "reasonable wrong ones" are those its generations and benchmarks supply. A specification that rejects every wrong program tried is untested on the rest, and the text gives no way to enumerate the wrong programs that matter.

The tasks are narrow. "The tasks are still mostly local and algorithmic," and the paper has not tested "rich stateful or effectful programs, long horizon proofs, or multi module verification." Nothing here shows that the nonvacuity test scales to specifications about state, effects or large libraries.

The checks are diagnostics, not guarantees. The authors write that the diagnostics "do not eliminate false confidence."[^s8] A specification that passes them has earned more trust, but the text does not say how much more, and a vacuity check cannot tell whether a non-vacuous specification states the intended property.

Results also depend on setting: "Results also vary across models, prompts, and search budgets."[^s9] The paper's own language for the gains is an "inductive bias," not a universal improvement.

## Related

- [[executable-answer-verification]] — a check that runs the candidate through an interpreter; a specification's discrimination test is an executable check of the same family, applied to the task statement rather than to an answer.
- [[test-weakening-task-specification]] — an executable specification used as the task itself; the nonvacuity question carries over to a test that may be too weak to reject anything.
- [[structured-specification-generation]] — a multi-part specification given to a model as input; this note asks whether a specification, once written, constrains anything.
- [[verifier-discrimination-and-calibration]] — a verifier's ability to separate good from bad outputs is one property among others; discrimination here is the same property for a formal specification.
- [[generation-verification-gap]] — the proof-side question of when checking is easier than producing; nonvacuity decides which statement is worth proving at all.

[^s1]: arxiv-2511-21104 — "A specification that compiles is not necessarily meaningful."
[^s2]: arxiv-2511-21104 — "can they help distinguish correct implementations from reasonable wrong ones"
[^s3]: arxiv-2511-21104 — "correct implementation acceptance, wrong implementation rejection, and downstream usefulness."
[^s4]: arxiv-2511-21104 — "a specification that typechecks but accepts both"
[^s5]: arxiv-2511-21104 — "generated specifications are often useful as discriminators"
[^s6]: arxiv-2511-21104 — "A theorem statement can elaborate while still being weak"
[^s7]: arxiv-2511-21104 — "specification reasoning yields gains of up to 17.5 percentage points"
[^s8]: arxiv-2511-21104 — "these do not eliminate false confidence"
[^s9]: arxiv-2511-21104 — "Results also vary across models, prompts, and search budgets"
