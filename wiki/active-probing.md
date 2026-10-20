---
description: "Choosing the next probe scene to maximally split the surviving hypothesis set for an LLM informant's word meaning, paired with pre-registration and revocation, drove undetected mistranslation to zero."
aliases: ["active scene selection", "active probing"]
sources: ["cordella-2026"]
---
# Active probing

> An active-learning selection rule for the next disambiguating scene shown
> to an LLM informant, combined with pre-registration and a revocation
> channel, that drove silent mistranslation to zero across 400+ runs.

## Definition / Mechanism

In Cordella & Cappelli (2026)'s constructed-lexicon
protocol, each word $w$ carries a surviving hypothesis set $\mathcal{H}_w$
(a [[version-space|version space]], updated by cross-situational elimination). The next probe
scene $s^*$ is chosen to maximise, lexicographically: (i) the split of
$\mathcal{H}_w$, (ii) the expected presence of the word, (iii) novelty of
unconstrained attributes:

$$s^* = \arg\max_s \big(\min(V_s, |\mathcal{H}_w| - V_s),\ \mathbb{1}[V_s>0],\ \mathrm{nov}(s)\big),\quad V_s = \sum_{h\in\mathcal{H}_w} \mathbb{1}[h(s)]$$

"The split criterion is the anti-kangaroo mechanism in its purest form: it
sends the conversation precisely to the scenes on which rival hypotheses
disagree."[^c1]

A four-arm campaign (probe selection random/active × [[recovery-postulate|recovery]] round
off/on, 50 seeds each) found that active selection alone drove the
[[kangaroo-effect|kangaroo]] rate to zero across all 50 worlds.[^c2]

Combining active selection with a second "recovery" probing round raised
coverage above the passive baseline at zero kangaroos: "these two
mechanisms are synergistic rather than additive: the recovery round
without active selection recovers little and can even promote a false
translation."[^c3]

The protocol adds two elements with no counterpart in
[[generalized-binary-search|Dasgupta's greedy]]: predictions are
pre-registered before the probe scene is shown, so a hypothesis cannot be
scored on evidence seen after the fact, and a promoted anchor that later
fails a probe is revoked rather than left standing.

## Why it matters

This is an experimental, not merely simulated, demonstration that
maximal-split query selection is the mechanism that suppresses a silent
wrong-referent error — the LLM-informant setting makes the failure mode
observable and countable, where pure theory only bounds expected query
count.

## Transfer

| | |
|---|---|
| **Home field** | active learning: Dasgupta's greedy version-space split, a finite noiseless test set, a mass-balance criterion |
| **Here (language-grounding, LLM informants)** | a finite discrete hypothesis set per word with an implicit uniform prior (count-split, not mass-split), tie-broken by expected word presence and scene novelty, embedded in a promote/revoke state machine |
| **What survives** | the core rule — pick the scene splitting the surviving hypotheses most evenly — and the qualitative synergy with a second corrective round |
| **What does not** | Dasgupta's approximation guarantee: no bound is proved here, and the reported zero-kangaroo result is an empirical count over 50 seeds under a noiseless, finite, scripted [[possible-worlds|hypothesis space]], not a worst-case theorem |

## Limits

The zero-kangaroo result holds under the tested conditions: a noiseless
(temperature-0) informant, a finite scripted hypothesis space, and the
paper's promotion criterion; under injected informant noise the guarantee
survives only up to 2% per-word channel noise and degrades thereafter by
[[abstention]] rather than error — a boundary this note does not re-derive.
`cordella-2026` is a single arXiv preprint (2026); no independent
replication is cited.

## Related

[[generalized-binary-search]] · [[kangaroo-effect]] · [[llm-hypothesis-proposer]] · [[constraint-seeking]]

[^c1]: cordella-2026
[^c2]: cordella-2026 — "a four-arm campaign over 50 random worlds (Section 5.1) showing that active probing drove the kangaroo rate to zero across all 50 tested worlds"
[^c3]: cordella-2026 — "these two mechanisms are synergistic rather than additive: the recovery round without active selection recovers little and can even promote a false translation"
