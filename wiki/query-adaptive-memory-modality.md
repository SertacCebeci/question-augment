---
description: "A video memory agent chooses per query among episodic, semantic and visual memory; adding memory types helped, and always pairing captions with frames was reported to distract."
aliases: ["adaptive memory-type selection", "per-query memory selection", "adaptive multimodal memory retrieval", "memory-source routing"]
sources: ["doi-10-48550-arxiv-2512-02425"]
---
# Query-adaptive memory modality

A long video can be queried through several stores built from the same footage: a textual episodic memory of captioned events at several time scales, a textual semantic memory of long-term relations and habits, and a visual memory of short segments kept as frames. WorldMM treats the choice among these stores as a decision made for each question. Its retrieval agent "adaptively selects the most relevant source" and formulates a query for it, conditioned on the question and on what earlier steps returned, and it stops once "sufficient information has been gathered".[^c1][^c2]

The motivation is that a fixed mixture is not neutral. The introduction argues that "a fixed strategy that always includes both captions and frames during response generation yields" suboptimal results, because visual context can distract the answerer.[^c3] The paper's ablation varies which memory types are available and reports that accuracy rises as they are added: it "show[s] a consistent improvement in performance as additional memories are incorporated."[^c4] That result is about having more kinds of memory. The choice among them is a separate step, made by the agent.

The choice is not uniform across question types. By category, "HabitInsight and RelationMap depend primarily on semantic memory", while "EntityLog and EventRecall benefit more from visual memory".[^c5][^c6] The authors read this as the model "leveraging the strength of each type in a context-dependent manner."[^c7] The figure is a usage proportion across retrieval iterations, so it shows which store the agent reached for, not whether that store was the right one for each question.

What survives the move away from video, in my reading: the unit being selected is the source, not the item. A question is routed to the store whose form matches what it needs, such as an event timeline, a long-term regularity, or fine perception, and the same loop that routes it also decides when to stop. The general claim I would draw is that the mixture of evidence forms a question draws on is a property of the question, and a fixed mixture is one choice among several. That step is my inference from one system; the paper tests it only inside its own agent.

## Limits

- The evidence is one agent on long-video QA benchmarks. The headline figure, "an average 8.4% performance gain," is aggregate over benchmarks and does not isolate the memory choice.[^c8]
- The ablation varies which memories exist, not how the agent chooses among them. In the sections read, I did not find a run that forces every memory into every answer, so the claim that a fixed caption-plus-frame mixture is worse rests on the introduction's single illustrative figure (Fig. 1c) and not on a measured comparison.
- The extracted text of the ablation table is garbled, so its cell values are not used here; only the direction of the reported trend is.
- The memories are built by preprocessing: "it still requires careful preprocessing, including video captioning, triplet extraction, and semantic consolidation."[^c9] Whether per-query selection still helps when the textual memories are poor is not tested here.
- The selector is a language model prompted as a retrieval agent. Whether a different selector behaves the same is not tested.
- Modality and temporal scale are varied together by the agent, and the per-category result does not separate them.
- Any transfer to a human asker or answerer is my inference. The paper's agent is a machine.

## Related

- [[modality-wise-retrieval]] — routes a query to the index of its own modality to avoid cross-modal mismatch; here the choice is among memory stores over one video, a different decision.
- [[query-adaptive-evidence-granularity]] — the same per-question variable on the grain axis; WorldMM applies it to time scales inside the same loop.
- [[stop-continue-criteria-in-retrieval-loops]] — the loop that picks the next memory also decides when to stop, a stop the paper ties to sufficiency and an iteration cap.
- [[weak-channel-addition-penalty]] — adding a weak image channel can lower accuracy below text-only, the same worry about an extra modality as a distractor, measured elsewhere.
- [[text-modality-dominance]] — which modality an omni-model leans on when modalities conflict; a neighbouring question about modality reliance, not linked by any measurement here.

[^c1]: doi-10-48550-arxiv-2512-02425 — "adaptively selects the most relevant source"
[^c2]: doi-10-48550-arxiv-2512-02425 — "sufficient information has been gathered"
[^c3]: doi-10-48550-arxiv-2512-02425 — "a fixed strategy that always includes both captions and frames during response generation yields"
[^c4]: doi-10-48550-arxiv-2512-02425 — "show a consistent improvement in performance as additional memories are incorporated"
[^c5]: doi-10-48550-arxiv-2512-02425 — "HabitInsight and RelationMap depend primarily on semantic memory"
[^c6]: doi-10-48550-arxiv-2512-02425 — "EntityLog and EventRecall benefit more from visual memory"
[^c7]: doi-10-48550-arxiv-2512-02425 — "the most relevant memory type for each category, leveraging the strength of each type in a context-dependent manner"
[^c8]: doi-10-48550-arxiv-2512-02425 — "an average 8.4% performance gain"
[^c9]: doi-10-48550-arxiv-2512-02425 — "it still requires careful preprocessing, including video captioning, triplet extraction, and semantic consolidation"
