---
description: "A generated test can build, run and pass while its assertion encodes a wrong expected value; execution checks show that a test runs, not that its expected output is the right one."
aliases: ["executability versus oracle correctness", "runnable but wrong assertion", "compile-and-run pass is not oracle correctness"]
sources: ["arxiv-2511-21382"]
---
# Executability and oracle correctness

A test has two obligations that a runner observes in different ways. It must build and execute, which a compiler and a test runner can see directly. And its assertion must state the behaviour the code ought to show, which no runner can see, because the runner only reports whether the assertion held. A systematic review of 178 LLM unit-test generation publications keeps the two apart: "Compilation and pass rates address executability", while assessing test value "requires measures suited to the objective, including oracle correctness, mutation or held-out fault" detection.[^c1][^c2]

The mechanism follows from that split. A pass on compilation and execution is evidence about the prefix (the objects, inputs and calls) and the environment. It is also satisfied by an assertion that agrees with whatever the code currently does. If the code is faulty, an assertion that copies the faulty output runs green, and nothing in the build or run stage records a defect. The review states the consequence as "Oracle correctness remains a central challenge because assertions can agree with faulty implementations."[^c3] Agreement with a reference does not fix this either: "matching a reference assertion does not establish oracle correctness."[^c4] Textual comparison fails in the other direction too, since "textual similarity cannot determine oracle correctness or fault detection."[^c5] Reasoning before the assertion does not guarantee it: a chain-of-thought rationale "does not guarantee a correct oracle."[^c6]

The review's own summary of the repair loops is that compiler and execution feedback "help make tests executable, although their contributions to oracle" correctness and fault detection vary by task and setting.[^c7] Feedback therefore buys the first obligation. It is not evidence for the second.

## Limits

- The review is a synthesis of published studies. In the parts I read it reports the gap as a recurring pattern across the corpus, with no pooled rate of runnable-but-wrong assertions on one common benchmark. I did not find such a rate.
- The "green test encodes the faulty output" mechanism is my inference from the definitions. The review states the consequence but gives no count of how often it occurs.
- The review also warns that "a method can admit several valid tests, so divergence from a reference need not imply failure."[^c8] The gap runs both ways: a reference match can pass a wrong oracle, and a mismatch can fail a right one.
- The point is about unit tests run by a runner. Outside that setting it transfers only as a structural claim (my inference): a check that confirms an output is well formed or runnable does not confirm that its content is right.
- Execution is not dismissed. The review's claim is that each check supports a different claim about the test. Which claim a given check supports is what this note tracks.

## Related

- [[test-prefix-oracle-split]] — the two obligations are the prefix and the oracle; the gap runs along that boundary.
- [[independent-implementation-check]] — a self round trip can pass while the output is wrong; the same blind spot appears when a single implementation checks itself.
- [[black-box-correctness-ceiling]] — in text-to-SQL, executability is one of several signals that rank correctness only weakly.
- [[program-computed-ground-truth]] — computing the expected value by a program moves it out of a model's reading, one way of narrowing this gap.

[^c1]: arxiv-2511-21382 — "Compilation and pass rates address executability"
[^c2]: arxiv-2511-21382 — "requires measures suited to the objective, including oracle correctness, mutation or held-out fault"
[^c3]: arxiv-2511-21382 — "Oracle correctness remains a central challenge because assertions can agree with faulty implementations."
[^c4]: arxiv-2511-21382 — "matching a reference assertion does not establish oracle correctness."
[^c5]: arxiv-2511-21382 — "textual similarity cannot determine oracle correctness or fault detection."
[^c6]: arxiv-2511-21382 — "its rationale does not guarantee a correct oracle"
[^c7]: arxiv-2511-21382 — "help make tests executable, although their contributions to oracle"
[^c8]: arxiv-2511-21382 — "method can admit several valid tests, so divergence from a reference need not imply failure"
