---
description: "Giving the model the full case up front, versus making it interview for it, splits a multi-turn failure into an inquiry deficit and a reasoning deficit; in dental dialogues the gap was inquiry."
aliases: ["Knowledge-Action Gap", "Direct Input Mode control", "inquiry versus reasoning decomposition"]
sources: ["arxiv-2601-12974"]
---
# Full-information control decomposition

A model that scores well on static questions often scores far lower when it must gather the facts itself over several turns. That drop alone does not say why. One design isolates the cause. Run the same cases twice. In "Multi-turn Inquiry Mode" a simulated patient holds the case vignette and the model must ask for what it needs. In "Direct Input Mode" the full vignette is handed to the model, which writes its management plan at once.[^c1] The difference between the two scores is the loss due to inquiry. What remains below the ceiling in Direct Input Mode is the loss due to knowledge or reasoning.[^c2]

## What was measured

The benchmark (SCMPE) covered dental cases: 118 real case reports, 498 checkpoint instances, 1,318 rubric points. In the interactive mode the target model decided when to stop, and was told to stop only when it was "100% confident" in the diagnosis. That forces it to judge whether it has enough information.[^c3] Every model scored higher in Direct Input Mode, with significance at p ≤ 0.0001 (weighted bootstrap, Holm correction).[^c4] The authors read the uniform uplift as showing that the bottleneck is "proactive information gathering and dynamic state tracking", not clinical knowledge.[^c5]

Safety was scored as a binary veto: one omitted safety-critical question gives Safety = 0 however fluent the later text is.[^c6] This ties the inquiry deficit to concrete failure. In implant-indication cases, models often did not assess bone volume and anatomy during the dialogue, and so triggered the veto despite having the theory.[^c7] Checkpoints with a standard pathway or obvious red flags (extraction contraindications, anaphylaxis) held up better.[^c8]

## Why the control matters for questioning

The design treats asking as a separable skill from knowing. A model can fail by not asking the right question even when it would answer correctly given the answer. The effect is measured by what the model does with complete versus elicited information, not by the quality of its final text. My inference: this is a template for locating where an asker fails, and any setting where a simulated respondent holds hidden facts could use it.

A related finding is that retrieval does not repair this gap. Adding guideline retrieval at every turn improved static open QA by 0.0125 to 0.1626, but in the dialogue task gains were heterogeneous: +0.1391 for one model, +0.0413 and +0.0357 for two leading ones, and -0.0147 for another.[^c9] The authors suggest that without a stable decision core, retrieved knowledge becomes "cognitive noise".[^c10]

## Limits

- The attribution is to the whole inquiry process (what to ask, when to stop, tracking state). The control does not separate these three from each other.
- Direct Input Mode is not a perfect reasoning ceiling. A full vignette also changes the task: no interaction, a different prompt, and possibly easier checkpoints. The authors' conclusion that the gap is driven "predominantly" by information gathering is an inference from a uniform uplift, not from a manipulated inquiry variable.
- The simulated patient and the question drafts were produced by one LLM family (Qwen), so simulator behaviour may shape the results. The paper does not test this.
- Single domain (dentistry), bilingual cases, 118 cases; whether the split carries over to other fields is untested.
- The explanation of RAG failure as "cognitive noise" is the authors' suggestion, not a tested mechanism.

## Related

- [[underspecified-question-eager-answering]] — answering before enough is known; the stopping rule here targets the same failure
- [[information-gathering-interview-style]] — how a questioner elicits facts in an interview
- [[knowledge-integration-decay]] — added knowledge failing to help downstream use

[^c1]: arxiv-2601-12974 — "By comparing scores between the"
[^c2]: arxiv-2601-12974 — "we can isolate performance deficits caused by information"
[^c3]: arxiv-2601-12974 — "This mechanism forces the"
[^c4]: arxiv-2601-12974 — "All models show a statistically significant performance improvement in the Direct Input Mode compared to the Multi-turn Inquiry Mode"
[^c5]: arxiv-2601-12974 — "the primary limitation in multi-turn dialogues is not the availability of clinical"
[^c6]: arxiv-2601-12974 — "a single"
[^c7]: arxiv-2601-12974 — "models often fail to systematically assess bone volume and anatomical constraints during the dialogue"
[^c8]: arxiv-2601-12974 — "several checkpoints remain comparatively stable in dynamic dialogues"
[^c9]: arxiv-2601-12974 — "other leading models like MedGPT and GPT-5.2 showed limited improvements"
[^c10]: arxiv-2601-12974 — "external knowledge can become cognitive noise rather than aid"
