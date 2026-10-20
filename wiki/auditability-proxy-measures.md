---
description: "Auditability of a generated program is proxied by a structural check for user-defined predicates and constraints, and by embedding similarity of its variable names to the task."
aliases: ["auditability metric", "structural validity", "semantic similarity of variable names", "program auditability score"]
sources: ["arxiv-2512-07407"]
---
# Auditability proxy measures

An auditable program is one a reader can check step by step against the problem. Nothing in a program's execution shows that property: a Prolog program that returns the right number may be a single line. A study that wants to speak of auditability has to define it as something measurable on the generated text. The Prolog-as-a-tool study defines two such measures, and they are the only auditability readouts in the text.

The first is structural validity. A static analyzer checks whether "the generated Prolog code includes at least one user-defined predicate other than solve/1" and at least one arithmetic constraint in braces.[^c1] The authors say the check "captures the cases where the LLM reasons mainly in natural language and only emits a final" solve statement.[^c2] It is a presence test. A program passes by having the parts a derivation would need, and the check does not test whether those parts compute the right thing. That is my reading of what the test can and cannot see.

The second is semantic similarity. The generated logic is compared with a reference Prolog program by cosine similarity over embeddings. The authors say "We have devised this metric to measure auditability."[^c3] The argument is that renaming variables does not change what a program computes, yet "it contributes to auditability when the variable names are semantically related" to the concepts in the task.[^c4] The argument is plausible, but the study does not test it against human readers.

What the two readouts do in the study: under the correctness-only suite, the most accurate Struct configuration scores 1.60% on structural validity and 8.27% on similarity, which is the low end the authors use to describe a model that reasons in prose (see [[accuracy-auditability-trade-off]]). Under the Declare prompt the structural score depends on the reward: "SP-Declare improves from 49.60% (Rwd1) to 94.67% (Rwd3) in structural validity."[^c5] The authors' reading is that the measure responds to the structure they reward. My reading is stronger: the measure reports what was rewarded, so a high score tells a reader that the reward worked, not that a reasoner can be audited.

## Limits

- Both measures are the authors' own constructs. The read text reports no human judgement of whether a program is auditable, so the measures have not been checked against the thing they are named after.
- The structural measure is syntactic. It tests for a predicate and a brace constraint, not for a derivation that follows the problem's steps.
- Semantic similarity is a reward term in some suites. Suite 2 "adds semantic similarity via Sentence-BERT embeddings and predicatename overlap."[^c6] On those suites a rise in the score is partly a rise in the training target, so it is not independent evidence of auditability.
- The name-relatedness argument is an argument. Whether a reader finds a program with semantically named variables easier to check is not tested in the study.
- All readouts come from one task (elementary arithmetic) and one small model, with the limits stated in [[accuracy-auditability-trade-off]].

## Related

- [[accuracy-auditability-trade-off]] — the measured trade-off these two scores are used to describe.
- [[reward-overoptimization]] — the general pattern in which a proxy score rises while the quantity it stands for need not; here the proxy is partly the reward.
- [[tool-integrated-reasoning]] — the loop whose generated code these measures would be applied to.

[^c1]: arxiv-2512-07407 — "the generated Prolog code includes at least one user-defined predicate other than solve/1"
[^c2]: arxiv-2512-07407 — "the LLM reasons mainly in natural language and only emits a final"
[^c3]: arxiv-2512-07407 — "We have devised this metric to measure auditability"
[^c4]: arxiv-2512-07407 — "it contributes to auditability when the variable names are semantically related"
[^c5]: arxiv-2512-07407 — "SP-Declare improves from 49.60% (Rwd1) to 94.67% (Rwd3) in structural validity"
[^c6]: arxiv-2512-07407 — "adds semantic similarity via Sentence-BERT embeddings and predicatename overlap"
