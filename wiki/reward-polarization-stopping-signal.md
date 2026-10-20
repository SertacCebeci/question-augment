---
description: "The share of RL rewards pushed to 0 or near 1 rises before a self-bootstrapped rubric run collapses, so it can flag over-bootstrapping one iteration before the task scores fall."
aliases: ["reward polarization", "score polarization", "extreme-score fraction"]
sources: ["doi-10-48550-arxiv-2606-01091"]
---
# Reward polarization as a stopping signal

Reward polarization is the fraction of reward values that sit at the extremes, defined in the paper as "the fraction of extreme scores at 0 or ≥0.99".[^p1] Because a rubric reward is the mean of 0/1 constraint judgments, a response that satisfies all or none of its constraints lands at an extreme, so the measure asks how much of a batch has stopped giving a middle-of-the-scale signal. This reading is my inference from the definition, not the authors' wording.

The paper uses the measure as an early-warning signal in a loop where each rubric generator is the policy trained on the previous step's rubrics (see [[bootstrap-rubric-generation]]). The authors read rising polarization as a symptom of "reward distortion": each step trains the next rubric generator on a policy that has already drifted, so surface-level exploitation compounds while task quality falls.[^p2] In the run on Qwen3-30B-A3B, polarization "remains low" in the selected regime, then crosses the stopping threshold at the third step, and the authors describe it as a "reliable leading indicator of over-bootstrap".[^p3]

The timing is the claim that matters. On the 30B model, polarization was low at the first and second steps (0.096 and 0.054), then crossed the threshold at the third step.[^p9] The authors say the signal picks up the onset one full iteration before performance collapse, at both the 30B and 14B scales.[^p4] The paper gives a rule rather than a single number: at step n, stop if Pn exceeds a threshold of max(0.15, 2·Pn−1).[^p5] The 14B pattern is reported in an appendix.[^p10]

The authors also relate the signal to the mechanism of the collapse: larger models make the failure modes "sharper and more diagnostic", including entropy collapse, reward polarization and gradient death.[^p6] Their bootstrap guidance pairs the polarization rule with an entropy check, "If min(entropy) < 0.70 within a step, the rubrics are too narrow".[^p7]

## Limits

- The rule's constants (the 0.15 floor and the factor of 2) are given without derivation in the parts of the paper read here. Whether the crossing point would move with different rubric sizes or base models was not shown.
- The early-warning evidence comes from two Qwen3 scales (30B-A3B and 14B). The paper's selected models "stop at BS-2 or BS-3", so in practice the rule is seen to fire once per run, at the step where the authors already chose to stop.[^p8]
- Polarization is a correlate of the collapse, not shown to cause it. The paper does not report whether it leads the entropy check, and no comparison between the two is given.
- High polarization on an easy benchmark could be honest, with most responses simply right or wrong. My inference, untested here: the signal does not by itself separate reward hacking from an easy task.
- The stopping rule is a rule for when to stop generating rubrics from the policy. It says nothing about what to do instead; the paper's remedy is to stop, not to repair the rubrics.

## Related

- [[bootstrap-rubric-generation]] — the self-generated rubric loop this signal is meant to stop
- [[rubric-difficulty-evolution]] — the opposite remedy for a saturated reward: add criteria mined from strong responses rather than stop
- [[gate-saturation-collapse]] — another collapse where the reward stops carrying gradient; the paper names gradient death among the same signatures

[^p1]: doi-10-48550-arxiv-2606-01091 — "tion of extreme scores at 0 or ≥0.99"
[^p2]: doi-10-48550-arxiv-2606-01091 — "reward distortion: each step trains the next"
[^p3]: doi-10-48550-arxiv-2606-01091 — "reliable leading indicator of over-bootstrap"
[^p4]: doi-10-48550-arxiv-2606-01091 — "the onset one full iteration before performance collapse at both scales, yielding a practical stopping"
[^p5]: doi-10-48550-arxiv-2606-01091 — "stop if Pn > τn"
[^p6]: doi-10-48550-arxiv-2606-01091 — "Larger models amplify both the benefits and the"
[^p7]: doi-10-48550-arxiv-2606-01091 — "Auxiliary: If min(entropy) < 0.70 within a step, the rubrics are too narrow"
[^p8]: doi-10-48550-arxiv-2606-01091 — "Final models stop at BS-2 or"
[^p9]: doi-10-48550-arxiv-2606-01091 — "lected regime (0.096 at BS-1, 0.054 at BS-2), then"
[^p10]: doi-10-48550-arxiv-2606-01091 — "The same pattern holds on 14B (Appendix I)"
