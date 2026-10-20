---
description: "The label a span's confidence is scored against: the tokens a minimal repair must change for a generated program to pass its hidden tests, an approximate proxy for intent."
aliases: ["minimal intent-aligning patch", "minimal patch label", "minimal repair edit label"]
sources: ["arxiv-2512-24560"]
---
# Minimal patch edit label

A span-level confidence needs a target: which spans were wrong, or in need of change. The work avoids the software term "buggy" for this target. Its reason: "matching intent" is a more general term that can apply outside software, and "this term captures the concept that uncertainty in the generated code might arise from ambiguity in the prompt, rather than model capability."[^m1]

## Mechanism

Intent is operationalized as a test suite. "For our experiments, we assume that intent is fully defined by hidden test cases, and that intent is matched when the generated code passes all the test cases."[^m2] When a generated program fails, the procedure looks for a repair that passes the failed tests and "changes the generated code as little as possible."[^m3] The diff between the generated and repaired programs then gives labels "at the token, line, and problem level."[^m4] A token or line inside the diff is an edited span; one outside it is kept.

The minimality is what makes the label useful. The work observes that "there are often cases where the LLM offers a near-miss solution which looks different from the known solution," and that "a small change to this near-miss solution is adequate."[^m5] So a program can look far from a reference solution and still need a one-line repair. The label records the second fact, not the first. My inference: this makes the target closer to what a reviewer would have to touch than to a similarity to a reference answer.

The work builds such labels over "1000+ problems which challenge even capable models like GPT-4o" and uses them as the ground truth for span confidences (see localized-calibration).[^m6]

## Limits

- Minimality is not computable in general. The authors: "Our process of finding minimal patches is not perfect," and "for general programs we might speculate it is uncomputable to know if a given patch is minimal."[^m7]
- Hidden tests stand in for intent. The authors justify this only as "a reasonable basis for evaluating correctness/intent of generated code."[^m8] A thin test suite produces labels that reflect the suite, not the user. This is an inference from the design, not a measured effect.
- Edited is not the same as wrong. A span can be wrong and untouched, because another span already passes the test. A span in the patch can be a stylistic edit. The label is one repair path; other minimal repairs with different spans may exist. These are my inferences; the work does not measure them.
- The label does not separate the two sources of uncertainty the work names. The text says uncertainty "might arise from ambiguity in the prompt, rather than model capability", but one repaired program cannot show which one produced a given edit.[^m9]
- The method is code-specific. It depends on tests that can be run, which the natural-language extension in the same work does not have.

## Related

- localized-calibration — the calibration this binary target is used to evaluate.
- [[defect-localization]] — the neighbouring fault-localization setting; the work contrasts its own setting with the one that needs failing tests.[^m10]

[^m1]: arxiv-2512-24560 — "this term captures the concept that uncertainty in the generated code might arise from"
[^m2]: arxiv-2512-24560 — "is fully defined by hidden test cases, and that intent is matched when the generated code passes all"
[^m3]: arxiv-2512-24560 — "changes the generated code as little as possible."
[^m4]: arxiv-2512-24560 — "Then we take the diff which gives us labels at the token, line, and problem level."
[^m5]: arxiv-2512-24560 — "a small change to this near-miss solution is adequate."
[^m6]: arxiv-2512-24560 — "using 1000+ problems which challenge even capable models like GPT-4o"
[^m7]: arxiv-2512-24560 — "for general programs we might speculate it is uncomputable to know if a given patch is minimal."
[^m8]: arxiv-2512-24560 — "provide a reasonable basis for evaluating correctness/intent of generated code."
[^m9]: arxiv-2512-24560 — "ambiguity in the prompt, rather than model capability."
[^m10]: arxiv-2512-24560 — "whereas our setting does not assume access to test cases"
