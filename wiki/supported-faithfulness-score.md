---
description: "A claim-level faithfulness metric that decomposes a reasoning output into atomic claims and scores the mean fraction verifiable against the provided evidence, invariant to the choice of decomposer."
aliases: ["SFS", "Supported Faithfulness Score"]
sources: ["shin-2026"]
---
# Supported Faithfulness Score (SFS)

> Answer accuracy tells you whether the output is right; SFS tells you how
> much of the *reasoning* it took to get there is actually anchored in the
> evidence it was given.

## Definition / Mechanism

SFS scores a reasoning output $O$ in three stages: an LLM [[decomposer-planner-centric-rl|decomposer]] $\phi$
splits $O$ into $N$ atomic claims; each claim's support score $s_i \in
[0,1]$ is the maximum entailment/similarity mass it earns against any
single passage of the evidence set $E$ (no multi-passage corroboration is
required, so a legitimate single-source claim is not penalised); the final
score is the uniform mean $\mathrm{SFS}(O) = \frac{1}{N}\sum_i s_i$. It
extends to round-level faithfulness as $F(t) = \mathrm{SFS}(O^t)$, the
quantity [[reasoning-trap]]'s Theorem 1 bounds along the debate chain.[^c1]

SFS is built to seven design axioms (A1–A7), the two load-bearing ones
being decomposer-invariance of condition-level rankings — different LLM
decomposers reorder individual claim scores but not which experimental
condition ranks above another (Spearman $\rho = 1.0$) — and the fabrication
penalty: a claim unentailed by any evidence passage contributes zero to
the numerator while still counting in the denominator, so adding an
unsupported claim weakly decreases the average score. A further validity
check (A7) shows two reasoning traces reaching the *same final answer* can
receive substantially different SFS ($\Delta > 0.05$ on 70% of paired
examples) — evidence that the score measures the process, not a re-skin of
accuracy.[^c2]

The estimator concentrates at an exponential rate by Hoeffding's inequality:
for $N=300$ trials the tail bound on a $0.10$ SFS gap is below $5\times
10^{-3}$, which the paper uses to certify the three reported condition-level
gaps (0.135, 0.149, 0.343) as statistically resolved at that sample size.[^c3]

## Why it matters

SFS is what makes [[reasoning-trap]] and [[evidence-grounded-socratic-reasoning]]
measurable rather than only theoretical: it is the operational stand-in for
$I(E; O^t)$, the quantity the [[data-processing-inequality|Data Processing Inequality]] bound and the
sub-martingale [[recovery-postulate|recovery]] result are stated about. Any protocol claiming to
preserve or recover evidence-grounded reasoning (not just the final answer)
needs a claim-level, decomposition-based score like this one rather than
an accuracy or agreement number.

## Limits

SFS presumes an explicit, enumerable evidence set $E$ against which claims
can be checked (fact-verification style tasks: SciFact, FEVER); it does
not obviously extend to open-ended reasoning where "the evidence" is not a
fixed passage set. The decomposer-invariance result (A2) is shown as rank
invariance across conditions, not value invariance per claim — individual
$s_i$ scores do shift with the decomposer, only the condition-level
ordering is stable. `shin-2026` is a single-author 2026 arXiv preprint;
the axioms and the reported invariance figure are `[?]` pending independent
verification.

## Related

[[reasoning-trap]] · [[evidence-grounded-socratic-reasoning]] · [[mutual-information]]

[^c1]: shin-2026
[^c2]: shin-2026
[^c3]: shin-2026
