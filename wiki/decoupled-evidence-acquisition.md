---
description: "A search agent is trained only to gather evidence, and a separate, swappable answer generator reasons over what it hands over, so acquisition is judged apart from derivation."
aliases: ["decoupled MRAG", "modular information-seeking agent", "searcher-generator decoupling", "acquisition-derivation split"]
sources: ["doi-10-48550-arxiv-2601-09278"]
---
# Decoupled evidence acquisition

A search agent can be built in two parts: one model decides what to search, which tool to call and when to stop, and another model writes the answer from the evidence the first one gathered. The M3 Searcher paper builds this split as its central design, and states it as the point of the work: the agent "explicitly decouples information acquisition from answer derivation."[^c1] In the rollout definition, "Under the decoupled agentic design, the final tool"[^c2] call goes to an answer expert, and that tool response is the final answer. The searcher's job ends at the hand-off; what it is responsible for is the evidence and the decision about when to stop.

The motivation is about where reasoning capacity lives. Training a model to internalise tool-use policies "comes at the expense of general reasoning capacity."[^c3] The paper's reading of the existing options is that large multimodal models reason well but are not optimised for web integration, while smaller models tuned for web search show a "degradation in general reasoning, limiting their"[^c4] use as a backbone. The split keeps the reasoning backbone out of the search-oriented training: the searcher is a small trainable model, and the generator is a large model that is not trained for search. The authors say the split "preserves the reasoning fidelity of the large-scale"[^c5] backbone while the searcher is optimised for information seeking.

Two consequences follow in the paper. The generator is swappable: the split "simultaneously removes modality constraints, enabling the"[^c6] use of modality-agnostic generators. In the transfer runs, "multimodal and purely textual backbones can reliably synthesize accurate answers," and "Notably, DeepSeek-R1 answer generator emerges as the top performer."[^c7][^c8] The searcher is also insulated from the search engine; the paper describes it as "exhibiting no degradation when switching search"[^c9] tools.

The mechanism is a claim about attribution. Once acquisition and derivation are separate objects, a wrong answer can be traced to one side: missing evidence, or a generator that did not use the evidence it had. My inference is that this is why the searcher can be trained against evidence rather than the final answer (see reference-hop-coverage-reward); the paper does not frame it as an attribution argument.

## Limits

- Decoupling alone is not shown to help. The paper's own comparison says that "explicit, hand-crafted prompt engineering provides a competitive advantage that decoupled, untrained agents fail to surpass."[^c10] The reported gains come from the trained searcher, not from the split by itself.
- The "specialization-generalization trade-off" is cited to other work (Kalajdzievski, 2024; Li et al., 2024a) as motivation. The paper's own evidence for it is one baseline: MMSearch-R1 "performs competitively on Infoseek, but its performance drops sharply on out-ofdistribution tasks."[^c11] That is an observation about one system, not a measured trade-off curve.
- The transfer experiments test whether a trained searcher works with other generators on the same evidence. They do not test whether evidence sufficient for one generator is sufficient for another. The DAC work argues that sufficiency depends on the generator ([[dac-cross-agent-abstention-reward]]); this paper does not address that.
- The ablation says that "each component provides a measurable performance gain"[^c12], but the magnitudes sit in a figure whose numbers are not in the text I read.
- Cost is not reported in the parts I read: a large generator is called once per query, and the number of search turns grows with the retrieval reward, but the text gives no latency or token figures for the two-model setup.

## Related

- [[dac-cross-agent-abstention-reward]] — the opposite coupling: searcher and generator are trained with cross rewards, so the generator's abstention is the searcher's signal. Here the searcher is rewarded for evidence and the generator is not in the loop.
- reference-hop-coverage-reward — the term that trains the searcher in this design, scored on the evidence it gathers.
- [[evidence-forgetting-rate]] — the measure that separates retrieval failure from generator failure in a finished system; the split above makes the same separation by construction.
- [[evidence-grounded-step-reward]] — puts a grounding check inside the search loop, a different place to attach a process signal.

[^c1]: doi-10-48550-arxiv-2601-09278 — "explicitly decouples information acquisition from answer derivation"
[^c2]: doi-10-48550-arxiv-2601-09278 — "Under the decoupled agentic design, the final tool"
[^c3]: doi-10-48550-arxiv-2601-09278 — "Training models to internalize multimodal tool-use policies comes at the expense of"
[^c4]: doi-10-48550-arxiv-2601-09278 — "degradation in general reasoning, limiting their"
[^c5]: doi-10-48550-arxiv-2601-09278 — "it preserves the reasoning fidelity of the large-scale"
[^c6]: doi-10-48550-arxiv-2601-09278 — "and simultaneously removes modality constraints, enabling the"
[^c7]: doi-10-48550-arxiv-2601-09278 — "multimodal and purely textual backbones can reliably synthesize accurate answers"
[^c8]: doi-10-48550-arxiv-2601-09278 — "Notably, DeepSeek-R1 answer generator emerges as the top performer"
[^c9]: doi-10-48550-arxiv-2601-09278 — "exhibiting no degradation when switching search"
[^c10]: doi-10-48550-arxiv-2601-09278 — "explicit, hand-crafted prompt engineering provides a competitive advantage that decoupled, untrained agents fail to surpass"
[^c11]: doi-10-48550-arxiv-2601-09278 — "MMSearch-R1 performs competitively on Infoseek, but its performance drops sharply on out-ofdistribution tasks"
[^c12]: doi-10-48550-arxiv-2601-09278 — "each component provides a measurable performance gain"
