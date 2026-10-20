---
description: "Replaces a clarifying text question with a small rendered panel of prototype images spanning the candidate set's modes; the user picks one instead of answering in words."
aliases: ["CLARA (visual disambiguation)", "CLArification by Rendering Alternatives", "generative visual disambiguation", "render-and-snap disambiguation"]
sources: ["tran-2026"]
---
# CLARA (visual disambiguation)

> When the axis of [[efe-planning-as-variational-inference|ambiguity]] is visual (viewpoint, fine appearance), CLARA
> asks by showing: it renders one prototype image per plausible reading and
> lets the user pick the closest, instead of phrasing the distinction as a
> text question a model must also learn to answer.

## Definition / Mechanism

CLARA operates on a calibrated retrieval belief over a corpus. When the
current conformal candidate set is too large to commit, the system clusters
candidates along interpretable ambiguity axes (preserved / changed /
viewpoint / background) into a few modes, renders one prototype target image
per mode with a conditional diffusion model, and asks the user to pick the
panel image closest to their intent: "We propose CLARA (CLArification by
Rendering Alternatives). When the candidate set is large, CLARA partitions
it into a few modes along interpretable ambiguity axes, renders one
prototype target image per mode with a conditional diffusion model, and
asks the user to do the easiest possible thing: pick the panel image
closest to their intent."[^c1]

The panel is chosen, not hand-designed: a submodular objective trades off
covering the belief's mass against panel diversity, and each rendered
prototype is snapped to its nearest real corpus image before entering the
candidate set, so generation can only change what is shown, never what
counts as a match: "Two design choices keep the rendering honest:
prototypes are chosen to cover the belief (a submodular generate-to-cover
objective), and each rendered prototype is snapped to its nearest real
corpus exemplars, so a hallucinated image can never enter or inflate the
prediction set."[^c2]

Across open-domain and fashion composed-image-retrieval benchmarks, CLARA
is statistically tied with text-question baselines at the first turn and
resolves the target in fewer interaction rounds: "Across open-domain and
fashion benchmarks CLARA is single-turn competitive, holds nominal coverage
across rounds, and reaches the target in fewer rounds than the strongest
text-question policy, with the largest gains on viewpoint and attribute
ambiguity."[^c3]

## Known as

| Field | Name there | Match |
|---|---|---|
| Tran, Le, Pham et al. (2026), abstract | CLARA / CLArification by Rendering Alternatives | exact — the paper's own name; disambiguated from the unrelated genomics-query system [[result-divergence-clarification-trigger]] that reuses the same acronym |
| Tran, Le, Pham et al. (2026), contributions | generative visual disambiguation | exact — the paper's name for the class of technique |
| This note | render-and-snap disambiguation | close — a descriptive label the wiki uses; not the paper's phrase |

## Why it matters

It changes *how* a question touches an axis (stall 3) when the axis is
visual: instead of forcing a viewpoint or fine-appearance distinction into
words and then training a model to both pose and predict the answer, CLARA
exposes the retrieval belief's own modes as pictures and lets the user's
pick be the constraint directly, with no answer-model standing in for the
user. It also bears on which mode to surface first (stall 2): the panel
selection is a coverage-diversity objective over the belief, not a
hand-picked or randomly ordered set of candidates.

## Transfer

The panel-selection rule imports a combinatorial-optimization guarantee:
"Greedy maximization of Eq. (8) gives a (1−1/e) approximation [25] and is
parameter-free given the belief, so no reinforcement-learned questioner is
needed."[^c4]

| | |
|---|---|
| **In its home field** | Greedy maximization of a submodular coverage-diversity objective (facility-location coverage minus a redundancy penalty) has a $(1-1/e)$ approximation guarantee (submodular optimization) |
| **Here** | The greedy rule selects which few prototype images to render and show as the clarification panel, recomputed from the current belief after every user pick |
| **What survives** | The $(1-1/e)$ worst-case guarantee on how well the shown panel covers the belief's mass, and the fact that no learned policy is needed to pick the panel |
| **What does not** | The guarantee bounds panel coverage of belief mass, not whether the user can correctly recognise their intent among the rendered options, and not the retrieval coverage guarantee itself (that rests on [[turn-valid-coverage]], a separate reweighting) |

## Limits

The claim rests on domains where the ambiguity is expressible as a small
number of interpretable visual modes with a real corpus image near each
(open-domain and fashion composed image retrieval); the paper's own
single-turn comparison is stated only as a tie within a ±1.0 paired-bootstrap
threshold, not a win, and CLARA depends on a frozen diffusion renderer and
embedding index that must already separate the relevant ambiguity axes —
an axis the retriever's embedding space does not resolve cannot be rendered
into distinguishable prototypes.

## Related

[[graphical-preview-disambiguation]] · [[turn-valid-coverage]] · [[value-of-information]]

[^c1]: tran-2026 — "We propose CLARA (CLArification by Rendering Alternatives). When the candidate set is large, CLARA partitions it into a few modes along interpretable ambiguity axes, renders one prototype target image per mode with a conditional diffusion model, and asks the user to do the easiest possible thing: pick the panel image closest to their intent."
[^c2]: tran-2026 — "Two design choices keep the rendering honest: prototypes are chosen to cover the belief (a submodular generate-to-cover objective), and each rendered prototype is snapped to its nearest real corpus exemplars, so a hallucinated image can never enter or inflate the prediction set."
[^c3]: tran-2026 — "Across open-domain and fashion benchmarks CLARA is single-turn competitive, holds nominal coverage across rounds, and reaches the target in fewer rounds than the strongest text-question policy, with the largest gains on viewpoint and attribute ambiguity."
[^c4]: tran-2026 — "Greedy maximization of Eq. (8) gives a (1−1/e) approximation [25] and is parameter-free given the belief, so no reinforcement-learned questioner is needed."
