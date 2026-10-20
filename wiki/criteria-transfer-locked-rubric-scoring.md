---
description: "A frozen LLM judge scores more like humans when the rubric is compiled once into a locked spec, each score is tied to checkable evidence, and outputs are mapped to the human score distribution."
aliases: ["criteria transfer", "RULERS", "rubric execution drift", "evidence-grounded rubric scoring"]
sources: ["arxiv-2601-08654"]
---
# Criteria transfer: locked-rubric, evidence-grounded scoring

The work treats a human rubric as a latent scoring structure, not a prompt, and asks how to transfer its intent to a frozen LLM judge. It names three failure modes: rubric execution drift (the rubric is reinterpreted at each call, so definitions vary with phrasing, criterion order or backbone), unverifiable score attribution (rationales not checkable against the text), and human-scale misalignment (raw scores do not match the human score distribution).[^c1]

## Mechanism

The protocol, called RULERS, has three phases, none of which updates the judge.

1. **Lock.** The raw rubric is converted once into a task-level bundle (a structured, reusable specification), so the judge no longer reinterprets criteria at runtime.[^c2]
2. **Evidence-grounded execution.** Each checklist item returns extractive evidence, and the evidence is checked mechanically against an operator-specific rule for that checklist type. A verifier sets grounding to 1 or 0.[^c3] Checklist decisions, trait scores and uncertainty flags pass on as structured signals.
3. **Distribution alignment.** A second-order ridge regression fitted on a labeled calibration set gives a latent score, which a monotone mapping between the empirical CDFs of latent scores and human scores turns into a human-scale integer. After fitting, both are frozen.[^c4]

## What was measured

On four rubric-governed benchmarks (ASAP 2.0 essays, SummHF summaries, DREsS EFL writing, WebNLG), the authors report stronger agreement with human scores (QWK) in most settings and not on all: on SummHF it was not the best method with some backbones.[^c5]

Ablation with GPT-4o-mini removed one phase at a time. QWK, full versus without locking, without evidence, without alignment: ASAP 2.0 0.7077 / 0.6766 / 0.6833 / 0.6569; WebNLG 0.6135 / 0.5476 / 0.5613 / 0.5040; SummHF 0.3984 / 0.3405 / 0.3737 / 0.3404; DREsS 0.5292 / 0.5055 / 0.5088 / 0.4912.[^c6] Every ablation lowered QWK in every dataset, and no single phase accounts for the whole gain.

**Calibration control.** The same ridge plus monotone alignment was applied to baseline outputs. It raised QWK but did not consistently reproduce RULERS' gains, so calibration works best when the upstream signals are already structured, rubric-grounded and informative.[^c7] About 100 labeled calibration examples already gave strong performance in many settings, and 200 added moderate gains.[^c8]

**Robustness.** Under semantically equivalent rubric perturbations RULERS was more stable. The gap was smaller for simple, low-dimensional rubrics such as WebNLG.[^c9]

## Why it matters for asking and answering

The result separates three things a judge prompt usually fuses: fixing what is asked (the criterion), requiring that the answer point to checkable support, and translating the answer onto the scale the asker actually uses. My reading, not the paper's: a vague criterion is a source of answer variance that more careful answering cannot remove, only a fixed question can.

## Limits

- The bundle is induced from the source rubric; if that rubric is ambiguous or misaligned with the intended standard, the bundle may preserve the ambiguity.[^c10]
- Phase III needs labeled human scores per task and scale; the protocol is task-level and does not transfer across tasks without refitting.
- Ablation uses one backbone (GPT-4o-mini); several ablation SEs (0.02 to 0.06) overlap the differences on SummHF, DREsS and ASAP 2.0, so individual gaps are weak evidence.
- It uses more tokens than single-pass scoring, because it returns checklists, evidence and signals.
- Evidence verification is mechanical only "when possible"; faithfulness of evidence to the actual reason for the score is not shown.
- Quote-level support covers only the claims footnoted; per-backbone tables were not read in full.

## Related

- [[llm-judge-biases]] — the drift and bias that locking and calibration are meant to contain
- [[recursive-rubric-decomposition]] — decomposing criteria, one ingredient of the locked bundle
- [[rubric-formation-gap]] — the quality of the source rubric bounds what can be transferred
- [[evidence-verified-identification]] — checking a claimed evidence span before accepting a conclusion

[^c1]: arxiv-2601-08654 — "rubric execution drift occurs"
[^c2]: arxiv-2601-08654 — "reducing runtime reinterpretation of criteria."
[^c3]: arxiv-2601-08654 — "We verify grounding by setting Vτ (e, Ux ) = 1 when the returned evidence e"
[^c4]: arxiv-2601-08654 — "After fitting, both the ridge"
[^c5]: arxiv-2601-08654 — "RULERS is not the best-performing"
[^c6]: arxiv-2601-08654 — "The ablation results indicate that all three phases"
[^c7]: arxiv-2601-08654 — "does not consistently reproduce the gains"
[^c8]: arxiv-2601-08654 — "provides additional but generally moderate gains."
[^c9]: arxiv-2601-08654 — "The robustness gap is smaller for settings with simple, low-dimensional rubrics"
[^c10]: arxiv-2601-08654 — "with the intended scoring standard, the induced bundle may preserve these ambiguities."
