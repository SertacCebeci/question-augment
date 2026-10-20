---
description: "A conformal set over action samples plus a none-of-the-above option separates ambiguous tasks (ask a cheap question) from incapable policies (ask for costly intervention) from confident ones (act)."
aliases: ["act-ask-learn routing", "uncertainty-aware policy steering", "UPS", "set-content uncertainty routing"]
sources: ["arxiv-2602-22474"]
---
# Ambiguity versus incapability routing

A system that can ask has two different reasons to be unsure, and they call for different questions. The task may be underspecified, so more than one candidate fits what the user said. Or the system may be unable to do the task, so no candidate fits. Treating both as one "low confidence" scalar hides which one holds and what to do about it. Uncertainty-aware policy steering (UPS, Yuan, Wu and Bajcsy) reads the *content and size* of a calibrated prediction set to tell them apart and to pick a response.[^c1]

## Mechanism

A robot draws K action samples from a pre-trained policy. A world model imagines each outcome, and a vision-language model narrates it. A (K+1)-th option, "none of the above samples are correct", is added "to ensure the system can detect incapability".[^c2] The verifier then answers a multiple-choice question over these options. [[conformal-prediction]] calibrates its probabilities into a set that contains a correct option with probability at least 1 − ε.[^c3]

The routing rule reads the set:

- One sample, and "none" absent: execute confidently.[^c4]
- More than one element: the task is semantically ambiguous. The robot asks a natural-language clarification, the answer replaces the instruction, and the verify-and-clarify loop repeats until the set is a singleton.[^c5]
- Only "none": the policy is incapable on this task. The robot asks a human to correct a trajectory, and a residual policy is trained on those corrections.[^c6]

Because the set is built to be small, the robot asks questions only when it needs to. The nonconformity score takes a minimum over every verifier call in a task (sequence-level calibration, since later inputs depend on earlier steering decisions) and over all acceptable labels. The second minimum is conservative: it discourages the verifier from guessing unstated intent and pushes it to ask about all plausible choices.[^c7] This is the same sequence-level device as [[sequence-level-conformal-prediction]], applied here to a verifier.

## Why the split matters

The two resolutions have very different costs: language queries are cheap and low-level action interventions are expensive. Gating interventions on semantic task alignment, not on variance in the policy's actions, avoids asking for help "where low-level policy has noisy actions, but all result in good outcomes". Human-gated interactive imitation, by contrast, demands monitoring of every trajectory.[^c8] The paper reports a 30% improvement over uncalibrated policy steering in ambiguous scenarios, and a lower intervention rate than the ensemble-disagreement baseline (0.20 against 0.27 for EnsembleDAgger).[^c9]

The design extends [[knowno]], which asks when the conformal set is not a singleton but assumes the low-level policy can always execute the chosen plan. The none option is what adds the incapability branch. The rule also reads set size as ambiguity, as [[calibrated-interactive-resolution]] does. Here, set content (empty of real options) is a second signal beyond size.

After residual learning the action distribution shifts, so the verifier is recalibrated, which closes the loop.[^c10]

## Limits

- The three scenario types (straightforward, ambiguous, incapable) are built by the authors in manipulation tasks. Real situations may be both ambiguous and incapable at once, and the rule does not say which to resolve first (my observation).
- Coverage is calibrated against labels annotated by an end user and against an imagined-outcome pipeline (Dreamer-v3 world model plus Gemini narration). Errors in imagination are not separated from verifier error in what I read.
- The ambiguity branch assumes the user can answer a clarification truthfully. Noisy or inconsistent answers were not what was measured here.
- Experiments use one simulated task and a small number of hardware tasks, a diffusion base policy, and K samples. Whether the routing rule transfers to text-only askers is untested. The mapping "none-only set means incapable" depends on the candidate generator being a real sample of the capability distribution.
- Guarantees are marginal over calibration-like deployments, and they were not shown to survive distribution shift.

## Related

- [[knowno]] — the conformal ask-when-not-singleton rule this extends with an incapability branch
- [[conformal-prediction]] — the calibration used to size the sets
- [[sequence-level-conformal-prediction]] — the min-over-sequence score used for dependent calls
- [[calibrated-interactive-resolution]] — uses set size as the ambiguity gate for questions
- [[pact-ask-or-act]] — another ask-or-act decision rule

[^c1]: arxiv-2602-22474 — "selects an uncertainty resolution strategy: execute a highconfidence action, clarify task ambiguity via natural language"
[^c2]: arxiv-2602-22474 — "none of the above samples are correct” to ensure the"
[^c3]: arxiv-2602-22474 — "provably"
[^c4]: arxiv-2602-22474 — "then the steering system confidently executes this sequence of"
[^c5]: arxiv-2602-22474 — "the verifier has identified high-level"
[^c6]: arxiv-2602-22474 — "the VLM verifier detects that none of"
[^c7]: arxiv-2602-22474 — "incentivizes the verifier to ask the user about the entire"
[^c8]: arxiv-2602-22474 — "where low-level policy has noisy actions, but all result in good"
[^c9]: arxiv-2602-22474 — "we show 30% improvement in ambiguous scenarios"
[^c10]: arxiv-2602-22474 — "we recalibrate"
