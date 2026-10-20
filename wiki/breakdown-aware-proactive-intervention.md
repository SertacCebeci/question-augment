---
description: "A two-stage pipeline that decides, turn by turn in a multi-user conversation, whether an agent stays silent or intervenes, gated on a diagnosed collaboration breakdown."
aliases: ["ProACT", "breakdown-aware proactive agent", "collaboration breakdown diagnosis"]
sources: ["yang-2026-proact"]
---
# Breakdown-aware proactive intervention

> Before an agent asks (or says anything unprompted) in a group
> conversation, it first names the collaboration failure that would justify
> speaking — silence is the default, and intervention is gated on a
> labelled breakdown, not a running value computation.

## Definition / Mechanism

Yang, Xu & Pei (2026) define proactive collaboration as
an agent's ability to decide, at each turn of a multi-user conversation,
whether to remain silent or provide a group-facing intervention before
being explicitly asked: "A non-silence action is appropriate only when the
conversation contains evidence of an intervention-worthy breakdown, the
selected intervention matches the collaboration issue, and the response is
likely to help the group move forward without disrupting productive
discussion."[^c1]

A **collaboration breakdown** is "an evidence-grounded state where the
group may lose progress, shared understanding, coordination quality, or
fair participation without timely repair" — operationalised into seven
named categories (conflict, uncertainty, underspecified plan, forgotten
constraint, goal drift, discussion loop, participation imbalance, risky
commitment).[^c2]

ProACT is a two-step decision pipeline over the conversation history
$H_t$: $(b_t, z_t) = \mathrm{Diagnose}(H_t)$, where $b_t$ is the detected
breakdown (if any) and $z_t \in \{0,1\}$ says whether intervention is
warranted; if $z_t=0$ the agent outputs silence, otherwise the breakdown is
routed to a matching collaboration skill $k_t = r(b_t)$ and the action is
$a_t = \pi_{k_t}(H_t) \in \{\emptyset, u_t\}$. Each skill is a lightweight
operating procedure with a trigger condition, diagnostic cues, social
constraints and an output contract; the diagnosis step "accounts for local
context, such as who is speaking, whether a question is already directed
to another participant, whether the group is actively making progress, and
whether the evidence is strong enough for a concise intervention."[^c3]

On a held-out benchmark built from GitHub issue discussions and QMSum
meeting transcripts plus synthetic conversations with injected breakdowns,
"the final dataset contains 3,244 examples: 2,444 real examples and 800
synthetic examples, balanced into 1,622 intervention cases and 1,622
silence cases."[^c4]

Across five LLM backbones (GPT-5.4, Kimi K2.5, Claude Sonnet 4.6, Gemini
3.1 Pro Preview, GPT-OSS-120B), tested against a Direct Chat baseline that
answers every turn without a silence option, "ProACT improves every
reported metric for every model, including collaborative appropriateness,
non-interruptiveness, conciseness, and intervention quality."[^c5]

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (Yang et al. 2026) | ProACT, breakdown-aware proactive agent | exact |
| This wiki | collaboration breakdown diagnosis | exact — the diagnosis stage named for its function |
| Proactive-service POMDP survey ([[intervention-advantage]], Tang et al. 2026) | intervention advantage, $\Delta_\eta$ | close — same silent-vs-speak gate, scored by a value difference over four action modes rather than a discrete breakdown label; single-user service tasks, not multi-user collaboration |

## Why it matters

This is a named, benchmarked trigger for *when* an agent should speak
unprompted in a group setting — the counterpart, for the answerer's
initiative, to selection criteria (stall 2) that assume the agent is
already the one asking. It replaces "ask whenever uncertain" with "ask
only once a specific, labelled failure mode is evidenced," and shows the
gate is learnable by prompting alone (no fine-tuning reported) across five
different backbones.

## Limits

- The breakdown taxonomy (Table 1, seven categories) is the authors'
  operationalisation of prior CSCW and conversation-analysis theory, not a
  claim that these seven categories are exhaustive or that a real
  deployment's failure modes fall cleanly into one label.
- Labels and quality scores come from an LLM judge (GPT-5.4-Nano) over an
  LLM-annotated, partly synthetic (800/3,244) dataset; only 694 examples
  received human review for disagreement resolution, so the effect sizes
  in `## Definition / Mechanism` are judge-scored, not human-graded end to
  end.
- `yang-2026-proact` is a single 2026 arXiv preprint reporting its own
  benchmark and baseline; no independent replication is cited.

## Related

[[intervention-advantage]] · [[value-of-information]] · [[bounded-rationality]] · [[abstention]]

[^c1]: yang-2026-proact — "A non-silence action is appropriate only when the conversation contains evidence of an intervention-worthy breakdown, the selected intervention matches the collaboration issue, and the response is likely to help the group move forward without disrupting productive discussion."
[^c2]: yang-2026-proact — "an evidence-grounded state where the group may lose progress, shared understanding, coordination quality, or fair participation without timely repair"
[^c3]: yang-2026-proact — "accounts for local context, such as who is speaking, whether a question is already directed to another participant, whether the group is actively making progress, and whether the evidence is strong enough for a concise intervention."
[^c4]: yang-2026-proact — "the final dataset contains 3,244 examples: 2,444 real examples and 800 synthetic examples, balanced into 1,622 intervention cases and 1,622 silence cases."
[^c5]: yang-2026-proact
