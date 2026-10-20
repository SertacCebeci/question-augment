---
description: "D2D ranks candidate attribute questions by preference uncertainty times a top-weighted discrimination entropy, asking only while the leading items remain unseparated."
aliases: ["D2D", "Dialogue to Discovery", "attribute preference uncertainty times attribute cumulative entropy"]
sources: ["harne-2026"]
---
# D2D attribute-informativeness score

> In a conversational product-search assistant, which attribute to ask about next is decided by multiplying two signals — how uncertain the assistant still is about the user's preference for that attribute, and how well that attribute currently separates the top-ranked candidate items — and whether to ask at all is gated by a separate check on whether the leading items are already distinguishable.

## Definition / Mechanism

For each attribute $j$ still live in the retrieved catalog, D2D computes two
scores per turn. Attribute Preference Uncertainty (APU), $\delta_j$, sums the
overlap between the confidence intervals of competing items' preference
scores on that attribute — high overlap means the assistant cannot yet tell
which value the user prefers: "The first, Attribute Preference Uncertainty
(APU), quantifies the [[efe-planning-as-variational-inference|ambiguity]] in the user's preference model (due to AVP).
High APU indicates that the assistant is uncertain about the importance a
user assigns to an attribute, leading to uncertainty in item preference
scores."[^c1]

Attribute Cumulative [[entropy|Entropy]] (ACE), $\gamma_j$, sums the Shannon entropy of
that attribute's value distribution across expanding top-$n$ windows of the
current ranking: "The second factor, Attribute Cumulative Entropy (ACE),
measures how effectively an attribute's values differentiate items,
particularly among the highest-ranked candidates... By summing across
increasing values of $n$, we prioritize attributes that are most
discriminative at the top of the ranking."[^c2]

The two are multiplied and the top attributes are chosen: "We rank
attributes by $\delta_j \times \gamma_j$ and select the top $m$ to guide
question generation."[^c3]

Whether to ask at all, rather than recommend, is a separate decision: the
items whose preference-score confidence interval overlaps the top item's
above a threshold $\tau$ form the top overlapping item set (TOI); the system
recommends only once TOI has shrunk to the number of available slots: "The
assistant decides to recommend items if the top overlapping set size
$|\bar C^t| \le m$ ... otherwise, it defers recommendation ($r_t = \emptyset$)
to seek more information via attribute-based questions."[^c4]

Simulated against three Amazon-derived product datasets, this combined
policy "achieves a 22.2–29.9% improvement in target-finding accuracy,
6.6–16.1% reduction in abandonment, and 27.5% shorter average conversations
over the state-of-the-art baselines."[^c5]

## Known as

| Field | Name there | Match |
|---|---|---|
| conversational-recommendation | D2D | exact (abbreviation) |
| conversational-recommendation | Dialogue to Discovery | exact (full name) |

## Why it matters

This is a two-part answer to "which axis first" that this stall's map does
not otherwise carry: a *composite* criterion (ambiguity × discriminativeness)
rather than a single entropy-drop or EIG number, paired with a *separate*
gate deciding whether to ask at all versus stop asking and show results — a
concrete, measured instance of coupling stall 2 (selection) to stall 7
(stopping) inside one policy, evaluated end-to-end rather than as an
abstract ordering result.

## Limits

The comparison is against LLM-simulated users (gpt-4.1-mini / o4-mini
playing the customer) whose patience and truthfulness follow the same
paper's own model, not independently sourced human behavior; the abstract
also reports "a complementary user study" but its method and numbers are not
in the slices of the extract read for this note. $\alpha$, $\tau$ and $m$
are fixed hyperparameters (e.g. $\tau = 0.2$, $m = 4$) reported as settings,
not swept or justified by an ablation in the material read. [?] no
independent replication found.

## Related

[[expected-information-gain]] · [[generalized-binary-search]] · [[stage-dependent-elicitation-strategy]] · [[value-of-information]]

[^c1]: harne-2026
[^c2]: harne-2026
[^c3]: harne-2026 — "We rank attributes by δj × γj and select the top m to guide question generation."
[^c4]: harne-2026
[^c5]: harne-2026 — "D2D achieves a 22.2–29.9% improvement in target-finding accuracy, 6.6–16.1% reduction in abandonment, and 27.5% shorter average conversations over the state-of-the-art baselines."
