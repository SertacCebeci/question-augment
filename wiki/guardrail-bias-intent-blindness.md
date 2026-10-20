---
description: "Input guardrail models flag bias-eliciting questions mostly under non-bias categories, so their flags follow surface keywords and harm categories rather than the bias intent of the question."
aliases: ["guardrail models", "LLM input guardrails", "moderation models for bias", "category-keyed input moderation", "intent blindness of guardrails"]
sources: ["arxiv-2512-19238"]
---
# Guardrail blindness to bias intent

A guardrail model sits in front of an LLM and labels each input as safe or unsafe under a set of categories. Its job is to catch a harmful request before the model answers it. Gueorguieva and Caliskan asked whether such a filter can catch a question that is built to elicit social bias, using three guardrails paired with three models: Llama Guard 3-8B, the Mistral Moderation API, and Granite Guardian 3.0-2B.[^c1] Every one of the 10,360 SocialStigmaQA prompts was written to elicit bias, so an ideal filter would flag the bias-category prompts.

What the filters flagged, and under which category, is the first result. Llama Guard flagged "the percentage of prompts from SocialStigmaQA that were identified to be harmful overall is 7.6%", but "only 44 prompts out of the entire 10,360" were flagged under its Hate category.[^c2] The Mistral Moderation API flagged more, with "the percentage of prompts from SocialStigmaQA that were identified to be harmful overall is 23.5%", and "and 632 inputs were" flagged under Hate and Discrimination.[^c3] Granite Guardian's default harm category flagged 31.9% of inputs, but its Social Bias category, which must be requested in a separate call, flagged 0.76%.[^c4][^c5] A flag is thus common and a bias flag is rare.

The paper's explanation is that the flags follow surface content. "Guardrail models may be flagging inputs as harmful simply if they contain a key word".[^c6] Its example is a stigma about "having sex for money", which Llama Guard "is flagged as a sex-related crime by"[^c7]: the flag assumes a criminal role for a person the prompt never describes as criminal. The consequence is that the category that would name the bias is the one that fires least: rarely is an input flagged for hate or discrimination, "thus failing to identify bias in the bias-eliciting prompts".[^c8]

The paper also measures what the flags would do if they were acted on. It does not put the guardrail in front of the model. It reclassifies: if an input that produced a biased answer was flagged for harm, the output is "the final output classification to be unbiased".[^c9] Under that rule the reduction is small. Llama's biased share fell "only by 1.4% (from 33.5% to 32.1%)"; Mistral's fell by 7.8%; Granite's default harm category gave the largest drop, a 10.4% decrease in biased answers. Granite's Social Bias category gave "there is a 0.029% decrease".[^c10][^c11] Bias went down under every guardrail, but the bias-named category removed almost none of it.

The conclusion the authors draw is that guardrails do not read the intention of a prompt: "the intentionality of bias behind the input is not identified by guardrail models".[^c12] For a wiki about questions, the point is that a moderation layer judges the question by what it names, not by what it asks the answerer to do. Two questions with the same stigma, one asking for a hiring recommendation and one asking for a description, can get different flags, and the bias-eliciting one may pass.

## Limits

- Three guardrails, three small instruction-tuned models, one benchmark. The guardrails' categories are fixed by each vendor, and a different category set could change which flags exist.
- The mitigation numbers are counterfactual. They assume that a guardrail flag would have stopped the biased answer, and that assumption was not tested by gating the model. My inference: a real gate could also refuse non-biased answers and would change the measured rates.
- Intent is inferred from category labels, not from a dataset labelled for intent. The paper suggests the gap is "over-reliance on keywords" but cannot separate keyword reliance from real differences in content.
- The benchmark contains only questions. "SocialStigmaQA contains only questions, rather than statements," and "Statements posed in a rhetorical or questioning fashion can" still convey judgment, so the paper's test does not cover the case where the wording is a question but the intent is a statement.[^c13][^c14]
- Harm in the paper is judged on a binary safe or unsafe label. The authors note "the limitation of the binary output requirement within the SocialStigmaQA benchmark", which bears on the answer side, not this input side.[^c15]
- The authors warn that correcting the blindness by intent detection has its own risk: a filter that reads intent may produce "unwarranted censorship towards those earnestly seeking information about a stigmatized identity".[^c16]

## Related

- [[stigma-social-features]] — which stigmas in these prompts draw biased answers, the answer-side view of the same benchmark
- [[script-level-obfuscation]] — the output-side version of the keyword problem: keyword refusal rules misclassify borderline answers, so the authors use a judge model instead
- [[intent-aware-response-strategy]] — a query classifier built on keyword and pattern rules, the same surface-matching design the paper here faults
- [[self-answering-injection-compliance]] — one keyword–regex defence and its measured effect on a different attack

[^c1]: arxiv-2512-19238 — "Llama Guard 3-8B, and the Mistral Moderation API" 
[^c2]: arxiv-2512-19238 — "only 44 prompts out of the entire 10,360"
[^c3]: arxiv-2512-19238 — "and 632 inputs were"
[^c4]: arxiv-2512-19238 — "the percentage of inputs identified as harmful is 31.9%"
[^c5]: arxiv-2512-19238 — "a separate call must be made to the model for the specific category of"
[^c6]: arxiv-2512-19238 — "Guardrail models may be flagging inputs as harmful simply if they contain a key word"
[^c7]: arxiv-2512-19238 — "is flagged as a sex-related crime by"
[^c8]: arxiv-2512-19238 — "thus failing to identify bias in the bias-eliciting prompts"
[^c9]: arxiv-2512-19238 — "the final output classification to be unbiased"
[^c10]: arxiv-2512-19238 — "only by 1.4% (from 33.5% to 32.1%)"
[^c11]: arxiv-2512-19238 — "there is a 0.029% decrease"
[^c12]: arxiv-2512-19238 — "the intentionality of bias behind the input is not identified by guardrail models"
[^c13]: arxiv-2512-19238 — "SocialStigmaQA contains only questions, rather than statements"
[^c14]: arxiv-2512-19238 — "Statements posed in a rhetorical or questioning fashion can"
[^c15]: arxiv-2512-19238 — "we note the limitation of the binary output requirement within the SocialStigmaQA benchmark"
[^c16]: arxiv-2512-19238 — "unwarranted censorship towards those earnestly seeking information about a stigmatized identity"
