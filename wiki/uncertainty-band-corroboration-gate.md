---
description: "A calibrated verifier scores each atomic fact; only scores in a two-sided uncertain band trigger domain-restricted web retrieval, leaving confident facts untouched."
aliases: ["Atomic+Search", "uncertainty-triggered web corroboration", "uncertainty-gated corroboration"]
sources: ["arxiv-2604-11036"]
---
# Uncertainty-band corroboration gate

> Do not retrieve for what a compact verifier already answers confidently in
> either direction — retrieve only for what it cannot yet call.

## Definition / Mechanism

Vinod & Erk (2026) first decompose a claim and its
single evidence document into atomic predicate–argument facts, each aligned
by embedding similarity to a local snippet, and score every fact with a
compact evidence-grounded verifier (MiniCheck-7B) as a support probability
$p_i \in [0,1]$: "Facts are labeled supported, refuted and Uncertain based
on the grounding probabilities. Facts with pi ∈ [α, β] (the Uncertain band)
trigger targeted web corroboration before a final verdict is produced."[^c1]

The band is fixed and two-sided ($\tau_{hi}=0.80$, band $[0.25, 0.80]$): a
fact scored above or below the band is settled by the compact verifier
alone: "Uncertainty-triggered web corroboration is applied only to facts
with intermediate scores between 0.25 and 0.80. For these, we issue concise
web queries that restate the fact and include its local snippet as context,
restricting search to authoritative biomedical sources."
[^c2]

A fact inside the band is re-scored, not just annotated: "Retrieved
snippets are summarized with inline citations into an auxiliary text,
which is concatenated with the snippet to form augmented evidence;
MiniCheck-7B is re-run on this augmented evidence, and we record both the
original and updated probabilities and whether rescoring occurred."
[^c3]

The band's edges are themselves calibrated, not guessed: "The 0.25–0.80
band is chosen from a held-out calibration study of MiniCheck [12], where
most ambiguous cases concentrate."[^c4]

When the web corroboration a gated fact receives disagrees with the
document the system was given, the mechanism does not let the louder
source win — it withdraws to abstention instead: "When D is insufficient,
our uncertainty-gated corroboration step may consult additional sources; if
those conflict with D, we abstain with Uncertain rather than overwrite the
provided context."[^c5]

## Why it matters

The gate is load-bearing, not decorative: an ablation that removes web
corroboration entirely (No-Search) drops BIONLI-300 F1 by 4.7 points, and
removing atomic decomposition costs even more, 6.4 points — "removing web
corroboration (No-Search) reduces F1 from 66.7% to 62.0% (− 4.7); removing
atomic decomposition (No-Atomic) further drops F1 to 60.3% (− 6.4),
indicating decomposition is the larger contributor."
[^c6]

The gate also does what a threshold is supposed to do — fire rarely: "web
corroboration was invoked for only a minority of atomic facts on average,
indicating that external evidence is consulted selectively under
calibrated uncertainty rather than routinely."
[^c7]

Together this separates *whether to ask* (band membership) from *whether
to trust what comes back* (the conflict-abstain rule), at the grain of a
single predicate–argument fact rather than a whole query — a finer unit
than a threshold gating one retrieval-or-not decision per question, as in
[[calibrated-retrieval-budget-allocation]].

## Limits

- The band's edges (0.25, 0.80) are fixed from one held-out calibration
  study of one verifier (MiniCheck) and carried unchanged across three
  datasets; the paper's own future work names this as unresolved: "Our
  approach still relies on fixed calibration thresholds, curated domain
  allow-lists, and heuristic snippet selection. Future work includes
  adaptive calibration."[^c8]
- The conflict-abstain rule (^c5) is stated as a design decision and
  appears in the aggregate results, but the paper reports no ablation that
  isolates its effect from the rest of the pipeline — how often it fires,
  and what it costs in coverage, is unverified by this note.
- The web side of the gate is restricted to a curated domain allow-list
  (PubMed, WHO, CDC, FDA, NIH, ClinicalTrials.gov, Wikipedia); the
  mechanism has not been shown to hold when corroboration is open-domain
  search rather than a vetted source list.
- Evaluated with one compact verifier and one embedding model for snippet
  selection; whether the band transfers to a different verifier's
  probability scale is untested here.

## Related

[[calibrated-retrieval-budget-allocation]] · [[calibration]] · [[abstention]] · [[verification-aware-stopping]] · [[uncertainty-gated-lm-fallback]]

[^c1]: arxiv-2604-11036 — "Facts are labeled supported, refuted and Uncertain based on the grounding probabilities. Facts with pi ∈ [α, β] (the Uncertain band) trigger targeted web corroboration before a final verdict is produced."
[^c2]: arxiv-2604-11036
[^c3]: arxiv-2604-11036 — "Retrieved snippets are summarized with inline citations into an auxiliary text, which is concatenated with the snippet to form augmented evidence; MiniCheck-7B is re-run on this augmented evidence, and we record both the original and updated probabilities and whether rescoring occurred."
[^c4]: arxiv-2604-11036 — "The 0.25–0.80 band is chosen from a held-out calibration study of MiniCheck [12], where most ambiguous cases concentrate."
[^c5]: arxiv-2604-11036 — "When D is insufficient, our uncertainty-gated corroboration step may consult additional sources; if those conflict with D, we abstain with Uncertain rather than overwrite the provided context."
[^c6]: arxiv-2604-11036 — "On BIONLI-300 (Table 3), removing web corroboration (No-Search) reduces F1 from 66.7% to 62.0% (− 4.7); removing atomic decomposition (No-Atomic) further drops F1 to 60.3% (− 6.4), indicating decomposition is the larger contributor."
[^c7]: arxiv-2604-11036 — "In our experiments, web corroboration was invoked for only a minority of atomic facts on average, indicating that external evidence is consulted selectively under calibrated uncertainty rather than routinely."
[^c8]: arxiv-2604-11036 — "Our approach still relies on fixed calibration thresholds, curated domain allow-lists, and heuristic snippet selection. Future work includes adaptive calibration"
