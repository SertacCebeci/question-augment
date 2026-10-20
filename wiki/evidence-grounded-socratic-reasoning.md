---
description: "A three-role protocol (Debater, Questioner, Checker) that asks Socratic sub-questions and re-checks each against external evidence every round, recovering faithfulness a closed debate loop erodes."
aliases: ["EGSR", "Evidence-Grounded Socratic Reasoning", "Hypothesis-Free Socratic Verification", "HFSV"]
sources: ["shin-2026"]
---
# Evidence-Grounded Socratic Reasoning (EGSR)

> Replace "agents arguing to win" with "agents asking to check": every round
> re-consults the evidence instead of only each other's prior output, and a
> round only survives if its claims can be re-verified against it.

## Definition / Mechanism

EGSR is an asymmetric three-role loop, unlike symmetric multi-agent debate:
the **Debater** produces an initial reasoning trace $O^0$ from the claim
$c$ and evidence $E$; each round, the **Questioner** generates
evidence-grounded sub-questions targeting claims in $O^{t-1}$ that look
underspecified, weakly grounded or unsupported, cycling through six
predefined question types (clarification, assumption-probing,
evidence-demanding, counter-example-seeking, implication-exploring,
meta-evaluation); the Debater answers each sub-question; the **Checker**
verifies each sub-answer against $E$ via NLI (Hypothesis-Free [[staged-socratic-hint-policy|Socratic]]
Verification — answering using only the retrieved passages, without access
to the original claim text or prior reasoning) and gates progression: the
round terminates once the minimum per-question verification score clears a
threshold $\tau$, or after up to $K=3$ iterations. Convergence is declared
on 2-of-3 criteria (evidence-[[sufficient-statistic|sufficiency]] score $\ge 0.75$, a stable
verdict, confidence gap $>0.20$); 90% of evaluations converge in a single
iteration.[^c1]

Because the Checker re-accesses $E$ every round rather than conditioning
only on prior agent outputs, $O^{t+1}$ is built by composing $O^t$ with
verified Checker output — this is what breaks the closed Markov chain of
[[reasoning-trap]]: the update satisfies the paper's open-system [[recovery-postulate|recovery]]
condition (its Theorem 2, applied via Lemma 2), making round-level
faithfulness $F(t)$ a sub-martingale — each round preserves or strictly
increases evidence-grounded mass rather than only ever losing it.[^c2]

Measured against the same 16-condition SciFact/FEVER evaluation as the
Debate Trap, EGSR recovers Supported Faithfulness Score
([[supported-faithfulness-score]]) to within 2% of the no-debate baseline
(98% recovery), at per-claim API cost the paper reports as comparable to
standard debate.[^c3]

## Why it matters

EGSR is a named, formally-motivated instance of *inquiry replacing
argument* inside a multi-agent loop: the questions it asks are not free —
each one must reference a specific evidence passage, and the round only
advances once an external check passes. For a wiki about asking, it is a
concrete answer to "how does an agent avoid asking (or answering) itself in
a circle": gate every step on external re-verification rather than on
consensus among copies of the same model.

## Transfer

| | |
|---|---|
| **Home field** | information theory / martingale theory — sub-martingales and Doob's optional-stopping theorem |
| **Here** | a bounded, gated sequence of Socratic sub-questions, each required to touch external evidence before the round is accepted |
| **What survives** | the qualitative guarantee that, as long as each round's auxiliary information genuinely carries new evidence about $E$, expected faithfulness cannot decrease (Theorem 2 of `shin-2026`) |
| **What does not** | the paper frames its stopping rule as an optional-stopping *interpretation*, not a proof that the deployment-time gate threshold $\tau$ is itself optimal for any domain; the six question types and the $K=3$ round cap are engineering choices validated on SciFact/FEVER, not derived from the martingale property |

## Limits

The 98%-recovery figure is measured on the same two fact-verification
datasets (SciFact, FEVER) as [[reasoning-trap]], with one faithfulness
metric family; it is not shown to transfer to open-ended reasoning tasks
without a checkable evidence set, and the "evidence" $E$ the Checker
verifies against is exactly the same evidence given to the Debater — EGSR
adds no new evidence to the world, it only re-spends the evidence already
provided, more thoroughly and more often. `shin-2026` is a single-author
2026 arXiv preprint; this note's numbers are `[?]` pending independent
verification.

## Related

[[reasoning-trap]] · [[supported-faithfulness-score]] · [[data-processing-inequality]] · [[mutual-information]]

[^c1]: shin-2026
[^c2]: shin-2026 — "the Checker re-references E at each round rather than conditioning only on prior agent outputs. This violates condition (ii) of Theorem 1 (“E provided once at t = 0, no re-injection”), and the chain E → O0 → O1 → · · · is no longer Markov in the sense the DPI bound requires. By Lemma 2, the running-aggregate update structure satisfies the information-accumulating property of Theorem 2, making F (t) a sub-martingale for the protocol"
[^c3]: shin-2026 — "Evidence-Grounded Socratic Reasoning (EGSR): a protocol that replaces adversarial argumentation with structured Socratic inquiry against external evidence; recovers SFS to within 2% of the no-debate baseline (98% recovery)."
