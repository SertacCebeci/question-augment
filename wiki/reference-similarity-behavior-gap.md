---
description: "Generated code can score high on similarity to a reference implementation yet behave identically to it in only about a fifth of cases; similarity to a reference is not functional equivalence."
aliases: ["similarity-plausibility gap", "semantic similarity vs functional plausibility", "similarity-correctness gap in code generation"]
sources: ["arxiv-2511-16224"]
---
# Reference-similarity–behaviour gap

When a generated program is scored against a reference implementation, two families of measures can disagree. Textual and embedding similarity ask whether the output looks like the reference, token by token or in a learned vector space. Behavioural equivalence asks whether the output returns the same values, and the same reverts, on the same inputs. These are different properties, and a generator can do well on the first while doing poorly on the second.

The Solidity benchmark makes the split visible. Four LLMs were asked for functions from their natural-language `@notice` descriptions, and each output was scored three ways. On similarity the models look strong: "ChatGPT4o achieves the highest average semantic similarity with a mean of 0.6813", and the authors summarise that "all models demonstrate the ability to generate code that is substantially semantically aligned with the ground truth."[^c1] On behaviour the picture is different: "only 20%–26% of zero-shot generations behave identically to ground-truth implementations under testing."[^c2] The authors name the split themselves: "Our findings reveal a significant gap between semantic similarity and functional plausibility in LLM-generated Smart Contracts."[^c3]

The mechanism is a difference in what each measure can see. Similarity metrics never run the code. Behavioural checking does. For each reference function the authors built two corner-case inputs, "one assigning minimum values and one assigning maximum values to all numeric parameters", plus ten random inputs, ran the generated and reference versions on each, and compared returned values and exceptions.[^c4] A generated function was counted as plausible only if it matched on all of them, and the authors describe the aim as "to detect clear behavioral mismatches in generated contracts," not as a proof of equivalence.[^c5]

Where the mismatch comes from is the part the paper says most about, and it points at guard logic. The authors attribute the gap "largely" to "subtle mismatches between the generated functions and the ground truth, especially in the way corner cases and input validation using require statements are managed."[^c6] The generated code is "consistently simpler, with significantly lower complexity and gas consumption, often due to omitted validation logic."[^c7] My reading of why this matters for the measure: a missing or extra check changes behaviour only at the inputs it guards, so a score over the whole token sequence or embedding moves little while the corner-case output changes. That is an inference from the mechanism the paper describes, and the paper does not run an ablation that isolates it.

Retrieval moves the two measures unevenly. Retrieving similar examples into the prompt raised plausibility for every model, but the similarity scores did not move in step. DeepSeek-Coder-v2's similarity rose after retrieval ("raises its semantic similarity mean from 0.636 to 0.8006"), and its plausibility more than doubled, "its accuracy from 21.71% to 45.19%."[^c8] ChatGPT-4o's similarity barely changed ("similarity increasing from 0.6813 to 0.6859"), yet its plausibility rose "from 20.79% to 29.00%, a substantial gain."[^c9] Reading Table 2 directly, CodeLlama's mean similarity fell under retrieval (0.6674 to 0.6434) while its plausibility rose slightly (22.32% to 23.56%).[^c10] So a similarity gain is neither necessary nor sufficient for a plausibility gain in this data.

The reading the wiki keeps is this. A similarity score to a reference answers "how close is the text to that one"; it does not answer "does it do the same thing on the inputs that matter." The two can be separated, and the separation is largest where the difference lies in a few edge cases.

## Limits

- One benchmark, one language. The study covers Solidity, one dataset from 2021, and 500 sampled functions. The authors say the findings "may not fully generalize to all blockchain ecosystems or SC programming languages."[^c11]
- Plausibility is a test-based lower bound on disagreement, not equivalence. The test cases are not assessed for adequacy: "We do not evaluate the adequacy of the resulting test cases." A pass means no mismatch was found on those inputs.
- The testable subset shrinks. Only the 198 reference functions that compiled after automatic repair were used, and for one zero-shot model the compilable set fell to 11 contracts. The paper notes this "raises concerns about assessing generated code purely based on semantic and structural similarity."[^c12]
- The similarity measure is itself a choice. SmartEmbed is from 2019, and in a 50-pair check "CodeBERT frequently assigned high similarity scores (>0.9) even to semantically divergent functions."[^c13]
- The validation-omission account is only partly tested. A paired test on counts of `require` statements found no significant difference in six of eight model–setup combinations, and the authors conclude that "deviations in validation logic are limited and do not materially affect the reliability of our correctness metrics."[^c14] That result weakens the omission story as the main cause, and the paper does not offer another.
- Gas was measured on Ganache, which "does not perfectly reflect mainnet execution."[^c15] The gas claims inherit this.

## Related

- [[refinement-effort-score]] — grades a program by the effort needed to repair it, explicitly not by similarity to a reference; the same objection to reference similarity, from the grading side.
- [[answer-evidence-embedding-similarity]] — embedding similarity fails as a grounding signal for short answers; another place where a similarity score stands in for a property it does not measure.
- [[three-test-metric-validity-audit]] — checks whether a metric tracks the property it names; behavioural testing against a reference is one way such a check can be run.
- [[algorithmic-clinical-alignment-gap]] — an automatic score and a second, expert measure of the same outputs move apart; the same two-measurement split in a clinical setting.
- [[demonstration-label-consistency]] — top-K similarity retrieval of in-context examples does not guarantee the property retrieval is meant to supply; the RAG result here is a measured case of the same gap between what retrieval selects by and what the answer needs.

[^c1]: arxiv-2511-16224 — "ChatGPT4o achieves the highest average semantic similarity with a mean of 0.6813"
[^c2]: arxiv-2511-16224 — "only 20%–26% of zero-shot generations behave identically to ground-truth implementations under testing"
[^c3]: arxiv-2511-16224 — "Our findings reveal a significant gap between semantic similarity and functional plausibility in LLM-generated Smart Contracts"
[^c4]: arxiv-2511-16224 — "one assigning minimum values and one assigning maximum values to all numeric parameters"
[^c5]: arxiv-2511-16224 — "to detect clear behavioral mismatches in generated contracts"
[^c6]: arxiv-2511-16224 — "especially in the way corner cases and input validation using require statements are managed"
[^c7]: arxiv-2511-16224 — "consistently simpler, with significantly lower complexity and gas consumption, often due to omitted validation logic"
[^c8]: arxiv-2511-16224 — "its accuracy from 21.71% to 45.19%"
[^c9]: arxiv-2511-16224 — "from 20.79% to 29.00%, a substantial gain"
[^c10]: arxiv-2511-16224
[^c11]: arxiv-2511-16224 — "The findings of this study may not fully generalize to all blockchain ecosystems or SC programming languages"
[^c12]: arxiv-2511-16224 — "which raises concerns about assessing generated code purely based on semantic and structural similarity"
[^c13]: arxiv-2511-16224 — "assigned high similarity scores (>0.9) even to semantically divergent functions"
[^c14]: arxiv-2511-16224 — "deviations in validation logic are limited and do not materially affect the reliability of our correctness metrics"
[^c15]: arxiv-2511-16224 — "Gas consumption was evaluated using Ganache, which does not perfectly reflect mainnet execution"
