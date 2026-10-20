---
description: "Stopping reasoning at an upper confidence threshold and a rising lower threshold, both calibrated with finite-sample risk control, turns a token budget into an interpretable error target."
aliases: ["Conformal Thinking", "risk-controlled adaptive reasoning", "two-threshold early exiting"]
sources: ["arxiv-2602-03814"]
---
# Dual-threshold risk-controlled early exit

Adaptive reasoning halts a model's chain when its confidence passes a threshold. That only converts the problem of choosing a token budget into choosing a threshold, and the threshold is harder to interpret than a budget.[^c1] Wang et al. instead let the user state an acceptable error rate and have a validation set derive the stopping rule from it.

## Mechanism

**Two thresholds.** The policy exits at the first step where the smoothed confidence is at or above an upper threshold or at or below a lower one.[^c2] The upper exit risks a false positive: the model is confident but wrong. The lower exit risks a false negative: stopping a chain that would later have answered correctly.[^c3]

**Losses.** The upper loss is the indicator of crossing the threshold times the indicator that the current answer is wrong. The lower loss is farsighted. It averages correctness over all present and future answers up to the budget T.[^c4] Separate efficiency losses measure the gap to the oracle stopping time; they do not depend on the threshold and only choose among feasible settings.[^c5]

**Lower threshold as schedule.** A static lower threshold fires only when confidence falls. The authors make it a parametric function of the step, so the model must show a regular rise in confidence to keep going.[^c6] Figure 2 contrasts an unsolvable instance, whose confidence fluctuates and is cut by the lower threshold, with a solvable one that crosses the upper.

**Calibration.** Validation risk is replaced by an upper-confidence-bound estimate (Bates et al.) with a finite-sample correction, so that P(R <= epsilon) >= 1 - delta over the draw of the validation set.[^c7] Among all signal and threshold pairs whose adjusted risk is within epsilon, the one with least efficiency loss is chosen; if none is feasible, the method returns none.[^c8] Choosing the best signal per epsilon forms an ensemble of signals.

**Joint selection.** The upper threshold is fixed first, then the schedule parameter, a decoupled procedure that is "with some loss of theoretical rigor".[^c9] The upper bound could be broken if the lower threshold exited more solvable than unsolvable instances, which the authors expect only under extreme shift.[^c10]

## What was measured

- Over 40 random splits with 50 validation examples, naive tuning's standard-deviation bands often cross the target line while the UCB correction keeps test risk below it.[^c11]
- Lower-threshold value depends on the mix. With mostly solvable questions (3:1) the upper threshold alone captures most savings; at 1:1 and 1:3 the upper-only curve stays near the full budget, because many runs never reach the confidence cutoff, and adding the lower threshold shifts the curve left at similar accuracy.[^c12]
- The best signal and the threshold needed for a given risk differ across signals, so no single method is most efficient at every risk level.[^c13]

## Limits

- The guarantee is for the upper threshold alone and for the lower given a fixed upper; the joint two-step procedure is not proved, and monotonicity of the risks in the parameters is assumed.[^c14]
- Losses are defined only for supervised classification tasks with a known answer, so open-ended questions are outside scope.
- The guarantee needs the validation and test distributions to match; the paper probes shift empirically only, and I did not read those ablations in detail.
- That the lower threshold helps on unsolvable-heavy sets is shown on constructed mixes of AIME and GPQA, not on natural distributions.

## Related

- [[conformal-prediction]] — the finite-sample calibration idea this builds on
- [[maxwise-conformal-stopping]] — conformal halting on a running uncertainty score; this note adds a lower, schedule-based side
- [[moderate-adaptive-reasoning-length]] — adaptive reasoning length as the goal being controlled
- [[selective-abstraction]] — stopping early as a form of declining to continue
- [[conformal-risk-control-selective-judging]] — risk control applied to another decision

[^c1]: arxiv-2602-03814 — "it only converts the problem of setting a token budget into setting a threshold."
[^c2]: arxiv-2602-03814 — "τ = min t ≥ 1 : s̃t ≥ λ+ ∨ s̃t ≤ λ−"
[^c3]: arxiv-2602-03814 — "false negative risk of thinking the current"
[^c4]: arxiv-2602-03814 — "Notice this loss, unlike the one for false positives above, is"
[^c5]: arxiv-2602-03814 — "not depend on the threshold parameter λ but rather be used"
[^c6]: arxiv-2602-03814 — "the model must demonstrate a regular increase in confidence"
[^c7]: arxiv-2602-03814 — "the UCB algorithm can return settings"
[^c8]: arxiv-2602-03814 — "This routine picks the most efficient hyperparameter configuration that does not exceed the risk target."
[^c9]: arxiv-2602-03814 — "though with some loss of theoretical rigor"
[^c10]: arxiv-2602-03814 — "The upper risk bound could be violated when the lower threshold"
[^c11]: arxiv-2602-03814 — "many individual runs exceed the target risk."
[^c12]: arxiv-2602-03814 — "yields a clear leftward shift at comparable"
[^c13]: arxiv-2602-03814 — "no single method is uniformly most efficient across"
[^c14]: arxiv-2602-03814 — "We assume that our risks are monotonic in c and λ+ ."
