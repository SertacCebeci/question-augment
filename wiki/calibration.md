---
description: "When you say \"70% sure\", are you right 70% of the time? The silent A forecaster is calibrated $\\iff$ events assigned probability $p$ occur a fraction $p$ of the time."
aliases: ["calibrated probabilities", "probabilistic calibration", "reliability"]
sources: ["brier-1950", "dawid-1982", "murphy-1977", "naeini-2015", "xiong-2024", "kadavath-2022", "suri-2026", "arxiv-2512-24560", "arxiv-2512-22245", "doi-10-48550-arxiv-2609-26035", "arxiv-2512-11998", "doi-10-48550-arxiv-2608-26846", "arxiv-2512-08810", "doi-10-48550-arxiv-2610-02005", "doi-10-48550-arxiv-2609-04115", "arxiv-2511-16625"]
---
# Calibration

> When you say "70% sure", are you right 70% of the time? The silent
> precondition under every information measure.

## Definition

A forecaster is calibrated $\iff$ events assigned probability $p$ occur a[^s1][^s2][^s3][^s4][^s5][^s6][^s7]
fraction $p$ of the time. Dawid (1982) states the criterion in this form for
a forecaster assigning probabilities to a sequence of events, and proves that
a coherent Bayesian expects to be well calibrated — so calibration is not an
extra virtue a coherent agent may lack in its own eyes, only in the world's.

Three measures, each a different object from the property itself:

| Measure | Established by | What it is |
|---|---|---|
| Brier score | Brier (1950) | mean squared error of the probability against the 0/1 outcome; a proper scoring rule, so it mixes calibration with resolution — a calibrated forecaster can still score badly |
| reliability diagram | Murphy & Winkler (1977) assess operational forecasts this way | observed relative frequency plotted against forecast probability; the diagonal is calibration |
| expected calibration error (ECE) | Naeini, Cooper & Hauskrecht (2015) | bin the predictions, average $\lvert$accuracy $-$ confidence$\rvert$ over bins, weighted by bin size |

## Known as

| Field | Name there | Relation |
|---|---|---|
| statistics (Bayesian) | well-calibrated (Dawid, 1982) | exact |
| machine learning | calibrated probabilities | exact |
| forecast verification | reliability | close — it names the calibration component of the Brier decomposition, i.e. this property measured on one item set; not psychometric reliability (consistency of a measure across items or occasions) and not engineering reliability (probability of failure-free operation) |

**Not aliases.** *Expected calibration error* and *reliability diagram* are
measures of this property, not other names for it; two systems can share an
ECE and differ in where on the diagram they miss. *Brier score* scores
calibration and resolution together and so is not a measure of this property
alone.

## Why it is a precondition

Every mechanism in this wiki rests on probability estimates:

```text
Computing EIG          →  the answer distribution must be right
SPRT thresholds        →  the likelihood ratios must be right
"this axis is uncertain" →  the uncertainty estimate must be right
```

If the model is uncalibrated, all of it breaks. And there is a measured
problem: across five datasets and five models including GPT-4 and LLaMA-2
Chat, Xiong et al. (2024) find that LLMs "when verbalizing their confidence,
tend to be overconfident", and that the gap narrows but does not close as
capability scales. The direction is not universal: Kadavath et al. (2022)
report that larger models are well calibrated on multiple-choice and
true/false questions *given in the right format*, and lose that calibration
on new tasks — so overconfidence is a property of the elicitation and the
distribution, not of the model alone.

*Conjecture (this wiki's own inference, unmeasured):* overconfidence is the
mechanism behind a questioner that stops far too early — an overconfident
model measures less uncertainty than exists, so any threshold in
[[stopping-rules]] fires before $|W|$ is actually small. No study links a
measured ECE to a measured early-stopping rate in a clarification dialogue;
this is the inference, not a finding.

## Model uncertainty vs specification uncertainty

A critical distinction (Suri et al., 2026):

```text
MODEL UNCERTAINTY          the model does not know what to do
SPECIFICATION UNCERTAINTY  the user never said what they want
```

The second does not reduce to the first. A model can be 100% confident and the
specification still be missing — because the model made its own choice (a
*silent fork*). Calibration measures only the first.

## Transfer

| | |
|---|---|
| **In its home field** | forecast verification: a long run of repeated forecasts whose outcomes are resolved and scored (Brier, 1950; Murphy & Winkler, 1977). Calibration is a property of the *sequence*, computable only after the outcomes arrive. |
| **Here** | an agent's probability estimates over candidate answers or worlds inside one unresolved design dialogue — the answer distribution behind an EIG, the [[likelihood-ratio|likelihood ratio]] behind a stopping threshold. |
| **What survives** | the criterion and its machinery wherever a repeated, resolvable item set exists: benchmark suites, per-domain re-fits, logged dialogues whose intent was later confirmed. There ECE and the reliability diagram are computed exactly as at home. |
| **What does not** | measurability on a one-off question — a single design dialogue is a sequence of length one and has no calibration; and any inference from calibration to informativeness, since the base-rate predictor is perfectly calibrated and answers nothing. |

## Practical measurement

[[semantic-entropy]] is the applicable measure of model uncertainty.
Specification uncertainty needs a separate mechanism — likely
[[metamorphic-probes]] or generating multiple interpretations.

## Limits

- The transfer's own assumption: every number in this note was measured on
  item sets with resolved ground truth. Applying it to a live dialogue
  presumes such a set exists for that domain; where it does not, the note
  supports no claim about that agent's calibration.
- Xiong et al. (2024) measure *verbalized* confidence elicited by prompt.
  Overconfidence there does not license the same claim about a model's token
  logits or an internal posterior — a different quantity, differently
  measured.
- A calibrated model can be uninformative — predicting the base rate
  everywhere is perfectly calibrated. Calibration is necessary, never
  sufficient.
- The early-stopping mechanism above is this wiki's conjecture, cited to no
  measurement; treat it as a hypothesis to test, not a finding.
- ECE can read low without skill. Where a model's confidence collapses to the base rate, the work notes that "ECE can give misleadingly low values when the models suffer" bucket collapse, so it reports a skill score against the base-rate predictor beside ECE.[^s8] A low ECE alone does not show that the confidences carry information.
- Accuracy does not settle calibration. For LLM judges the paper reports that "not guarantee good calibration" follows from high accuracy, and that on an easy set "higher overall accuracy across models, leading verbalized confidence" to look better calibrated than it is. Calibration comparisons on easy data can therefore favour the overconfident method; the paper's own probe loses there, and wins on harder sets.[^s9][^s10]
- Fixed-anchor ECE can read as calibrated for a policy with no evidence sensitivity. In one measured layer, an always-assert arm had near-zero expression-ECE because its asserted content sat near 0.9 accuracy, which is the assert anchor. The paper notes that a degenerate all-assert policy scores as calibrated by anchor-based ECE whenever corpus accuracy sits near one anchor.[^s11] Discrimination over expressed categories is a separate check, and any single-category policy scores exactly 0.5 on it by construction.[^s12] Compare [[verifier-discrimination-and-calibration]], which separates AUC from ECE for the same kind of reason.
- The reference need not be accuracy. Where the stated confidence is compared with the model's own answer-token probability, the measure is alignment between two confidences, and a calibration score against correctness does not measure it. The work says its method "not focused on accuracy-based calibration", treating the internal number as "a reference signal".[^s13] See [[verbal-internal-confidence-alignment]].
- A numerical commitment threshold means a probability only for a calibrated
  score. In a replay that holds states fixed, the same 0.7 cutoff selects
  different states under raw and isotonic-calibrated confidence;
  [[monotone-recalibration-operating-point-shift]] has the mechanism.
  A map fitted at depth zero also decays as evidence accumulates: it improves
  held-out calibration through depths one and two, but at depth three the raw
  score is better for all three models tested.[^s14][^s15] The paper's own
  scope is two QA datasets and three models, one response collection each.

- A marginal guarantee can hold while confidence is miscalibrated within subsets of the items. For code LLMs, a calibrated model can be overconfident on complex tasks and underconfident on simple ones, and the study's answer is to condition the guarantee on groups ([[multicalibration]]).[^s16] Whether that conditioning helps outside function synthesis was not tested.

- A posterior is calibrated only as far as its model is right. The committee paper states its calibration property with a condition: if the prior and likelihood match the data-generating process, the confidence is calibrated in Dawid's sense. In practice the prior is fitted by cross-validation, which makes it, in the paper's words, "a one-parameter recalibrator, not a theorem."[^s17][^s18]
- A low calibration error can come from the recalibration step rather than the model. The paper reports that its supervised posterior is "the best-calibrated free aggregator (ECE 0.016)" on clean data, but when the baselines are granted the same labels, isotonic recalibration "collapses everyone" calibration error, so the gap is largely a matter of the recalibrator.[^s19][^s20]

- Calibration is a frequency property of a declared regime, not of one forecast in isolation. The paper says calibration "is a frequency property of the joint system generating forecasts and outcomes" and so depends on what is held fixed, which it calls the [[reference-structure|reference structure]].[^s21] Under a governing law, conditional-mean correctness gives a vanishing calibration gap only for a fixed, predeclared bin on the event of infinite visitation: "the same martingale structure does yield a calibration gap converging to zero on the event of infinite visitation." It does not guarantee visitation or uniform calibration: "Conditional-mean correctness does not guarantee visitation, unconditional calibration, or".[^s22][^s23] The separation from coherence is in [[coherence-frequency-role-separation]].

- A calibration gain can leave ranking where it was. In a clinical multiple-choice study, a layer of [[monte-carlo-dropout]] averaging, fitted temperature and an abstention gate "reduces expected calibration error by 0.23 to 0.33 absolute" on MedMCQA and MedQA-USMLE.[^s25] Its AURC was nonetheless "indistinguishable from the base model in three of four settings," and the authors read the gain as one to the confidence scale, not to the ordering of predictions by reliability.[^s26][^s24] The abstention rule itself adds nothing to the confidence it is given: the abstention-only variant is "identical to the base predictor, since abstention is a threshold policy applied to the underlying confidence."[^s27] Where safety does rise, it is paid for in coverage; at one threshold, "coverage at τ =0.7 falls from 0.541 to 0.100 on MedMCQA with" PubMedBERT.[^s28] A severity-weighted reading of the same errors is [[severity-weighted-calibration]].

## Related

[[coherence-frequency-role-separation]] · [[reference-structure]] · [[semantic-entropy]] · [[stopping-rules]] · [[maximum-entropy-principle]] · [[uncertainty-decomposition]] · [[calibration-training]] · [[hard-easy-effect]] · [[brier-calibration-probe]] · [[kuiper-statistic]] · [[verbal-internal-confidence-alignment]] · [[multicalibration]] · [[brier-skill-score]]

[^s1]: brier-1950
[^s2]: dawid-1982
[^s3]: murphy-1977
[^s4]: naeini-2015
[^s5]: xiong-2024
[^s6]: kadavath-2022
[^s7]: suri-2026
[^s8]: arxiv-2512-24560 — "ECE can give misleadingly low values when the models suffer"
[^s9]: arxiv-2512-22245 — "higher overall accuracy across models, leading verbalized confidence"
[^s10]: arxiv-2512-22245 — "not guarantee good calibration"
[^s11]: doi-10-48550-arxiv-2609-26035 — "anchor-based ECE whenever corpus accuracy sits near one anchor"
[^s12]: doi-10-48550-arxiv-2609-26035 — "Any single-category policy scores exactly 0.5 by construction"
[^s13]: arxiv-2512-11998 — "not focused on accuracy-based calibration"
[^s14]: doi-10-48550-arxiv-2608-26846 — "for raw confidence, the identical number is only a heuristic"
[^s15]: doi-10-48550-arxiv-2608-26846 — "but is worse than raw confidence at depth three for all three"
[^s16]: arxiv-2512-08810 — "systematically overconfident on complex tasks and underconfident on"
[^s17]: doi-10-48550-arxiv-2610-02005 — "match the data-generating process, the BDA confidence is"
[^s18]: doi-10-48550-arxiv-2610-02005 — "a one-parameter recalibrator, not a theorem"
[^s19]: doi-10-48550-arxiv-2610-02005 — "BDA per-agent is the best-calibrated free aggregator (ECE 0.016)"
[^s20]: doi-10-48550-arxiv-2610-02005 — "collapses everyone"
[^s21]: doi-10-48550-arxiv-2609-04115 — "It is a frequency property of the joint system generating forecasts and outcomes"
[^s22]: doi-10-48550-arxiv-2609-04115 — "the same martingale structure does yield a calibration gap converging to zero on the event of infinite visitation"
[^s23]: doi-10-48550-arxiv-2609-04115 — "Conditional-mean correctness does not guarantee visitation, unconditional calibration, or"
[^s24]: arxiv-2511-16625 — "The improvements above are to the confidence scale, not"
[^s25]: arxiv-2511-16625 — "by 0.23 to 0.33 absolute and drives harmful overconfident errors"
[^s26]: arxiv-2511-16625 — "indistinguishable from the base model in three of four settings"
[^s27]: arxiv-2511-16625 — "identical to the base predictor, since abstention is a threshold policy applied to the underlying confidence"
[^s28]: arxiv-2511-16625 — "coverage at τ =0.7 falls from 0.541 to 0.100 on MedMCQA with"
