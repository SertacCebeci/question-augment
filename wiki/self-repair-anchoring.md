---
description: "Conditioning a small code model on its own failed attempt before retrying costs accuracy relative to blind resampling, because the model reproduces near-identical code far more often."
aliases: ["self-repair anchoring", "blind-resampling advantage"]
sources: ["verma-2026", "arxiv-2512-18605"]
---
# Self-repair anchoring

> Asking a code model to "fix" its own failed attempt is not free: below 7B
> parameters it costs accuracy and tokens relative to simply asking the
> question again from scratch, because showing the model its prior output
> anchors generation on local edits of that output.

## Definition / Mechanism

At matched token budget on MBPP+ (Qwen2.5-Coder, 1.5B/3B/7B), a
placebo-controlled decomposition separates four retry conditions: blind
resampling (no reference to the failure), a content-free placebo notice,
genuine execution feedback, and feedback plus verbal reflection. "Blind
resampling is the strongest condition below 7B, and remains statistically
tied with the best condition at 7B, while consuming 2.5–5.5× fewer tokens;
conditioning on the model's own failed attempt costs 6.1 points at 1.5B
(p=0.006), and the informational content of execution feedback adds nothing
measurable over the placebo."[^c1]

The mechanism is anchoring: exposure to the prior failed program biases
generation toward local edits of it rather than a fresh attempt at the
solution. "Similarity rises by 0.30 to 0.38 relative to blind resampling at
every scale, and the proportion of retries that are near-identical (>
0.95) rises from 2–14% to 33–68%. Shown its own code, the model edits;
asked afresh, it reconsiders."[^c2]

The penalty shrinks with scale not because feedback becomes useful but
because a larger model's own mistake is a less costly thing to anchor on:
"Anchoring strength is roughly constant across scale, but its cost
declines: a larger model's failed first attempt is a better object to
anchor upon. The diminishing penalty at 7B therefore reflects anchoring
becoming inexpensive rather than feedback becoming useful."[^c3]

Reflection (feedback plus an instruction to diagnose the failure in prose
before rewriting) is the only own-output condition that measurably weakens
the anchor, but it does not pay for the tokens it costs below 7B: "reflection
... is the only own-output condition that measurably reduces anchoring ...
and it is correspondingly the strongest" of the own-output conditions, yet
at 7B it "remains dominated on cost," buying +0.8 non-significant points for
2.5× the output tokens.[^c4]

## Why it matters

For stall 2 (which axis first — here, whether to re-ask the same question
with the failed attempt attached or ask fresh), this is a named, quantified
case where the intuitively richer question — "here is what you got wrong,
try again" — is dominated by the plain repeat. An agent that automatically
conditions retries on the prior failure is paying an anchoring tax that a
blind resample avoids, and the tax is largest exactly where the agent is
weakest (small models, early iterations: 46–53% of all attainable gain
across k=8 iterations is realized by k=2).

## Limits

- Small models only (1.5B–7B, Qwen2.5-Coder); "our 7B results are
  consistent with" reports that execution feedback matters little at
  frontier scale, but the paper does not test whether the anchoring penalty
  itself, not just its cost, persists past 7B.
- Single benchmark family (MBPP+, with HumanEval+ underpowered), single task
  type (short function synthesis); the anchoring measure (longest-matching-
  subsequence similarity) resolves the ordering only between conditions
  whose anchoring differs by more than the metric's noise — placebo and
  feedback differ by as little as 0.003–0.039 and their accuracy ordering
  does not follow the similarity ordering.
- A null result rules out prompt length as the driver (cross-task retrieved
  exemplars of matched length cost nothing, bounded to ±3.5 points), which
  is why the claim is anchoring specifically and not generic context
  dilution — but this is still one paper's mechanism attribution, not a
  cross-lab replication; `replicated: false` (the paper's own replication is
  within-paper, across two model families and two precisions, not an
  independent lab).

- A different setting points the other way. On AIME 2025 with Qwen3-8B, a
  reflection prompt spliced into a reasoning trace beat a plain restart, and
  the authors credit the gain to "guided reflection mechanism over naive
  re-generation."[^c5] That intervention ran mid-trace on a confidence drop,
  not after a finished failed attempt, and on math, not code. It does not
  overturn the 1.5B–7B result above, but it shows the own-output penalty is
  not a law for every form of self-directed re-prompting.

## Related

[[diagnostic-anchoring-in-agentic-llms]] · [[bounded-rationality]] · [[value-of-information]] · [[confidence-triggered-reflection]] — the mid-trace variant whose guided restart outperformed plain restart

[^c1]: verma-2026 — "Blind resampling is the strongest condition below 7B, and remains statistically tied with the best condition at 7B, while consuming 2.5–5.5× fewer tokens; conditioning on the model’s own failed attempt costs 6.1 points at 1.5B (p=0.006), and the informational content of execution feedback adds nothing measurable over the placebo."
[^c2]: verma-2026 — "Similarity rises by 0.30 to 0.38 relative to blind resampling at every scale, and the proportion of retries that are near-identical (> 0.95) rises from 2–14% to 33–68%. Shown its own code, the model edits; asked afresh, it reconsiders."
[^c3]: verma-2026 — "Anchoring strength is roughly constant across scale, but its cost declines: a larger model’s failed first attempt is a better object to anchor upon. The diminishing penalty at 7B therefore reflects anchoring becoming inexpensive rather than feedback becoming useful."
[^c4]: verma-2026
[^c5]: arxiv-2512-18605 — "guided reflection mechanism over naive re-generation"
