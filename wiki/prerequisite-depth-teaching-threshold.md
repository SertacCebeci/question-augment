---
description: "Teaching time is bounded below by prerequisite distance to the target; below that depth completion is impossible, returns are non-concave and a common broadcast costs a factor linear in learner types."
aliases: ["structural barrier", "structural distance to target", "linear broadcast penalty"]
sources: ["arxiv-2603-19349"]
---
# Prerequisite-depth teaching threshold

In the model of [[prerequisite-gated-decodability]], the structural distance L(c) is the length of the shortest prerequisite-respecting route from the learner's axioms to a state containing target c. Each round adds at most one concept.[^c1]

## The barrier

Completion time is at least L(target) almost surely, "regardless of how informative the signals are".[^c2] Consequently the fixed-horizon completion probability is zero for any horizon below the minimum depth of any target with positive prior.[^c3] For a deterministic target it is a step function: zero below L, and achievable with certainty at or above it.[^c4] The paper adds that once the target is reachable, one additional signal suffices for identification.[^c5]

## Consequences the paper derives

- Non-concave returns. The paper contrasts this with smooth human-capital production functions, where every marginal unit yields some return; here a signal has no effect until the structure admits the target.[^c6]
- Allocation. Spreading B rounds over N identical learners so each gets fewer than L rounds produces zero completions. Concentrating on floor(B/L) learners produces completions.[^c7]
- Broadcast. For k learner types with different rule sets, a construction exists in which each type can be taught in L steps by a personalized curriculum, but any common sequence needs at least k(L-1)+1 steps.[^c8] The penalty comes from prerequisite geometry, not from different learning algorithms.[^c9]

For asking and answering, this suggests that a single fixed explanation or question sequence aimed at a mixed audience is paid for in the number of distinct prerequisite structures. This reading is my inference.

## Limits

- All results are for a stylized discrete model with a deterministic parsing gate. The step function is proved for deterministic targets only; for random targets the paper says it need not persist and only the zero region survives.[^c10]
- The broadcast penalty is an existence construction (a worst case built from chosen minds), not a measured typical penalty.
- The model does not test whether real learners show threshold effects. No empirical data were read.
- Learners are assumed to start from known axioms, so uncertainty about the learner's state is not modeled here.

## Related

- [[prerequisite-gated-decodability]] — the parsing gate that produces the barrier
- [[curriculum-sequencing-policy]] — a learned policy for ordering prerequisite nodes
- [[dependency-aware-subquestion-scheduling]] — scheduling under dependency structure
- [[blackwell-informativeness]] — the order used to compare learner states

[^c1]: arxiv-2603-19349 — "The quantity Lm (c) measures the shortest prerequisite-respecting route from"
[^c2]: arxiv-2603-19349 — "Proposition 4.8 is the purely geometric obstruction in the model. Regardless"
[^c3]: arxiv-2603-19349 — "In particular, V(t) = 0 for all t < Lmin ."
[^c4]: arxiv-2603-19349 — "is impossible; at and above it, acquisition can be achieved with certainty."
[^c5]: arxiv-2603-19349 — "In our model, once the prerequisite structure makes"
[^c6]: arxiv-2603-19349 — "In such models every marginal unit of investment yields a positive, though"
[^c7]: arxiv-2603-19349 — "Proposition 5.5 shows that evenly spreading a fixed training budget can waste"
[^c8]: arxiv-2603-19349 — "structural cost: even when each learner can be taught efficiently by a personalized"
[^c9]: arxiv-2603-19349 — "rather than by differences in algorithmic update rules across learners."
[^c10]: arxiv-2603-19349 — "For random targets, the step-function structure need not persist, because"
