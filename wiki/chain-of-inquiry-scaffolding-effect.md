---
description: "Sequencing questions as an ordered, intent-conditioned chain — not merely giving a model prior dialogue history — is what drives the measured gain in diagnostic accuracy and reduced hallucination."
aliases: ["Chain of Inquiry", "CoI", "structural inquiry scaffolding"]
sources: ["arxiv-2604-20983", "arxiv-2512-11995"]
---
# Chain-of-inquiry scaffolding effect

> Structural inquiry — not oracle history — drives the observed gains.

## Definition / Mechanism

A **Chain of Inquiry (CoI)** models a diagnostic trajectory as an[^s1]
ordered sequence of question–answer turns `(q1,a1), …, (qT,aT)`, where
each question is conditioned on the visual evidence, the prior turns,
and a latent epistemic intent — in [[arxiv-2604-20983|Thinking Like a
Botanist (2026)]]'s domain, one of Diagnosis, Prognosis or Management,
itself a function of the case's severity. Botanists inspect an image,
infer this diagnostic intent, and probe further with questions that
adapt to species, symptoms and severity; the CoI formalizes that
trajectory as a dataset-level artifact rather than leaving it implicit
in a model's free-form reasoning.^c1

The paper isolates *why* CoI-structured evaluation helps, with a
three-way ablation on the same eighteen MLLMs: **Direct** (diagnose
from the image alone), **Scaffolded** (answer each question in
isolation, no prior turns), **Guided** (answer sequentially, given the
ground-truth history of previous turns) and **Cascading** (answer
sequentially, conditioned only on the model's own previously generated
answers, not an oracle). Question-Guided diagnosis is significantly
more correct than Direct diagnosis across all severity levels: forced
to attend to the specific visual features a question names (lesion
margins, halo presence) rather than free-associating from a prior over
common diseases, models hallucinate less.^c2

Critically, Cascading — no oracle history, only the model's own,
possibly wrong, prior answers — retains 96.3% of Guided's efficiency
gain and 81.7% of its diagnostic-accuracy gain, across all eighteen
models. Perfect context access (Guided) is only a marginal addition
over the realistic autoregressive regime (Cascading). The dominant
driver of both effects is the ordered, intent-conditioned *structure*
of the question chain itself, which keeps acting as an attentional
prior that constrains hallucination even when every prior answer in
the chain was self-generated and possibly wrong.^c3

## Why it matters

This separates two things a question-asking system might be credited
for: giving an answerer more *context* (memory of prior turns) versus
giving it a *scaffold* (an ordered sequence of targeted questions that
routes attention to specific evidence). The ablation shows the second
does most of the work — an architecture that only appends raw
conversation history without a targeted next-question policy would
capture under a fifth of the accuracy gain a structured chain gets.

## Limits

Measured in one domain (plant-leaf image diagnosis) with a fixed,
expert-authored question taxonomy (7 categories, 3 intents); whether
the same decomposition (structure vs. memory) transfers to open-ended
or adversarial domains is unverified. Even under the full CoI
scaffold, top-tier models still exhibit "false reassurance" —
classifying a diseased sample as healthy — so the effect reduces but
does not eliminate the most consequential failure mode.

A multi-step visual benchmark measures the same direction with uneven size. Giving the chain's ground-truth steps raises final accuracy for most models and categories, "higher accuracy on final questions when intermediate steps are introduced";[^c4] but "The Retrieval category shows relatively minor improvements in both tasks",[^c5] and for some models the chain "can generate distractive reasoning paths or omit essential reasoning cues in Planning task".[^c6] So the structure effect is not uniform across task types, and it can reverse for some models.

## Related

- [[expected-information-gain]]
- [[decision-centric-design]]
- [[grounding-entropy-clarification-gate]]
- [[four-causes-follow-up-generation]]
- [[uncertainty-band-corroboration-gate]]
- [[question-planning-following-split]] — the same kind of chain, scored by separating the choice of the next sub-question from answering it

[^s1]: arxiv-2604-20983
[^c4]: arxiv-2512-11995 — "higher accuracy on final questions when intermediate steps are introduced"
[^c5]: arxiv-2512-11995 — "The Retrieval category shows relatively minor improvements in both tasks"
[^c6]: arxiv-2512-11995 — "distractive reasoning paths or omit essential reasoning cues in Planning task"
