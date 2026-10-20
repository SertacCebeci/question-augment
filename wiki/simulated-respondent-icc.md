---
description: "Fine-tuning an LLM on ability-level descriptors and reading its answer-token probabilities as an item characteristic curve estimates IRT parameters without field-test data."
aliases: ["synthetic ICC", "simulated student responses", "LLM-simulated examinee"]
sources: ["arxiv-2601-02580", "arxiv-2512-18880"]
---
# Simulated-respondent item characteristic curve

The idea is that a language model can stand in for a population of examinees. The paper frames it as "can stand in for a population of examinees at a given" ability level, so that item parameters are recovered from simulated answers rather than from field data.[^s1] The earlier form of this idea fine-tuned transformer models to produce synthetic responses to a 2PL-calibrated grammar item, which the paper credits to Maeda.[^s2] The present method instead conditions a generative model on discrete ability descriptors and reads its answer probabilities as a discrete [[item-characteristic-curve]].

## Mechanism

Three steps carry it.

1. **Ability as labelled classes.** Instead of N students with θ values, the method provides "N classes of students, each associated with" a descriptor.[^s3] Each label L_k covers an interval of θ, so every θ maps to exactly one label. The paper uses 20 descriptors, running from low to high ability, and generated the descriptors and their bounds by prompting a language model.[^s4][^s19]

2. **Answer probabilities as a discrete curve.** For each item, the discrete ICC is the set of probabilities, one per label, that a student in that class answers correctly. The paper writes it as "item j is given by the N probabilities", one entry per label.[^s5] The LLM is fine-tuned so that, given a descriptor and an item, the probability mass on the option tokens matches a softmax of the form of the [[nominal-response-model]].

3. **Back to continuous parameters.** To turn the discrete curve into a and b, each label is mapped to an expected θ inside its interval, under the assumption that θ is normal: "we map the label Lk to the expected θ values".[^s6] The labels are weighted by how much of the ability distribution each one covers: "We take this into account by defining weights".[^s7] The two-parameter curve is then fitted to the discrete points by weighted least squares.

Training has two stages. Supervised fine-tuning first teaches the model the answer format, with "We sampled a single answer for each item for each ability level".[^s21] A second stage equates the LLM's option probabilities with the nominal model's, using a squared-difference loss, "is the square of the difference between the left and right" side of the equation,[^s22] and a lower learning rate.[^s8] The adapters are low-rank (LoRA), so only a small set of weights is trained on top of a frozen model.[^s9]

## What was measured

On the ELA dataset (754,000 responses to 275 items), the Qwen-14B model "demonstrated the strongest" performance,[^s23] reaching "an average correlation of 0.503 for the 1PL difficulty parameter and 0.446 for 2PL" discrimination.[^s10] The abstract's own reading is that the technique "seems particularly effective at modeling item discrimination".[^s11] On the BEA 2024 Shared Task (201 test items, difficulty only), "Qwen-8B achieved the highest Pearson Correlation of 0.381".[^s12]

## Limits

- The datasets are small. The paper says "student performance data may be necessary to fully validate the scaling laws" and the IRT approximations before the result can be trusted.[^s13]
- The paper is explicit that the field is not there yet: "the field is not yet at a point where LLMs can be reliably trusted for high-stakes difficulty prediction".[^s14] Its own reading is that the models are for low-stakes pre-testing.
- The BEA evaluation has no student responses, so the uniform-guessing correspondence was assumed: "Because student response data was not directly available".[^s15] That result is therefore a check against benchmark labels under an assumption, not against simulated choices.
- The regression of difficulty estimates toward the mean is expected: "we expect this process to regress the difficulty estimates to the mean".[^s16] The paper corrects it with a linear map fitted on a development set, "we fit the ability level estimates on the development set to the true ability level values".[^s17] The final scale therefore depends on that fitted map, not on the simulation alone.
- Only the final answer is simulated. "While the current study focused on the final answer produced by the simulated" respondent, reasoning traces were not used.[^s18]
- My inference, not the paper's: the curve estimated this way describes the simulator's response pattern, which need not match a real population. Agreement with field parameters is an empirical question for each dataset, and the reported correlations are moderate on the larger set.

- A zero-shot baseline is weaker. A separate study prompts unfine-tuned models for item difficulty for students and concludes that "LLMs struggle with cold-started IDP." Its correlations are highest on SAT Math and lowest on USMLE, where "alignment is stronger in logic-driven tasks" than in knowledge-heavy items.[^s24][^s25] The fine-tuned route here is a different regime; the zero-shot study tests only prompting, so it does not show that fine-tuning would fail.

## Related

- [[item-characteristic-curve]] — the curve and two-parameter form this method estimates, without field responses
- [[nominal-response-model]] — the softmax form the LLM's option probabilities are matched to, and the uniform-guess reduction used on BEA
- [[difficulty-conditioned-evolving-item-generation]] — estimates item parameters from many LLMs' real responses; this route needs one simulated respondent and no examinee data
- [[item-writing-guidelines]] — difficulty and discrimination are the criteria those guidelines are checked against; item analysis computes them after administration, and this method estimates them before it

[^s1]: arxiv-2601-02580 — "can stand in for a population of examinees at a given"
[^s2]: arxiv-2601-02580 — "was first articulated by Maeda, who fine-tuned transformer-based models according to"
[^s3]: arxiv-2601-02580 — "Instead of having N students, we will be providing N classes of students, each associated with"
[^s4]: arxiv-2601-02580 — "We prompted a language model to provide appropriate descriptors and bounding values for use"
[^s5]: arxiv-2601-02580 — "item j is given by the N probabilities"
[^s6]: arxiv-2601-02580 — "we map the label Lk to the expected θ values"
[^s7]: arxiv-2601-02580 — "We take this into account by defining weights"
[^s8]: arxiv-2601-02580 — "we are now looking to equate the output"
[^s9]: arxiv-2601-02580 — "select a collection of linear layers and augment them by the addition of an additive factor"
[^s19]: arxiv-2601-02580 — "where 20 is the number of ability level descriptors"
[^s21]: arxiv-2601-02580 — "We sampled a single answer for each item for each ability level"
[^s22]: arxiv-2601-02580 — "is the square of the difference between the left and right"
[^s23]: arxiv-2601-02580 — "the Qwen-14B model demonstrated the strongest"
[^s10]: arxiv-2601-02580 — "achieving an average correlation of 0.503 for the 1PL difficulty parameter and 0.446 for 2PL"
[^s11]: arxiv-2601-02580 — "technique seems particularly effective at modeling item discrimination"
[^s12]: arxiv-2601-02580 — "Qwen-8B achieved the highest Pearson Correlation of 0.381"
[^s13]: arxiv-2601-02580 — "student performance data may be necessary to fully validate the scaling laws"
[^s14]: arxiv-2601-02580 — "the field is not yet at a point where LLMs can be reliably trusted for high-stakes difficulty prediction"
[^s15]: arxiv-2601-02580 — "Because student response data was not directly available"
[^s16]: arxiv-2601-02580 — "we expect this process to regress the difficulty estimates to the mean"
[^s17]: arxiv-2601-02580 — "we fit the ability level estimates on the development set to the true ability level values"
[^s18]: arxiv-2601-02580 — "While the current study focused on the final answer produced by the simulated"
[^s24]: arxiv-2512-18880 — "alignment is stronger in logic-driven tasks"
[^s25]: arxiv-2512-18880 — "LLMs struggle with cold-started IDP."
