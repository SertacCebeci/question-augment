---
description: "Stop decisions are taken only at naturally occurring self-reflective tokens like 'hmm' and 'wait', where the model already revises its plan, not at every token or a fixed budget."
aliases: ["cue tokens", "reasoning cues", "self-reflective tokens", "natural decision points"]
sources: ["arxiv-2512-05325"]
---
# Reflective-cue decision points

A stop rule must say where it looks. One option is every token, which makes the rule expensive and gives it no reason to fire at one place rather than another. Another is a fixed budget, which ignores what the model is doing. LYNX takes a third option: the stop is considered only at a small set of tokens the model emits on its own, "hmm", "wait" and "alternatively". The stated reason is that such tokens mark "transitions between reasoning segments", for instance "switching from exploration to verification, or revising a previous plan".[^c1] Between cues, decoding proceeds as usual, and the probe is consulted only at cue positions: "These cue positions are the only places where LYNX considers early exit."[^c2]

**Mechanism.** At each cue the probe reads the hidden state and returns a probability that an exit there would be correct. A conformal threshold, calibrated once offline, decides whether to exit or continue. The abstract puts the frame in one sentence: "LYNX attaches exit decisions to naturally occurring reasoning cues".[^c3] The threshold is not a single number chosen by hand. The offline stage precomputes thresholds "for a grid of confidence levels", so that a user picks the operating point at deployment.[^c4]

The calibration uses only the cues where the forced exit was correct: "we compute nonconformity scores for correctly answered" cues.[^c5] The nonconformity score is one minus the probe probability, and the threshold is the (1 − δ) quantile of those scores. The rule therefore asks one question, how confident the probe is that exiting here is safe, and controls how often an exit is wrong: the construction "controls the fraction of incorrect early exits at approximately" δ.[^c6] Nothing in the rule penalises continuing when continuing was not needed; that side is left to the token count.

**What was measured.** The headline is about tokens and accuracy together: "On GSM8K, LYNX matches or improves baseline accuracy while reducing tokens by 40–65%".[^c7] The same operating rule is applied to the other benchmarks, with the confidence level as the only knob. The authors note that the level behaves monotonically: higher confidence gives more conservative exits.

**Contrast with neighbouring triggers.** [[in-stream-uncertainty-marker]] trains a token into the trace and emits it where the state looks unreliable; here the cue tokens are already in the model's vocabulary and nothing is trained into them. [[moderate-adaptive-reasoning-length]] uses a count of "wait" tokens as a trigger with a fixed threshold; LYNX uses the same kind of token but reads the hidden state there, and gates on a calibrated probe rather than on the count.

## Limits

- The cue set was chosen by hand. The authors list "learning latent decision points beyond hand-specified cues" as future work.[^c8]
- The method assumes explicit thinking segments and self-reflective tokens: "Models without such structure may require alternative trigger definitions."[^c9]
- The paper does not compare cue-restricted stops against stops at every token in the sections I read. The restriction is a design choice with a stated reason, not a measured advantage. My inference.
- Exchangeability is assumed. "strict exchangeability would require calibrating on a held-out portion of each test benchmark" [^c10], and LYNX instead calibrates once on math and reuses the threshold. The authors warn that "under strong domain shift the effective coverage may deviate from nominal levels."[^c11]
- The transfer to CommonsenseQA is reported zero-shot. The paper reads it as evidence of domain-general signals, but a cue set picked on math is not shown to be the right set for other domains. My inference.

## Related

- [[forced-exit-label]] — how the supervision at each cue is produced, by forcing an answer there
- [[in-stream-uncertainty-marker]] — a trained marker token, where these cues are natural and untrained
- [[moderate-adaptive-reasoning-length]] — a "wait"-count trigger with a fixed threshold
- [[implicit-stopping-knowledge]] — the claim that models know when to stop, which a cue probe reads out
- [[maxwise-conformal-stopping]] — a conformal halting threshold on a running score, with a finite-sample bound on early stops
- [[conformal-abstention]] — a related conformal rule with correctness conditioned on participating

[^c1]: arxiv-2512-05325 — "switching from exploration to verification"
[^c2]: arxiv-2512-05325 — "These cue positions are the only places where LYNX considers early exit."
[^c3]: arxiv-2512-05325 — "LYNX attaches exit decisions to naturally occurring reasoning cues"
[^c4]: arxiv-2512-05325 — "we precompute thresholds for a grid of confidence levels"
[^c5]: arxiv-2512-05325 — "we compute nonconformity scores for correctly answered"
[^c6]: arxiv-2512-05325 — "controls the fraction of incorrect early exits at approximately"
[^c7]: arxiv-2512-05325 — "reducing tokens by 40–65%"
[^c8]: arxiv-2512-05325 — "learning latent decision points beyond hand-specified cues"
[^c9]: arxiv-2512-05325 — "Models without such structure may require alternative trigger definitions."
[^c10]: arxiv-2512-05325 — "strict exchangeability would require calibrating on a held-out portion of each test benchmark"
[^c11]: arxiv-2512-05325 — "effective coverage may deviate from nominal levels"
