---
description: "A hand-built tree of interview openers and BM25-matched follow-up branches that fixes a screening agent's early question order offline, so a weaker LLM interviewer need not choose it live."
aliases: ["dialogue tree", "precomputed dialogue tree", "structured algorithmic guidance"]
sources: ["gong-2026"]
---
# Precomputed dialogue tree routing

> Instead of letting the interviewing LLM choose each question live, Gong & Guecha (2026)
> precompute a tree of openers and follow-ups offline, so the first several
> turns of axis selection cost no model call and carry no live selection
> variance.

## Definition / Mechanism

For an automated depression-screening interview that must estimate a BDI-II
score from 21 symptoms without asking about them directly, the authors
"constructed a precomputed dialogue tree with 7 symptom clusters, 12
cluster-opening questions, and 17 follow-up probes," grouping symptoms
"thematically so that semantically related items can be probed within a
single conversational thread."[^c1]

The first question of every conversation is hardcoded (targeting sadness
and anhedonia); subsequent openers are pulled on demand — "the system
retrieves the first unused opener whose target symptoms appear in the
orchestrator's current priority list of unassessed or low-confidence
items" — and within an opener, "BM25 text matching on the persona's
response chooses the best follow-up branch." Clinically sensitive symptoms
(suicidal ideation, loss of interest in sex) are deliberately left off the
tree and handled case-by-case rather than scripted. This structure covers
"approximately 2-3 interview turns without any LLM call."[^c2]

The tree was added specifically to compensate for a weaker open-source
interviewer model (Gemma 27B) that showed "higher [[fisher-information|score variance]] across
runs" and "less reliable adherence to the structured interview
instructions" than a stronger paid model; the hybrid system using the tree
(plus two other components) reached an ADODL of 0.9063, beating the same
team's paid-model baseline (0.8841) at about one-quarter of the
per-persona API cost.[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Conversational agents / clinical NLP (Gong & Guecha 2026) | dialogue tree | exact |
| Conversational agents / clinical NLP (Gong & Guecha 2026) | structured algorithmic guidance (umbrella term, covers this plus two other components) | close |

## Why it matters

This is a working answer to stall 2 (which axis first) and stall 3 (how a
question touches the axis) that removes live selection entirely for the
opening moves: axis order is fixed at design time by a human's thematic
grouping, not computed by an information measure or by the model at
run-time, and a cheap retrieval rule (BM25 over the persona's last answer)
substitutes for live natural-language question generation on the
follow-up. It is offered as a [[calibration|reliability]] patch for a weaker interviewer,
not as an efficiency or optimality claim over EIG or greedy submodular
selection.

## Limits

- The claim rests on one system, one task (eRisk 2026 Task 1, 20 personas)
  and no independent replication; the ADODL improvement is attributed
  jointly to the dialogue tree, reliability-weighted aggregation and
  cluster imputation together — the paper does not isolate the tree's own
  contribution with an ablation.[^c4]
- The tree's clusters and donor groupings were "manually chosen," not
  learned or derived from an information-theoretic criterion — there is no
  optimality argument analogous to [[optimal-decision-tree]] or
  [[generalized-binary-search]].
- It only covers the first 2-3 turns per persona; after the tree is
  exhausted, axis selection reverts to the live orchestrator (see
  [[confidence-weighted-symptom-prioritization]]), so the tree does not
  answer selection for the bulk of an interview.

## Related

[[confidence-weighted-symptom-prioritization]] · [[optimal-decision-tree]] · [[generalized-binary-search]] · [[value-of-information]]

[^c1]: gong-2026 — "we constructed a precomputed dialogue tree with 7 symptom clusters, 12 cluster-opening questions, and 17 follow-up probes. Symptoms are grouped thematically so that semantically related items can be probed within a single conversational thread"
[^c2]: gong-2026
[^c3]: gong-2026 — "less reliable adherence to the structured interview instructions embedded in the prompt [12]. We developed three algorithmic components to address these limitations."
[^c4]: gong-2026 — "We developed three algorithmic components to address these limitations."
