---
description: "In the BAPO model, binary majority, triplet matching and graph reachability need Omega(n) chain-of-thought tokens; below that budget accuracy collapses, though models spend far more than the bound."
aliases: ["BAPO token complexity", "minimum reasoning budget", "BAPO-CoT lower bound"]
sources: ["arxiv-2602-02909"]
---
# CoT token complexity lower bound

The bounded attention prefix oracle (BAPO) model abstracts an LLM as communication-bound: if a problem needs too much information to cross an arbitrary prefix/suffix split inside one token-generation step, the step fails.[^c1] Problems solvable with constant bandwidth are BAPO-easy (parity, equality, disjointness, index); the rest are BAPO-hard.[^c2] Chain of thought turns a hard problem into a sequence of easy steps, so the open question is how many steps are needed.

**Definition.** The token complexity c(n) of a problem is the worst-case CoT length of the best constant-bandwidth BAPO-CoT that solves every size-n instance; no such BAPO-CoT can use fewer than c(n) tokens.[^c3]

**Lower bounds.** Any constant-bandwidth BAPO-CoT needs Omega(n) tokens for Majority (n inputs), Match3 (n inputs) and Omega(m) for Reachability on m-edge graphs.[^c4] The proof extends the BAPO-hardness argument to every possible reasoning chain at once. Since these bounds hold for the unrestricted model they carry over to the restricted self-consistent variant (cBAPO) used for upper bounds.[^c5]

**Upper bounds.** In cBAPO, Majority is O(n log n), Match3 O(n) and Reachability O(n^2); the unrestricted BAPO can reach n+1 tokens for Majority and Match3 and m+3 for Reachability, but only because a powerful prefix oracle can do the work, which the authors call unrealistic.[^c6]

**Not every hard problem is linear.** Pointer chasing is BAPO-hard yet its token complexity scales with the length of the pointer chain, not the input.[^c7]

**Measured behaviour.** GPT-5.2 with reasoning gets near-perfect accuracy with reasoning tokens scaling linearly in problem size; with reasoning off or at minimum budget accuracy falls to random guessing.[^c8] Word-limited external CoT of 50 and 100 words only partly closes the gap, while 200 words suffices at n = 101, so models use far more tokens than the bound requires.[^c9] Linear token needs imply at least quadratic compute as context grows.[^c10]

## Limits

The bounds are asymptotic and for a stylised model with constant bandwidth; the constant factors, and whether real transformers obey the BAPO abstraction, are not established. The definition is nonuniform (a different BAPO per n). Only three synthetic tasks plus one sublinear counter-example were analysed; no natural question-answering tasks, so how much real questions fall in the BAPO-hard class is untested here. The experiments used two models (GPT-5.2, Gemini 2.5 Pro). Matching upper bounds are only near-matching for Majority and Reachability.

## Related

- [[moderate-adaptive-reasoning-length]] — empirical evidence that longer reasoning can hurt; this note gives a floor below which it fails
- [[reasoning-trap]] — more reasoning degrading outcomes, the opposite pressure from the floor

[^c1]: arxiv-2602-02909 — "LLMs are communication-bound: if a problem requires too much"
[^c2]: arxiv-2602-02909 — "BAPO-easy examples include PARITY, E QUALITY, D IS JOINTNESS and I NDEX"
[^c3]: arxiv-2602-02909 — "This means that no constant-bandwidth BAPO-CoT can"
[^c4]: arxiv-2602-02909 — "Any constant-bandwidth BAPO-CoT for M A JORITY on length-n inputs uses Ω(n) CoT tokens"
[^c5]: arxiv-2602-02909 — "Note that the"
[^c6]: arxiv-2602-02909 — "which is clearly unrealistic."
[^c7]: arxiv-2602-02909 — "has token complexity scaling with the length of the pointer"
[^c8]: arxiv-2602-02909 — "accuracy rapidly degrades to random guessing for"
[^c9]: arxiv-2602-02909 — "indicating they are below the"
[^c10]: arxiv-2602-02909 — "linear lower bounds on required reasoning length translate into at"
