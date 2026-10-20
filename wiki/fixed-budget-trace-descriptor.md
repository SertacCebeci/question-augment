---
description: "A verifier that reads whole generation traces can cost the same at any length if hidden states and attention maps are pooled into fixed-size descriptors before the learned head."
aliases: ["fixed-budget compression", "length-invariant trace descriptor", "fixed-size projection of a generation trace"]
sources: ["arxiv-2512-20578"]
---
# Fixed-budget trace descriptor

A generation leaves a trace that grows with the answer. The hidden state at every position gives a matrix of S rows, and each layer-and-head attention map gives an S×S array. A learned reader that takes the raw trace therefore costs more as the response gets longer. A reward model that reads the text pays the same penalty, because it must process the response again.

The Gnosis paper removes that dependence with a projection in front of the learned head. The projection is described as "a projection operator Π that maps variable-length" traces to fixed-size tensors.[^c1] For hidden states, the sequence is "interpolated and adaptively pooled along" the sequence dimension to a fixed budget of rows, and the paper gives 192 as an example budget.[^c2] For attention, each map is pooled to a fixed k×k grid, with k = 256 as the example.[^c3] Everything downstream then has fixed dimensions, and the head's input does not change shape with S. The paper's own sentence on the consequence is that the backbone's internal traces are read "at a fixed budget independent of sequence length."[^c4]

The mechanism is simple, and its effect is a measured one. In the Math-Reasoning latency comparison, the Gnosis head stays at about 25 ms whether the response budget is 12k or 24k tokens. A reward model that reads the text takes 930 ms and 2465 ms at those two lengths.[^c5] The paper's gloss is that Gnosis "maintains near-constant" latency.[^c6] The reported AUROC at the two lengths is about 0.95 and 0.94, so the cost stays flat while accuracy holds.[^c5]

What survives the transfer is the idea of a fixed-size summary of a variable-size object. Any trace with a length that grows with use, such as a retrieval loop, an agent's tool log, or a long reasoning chain, could be pooled the same way before a check reads it. Whether a given trace carries the signal after pooling is a separate question. My inference: the constant cost is a property of the descriptor, not of the backbone, which still pays for every token it generates.

## Limits

- The constant-cost claim is shown against one reward model at two response lengths, on one stated setup. The text gives latency for those two points only.
- Pooling is lossy by construction. The paper reports that its appendix examines "map downsampling" and pooling strategy, and says these affect performance, but the appendix tables are not in the text I read.[^c7]
- A fixed budget fixes the cost of the check, not the cost of generating the trace it checks. Only the verifier is constant in S.
- The descriptor gives one correctness score for a whole response. It does not say which token or step caused a failure. My inference from the design: the paper reports no localisation.
- The fixed budget was chosen on the benchmarks reported, so the particular sizes (192, 256) are not tested as a general rule.

## Related

- [[attention-map-correctness-descriptor]] — the attention side of the same projection, where each map becomes a grid and then a statistics or CNN summary.
- [[prefix-correctness-readout]] — a fixed-size descriptor is what lets one head read a partial trace of any length.
- [[pre-generation-success-probe]] — reads one state before any answer is written, the opposite end of the trace: one position, no pooling.
- [[trajectory-geometry-uncertainty-probe]] — also reads a trajectory of states, but across the layers of one token rather than across positions of a generation.

[^c1]: arxiv-2512-20578 — "a projection operator Π that maps variable-length"
[^c2]: arxiv-2512-20578 — "is interpolated and adaptively pooled along"
[^c3]: arxiv-2512-20578 — "is downsampled via adaptive pooling to"
[^c4]: arxiv-2512-20578 — "at a fixed budget independent of sequence length,"
[^c5]: arxiv-2512-20578
[^c6]: arxiv-2512-20578 — "Gnosis maintains near-constant"
[^c7]: arxiv-2512-20578 — "and map downsampling affect performance"
