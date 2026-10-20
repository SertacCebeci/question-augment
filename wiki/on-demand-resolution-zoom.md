---
description: "An answerer that starts from a coarse overview and requests finer clips mid-reasoning, under a per-call frame budget, beat denser fixed sampling on fewer frames in reported runs."
aliases: ["temporal zoom", "first glance then zoom", "agentic zoom-in", "adaptive frame zoom"]
sources: ["arxiv-2512-22315", "arxiv-2512-20618"]
---
# On-demand resolution zoom

An answerer given a long source can be handed it in two ways. One is a fixed set of samples chosen before any reasoning starts. The other is a coarse overview plus a tool that returns a finer piece of the source on request, in the middle of reasoning. The paper (VideoZoomer) builds the second and states the problem with the first directly: prevailing approaches "rely on uniform frame sampling or static pre-selection, which might overlook critical evidence and unable to correct its initial selection error during its reasoning process."[^c1] The alternative starts "from a coarse low-frame-rate overview," and the model then calls a temporal zoom tool for high-frame-rate clips "at autonomously chosen moments, thereby progressively gathering fine-grained evidence in a multi-turn interactive manner."[^c2][^c3]

The mechanism has two budgets. Each request is capped: a segment at frame rate f over a window of length t must satisfy f times t at most B, and "Each tool calling is constrained by a frame budget."[^c4] The number of requests is also capped. The episode runs "until the agent determines it has sufficient information to produce a final answer."[^c5] Perception is therefore paid for only where the model asks for it, and the decision to stop belongs to the answerer. The difference from static pre-selection is where the location of the fine evidence is decided: after a first look, not before reasoning. My reading is that this defers commitment to a reading until a targeted look has been taken; the paper does not frame it that way.

Two results are reported for the 7B model. On MLVU, the model "achieves 0.64 accuracy using only 48 frames on average, surpassing" a uniform baseline at a much larger 128-frame budget.[^c6] On LVBench, the model with 77 frames outperforms the baseline with 256 frames.[^c7] The model's count is an average the model produced, not a cap: "For our model, it represents the actual average number of frames consumed per dataset, a result of its dynamic decision-making process."[^c8]

The policy is learned in two stages, and the second stage shows what the zoom needs. Reinforcement learning from scratch over structured tool calls "is notoriously sample-inefficient and prone to instability," so the model is first given supervised trajectories, distilled from proprietary models: "We leverage state-of-the-art proprietary models, such as GPT-4o."[^c9][^c10] Trajectories in which the first clip was wrong and a later one corrected it are the reflection data, made by "having an expert model correct the failures of an initial agent."[^c11] Without them, the policy shows what the paper calls a "simple strategy, where the average tool call count stabilizes at about 1.0."[^c12] With them, the full method "learns to make nearly two calls on average."[^c13] The reward matters too: "removing the conditional tool-use bonus" makes tool use trend toward zero during training, which the authors read as the agent failing to find the tool's utility without explicit encouragement.[^c14]

A second loop of the same shape was measured with its stages separated.
In LongVideoAgent a text-only master calls a grounding tool to localise a
clip, and then a vision tool to read it, under a step cap. Grounding alone
raises answer accuracy "from 64.3 to 69.0," and adding vision after grounding
reaches 74.8, so each stage's share is reported apart.[^c17][^c18] The
backbone and prompts are held fixed, which the authors take to attribute the
gain to the procedure.[^c19] The overview there is subtitles, not frames, so
this is a request-a-finer-look move on a text-first source, not a coarse-to-fine
visual zoom.

## Limits

- The efficiency claim is in frames consumed. Tokens, latency and money are not the measure in the sections read, so the cost of the zoom in the context window is not shown.
- The baseline is one family, Qwen2.5-VL-7B, and the comparisons are on video benchmarks. The paper's own note on reasoning-heavy data is that "complex reasoning tasks may not benefit from increasing visual information, which" can add noise; on LongVideoReason both models peak near 64 frames.[^c15] More frames is not a monotone gain, and a model that uses fewer frames is not automatically more accurate.
- The overview still matters. Replacing the uniform overview with a learned selector raised accuracy further, "and +3.0 on LongVideoBench."[^c16] The zoom adds to a good overview; it does not replace one.
- The supervised data depends on strong proprietary teachers. Whether the policy survives weaker teachers is not tested in the sections read.
- The paper does not measure the case that matters most for the mechanism: a moment that the overview missed and the model never asked about. The correction claim rests on the reflection data, not on a measured miss rate.
- The ablations are single configurations. I read their direction in the text, not the full table.

## Related

- [[perception-context-tradeoff]] — the trade-off this mechanism sits inside. Raw input floods the context and text proxies lose detail; the zoom is a third option, raw detail on request.
- [[cost-ordered-perception-pyramid]] — also orders perception by cost, but in fixed stages before reasoning, not inside the reasoning loop.
- [[chain-of-thought-interleaved-retrieval]] — the text-retrieval case of fetching evidence mid-reasoning. The zoom fetches finer resolution of the same source rather than new sources.
- [[stop-continue-criteria-in-retrieval-loops]] — the stopping decision of the same loop; here the answerer stops when it judges its information sufficient.

[^c1]: arxiv-2512-22315 — "static pre-selection, which might overlook critical evidence and unable to correct its initial selection error during its reasoning process"
[^c2]: arxiv-2512-22315 — "Starting from a coarse low-frame-rate overview"
[^c3]: arxiv-2512-22315 — "autonomously chosen moments, thereby progressively gathering fine-grained evidence in a multi-turn interactive manner"
[^c4]: arxiv-2512-22315 — "Each tool calling is constrained by a frame budget"
[^c5]: arxiv-2512-22315 — "this process continues until the agent determines it has sufficient information to produce a final answer"
[^c6]: arxiv-2512-22315 — "On MLVU, our model achieves 0.64 accuracy using only 48 frames on average, surpassing"
[^c7]: arxiv-2512-22315 — "where our model using 77 frames outperforms the baseline using 256 frames"
[^c8]: arxiv-2512-22315 — "For our model, it represents the actual average number of frames consumed per dataset, a result of its dynamic decision-making process."
[^c9]: arxiv-2512-22315 — "Reinforcement learning from scratch on a complex, high-dimensional action space, such as generating structured tool calls, is notoriously sample-inefficient and prone to instability"
[^c10]: arxiv-2512-22315 — "We leverage state-of-the-art proprietary models, such as GPT-4o"
[^c11]: arxiv-2512-22315 — "generate reflection data by having an expert model correct the failures of an initial agent"
[^c12]: arxiv-2512-22315 — "simple strategy, where the average tool call count stabilizes at about 1.0"
[^c13]: arxiv-2512-22315 — "our full method learns to make nearly two calls on average"
[^c14]: arxiv-2512-22315 — "removing the conditional tool-use bonus"
[^c15]: arxiv-2512-22315 — "complex reasoning tasks may not benefit from increasing visual information, which"
[^c16]: arxiv-2512-22315 — "and +3.0 on LongVideoBench"
[^c17]: arxiv-2512-20618 — "answer accuracy from 64.3 to 69.0"
[^c18]: arxiv-2512-20618 — "Enabling vision after grounding further lifts accuracy to 74.8"
[^c19]: arxiv-2512-20618 — "Because backbones and prompts are held fixed, these improvements are attributable to the agentic procedure"
