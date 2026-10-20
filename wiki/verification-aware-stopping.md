---
description: "A retrieval-augmented search agent stops when a trained per-hop verifier matches evidence to every expected reasoning-hop claim, not when the generator reports confidence."
aliases: ["HALT", "Hop-Aligned Loop Termination", "verification-aware stopping", "evidence-coverage stopping"]
sources: ["roh-2026"]
---
# Verification-aware stopping (HALT)

> A multi-hop retrieval agent's "ask again?" decision reframed as a coverage
> check: does the evidence gathered so far support every reasoning hop the
> question needs, not whether the generator feels ready to answer.

## Definition / Mechanism

HALT (Hop-Aligned Loop Termination) sits on top of a frozen search agent —
policy, retriever and generator untouched. Given a question $q$, it is
handed expected hop claims $C(q)=(c_1,\dots,c_K)$, one per reasoning step,
either taken from gold supporting-fact annotations (diagnostic) or generated
zero-shot from the question alone (deployable). After each retrieval loop, a
small trained verifier $V_\theta$ labels every claim–sentence pair
MATCH/PARTIAL/NULL; each claim keeps the strongest label seen over all
retrieved sentences so far (running max, MATCH > PARTIAL > NULL). The
default policy, ALL_MATCH, stops only when every expected hop claim is
MATCH; the lenient contrast ANY_MATCH stops when at least one is.
"We frame stopping as evidence coverage rather than generator confidence,
and introduce HALT, a lightweight verification-aware policy that leaves the
search agent unchanged. Given expected hop claims, HALT stops only when
cumulative evidence supports each required claim."[^c1]

The verifier is Qwen2.5-3B-Instruct with a LoRA adapter, trained once on
9,626 HotpotQA claim–sentence rows and reused without retuning across
datasets and agent scales, reaching 0.9304 macro-F1 on a question-disjoint
dev split.[^c2]

## Known as

| Field | Name there | exact / close |
|---|---|---|
| this paper (Roh & Han, 2026) | HALT | exact — the acronym |
| this paper (Roh & Han, 2026) | Hop-Aligned Loop Termination | exact — the acronym's expansion |

## Why it matters

On a Self-Ask 3B agent (BM25 closed-pool retrieval, gold hop claims), HALT
cuts average search loops on all three tested multi-hop QA benchmarks while
largely preserving standardized exact match, [[proactive-expertise-clarification|passing]] non-inferiority (ε=2pp,
paired bootstrap, Holm-corrected) in 5/6 cells of the full gold+generated
family and loop superiority in all six; the headroom exists because the
unmodified agent runs to its search budget on 78–88% of questions instead of
halting on its own.[^c3]

Applying the same 3B-trained verifier to a 7B Self-Ask agent with no
retraining passes both endpoints (Holm m=6) on all three benchmarks, though
savings shrink because the larger agent already stops earlier natively.[^c4]

The same coverage signal also runs the other direction: on the 7B agent,
ALL_MATCH is *not* satisfied at the agent's own native stop loop on 51–79%
of questions across the three benchmarks — under-search at scale. Forcing
continuation on the flagged HotpotQA subset until ALL_MATCH (or budget)
roughly doubles exact match, from 0.162 to 0.323.[^c5]

## Limits

- Primary results are Setting A: a controlled closed BM25 pool built from
  the benchmark's own gold + distractor passages, which by construction
  isolates the stopping decision from retrieval failure. The open-corpus
  pilot (Setting B) shows HALT becomes cautious rather than delivering the
  same savings: "Open-corpus pilots further suggest that HALT abstains
  when coverage cannot be reliably verified."[^c6]
- One of the three gold-claim cells (HotpotQA, 3B) fails EM non-inferiority
  outright (its 95% CI crosses −ε); this note's headline savings hold for
  two of three datasets at gold quality, not all three.
- The verifier is trained once on HotpotQA discrepancy labels; cross-dataset
  and cross-scale transfer is demonstrated only within the same three
  benchmarks and one model family (Qwen2.5 3B/7B), not established as
  general.
- Deployable (generated, not gold) hop claims give smaller savings and are
  themselves imperfect (generated–gold alignment F1 = 0.701 on 2Wiki,
  0.455 on HotpotQA) — the method's ceiling depends on claim-generation
  quality the paper does not solve.

## Related

[[stopping-rules]] · [[self-ask-decomposition]] · [[sprt]] · [[value-of-information]]

[^c1]: roh-2026 — "We frame stopping as evidence coverage rather than generator confidence, and introduce HALT, a lightweight verification-aware policy that leaves the search agent unchanged. Given expected hop claims, HALT stops only when cumulative evidence supports each required claim."
[^c2]: roh-2026 — "The balanced training set contains 9,626 rows from 4,903 questions. We train for 1,000 steps and obtain 0.9304 macro-F1 on a question-disjoint dev split of 2,374 rows. The verifier is trained once on HotpotQA and reused without tuning across Self-Ask backbones (Qwen2.5-3B/7B) and the three benchmark datasets."
[^c3]: roh-2026 — "HALT reduces average search loops on all three datasets while largely preserving Std-Ext EM: two of three gold cells pass EM non-inferiority, and HotpotQA gold fails only because its 95% CI crosses −ε around a small point decrease (∆EM=−0.9 pp). Across the full 3B family, including generated claims, HALT passes EM non-inferiority in 5/6 cells and loop superiority in all six"
[^c4]: roh-2026 — "We apply the same 3B verifier to a 7B Self-Ask agent without retraining. Table 2 shows that all three datasets pass both endpoints under Holm m=6. Loop savings are smaller than at 3B, consistent with the 7B agent already stopping earlier."
[^c5]: roh-2026 — "HALT’s own ALL _ MATCH criterion is never satisfied at the agent’s native stop loop on 51% / 64% / 79% of questions (HotpotQA / 2Wiki / MuSiQue) — direct evidence of under-search at scale"
[^c6]: roh-2026 — "Open-corpus pilots further suggest that HALT abstains when coverage cannot be reliably verified."
