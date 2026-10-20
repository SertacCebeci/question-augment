---
description: "An explanation agent chooses between presenting a value-aligned recommendation directly or the default one with a counterfactual, gated on inferred user receptivity."
aliases: ["counterfactual nudging", "direct-alignment vs counterfactual-nudging strategy"]
sources: ["arxiv-2604-14223"]
---
# Receptivity-gated counterfactual nudge

> Had you expressed interest in lower environmental impact, the greener
> option would have been recommended because …

## Definition / Mechanism

An explanation-generation agent $A_{EG}$ holds two already-built
recommendation sets: a baseline $R_0$ (relevance only) and a value-aligned
set $R_1$ (relevance plus a target value — here, sustainability). It also
holds a scalar signal inferred earlier in the conversation, the user's
**willingness to compromise** (WTC) on that value, extracted from their
[[clarification-request|responses to clarifying questions]] rather than
asked for directly. $A_{EG}$ branches on WTC to pick both *which*
recommendation to surface as primary and *how* to justify it
Banerjee et al. (2026):

- **Direct alignment** — if WTC signals openness, it surfaces $r^* \in R_1$
  and explains the gain $\Delta S = M(R_1) - M(R_0)$ directly, $M(\cdot)$
  being the value's measured dimensions (e.g. CO2, visitor pressure,
  walkability).[^c1]
- **Counterfactual nudging** — if WTC signals resistance, it surfaces the
  baseline $r^* \in R_0$ to preserve trust, but attaches a counterfactual
  explanation of the unchosen $r_{alt} \in R_1$, conditionally framed.[^c2]
  The example the agent is instructed toward: "Had you expressed interest
  in lower environmental impact, $r_{alt}$ would have been recommended
  because …". The alternative is disclosed, not substituted — the
  stated constraint is never violated.

The gate is the same signal a clarification loop already produced; no
extra question is asked to decide which branch to take. In a 24-participant,
107-session user study, 79.1% of users chose the primary option when
offered a primary/alternative pair, and 75.5% of those choices were
the value-aligned recommendation. 55.2% rated the clarifying
questions and 65.4% the explanations "Very well" or better.[^c6]

## Why it matters

The mechanism separates *which recommendation to show* from *whether to
argue for the value at all*: instead of a single explanation policy, the
agent has two, chosen by a receptivity estimate, so that pushing a value
(sustainability, safety, cost) never overrides an explicit preference —
it only ever appears as a disclosed road not taken. This is a general
pattern for any agent that has both a preferred-by-the-agent option and a
preferred-by-the-user option and wants to move the user without
overriding them.

## Limits

The receptivity signal (WTC) is itself LLM-inferred from a handful of
clarification turns and is not independently validated against a ground
truth; the paper reports coherence between agents via sentence-embedding
similarity (0.70–0.79, all-MiniLM-L6-v2), not accuracy of WTC itself. The
79.1%/75.5% figures conflate "chose the primary option" with "accepted the
nudge" — no counterfactual arm compares against showing $R_1$
unconditionally. The paper itself notes a second-order risk: consistently
nudging toward less-popular alternatives can create new hotspots,
shifting rather than reducing the externality the nudge targets
(**unverified** beyond the authors' own observation). The demo is scoped
to single-city European trips; the mechanism is not tested outside that
scope or outside tourism.

## Related

- [[clarification-request]] — the upstream turns whose responses set WTC.
- [[constraint-as-information]] — WTC is a constraint the user never
  stated as such.
- [[counterfactual-search-routing-oracle]] — counterfactual framing used
  for a different decision (search vs. no-search), not persuasion.
- [[value-of-information]] — the value a branch would add is exactly what
  the counterfactual explanation discloses without acting on it.
- [[decision-theoretic-grounding]] — the two-branch policy is a decision
  rule conditioned on an inferred latent state.

[^c1]: arxiv-2604-14223 — "trade-offs, the agent selects 𝑟 ∗ ∈ 𝑅1 and generates an explanation"
[^c2]: arxiv-2604-14223 — "Counterfactual Nudging. If WTC indicates resistance to sustainability trade-offs, the agent selects the baseline recommendation"
[^c6]: arxiv-2604-14223 — "55.2% of users rated the clarifying questions and 65.4%"
