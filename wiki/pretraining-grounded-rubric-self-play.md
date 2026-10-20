---
description: "Grounding a self-play LLM's own query, rubric and grading in the same sampled pre-training document narrows the generation-verification gap and lifts open-ended task scores."
aliases: ["POP", "Post-trains LLMs for Open domains with Pretraining text"]
sources: ["arxiv-2604-20051"]
---
# Pretraining-grounded rubric self-play

> The same document that seeded the question is handed back to the model when it grades the answer, so self-play's asker and its judge share one piece of ground truth neither of them wrote.

## Definition / Mechanism

Self-play post-training has one model synthesize a task, solve it, and score its
own solution; outside math and code, where a checker exists, the scorer has
nothing but the model's own judgment to lean on, and can drift into rewarding
whatever it already produces. POP (Huang et al. (2026)) grounds
every stage of a non-verifiable self-play round in one sampled pre-training
document $d$, in three roles run by the same base model: a Proposer that reads
$d$ and writes a query $x$ and a reference answer $y_{ref}$; a Solver that samples
$J$ candidate answers to $x$ without seeing $d$; and a Verifier that, conditioned on
$d$, $x$, $y_{ref}$ and the candidates, writes a query-specific rubric and grades each
candidate against it, extracting a gold label from $d$ for criteria that have one.
"Crucially, we ground the framework on a content-rich pretraining corpus to (1)
enable an exploitable generation-verification gap and reduce reward hacking, and
(2) prevent mode collapse." Only the highest- and lowest-scored candidates
become the preferred/dispreferred pair for DPO training — the rubric never enters
training directly, only through this selection.

## Why it matters

Prior self-play work stayed inside verifiable domains because an ungrounded
self-judge is free to certify its own output. POP measures the gain from
grounding directly: "POP increases performance of both the pretrained base model
and instruction-tuned model on multiple tasks ranging from long-form healthcare
QA to creative writing and instruction following." An ablation isolates the
grounding's own contribution: "Removing grounding of our rubric evaluation on the
pre-training document reduces the overall performance to 29%. We suspect this to
be a result of an insufficient generation-verification gap and an increase in
reward hacking." The selection rule this trains on is coarse — only the
extremes of a noisy ranking are kept — yet it still produces a usably correct
signal: "pairing the highest and lowest scored responses produces mostly correct
training signals."[^c4]

## Limits

The generation-verification gap the grounding buys is real but small: on the
paper's own measurement, grounded self-grading correlates with a stronger
teacher model's rankings at Spearman's r = 0.34, against 0.33 ungrounded —
reward hacking is reduced, not closed. The pairwise accuracy of the kept
extremes (85% grounded vs. 82% ungrounded) is what actually licenses training on
them; a weaker gap would not. Validating "true quality" at all still required an
external teacher model, so the method removes strong supervision from training
but not from evaluation. Results are shown on one base model (Qwen-2.5-7B) and
three tasks; whether the gap holds as the model being trained gets stronger than
its own judge is unverified.

## Related

- [[qcp-guided-self-distillation]] — another self-play framework that keeps a
  privileged artifact from task generation instead of discarding it.
- [[rubric-complexity-normalized-reward]] — a rubric-based RL reward built for a
  different failure mode (rubric size, not grounding).
- [[self-questioning-vlm-grpo]] — a model rewarded for generating its own
  sub-questions, with no grounding document.
- [[factual-novelty-elicitation-reward]] — a self-generated reward scored against
  a fixed corpus rather than a sampled document.

[^c4]: arxiv-2604-20051 — "pairing the highest and lowest scored responses produces mostly correct training signals"
