---
description: "Critique-driven refinement gave the largest bias reduction but lost Urdu utility that best-of-N selection kept, so debiasing can trade semantic fit for stereotype score."
aliases: ["debiasing overcorrection", "oversmoothing under debiasing", "bias-utility trade-off in debiasing", "overcorrecting refinement"]
sources: ["arxiv-2512-09854"]
---
# Debiasing utility overcorrection

Debiasing an output can raise one score while lowering another. A mitigation is easy to judge by the bias score alone, but the two scores can move apart, and which one moves depends on the method. The work measures this for single-word completions from GPT-3.5 in English and Urdu. Each candidate is scored by a zero-shot judge, GPT-4o-mini, on two axes, bias and utility, both in [0,1]. The composite is "S = (1 − α) · bias + α · utility", with "α = 0.5."[^d1][^d2] In the figure caption, "Higher scores indicate lower stereotype presence."[^d3] A method can therefore lift the bias term and lower the utility term at once.

Two inference-time methods are compared against a one-shot baseline. PRM-Select "generates N = 8 completions, scores each, and selects the highest-scoring candidate."[^d4] PRM-Sequential "iteratively refines the baseline word based on PRM critiques, up to 5 rounds."[^d5] On the bias axis the sequential method wins: "Sequential refinement achieves the highest fairness scores."[^d6] On utility it does not. In Urdu, utility fell to 0.8825 under sequential refinement from 0.9825 under PRM-Select. The authors attribute the drop to overcorrection: "as PRM critiques tend to overcorrect, sometimes producing overly generic or abstract Urdu words."[^d7]

The drop is relative to selection, not to the baseline. Urdu utility was 0.85 at baseline, so the sequential word is still above the starting point on utility and only below the selected one. The comparison that matters is between methods, applied to the same prompts and the same judge.

The mechanism the authors give is that critiques push the output toward neutral vocabulary, and neutral vocabulary fits the sentence less well. Their wording: "Urdu utility sometimes decreases because refinement steps nudge GPT-3.5 toward overly neutral or generic words."[^d8] They read this as support for the view that "debiasing can oversmooth language representations."[^d9] This is an interpretation of score patterns. The text read does not inspect which words were chosen, so the mechanism is asserted rather than shown.

## What survives the transfer

The transferable part is the shape. A selection step chooses among samples that were produced without reference to the score. A refinement step conditions each new sample on the previous one and on a critique, so it can drift further from the start with each round. A critique that asks for less stereotype does not say how much fit to keep. The paper's own advice follows the shape: "Sequential refinement is preferable when maximal fairness is required, PRM-Select when consistency is a priority."[^d10] Read as a design rule, the choice of method decides which of the two terms gives way. That is my inference from the two arms, not a result the paper states.

The same shape appears in other settings. Iterative self-revision of a rice-yield explanation rose to a peak and then fell below its starting quality ([[refinement-quality-peak]]). Debiasing prompts that cut clean accuracy also cut helpful cues in a shortcut-learning setting ([[non-predictive-cue-training]]). These are different systems and different scores. The text does not show that they share a cause.

Best-of-N selection is also one of the test-time compute methods, where the choice of selection score decides whether extra samples help ([[test-time-scaling]]). Here the score is a bias-and-utility composite, so the selection step can only be as good as the composite it is given.

## Limits

- The composite fixes α at 0.5. The text reports no sweep over α, so whether the overcorrection survives a different weight is not tested. The text also does not say whether each refinement round keeps the composite-best word or simply the latest one. That detail changes the mechanism.
- The utility axis is itself a zero-shot judge score. The authors say "PRM zero-shot scoring may be inconsistent across contexts,"[^d11] and "No human annotator study was conducted."[^d12] Whether utility fell is what the judge reports.
- The paper says both methods "significantly reduce bias across languages,"[^d13] but the text read reports means without intervals or tests. The differences between methods are not shown to exceed run-to-run variation.
- The methods differ in cost: PRM-Select is "computationally cheaper,"[^d14] and sequential refinement runs up to five rounds. The comparison is not at matched model calls.
- English utility under sequential refinement is not given in the text read, so the overcorrection is shown only for Urdu.
- One dataset of 200 prompts with single-word completions. The authors note that "Single-word generation simplifies fairness but limits generalization."[^d15]

## Related

- [[refinement-quality-peak]] — iterative revision that rises and then falls; the same non-monotone shape, measured on explanation quality
- [[non-predictive-cue-training]] — debiasing that also removes helpful signals, in a shortcut-learning setting
- [[test-time-scaling]] — best-of-N and related selection rules; here the selection score is a bias-utility composite
- [[language-gap-under-mitigation]] — the English–Urdu gap in the same composite score, and how the two methods move it

[^d1]: arxiv-2512-09854 — "S = (1 − α) · bias + α · utility"
[^d2]: arxiv-2512-09854 — "with α = 0.5."
[^d3]: arxiv-2512-09854 — "Higher scores indicate lower stereotype presence."
[^d4]: arxiv-2512-09854 — "Generates N = 8 completions, scores each, and selects the highest-scoring candidate."
[^d5]: arxiv-2512-09854 — "Iteratively refines the baseline word based on PRM critiques, up to 5 rounds."
[^d6]: arxiv-2512-09854 — "Sequential refinement achieves the highest fairness scores."
[^d7]: arxiv-2512-09854 — "as PRM critiques tend to overcorrect, sometimes producing overly generic or abstract Urdu words"
[^d8]: arxiv-2512-09854 — "Urdu utility sometimes decreases because refinement steps nudge GPT-3.5 toward overly neutral or generic words."
[^d9]: arxiv-2512-09854 — "This supports critiques that debiasing can oversmooth language representations"
[^d10]: arxiv-2512-09854 — "Sequential refinement is preferable when maximal fairness is required, PRM-Select when consistency is a priority."
[^d11]: arxiv-2512-09854 — "PRM zero-shot scoring may be inconsistent across contexts."
[^d12]: arxiv-2512-09854 — "No human annotator study was conducted."
[^d13]: arxiv-2512-09854 — "Both PRM-Select and PRM-Sequential significantly reduce bias across languages"
[^d14]: arxiv-2512-09854 — "computationally cheaper"
[^d15]: arxiv-2512-09854 — "Single-word generation simplifies fairness but limits generalization."
