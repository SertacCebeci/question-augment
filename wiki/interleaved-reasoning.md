---
description: "A reasoning model alternates unobserved thinking with user-facing intermediate responses, and when the first response is a plan, a user can correct the route before the long reasoning runs."
aliases: ["Plantain", "plan-first interleaved reasoning", "Plan-Answer interleaving", "think-and-surface interleaving", "IR"]
sources: ["arxiv-2512-03176"]
---
# Interleaved reasoning

The usual reasoning model runs in one pattern: a prompt, then one long block of thought, then an answer. The user sees nothing until the end. Interleaved reasoning changes the shape of the output rather than its length. The model "alternates between thinking and surfacing intermediate responses, as an alternative to the standard 'think-then-answer' approach."[^c1]

The unit that reaches the user is defined by what it allows. The paper defines an intermediate response as "a self-contained, usable" piece of information that shows how the model reads the user's intention and what it plans to do.[^c2] The point of the definition is the failure case: "When this understanding or plan is incorrect, it should be possible for the user to act" on it at once, without waiting for the final answer.[^c2]

The specialization the paper studies is plan-first. There the first intermediate response is "an explicit, step-by-step plan for executing the task," and the stated benefit is that this "allows for user intervention and early feedback for subsequent reasoning steps."[^c3][^c4] A plan is short and checkable, so it can be judged before the long reasoning has been spent on it.

The behavior has to be trained. Naive prompting does not produce it: "Models prompted in this way often collapse the plan generation into the reasoning trace and revert to the" standard format.[^c5] The recipe is synthetic interleaved traces from a larger model, supervised fine-tuning on them, and then reinforcement learning in which the format is a gate: rewards are applied "only when the interleaved format is satisfied."[^c6] So the interleaving is a property of the weights, not of the instruction.

## What is measured

The paper's latency measure is time-to-first-response (TTFR): "TTFR captures the number of thought tokens generated before the first user-visible response," which is the initial plan.[^c7] Its authors concede that this is a proxy: "token count does not map linearly to wall-clock time, it provides a reliable model-agnostic proxy for" response latency.[^c8] On the reported results, the abstract claims a reduction of TTFR "by over 60% relative to think-then-answer baselines."[^c9] Table 1 reads "Plan-first decoding (Plan-Answer) substantially lowers time-to-first-response (TTFR) while" maintaining or improving pass@1 against the Think-Answer baseline.[^c10] Latency and accuracy are two separate numbers in the paper; the claim is that the first does not cost the second.

The paper's comparison that matters for this wiki is where feedback lands. Plan-level evaluation is set against answer-level feedback: "Unlike answer-level feedback that arrives only after full reasoning," the plan-level check "intervenes before subsequent reasoning begins, allowing the model to revise" a faulty plan.[^c11] The paper reports that "Early plan-level feedback guides reasoning toward correct solution paths, yielding up to +2–3%" higher accuracy at much lower TTFR.[^c12]

## Relation to the asker's side

The motivation is conversational. Human speakers "perform lightweight, incremental grounding acts to ensure that participants in the conversation are on" the same page.[^c13] My inference: the transfer that survives is the timing. An answerer who commits to a checkable reading early gives the asker a place to correct it, and the cost of a wrong early reading is one short plan rather than a full wrong derivation. What does not survive is the typed machinery of grounding. The paper's intermediate responses are model plans, not discourse units with acknowledgement or repair, so the typing in [[grounding-act-discourse-unit]] does not apply to them.

Two nearby mechanisms share words without sharing the object. [[asynchronous-reasoning]] also shows a visible answer while the model still thinks, but it does so by re-indexing one cache and asking a probe whether the thinking is ahead; interleaved reasoning emits discrete responses that were trained in. [[chain-of-thought-interleaved-retrieval]] interleaves retrieval calls with reasoning; here the interleaving is between thought and the user.

## Limits

- The user is simulated. The paper states that "we simulate the human using an autorater that provides feedback on candidate plans."[^c14] The autorater sees the prompt and the plan but not the thoughts, which is a deliberate "information asymmetry", but no human user was studied. The authors name human studies as "an important next step".[^c15]
- The benefit is shown on verifiable tasks: "Plantain focuses on structured, verifiable tasks where plan correctness can be automatically assessed."[^c15] The paper lists ambiguous or under-specified prompts as future work, though those are the cases where an early plan would matter most.[^c16]
- The training data is small. The SFT set is "125 total interleaved reasoning traces," built on coding prompts and then tested on math, text-to-SQL and reading comprehension.[^c17]
- The intermediate responses are graded by an LLM as "helpful or not helpful."[^c18] No human judged whether a surfaced plan was useful to someone acting on it.
- TTFR counts tokens, not seconds, and the judge that gates plans adds its own cost: it "introduces nontrivial latency and may reflect biases of the" underlying model.[^c19]

## Related

- [[plan-prefix-rewind]] — the inference-time procedure that uses the first plan as a gate, rejecting and resampling only the plan
- [[asynchronous-reasoning]] — a visible answer during thought by a different mechanism, a shared cache rather than trained intermediate responses
- [[grounding-act-discourse-unit]] — the conversational grounding this paper cites as its motivation, typed per utterance
- [[chain-of-thought-interleaved-retrieval]] — interleaving retrieval with reasoning, not thought with user-facing responses
- [[plan-level-retrospection]] — a model revising its own plan mid-run; the plan here is surfaced to a user before the reasoning goes on

[^c1]: arxiv-2512-03176 — "we propose interleaved reasoning (IR), in which the model alternates between thinking"
[^c2]: arxiv-2512-03176 — "When this understanding or plan is incorrect, it should be possible for the user to act"
[^c3]: arxiv-2512-03176 — "intermediate response is an explicit, step-by-step plan for executing the task"
[^c4]: arxiv-2512-03176 — "allows for user intervention and early feedback for subsequent reasoning steps"
[^c5]: arxiv-2512-03176 — "Models prompted in this way often collapse the plan generation into the reasoning trace and revert to the"
[^c6]: arxiv-2512-03176 — "applied only when the interleaved format is satisfied"
[^c7]: arxiv-2512-03176 — "TTFR captures the number of thought tokens generated before the"
[^c8]: arxiv-2512-03176 — "token count does not map linearly to wall-clock time, it provides a reliable model-agnostic proxy for"
[^c9]: arxiv-2512-03176 — "reducing time-to-first-response by over 60% relative to think-then-answer baselines"
[^c10]: arxiv-2512-03176 — "Plan-first decoding (Plan-Answer) substantially lowers time-to-first-response (TTFR) while"
[^c11]: arxiv-2512-03176 — "plan-level evaluation intervenes before subsequent reasoning begins, allowing the model to revise"
[^c12]: arxiv-2512-03176 — "Early plan-level feedback guides reasoning toward correct solution paths, yielding up to +2–3%"
[^c13]: arxiv-2512-03176 — "perform lightweight, incremental grounding acts to ensure that participants in the conversation are on"
[^c14]: arxiv-2512-03176 — "we simulate the human using an autorater that provides feedback on candidate plans"
[^c15]: arxiv-2512-03176 — "An important next step is to conduct human studies evaluating the perceived usefulness,"
[^c16]: arxiv-2512-03176 — "We also plan to extend evaluations to scenarios with ambiguous or under-specified user prompts"
[^c17]: arxiv-2512-03176 — "resulting in 125 total interleaved reasoning traces used for SFT"
[^c18]: arxiv-2512-03176 — "which labels each segment as helpful or not helpful"
[^c19]: arxiv-2512-03176 — "introduces nontrivial latency and may reflect biases of the"
