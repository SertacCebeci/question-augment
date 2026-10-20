---
description: "Frozen VLM readers given retrieved passages use evidence at prompt slot 0 far better than the same evidence later; the effect is slot-anchored, not similarity- or image-driven."
aliases: ["lost at the end", "primacy bias in retrieval-augmented QA", "slot-0 privilege"]
sources: ["doi-10-48550-arxiv-2606-16494", "arxiv-2512-14313", "arxiv-2512-13109"]
---
# Reader slot-zero primacy

In knowledge-based VQA, a frozen reader is fed up to 20 retrieved passages. Liu et al. (2026) ask whether the text-LLM "lost in the middle" U-shape holds there. Their gold-position protocol holds everything bit-identical within a question except the prompt slot of the gold passage, so any accuracy difference is attributable to position.[^c1]

## What was measured

**Shape is primacy, not U.** On Qwen2.5-VL-7B reading top-10 InfoSeek passages: 45.2% with gold first, 32.3% middle, 28.6% last (n=496).[^c2] Across three readers and two benchmarks the first-versus-last gap is 16 to 26 points in all six cells; middle and last sit close together, far below first, and a recency rebound is absent on five of six cells.[^c3] The gap does not shrink steadily with reader scale: +14.5 pp at 3B, +16.5 pp at 7B, +10.5 pp at 32B.[^c4]

**It is not introduced by the image.** A text-only control that removes the image and changes nothing else does not shrink the gap.[^c5] Moving the image after the passages leaves the first-versus-last gap at 1.12 times the anchor, so image-token proximity is not the primary driver.[^c6]

**It follows the slot, not retrieval similarity.** Errors shift from "did not use the right passage" to "used a wrong passage instead": distractor-lift errors grow monotonically as gold moves later.[^c7] Because the rank-1 distractor normally sits at slot 0, position and similarity are confounded. In a shuffle ablation, with the least-similar distractor placed at slot 0 the reader picked it 73 times, but picked the most-similar one only 7 times when it sat at slot 8: the reader follows the slot.[^c8] The pattern replicates on E-VQA.

**Later evidence is largely wasted.** In a pre-registered multi-gold test (n=240), a second answer-bearing passage at slot 9 adds a statistically unseparable +2.92 pp when slot 0 already holds gold. One gold at slot 0 beats two golds at slots 4 and 9.[^c9] So "slot 0 is privileged" fits better than "decay toward the end."

**Retrieval-side fixes do not help.** MMR diversification, oracle reranking and rank-based distractor reordering all fail to improve on the deployment default within paired-bootstrap CIs.[^c10] The authors infer that recall@k is the wrong metric for a frozen reader and that reranking should reward rank 1. That inference is theirs and is untested as a training objective.

## Limits

- The underlying mechanism (positional encoding, attention sinks) is left open by the authors; slot-0 anchoring is a localization, not an explanation.
- A candidate for the positional side now sits in the wiki: [[initial-token-saliency]], an attention term tied to the initial token that position scaling does not reach. It is a proposal from a different study of attention in LLMs, not a test on readers; nothing here shows it produces the slot-0 gap.[^c13]
- Only open 7B/8B readers (plus 3B and 32B on one benchmark) and two benchmarks; the 32B attenuation rests on a single cell.
- The multi-gold test uses pseudo-gold chunks, nearly always from the same Wikipedia article. It tests positional privilege under redundant evidence, not multi-hop combination, and E-VQA has no multi-positive questions.[^c11]
- One reader on E-VQA (Qwen3-VL-8B) shows last above middle, so middle-versus-last ordering is reader-specific. Oracle-reranking promotion is underpowered (n=254).
- "Instruction-tuned reader" is part of the claim; base models were not compared as far as I read.
- A text-only generator on a different task gave the opposite end-versus-start order. Iratni et al. put five passages, gold and distractors, into Flan-T5-XL on MuSiQue, and found that "placing relevant passages at the end led to the best performance, while placing them in the middle resulted in the lowest generation quality."[^c12] The gap is small, under two points of exact match by my reading of the table, and I found no significance test for it in the text. So the direction of the position effect is reader- and task-specific, and the slot-zero result is not a general rule.

## Related

- [[rank-zero-misinformation-collapse]] — the same slot-0 anchoring seen in agents: a falsehood at rank 0 captures the answer
- [[mcq-answer-position-bias]] — position effects on answer options rather than evidence passages
- [[rubric-option-position-bias]] — option-order sensitivity in judging
- [[llm-judge-biases]] — position bias as one of several systematic reader/judge biases
- [[initial-token-saliency]] — the attention-side candidate for the positional part of the slot-0 shape

[^c1]: doi-10-48550-arxiv-2606-16494 — "holds everything bitidentical within question except the gold passage’s"
[^c2]: doi-10-48550-arxiv-2606-16494 — "Accuracy drops sharply with gold position: 45.2% at first, 32.3% at middle, 28.6% at last"
[^c3]: doi-10-48550-arxiv-2606-16494 — "No recency rebound appears at k=20 on five of six"
[^c4]: doi-10-48550-arxiv-2606-16494 — "does not shrink steadily with it: +14.5 pp at 3B,"
[^c5]: doi-10-48550-arxiv-2606-16494 — "removing the image and changing nothing else does not"
[^c6]: doi-10-48550-arxiv-2606-16494 — "first-vs-last +18.55 pp, 1.12× the anchor. Proximity is therefore not the primary driver."
[^c7]: doi-10-48550-arxiv-2606-16494 — "Distractor-lift grows monotonically with gold position (30.1 → 53.3 → 56.5%)"
[^c8]: doi-10-48550-arxiv-2606-16494 — "The reader follows the slot,"
[^c9]: doi-10-48550-arxiv-2606-16494 — "beats two at {4, 9} by +9.17 pp [+4.17, +14.58]."
[^c10]: doi-10-48550-arxiv-2606-16494 — "distractor reordering all fail to improve on the deployment default"
[^c11]: doi-10-48550-arxiv-2606-16494 — "supplies pseudo-gold passages rather than curated oracles"
[^c12]: arxiv-2512-14313 — "placing relevant passages at the end led to the best performance, while placing them in the middle resulted in the lowest generation quality"
[^c13]: arxiv-2512-13109 — "However, both approaches overlook sal(i)."
