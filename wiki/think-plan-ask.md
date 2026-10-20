---
description: "A three-step multi-agent question-selection cycle — analyse the diagnostic gap, pick a strategy, generate a question — that beat six dialogue-planning baselines at eliciting latent clinical traits."
aliases: ["TPA", "Think-Plan-Ask", "Think", "Plan", "Ask"]
sources: ["hu-2026-proactive"]
---
# Think-Plan-Ask (TPA)

> A multi-agent architecture that separates *which unconfirmed axis to
> target* from *how to phrase the question*, so the selection step is an
> explicit, inspectable reasoning chain rather than something the question
> generator does implicitly.

## Definition / Mechanism

TPA is a proactive multi-agent dialogue framework for structured clinical
interviewing: a doctor agent explicitly reasons about which of a fixed set
of traits remain unobserved before selecting a clinically grounded
questioning strategy and generating a targeted question.[^c1]

At every dialogue turn the TPA Selector runs three conditioned steps.
**Think** produces a reasoning chain over the current diagnostic state:
which confirmed traits imply co-occurring ones, and — critically — which
unconfirmed traits carry the highest diagnostic uncertainty, measured as
the [[entropy]] of a per-trait Beta belief distribution updated from detector
evidence each turn; the four highest-entropy undetected traits are
injected into the prompt so reasoning does not drift back to
already-confirmed traits. **Plan** selects one strategy from a fixed
six-element action set (e.g. open-ended, hypothetical, correction-inducing),
conditioned on the Think output, not on the raw dialogue history. **Ask**
generates the question conditioned on both the reasoning chain and the
chosen strategy, applying the strategy implicitly rather than naming it.[^c3]

Evaluated on 484 simulated episodes across 35 patients (Autism Diagnostic
Observation Schedule, Module 4), TPA outperformed six dialogue-planning
baselines — including tree-search and Bayesian-EIG methods — on every
primary metric, reaching 82.1% trait coverage against 65.5% for automated
replay of real clinician dialogue, a 16.6-point gain.[^c2]

The paper's own decomposition of that gain: TPA does not elicit more per
use of any single strategy. Real clinical dialogue puts 90% of turns into
one strategy (open-ended) regardless of what remains unconfirmed, and
plateaus after turn 10; TPA reallocates turns toward whichever strategy
targets the traits open-ended questioning fails to surface, driving the
coverage gain.[^c4]

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Clinical dialogue agents | TPA | exact — the paper's own abbreviation |
| Clinical dialogue agents | Think-Plan-Ask / Think, Plan, Ask | exact — the spelled-out cycle name |

## Why it matters

It is a working instance of the wiki's stall-2 question: *given several
still-open axes (here, unconfirmed diagnostic traits), which do you target
next, and how do you turn that choice into an actual question?* TPA answers
by separating axis-selection (Think, driven by per-axis uncertainty) from
phrasing (Ask), and reports the separation itself — not extra search depth
— as what beat search-heavy baselines.

## Transfer

| | |
|---|---|
| **Home field** | active learning / experiment design: rank candidate queries by a formal uncertainty or information functional over a modelled variable |
| **Here** | rank *traits* (axes of $W$) by the entropy of a per-trait Beta belief updated from an LLM trait detector's noisy calls, then hand the top ones to a second LLM step that picks a strategy, then a third that phrases the question |
| **What survives** | the ranking-by-uncertainty logic for choosing which axis to attend to next, and re-scoring it every turn as evidence arrives |
| **What does not** | any approximation guarantee — Plan and Ask are LLM generations conditioned on the ranking, not a scored selection over $W$; the Beta parameters come from a detector with unquantified error, so the entropy is an estimate on top of an estimate, not the closed-form quantity [[expected-information-gain]] or [[mutual-information]] are defined over |

## Limits

- Single study, one domain (ADOS-2 Module 4 autism assessment), one
  detector, evaluated against a **simulated** patient agent, not real
  patients — the 82.1%/65.5% gap is a comparison against automated replay
  of real clinician transcripts run through the same simulated-patient
  pipeline as TPA, not a live clinical trial.
- The claim that reallocation (not per-strategy skill) drives the gain is
  this paper's own post-hoc decomposition of its result, not an
  independent replication.
- No ablation isolating the Think step's contribution from Plan or Ask
  was found in the extract read for this note.

## Related

[[mutual-information]] · [[expected-information-gain]] · [[adaptive-submodularity]] · [[value-of-information]]

[^c1]: hu-2026-proactive — "Here we present TPA (Think, Plan, Ask), a proactive multi-agent dialogue framework applied to the language assessment component of the Autism Diagnostic Observation Schedule Module 4 (ADOS-2), in which a doctor agent explicitly reasons about which traits remain unobserved before selecting a clinically grounded strategy and generating a targeted question."
[^c2]: hu-2026-proactive — "Evaluated on 484 episodes from 35 patients, TPA outperforms six competitive dialogue planning baselines across all primary metrics, achieving 82.1% SLD trait coverage, 16.6% points higher than automated replay of real clinical dialogues conducted by trained clinicians (65.5%)"
[^c3]: hu-2026-proactive
[^c4]: hu-2026-proactive
