---
description: "Rewarding a model for quoting the helpful passage inside noisy context, judged against a gold reference, cuts distractor-driven reasoning and beats outcome-only RL reward."
aliases: ["RARE", "rationale-aware reward", "reference-span reward"]
sources: ["arxiv-2601-07226"]
---
# Rationale-aware reward

Outcome-only reinforcement learning pays for a correct final answer. Under noisy context that cannot separate a model that found the relevant passage from one that guessed or recalled from memory, or distinguish ignorance from distraction.[^c1] RARE adds a process term: the model must paraphrase or copy the helpful information inside a `<reference> ... </reference>` span, and a judge model compares the extracted content with the gold reference and gives a binary reward.[^c2]

## What was measured

Combining outcome reward with RARE outperformed outcome reward alone across all distractor settings (random documents, random chat, hard negatives) and models.[^c2] During training, RARE reduced the share of distracted chains of thought while outcome reward rose, and final accuracy exceeded outcome-only training.[^c3] Outcome-only RL still often rewarded runs that failed to filter noise.[^c4] Prompting, SFT and context-engineering methods (GEPA, DC, ACE) gave limited or no robustness; outcome RL helped more than prompting or SFT.[^c5]

The mechanism claimed: the reward supplies fine-grained supervision on whether the reasoning identified the right source, so the model learns relevance selection, not only answer production.[^c1]

## Limits

- Needs a gold reference passage per training item and a judge model; where no gold evidence exists the reward cannot be formed.
- Gains are shown on the authors' NoisyBench tasks; transfer to open-ended questions without a single supporting span is untested.
- The explanation (reduced distracted chains) rests on a judged proxy for "distracted" whose reliability is not independently checked here.
- Whether the explicit extract step itself, rather than the reward, would help at inference was not isolated in what I read.

## Related

- [[distractor-similarity-reasoning-inflation]] — the failure this reward targets.
- [[rationale-level-relevance-judging]] — judging relevance at the rationale level.
- [[hint-adherence-without-acknowledgement]] — models using context without stating it, the gap a process reward tries to close.
- [[parametric-knowledge-gates-retrieval-noise-damage]] — separate when memory versus context drives answers.

[^c1]: arxiv-2601-07226 — "RARE provides rewards when the model identifies and uses the correct source during reasoning"
[^c2]: arxiv-2601-07226 — "A judge model compares the extracted content with the gold reference and assigns a binary reward."
[^c3]: arxiv-2601-07226 — "training with RARE reduces the"
[^c4]: arxiv-2601-07226 — "OR-trained models often receive rewards even when"
[^c5]: arxiv-2601-07226 — "RL with outcome-based rewards (OR) mitigates performance degradation more effectively than prompting"
