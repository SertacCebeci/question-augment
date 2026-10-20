---
description: "A small compressor's summary bounds what a larger predictor can answer, so accuracy tracks compressor size and family far more than predictor size past about 70B."
aliases: ["compressor-predictor system", "compressor-predictor agentic system", "front-loading compute into compressors"]
sources: ["arxiv-2512-21720"]
---
# Compressor-predictor scaling

A recurring agentic pattern splits a job in two. A smaller model compresses raw context into compact text, and a larger model reads only that text and produces the answer: "smaller compressor models distill raw contexts into" compact texts that larger predictor models then consume.[^c1] The predictor never sees the raw context, so whatever the compressor drops is unavailable to it. The paper's breakdown of compressor failures makes the loss concrete. Of the errors made in the compression step, one share is "contains no answer (33.3% of compressor errors)", and another is that "the compression omits details or parts of the" information the answer needs.[^c2][^c18]

The paper tests which stage to spend compute on by scaling both. On LongHealth, "scaling a Qwen-2.5 compressor from 1B to 7B improves accuracy by 60%".[^c3] Scaling the predictor buys much less: "whereas scaling the predictor from 70B to 405B yields only a 12% improvement on LongHealth."[^c4] The predictor gains level off once a baseline capacity is reached: the predictor "provides only marginal improvements in accuracy once a baseline predictor capacity" of roughly 8B to 70B is reached.[^c5] The paper states the comparison as "Scaling compressors is more effective than scaling predictors."[^c6]

The compressor side is also cheap in compute, which the paper treats as the reason to run it locally. Larger compressors emit fewer output tokens at similar accuracy, so compute per generation grows sublinearly with size. On LongHealth, a Qwen-2.5 compressor scaled "from 1.5B to 7B parameters with only a 1.3%" increase in FLOPs-per-generation.[^c7] The resulting design principle is to front-load compute into a larger local compressor and so reduce the work the cloud predictor must do.[^c8] In the Deep Research pipeline, a Qwen-2.5-14B compressor with a GPT-4o predictor "achieves 2.3% higher RACE scores at only" 28.1% of the API cost of the uncompressed baseline.[^c9]

Across the logistic regression over all settings, the paper ranks the factors as "compressor model family > compressor size > predictor size."[^c10] Its meta-analysis says "compressor model family is the most important factor", and that scaling the compressor "matters substantially more" than scaling the predictor.[^c11]

The paper frames the pair as an information bottleneck: it evaluates "the compressor-predictor system as an information bottleneck across different tasks and domains."[^c12] This is where the result is anchored, not a proof of it. My reading, which the paper does not test directly, is that the predictor's accuracy is capped by how much of the context the summary still carries. Past a point a larger predictor cannot recover what the compression no longer holds, which is why predictor scaling flattens.

## Limits

- The predictor finding holds only over the predictor sizes tested: Llama-3 from 1B to 405B, Qwen-2.5 72B, and GPT-4o. The paper is not consistent about the size of the top gain. The introduction says a 12% improvement, while section 3.1 says "The gains in accuracy by increasing predictor size from 70B to 405B are within 12%". Read the magnitude as approximate.[^c13]
- The scope is non-reasoning, single-round systems. The paper says it "primarily focus[es] on GPT-style non-reasoning models with single-round communication, limiting generalizability to reasoning-augmented models or iterative multi-agent workflows."[^c14] Whether the predictor stays unimportant when it must reason over the summary, or when the workflow loops, is not tested.
- Compression here means summarization: "While we define compression as summarization in this work" the paper notes that structured extraction and function-call generation also compress, and these are not measured.[^c15]
- Accuracy is scored by a judge model, "against the ground-truth using a GPT-4o-mini judge", so the scaling curves inherit that judge's errors.[^c16]
- Family and size are confounded across the comparison. The paper reports that "Qwen-2.5 compressors scale more compute-efficiently than" Llama and Gemma-3, so a size curve drawn for one family does not transfer to another.[^c17]

## Related

- [[information-bottleneck]] — the frame the paper uses to read the compressor as the bottleneck between context and answer.
- [[compound-ai-systems]] — the systems-over-models view under which this two-model pattern sits.
- [[compressed-memory-versus-raw-retrieval]] — the same tension from the memory side: raw records beat compressed memory there, and the gap narrows as models grow.
- [[information-rate-per-token]] — the per-token measure the paper uses to rank compressors without running the full pipeline.
- [[sampled-mutual-information-estimator]] — how the information a compression carries is estimated, independent of any task.

[^c1]: arxiv-2512-21720 — "smaller compressor models distill raw contexts into"
[^c2]: arxiv-2512-21720 — "contains no answer (33.3% of compressor errors)"
[^c18]: arxiv-2512-21720 — "the compression omits details or parts of the"
[^c3]: arxiv-2512-21720 — "scaling a Qwen-2.5 compressor from 1B to 7B improves accuracy by 60%"
[^c4]: arxiv-2512-21720 — "whereas scaling the predictor from 70B to 405B yields only a 12% improvement on LongHealth."
[^c5]: arxiv-2512-21720 — "predictor LM provides only marginal improvements in accuracy once a baseline predictor capacity"
[^c6]: arxiv-2512-21720 — "Scaling compressors is more effective than scaling predictors."
[^c7]: arxiv-2512-21720 — "Qwen-2.5 compressors can scale from 1.5B to 7B parameters with only a 1.3%"
[^c8]: arxiv-2512-21720
[^c9]: arxiv-2512-21720 — "A Qwen-2.5-14B compressor paired with a GPT-4o predictor achieves 2.3% higher RACE scores at only"
[^c10]: arxiv-2512-21720 — "compressor model family > compressor size > predictor size."
[^c11]: arxiv-2512-21720 — "compressor model family is the most important factor"
[^c12]: arxiv-2512-21720 — "We evaluate the compressor-predictor system as an information bottleneck across different tasks and domains."
[^c13]: arxiv-2512-21720 — "The gains in accuracy by increasing predictor size from 70B to 405B are within 12%"
[^c14]: arxiv-2512-21720 — "limiting generalizability to reasoning-augmented models or iterative multi-agent workflows."
[^c15]: arxiv-2512-21720 — "While we define compression as summarization in this work"
[^c16]: arxiv-2512-21720 — "against the ground-truth using a GPT-4o-mini judge."
[^c17]: arxiv-2512-21720 — "Qwen-2.5 compressors scale more compute-efficiently than"
