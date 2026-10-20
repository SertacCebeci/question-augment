---
description: "Models a non-expert user's preferences as a state that starts sparse and grows only when an agent's dialog action (question, example, or explanation) matches what the feature needs."
aliases: ["CoPref", "Co-constructed Preferences"]
sources: ["saracay-2026"]
---
# Preference construction (CoPref)

> A model of underspecified users in which a preference over a feature is
> not retrieved by asking, but constructed by an agent's dialog action —
> and only if that action matches what the feature needs.

## Definition / Mechanism

CoPref models an interactive task over a feature set $F$ and target item
$x^*$. A user's preference state $S_t \subseteq F(x^*)$ starts sparse
($S_1$) and updates each turn based only on the agent's previous message: a
feature $f$ enters $S_t$ once an agent action "unlocks" it. Features
partition into $F_s$ (search — assessable by a direct question), $F_e$
(experience — the user needs to see example items before reacting), and
$F_c$ (credence — the user needs a technical explanation to have the domain
knowledge to hold an opinion at all). A clarifying question unlocks only
search features; showing example items unlocks experience (and search)
features; a technical explanation unlocks credence (and search) features.
This replaces the "expert user" assumption ($S_t = F$ for all $t$, any
question answerable) that the paper argues rewards an agent for bombarding
users with questions upfront.[^c1]

A human study (n=25, simulated sweater shopping, 10 features each) tested
the model against that expert-user baseline: no participant had only search
features — every one requested an example or explanation on at least one
feature — and, aside from gender, no single feature was uniformly search,
experience, or credence across participants, i.e. the type is a property of
the individual, not fixed for a population.[^c2]

Dialog actions measurably unlock the matching type: of (participant,
feature) pairs where the participant asked for examples after indicating
uncertainty, 85% were subsequently unlocked (went on to state a non-empty
preference); of pairs where the participant asked for an explanation, 75%
were unlocked.[^c3]

## Known as

| Field | Name there | exact / close |
|---|---|---|
| Preference elicitation (Saracay et al. 2026) | CoPref / Co-constructed Preferences | exact |

[^c4]

## Transfer

| | |
|---|---|
| **Home field** | Information economics — the Search-Experience-Credence typology (Nelson 1970; Darby & Karni 1973, as cited by Saracay et al. 2026), classifying product qualities by what a buyer needs before assessing them, under information asymmetry between seller and buyer. |
| **Here** | Reused to classify which agent dialog action — question, example item, or technical explanation — a feature needs before a non-expert dialog user can state a preference over it. |
| **What survives** | The three-way partition of attributes by the kind of information required to judge them, and the finding that the split is a per-individual property rather than fixed across a population. |
| **What does not** | The signaling economics of the original framework — quality guarantees, certification, adverse selection between a seller and a buyer — has no counterpart in CoPref's single-agent, single-user dialog setting; only the assessability taxonomy travels. |

[^c5]

## Limits

CoPref assumes a feature's preference is unlocked by a single matching
agent action rather than by iterative refinement, and that once unlocked a
preference is never revised or forgotten — the state $S_t$ is
monotonically non-decreasing. The paper names both as simplifications made
to keep the modeled user easier to collaborate with, not harder; the
reported agent failures (see [[coshop-benchmark]]) therefore hold under a
favorable model of the user, not a worst case.[^c6]

## Related

[[coshop-benchmark]] · [[cross-type-eig]] · [[volume-removal]] · [[expected-information-gain]]

[^c1]: saracay-2026 — "Search features Fs are easy for the user to form preferences over; they do not require additional information for the user to assess what they prefer (e.g., price, size)."
[^c2]: saracay-2026 — "0 participants had all search features, as every participant asked for examples and/or an explanation on at least one feature"
[^c3]: saracay-2026 — "of (participant, feature) pairs where the participant requested examples after indicating uncertainty, 85% were subsequently ”unlocked” (i.e., the participant went on to provide a non-empty free-text preference); of pairs where the participant requested an explanation, 75% were unlocked."
[^c4]: saracay-2026 — "we propose C O P REF (Co-constructed Preferences), a model of how non-expert users construct — rather than simply reveal — preferences based on agent dialog actions"
[^c5]: saracay-2026 — "The Search-Experience-Credence (SEC) framework (Nelson, 1970; Darby & Karni, 1973; Ford et al., 1990) formalizes this by classifying features according to what a consumer needs in order to assess them"
[^c6]: saracay-2026 — "First, users form a preference over a feature based on a single agent action, rather than requiring multiple interactions. Second, once formed, preferences are stable and never forgotten: we assume that St is monotonically non-decreasing."
