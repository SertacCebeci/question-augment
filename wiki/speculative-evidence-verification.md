---
description: "A small draft model samples frames inside regions a large target model points to, and the target verifies them and decides whether to loop again until convergence."
aliases: ["speculative temporal reasoning", "draft-verify evidence selection", "reasoning-level speculative decoding"]
sources: ["arxiv-2512-00805"]
---
# Speculative evidence verification

When the input is too long to attend to at once, one way to split the work is by capacity. A small draft model does the costly local search: it samples densely inside a region that a larger target model has named, and returns a few salient items. The target does not search. It checks the draft's proposal against its own reasoning, then either stops or asks for another draft over a new region. The clearest case is the long-video paper SpecTemp, where the target is a 7B model and the draft a 3B one. The target keeps "temporal reasoning and verification of the draft", and the draft does the frame selection.[^c1] The loop is the point of the design: the target "decides whether sufficient information has been gathered, or iteratively triggers another round of draft speculation and verification until convergence."[^c2]

Concretely, the target first reads uniformly sampled frames and predicts a temporal clue. Dense frames are then taken "from the attentive regions predicted by the target MLLM", and the draft returns a compact set "selected by the lightweight draft MLLM as the most informative subset."[^c3][^c4] An iteration cap, Tmax, bounds the loop.[^c5] The paper's stated reason for the split is that the draft gives "dense perception with minimal computational cost, while" the target carries the high-level reasoning and checking.[^c6]

What the paper measured. On LongVideoBench, the dual setup reached 57.5% accuracy against 54.1% for the 7B target alone, and ran at 2.3 s per sample against about 3.1 s for the 7B alone (the table's numbers).[^c7][^c8][^c9] The 3B model alone was fast but reached 40.3%.[^c19] The latency gain is credited to "offloading dense exploration to the 3B draft model".[^c9] A trained draft also beat heuristic selectors on frame choice: the paper says "training a specialized draft model is superior to heuristic" methods, with CLIP-based selection as the comparison.[^c10]

What transfers from the source. The idea comes from speculative decoding, where "a smaller draft model to rapidly generate multiple tokens" is "verified in parallel by the target" LLM.[^c11] The paper's own wording for its version is "semantic-level approximation and verification between models of different capacities."[^c12] So what carries over is the propose, verify and stop asymmetry. What does not carry over is the token-level acceptance test: the object proposed is a set of frames, and the check is a judgement by reasoning, not a comparison of token probabilities. The result is approximate. I am inferring that no lossless guarantee applies here; the paper does not claim one.

## Limits

- One model pair and one capacity ratio. The parts I read compare a 7B target with a 3B draft only. Whether another ratio, or a draft of the same size, gives the same pattern is not shown.
- The efficiency figure is a ratio the paper defines, "Efficiency = Accuracy / Latency",[^c13] measured "under identical hardware configurations" at batch size 1.[^c14] A ratio can move because of either term, and one hardware setup does not show how the gain varies across systems. The paper's headline speedup, "19-23% on long-form videos",[^c15] is a separate summary of the same comparison.
- Where the time goes. The paper finds that "LLM prefill dominates total inference time".[^c16] The parts I read say the draft saves time by offloading dense exploration, but do not show how that reduces the target's prefill cost. I did not read the latency breakdown in full.
- The stopping rule. The parts I read define the loop's end by convergence with the Tmax cap. I did not find the convergence test itself, and I did not read the Tmax ablation in full, so how often the cap binds is not established here.
- Scope. The experiments are video question answering with the question fixed in advance. Whether the draft's proposals change when the question is phrased differently is not tested. My inference is that the proposals depend on the question, since the target names the region from it, but the paper does not measure this.
- The motivation rests on one example and one distribution: an attention map from a single four-frame input, and a long-tailed attention histogram.[^c17] This supports the redundancy premise, not the claim that the draft's chosen frames are the right ones.

## Related

- [[decoupled-evidence-acquisition]] — the same split of acquiring evidence from deriving the answer; there the searcher acts once and a fixed generator answers, while here the large model re-enters the loop and decides when to stop.
- [[learned-model-coordinator]] — also a loop that stops when a verifier accepts, over a pool of models; it routes whole turns by a learned policy, whereas here the roles are fixed by size and what is proposed is evidence.
- [[test-time-scaling]] — the paper presents its scheme as "a hierarchical test-time scaling framework"[^c18], which places the loop inside inference-time compute.

[^c1]: arxiv-2512-00805 — "while reserving the target MLLM for temporal reasoning and verification of the draft"
[^c2]: arxiv-2512-00805 — "whether sufficient information has been gathered, or iteratively triggers another round of draft speculation and verification until convergence"
[^c3]: arxiv-2512-00805 — "from the attentive regions predicted by the target MLLM"
[^c4]: arxiv-2512-00805 — "selected by the lightweight draft MLLM as the most informative subset"
[^c5]: arxiv-2512-00805 — "Tmax denotes the maximum iteration number"
[^c6]: arxiv-2512-00805 — "dense perception with minimal computational cost, while"
[^c7]: arxiv-2512-00805 — "Large-only achieves high accuracy (54.1%) but suffers from substantial latency"
[^c8]: arxiv-2512-00805 — "accuracy (57.5%) and the best efficiency score (25.0)"
[^c9]: arxiv-2512-00805 — "SpecTemp achieves the lowest latency (2.3s) by offloading dense exploration to the 3B draft model"
[^c10]: arxiv-2512-00805 — "training a specialized draft model is superior to heuristic"
[^c11]: arxiv-2512-00805 — "employing a smaller draft model to rapidly generate multiple tokens that are then verified in parallel by the target"
[^c12]: arxiv-2512-00805 — "enabling semantic-level approximation and verification between models of different capacities"
[^c13]: arxiv-2512-00805 — "Efficiency = Accuracy / Latency"
[^c14]: arxiv-2512-00805 — "measure average inference latency per sample under identical hardware configurations"
[^c15]: arxiv-2512-00805 — "accelerating inference by 19-23% on long-form videos"
[^c16]: arxiv-2512-00805 — "LLM prefill dominates total inference time"
[^c17]: arxiv-2512-00805 — "observe a clear long-tailed distribution, where"
[^c18]: arxiv-2512-00805 — "a hierarchical test-time scaling framework that integrates"
[^c19]: arxiv-2512-00805 — "Small-only is fast but shows significantly degraded accuracy (40.3%)"
