---
description: "Splits a candidate pool each round by an attribute one group has and another lacks, asks one binary question about it, and prunes the losing group."
aliases: ["Recursive Comparative Judgment", "RCJ", "comparative judgment", "ProCompNav", "discriminative attribute discovery"]
sources: ["kwon-2026"]
---
# Recursive Comparative Judgment

> An embodied-agent question-selection rule for disambiguating a target
> instance among visually similar distractors: split the candidate pool
> into two groups by an attribute the pool itself contrasts on, ask one
> binary question about that attribute, and prune the losing group.

## Mechanism

At each interaction round $t$, ProCompNav holds an active candidate pool
$U_t$ (instances still consistent with the user's answers). It first
divides $U_t$ into a semantically coherent **core set** $G_c$ (found by
greedy peeling to maximize mean pairwise similarity) and the **remainder**
$G_r = U_t \setminus G_c$, then extracts candidate attributes from $G_c$'s
descriptions with an LLM and scores each on every instance in $G_c \cup
G_r$ with a natural-language-inference (NLI) entailment model, choosing
the attribute $a_t^*$ that maximizes the score gap between the two groups:
"At each interaction round, ProCompNav extracts an attribute-value
pair—a Discriminative Attribute (DA) that one group of candidates in the
current pool has but the rest lack—asks the user whether T ∗ has it, and
removes the inconsistent group."[^c1]

The selection rule itself: "we select the DA a∗t that maximizes the
contrast between Gc and Gr" — computed as the expected NLI entailment
score of $a$ over $G_c$ minus its expected score over $G_r$.[^c2]

Unlike question selection built from a single candidate's own attributes
("independent matching"), the attribute is chosen because it splits the
*pool*, so a single yes/no answer prunes every candidate on the losing
side at once regardless of how many share it. On CoIN-Bench, replacing
independent matching with this pool-splitting rule (holding the same
candidate pool fixed) raised Success Rate over the ablation that uses the
identical pool-construction stage but independent-matching questions:
"Using the same candidate pool, ProCompNav further improves SR by
selecting attribute-value pairs that split the pool and asking binary
questions to prune inconsistent candidates, greatly reducing response
length."[^c3]

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Embodied instance navigation (this paper) | comparative judgment | exact — the strategy contrasted with independent matching |
| Embodied instance navigation (this paper) | Recursive Comparative Judgment / RCJ | exact — the named algorithm (Sec. 4.3) |
| Embodied instance navigation (this paper) | ProCompNav | close — the full two-stage system (pool construction + RCJ), not the question-selection rule alone |

## Limits

- User answers in the reported CoIN-Bench numbers are simulated by an
  MLLM with access to the target's image, not collected from people; the
  binary-question framing's effect on real users is untested here.
- The attribute vocabulary a round can choose from is whatever an LLM
  extracts from the core set's generated descriptions — a question the
  pool's own candidates never mention cannot be asked.
- Each round's split is chosen greedily by maximizing one round's
  core/remainder contrast; no bound relates this to an optimal question
  sequence over the pool, unlike the mass-balance guarantee for
  [[generalized-binary-search]].
- Reported only on two simulated 3D navigation benchmarks (CoIN-Bench,
  TextNav) with one [[backbone-of-a-formula|backbone]] (Qwen3-VL-8B) and one NLI verifier
  (DeBERTa-v3-large); generalization to other domains or verifiers is not
  shown.

## Related

[[generalized-binary-search]] · [[constraint-seeking]] · [[value-of-information]]

[^c1]: kwon-2026 — "At each interaction round, ProCompNav extracts an attribute-value pair—a Discriminative Attribute (DA) that one group of candidates in the current pool has but the rest lack—asks the user whether T ∗ has it, and removes the inconsistent group."
[^c2]: kwon-2026 — "we select the DA a∗t that maximizes the contrast between Gc and Gr"
[^c3]: kwon-2026 — "Using the same candidate pool, ProCompNav further improves SR by selecting attribute-value pairs that split the pool and asking binary questions to prune inconsistent candidates, greatly reducing response length."
