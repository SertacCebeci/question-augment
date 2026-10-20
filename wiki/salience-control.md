---
description: "Salience control moves which evidence a fixed model foregrounds, so a prompt can change both the evidence selected and the label that evidence supports; accuracy alone does not capture it."
aliases: ["evidence foregrounding", "evidence-first prompting", "prompt salience control"]
sources: ["arxiv-2512-12688"]
---
# Salience control

Salience control is the second of the three levels: how a prompt foregrounds information within a task. "Salience control concerns how information is foregrounded within a task."[^s1] The distinction it draws is between what is available and what becomes central. "Interpretation depends not only on what information is available" — it also depends on which parts of that information become central to the response.[^s2] The level matters when an input holds several candidate evidence sentences and only some should guide the decision.

Claim verification is the paper's measurable case. The same claim and the same candidate evidence are presented under different prompts: neutral verification, evidence-first selection, support-oriented, and refutation-oriented. "An evidence-first prompt makes evidence identification prior to labeling."[^s3] Because the evidence is the same in every condition, a change in what the model selects is a change in foregrounding. The paper notes that these prompts "can therefore change both the selected evidence and the label supported by that evidence."[^s4] The output carries both a label and the identifiers of the evidence it rests on, so label and evidence can be scored separately and together.

The paper's measures are evidence gain (change in evidence F1 against the neutral prompt), joint gain (change in label–evidence joint performance) and leakage reduction (fewer distractor sentences selected). The reason for these measures is stated in the text: "The relevant movement is not exhausted by label accuracy."[^s5] A prompt can keep the label and still change which evidence carries it, or raise evidence overlap while the label stays flat.

The effects are model-specific. For one model the paper reports that "evidence-first and support-oriented prompts improve several grounding-related measures, while refutation-oriented prompting shifts behavior toward REFUTES decisions."[^s6] For another, "the salience prompts mainly produce targeted changes in evidence overlap, leakage, and class-wise recall rather than broad performance gains."[^s7] The paper's summary is that these prompts "do not simply make verification better or worse".[^s8]

## Limits

- The evidence set is fixed in each example, with gold sentences and sampled distractors. The paper's own caveat is that "Salience prompts depend on both wording" and on the evidence environment, so the effect is conditional on what the context holds.[^s9]
- The context itself was not varied. The paper names what would be needed: "vary retrieval quality, sentence ordering, distractor density, and evidence filtering".[^s10] Until those are run, the claim that a prompt moves salience is shown only for one fixed candidate set per example.
- One model's evidence choices are noisy. The paper says that for one model "its evidence choices remain noisy", so the salience movement there is weak evidence about the model's grounding.[^s11]
- The measures are of what the model selects, not of what it uses internally. Whether the selected sentence is the one the answer depends on is not tested.
- The paper says a foregrounding prompt cannot create evidence that is absent: "foregrounding depends on whether relevant information is available, distinguishable from distractors, and placed in a useful context."[^s12] This restriction follows from the paper's account; I have not tested it.

## Related

- [[frame-activation]] — the level above in the paper's hierarchy: a prompt changes the criterion of judgment, not the evidence
- [[retrieval-utilization-gap]] — a failed run is either evidence never surfaced or evidence surfaced but misused; salience control acts on the surfaced side, which is my reading of the paper's context-engineering remark
- [[instruction-steered-cue-reliance]] — the same kind of effect in a multimodal answerer, where the question's wording moves which cue is relied on
- [[construal-selection]] — the level below in the hierarchy: the task's organization, not the evidence it foregrounds

[^s1]: arxiv-2512-12688 — "Salience control concerns how information is foregrounded within a task."
[^s2]: arxiv-2512-12688 — "Interpretation depends not only on what information is available"
[^s3]: arxiv-2512-12688 — "An evidence-first prompt makes evidence identification prior to labeling."
[^s4]: arxiv-2512-12688 — "can therefore change both the selected evidence and the label supported by that evidence"
[^s5]: arxiv-2512-12688 — "The relevant movement is not exhausted by label accuracy."
[^s6]: arxiv-2512-12688 — "evidence-first and support-oriented prompts improve several grounding-related measures, while refutation-oriented prompting shifts behavior toward REFUTES decisions"
[^s7]: arxiv-2512-12688 — "rather than broad performance gains"
[^s8]: arxiv-2512-12688 — "do not simply make verification better or worse"
[^s9]: arxiv-2512-12688 — "Salience prompts depend on both wording"
[^s10]: arxiv-2512-12688 — "vary retrieval quality, sentence ordering, distractor density, and evidence filtering"
[^s11]: arxiv-2512-12688 — "its evidence choices remain noisy"
[^s12]: arxiv-2512-12688 — "foregrounding depends on whether relevant information is available, distinguishable from distractors, and placed in a useful context"
