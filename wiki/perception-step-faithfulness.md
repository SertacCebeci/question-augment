---
description: "Scoring each perception step of a reasoning chain against the image gives a rate that can diverge from final-answer accuracy, so a correct answer can rest on ungrounded visual claims."
aliases: ["unfaithful perception rate", "UPR", "visual faithfulness of reasoning chains", "step-level visual faithfulness"]
sources: ["arxiv-2512-12218"]
---
# Perception-step faithfulness

A reasoning chain from a vision-language model mixes two kinds of step. A perception step reads something off the image; a reasoning step operates on facts already stated: "reasoning steps (operating over previously inferred facts)".[^c17] Only the first kind makes a claim the image can check, so the measure is defined for perception steps alone. A perception step is Unfaithful "if it introduces hallucinated or incorrect visual details"; the rest of the chain is not scored for visual faithfulness.[^c1]

The measure is a rate. The Unfaithful Perception Rate is "simply the fraction of" perception steps that are unfaithful, computed over a dataset.[^c2] The chain is first segmented, with "the judge is tasked with segmenting the chain into individual steps" and each step labelled as perception or reasoning.[^c16] The labels come from an off-the-shelf VLM judge, which is first asked for a "detailed description of the image I prior to annotation", so that each step is checked against the image rather than against the judge's priors.[^c3]

The reason to score steps is that the final answer does not carry the information. The authors put it directly: "Standard evaluations that only measure final-answer accuracy cannot distinguish these behaviors."[^c4] The two behaviors are a correct answer reached through "visually unfaithful intermediate steps"[^c5] and a faithful chain that ends in a wrong answer. The mechanism they point to is a shortcut around the chain: a model can map its hidden features to the answer "via spurious correlations or language priors, bypassing R", so the chain's accuracy does not certify its steps.[^c6] Errors also travel: "steps can propagate through the chain and contaminate subsequent reasoning."[^c7] A perception error early in a chain is therefore not only one wrong claim; it conditions what follows.

The judge is itself a measured instrument. Against two human annotators on 300 samples, ICC(3,1) was computed for several judges, and "Claude Sonnet 4 achieves the highest" agreement.[^c8] The samples were "VLM generations (acquired from a 7B reasoning model) are annotated both automatically and manually", so the calibration is for one generator.[^c14] The authors read the agreement as showing that the metric "highly correlates with human judgments of faithfulness."[^c9] A more elaborate prompt did not help: "increasingly complex prompts (Grounding + Rationales) may worsen correlation."[^c10]

## Limits

- The work's claim is that the final-answer metrics "do not determine whether" intermediate steps are grounded.[^c11] That is shown on four 7B reasoning-trained models and three perception benchmarks (MMEval-Pro, MMVP, HallusionBench). It is not a rate of unfaithful correct answers across tasks; the note does not claim one.
- Scope is narrow by the authors' own account: "reasoning tasks; generalizing to broader settings" is left open.[^c12] Visual faithfulness is defined only where there is an image; for text-only chains the analogue would be a different check, which the work does not provide (my inference).
- The judge is a VLM. The method "relies on a strong external VLM", and the authors say so as a limit.[^c13] A judge that shares the model's blind spots would miss the same hallucinations. This is my inference; the work does not test it.
- The rate's denominator is perception steps only. A chain with few perception steps gives a noisy rate, and the text does not report per-chain counts (my inference).
- The same judge labels both the baseline and any corrected chain. An improvement in the rate after an intervention is therefore measured by the instrument that the intervention was built to satisfy. The work's accuracy gains are the check that is independent of the judge; the rate gains are not (my inference).
- The labels are agreement with a judge, validated on a small sample, not with image ground truth. "Faithful" means "consistent with what the judge reads in the image."
- Whether the unfaithful steps cause the wrong answers, or merely co-occur with them, is not established by the rate alone.

## Related

- [[grounding-answer-dual-axis-audit]] — crosses answer correctness with crop-based localization; the measure here labels the claims a chain makes, not where the model looked
- [[cot-hallucination-trap]] — fluent rationales that drift from the image; the trap is one mechanism that would produce unfaithful perception steps
- [[cot-judge-detection-localization-gap]] — judges flag a broken chain without naming the step, which a per-step measure would need to do
- [[process-outcome-consistency-verification]] — checks a derivation against its outcome in text; this checks perception claims against the image
- [[accuracy-masks-unstable-reasoning]] — another correction to accuracy as the only outcome measure

[^c1]: arxiv-2512-12218 — "Unfaithful if it introduces hallucinated or incorrect visual details"
[^c2]: arxiv-2512-12218 — "which is simply the fraction of"
[^c3]: arxiv-2512-12218 — "detailed description of the image I prior to annotation."
[^c4]: arxiv-2512-12218 — "Standard evaluations that only measure final-answer accuracy cannot distinguish these behaviors"
[^c5]: arxiv-2512-12218 — "models may reach correct answers via visually unfaithful intermediate steps"
[^c6]: arxiv-2512-12218 — "via spurious correlations or language priors, bypassing R"
[^c7]: arxiv-2512-12218 — "steps can propagate through the chain and contaminate subsequent reasoning"
[^c8]: arxiv-2512-12218 — "Claude Sonnet 4 achieves the highest"
[^c9]: arxiv-2512-12218 — "which demonstrates that our metric highly correlates with human judgments of faithfulness"
[^c10]: arxiv-2512-12218 — "increasingly complex prompts (Grounding + Rationales) may worsen correlation"
[^c11]: arxiv-2512-12218 — "we show that such metrics do not determine whether"
[^c12]: arxiv-2512-12218 — "reasoning tasks; generalizing to broader settings"
[^c13]: arxiv-2512-12218 — "approach relies on a strong external VLM"
[^c14]: arxiv-2512-12218 — "(acquired from a 7B reasoning model) are annotated both automatically"
[^c16]: arxiv-2512-12218 — "the judge is tasked with segmenting the chain into individual steps"
[^c17]: arxiv-2512-12218 — "reasoning steps (operating over previously inferred facts)"
