---
description: "Closed-loop controller that reduces a hidden-profile multi-agent discussion to six state variables and picks the next communication action from a conformally screened set each round."
aliases: ["Consilience", "closed-loop communication control", "conformally calibrated communication control"]
sources: ["babu-2026"]
---
# Consilience communication control

> In a hidden-profile discussion, which of four possible interventions
> should the group take next — and existing protocols (fixed schedule,
> round-robin, unstructured debate) never answer that question at all.

## Definition / Mechanism

Each agent in a hidden-profile task holds a private clue no other agent
sees; a correct group answer requires that evidence to surface on the
shared transcript. Fixed schedules, round-robin exchange, and unstructured
debate provide no guarantee that a given turn's action is the one the
discussion needs.[^c1]

Consilience treats action selection as a per-round online control loop.
After each message the group's aggregate belief is summarized into six
observables — group uncertainty $H_t$ (normalized [[entropy]] of the mean
belief), inter-agent disagreement $D_t$ (mean Jensen–Shannon divergence of
each agent's belief from the mean), message redundancy $R_t$, evidence
gain $G_t$, communication cost $C_t$ (transcript length), and premature
consensus $P_t$ (high confidence with low recent evidence gain, early in
the discussion). A fixed linear combination of these, $J(s_t)$, is the
one-step surrogate discussion loss a controller tries to lower. "At each
turn, Consilience summarizes the discussion using a compact state
capturing uncertainty, disagreement, evidence gain, redundancy, and
premature consensus, then selects both a communication intervention
(challenge, clarify, seek evidence, or route) and an appropriate speaker."[^c2]

A controller (rule-based, a small MLP, or an LLM) proposes one action from
{Challenge, Clarify, SeekEvidence, Route, Vote}; a conformal acceptance
stage (see [[round-wise-regret-conformal-acceptance]]) either passes the
proposal through or replaces it with a lower-regret alternative; a fixed
router then picks the speaker — the most-disagreeing agent for
Challenge/Clarify, the least-heard agent for SeekEvidence/Route. The
selected agent's message updates the transcript and every agent's belief,
closing the loop.

## Known as

| Field | Name there | Match |
|---|---|---|
| Babu et al. (2026), title | Consilience | exact |
| Babu et al. (2026), §1 | closed-loop communication control | exact — the paper's name for the same loop |
| Babu et al. (2026), abstract | conformally calibrated communication control | exact — names the whole pipeline including the conformal stage |

## Why it matters

Stall 2 asks which axis a question should open next; here the "axis" is
which of four communication acts a multi-agent group should take, and the
answer is state-dependent rather than fixed by role or schedule. On
HiddenBench-style tasks across 12 models, Consilience's controllers "improve
decision accuracy and communication efficiency over fixed and unstructured
discussion protocols, sometimes surpassing a full-information baseline
where every agent observes all evidence" — evidence that *how* the group
asks for missing evidence can matter more than how much evidence exists to
begin with.[^c3]

## Limits

- Evaluated only on HiddenBench-style synthetic hidden-profile tasks and an
  LLM-generated benchmark; no test with human discussants.
- The state's coefficients ($\alpha_H,\alpha_D,\dots$) in $J(s_t)$ are
  fixed hyperparameters chosen before evaluation, not derived from a
  decision-theoretic objective — the ranking of actions is a heuristic
  surrogate for group-answer quality, not a proven bound on it.
- The action space (Challenge, Clarify, SeekEvidence, Route, Vote) is fixed
  to this benchmark family; the note makes no claim about other
  communication-act inventories.

## Related

[[round-wise-regret-conformal-acceptance]] · [[value-of-information]] · [[adaptive-submodularity]] · [[multi-agent-clarification]]

[^c1]: babu-2026 — "Existing protocols, including fixed schedules, round-robin exchange, and unstructured debate, provide no guarantee that a conversational action is appropriate."
[^c2]: babu-2026 — "At each turn, Consilience summarizes the discussion using a compact state capturing uncertainty, disagreement, evidence gain, redundancy, and premature consensus, then selects both a communication intervention (challenge, clarify, seek evidence, or route) and an appropriate speaker."
[^c3]: babu-2026 — "On HiddenBench-style hidden-profile tasks spanning 12 open and closed weight language models, Consilience improves decision accuracy and communication efficiency over fixed and unstructured discussion protocols, sometimes surpassing a full-information baseline where every agent observes all evidence."
