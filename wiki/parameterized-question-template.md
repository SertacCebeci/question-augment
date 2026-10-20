---
description: "A question written as a template with named input slots, plus a program that computes its answer for any values, yields many checkable instances from one problem."
aliases: ["dynamic benchmark", "parameterized benchmark", "question template with input slots", "dynamic question generation", "fully parameterized problem"]
sources: ["arxiv-2512-05954"]
---
# Parameterized question template

A usual question is one text with one answer. A parameterized question is a template: it names input variables and constants, the question and its worked solution refer to them by symbol, and a program computes the answer for any assignment of values. SymPyBench describes its items this way: "Each problem is fully parameterized, supporting an effectively infinite range of input configurations,"[^c1] and each comes with "executable Python code that produces the ground-truth solution for any parameter set".[^c2]

The mechanism runs in stages. A language model first writes each question as a structured record with input variables, output variables, constants, a question and a reasoning step. "At the conclusion of this process, each question is represented in a structured JSON format encompassing these five components."[^c3] The question text and the solution are then rewritten with symbols "drawn from the Input Variables, Output Variables, and Constants fields",[^c4] so that the same symbol means the same quantity wherever it appears. A code model writes a function over those symbols. The code is kept only if, run on the original values, its outputs match the expected outputs: "If the computed outputs match the expected Output Variables".[^c5] The paper reports that this check passes for "approximately 88% of problems".[^c6]

The consequence for evaluation is that one problem can yield a family of instances, each with a key that the program computes. The paper adds three rephrasings per question: "generate three textual variations of each question".[^c7] A family like this is what a group-level score needs; that scoring is described in variant-group-consistency.

## What it does for the asker

A template makes an input slot explicit. The question says which values are needed and leaves them open until the answerer supplies them. INTENT.md describes the asker as one who opens slots for constraints and the answerer as one who supplies them. A template is that picture written as data (my reading, not the paper's framing).

The paper's one probe of the slot side is omission. Its benchmark can be used "by selectively omitting critical variables and analyzing how often models hallucinate versus recognize under-specified".[^c8] The one example is a question that leaves out a diffusion coefficient. Given that version, the model "does not request the missing value or flag the input as".[^c9] It invented a scenario and answered that. The authors say they "plan to formalize this capability and systematically benchmark hallucination rates across model families".[^c10]

## Limits

- The probe is an anecdote. One omitted variable, one model, one case described in a paragraph. The paper does not measure how often models ask for a missing value; it proposes to. Whether a template can separate asking from fabricating at scale is untested.
- The key is only as good as the template and the code. Both come from an LLM. The check is that code reproduces the original numbers, so a template whose formula is wrong, but whose code matches it, passes. This is my inference from the check's definition.
- The 12% of problems whose code failed the check are not described in the text I read. The surviving families are the ones a program could solve, a selection I cannot size from the text.
- "Effectively infinite" describes the parameter space of each template, not the coverage of physics. The corpus is "a large-scale synthetic benchmark of 15,045 university-level physics problems".[^c11] The variety is across physics templates, not across kinds of question.
- A template fits questions with a closed-form computation. Open conceptual questions, or questions whose answer is a judgement, do not reduce to a program; the paper does not discuss that boundary and this is my inference.
- Fresh numbers do not prove that a model has not memorized the template's wording. The paper's variants change numbers and phrasing, and do not test memorization directly.

## Related

- [[program-computed-ground-truth]] — there the answer is a program run over simulator geometry, written per question and checked by a vote; here the program is generated with the template and checked against the template's own numbers.
- [[ground-truth-first-corpus-generation]] — another route where the answer key exists before the text; this template is the object whose slots are filled.
- [[recoverability-gated-ask-abstain]] — what an answerer should do when a needed value is missing: ask when a reply could supply it. The omission probe above is the test for that behaviour.
- variant-group-consistency — the scoring that the template's families make possible.
- [[post-cutoff-corpus-benchmark-isolation]] — avoiding contamination by building the test set after a cutoff; a template avoids it differently, by making each instance new through substitution (my inference).

[^c1]: arxiv-2512-05954 — "Each problem is fully parameterized, supporting an effectively infinite range of input configurations"
[^c2]: arxiv-2512-05954 — "ground-truth solution for any parameter set"
[^c3]: arxiv-2512-05954 — "At the conclusion of this process, each question is represented in a structured JSON format encompassing these five"
[^c4]: arxiv-2512-05954 — "placeholders drawn from the Input Variables, Output Variables, and Constants fields"
[^c5]: arxiv-2512-05954 — "If the computed outputs match the expected Output Variables"
[^c6]: arxiv-2512-05954 — "generate correct code for approximately 88% of problems"
[^c7]: arxiv-2512-05954 — "generate three textual variations of each question"
[^c8]: arxiv-2512-05954 — "selectively omitting critical variables and analyzing how often models hallucinate versus recognize under-specified"
[^c9]: arxiv-2512-05954 — "when prompted with this version, Gemini does not request the missing value or flag the input as"
[^c10]: arxiv-2512-05954 — "In future work, we plan to formalize this capability and systematically benchmark hallucination rates across model"
[^c11]: arxiv-2512-05954 — "a large-scale synthetic benchmark of 15,045 university-level physics problems"
