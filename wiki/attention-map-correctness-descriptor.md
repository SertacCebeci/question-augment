---
description: "A frozen LLM's full layer-by-head attention maps, each pooled to a small grid and summarised, carry a correctness signal that is strong on math and MMLU-Pro but weaker on short factual QA."
aliases: ["attention circuit", "attention-map descriptor", "attention routing signal", "attention stream of a self-verifier"]
sources: ["arxiv-2512-20578"]
---
# Attention-map correctness descriptor

A model's attention is ordinarily read as the weight it puts on earlier tokens while it writes the next one. Read over a whole generation, the maps of every layer and head form a second trace next to the hidden states, and the Gnosis paper treats the shape of that trace as evidence about whether the answer is right. Each map is an S×S array, with S the total token count, and the paper reduces it to a fixed size: each map "is downsampled via adaptive pooling to" a k×k grid, so the map's size stops depending on the length of the response.[^c1]

Each pooled map is then summarised by one of two extractors, or by both. One is a small convolutional network that treats the map as an image. The other is a set of interpretable statistics that "summarizes how attention is distributed, where" the attention concentrates and "how local or long-range it is."[^c2] The paper adopts the two together. The summaries are placed on a layer-by-head grid, given learned layer and head embeddings "to preserve depth and head identity," mixed across layers and heads by a light axial encoder, and pooled into one attention descriptor.[^c3]

The signal is not uniform across tasks. The paper reports that on math reasoning and MMLU-Pro the attention stream alone is strong, while on TriviaQA the hidden-state stream dominates and fusion adds little.[^c4] Its reading is that attention "is most useful for long-form reasoning," and that the two streams together are "the most reliable" overall.[^c9][^c10] The two streams feed one gated head that weights them per example, so a single model can lean on attention for reasoning traces and on hidden states for factual recall.[^c6]

The attention side is a different object from the scalar in [[attention-entropy-ambiguity-signature]]. That note reads one dispersion number, the entropy of attention on an ambiguous token of the prompt, before the answer exists. The descriptor here reads the whole pattern across every layer and head of a finished generation, learned against correctness labels. My inference: both take attention diffusion to carry information about the answerer's state, but a scalar summary and a learned read of the full map are different instruments, and the paper does not compare them.

What a reader can take from it is a design, not a ranking of attention statistics. Its extractor choice was made on the same benchmarks it reports, and the text summarises the variants without giving their attention-only numbers.

## Limits

- The attention-only and per-extractor numbers are in appendix tables. The text I read gives only the qualitative ordering: "Appendix Table 5 shows that both streams help."[^c5] I cannot quote an attention-only AUROC from the main text.
- The labels are agreement with a reference answer: the paper labels correctness "by comparing predictions to groundtruth answers."[^c7] A head trained this way learns to predict that agreement on math and trivia questions, not correctness in general.
- The descriptor needs every layer's attention maps at inference. A model that exposes only text is outside the method. This is my inference from the design, not a limit the paper states.
- The paper says Gnosis is "not capable" of acting as a universal judge across models, and gives "unrelated architectures or differing generation styles" as the cases it does not cover.[^c8] Whether an attention descriptor transfers across architectures is not tested.
- All reported results come from one family of Qwen3 backbones plus gpt-oss-20B, with one training mix. The attention stream's advantage on reasoning is a within-setting measurement.

## Related

- [[attention-entropy-ambiguity-signature]] — one attention-entropy scalar on a prompt's ambiguous token, read before generation; this note is the whole map across layers and heads, read after decoding.
- [[single-pass-internal-signal-detector]] — the same family of supervised heads over internal signals, from one forward pass; there the inputs are token entropy and hidden embeddings, and here the attention stream is the added input.
- [[fixed-budget-trace-descriptor]] — the projection that turns each variable-size attention map into a fixed grid before any learned reading.
- [[nonlinear-hidden-state-probe]] — a hidden-state readout; the paper's hidden stream is the closest counterpart, and the attention stream is what it adds.

[^c1]: arxiv-2512-20578 — "is downsampled via adaptive pooling to"
[^c2]: arxiv-2512-20578 — "summarizes how attention is distributed, where"
[^c3]: arxiv-2512-20578 — "to preserve depth and head identity"
[^c4]: arxiv-2512-20578 — "attention-only is strong"
[^c5]: arxiv-2512-20578 — "Appendix Table 5 shows that both streams help"
[^c6]: arxiv-2512-20578 — "This head lets Gnosis adaptively weight hidden versus attention features on"
[^c7]: arxiv-2512-20578 — "correctness by comparing predictions to groundtruth answers"
[^c8]: arxiv-2512-20578 — "of acting as a universal zero-shot judge for every"
[^c9]: arxiv-2512-20578 — "is most useful for long-form reasoning"
[^c10]: arxiv-2512-20578 — "combining both is the most reliable"
