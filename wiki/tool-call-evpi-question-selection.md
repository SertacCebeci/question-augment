---
description: "Scores a candidate clarifying question by expected gain in tool-call certainty minus a per-aspect redundancy cost; asks only above a belief-scaled threshold."
aliases: ["SAGE-Agent question scoring", "structured EVPI for tool calls", "aspect-based redundancy cost"]
sources: ["suri-2025"]
---
# Tool-call EVPI question selection

> Which clarifying question to ask next, scored directly over a tool's
> structured parameters instead of over free text.

## Definition / Mechanism

Suri et al. maintain a belief state $B(t)$ — a distribution $\pi_c(t)$ over
candidate tool calls $c$, each an assignment of concrete values or `<UNK>`
to a tool's parameters. A candidate question $q$ targets a set of
**aspects** $A(q) \subseteq A$, where an aspect $a=(T_i,\theta_j)$ is one
parameter $\theta_j$ of one tool $T_i$. The expected benefit of asking $q$
is defined as the expected rise in the best candidate's probability once a
response $r$ is simulated: "measuring expected improvement in
best-candidate certainty."[^c1]

To stop the agent re-asking about the same parameter, each aspect carries a
count $n_a(t)$ of how often it has already been queried, and the question's
cost scales with that count — "To discourage repetitive questioning" the
paper defines Definition 5 so that "λ controls penalty strength" over
$\sum_{a\in A(q)} n_a(t)$.[^c2]

The agent selects $q^*(t)=\arg\max_q \mathrm{EVPI}(q,B(t))-\mathrm{Cost}(q,t)$
at every step, and "terminates when the maximal net gain falls below α ·
maxc πc (t)" — a threshold that shrinks or grows with the agent's own
current confidence rather than a fixed number.[^c3]

## Why it matters

Packaged into SAGE-Agent (a Reason-Act-Observe loop with this scoring
inserted at the reasoning step), the rule reported "7–39% higher coverage
on ambiguous tasks while reducing clarification questions by 1.5–2.7×
compared to strong prompting and uncertainty-based baselines," across GPT-4o
and Qwen2.5-14B-Instruct backbones on the paper's ClarifyBench benchmark and
on BFCLv2 (When2Call).[^c4]

## Transfer

| | |
|---|---|
| **In its home field** | EVPI (decision analysis, Howard 1966) is the expected gain from resolving all uncertainty about a state before choosing an action under a fixed action set and utility — see [[value-of-information]]. |
| **Here** | The "state" is which structured tool call is correct; the "utility" is implicit — a 0/1 payoff for identifying the right candidate — and EVPI is computed as the expected rise in the winning candidate's own posterior probability, not against a written utility function. |
| **What survives** | The expected-gain-before-asking logic, and pairing it with an explicit cost so that asking is a net calculation rather than a fixed rule. |
| **What does not** | A general utility function; belief propagation here is exact only because tool-parameter domains shrink monotonically under user answers (each response only removes values), a structural fact about typed parameters that free-text answers do not give. |

## Limits

- This claim rests on `suri-2025`'s own equations (Definitions 4–5, Eq. 3–5)
  being read as reported; the source's text extract was read directly, but
  the note has not independently re-derived the belief-propagation proof
  the paper sketches only in its appendix.
- The 0/1-utility reading of EVPI is this note's characterisation of what
  the formula computes, not a phrase the paper uses; the paper calls it
  EVPI without specifying a utility, so the equivalence to a 0/1 payoff is
  an inference, not attributed.
- Reported gains are against four specific baselines on two benchmarks the
  same team built (ClarifyBench, a subset of When2Call); no independent
  replication is on record.
- Exact belief propagation depends on treating every user response as a
  hard domain-restricting constraint; a vague or contradictory answer is
  outside what the mechanism as described handles.

## Related

[[value-of-information]] · [[uncertainty-decomposition]] · [[expected-information-gain]] · [[clarification-benchmarks]] · [[calibration]]

[^c1]: suri-2025 — "measuring expected improvement in best-candidate certainty."
[^c2]: suri-2025 — "To discourage repetitive questioning"
[^c3]: suri-2025 — "terminates when the maximal net gain falls below α · maxc πc (t)"
[^c4]: suri-2025
