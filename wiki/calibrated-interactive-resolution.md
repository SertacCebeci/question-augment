---
description: "Gates clarification on a conformal set's size as an ambiguity signal, then restricts information-gain question search to that set, cutting interaction turns under a coverage guarantee."
aliases: ["calibrated interactive resolution"]
sources: ["tran-2026-resolving"]
---
# Calibrated interactive resolution

> Do not score every candidate question against the whole answer space —
> wrap the current belief in a coverage-guaranteed set first, and only ask
> when that set is still large; then search for the question inside it.

## Definition / Mechanism

Tran, Le & Pham (2026) wrap a composed-image-retrieval
belief $p(I\mid q,h_m)$ in split [[conformal-prediction]] (Mondrian,
group-conditional by query-type stratum) to obtain a set $C_\alpha(q,h_m)$
with a finite-sample coverage guarantee, and read its **size as the
[[efe-planning-as-variational-inference|ambiguity]] signal**: small when the belief concentrates, large when many
candidates remain plausible. The decision rule commits when the set is
small enough or the turn budget is spent, and clarifies otherwise:
"$|C_\alpha(q,h_m)|\le\tau$ or $m=M \Rightarrow$ COMMIT, otherwise CLARIFY."[^c1]

When it clarifies, the policy scores each candidate question by
[[expected-information-gain]] (Lindley's criterion), but restricted: the
expectation in that criterion "is taken only over $C_\alpha$ rather than
the full corpus, [so] the policy is cheap to evaluate even for large $D$."[^c2]

The chosen question's answer then updates the belief by a semantic
re-encoding of the query plus a logical reweighting against an MLLM answer
model, the conformal set is recomputed, and the commit/clarify test
repeats until it commits.

Measured effect on CIRR: "A single information-gain question lifts CIRR
success from 58.4 to 74.2 — more than MLLM-Q reaches in three turns — and
by $T=3$ our policy nears the oracle." Random or generic questioning
wastes turns, isolating the criterion's contribution from interaction
itself.[^c3]

An ablation that replaces the information-gain criterion with random
questions, or the conformal trigger with a fixed Top-K threshold, degrades
efficiency more than removing any other tested component.[^c4]

## Why it matters

It gives the two nearby decisions — *is the query ambiguous enough to
interrupt for* (stall 7, via the coverage-guaranteed set size) and *which
question to ask given that it is* (stall 2, via EIG) — a shared, calibrated
quantity instead of two independently-tuned heuristics, and restricting the
search to the conformal set is what keeps the selection step's cost from
scaling with corpus size.

## Transfer

| | |
|---|---|
| **Home field** | Composed image retrieval: a bimodal (image + text-edit) query against a fixed image corpus |
| **Here** | Any asker whose candidate answer space is large enough that scoring every question against every hypothesis is expensive |
| **What survives** | The coverage-guaranteed-set-size-as-ambiguity-gate, and restricting an information-theoretic selection criterion's expectation to that set rather than the full [[possible-worlds|hypothesis space]] |
| **What does not** | The specific axis pool (preserved / changed / viewpoint / background) is domain-annotation-specific to CIRR; the answer model and question generator are the same MLLM, so selection quality is bounded by that one model's [[calibration]], not by the conformal guarantee itself |

## Limits

- The coverage guarantee "inherit[s] the assumptions of split conformal
  prediction: coverage holds under exchangeability between the calibration
  and test distributions and degrades under severe distribution shift,"
  only partially addressed by the Mondrian stratification. The clarification
  policy "relies on an MLLM as both question generator and internal answer
  model, so its quality is bounded by that model and adds inference cost on
  the queries that trigger interaction."[^c5]
- The reported gains are simulator-validated against 4,000 human answers,
  not a fully human-in-the-loop deployment; the paper itself notes
  "simulated users cannot fully capture the variability, inconsistency, and
  strategic behavior of real ones."

## Related

[[expected-information-gain]] · [[conformal-prediction]] · [[value-of-information]] · [[semantic-entropy]]

[^c1]: tran-2026-resolving — "The set size |Cα (q, hm )| is exactly the quantity missing from prior CIR systems: it is small when the (calibrated) belief concentrates—i.e., the query is precise—and large when many candidates remain plausible—i.e., the query is underspecified. We commit when the set is small enough or the turn budget is spent, and clarify otherwise"
[^c2]: tran-2026-resolving — "Because the expectation in Eq. (7) is taken only over Cα rather than the full corpus, the policy is cheap to evaluate even for large D."
[^c3]: tran-2026-resolving — "A single information-gain question lifts CIRR success from 58.4 to 74.2 — more than MLLM-Q reaches in three turns — and by T =3 our policy nears the oracle."
[^c4]: tran-2026-resolving — "Replacing the conformal trigger with a fixed Top-K threshold, the EIG criterion with random questions, or the joint belief update with re-ranking each degrades efficiency; the EIG criterion contributes most."
[^c5]: tran-2026-resolving
