---
description: "A question's answer form decides which checker can grade it: numeric, keyword and per-option answers admit deterministic rules, and only open generative answers need an LLM judge."
aliases: ["answer-type routing", "rule-verifiable answer format", "verifiable answer types", "answer-format verifiability", "assessment-equivalent reformulation", "AER"]
sources: ["arxiv-2511-17405", "arxiv-2511-16205"]
---
# Answer-type verifiability

Whether an answer can be checked by a rule is set by the form the answer takes, and that form can be chosen when the question is written. ReVeL, a rewrite-and-verify pipeline built for multimodal benchmarks, sorts each multiple-choice item by its answer type and rewrites it so that a deterministic checker can grade it. A quantity becomes a numeric prompt that states units and an answer format, and is checked by pattern matching.[^c1] A short name or date becomes a keyword prompt, where the rewrite "enumerates acceptable synonyms or lexical variants" so that exact matching stays fair.[^c2] An item that leans on its option set becomes a list of statements, one per option, and the model returns True or False for each.[^c3] What is left open is graded by an LLM judge. The paper's summary of the division is that "and only the last type may need an LLM".[^c4]

The sorting is a pipeline, not a single label. A rule filter first sends numeric items aside. A lightweight LLM-assisted classifier then assigns the remaining items to a rule-checkable type or to the open type. Each type has its own rewriting prompt, and a refinement pass can refuse a rewrite. For keyword items the refiner rejects answers that are "too broad, such as an explanation, description, list, or complete sentence," because a keyword match would be unreliable there.[^c5] The stated goal is "to maximize deterministic, rulebased evaluation for questions with unambiguous answers," with LLM judging kept for the rest.[^c6]

The paper reports how much of the data this leaves to rules. "Across four benchmarks, 70–96%" of items fall into the rule-checkable types.[^c7] On a sample of responses drawn "across 600" model outputs from three models,[^c8] the hybrid scheme reached "ReVeL achieves an overall accuracy of 98.5%," against 97.3% for a pure LLM judge on the same responses.[^c9] The gain is small, but the rule-checkable part no longer depends on a judge's wording. The same design also gives the training signal: in the reinforcement runs on 20k rewritten items, "Rewards are derived from rule-based exact match."[^c10][^c11]

The transfer beyond benchmarks is my inference, not the paper's. If the answer form fixes the checker, then a question written to need a sentence cannot be graded by a keyword rule however well the rule is built, and a question written to need a number can be graded without any judge. Verifiability is therefore a property the question acquires when it is formulated, and the answerer's output is only checkable to the extent the form allows.

The same move appears in ChemO, an olympiad chemistry benchmark built from IChO 2025, under the name Assessment-Equivalent Reformulation (AER). A problem whose answer is a drawing is rewritten so that the answer is a string: "Draw the structure of A" becomes "Output the SMILES string of A", with a requirement, a problem type and an evaluation method attached to the item.[^c17] The aim is to keep the grading standard while changing the output, turning visual-output problems into ones "requiring symbolic or textual outputs that are assessment-equivalent but computationally tractable for automated evaluation."[^c18] The reason given is practical: when models rendered structures themselves, "generated outputs were difficult to verify programmatically" and exhibited high error rates.[^c19] Chemistry education experts led the reformulation and validated it.[^c20] This is the same claim seen from the answer side: the checker is fixed first, and the question is written to fit it.

## Limits

- The sorting and rewriting are, in the authors' words, "not perfect and may occasionally introduce errors."[^c12] The paper gives no error rate for the rewrite step in the sections I read.
- The judge's own weaknesses are set aside: the authors state the work is "without addressing the inherent fallibility of the LLM-judge itself."[^c13] The open remainder is therefore only as good as the judge that grades it, see [[llm-judge-validation-gap]].
- Rule-based checks break on symbolic answers. The paper's example is a numerical range written with a symbol that has many surface forms, which "presents a significant challenge for any keyword-based or rule-based system."[^c14]
- The numeric route has a fallback. Where a question "cannot be reformulated as a numeric expression," the rewrite returns that it cannot be converted, so the four types do not cover every item.[^c15]
- The stated aim of the rewrite is to "preserve semantics while enabling" deterministic checks.[^c16] I did not find a measure of semantic fidelity in the sections I read; the 98.5% figure measures grading agreement, not whether the rewritten question asks the same thing.
- The judging comparison is one sample of 600 responses across four benchmarks and three models. I did not find in the sections read how the reference labels for that sample were produced.
- The AER equivalence in ChemO rests on expert review. The main text I read gives no error rate for the reformulated items, and the validation details sit in an appendix I did not read (my inference from the sections read).[^c20]

## Related

- [[closed-choice-verifiable-reward]] — the same checkability argument for a closed index choice in image classification; there the answer form is the option index.
- [[llm-judge-validation-gap]] — what an LLM grader misses, which is the risk carried by the generative remainder here.
- [[option-matching-shortcut]] — why an open rewrite is proposed as a route away from matching an answer to its options.
- [[distractor-strength-reward-signal]] — converting multiple choice to open form drops the contrast that distractors carry, the cost the rewrite pays for verifiability.
- [[structured-visual-substitution]] — the other ChemO device: machine-readable encodings of the diagram given to the model, so the input side rather than the answer side is made checkable.

[^c1]: arxiv-2511-17405 — "These will be processed via pattern"
[^c2]: arxiv-2511-17405 — "enumerates acceptable synonyms or lexical variants"
[^c3]: arxiv-2511-17405 — "Each option is converted into a declarative statement, and models output a"
[^c4]: arxiv-2511-17405 — "and only the last type may need an LLM"
[^c5]: arxiv-2511-17405 — "The possible answer of the question is too broad, such as an explanation, description, list, or complete sentence"
[^c6]: arxiv-2511-17405 — "The core principle is to maximize deterministic, rulebased evaluation for questions with unambiguous answers"
[^c7]: arxiv-2511-17405 — "Across four benchmarks, 70–96%"
[^c8]: arxiv-2511-17405 — "across 600"
[^c9]: arxiv-2511-17405 — "ReVeL achieves an overall accuracy of 98.5%"
[^c10]: arxiv-2511-17405 — "converted 20k MCQA examples"
[^c11]: arxiv-2511-17405 — "Rewards are derived from rule-based exact match"
[^c12]: arxiv-2511-17405 — "are not perfect and may occasionally introduce errors"
[^c13]: arxiv-2511-17405 — "without addressing the inherent fallibility of the LLM-judge itself"
[^c14]: arxiv-2511-17405 — "for any keyword-based or rule-based system"
[^c15]: arxiv-2511-17405 — "For questions that cannot be reformulated as a numeric expression"
[^c16]: arxiv-2511-17405 — "with the goal to preserve semantics while enabling"
[^c17]: arxiv-2511-16205 — "Output the SMILES string of A"
[^c18]: arxiv-2511-16205 — "assessment-equivalent but computationally"
[^c19]: arxiv-2511-16205 — "generated outputs were difficult to verify programmatically"
[^c20]: arxiv-2511-16205 — "Chemistry education experts led the reformulation process"
