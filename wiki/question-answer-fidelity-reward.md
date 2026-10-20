---
description: "A generated image is scored by asking the same diagnostic questions of it and of its source image, with reference answers from the same solver, so the reward needs no labels."
aliases: ["QA fidelity", "question-answer fidelity score"]
sources: ["doi-10-48550-arxiv-2606-27376"]
---
# Question-answer fidelity reward

A generated image is usually scored by a learned reward model or a preference label, both of them external to the generator. This work scores it by questions. A set of diagnostic questions is drawn about the source image, the solver answers them on that source image to give reference answers, and the same questions are then answered on the generated image. The reward is the agreement between the two sets of answers.[^q1] The agreement is a soft match, "a soft answer match combining exact/substring/numeric agreement with the Solver majority fraction".[^q2] The resulting score "measures how well local attributes, counts, and relations are preserved".[^q3]

The reference answers are what keep this from being a self-graded label. The paper says they are generated internally from the real image and are "not Proposer labels, human annotations, dataset labels, or external supervision".[^q4] Before any generator update, low-quality prompt cards are dropped by a spec-quality gate and a minimum-QA gate, so a generated image cannot score well by matching an underspecified prompt.[^q5]

The question score is local. A global counterpart recaptions the generated image with the solver and compares the caption with the prompt: "QA fidelity is local; we add a global check by captioning the generated image".[^q6] The generator's reward combines the two, with the default weights given as "QA fidelity weight 0.65, cycle-consistency weight 0.20", plus small diversity and contradiction terms.[^q7] In the paper's ablation the question term matters more: "On generation, QA fidelity contributes more than cycle-consistency", and "removing QA fidelity causes the largest GenEval drop".[^q8][^q9] The headline result is that on BAGEL the method "improves image generation performance on GenEval from 82% to 85%".[^q10]

## Limits

- Shared error. The reference answers come from the same solver that is being trained. If the solver misreads the source image, that misreading becomes the reference the generator is rewarded for matching. The paper's answer is that the references are not external labels, which does not rule out a shared error. This objection is my inference.
- Validity is shown by correlation across checkpoints, not per image. The paper reports that "The clearest relationship appears for QA fidelity" when the internal scores are set against external GenEval, and it calls that evidence "supporting evidence for the coupling claim alongside the main loop-ablation results" rather than a causal test.[^q11][^q12]
- Coverage is bounded by the questions. An attribute that no sampled question touches is never scored. The paper does not measure how much of an image the question set covers. This is my inference.
- The cycle term relies on frozen similarity backends, CLIP-style where needed, which the paper says "are not trained reward models".[^q13] The scoring model is thus not learned, but it is also not checked against human judgement in the slices read here.
- The reward is shared across three generator families, but "the supervision signal is shared" while the update rule differs per backbone.[^q14] That transfer is tested on three backbones in one paper, not on a wider set.

## Related

- [[solver-token-entropy]] — the same solver's token-level uncertainty, used on the question side of this paper
- [[self-consistency-difficulty-score]] — the answer-agreement signal used to judge questions rather than images
- [[question-reconstructability-reward]] — a cycle-consistency reward on questions; this note's cycle term instead recaptions an image and compares
- [[question-based-summary-evaluation]] — question-answer scoring applied to summaries rather than generated images

[^q1]: doi-10-48550-arxiv-2606-27376 — "We sample M diagnostic questions about I (from the Proposer)"
[^q2]: doi-10-48550-arxiv-2606-27376 — "a soft answer match combining exact/substring/numeric agreement with the Solver majority fraction"
[^q3]: doi-10-48550-arxiv-2606-27376 — "measures how well local attributes, counts, and relations are preserved"
[^q4]: doi-10-48550-arxiv-2606-27376 — "they are not Proposer labels, human annotations, dataset labels, or external supervision"
[^q5]: doi-10-48550-arxiv-2606-27376 — "Low-quality prompt cards are filtered by spec-quality and minimum-QA gates before any generator update"
[^q6]: doi-10-48550-arxiv-2606-27376 — "QA fidelity is local; we add a global check by captioning the generated image"
[^q7]: doi-10-48550-arxiv-2606-27376 — "Generation reward uses QA fidelity weight 0.65, cycle-consistency weight 0.20"
[^q8]: doi-10-48550-arxiv-2606-27376 — "On generation, QA fidelity contributes more than cycle-consistency"
[^q9]: doi-10-48550-arxiv-2606-27376 — "removing QA fidelity causes the largest GenEval drop"
[^q10]: doi-10-48550-arxiv-2606-27376 — "improves image generation performance on GenEval from 82% to 85%"
[^q11]: doi-10-48550-arxiv-2606-27376 — "The clearest relationship appears for QA fidelity"
[^q12]: doi-10-48550-arxiv-2606-27376 — "supporting evidence for the coupling claim alongside the main loop-ablation results"
[^q13]: doi-10-48550-arxiv-2606-27376 — "They are not trained reward models."
[^q14]: doi-10-48550-arxiv-2606-27376 — "the supervision signal is shared"
