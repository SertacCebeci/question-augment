---
description: "A bias test is a measurement whose conceptualisation (what it claims to measure) and operationalisation (how it is built) must both be stated, or its validity cannot be judged."
aliases: ["measurement modelling", "construct-operationalisation split", "conceptualisation versus operationalisation"]
sources: ["doi-10-48550-arxiv-2305-12757"]
---
# Measurement modelling

Measurement modelling is a framework "originating from the social sciences" that splits any measurement into two parts.[^c1] The conceptualisation is what the measurement is meant to capture. For a bias test it includes the bias or harm meant, and the outcome the model should show. The operationalisation is the concrete construction: the prompt, the metric, the groups compared. In the authors' words, "Our taxonomy captures both what a bias test aims to measure—its conceptualisation—and details of how that measurement is carried out—its operationalisation."[^c2]

The split turns validity into a matching question. Validity concerns whether a measurement "measures what it claims to", and the claim lives in the conceptualisation while the test lives in the operationalisation.[^c3] The framework names several kinds of validity, each a different way the match can fail. Content validity needs the conceptualisation "clearly articulated" and the operationalisation to "capture relevant aspects of it, without capturing irrelevant ones."[^c4] Convergent validity asks for agreement with other established measures. Predictive validity asks whether the measure is "able to correctly predict measurements of a related concept".[^c5] Ecological validity asks how well results generalise to the world, and consequential validity asks what the measure does to the world, such as introducing new harms.[^c6] The authors draw most of this list from Jacobs and Wallach (2021) and add ecological validity.[^c7]

Applied to 90 bias tests, the framework finds that the two halves are often unstated or mismatched. "core aspects of bias test conceptualisations and operationalisations are frequently unstated or ambiguous, carry implicit assumptions, or be mismatched."[^c8] Eleven per cent of tests are unclear about the bias studied, and 22 per cent are unclear about the desired outcome.[^c9] Without the second, a test cannot be checked against its goal: "Without clear desired outcomes, we cannot assess if the prompt task or the metric is appropriate for that goal."[^c10]

The same split shows a concrete mismatch. A test that compares sentiment across groups measures sentiment. Whether that is a measure of harm depends on a harm the paper says is often never defined: "without defining the anticipated harm, it is unclear if comparing sentiment is an appropriate measure of that harm."[^c11] The desired outcome is also a choice with content. "Since choices of bias conceptualisation and desired outcome inevitably encode assumptions about what a language model ought to do," leaving them unstated leaves those assumptions unexamined.[^c12] One common unstated choice is invariance, where "Many tests implicitly adopt invariance as a desired outcome", requiring the same treatment of every demographic group.[^c13]

Validity threats also cross the boundary of the test. 68 per cent of tests address only upstream models, and the authors call this a threat to predictive validity, because "there is as yet no study showing a clear relationship between behaviour in an upstream LM and how it is used in a generative context."[^c14]

What survives the transfer from the social sciences is the split and the matching question: a measure can be well built and still measure the wrong thing, and the stated claim is what decides which. What does not transfer cleanly is the scoring. The framework gives categories, not a number for how much a threat distorts a result, and the paper does not say which threat matters most for a given purpose.

## Limits

- The percentages (68, 26, 11, 22) are counts from annotating 77 papers covering 90 tests. Ten per cent of papers were double-annotated, and "the remaining papers were annotated by a single author."[^c15]
- The paper is an analysis of how tests are described and built, not an experiment. It shows the threats are present in the literature, not that any given test's results are wrong. The authors also say their taxonomy "is a reflection of what is missing as much as what is present."[^c16]
- Validity types are used by different fields with different definitions; the paper itself notes "alternate definitions" of ecological validity.[^c17]
- Stereotype conceptualisations are inconsistent across papers, which the authors identify as a barrier to comparing convergent results, so the framework diagnoses a mismatch without resolving which concept is right.[^c18]

## Related

- [[validity-reliability-tradeoff]] — the same design choices that secure validity can cost reliability, a second axis the framework does not score.
- [[sentiment-as-harm-proxy]] — a worked content-validity mismatch: sentiment used to operationalise harm.
- [[metric-criterion-decoupling]] — the NLG-wide version of the problem: metrics and quality criteria are picked independently, so a score is not tied to what it measures.
- [[validity-screening-protocol]] — "validity" here means something narrower: whether a confidence signal carries item-level information at all.

[^c1]: doi-10-48550-arxiv-2305-12757 — "a framework originating from the social sciences"
[^c2]: doi-10-48550-arxiv-2305-12757 — "Our taxonomy captures both what a bias test aims to measure—its conceptualisation—and details of how that measurement is carried out—its operationalisation."
[^c3]: doi-10-48550-arxiv-2305-12757 — "each of which identifies some aspect of whether a measurement measures what it claims to."
[^c4]: doi-10-48550-arxiv-2305-12757 — "our conceptualisation of the underlying construct should be clearly articulated and our operationalisation should capture relevant aspects of it, without capturing irrelevant ones."
[^c5]: doi-10-48550-arxiv-2305-12757 — "Predictive validity requires that a measurement be able to correctly predict measurements of a related concept."
[^c6]: doi-10-48550-arxiv-2305-12757 — "Ecological validity we use to refer to how well experimental results generalise to the world"
[^c7]: doi-10-48550-arxiv-2305-12757 — "here we largely draw from the categorization presented by Jacobs and Wallach (2021), adding ecological validity"
[^c8]: doi-10-48550-arxiv-2305-12757 — "core aspects of bias test conceptualisations and operationalisations are frequently unstated or ambiguous, carry implicit assumptions, or be mismatched."
[^c9]: doi-10-48550-arxiv-2305-12757 — "11% of bias tests (Fig 1b) are not clear about the bias being studied, and 22% (Fig 1c) are not clear about the desired outcome"
[^c10]: doi-10-48550-arxiv-2305-12757 — "Without clear desired outcomes, we cannot assess if the prompt task or the metric is appropriate for that goal."
[^c11]: doi-10-48550-arxiv-2305-12757 — "without defining the anticipated harm, it is unclear if comparing sentiment is an appropriate measure of that harm"
[^c12]: doi-10-48550-arxiv-2305-12757 — "Since choices of bias conceptualisation and desired outcome inevitably encode assumptions about what a language model ought to do"
[^c13]: doi-10-48550-arxiv-2305-12757 — "Many tests implicitly adopt invariance as a desired outcome"
[^c14]: doi-10-48550-arxiv-2305-12757 — "there is as yet no study showing a clear relationship between behaviour in an upstream LM and how it is used in a generative context."
[^c15]: doi-10-48550-arxiv-2305-12757 — "the remaining papers were annotated by a single author."
[^c16]: doi-10-48550-arxiv-2305-12757 — "Our taxonomy is a reflection of what is missing as much as what is present."
[^c17]: doi-10-48550-arxiv-2305-12757 — "(though see Kihlstrom (2021) for alternate definitions)"
[^c18]: doi-10-48550-arxiv-2305-12757 — "inconsistencies among conceptualisations of stereotyping present a challenge for assessing convergent validity"
