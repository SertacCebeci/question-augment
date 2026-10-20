---
description: "The silent attachment of a word to the wrong referent, operationalising Quine's indeterminacy of translation as a checkable classification of promoted answers."
aliases: ["kangaroo effect", "Quinean underdetermination", "indeterminacy of translation"]
sources: ["cordella-2026"]
---
# Kangaroo effect

> A named failure mode for stall 5: an answer that looks like a resolved
> constraint but has silently attached to the wrong referent, plus an
> outcome classification that turns "was this a real constraint?" into a
> measurable, four-way decision.

## Definition / Mechanism

"The failure mode that organizes the entire enterprise is what we call the
kangaroo effect: the silent attachment of a word to the wrong referent"
Cordella & Cappelli (2026) — named after Cook's expedition
recording a word for "kangaroo" without ever verifying what question the
informant thought he was answering.[^c1]

"The kangaroo effect is our operational rendering of Quine's (1960)
indeterminacy of translation: two hypotheses about a word's referent can
agree on every scene observed so far and diverge only on scenes never
shown."[^c2]

The protocol classifies every word's outcome by comparing the promoted
hypothesis set $\mathcal{H}_w$ to the true referent $r_w$: `unresolved` if
never promoted, `KANGAROO` if promoted and $r_w \notin \mathcal{H}_w$,
`CORRECT` if promoted and $\mathcal{H}_w=\{r_w\}$, and
`UNDERDETERMINED` if promoted with $r_w \in \mathcal{H}_w$ but
$|\mathcal{H}_w|>1$: "a word is a kangaroo only if the true referent is
provably excluded; if it survives alongside extensionally indistinguishable
rivals, the honest output is the equivalence class — Quinean
underdetermination made operational."[^c3]

Two fail-safes back the classification. A promoted anchor that later fails
a probe is revoked rather than left standing: "in no run reported in this
paper was a false translation ever left promoted."[^c4]

When no discriminating scene exists in the world at all, the protocol
abstains rather than guesses: "the contrastive precondition ... is never
met, and the protocol abstains entirely (50/50 unresolved)."[^c5]

Under deliberately injected "kangaroo traps" (decoy hypotheses
extensionally equivalent to the truth on a restricted scene set), "naive
ostension and pure statistical learning" were fooled in 100% of runs, while
the full protocol ([[active-probing|active probing]] + pre-registration + revocation) promoted
no kangaroo in any of 200 trap runs.[^c6]

## Why it matters

For stall 5 — is what came back actually a constraint? — this gives a
name and a decision procedure for the case where an answer is accepted as
resolving but has quietly attached to the wrong world: the distinction
between "wrong" (KANGAROO), "right but underdetermined" (declare the
equivalence class), and "no answer yet" (abstain) replaces a single
accept/reject judgement with three outcomes, each independently checkable
against ground truth in this micro-world.

## Limits

The classification is checkable only because the constructed lexicon gives
complete ground truth — a condition no real interlocutor offers, which is
the paper's own stated reason for building the micro-world. The zero-false-
promotion results are reported for a scripted, noiseless (temperature-0)
LLM informant over at most 400 runs in one micro-world; the traps tested are
the two the authors designed (an atomic and a conjunctive decoy), not an
adversarial or naturally occurring set. `cordella-2026` is a single 2026
arXiv preprint; no independent replication is cited.

## Related

[[active-probing]] · [[llm-hypothesis-proposer]] · [[constraint-as-information]] · [[semantic-entropy]]

[^c1]: cordella-2026 — "The failure mode that organizes the entire enterprise is what we call the kangaroo effect: the silent attachment of a word to the wrong referent"
[^c2]: cordella-2026
[^c3]: cordella-2026 — "a word is a kangaroo only if the true referent is provably excluded; if it survives alongside extensionally indistinguishable rivals, the honest output is the equivalence class — Quinean underdetermination made operational"
[^c4]: cordella-2026 — "in no run reported in this paper was a false translation ever left promoted"
[^c5]: cordella-2026
[^c6]: cordella-2026
