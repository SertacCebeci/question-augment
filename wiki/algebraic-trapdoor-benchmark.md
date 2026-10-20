---
description: "Hides a construction-time secret so the verifier computes ground truth in O(1) while the solver faces an open-decidability membership question, making calibrated abstention measurable."
aliases: ["algebraic trapdoor benchmark", "trapdoor benchmark", "verifier-prover asymmetry benchmark"]
sources: ["rivin-2026"]
---
# Algebraic trapdoor benchmark

> A math benchmark built like a cryptographic trapdoor: construction-time
> secret data makes the ground truth trivial to check but forces the
> solver either to reconstruct hidden algebraic structure or to face a
> membership question of unknown decidability — turning the choice to
> commit or abstain into a ground-truthed, measurable signal instead of a
> guess about the model's confidence.

## Definition / Mechanism

Rivin (2026) constructs subgroup problems in SL(3,Z) from
secret construction-time data $(N,K)$: a subgroup $H$ is built by lifting
generators of $K \subseteq \mathrm{SL}(3,\mathbb{Z}/N)$ and then scrambling
them via Nielsen moves so the published matrices hide $(N,K)$. "the answer
is computable in O(1) closed form by anyone with construction-time data (N,
K), but the solver, without that data, faces either heuristic structural
detection or an algorithmic question of unknown decidability."[^c1]

The benchmark scores four outcomes rather than one: "commit-correct: model
commits to a specific answer matching ground truth." (and symmetrically
commit-wrong, abstain-correct, abstain-wrong), so a model that declines to
answer is scored differently depending on whether the true answer was in
fact undetermined.[^c2]

One family is built specifically to force this distinction: "On the index
variant, the kernel/cokernel asymmetry creates a calibrated [[abstention]]
test: a model that can compute the cokernel but not the kernel-side
membership should abstain rather than commit to the cokernel-side upper
bound."[^c3]

The prompt never asserts that $H$ is finite-index, which is what makes
abstention rational on some instances and forces the distinction to fire
at all: "The prompt design is therefore not neutral: it is a load-bearing
element of the benchmark."[^c4]

## Why it matters

Existing abstention benchmarks measure [[calibration]] against statistical
uncertainty — a model that does not know an answer with confidence. This
design instead grounds abstention in a structural fact the *constructor*
knows and the *solver* cannot derive from the presented instance alone
(the kernel-side membership problem in SL(3,Z) has open decidability
status), so "correctly abstaining" and "correctly computing" are graded
against different, independently verified ground truths on the same
instance family, not against the same accuracy count.

## Transfer

| | |
|---|---|
| Home field | cryptography: a trapdoor function is easy to invert only with a secret, and hard (conjecturally) without it |
| Here | benchmark design for LLM math reasoning and calibrated abstention |
| What survives | the asymmetry structure itself — a constructor-side secret that makes verification O(1) while withholding it from the solver, and using that gap to force a measurable choice between commit and abstain |
| What does not | cryptographic hardness is a computational-complexity assumption with a security parameter; here the solver's difficulty comes from an *open mathematical decidability* question (SL(3,Z) membership) and from heuristic structural detection, neither of which carries a hardness proof or a tunable security level |

## Limits

- Single arXiv preprint (2026), read from the archived extract only, not
  independently verified [?].
- The headline abstention result (§5.2, instance X10) is one 152-minute
  reasoning trace from one model on one instance; the paper reports five
  full traces total across two models and three instance families, not a
  statistical benchmark run.
- Ground truth and the four-way scoring depend on the constructor's own
  Sage-script derivation of $(N,K)$ being correct; the paper reports one
  bug it caught this way (a Sanov-subgroup index error) but that check is
  internal to the same construction pipeline, not an external audit.
- The design assumes a solver with no access to construction-time
  metadata; it does not test abstention under partial information leakage.

## Related

[[abstention]] · [[solve-verify-detection-gap]] · [[value-of-information]] · Commitment

[^c1]: rivin-2026 — "the answer is computable in O(1) closed form by anyone with construction-time data (N, K), but the solver, without that data, faces either heuristic structural detection or an algorithmic question of unknown decidability."
[^c2]: rivin-2026 — "commit-correct: model commits to a specific answer matching ground truth."
[^c3]: rivin-2026 — "On the index variant, the kernel/cokernel asymmetry creates a calibrated abstention test: a model that can compute the cokernel but not the kernel-side membership should abstain rather than commit to the cokernel-side upper bound."
[^c4]: rivin-2026 — "The prompt design is therefore not neutral: it is a load-bearing element of the benchmark."
