---
description: "In URAG, adding irrelevant documents to retrieval hurts accuracy and raises conformal set size only where the LLM's own knowledge is weak; tasks it already handles are unaffected."
aliases: ["retrieval noise sensitivity depends on parametric knowledge", "irrelevant-context degradation"]
sources: ["arxiv-2603-19281", "arxiv-2512-14313", "arxiv-2512-01183"]
---
# Parametric knowledge gates retrieval-noise damage

URAG (Nguyen et al., 2026) turns open-ended RAG tasks into multiple-choice questions and measures uncertainty as the size of a conformal prediction set (larger set, more uncertainty) beside accuracy. Across RAG methods, higher accuracy usually goes with a smaller set: the paper reports a correlation of r = -0.76 over ten datasets.[^c1]

## The noise probe

To simulate noisy retrieval, the authors randomly draw 10 irrelevant documents from the database and add them to the 10 retrieved ones on every retrieval call. They test three subsets: ODEX, LCA and DialFact.[^c2]

The effect depends on the task. Where the base LLM already does well (ODEX), noise changes little. On LCA and DialFact accuracy and certainty both drop sharply for most RAG methods.[^c3] The authors state it as a rule: RAG becomes less sensitive to irrelevant context when the model already has strong parametric knowledge.[^c4] The same pattern appears in the abstract: the accuracy-uncertainty link "breaks under retrieval noise".

So the accuracy-uncertainty relationship is not a property of the retriever alone. It is a property of how much the answerer can fall back on itself when the evidence it is handed is useless. For someone answering from supplied context, the practical reading is that extra, unfiltered evidence is harmless when the answerer is already competent. It is costly when the answerer is leaning on that evidence. (This reading is mine, not tested directly by the paper.)

## Limits

- Noise is one kind only: random, topic-unrelated documents, at a fixed 1:1 ratio. Misleading or contradictory but on-topic evidence is a different condition, and the paper's introductory example of it (coffee in pregnancy) is an illustration, not a measurement.
- Three subsets, a single noise level, and an 8B main model; a smaller-model replication is in the appendix but I did not read it.
- "Parametric knowledge is strong" is inferred from base-LLM task performance, not isolated per question here; the paper's separate LLM-correct versus LLM-incorrect split is a different probe.
- Set size depends on the multiple-choice reformulation and its generated distractors, so absolute uncertainty values may not carry to open-ended answering.
- Causal direction is not established: the paper shows co-occurrence of weak base performance and noise damage across tasks, not an intervention on the model's knowledge.
- A second axis is measured elsewhere. Iratni et al. add distractors to the gold passages of MuSiQue questions and find the damage depends on how many hops the question needs: "This is specifically true in the case of 2-hop questions, where a single distractor dropped the performance by more than 26%."[^c5] That dependence is on the question's structure, not on what the model knows. The paper does not measure parametric knowledge, so it neither confirms nor refutes the gate; the two effects may both hold.

## Related

- [[conformal-set-size-calibration-tradeoff]] — what set size does and does not say about honest uncertainty
- [[contextual-inertia]] — another way supplied context overrides what the model would answer alone
- [[confidently-wrong-low-entropy-regime]] — confident errors, which URAG says retrieval can amplify
- [[calibration]] — the property whose loss under noise is at issue
- [[decoupled-support-contradiction-retrieval]] — retrieval design for conflicting evidence
- [[temperature-perturbation-interaction]] — the sampling temperature is a second condition under which the same corrupted context does more or less damage; there the damage grows with temperature[^c6]

[^c1]: arxiv-2603-19281 — "A strong negative correlation"
[^c2]: arxiv-2603-19281 — "randomly collecting 10 irrelevant documents from the"
[^c3]: arxiv-2603-19281 — "will not be affected by noisy information. However, LCA"
[^c4]: arxiv-2603-19281 — "already possesses strong parametric knowledge."
[^c5]: arxiv-2512-14313 — "This is specifically true in the case of 2-hop questions, where a single distractor dropped the performance by more than 26%"
[^c6]: arxiv-2512-01183 — "temperature acts as a performance degradation amplifier"
