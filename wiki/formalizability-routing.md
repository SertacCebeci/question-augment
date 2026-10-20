---
description: "Sort each claim by whether a solver can take its meaning: precise claims go to formal proof, vague ones to soft consensus, so ambiguous language never gets a false formal guarantee."
aliases: ["semantic routing", "verification routing by claim type", "false formalization", "semantic gap routing"]
sources: ["doi-10-48550-arxiv-2601-20055"]
---
# Formalizability routing

Checking an answer formally needs each claim written as a logical formula. Natural language often does not survive that translation: a claim such as "is similar to" has no fixed truth value, and forcing it into a formula produces an assertion that looks checkable and is not. The paper calls the error "false formalization", defined as "the error of forcing ambiguous natural language into rigid logic."[^r1] Its response is to decide, claim by claim and before any solver call, which verifier a claim may use.

The mechanism has three steps. An LLM labels each atomic claim with a semantic type: mathematical, logical, temporal, probabilistic, commonsense or vague. Then a routing function sends the claim to one of three verifiers. Logical, mathematical and temporal claims go to the SMT solver. Commonsense, probabilistic and vague claims go to "an ensemble of LLM judges" whose verdicts are a confidence-weighted vote.[^r2] Claims that the solver cannot handle for non-logical reasons, such as a syntax error or a timeout, fall back to soft checking, so the pipeline does not stall.[^r3] The paper's stated rule is "Apply formal verification where the semantic gap is narrow (mathematical/logical claims), and fall back to consensus-based verification where it is wide (commonsense/vague claims)."[^r4]

The point the authors take from the design is that the two verifiers give different kinds of guarantee, and the score is built to keep them apart. A soft-verified claim is capped below a formally entailed one: entailed scores 1.0, supported 0.9, possible 0.7, contradicted 0.0.[^r5] The weights are described as "an ordinal hierarchy, not a tuned operating point."[^r6]

The router was measured on a small stress set: "N = 54 claims, including adversarial edge cases" such as idioms and vague quantifiers. It reached "of 94%" overall accuracy, and the authors report that "1 out of 32 soft claims was misrouted to SMT."[^r7] The asymmetry is the design goal: a vague claim sent to the solver is the costly error, and a precise claim sent to soft checking only loses strength.

Routing is also measured as an ablation. Removing the solver altogether, so that all claims go to LLM consensus, "results in the most significant performance degradation across the board," with an average drop of 22.8%.[^r8] Forcing the solver onto every claim is also reported to underperform the full routed system.

## Limits

- **The router is itself an LLM.** The type labels come from the same model family the pipeline uses, so routing inherits the generator's errors. The 94% figure comes from one 54-claim set built by the authors.
- **Routing does not make hard domains formal.** On benchmarks like HLE and BBEH the paper reports them as "soft-dominated by necessity," while logic-heavy benchmarks are mostly solver-verified. The formal guarantee therefore covers a subset of claims, which varies by domain.
- **The formal fragment is narrow.** The solver targets QF-UF and LIA. The limitations section says that restricting to these logics "sacrifices expressiveness" and that claims needing universal quantification or non-linear arithmetic "cannot be formally verified and must fall back to" soft checking.[^r9]
- **Overhead on synthetic tasks.** On ProofWriter, a program-synthesis baseline beats the routed system (98.4% against 89.9%), and the authors say the routing and decomposition "introduces unnecessary complexity compared to PoT" on purely synthetic tasks.[^r10]
- **The line between types is not measured as a boundary.** The paper gives no principled criterion for when a claim is "precise enough." It is the labeler's judgement, checked only on the stress set above.

## Related

- minimal-correction-subset — the feedback the solver branch produces; it applies only to claims routed to the solver.
- [[refutation-based-entailment-check]] — the test the solver branch runs: premises plus the negated claim, unsatisfiable means entailed.
- [[atomic-entailment-repair-loop]] — an atom-level check with a ternary label, a close relative of routing without the type split.
- [[neurosymbolic-text-to-logic-retrieval]] — the same translation-to-logic step, used for retrieval rather than answer checking, with the same fragility on open language.
- [[semantic-entropy]] — the paper's consensus step compares sampled formalizations by solver-checked equivalence instead of syntax, which is in spirit a meaning-level agreement check; the link is my inference, not the paper's claim.

[^r1]: doi-10-48550-arxiv-2601-20055 — "the error of forcing ambiguous natural language into rigid logic"
[^r2]: doi-10-48550-arxiv-2601-20055 — "we use an ensemble of LLM"
[^r3]: doi-10-48550-arxiv-2601-20055 — "fail due to non-logical errors (e.g., syntax errors, undeclared variables, or timeouts)"
[^r4]: doi-10-48550-arxiv-2601-20055 — "Apply formal verification where the semantic gap is narrow (mathematical/logical claims)"
[^r5]: doi-10-48550-arxiv-2601-20055 — "soft-verified claims are capped at a lower"
[^r6]: doi-10-48550-arxiv-2601-20055 — "encode an ordinal hierarchy"
[^r7]: doi-10-48550-arxiv-2601-20055 — "1 out of 32 soft claims was misrouted to SMT"
[^r8]: doi-10-48550-arxiv-2601-20055 — "results in the most significant performance degradation across the board"
[^r9]: doi-10-48550-arxiv-2601-20055 — "cannot be formally verified and must fall back to"
[^r10]: doi-10-48550-arxiv-2601-20055 — "introduces unnecessary complexity compared to PoT"
