---
description: "Handing a model a contiguous clip instead of scattered keyframes keeps the order and transitions of the evidence; a video-RAG paper finds clip retrieval ahead of keyframe retrieval on one benchmark."
aliases: ["clip-level retrieval", "video clip RAG", "contiguous evidence span", "clip as knowledge fragment"]
sources: ["arxiv-2512-08410"]
---
# Contiguous clip as evidence unit

A model that cannot take a long video whole has to be handed a part of it, and the unit of that handover is a choice. The common unit is the keyframe: a sample of frames picked for their relevance to the question. The paper argues that a keyframe is the wrong grain for evidence. Uniform sampling "is prone to losing key information,"[^c1] and frame selection that follows the question has the opposite problem: the selected frames "may face challenges in maintaining temporal and content coherence across selected frames."[^c3] The authors prefer a clip because it is a knowledge fragment: "video clips are the better choice as knowledge fragments," carrying "more complete and continual semantics, avoiding potential conflicts between selected frames."[^c2][^c7]

The mechanism named here is continuity of the retrieved unit. A set of keyframes is a sample: its members can come from different scenes, and what happened before what is not in the set. A clip is a span: the frames inside it stay in order and keep their transitions. Retrieval then works over spans whose boundaries sit where the content changes. The paper says its clips are meant to "capture clips that involve content changes related to the instruction,"[^c8] so the unit is shaped by the question rather than fixed in advance. A question that turns on several scene transitions can be served by one span that contains them, where a set of frames would supply the transitions without their order.

The measured effect is an ordering on the paper's own ablation. Uniform sampling is weakest; "Key Frames can obtain more relevant visual information for MLLMs" than uniform sampling;[^c4] and "the last three clip-based settings can further improve the performance on" LongVideoBench, with the query-guided variant "the best among all comparisons."[^c5][^c6] The numbers in the ablation table were not legible in the text I read, so I take the ordering from the prose, not the table.

For an asker or answerer the transferable point is the principle, not the video machinery: when an answer depends on how things unfold, the evidence should be a span that preserves the unfolding, not a sample of its moments. That step from video to text questions is my inference; the paper tests only video QA.

## Limits

- Coherence is argued, not measured. The paper asserts that keyframes break coherence and clips keep it. In the text I read I did not find a measure of coherence itself; the support is downstream accuracy on video QA.
- The clip-versus-keyframe ordering rests on one benchmark in the ablation I read. The full method is validated on several long-video benchmarks, but those results bundle the clip unit with its chunking rule and with an embedding model trained on the authors' own data.[^c9] The clip effect is not isolated from that training in the part I read.
- The keyframe baseline's configuration (frame count, embedding model, token budget) is not given in the text I read, so a fair frame-versus-clip comparison at equal cost is not established.
- Clip length and clip count are not swept in what I read. My inference is that a clip too long reintroduces the dilution a sample avoids, but the paper does not test that boundary.
- Only video is tested. Whether the continuity argument carries to text passages, where chunking is already routine, is not checked here.

## Related

- [[query-adaptive-evidence-granularity]] — the grain of evidence set per question; here the grain is a contiguous span and the claim concerns its continuity rather than its size.
- [[dispersed-evidence-retrieval-collapse]] — evidence scattered over a corpus defeats top-k retrieval; the keyframe problem looks like a small-scale version of the same dispersion inside one video (my inference, not tested by either paper).
- [[decoupled-search-context-chunk-size]] — the search-versus-answer grain choice on text; the text version does not raise the coherence issue the paper raises for sampled frames.

[^c1]: arxiv-2512-08410 — "prone to losing key information"
[^c2]: arxiv-2512-08410 — "video clips are the better choice as knowledge fragments"
[^c3]: arxiv-2512-08410 — "may face challenges in maintaining temporal and content coherence across selected frames"
[^c4]: arxiv-2512-08410 — "Key Frames can obtain more relevant visual information for MLLMs"
[^c5]: arxiv-2512-08410 — "the last three clip-based settings can further improve the performance on"
[^c6]: arxiv-2512-08410 — "our query-guided strategy is the best among all comparisons"
[^c7]: arxiv-2512-08410 — "more complete and continual semantics, avoiding potential conflicts between selected frames"
[^c8]: arxiv-2512-08410 — "capture clips that involve content changes related to the instruction"
[^c9]: arxiv-2512-08410 — "design a progressive training regime for OneClip-RAG"
