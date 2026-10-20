---
description: "Answering from a rich source floods the context window, while compressing it to text is cheap but drops the visual detail the question needs; the two failures are measured separately."
aliases: ["perception-context trade-off", "context explosion versus textual proxy", "raw-input versus summary trade-off"]
sources: ["arxiv-2512-23044", "arxiv-2512-20618"]
---
# Perception-context trade-off

When the evidence for an answer is a video, a page of images, or any rich
stream, an answerer has two cheap-looking options and both fail. It can feed
the raw source to the model, which keeps the detail but fills the context.
Or it can compress the source to text first, which keeps the context small
but throws away what only the raw signal carries. The paper states the
trade-off as a problem for agents: direct visual inference "maximizes
perception but incurs prohibitive context costs," while text-centric
summarisation "optimizes efficiency but often misses critical visual details
required for accurate grounding."[^c1][^c15]

The two failures were measured against each other on the same benchmark, with
GPT-5.1 as backbone. Direct visual inference reached 19.05% accuracy, and its
context was 76,955 tokens against a total of 78,229.[^c2] The paper reads
that as "This confirms the context explosion bottleneck: the agent is forced
to watch every frame," which leaves little room for further reasoning.[^c3]

Summarisation removed the context problem and not the accuracy one. It
reduced the context to 919 tokens, but its total still came to 75,728 tokens,
because the model had to process the full video to write the summary.[^c4]
Its accuracy was 18.57%, close to direct inference's 19.05% and with a higher
calibration error. The paper's heading for this result is "Lossy
Compression," and it reports that accuracy drops to 18.57%.[^c5]

The qualitative case makes the same point at the level of one question. Asked
the colour of a pen that appears in a film, the direct method answered that
the colour "cannot be determined from the provided videos."[^c6] The summary
answered that the colour "is not specified in the provided videos."[^c11] The
sampled-frame method found the red-capped pen in the early close-ups and
answered "Answer: Red."[^c12]

## The modality gap, in this sense

The paper uses "modality gap" for a narrower thing than the embedding-space
gap of multimodal retrieval. Here it means that a text proxy of a video is
not equivalent to the video. A transcript-only run, with no visual input,
scored 7.14%, against 12.86% for the full system.[^c7] The authors call the
44% relative drop "definitive empirical evidence of the modality gap."[^c13]

A second observation makes the same point from the search side. Search
agents with web access did well on explicit retrieval but "performance
collapses in Level 2 and Level 3 tasks."[^c8] The authors read this as search
agents being able to "locate metadata" without being able to verify the
visual details.[^c14]

## What the trade-off is not

The trade-off concerns what the answerer can see, not how much it can read. A
text source is already the compact form, so the context explosion has no
direct analogue there. The paper's own statement is that text proxies fail to
capture the visual detail of a video.[^c9] Whether the same trade-off governs
other rich sources is my inference, not the paper's, and it needs a test on
each source type before it is assumed.

## Limits

- One benchmark of 210 questions, with two backbones: GPT-5.1 for the main
  comparison and Qwen3 for the rest. With Qwen3 the direct-inference row
  reached 13.81%, and the summary row 9.52%, so the ordering of the paradigms
  is clearer for GPT-5.1 than for the other model.[^c10]
- Absolute accuracies are low, between about 10% and 26%. The trade-off is
  shown among systems that all fail most questions, so it says how the
  failures differ, not how an answerer succeeds.
- The summary baseline is one way to compress. A summary written with the
  question in mind, or a learned compression, is not tested here. The claim is
  about this summariser, not about every text proxy.
- The token counts for summarisation include the cost of processing the full
  video. An answerer who already holds a transcript would pay less, and that
  case is not measured.
- The summary tested above is not written with the question in mind, and a
  text channel that is written for the question at hand is a different case.
  LongVideoAgent measures one such channel, though not against raw frames. Its
  master agent reads subtitles and the text a vision agent returns for a query
  the master writes, called when "you need visual details conditioned on the
  subtitles for" the current segment.[^c16][^c17] On the authors' LongTVQA
  episodes, grounding added to the text-only master raises "answer accuracy
  from 64.3 to 69.0,"[^c19] and "Enabling vision after grounding further lifts
  accuracy to 74.8."[^c18]
  The backbone and prompts are held fixed. The gain therefore comes from the
  question-conditioned text, but no raw-frame master is run, so whether such
  text matches raw frames is not shown. My inference: the trade-off is between
  question-agnostic text and raw input, and question-conditioned text sits
  between them.

## Related

- [[cost-ordered-perception-pyramid]] — the method the paper builds to resolve
  this trade-off, by ordering the perception cost stage by stage.
- [[perception-substitution-gap]] — the measured gap when a model's
  perception is replaced by another channel; the same concern on the model side.
- [[hierarchical-retrieval-interfaces]] — choosing how much of a source to read
  per step, the text-retrieval version of the same choice.
- [[query-relative-token-overflow]] — the same point for a compressed token: whether the compressed form is adequate is a property of the pair (context, question), not of the compression alone.

[^c1]: arxiv-2512-23044 — "perception but incurs prohibitive context costs,"
[^c2]: arxiv-2512-23044 — "w/ GPT-5.1 19.05 50.80 78,229 76,955"
[^c3]: arxiv-2512-23044 — "This confirms the context explosion bottleneck: the agent is forced to watch every frame,"
[^c4]: arxiv-2512-23044 — "reducing the context load to a negligible"
[^c5]: arxiv-2512-23044 — "Lossy Compression: Accuracy drops to 18.57%,"
[^c6]: arxiv-2512-23044 — "The color of the pen cannot be determined from the provided videos."
[^c7]: arxiv-2512-23044 — "w/ Transcript 7.14 52.49 15,606"
[^c8]: arxiv-2512-23044 — "performance collapses in Level 2 and Level 3 tasks,"
[^c9]: arxiv-2512-23044 — "the modality gap: textual proxies fail to capture the"
[^c10]: arxiv-2512-23044 — "w/ Qwen3 13.81 70.83 55,047 53,764"
[^c11]: arxiv-2512-23044 — "The color of the pen is not specified in the provided videos."
[^c12]: arxiv-2512-23044 — "Answer: Red"
[^c13]: arxiv-2512-23044 — "definitive empirical evidence of the modality gap."
[^c14]: arxiv-2512-23044 — "exposing that search agents can locate metadata"
[^c15]: arxiv-2512-23044 — "while text-centric summarization optimizes efficiency but often misses critical visual details required for accurate grounding."
[^c16]: arxiv-2512-20618 — "no raw images are passed to the master agent"
[^c17]: arxiv-2512-20618 — "you need visual details conditioned on the subtitles for"
[^c18]: arxiv-2512-20618 — "Enabling vision after grounding further lifts accuracy to 74.8"
[^c19]: arxiv-2512-20618 — "answer accuracy from 64.3 to 69.0"
