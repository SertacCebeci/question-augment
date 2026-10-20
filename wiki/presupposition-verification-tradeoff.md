---
description: "Extracting and fact-checking a question's presuppositions before answering raises accuracy on false-presupposition questions but measurably lowers it on true-presupposition ones."
aliases: ["FPQ-TPQ tradeoff", "weak presupposition verification"]
sources: ["wang-2026-well"]
---
# Presupposition-verification tradeoff

> The pipeline that fixes accommodation — extract each presupposition, fact-check it, correct or abstain — does not just add accuracy on questions with false presuppositions (FPQs); it takes accuracy away on ordinary questions (TPQs), because the fact-checker cannot tell "false" from "I could not verify this."

## Definition / Mechanism

Wang, Shwartz & Gonen (2026) evaluate the standard false-presupposition-QA (FPQA) pipeline — extract atomic presuppositions from a question, fact-check each against source documents, then answer, correct, or abstain (the pipeline [[presupposition-accommodation]] cites from Kim et al. 2021) — across four benchmarks ((QA)², CREPE, Syn-QA2, Cancer-Myth), five model families (Gemma, Llama-3, Qwen2.5, OLMo-3, Gemini-3-Flash) and several retrieval conditions. Across almost every method and setting, the method that scores best on FPQs scores worst on TPQs and vice versa: Direct QA (no presupposition check) is the best-scoring method on TPQs and the worst on FPQs because it rarely rejects anything; FP Identification and the Decompose-then-Fact-Check pipeline are the best on FPQs and the worst on TPQs because they reject true presuppositions along with false ones.[^c1]

An ablation isolates the cause: fact-checking accuracy on the *true* presuppositions of TPQs is below 50% in most settings (Cancer-Myth) even where the same fact-checker scores near-perfect on the false presuppositions of FPQs — the module is not discriminating true from false, it is rejecting whatever it cannot verify, and unverifiable-but-true claims are common.[^c2]

## Known as

| Name | Field | Relation |
|---|---|---|
| FPQ-TPQ tradeoff | NLP / QA evaluation (this paper's own term) | exact |
| weak presupposition verification | this paper's title | exact — names the cause, not the effect |

## Why it matters

An agent that adds a presupposition-check step to guard against [[presupposition-accommodation|accommodating a false premise]] is not a free improvement: this measures the cost side of that decision, not just the benefit side. [[value-of-information]] scores a question by what it removes from $W$; here the "question" is the agent's own presupposition-check on an *incoming* question, and its expected value depends on the true/false base rate the agent will actually see (see [[false-presupposition-prevalence]]) weighted against a fact-checking accuracy that is measured, not assumed, to be poor.

## Limits

- The effect is measured with an LLM-as-judge (Gemini-3-Flash) scoring scheme, not human annotation on most items; the authors justify this with an Alternative Annotator Test but it is still one evaluator's judgement standing in for accuracy.
- All benchmarks combine an FPQ set and a TPQ set that were not originally paired for this comparison; Cancer-Myth's TPQ presuppositions were the authors' own manual annotations, not the dataset's.
- The claim is about the *fact-checking* component specifically; it says nothing about presupposition-extraction quality in isolation, since extraction was not ablated separately from fact-checking in the reported tables (§3.2 only breaks out fact-checking accuracy).
- Five model families and four benchmarks, all English-language QA; nothing here is evidence the tradeoff holds for other verification tasks the agent might run before answering.

## Related

[[presupposition-accommodation]] · [[value-of-information]] · [[false-presupposition-prevalence]] · [[expected-information-gain]]

[^c1]: wang-2026-well — "The main takeaway is that across almost all settings, improvement on FPQ resulted in worse performance on TPQ. In particular, the best method for TPQ is Direct QA, which performs especially badly on FPQ as it rarely rejects a false presupposition. Conversely, methods that perform best on FPQ, such as FP Identification, tend to perform worst on TPQ due to rejecting true presuppositions."
[^c2]: wang-2026-well — "Despite achieving near-perfect performance on FPQs, accuracy is below 50% for Cancer-Myth-TPQ and most settings in SynQA2 -FPQ."
