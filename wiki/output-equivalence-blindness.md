---
description: "Two programs can return identical outputs and exit codes on ordinary inputs and differ only in their execution trace on adversarial ones, so output matching cannot grade the difference."
aliases: ["observational equivalence of outputs", "output-matching blindness", "trace-only failure", "observationally equivalent implementations"]
sources: ["arxiv-2511-20709"]
---
# Output-equivalence blindness

Two implementations of one specification can be observationally equivalent: same outputs, same exit codes, on the inputs a test happens to use. DualGauge's motivating example makes the point with a file loader specified to return None on error. Both candidate programs return None with exit code 0 on an adversarial path input. One attempts the file access before it fails; the other rejects the unsafe path before any access happens.[^o1] The paper states that "the distinction only emerges on adversarial inputs,", and even then, "only in the execution trace" and not in the output.[^o2]

The mechanism is a matter of what the observable contains. A functional test compares an output with an expected output. If the difference between two programs lies in what they did on the way to the output, a comparison of outputs has nothing to compare. The authors draw the consequence directly: functional tests "are therefore structurally blind to this class of failure," and security evaluation "requires semantic reasoning over runtime behavior."[^o3][^o4] Their remedy is to read the trace: "semantic judgment over the execution trace can serve as the security-test oracle."[^o5] The example is small, but the structure is general: the same output, reached through a different path, gets the same grade under any test that reads only the output.

This is a claim about what a grading rule can see, and it leaves the question open of what the grader should be. A trace is a richer observable, but a reader must still decide which features of the trace count as failure. The paper settles that with an LLM-based evaluator checked against manual judgment, not with a fixed rule.

## Limits

- The argument rests on one worked example (Figure 1) and on the benchmark built around it. The text does not run a controlled comparison of output-only and trace-based graders on the same set of generations and report how their verdicts differ.
- The trace reading is itself a judgment. The paper reports that "although validation shows strong alignment with manual judgment," unfamiliar libraries and ambiguous traces "can still lead to evaluator errors."[^o6] So the blindness moves into the evaluator; it is not removed.
- The claim is about grading. It says nothing about whether a model that sees its own trace would avoid the failure. The paper's agentic results point the other way: "feedback do not automatically overcome the core challenge" of joint correctness and security.[^o7]
- My inference, not the paper's: the same gap between equal outputs and unequal processes could hold in question answering, where two answers can match on the asked-for content and differ in the reasoning that produced them. The paper does not test answers, and nothing here measures that case.

## Related

- [[has-bench]] — process-level metrics computed from execution traces, the same move of scoring the path rather than the outcome.
- [[correctness-congruence-gap]] — a second case where a check on the artefact passes while the purpose it stands for is missed.
- [[joint-pass-rate-paired-suites]] — where this blindness bites: the functional half of a paired suite cannot see the difference the security half is meant to catch.
- [[partial-requirement-coverage]] — a guard that matches the output of a complete one on the cases a test uses.

[^o1]: arxiv-2511-20709 — "As Figure 1 illustrates, a secure and a vulnerable implementation"
[^o2]: arxiv-2511-20709 — "and even then only in the execution trace"
[^o3]: arxiv-2511-20709 — "blind to this class of failure"
[^o4]: arxiv-2511-20709 — "requires semantic reasoning over runtime behavior"
[^o5]: arxiv-2511-20709 — "Thus, semantic judgment over the execution trace can serve as the security-test oracle."
[^o6]: arxiv-2511-20709 — "although validation shows strong alignment with manual judgment"
[^o7]: arxiv-2511-20709 — "feedback do not automatically overcome the core challenge"
