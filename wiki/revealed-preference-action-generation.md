---
description: "Predicting and generating the report-editing actions a user wants works best from that user's own past selections, beating self-reported rules, papers, and generic prompts alike."
aliases: ["user history as personalization signal", "actions speak louder than words"]
sources: ["arxiv-2604-23815"]
---
# Revealed-preference action generation

> What a user has actually picked before predicts, and generates, what
> they will pick next better than what they say they want, who they are,
> or what they have written.

## Definition / Mechanism

Within [[intermediate-action-feedback|DRACULA]]'s action-selection dataset,
[[arxiv-2604-23815|Balepur, Hamada, Kishore, Feldman, Singh, Siangliulue,
Chang, Rudinger, Choi, Boyd-Graber, Downey & Naik (2026)]] run a simulation
task — predict, from a query and a proposed action, whether a given user
selects it — and test which kind of user context an LLM judge should
condition on. Conditioning on that user's own past selections beats a
context-free baseline outright: "As action selection varies by user, we
test whether conditioning on past selections from just the target user
aids predictions. This largely boosts F1... so user modeling benefits the
task."
[^c1]

Every other context tried adds little to nothing on top of that history:
augmenting it with the user's flagged papers, the action's category label,
past rationales, or self-reported intent and expertise "never largely beat
the user history baseline."
[^c2]

Explicitly-elicited **stated preferences** — five rules a user writes
describing their ideal DR system, and five rules GPT-4.1 infers from that
same user's history — fare no better: "GPT rules are more predictive than
user-written rules, but neither exceeds user-specific history. Thus,
capturing how users actually select actions is more predictive than the
actions they say they prefer."
[^c3]

The same ordering holds one step downstream, in *generation* rather than
prediction: when GPT-4.1 generates candidate actions conditioned on each
of four context types (generic query, the user's papers, stated
preferences, or **revealed preferences** — the user's own past queries,
actions and judgments as few-shot examples), users pick revealed- and
stated-preference actions at a higher rate than paper-conditioned ones:
"Selection rates for actions from stated and revealed preferences exceed
paper actions. Research papers are not tied to DR interactions,
highlighting the challenge of finding useful cold-start personalization
signals for DR."
[^c4]

The gain over generic actions is modest in rate, but not in kind: revealed-
preference actions overlap generic actions only 12.1% of the time and are
still picked above chance, so the mechanism is expanding the space of
useful actions offered, not just re-ranking the same ones: "personalization
yields varied actions... that users still pick above random (>50%),
expanding the actions DR can take to help users."
[^c5]

## Why it matters

The result locates the useful personalization signal for this task at a
specific point on a spectrum from self-report to behavior: neither
demographic-style descriptors (expertise, stated intent) nor an
unconnected artifact (a research paper) substitute for the user's own
task-format history, and asking the user to *articulate* their preference
(stated preferences) does not close that gap either — only the record of
what they actually did does. For an agent deciding what to elicit or
condition on, this argues for logging and reusing selection history over
building richer self-report or profile elicitation.

## Limits

- Both effects (prediction and generation) are shown on one DR system,
  one user pool (18–20 paid CS researchers), and one context source per
  condition; the paper does not test whether combining revealed
  preferences with retrieval or larger context budgets closes more of the
  gap to human agreement.
- The revealed-preference generation gain over generic actions is
  described by the authors themselves as "modest," and the paper does not
  report whether it is statistically significant at the same confidence
  level as the stated-vs-generic gap.
- The mechanism is bounded by within-user preference instability: "action
  prediction is inherently bounded by latent shifts in users' intent and
  audience... for such users, clarification mechanisms such as our actions
  remain practical" — i.e. for users whose goals visibly shift between
  sessions, no amount of past-selection conditioning is claimed to recover
  what a live elicitation step (the action menu itself) still supplies.
[^c6]

## Related

[[intermediate-action-feedback]] · [[information-need-reification]] · [[decision-centric-design]] · [[compound-ai-systems]]

[^c1]: arxiv-2604-23815 — "User History is Key. As action selection varies by user (§3.1), we test whether conditioning on past selections from just the target user aids predictions. This largely boosts F1 (Table 3, User-Specific History vs All User History), so user modeling benefits the task."
[^c2]: arxiv-2604-23815
[^c3]: arxiv-2604-23815
[^c4]: arxiv-2604-23815 — "Selection rates for actions from stated and revealed preferences exceed paper actions (Table 4). Research papers are not tied to DR interactions, highlighting the challenge of finding useful cold-start personalization signals for DR (Zhao et al., 2025b)."
[^c5]: arxiv-2604-23815
[^c6]: arxiv-2604-23815
