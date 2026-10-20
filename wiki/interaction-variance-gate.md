---
description: "The spread, across a model's top-k candidate tokens, of an image-text interaction score marks decoding steps where the next word depends on the picture, and marks where hallucinations cluster."
aliases: ["interaction variance gate", "Cognitive Demand Sensor", "CDS gate", "Harsanyi interaction variance", "cross-modal synergy variance"]
sources: ["arxiv-2512-05546"]
---
# Interaction-variance gate

At each decoding step, the model's candidate next tokens are not all equally tied to the image. The gate asks how much the image and the text *jointly* move each candidate's logit, beyond what each input moves it alone. The paper takes this quantity from Harsanyi interactions and measures how much each modality contributes to the logit of a candidate token.[^c1] The four terms come from masking: the full input, the image alone, the text alone, and neither.[^c2]

The gate is the variance of these interaction values across the top-k candidates at that step. "High variance among the Iy interaction values for the top-k candidates" marks a step where the next word depends on visual cues.[^c3] When the next word follows from the text history, the candidates' interaction values "remain similar and the variance is low."[^c4] When the image separates candidates, as in telling a dog from a cat, "the interaction values diverge and the variance increases."[^c5] The gate fires when this variance exceeds a threshold κ, and the paper uses the firing to trigger a re-weighting of middle-layer attention toward image tokens.[^c6]

**What the formalism carries over.** Harsanyi's decomposition splits a joint value into single-player terms and an interaction term that is zero when the inputs do not interact. That survives the transfer as a bookkeeping device: a candidate whose logit changes only because image and text are present together shows a non-zero interaction. The paper calls the quantity "a gametheoretic quantity satisfying efficiency and symmetry axioms."[^c7] Those axioms belong to the game-theoretic setting, where the value of each coalition is a payoff. A decoder's logit for a masked input is not a payoff in that sense, so the axioms are inherited by name, not checked in the text read.

**What was measured.** On POPE with InstructBLIP, "nouns account for 52%" of gate triggers, against 17% for function words.[^c8] Hallucinations are reported three times likelier at triggered steps, at 24.2% against 8.1% without the trigger.[^c9] The paper reports POPE F1 gains of "1.5–7%" over the baselines, and reports that the entropy and margin gates it compares against "soften" the cost of static intervention "but still trail" its gate.[^c10][^c11][^c12] The gate fires on about half the tokens, a rate the authors call a balance between intervention frequency and runtime.[^c13]

## Limits

- The "visual indispensability" reading is the authors' interpretation: "High variance thus quantifies visual indispensability: it" is their claim, backed by the correlation above and by the attention traces, not by a separate test that the image is the cause.[^c14]
- The threshold is set per backbone. For InstructBLIP it was chosen on a "1,000-question POPE subset (see Appendix B)"; the κ sweep shows "a plateau" only "over [1.4, 2.2] where trigger rates stay between 28% and 48%", so the value is not shown to transfer.[^c15][^c16]
- The hallucination rates are conditional on the gate firing, which is a correlation. The gate's effect on accuracy is shown against a static intervention and two alternative gates, on one backbone for the ablation.
- Cost is not small: "Each condition requires its own forward pass" to evaluate the coalitions, so each step needs four passes before any attention intervention runs.[^c17]
- The gate needs residual disagreement between modalities. Under OPERA, which already flattens high-entropy logits, it fires on 19% of steps against 48% for InstructBLIP, and "it needs residual vision-text" disagreement that aggressive penalties can hide.[^c18]
- The masking baselines (zeroed image features, padded text) are out-of-distribution inputs. Whether the variance tracks visual evidence or an artefact of those inputs is not tested. (My inference.)
- Evaluated on POPE and CHAIR across four open backbones, with GPT-4o ratings for captions. It needs logit access and the ability to mask each modality, so it does not apply to closed systems. (My inference.)

## Related

- [[text-prior-over-visual-evidence]] — the failure this gate targets: the answer follows the language prior when the image should decide
- [[visual-forgetting-during-reasoning]] — the attention decline during generation that the gate is meant to catch at the step where it matters
- [[null-image-logit-subtraction]] — the same blank-image probe, used there to subtract a language prior rather than to isolate the image's share
- [[evidence-gain-hallucination-score]] — an answer-level image-ablation score; this gate works per token and compares candidates, not whole answers
- [[multi-signal-uncertainty-gate]] — a VLM gate on a weighted sum of uncertainty signals; this one reads cross-modal dependence instead
- [[confidence-triggered-visual-reattention]] — also re-looks at the image on a trigger, but the trigger is the model's own confidence, not interaction spread

[^c1]: arxiv-2512-05546 — "to quantify how much each modality contributes to the logit"
[^c2]: arxiv-2512-05546 — "terms through selective masking:"
[^c3]: arxiv-2512-05546 — "High variance among the Iy interaction values for the"
[^c4]: arxiv-2512-05546 — "remain similar and the variance is low."
[^c5]: arxiv-2512-05546 — "cat, the interaction values diverge and the variance increases."
[^c6]: arxiv-2512-05546 — "Conditioned on this signal, a Focused Consensus Induction"
[^c7]: arxiv-2512-05546 — "a gametheoretic quantity satisfying efficiency and symmetry axioms"
[^c8]: arxiv-2512-05546 — "nouns account for 52%"
[^c9]: arxiv-2512-05546 — "Hallucinations are three times likelier when"
[^c10]: arxiv-2512-05546 — "boosts grounding metrics (1.5–7% F1 gains on"
[^c11]: arxiv-2512-05546 — "Entropy/margin gates soften"
[^c12]: arxiv-2512-05546 — "this but still trail CG-VLM."
[^c13]: arxiv-2512-05546 — "The 48% trigger rate balances intervention"
[^c14]: arxiv-2512-05546 — "High variance thus quantifies visual indispensability: it"
[^c15]: arxiv-2512-05546 — "1,000-question POPE subset (see Appendix B)."
[^c16]: arxiv-2512-05546 — "over [1.4, 2.2] where trigger rates stay between 28% and 48%"
[^c17]: arxiv-2512-05546 — "Each condition requires its own forward pass"
[^c18]: arxiv-2512-05546 — "it needs residual vision-text"
