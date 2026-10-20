---
description: "A step evaluator reads a bounded running summary, rewritten each step from the prior summary and the latest tool output, instead of the full growing trajectory, and beats raw history."
aliases: ["recursive trajectory summary", "running summary state", "compressed trajectory summary", "recursively updated summary for a PRM"]
sources: ["arxiv-2511-19314"]
---
# Rolling trajectory summary

An agent's trajectory grows with every tool call, because each tool response can be long. PRInTS keeps that growth away from its step evaluator by maintaining a running summary. At each step the model rewrites the summary from the query, the previous summary, the latest tool response and the current step, so that the summary "captures essential findings and plans up to the current timestep".[^r1] The result is a state rather than a transcript: the input to the evaluator is one summary plus one step, so "This keeps input length bounded".[^r2] Candidate next steps are then scored against that state, not against the raw history.

The summary is written by the same model that scores steps. The model is trained in two parts: supervised fine-tuning "for summarization that recursively updates the trajectory summary", and reinforcement learning for scoring.[^r3] The training target is therefore the summary's use in evaluation, not general compression. The authors describe the aim as "preserving key information needed for step-level evaluation".[^r4] The design choice is that the summary is shaped by what the scorer needs to read, rather than by a fixed rule such as keeping the last few turns.

What it was measured to do. On Qwen3-32B, over FRAMES and GAIA levels 1 and 2, the summary input outperformed the full raw-history baseline "by 7.7% absolute average accuracy".[^r5] Extending the raw history did not help: "extending raw history does not improve performance".[^r6] Among raw windows, the most recent two steps beat one step, four steps, and the full history. The authors read this as "long histories introduce noise and irrelevant information that distract step-level evaluation".[^r7] The ablation's summary sentence is the plainest statement of the claim: "providing compressed summaries outperforms using raw trajectories as input context".[^r8]

So the measured claim is narrow. A bounded, recursively updated state gives a step evaluator better input than the full history, and a short raw window is not enough. It is not a claim that summaries are always the best compression.

## Limits

- The 7.7-point gap comes from one scoring model, Qwen3-32B, and from FRAMES and GAIA levels 1 and 2 only. The ablation did not run on WebWalkerQA or on GAIA level 3, which the authors call low-performing.
- The comparison set is raw windows and the full history. The paper does not compare the summary against other learned compressors or retrieval over past steps, so "summary beats raw" does not show that summaries beat every alternative. This is my inference from the table's scope.
- A summary is lossy by construction. The paper reports the aggregate gain, not cases where a dropped detail changed a step's score. Whether the summary can lose a fact that a later step needs is my inference, not something the paper measured.
- Errors can compound. Each summary is built from the previous one, so a wrong early summary feeds every later step. The paper does not report how far this drift goes over long trajectories; this is my reading of the recursive design.
- The QA samples behind the training data are English: "the underlying QA samples we collected are focused on English queries".[^r9] Whether the rolling summary holds across languages is untested.

## Related

- [[summarized-rationale-verification]] — the nearest relative: a verifier reads a condensed path distilled from one long chain of thought; here the condensed state is rewritten across tool calls
- [[structure-then-select-compression]] — compresses context by discourse structure rather than by a learned rewrite
- [[perception-context-tradeoff]] — the same tension between a rich source and a compressed text, for visual input
- [[counterfactual-retrieval-information-gain]] — the step score that this state is read to predict, in PRInTS estimated from rollouts

[^r1]: arxiv-2511-19314 — "captures essential findings and plans up to the current timestep"
[^r2]: arxiv-2511-19314 — "This keeps input length bounded"
[^r3]: arxiv-2511-19314 — "supervised fine-tuning for summarization that recursively updates the trajectory summary"
[^r4]: arxiv-2511-19314 — "preserving key information needed for step-level evaluation"
[^r5]: arxiv-2511-19314 — "outperforming the full raw-history baseline by 7.7% absolute average accuracy"
[^r6]: arxiv-2511-19314 — "extending raw history does not improve performance"
[^r7]: arxiv-2511-19314 — "long histories introduce noise and irrelevant information that distract step-level evaluation"
[^r8]: arxiv-2511-19314 — "providing compressed summaries outperforms using raw trajectories as input context"
[^r9]: arxiv-2511-19314 — "the underlying QA samples we collected are focused on English queries"
