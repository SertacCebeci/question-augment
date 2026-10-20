---
description: "Order perception by cost: rank candidate videos by cheap metadata, localise sparse frames in the survivors, and decode densely only the windows that remain."
aliases: ["pyramidal perception", "Pyramidal Perception", "metadata-first filtering before visual decoding", "cheap-to-dense perception cascade", "lightweight gatekeeper before a larger model"]
sources: ["arxiv-2512-23044", "arxiv-2512-22442"]
---
# Cost-ordered perception pyramid

An answerer who must look at many candidate sources can spend its expensive
perception in three stages, each more costly than the last and each run only
on what the stage before kept. The paper calls this Pyramidal Perception. Its
agent, Video-Browser, is described as "effectively mitigating the
perception-context trade-off" by this ordering.[^c1]

At the base, nothing is decoded. A text model reads each candidate's titles
and snippets and judges its relevance to the current sub-task. This costs no
visual inference, and it "aggressively prunes the search space before data
loading occurs."[^c2]

In the middle, the survivors are localised rather than watched. The paper's
claim is that for retained videos "the challenge shifts from selection to
localization, finding where the relevant information resides without
incurring the cost of full decoding."[^c3] A sparse set of frames is sampled
together with the full transcript, and the model proposes time windows. The
windows are the "glimpses" that the paper says "compresses hourlong videos
into focused" evidence.[^c4]

At the tip, only those windows are decoded at high frequency. The paper
argues that "expensive reasoning power is allocated exclusively" to them, so
that it goes "to the most information-dense moments, effectively" resolving
the trade-off.[^c5][^c6]

The mechanism is an ordering by cost, with the gate being survival rather
than confidence. A cheaper stage removes candidates, and the more expensive
stage never sees them. This is the same cheapest-first routing that
[[sage-abstention-evaluation]] uses for verifiers, except that there the
escalation is triggered by a stage abstaining, and here by a candidate
passing a relevance judgement made from text alone.

## What was measured

The measurements are on the paper's Video-BrowseComp benchmark, with GPT-5.1
as the backbone unless marked. Direct visual inference, which feeds raw frames
to the model, reached 19.05% overall accuracy at a total of 78,229 tokens.[^c7]
The pyramid reached 26.19% and used 32,627 tokens, which the paper reports as
a 58.3% reduction against direct inference.[^c8] The accuracy claim is that
"By equipping the agent with Pyramidal Perception" the agent reaches the
highest score among the systems compared.[^c9]

The ablation in the same paper removes one stage at a time. Removing the
base stage gives the lowest of the component variants, at 9.52% against 12.86%
for the full system.[^c10] Denser sampling at the middle stage helps as well:
raising the number of scanned frames from 4 to 64 moved accuracy from 10.5%
to 15.7%, which the authors read as the sparse stage's ability to localise
improving with density.[^c11]

The cost is counted as "the cumulative cost of scanning, filtering, and
reasoning" in tokens.[^c12]

## The same ordering in text retrieval

HiFi-RAG applies the same cheapest-first gate to web text, with a text model in the base role. Gemini 2.5 Flash, described as "4-6× cheaper than Pro",[^c21] screens search results by URL, title and preview before any page is scraped. It then judges each parsed section from its title and "using only its title and a small snippet (the first 200 characters of content)", and only the surviving sections go to Gemini 2.5 Pro.[^c14][^c15] The gate is a model judgement, not an embedding: the paper reports that embedding-based filtering "performed worse than LLM-based filtering".[^c16]

The measured effect is on what gets removed. The URL step "reduces the URL count by 33.5% (averaging across 100 queries)", and the section step "removes 60.5% of chunks (averaged across 100 queries)".[^c17][^c20] On the validation set the paper credits the search-plus-filter stack with "another 4%" over plain search.[^c18] On Test2025, my reading of Table 3 gives ROUGE-L 0.2915 for search alone, 0.2966 with the URL gate, and 0.3031 with the URL and section gates. The paper also contrasts the deterministic pipeline with a full agent that chooses its own steps, which "was 10× more expensive and significantly slower, often timing out without improving ROUGE scores".[^c19]

The gate here also judges from a thin preview, so the base-stage caveat below applies: the paper reports no recall figure for the filters, and nothing shows that the 60.5% removed held no needed chunk. The "4-6×" is a price ratio, not a measured total cost.

## Limits

- The base stage judges relevance from titles and snippets alone. A correct
  candidate with an uninformative title is removed before any visual check can
  find it. The excerpt read gives no recall figure for this stage, so how often
  it prunes the right source is not shown.
- The advantage depends on the backbone. With Qwen3 the pyramid scored 14.29%
  at 26,525 tokens, against 13.81% at 55,047 tokens for direct inference, so the
  accuracy gap there is under half a point on 210 questions.[^c13] The excerpt
  reports no variance across runs, so that gap cannot be separated from noise.
- The benchmark has 210 questions, of which 23 are Level 3. The ablation is one
  configuration, not a sweep.
- Efficiency is measured in tokens, not latency or cost in money. Whether the
  stages save wall-clock time when decoding is cached or parallel is not shown.
- The pyramid is one way to order the work. The paper does not compare it with
  other orderings, such as ranking by a visual pass over thumbnails first.

## Related

- [[perception-context-tradeoff]] — the trade-off this ordering is built to
  resolve; the measured failures of the two ends it sits between.
- [[hierarchical-retrieval-interfaces]] — the same coarse-to-fine choice of
  granularity per step, in text retrieval rather than video.
- [[sage-abstention-evaluation]] — cheapest-first routing with escalation on
  abstention, in verification of dialogue agents.
- [[confidence-triggered-visual-reattention]] — a single zoom-in re-query gated
  by the model's own confidence, not by a ranking of candidates.

[^c1]: arxiv-2512-23044 — "effectively mitigating the perception-context trade-off"
[^c2]: arxiv-2512-23044 — "aggressively prunes the search space before data"
[^c3]: arxiv-2512-23044 — "the challenge shifts from selection to localization, finding where the relevant information"
[^c4]: arxiv-2512-23044 — "compresses hourlong videos into focused"
[^c5]: arxiv-2512-23044 — "expensive reasoning power is allocated exclusively"
[^c6]: arxiv-2512-23044 — "resolving the perception-context trade-off."
[^c7]: arxiv-2512-23044 — "prohibitively expensive, consuming 78,229 total"
[^c8]: arxiv-2512-23044 — "reduces the Total Tokens to 32,627, a 58.3% (GPT5.1) reduction compared to Direct Visual Inference."
[^c9]: arxiv-2512-23044 — "By equipping the agent with Pyramidal Perception"
[^c10]: arxiv-2512-23044 — "Removing it yields the lowest performance among all component variants (9.52%)"
[^c11]: arxiv-2512-23044 — "leads to a consistent performance gain (10.5%"
[^c12]: arxiv-2512-23044 — "cost of scanning, filtering, and reasoning"
[^c13]: arxiv-2512-23044 — "w/ Qwen3 14.29 65.74 26,525 7,678"
[^c14]: arxiv-2512-22442 — "as a lightweight gatekeeper to semantically filter hierarchically parsed web content before"
[^c15]: arxiv-2512-22442 — "using only its title and a small snippet (the first 200 characters of content)"
[^c16]: arxiv-2512-22442 — "This performed worse than LLM-based filtering"
[^c17]: arxiv-2512-22442 — "This process reduces the URL count by 33.5% (averaging across 100 queries)"
[^c18]: arxiv-2512-22442 — "The addition of Search (RAG) and active Filtering (Filters) added another 4%"
[^c19]: arxiv-2512-22442 — "was 10× more expensive and significantly slower, often timing out without improving ROUGE scores"
[^c20]: arxiv-2512-22442 — "This removes 60.5% of chunks (averaged across 100 queries)"
[^c21]: arxiv-2512-22442 — "Gemini 2.5 Flash (4-6× cheaper than Pro)"
