---
description: "Decoding temperature and corrupted retrieved context compound in RAG: at high temperature the same perturbation costs more accuracy, and temperature drives output variability more."
aliases: ["temperature-perturbation interaction", "internal versus external noise in RAG", "temperature as degradation amplifier"]
sources: ["arxiv-2512-01183"]
---
# Temperature–perturbation interaction

A RAG answer can go wrong from two noise sources. The retriever may hand the model the wrong evidence, which is external noise. The model then draws its tokens from a distribution whose spread the decoding temperature sets, which is internal noise. Temperature rescales the token probabilities so that the distribution "peaks (resp. is flat) for large (resp. low) temperature values", and because the sampling then runs token by token, the setting shapes the whole generation, not one word.[^t1] Robustness studies usually fix one source and vary the other. The TempPerturb-Eval paper names the gap directly: retrieval and generation parameters are examined "in isolation, overlooking their interaction."[^t2]

## The mechanism

Take a multi-hop HotpotQA question with its gold supporting sentences as the context, and perturb that context in one of three ways. Sentence replacement swaps the latter part of a supporting sentence for "irrelevant sentences from the same title." Sentence removal deletes "the latter half of" the supporting sentences. NER replacement masks entities, "replacing them with [MASK] tokens".[^t3] The same prompt is then sampled across a temperature grid, "(0.0, 0.2, 0.4, … , 1.8, 2.0)", and each answer is scored against a reference by BERTScore.[^t4]

The design uses repeated runs to separate the two sources. Each condition is run three times, "to help distinguish the effect" of internal noise, which is the spread across runs, "from that of external perturbations", which is the gap between perturbed and unperturbed conditions.[^t5] The interaction is the claim that the second quantity is not constant across the first.

## What was measured

The damage a perturbation does depends on the temperature it is sampled at. The paper's summary is that "temperature acts as a performance degradation amplifier."[^t6] For gpt-4o, degradation "beginning at T = 1.4" is reported, while Llama models show "earlier performance deterioration at T = 0.6", with a gentler slope.[^t7] The deepseek-reasoner model "maintains nearly invariant performance" across the grid, so the amplification is model-specific rather than universal.

The interaction also reorders the models. At lower temperatures "GPT models achieve the highest BERTScore", but at T = 2.0 "deepseekreasoner maintains consistent performance while" the GPT models fall below the Llama models.[^t8] The ordering of the perturbation types is not stable either: for gpt-4o, "NER Replacement induces minimal degradation at T = 2.0, whereas Sentence Replacement and Sentence Removal lead to more substantial performance loss."[^t9]

For output variability the two axes differ. Measured by the coefficient of variation of BERTScore, temperature has "stronger influence on output variability than perturbation types in most models."[^t10] So in this setup temperature is the larger driver of spread, while for correctness the perturbation and the temperature have to be read together. The qualitative cases point the same way: at T = 2.0 the sentence perturbations produce refusals and garbled text, and at T = 0.6 models are more robust but "do not eliminate sensitivity to perturbations."[^t11]

## Limits

- One task and one dataset. The paper says "the generalizability of the observed temperature-perturbation interaction patterns to other task types" is still to be validated.[^t12]
- Gold contexts only. The study is "perturbing gold contexts, thereby controlling for retrieval noise", so the retriever is not in the loop and the compounding of retrieval error with sampling error is not measured.[^t13]
- Temperature is the only sampling parameter varied; the paper holds "other generation parameters (e.g., top-p, frequency penalty)" at defaults.[^t14]
- The sample is 600 items across five models, three runs per condition. Three runs give thin estimates of spread per cell (my inference), and the paper's own grid of thresholds (1.4, 0.6) is specific to these models and this prompt.
- The qualitative failure modes come from "the sample with the largest BERTScore gap" in each cell, which is a selected case, not a random one.[^t15]
- Reference answers were built by a model from the short gold answer, and "we transform the reference information into" a full sentence before scoring.[^t16] The metric therefore measures agreement with a model-written reference (my inference from the method).
- The interaction is a pattern across a grid of settings. The paper does not intervene on the mechanism that makes the damage grow with temperature.

## Related

- [[parametric-knowledge-gates-retrieval-noise-damage]] — another condition that decides how much irrelevant context hurts: the answerer's own knowledge. Here the second condition is the sampling setting (my reading).
- [[variability-source-attribution]] — sorts run-to-run variability by its source; temperature is the model-induced kind there, and this paper measures it against input perturbation.
- [[inference-time-input-noise-injection]] — noise added to the input at inference to steady a forecast, the opposite use of input noise: here noise is the thing being measured, not a tool.

[^t1]: arxiv-2512-01183 — "peaks (resp. is flat) for large (resp. low) temperature values"
[^t2]: arxiv-2512-01183 — "parameters like temperature in isolation, overlooking their interaction"
[^t3]: arxiv-2512-01183 — "with irrelevant sentences from the same title"
[^t4]: arxiv-2512-01183 — "(0.0, 0.2, 0.4, … , 1.8, 2.0)"
[^t5]: arxiv-2512-01183 — "noise (due to temperature) from that of external perturbations"
[^t6]: arxiv-2512-01183 — "temperature acts as a performance degradation amplifier"
[^t7]: arxiv-2512-01183 — "degradation beginning at T = 1.4"
[^t8]: arxiv-2512-01183 — "where deepseekreasoner maintains consistent performance while"
[^t9]: arxiv-2512-01183 — "minimal degradation at T = 2.0, whereas Sentence Replacement and Sentence Removal lead"
[^t10]: arxiv-2512-01183 — "stronger influence on output variability than perturbation types in most models"
[^t11]: arxiv-2512-01183 — "do not eliminate sensitivity to perturbations"
[^t12]: arxiv-2512-01183 — "the generalizability of the observed temperature-perturbation interaction patterns to other task types"
[^t13]: arxiv-2512-01183 — "perturbing gold contexts, thereby controlling for retrieval noise"
[^t14]: arxiv-2512-01183 — "holding other generation parameters (e.g., top-p, frequency penalty)"
[^t15]: arxiv-2512-01183 — "the sample with the largest BERTScore gap"
[^t16]: arxiv-2512-01183 — "we transform the reference information into"
