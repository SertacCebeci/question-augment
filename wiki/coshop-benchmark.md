---
description: "Five frontier LLM shopping agents score below 56% team accuracy on a five-turn benchmark, because they leave most non-expert users' preferences unconstructed, not because they search badly."
aliases: ["CoShop"]
sources: ["saracay-2026"]
---
# CoShop benchmark

> Five frontier LLMs, evaluated as shopping agents against simulated
> non-expert users, never exceed 56% team accuracy after five
> conversation turns — and the shortfall traces to preferences the agent
> never helped the user construct, not to search failure.

## Definition / Mechanism

CoShop evaluates an agent-user *team's* accuracy, not the agent alone.
Each rollout: (1) conversation — the agent searches a catalog and talks to
a [[preference-construction|CoPref]] simulated user for up to 5 turns; (2)
research — a wider, non-interactive search; (3) report — the agent writes
$k=5$ recommendations; (4) selection — the user picks one item based on
its final preference state $S_{T+1}$. Team accuracy is whether the picked
item matches the user's true target, and is upper-bounded by whether the
target is even among the agent's $k$ recommendations (agent recall@$k$).
State completeness — the fraction of the user's true preference set
recovered by end of conversation — is reported separately.[^c1]

Across three product domains (H&M fashion, MovieLens, Goodreads) and five
models (gpt-4.1-mini, gpt-5.2, claude-haiku-4.5, claude-sonnet-4.6,
gpt-oss-120b), every model scores highly when the user's full preference
set is given upfront (claude-sonnet-4.6 averages 94.3%), but none recovers
that level through conversation with a CoPref user: claude-sonnet-4.6 falls
to 27.6% team accuracy after 5 turns, and no model exceeds 56% team
accuracy on any domain. gpt-5.2 scores 57.0% when every feature is a
search feature (any question suffices) but only 27.7% once some features
require an example or an explanation instead.[^c2]

The team-agent gap is decomposed experimentally: replaying user selection
with a programmatically complete report (all true features shown) raises
team accuracy for gpt-oss-120b substantially and slightly for
gpt-4.1-mini and claude-sonnet-4.6 — poor report quality is one source.
A second, separate source is the preference state itself: no tested model
recovers more than 54% of the user's preferences over a conversation, and
even with a complete report the user's incomplete final state leaves them
unable to break ties among the $k$ options — e.g. gpt-5.2 reaches 65%
agent recall@$k$ on H&M but only 56% team accuracy, a 9-point gap
attributable to the user, not the search.[^c3]

## Limits

Results depend on an LLM-simulated CoPref user (gpt-oss-120b, conditioned
only on the current preference state, not a persona) and on an automatic
parser that reads dialog actions and referenced features out of the
agent's free-text turns; the paper reports that parser's own accuracy at
74.0% for identifying which feature a question referenced (94.0% for
items), so some of the measured preference-construction failure is parsing
noise rather than agent behavior — a structured-action ablation without
parsing is reported to change the ranking (it degrades all models further,
via hallucinated feature names) rather than confirm it exactly.[^c4]

## Related

[[preference-construction]] · [[cross-type-eig]] · [[volume-removal]] · [[expected-information-gain]]

[^c1]: saracay-2026 — "Performance is measured by the user-agent team’s accuracy: whether x̂ matches x ∗ ."
[^c2]: saracay-2026 — "claude-sonnet-4.6 scores 94.3% accuracy given fully-specified preferences upfront, it scores only 27.6% team accuracy on C O S HOP after 5 turns of conversation. No model exceeds 56% on any domain in C O S HOP"
[^c3]: saracay-2026 — "no model recovers more than 54% of the user’s preferences over the course of the conversation."
[^c4]: saracay-2026 — "gpt-oss-120b has question parsing accuracy of 74.0% and item parsing accuracy of 94.0%."
