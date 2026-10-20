---
description: "Self-training labels come from the action sequence with the highest reward averaged over a query's interpretations, then its best rollout, so a single lucky guess is not trained on."
aliases: ["coarsened action-sequence selection", "interpretation-averaged best-rollout selection", "expected-reward action sequence"]
sources: ["arxiv-2512-04068"]
---
# Interpretation-averaged action selection

When a policy is trained by rejection sampling on its own rollouts, the obvious
label is the single highest-reward rollout. In an ambiguous setting that label can
be wrong for the reason it scored well: the rollout guessed an intent that
happened to be the one the simulated user had in mind. Berant and colleagues
change the unit of selection. They first coarsen each rollout into its sequence of
actions (ask, answer, enumerate), then ask which action sequence does best in
expectation, and only then take an example from it.

## Mechanism

For a query and a price pair (α, β), the rollouts are generated over the query's
interpretations and grouped by action sequence. The sequence chosen is the one with
the highest expected reward, averaged over rollouts and over interpretations. The
paper's wording is that the sequence is the one "that leads to the highest reward in
expectation over rollouts and interpretations."[^c1] Interpretations are weighted
by their probabilities in the paper's formula, but "In practice, we assume Pq is
uniform," so each interpretation counts equally.[^c2]

Only after the sequence is fixed do they take training data from it: "construct
training examples from the best rollout compatible with this action sequence."[^c3]
That is, for each interpretation the highest-reward rollout that follows the chosen
sequence is kept. The result is a label that belongs to the action pattern across
readings of the query, not to one draw.

Rollouts are filtered first. The paper discards rollouts with a low F1 ("we discard
rollouts with low F1") and rollouts where the simulated user ignores the assistant's
answer.[^c4] Training uses many rollouts per query: "We use nr = 192 rollouts at
training time."[^c5]

The motivation is the paper's own. The top-scoring rollout can reach a high reward
by chance, through an action that is poor but happened to fit the user's intent.
That is my reading of the motivation, not a quoted statement, and the paper's
measured gain from this rule over plain best-rollout training is in an ablation I
did not read.

## Transfer

The move is a standard one from decision theory: rank policies by their mean value
over the latent state, not by their best sample. Selection by mean is common in
bandit and reinforcement-learning practice. What survives is the principle that a
label should be scored across the states the query can take. What does not survive
is the rest of the machinery: the paper's action sets are tiny (four sequences, one
clarifying question), so the averaging is cheap and the argmax is exact. With a
richer action space, or a longer dialogue with many possible action sequences, the
averages would rest on far fewer rollouts per sequence. That is my inference; the
paper does not test it.

The same failure appears in other settings. [[judge-scored-reflection-memory]]
stores reflections that credit a lucky outcome with the same standing as the rest,
and the work there does not test it. The selection rule here is one answer to that
kind of lucky credit.

## Limits

The averaging is over the interpretations the dataset lists, which are themselves
imperfect. In building AmbigQA the authors "found noisy annotations (annotated
interpretations that are not plausible)" and filtered queries with a model.[^c6] An
average over a noisy set of readings inherits the noise.

The uniform-P_q assumption means the expectation is over annotated readings, not over
the real distribution of user intents. Where that distribution is skewed, the chosen
sequence can differ from the one that is best for the real population.

The rule selects an action sequence per price pair, then keeps rollouts from it. It
does not say what to do when no rollout follows the chosen sequence for some
interpretation; the paper's filtering handles this by dropping cases, and the count
of dropped cases is in an appendix I did not read.

## Related

- [[steerable-clarification-policy]] — the policy whose per-price labels this rule produces.
- [[multi-turn-reward-clarification-training]] — credits a trajectory's final reward back to every earlier turn, a different credit rule for the same kind of self-play data.
- [[judge-scored-reflection-memory]] — the same lucky-outcome credit, in reflection memory rather than action labels.
- [[interpretation-space]] — the set of readings over which this rule averages.

[^c1]: arxiv-2512-04068 — "that leads to the highest reward in expectation over rollouts and interpretations"
[^c2]: arxiv-2512-04068 — "In practice, we assume Pq is uniform"
[^c3]: arxiv-2512-04068 — "construct training examples from the best rollout compatible with this action sequence"
[^c4]: arxiv-2512-04068 — "we discard rollouts with low F1"
[^c5]: arxiv-2512-04068 — "We use nr = 192 rollouts at training time"
[^c6]: arxiv-2512-04068 — "we found noisy annotations"
