---
description: "A program can know a security requirement yet guard only part of its input space, passing some tests and failing the full suite: knowing a pattern is not applying it everywhere."
aliases: ["partial security", "partial defence", "partial guard", "coverage failure of requirements"]
sources: ["arxiv-2511-20709"]
---
# Partial requirement coverage

A requirement can be met in part, and a partial answer can look like a whole one on the cases it touches. DualGauge audits the failed security cases of ten models and three coding agents, and finds that the typical failure is not a missing defence. The authors' phrase is that "defenses are present but incomplete."[^p1] The commonest form is an input check. The paper reports that nine of ten input-control failures include a guard, such as a regex, a type check, a length cap or a blocklist, that "looks reasonable but fails to cover the actual attack vector."[^p2]

The mechanism is a matter of coverage against a fixed set of cases. A security suite is a set of adversarial inputs. A guard that handles some of them passes those tests and fails the rest, and a test suite is passed only when every case passes. The authors describe the models as addressing requirements "partially," with enough done "to pass some test cases but not enough to satisfy the full suite."[^p3] The same pattern shows at the call layer, where protection is placed at the "wrong abstraction level."[^p4]

The paper's central reading is about knowledge and application. It says "the problem is not that models lack security knowledge, but that they do not apply it with sufficient coverage."[^p5] The challenge is therefore "consistently applying them across the full space of requirements in a single implementation," whether in one shot or over many iterations.[^p6] On this reading, a model that has a pattern for one case still fails when the implementation must apply the pattern to every case at once.

The agentic results give one more part of the mechanism. An agent that writes its own checks can be satisfied by a guard that the benchmark's suite would reject. "A partial guard that passes the agent's scripts but not" the benchmark's security tests does not trigger a revision, so iteration spends its effort on environment problems and leaves the coverage gap in place.[^p7]

## Limits

- The coverage reading is the authors' interpretation of audits of 30 stratified failed cases per group. The counts in the text ("nine of ten", "14 of 15") are counts inside those audits, not rates over the benchmark.
- No probe in the text separates knowing a requirement from applying it. The conclusion that models "are not unaware" of security requirements is drawn from the partial pattern itself. A test that asked the model to state the requirement and then checked its code would be needed to separate the two, and the paper does not run one.
- Coverage is measured against the benchmark's own suites, which the authors say are "not exhaustively covering all vulnerability classes." A guard that is partial against this suite may be complete against a threat the suite never includes.
- Only specification-only generation with one sample per prompt was measured. Whether the same partiality holds with the specification enumerating the cases is not tested.
- My inference, not the paper's: where a question leaves several constraints open, an answer that satisfies some of them is the same kind of partial object. The paper does not study questions or answers.

## Related

- [[implicit-requirement-recovery-bottleneck]] — there the failure is recovering a requirement the issue never states; here the requirement is known and applied only in part.
- [[rubric-verifier-failure-modes]] — the verifier-side version of the same question: a grader that credits part of a compound criterion.
- [[joint-pass-rate-paired-suites]] — the joint measure that makes partial coverage count as failure.
- [[output-equivalence-blindness]] — a partial guard can match the output of a complete one on the cases a test uses.
- [[structural-versus-semantic-underspecification]] — the functional side of the same paper, where a specification leaves the output contract open and the implementation fills it.

[^p1]: arxiv-2511-20709 — "defenses are present but incomplete"
[^p2]: arxiv-2511-20709 — "fails to cover the actual attack vector"
[^p3]: arxiv-2511-20709 — "enough to pass some test cases but not enough"
[^p4]: arxiv-2511-20709 — "wrong abstraction level"
[^p5]: arxiv-2511-20709 — "but that they do not apply it with sufficient coverage"
[^p6]: arxiv-2511-20709 — "consistently applying them across the full space of"
[^p7]: arxiv-2511-20709 — "a partial guard that passes the agent’s scripts but not"
