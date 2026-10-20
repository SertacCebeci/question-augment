---
description: "In multi-hop RAG, garbled entities in a spoken question hurt most the pipelines with entity-graph linking and iterative reformulation, which are best on clean text; surface fixes recover little."
aliases: ["ASR error amplification in multi-hop RAG", "better retrieval worse robustness"]
sources: ["doi-10-48550-arxiv-2608-22872"]
---
# Structural amplification of query-entity corruption

A question that reaches a retrieval pipeline through speech recognition arrives with errors the pipeline cannot see. The work compares four configurations on three multi-hop QA sets (HotpotQA, 2WikiMultiHopQA, MuSiQue) using synthesized speech in four accents: plain dense retrieval, entity-graph linking (HippoRAG2), iterative reformulation (IRCoT), and both combined. Amplification is defined as a larger F1 gap between clean text and transcribed input within the same method, not lower absolute F1.[^c1]

## What was measured

The strongest configuration on clean text loses the most. The combined method has the highest clean F1 on all three sets, yet its clean-to-noisy gap is 36.5%, 42.3% and 67.4% larger than plain retrieval's.[^c2] Higher absolute accuracy and a wider gap can coexist: on Nigerian-accented 2Wiki the combined method has the biggest gap but also the best noisy F1 (0.450 vs. 0.331).[^c3] Each extension alone widens the gap too, and the combined effect is significant on all three benchmarks.[^c4]

The mechanism is corruption of named entities in the question. Entity corruption is the largest error category for every accent (87%-94% of degraded cases on 2Wiki), and it stays dominant for all four configurations, not just plain retrieval.[^c5] Multi-hop questions chain several named entities by design, which is why the effect is strongest on 2Wiki.[^c6]

Why structure amplifies: a reformulation step can anchor on the corrupted entity and discard the uncorrupted fragment that the base retriever still used. In the case study, the combined method "abandons the remaining Vijay signal used by the base retriever" and answers wrongly, and even a one-letter change broke both iterative variants while the base retrievers stayed intact.[^c7] More iteration is not monotone: one round does not amplify, the gap peaks at three steps, and later narrowing for the graph method reflects clean-side degradation, not recovery.[^c8]

Surface repairs help little. Pooling n-best hypotheses closed essentially none of the gap (recovery from -2.2% to +2.5%); phonetic entity correction recovered +4.4% to +11.1%, and neither exceeded 12% in any configuration.[^c9] The n-best result implies the error is systematic in the recognizer, not sampling noise.[^c10]

## Reading for asking and answering

My inference, not tested as an intervention: an asker (or an upstream transcriber) who cannot verify the entities in a question should expect deeper, more structured answerers to be more brittle to them, and a check on entity identity before the first retrieval hop would matter more than extra hops.

## Limits

- Speech is synthesized (TTS) and recognition is mostly one model; a real-speech check shows the error pattern holds but is not end-to-end evaluation on real spoken multi-hop questions.[^c11]
- Error categories are rule-based proxies (capitalized spans as entities), and labels overlap.
- Mitigations were run only on the single worst cell (2Wiki, Nigerian accent) and were described as diagnostic probes.
- The reading-for-asking paragraph is my inference and was not tested.

## Related

- [[hop-depth-difficulty-with-entropy-check]] — hop depth as a difficulty axis; here depth also multiplies exposure to upstream noise
- [[intermediate-query-quality-credit]] — quality of reformulated intermediate queries, the step where corruption gets locked in
- [[agentic-asr]] — recognition that could repair the entity before retrieval
- [[clarification-request]] — asking back about an unreliable entity as the alternative to proceeding

[^c1]: doi-10-48550-arxiv-2608-22872 — "We distinguish robustness from absolute performance: amplification denotes a larger F1 gap between clean text and ASR input within the same method, not lower absolute F1 under ASR noise."
[^c2]: doi-10-48550-arxiv-2608-22872 — "The configuration that performs best on clean input shows the largest drop under ASR noise."
[^c3]: doi-10-48550-arxiv-2608-22872 — "Structural complexity can therefore raise absolute accuracy and widen the gap at the same time."
[^c4]: doi-10-48550-arxiv-2608-22872 — "The combined IRCoT+HippoRAG2 amplification is statistically significant on all three benchmarks (p ≤ 0.007)."
[^c5]: doi-10-48550-arxiv-2608-22872 — "Entity corruption is the dominant category for every accent (87%–94% of cases)"
[^c6]: doi-10-48550-arxiv-2608-22872 — "The effect is strongest on 2WikiMultiHopQA, where bridge and comparison questions chain multiple named entities by design."
[^c7]: doi-10-48550-arxiv-2608-22872 — "Even the mild US corruption (a single-letter change, Patal → Patil) breaks both IRCoT variants while the base retrievers stay intact."
[^c8]: doi-10-48550-arxiv-2608-22872 — "A single iterative round therefore does not amplify the error."
[^c9]: doi-10-48550-arxiv-2608-22872 — "Neither mitigation closes more than 12% of the gap in any configuration."
[^c10]: doi-10-48550-arxiv-2608-22872 — "pooling hypotheses across five decoding temperatures yields the same entity corruption"
[^c11]: doi-10-48550-arxiv-2608-22872 — "Neither constitutes end-to-end evaluation on real spoken multi-hop questions"
