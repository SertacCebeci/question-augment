---
description: "A greedy adaptive question-selection algorithm that picks the next question maximizing an LLM-estimated, redundancy-penalized incremental information gain within a fixed turn budget."
aliases: ["NBQ", "next-best-question", "next-best-question selection"]
sources: ["shi-2026-next"]
---
# Next-Best-Question (NBQ)

> At each turn, ask the question whose predicted answer would most raise a
> running coverage score, after discounting whatever the conversation
> already covers.

## Definition

For a topic $\alpha$ and a candidate pool $Q(\alpha)$, an interview runs for
at most $T$ turns. The problem is posed as choosing, after each answer, the
question that maximizes expected terminal utility under the turn budget:
"The problem here is to choose the next best question that is expected to
maximize terminal utility under a strict turn budget 𝑇 : 𝑞𝑡 +1 = arg
max𝑞 ∈ Q E𝑞 [𝐽 (𝐷𝑇 ; 𝛼)], where the expectation is over the answer
randomness."[^c1]

NBQ instantiates this as a greedy policy over a **user state** vector
$s\in[0,1]^{|Q|}$, one entry per candidate question, initialized to zero and
updated after every answer: "we propose a greedy adaptive question selection
algorithm, denoted as NBQ. At each conversation turn 𝑡, it selects the next
best question 𝑞𝑡∗+1 ∈ Q that is expected to yield the largest incremental
information gain"[^c2]

## Mechanism: relevance, not entropy

NBQ never estimates a probability distribution over answers. Instead it
precomputes a pairwise **relevance matrix** $R$ over all candidate questions
(an LLM-judged, then regression-calibrated semantic-overlap score), and
scores each new answer $a_t$ against every question $q_i$ by how much it
adds over what earlier answers already covered — a redundancy-discounted
relevance, not an [[entropy]] drop: "The second term acts as a redundancy
penalty: it deducts the portion of 𝑎𝑡's contribution with respect to 𝑞𝑖
that is already covered by earlier conversation turns."[^c3]

To rank candidates *before* asking, NBQ substitutes the LLM's own prediction
of what a candidate's answer would contain for the true (unknown) next
answer: "we approximate the unknown next response 𝑎𝑡 +1 with the predicted
answer elements 𝑎ˆ𝑖 for candidate question 𝑞𝑖"[^c4]

Because $R$ does not depend on the respondent, it is computed once offline
and reused across all users, shifting the selection cost from an online
LLM call per candidate to a matrix lookup.

## Empirical gain

Against random and prior LLM-elicitation baselines (MockLLM, GATE-style
constrained prompting), the resulting profiles score higher on two
coverage/confidence metrics: "Compared with random or conventional
generative questioning baselines, NBQ improves the quality of user
profiling by up to 13.6% and 14.0% in terms of AC@T and AR@T."[^c5]

## Limits

- The ranking rests on an LLM's *point prediction* of a candidate's likely
  answer content, not a distribution over answers — unlike
  [[expected-information-gain]], there is no averaging over answer
  randomness at selection time, only over one imagined answer per
  candidate.
- The relevance score itself is a learned proxy (embedding cosine similarity
  passed through a fitted polynomial [[calibration]]), not a measured
  information-theoretic quantity; its fidelity to true incremental
  information gain is validated only on the paper's own calibration set.
- Evaluated on reciprocal-matchmaking profiling with the paper's own AC@T /
  AR@T metrics; the gain over baselines is not shown to hold for objectives
  with a different terminal-utility structure.

## Related

[[expected-information-gain]] · [[semantic-entropy]] · [[value-of-information]] · [[adaptive-submodularity]]

[^c1]: shi-2026-next — "The problem here is to choose the next best question that is expected to maximize terminal utility under a strict turn budget 𝑇 : 𝑞𝑡 +1 = arg max𝑞 ∈ Q E𝑞 [𝐽 (𝐷𝑇 ; 𝛼)], where the expectation is over the answer randomness."
[^c2]: shi-2026-next — "we propose a greedy adaptive question selection algorithm, denoted as NBQ. At each conversation turn 𝑡, it selects the next best question 𝑞𝑡∗+1 ∈ Q that is expected to yield the largest incremental information gain"
[^c3]: shi-2026-next
[^c4]: shi-2026-next — "we approximate the unknown next response 𝑎𝑡 +1 with the predicted answer elements 𝑎ˆ𝑖 for candidate question 𝑞𝑖"
[^c5]: shi-2026-next — "Compared with random or conventional generative questioning baselines, NBQ improves the quality of user profiling by up to 13.6% and 14.0% in terms of AC@T and AR@T."
