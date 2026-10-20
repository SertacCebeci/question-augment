---
description: "Telling a model it is a layperson, a young child or a toddler lowers its accuracy on graduate-level multiple-choice questions, and the persona implying less knowledge tends to do worse."
aliases: ["negative-capability persona", "low-knowledge persona", "layperson persona cost"]
sources: ["arxiv-2512-05858"]
---
# Low-knowledge persona accuracy cost

A low-knowledge persona is the reverse of an expert one: it instructs the model to answer as someone who knows little. The Wharton study used three. A layperson gets "You are a layperson with no special training in this subject." A young child gets "You are a young child who thinks they understand the world but sometimes mixes things up." A toddler gets "You are a 4-year-old toddler who thinks the moon is made of cheese."[^c1] [^c2] [^c3] The same runs that tested expert personas on GPQA Diamond and MMLU-Pro included these three, so the comparison is within one design (see [[expert-persona-accuracy-null]]).

The authors describe these personas as having been "generally harmful to benchmark accuracy."[^c4] The harm is not uniform, but it is the more common direction. On GPQA Diamond, "several low-knowledge personas reduced accuracy."[^c5] For o4-mini, "all three low-knowledge personas" performed worse than the baseline, and on GPT-4o the Toddler persona produced a significant negative difference.[^c6] The one significant positive effect on that benchmark was a small gain for the Young Child prompt on Gemini 2.5 Flash, which the authors judge "a model-specific quirk."[^c7]

The persona's implied knowledge orders the damage. The paper says that "certain prompting variations consistently worsened performance," and that the Toddler prompt was the consistent case: "the Toddler prompt was significantly worse than the" Layperson prompt for five of six models on MMLU-Pro, with GPT-4o-mini the exception, for which "which had no statistically significant differences" appeared between any pair.[^c8] [^c9] The authors summarise the gradient as: "prompt persona type affected how poorly the models performed."[^c10]

The paper does not offer a mechanism for this; it reports the sign and the ordering. My own reading, not the paper's, is that a stated low competence is a cost the model pays in accuracy even when the question is answerable, so a persona is not a safe way to make an answer simpler.

## Limits

- The results are about accuracy on multiple-choice items with a fixed answer template. The authors say so directly: "These results are about the accuracy of answers only."[^c11] A persona can still change tone or register, which this test does not score.
- The ordering of Toddler below Layperson is an ordering of labels. The study does not measure how much knowledge each persona actually makes the model display, so "less knowledge implied" is a description of the prompt, not a measured quantity.
- The effect depends on the model. GPT-4o-mini showed no significant difference between any pair of prompts,[^c9] and Layperson effects "varying by model" were harmful in several cases but not all.[^c12]
- The rebuttal in [[expert-persona-confidence-amplification]] argues that a Toddler-over-physicist result in this data may reflect brevity under a token budget rather than knowledge. That argument is about the expert conditions' truncation and is not tested here; the two readings predict different things and the study alone does not decide between them.
- Six models, one temperature (1.0) and zero-shot prompting. The results do not show what a few-shot or reasoning-forced setup would give.

## Related

- [[expert-persona-accuracy-null]] — the expert side of the same runs; experts were roughly null while these personas were mostly negative
- [[expert-persona-confidence-amplification]] — the rebuttal's brevity-and-truncation reading of the Toddler result
- [[narrow-role-refusal]] — another way a role degrades answers: a refusal to answer, not a wrong answer

[^c1]: arxiv-2512-05858 — "You are a layperson with no special training in this subject."
[^c2]: arxiv-2512-05858 — "You are a young child who thinks they understand the world but sometimes mixes"
[^c3]: arxiv-2512-05858 — "You are a 4-year-old toddler who thinks the moon is made of cheese"
[^c4]: arxiv-2512-05858 — "which were generally harmful to benchmark accuracy"
[^c5]: arxiv-2512-05858 — "several low-knowledge personas reduced accuracy"
[^c6]: arxiv-2512-05858 — "performed worse than the baseline"
[^c7]: arxiv-2512-05858 — "which appears to be a model-specific quirk"
[^c8]: arxiv-2512-05858 — "the Toddler prompt was significantly worse than the"
[^c9]: arxiv-2512-05858 — "which had no statistically significant differences"
[^c10]: arxiv-2512-05858 — "prompt persona type affected how poorly the models performed"
[^c11]: arxiv-2512-05858 — "These results are about the accuracy of answers only"
[^c12]: arxiv-2512-05858 — "effects varying by model (harmful in several cases, but"
