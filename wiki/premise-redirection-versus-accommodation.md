---
description: "Clinicians answer questions built on false premises by correcting the premise and not answering as asked; LLMs flag the premise yet still accommodate it by supplying the requested advice (60-80%)."
aliases: ["redirective communication", "false assumption accommodation", "redirection"]
sources: ["arxiv-2601-09853"]
---
# Premise Redirection Versus Accommodation

Patients often embed false assumptions in a question without intending to. The clinical skill is redirection: "addressing the implicit misconception and then responding to the underlying patient context, rather than the original question."[^c1] The question asked is deliberately left partly unanswered. MedRedFlag collects 1100+ Reddit health questions where clinician answers diverge from the question asked, a mismatch used to detect that redirection took place.[^c2]

Two separate measurements are needed. "Addressed" asks whether the response corrects the false assumption. "Accommodated" asks whether the response still gives information that implicitly accepts it; physicians write a per-question condition, for instance "Does the response describe splinter removal?" for a diabetic patient who needs emergency evaluation. Any such instructions count as accommodation even alongside a warning.[^c3] An LLM judge agreed with physicians 93% of the time on both metrics.[^c4]

On 100 test questions, GPT-5 addressed the premise in 88% of cases yet accommodated it in 73%. Claude Opus 4.5 scored 78% and 60%. Llama-3.3-70B scored 50% and 74%, and Qwen-3-32B 72% and 80%.[^c5] The authors conclude that "correcting a false assumption alone is insufficient to prevent harmful accommodation."[^c6] Physicians also saw the correction "drowned out" by volume: in 3 of 10 GPT-5 responses that did address the premise, 5% or less of the text was devoted to it.[^c7]

The split persists when identification is made free. Given an oracle list of the false assumptions, addressing rose to 92-100%, but even the best configuration (Claude Opus 4.5) still accommodated 33%.[^c8] Prompting the model to identify assumptions first did not change addressing and only lowered accommodation modestly; retrieval-augmented generation generally lowered addressing while reducing accommodation.[^c9] The authors name two separable challenges: identifying the premise, relatively strong, and refraining from answering what was built on it, less explored. They tie the second to alignment that treats helpfulness as "answering the question asked."[^c10] Physicians also observed diagnostic anchoring: a question framed around an assumed diagnosis is answered on that diagnosis without first examining the broader symptoms.[^c11]

For asking and answering, the point is that a good answer to a premise-laden question can require withholding the requested content, and that evaluating only whether the flaw was named misses the failure.

## Limits

Only 100 test questions and five models were evaluated, with a GPT-5 judge (Claude Opus 4.5 as a check). Reddit r/AskDocs questions may not match other patient populations. The tie to reward-driven sycophancy is the authors' interpretation, not tested here. Whether always redirecting harms questions that should be answered was checked in an appendix only. Mitigations were inference-time prompts and retrieval, not training.

## Related

- [[detection-correction-gap]] — the same pattern, diagnosis present but answer not aligned to it, in causal claims
- [[false-premise-question]] — the general phenomenon of questions that rest on false premises
- [[sycophantic-capitulation]] — agreeing with the user, a candidate cause
- [[frictive-intervention]] — redirection as a deliberate dialogue move that resists task completion
- [[wise-refusal]] — refusal after diagnosis

[^c1]: arxiv-2601-09853 — "addressing the implicit misconception and then responding to the underlying patient context,"
[^c2]: arxiv-2601-09853 — "a dataset of 1100+ questions sourced from Reddit that require redirection"
[^c3]: arxiv-2601-09853 — "Does the response describe splinter removal?"
[^c4]: arxiv-2601-09853 — "concordance between the physicians and the LLMas-a-judge were 93%"
[^c5]: arxiv-2601-09853 — "Percentage of 100 questions in MedRedFlag where models explicitly addressed any false assumption"
[^c6]: arxiv-2601-09853 — "correcting a false assumption alone is insufficient to"
[^c7]: arxiv-2601-09853 — "drowned out"
[^c8]: arxiv-2601-09853 — "still accommodated 33% of questions with"
[^c9]: arxiv-2601-09853 — "The RAG approach generally worsened performance on"
[^c10]: arxiv-2601-09853 — "Aligned models typically interpret helpfulness"
[^c11]: arxiv-2601-09853 — "diagnostic anchoring"
