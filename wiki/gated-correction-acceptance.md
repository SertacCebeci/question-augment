---
description: "A user correction to a stored belief is accepted only if the belief is weakly held or retrieval corroborates it, which separates revision from sycophancy on a synthetic benchmark."
aliases: ["correction acceptance rule", "weak-belief correction rule", "corroborated correction gate"]
sources: ["doi-10-48550-arxiv-2609-26035"]
---
# Gated correction acceptance

A conversational agent that holds a claim faces a user who says the claim is
wrong. Accepting the correction every time is one failure; resisting it every
time is another. The paper's rule sits between them. A stored belief b carries
a combined confidence κ̂(b). A correction to b is accepted if κ̂(b) is below a
threshold θacc = 0.75, or if the correction is corroborated by a retrieval
store. Otherwise the belief is kept and the refusal is written to a log. The
authors state the reason directly: "an epistemic-humility layer that accepts
every correction is sycophancy", not humility.[^c1]

Three sub-cases follow from the same rule. A correction to a claim the store
does not hold is "accepted unconditionally, logged, and not acknowledged", since
there is no prior value to retract.[^c2] For a weakly held belief, a correction
is accepted even when retrieval contradicts it; for a strongly held one,
retrieval corroboration "can rescue a strongly held belief but never vetoes a
correction to a weak one".[^c3] Retrieval conflicts apply the same weak-belief
threshold "with no corroboration clause".[^c17] Accepted revisions re-enter the
store with fixed post-revision states, and an acknowledgment utterance is
emitted only when a matching accepted log entry exists.[^c18] The paper calls
this auditability: "every public admission of error traces to a recorded state
change".[^c7]

What was measured. On a constructed benchmark (120 three-session conversations
per arm, half the statements and corrections false by injection), the Stage-B
rule accepts 87.5% of true corrections and 42.0% of false ones.[^c10] Most of
the false-side acceptance runs through the unheld path: corrections to claims
the store did not yet hold were accepted unconditionally, 93 of 93 true and 62
of 62 false.[^c11] A post hoc split, not pre-specified, isolates corrections
that contradicted a held belief: 12 of 27 true (0.444) against 19 of 131 false
(0.145).[^c4] The fact-clustered 95% interval for that held-belief gap is
"Its fact-clustered 95% interval, [0.09, 0.54]", which excludes zero but reaches
below the 0.10 margin the authors set.[^c6] The authors attribute the held-belief
discrimination to "the corroboration clause operating over the" constructed
retrieval store.[^c5] A freshly seeded replication reports "correction
discrimination 0.892 vs. 0.482".[^c12]

Acknowledgment soundness holds by construction and was checked on a real model:
42 of 42 acknowledged revisions trace to an accepted log entry.[^c7] The reverse
direction is a different kind of claim: "The reciprocal direction is a measured
quantity, not a guarantee".[^c21] In the run, 42 of the 197 accepted revisions
were flagged for acknowledgment, about 21%.

## Limits

- **The guarantee is on linkage, not wording or truth.** "It certifies neither
  the wording of the admission" nor the truth of the accepted value; the
  template names a stored prior value the layer may never have uttered.[^c8]
  An auditable admission is therefore a trace to a state change, not evidence
  that the agent was wrong in the way it says.
- **Adversarial users are the stated residual threat.** The authors write that
  "user can rewrite any weakly held belief without corroboration".[^c9] Their
  rule has no answer to a patient adversary who pushes on the weak beliefs.
  Adjudicating contested corrections is listed as future work.
- **The held-belief result depends on the store.** The gap "scales with the
  constructed store", and by the rule's structure is largely designed in; the
  realized store holds "34 of the 60 subjects, one of them stale".[^c13][^c22]
  The authors add that the gap "is not a store-independent property of the
  layer".[^c15]
- **False acceptance stays high.** The paper calls the absolute false-acceptance
  rate on the scored set "remains substantial", at about 0.42 to 0.48 across
  grids, mostly through the unheld path.[^c23] Even on the held-belief contrast,
  which is positive, most false corrections still pass. That is my reading of
  the numbers, not a claim the paper makes.
- **Small, synthetic, single model.** The benchmark is generator-built, the
  model is a 0.5B instruction-tuned network, and "All margins below were
  recorded by the author before the Stage-B grid ran".[^c20] The paper says the
  Stage-B tests were "pre-specified, not preregistered".[^c14]
- **The gate reads the confidence it is given.** κ̂ is a combination over
  extractors, and "a layer gated on their conservative minimum inherits" the
  token-probability extractor's rankings when that signal binds; see
  [[semantic-entropy]].[^c19]

## Related

- [[challenge-type-dissociation-in-capitulation]] — how models give way under
  pushback; this rule is a designed resistance to the same failure, which the
  cited measurement did not test.
- [[belief-base-revision]] — the store is a base of received claims; the
  paper cites AGM [[agm-belief-revision]] as lineage only and does not implement
  its operators.
- [[hint-adherence-without-acknowledgement]] — the reverse split: a model that
  uses a cue but does not say so, where this layer makes the admission
  auditable by construction.
- [[provenance-gated-assertion]] — the expression side of the same layer; the
  source cap decides how loudly a stored claim is voiced.

[^c1]: doi-10-48550-arxiv-2609-26035 — "an epistemic-humility layer that accepts every correction is sycophancy"
[^c2]: doi-10-48550-arxiv-2609-26035 — "accepted unconditionally, logged, and not acknowledged"
[^c3]: doi-10-48550-arxiv-2609-26035 — "retrieval corroboration can rescue a strongly held belief but never vetoes a correction to a weak one"
[^c4]: doi-10-48550-arxiv-2609-26035 — "12 of 27 true (0.444) versus 19 of 131 false (0.145)"
[^c5]: doi-10-48550-arxiv-2609-26035 — "the corroboration clause operating over the"
[^c6]: doi-10-48550-arxiv-2609-26035 — "Its fact-clustered 95% interval, [0.09, 0.54]"
[^c7]: doi-10-48550-arxiv-2609-26035 — "every public admission of error traces to a recorded state change"
[^c8]: doi-10-48550-arxiv-2609-26035 — "It certifies neither the wording of the admission"
[^c9]: doi-10-48550-arxiv-2609-26035 — "user can rewrite any weakly held belief without corroboration"
[^c10]: doi-10-48550-arxiv-2609-26035 — "the rule accepts 87.5% of true corrections and 42.0% of false"
[^c11]: doi-10-48550-arxiv-2609-26035 — "accepted unconditionally (93 of 93 true and 62 of 62 false)"
[^c12]: doi-10-48550-arxiv-2609-26035 — "correction discrimination 0.892 vs. 0.482"
[^c13]: doi-10-48550-arxiv-2609-26035 — "scales with the constructed store"
[^c14]: doi-10-48550-arxiv-2609-26035 — "pre-specified, not preregistered"
[^c15]: doi-10-48550-arxiv-2609-26035 — "is not a store-independent property of the layer"
[^c17]: doi-10-48550-arxiv-2609-26035 — "with no corroboration clause"
[^c18]: doi-10-48550-arxiv-2609-26035 — "Accepted revisions re-enter the store with fixed post-revision"
[^c19]: doi-10-48550-arxiv-2609-26035 — "a layer gated on their conservative minimum inherits"
[^c20]: doi-10-48550-arxiv-2609-26035 — "All margins below were recorded by the author before the Stage-B grid ran"
[^c21]: doi-10-48550-arxiv-2609-26035 — "The reciprocal direction is a measured quantity, not a guarantee"
[^c22]: doi-10-48550-arxiv-2609-26035 — "holds 34 of the 60 subjects, one of them stale"
[^c23]: doi-10-48550-arxiv-2609-26035 — "remains substantial"
