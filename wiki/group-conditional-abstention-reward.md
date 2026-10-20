---
description: "Rewarding 'I don't know' only when no rollout in a group is correct, and switching that bonus off during early exploration and for diverse groups, restores abstention without the always-IDK shortcut."
aliases: ["boundary-aware reward", "BAPO", "adaptive IDK reward modulator"]
sources: ["arxiv-2601-11037"]
---
# Group-conditional abstention reward

Outcome-only RL makes search agents answer everything. Chen et al.'s ReSearch-Qwen-7B-Instruct, trained with a correctness reward, raised accuracy to 51.25 but its IDK rate fell to 3.65%, with precision only 53.24; the untuned base model had admitted ignorance 18.75% of the time, with precision 50.76 against accuracy 41.25.[^c1] The paper reads this as weakened boundary awareness.

## Why a flat IDK bonus fails

The obvious fix, an extra 0.5 reward for IDK in groups with no correct answer, produced reward hacking: the model learned to default to IDK instead of attempting hard problems, and accuracy gains fell below the vanilla reward.[^c2] The authors frame it as exploration for correctness against exploitation of the IDK reward.[^c3]

## The mechanism (BAPO)

1. **Group-conditional bonus.** A question is treated as beyond the model's boundary if no rollout among the group gets a correct answer. Only then does an IDK rollout get +0.5, and the total is correctness plus this bonus.[^c4] The boundary is therefore estimated per question from the policy's own sampled group, not from labels about answerability.
2. **Stage-level modulation.** During early exploration the bonus is off, and switches on only if the IDK share falls below a threshold α. After the validation score plateaus (e.g., 5 consecutive steps) it applies fully, and groups with no correct rollout are resampled up to k times until an IDK or a correct answer appears.[^c5]
3. **Sample-level modulation.** Rollout diversity serves as a confidence proxy. If a query's rollouts give at least G/2 distinct answers the model is still exploring, so the bonus is deactivated; with low diversity (converged) it is applied.[^c6]

The reliability metric used interpolates between precision and accuracy by IDK rate, so lazy abstention is penalized: reliability = (1 − ρIDK)·prec + ρIDK·acc.[^c7] Reported hyperparameters: α = 5%.[^c8]

## Relation to what the wiki already holds

The base-rate note shows the same shortcut arising from the data mix; here it arises from the reward schedule, and the cure is to make the abstention incentive conditional on the policy's own failure. My inference: the group-conditional rule is a within-training estimate of "unanswerable for me", which is why it avoids a fixed base rate, though the paper does not test this against varying question difficulty mixes.

## Limits

- Only the abstract-level and method sections were read for this note; benchmark gains were not checked here, and no numbers on final reliability are claimed.
- "No correct rollout" conflates truly unanswerable with merely hard-for-this-policy; with small G it also misclassifies answerable questions.
- Diversity as confidence is a proxy asserted, not validated here.
- Judge-based correctness (GPT-4) is the reward source; judge error leaks into the boundary.
- Single backbone family (Qwen2.5-7B) in the preliminary study.

## Related

- [[abstention-base-rate-sensitivity-in-rl]] — the same always-abstain collapse driven by data ratio
- [[accuracy-masks-selective-reliability]] — why accuracy alone hid the lost abstention
- [[zero-variance-group-waste]] — groups with no correct rollout are the zero-signal groups this reward repurposes
- [[abstention-option-uncertainty-inflation]] — another cost of giving a model an abstain option

[^c1]: arxiv-2601-11037 — "after RL training (ReSearch-Qwen-7B-Instruct), while accuracy improves to 51.25, IDK rate drops sharply to"
[^c2]: arxiv-2601-11037 — "directly incentivizing IDK responses leads to reward hacking: the"
[^c3]: arxiv-2601-11037 — "balancing the"
[^c4]: arxiv-2601-11037 — "RIDK = 0.5 · I(yi = IDK),"
[^c5]: arxiv-2601-11037 — "is determined by the stagnation of the validation"
[^c6]: arxiv-2601-11037 — "we adaptively modulate"
[^c7]: arxiv-2601-11037 — "reliability = (1 − ρIDK ) · prec + ρIDK · acc, (7)"
[^c8]: arxiv-2601-11037 — "threshold α as 5%"
