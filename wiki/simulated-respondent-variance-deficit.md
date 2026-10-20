---
description: "Persona-conditioned LLM respondents match human item means but produce less variance across respondents than humans, under every model, prompt and temperature tested."
aliases: ["silicon sample variance", "LLM response homogeneity", "variance shrinkage in LLM survey simulation"]
sources: ["doi-10-5281-zenodo-18247291", "doi-10-1038-s41746-026-02942-6", "arxiv-2601-14264", "doi-10-3389-frai-2024-1393903", "arxiv-2512-02910", "arxiv-2511-21218"]
---
# Simulated-respondent variance deficit

When a language model is asked to answer a survey as a given person, its answers track the human item means reasonably well but spread out less across people. In the BREQ study, the item-level variances of LLM-generated responses "were much lower than human responses under all conditions," so the simulated sample is less diverse than the human sample it stands in for.[^v1] The means are close: the three chatbots "produced approximately similar tendencies of item means" to the human participants.[^v2] The gap is in the spread. The authors read it as a general pattern in persona simulation: well-crafted personas "approximate real-world human behaviors on average but hardly approximate the variability of human behaviors."[^v3]

The spread depends on how the prompt is built. When every simulated participant gets the same prompt, variability is near zero: "LLM variability is low to zero."[^v4] Adding per-person content raised it: "the more information one prompt contains, the higher variances LLM-generated responses yielded."[^v5] Interview content widened the spread for some models, not all. Claude gave more diverse responses when its prompts held the interview, and the paper concludes that "incorporating personal interview data can improve the diversity of generated responses for some LLM chatbots."[^v6] Gemini was the exception, more diverse with demographics alone.[^v14] The outputs also sat at the extremes: "LLMs tended to generate more extreme responses than humans."[^v7]

Temperature moved the spread in the expected direction. Higher temperature (0.5 against 0) gave "higher variances of item responses than lower temperature conditions" for all three chatbots.[^v8] The gain has a ceiling. A preliminary check found that temperatures above 0.5 "produced highly variable and conversational outputs that lacked the structure necessary for generating coherent item-level survey responses."[^v9] The discussion moves the threshold: "temperatures exceeding a certain threshold (e.g., >0.8)" tend to lose coherence, so the paper itself gives two values.[^v15]

The mechanism of the deficit is not established. The method generates all 15 items in one completion, "for all 15 survey items simultaneously within a single condition,"[^v13] which is a plausible place for answers to be pulled together, but this paper does not test it, so the link is my inference; compare [[shared-completion-batching-distortion]] for a related effect in batched generation. The persona literature also reports that expert personas lower answer entropy ([[expert-persona-confidence-amplification]]); this paper does not measure entropy, so that is a candidate mechanism, not a finding. The authors say "the underlying causes of this limitation remain poorly understood."[^v10]

A judging setting shows a similar narrowing. When AI agents configured to mirror physicians rank LLM outputs, they "produced highly stable rankings across simulated experience profiles": by the paper's count, 76.7% of ranking pairs were identical across seniority levels, against 3.3% among physicians.[^v16] The authors decline to read this stability as a merit: "This consistency, however, should not be equated with validity."[^v17] The measure is rankings, not survey item spread, and the task is evaluation rather than self-report. The paper does not test why the agents collapse; I read it as the same loss of spread appearing in a different output, which is my inference.

The compression also shows up at the level of whole surveys, in a different study with a larger sample. Across Studies 2 and 3 of the digital-twin paper, twins showed "substantial under-dispersion relative to humans," with responses regressing toward the mean.[^v18][^v19] The paper separates two remedies. Decoding changes are untested: raising temperature or top-p broadens outputs, but whether the added spread is real between-person variation or noise is not checked.[^v20] Calibration against a small human sample corrects aggregate and relational estimates, but it does not restore individual variance; the authors therefore read compression as partly correctable rather than as an absolute barrier.[^v21][^v22]

The narrower spread also appears in unprompted answers, measured on a different quantity. In a study of 2000 Stack Overflow questions, the emotion scores of ChatGPT answers vary less than those of human answers: "emotions exhibit higher variance compared to ChatGPT."[^v23] The measure is a classifier's emotion scores on text that no persona produced, so this is the same loss of spread on another object, not item responses across respondents (my inference that the two share a cause; the paper does not test it). The paper is not consistent on the direction. Its abstract says "Human responses displayed a broader" emotional spectrum,[^v24] while its third research question concludes that "highlights that humans tend to exhibit a narrower emotional range" within each topic.[^v25] The sections read do not settle which holds, so this finding is weaker than the survey ones above.

Finetuning on individual human responses is a second remedy, tested in a different setting. A study of GPT-4.1 finetuned on 25% of one treatment group, about 30 human observations, reports that "even a small number of finetuned samples can drastically improve diversity and mitigate homogeneity issues relative to the unfinetuned baseline."[^v28] The comparison is with the base model. The paper does not show that the restored spread equals the human spread, and the calibration result above is about estimates rather than training on individual responses, so the two are not directly comparable (my reading).

## Limits

- One study: 19 staff members, a 15-item BREQ, three commercial chatbots at one point in time. The authors warn that "the conclusions of this study should be interpreted with caution given the small sample size."[^v11] With 19 humans the human variance is itself a noisy target.
- Each condition yields one response per participant. The paper says its analysis "focused on single realizations from the sampling distribution rather than characterizing the full distributional variability."[^v12] So the deficit is measured across respondents, not within one respondent's repeated samples.
- The paper finds the deficit; it does not close it. Interview content helped two of three models, and no tested setting matched human spread.
- The authors of a related study give a conceptual reason for the spread gap. Every simulated answer is a draw from one conditional distribution fixed by training, so the randomness that temperature adds is not individual variation, and treating it as such is a category error.[^v26] [^v27] The argument is theirs; their study reports the gap, not its cause.
- Whether a compressed spread biases what is later estimated from simulated respondents (for example the item parameters in [[simulated-respondent-icc]]) is not tested. My inference: a simulator with less spread would understate the dispersion of any quantity estimated from it.

## Related

- [[narrative-over-demographic-persona-conditioning]] — which person-level content moves simulated answers toward a given person; the same prompts, judged on agreement rather than spread
- [[expert-persona-confidence-amplification]] — persona prompts lower answer entropy, a candidate mechanism for the spread deficit, untested here
- [[shared-completion-batching-distortion]] — batched generation of several items in one completion can distort the structure of synthetic data; a possible contributor, my inference
- [[simulated-respondent-icc]] — uses a simulated respondent to estimate item parameters; a compressed spread would bear on that use
- [[evaluator-cohort-ranking-shift]] — the human evaluator cohorts split on which model ranks first while the AI-agent cohort does not; the judging-side version of the same loss of spread
- [[network-measurement-invariance]] — the same compression is the authors' reason to prefer a network invariance test to SEM scalar and strict tests, which compression makes hard to satisfy
- [[nomothetic-span]] — compressed spread may bear on the correlations a span check reads (my inference; the digital-twin paper does not test this link)
- [[default-tone-skew]] — the mean side of the human-versus-ChatGPT answer comparison; the lean is read there, the spread here
- [[simulated-respondent-coefficient-recovery]] — finetuning on about 30 human observations widened the spread in one study, yet regression conclusions still did not match the human data

[^v1]: doi-10-5281-zenodo-18247291 — "were much lower than human responses under all conditions"
[^v2]: doi-10-5281-zenodo-18247291 — "produced approximately similar tendencies of item means"
[^v3]: doi-10-5281-zenodo-18247291 — "hardly approximate the variability of human behaviors"
[^v4]: doi-10-5281-zenodo-18247291 — "LLM variability is low to zero"
[^v5]: doi-10-5281-zenodo-18247291 — "the more information one prompt contains, the higher variances LLM-generated responses yielded"
[^v6]: doi-10-5281-zenodo-18247291 — "incorporating personal interview data can improve the diversity of generated responses for some LLM chatbots"
[^v7]: doi-10-5281-zenodo-18247291 — "LLMs tended to generate more extreme responses than humans"
[^v8]: doi-10-5281-zenodo-18247291 — "showed higher variances of item responses than lower temperature conditions"
[^v9]: doi-10-5281-zenodo-18247291 — "produced highly variable and conversational outputs that lacked the structure necessary for generating coherent item-level survey responses"
[^v10]: doi-10-5281-zenodo-18247291 — "the underlying causes of this limitation remain poorly understood"
[^v11]: doi-10-5281-zenodo-18247291 — "should be interpreted with caution given the small sample size"
[^v12]: doi-10-5281-zenodo-18247291 — "single realizations from the sampling distribution rather than characterizing the full distributional variability"
[^v13]: doi-10-5281-zenodo-18247291 — "the LLM generated responses for all 15 survey items simultaneously within a single condition"
[^v14]: doi-10-5281-zenodo-18247291 — "gemini had more diverse responses when prompts contained demographic information only"
[^v15]: doi-10-5281-zenodo-18247291 — "temperatures exceeding a certain threshold (e.g., >0.8)"
[^v16]: doi-10-1038-s41746-026-02942-6 — "AI-agent evaluators produced highly stable rankings across simulated"
[^v17]: doi-10-1038-s41746-026-02942-6 — "This consistency, however, should not be equated with validity."
[^v18]: arxiv-2601-14264 — "substantial under-dispersion relative to humans"
[^v19]: arxiv-2601-14264 — "responses regressing toward the mean and flattening individual heterogeneity"
[^v20]: arxiv-2601-14264 — "genuine between-person heterogeneity rather than noise is untested"
[^v21]: arxiv-2601-14264 — "compression is better viewed as a quantifiable, partly correctable property than as an"
[^v22]: arxiv-2601-14264 — "estimands rather than restoring individual variance"
[^v23]: doi-10-3389-frai-2024-1393903 — "emotions exhibit higher variance compared to ChatGPT."
[^v24]: doi-10-3389-frai-2024-1393903 — "Human responses displayed a broader"
[^v25]: doi-10-3389-frai-2024-1393903 — "highlights that humans tend to exhibit a narrower emotional range"
[^v26]: arxiv-2512-02910 — "This is a category error that may upend the"
[^v27]: arxiv-2512-02910 — "repeatedly from the same LLM model: a single conditional probability distribution whose"
[^v28]: arxiv-2511-21218 — "even a small number of finetuned samples can drastically improve diversity and mitigate homogeneity issues relative to the unfinetuned baseline"
