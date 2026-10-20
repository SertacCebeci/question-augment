---
description: "Q-Guide is an LLM agent that each turn judges what visual evidence a question still needs, calls a targeted perception tool to recover it, and stops on a confidence-and-verification gate."
aliases: ["Q-Guide", "question-guided evidence acquisition", "question-conditioned evidence acquisition", "question-conditioned perception"]
sources: ["popa-2026"]
---
# Question-conditioned evidence acquisition (Q-Guide)

> Instead of encoding a document once and answering from whatever that pass
> extracted, the agent asks, turn by turn, what this particular question
> still needs and spends compute recovering exactly that.

## Definition / Mechanism

Popa (2026) casts document VQA as a loop over an evidence state
$e_t=(q,\mathcal{D},O_t)$ rather than a single encoding pass: "instead of
committing to one fixed encoding, the model should spend a little extra
compute at inference time working out what to look at next, and only then
answer. We build this into Q-Guide, a small agent that reads a question,
works out what evidence it is still missing, and calls targeted tool(s) to
recover it."[^c1]

At each turn the same policy (one MLLM) both selects which of five
[[recovery-postulate|recovery]] tools to invoke — text, visual-detail, targeted-lookup, spatial,
or structure recovery — and judges a [[sufficient-statistic|sufficiency]] predicate $\phi$ over the
accumulated observations. Termination is confidence-gated: the policy
emits a self-reported confidence level, and "high- and medium-confidence
answers pass directly, while a less-confident submission commits only if
verification backs it and otherwise abstains — a test applied by the
policy itself, not a separate critic module."[^c2]

On DocVQA2026 and M109NC (Manga109-based character naming), across three
Claude backbones, "Q-Guide outperforms both direct prompting and recent
multi-agent document systems (65.0% vs. 40.0% on DocVQA2026, 32.4% vs.
24.4% on M109NC)."[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| The paper's own system name | Q-Guide | exact |
| Descriptive term used in this note | question-conditioned evidence acquisition | exact — same object, named by its mechanism rather than the system |

[^c6]

## Why it matters

This is a selection mechanism (stall 2) with no formal value function: no
[[entropy]] drop, no EIG, no submodular guarantee is computed anywhere in the
loop — the policy's own judgment of "what's still missing" stands in for
all of them. The paper's central ablation reports that this beats adding
structure to the selection process rather than depending on it: "The
3-stage research pipeline reaches only 35.7% — below the Visual+OCR
baseline — and Advisory Routing (44.3%) merely matches Extract-Synthesize:
the bottleneck is not the absence of a plan. … Basic agentic reasoning
reaches 50.0% and Q-Guide 65.0%, a 37.5-point improvement over Visual
Prompt — the payoff is in perceptual recovery tools, not orchestration
complexity."[^c4]

Accuracy also scales with how many rounds the loop is allowed, then
plateaus: "accuracy grows with the perception budget … from 40.0% at
Tmax = 1 to 55.0% at Tmax = 2 and ∼65% at Tmax ≥ 3, after which it
plateaus — most of the gain is already captured within two to three
deliberate rounds."[^c5]

For this stall that is an empirical bound on how many selection rounds a
myopic, unformalized "what's missing" criterion needs before it saturates
— a number a formal greedy criterion ([[adaptive-submodularity]]) would
have to match without a proof that it will.

## Limits

- The claim that orchestration does not help rests on one paper's own
  ablation, on two small benchmarks (80 questions across 8 categories for
  DocVQA2026), with one family of backbones (Claude Opus/Sonnet 4.6, Opus
  4.5) and the authors' own re-implementation of the compared baselines —
  it is not a general result about planning or routing.
- The termination gate's confidence threshold and verification check are
  applied by the same policy that selected the evidence, not calibrated
  against a held-out labelled sample the way [[abstention]]'s certified
  thresholds are; no risk guarantee is claimed for it.
- Accuracy is capped by the quality of what the tools recover: "Q-Guide is
  only as good as the text it can read" — M109NC accuracy rises from 21.8%
  (no text) to 32.4% (its own OCR) to 53.7% (ground-truth text).[^c7]

## Related

[[abstention]] · [[adaptive-submodularity]] · [[mutual-information]] · [[value-of-information]]

[^c1]: popa-2026 — "instead of committing to one fixed encoding, the model should spend a little extra compute at inference time working out what to look at next, and only then answer. We build this into Q-Guide, a small agent that reads a question, works out what evidence it is still missing, and calls targeted tool(s) to recover it"
[^c2]: popa-2026
[^c3]: popa-2026 — "Q-Guide outperforms both direct prompting and recent multi-agent document systems (65.0% vs. 40.0% on DocVQA2026, 32.4% vs. 24.4% on M109NC)"
[^c4]: popa-2026 — "The 3-stage research pipeline reaches only 35.7%—below the Visual+OCR baseline—and Advisory Routing (44.3%) merely matches Extract-Synthesize: the bottleneck is not the absence of a plan."
[^c5]: popa-2026 — "accuracy grows with the perception budget (Fig. 8, right): from 40.0% at Tmax = 1 to 55.0% at Tmax = 2 and ∼ 65% at Tmax ≥ 3, after which it plateaus—most of the gain is already captured within two to three deliberate rounds."
[^c6]: popa-2026 — "We build this into Q-Guide, a small agent that reads a question, works out what evidence it is still missing, and calls targeted tool(s) to recover it"
[^c7]: popa-2026
