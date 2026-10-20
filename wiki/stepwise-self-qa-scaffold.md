---
description: "Questions-of-Thoughts: an ordered plan whose every step gets its own self-generated clarify/verify questions, answers accumulating in a memory; gains on code quality are model- and domain-dependent."
aliases: ["Questions-of-Thoughts", "QoT", "time-series self-QA chain", "per-step self-questioning"]
sources: ["arxiv-2603-11082"]
---
# Stepwise self-QA scaffold

Questions-of-Thoughts (QoT) is an inference-time protocol that wraps an unchanged model. It has three parts: a sequential process chain that splits a goal G into ordered steps S1..Sn; a question-answer chain that, for each step, generates a set of questions meant to "clarify, expand, or verify" that step; and a reasoning knowledge base that stores accumulated answers (the thinking process) and a progressively updated response.[^c1]

## Mechanism

The loop is simple. Generate the steps, then for each step generate its questions, answer each, and append every answer to the thinking-process store. After the last step the final response is rebuilt from that store.[^c2] The questions are not asked once up front. They are tied to the step they check, so each step's question themes differ. In the paper's API-design example, the user-model step asks about uniqueness and password security, while the reservation step asks about double-booking, concurrency and cancellation rules, with 7 to 10 questions per step across 8 steps.[^c3] The questioning is described as Socratic-inspired and iterative; its target is quality criteria (completeness, modularity, security), not only answer correctness.[^c4] The failure policy is crude: an error in step, question or answer generation ends the branch with an error message.[^c5]

This differs from [[chain-of-self-questioning]], which asks what information an answer needs and gates commitment on a threshold. QoT has no gate. Its questions only add content to context. It is a close cousin of [[self-ask-decomposition]], with the plan's ordering and the shared memory as the additions, and of [[dependency-aware-subquestion-scheduling]], though here the order is a fixed linear plan.

## What was measured

Four Llama models (3b, 8b, 70b of 3.1, 70b of 3.3) were run on three backend tasks (API design, data communication, file systems). Outputs were scored 1 to 4 on scalability, completeness, modularity and security by an LLM judge (Gemini 3.1 Pro Preview), blinded as Method A/B/C, with the previous round's code and scores in the judge's context.[^c6]

Against chain-of-thought (CoT), Llama 3.1 70b gained +5.8 in API design and +6.6 in data communication, and +3.2 in file systems; Llama 3.3 70b improved in all three domains.[^c7] Against no QoT, two large models scored negative in file systems (-2.80 and -3.00), which the authors read as possible "over-thinking or over-engineering".[^c8] Small models gained moderately with high variance. The authors suggest, without testing it, that small models write poor intermediate questions that miss key constraints and destabilize the accumulated context.[^c9]

My reading: the scaffold's value depends on question quality at each step, because the questions are the only channel through which constraints enter the memory. A wrong or vacuous question is carried forward unchecked.

## Limits

- Several differences are small beside the reported spread (for example 1.40 ± 2.07, 0.40 ± 2.97, 1.00 ± 2.55 in QoT minus NoQoT), and the number of runs per cell is not stated in the slices read.[^c10]
- Scoring is by a single LLM judge; the rubric is a checklist of observable evidence, but no human agreement is reported in what I read.
- Only Llama models and three Flask-style backend tasks; nothing shows transfer to other tasks or families.
- No ablation separates the plan, the per-step questions and the memory, so which part carries the gain is unknown.
- The over-thinking and small-model-question-quality explanations are the authors' conjectures, not tested.
- Cost: extra generation is acknowledged; no token accounting was read.

## Related

- [[chain-of-self-questioning]] — gated self-questioning before commitment, as opposed to enrichment of context
- [[self-ask-decomposition]] — follow-up questions in the model's own reasoning
- [[dependency-aware-subquestion-scheduling]] — ordering sub-questions by dependency

[^c1]: arxiv-2603-11082 — "the Sequential Process Chain for dependency-aware decomposition,"
[^c2]: arxiv-2603-11082 — "T P ← T P ∪ Answeri,j ▷ Accumulate reasoning"
[^c3]: arxiv-2603-11082 — "double-booking, concurrency, cancellation rules, storage (n=10)"
[^c4]: arxiv-2603-11082 — "Inspired by the Socratic method, this module allows"
[^c5]: arxiv-2603-11082 — "the system terminates"
[^c6]: arxiv-2603-11082 — "the evaluation process is"
[^c7]: arxiv-2603-11082 — "QoT demonstrates substantial improvements of +5.8 in"
[^c8]: arxiv-2603-11082 — "This phenomenon suggests a potential"
[^c9]: arxiv-2603-11082 — "smaller models may generate lower-quality intermediate questions"
[^c10]: arxiv-2603-11082 — "1.40 ± 2.07"
