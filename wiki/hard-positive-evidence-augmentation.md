---
description: "Counters an answering agent's learned bias toward over-abstention by training it on sufficient evidence deliberately polluted with irrelevant noise documents."
aliases: ["hard-positive evidence augmentation", "hard-positive sample augmentation"]
sources: ["park-2026"]
---
# Hard-positive evidence augmentation

> When an agent is rewarded for correctly refusing to answer, it can learn
> to refuse too much. This trains the refusal boundary back out by forcing
> it to answer through noise, not just through clean sufficient evidence.

## Definition / Mechanism

In [[dac-cross-agent-abstention-reward|DAC]]'s training, a generator
rewarded for abstaining on insufficient evidence develops a "predictable
failure mode": over-[[abstention]], where "limited exposure to sufficient
evidence may cause it to learn an overly conservative verification
boundary and abstain even on evidence that is sufficient but imperfect."[^c1]

The fix: for every question-evidence pair $(Q,E)$ already labelled
sufficient ($s(Q,E)=1$), sample irrelevant or weakly related noise
evidence $E_N$ and train the generator on $E' = E \cup E_N$ instead of (or
alongside) $E$. "Since $E$ is already sufficient, the added noise preserves
answerability while making the input harder," pressuring the generator "to
expand its answerable region rather than accepting only clean sufficient
evidence." The paper frames this as a lightweight substitute for an
adversarial prover: rather than training an agent to generate hard
sufficient evidence, noise is injected directly.[^c2]

## Why it matters

This is the only mechanism DAC reports for keeping the cross-agent
[[savor-calibration-abstention-reward|abstention reward]] from collapsing into a policy that refuses everything —
without it, the stopping/answering judgment that prices the searcher's
reward degrades in exactly the direction that makes the whole scheme
useless (a generator that always abstains gives the searcher no signal
that distinguishes good retrieval from bad).

## Transfer

| | Home field (adversarial training / prover-verifier games) | Here (asking) |
|---|---|---|
| Formalism | an adversarial prover searches for inputs that push a verifier's boundary toward error (Kirchner et al. 2024, cited by the source as the model this augmentation approximates) | noise is injected directly into already-sufficient evidence instead of learning an adversarial searcher |
| What survives | the goal — pressure the boundary with hard cases so it does not collapse to a trivial rule | |
| What does not | the adversary itself: no agent learns to generate the hard cases here, so the augmentation only reaches the noise distribution it is given, not whatever the generator's true failure region turns out to be | |

## Limits

- Reported only as a component of DAC's own ablation on the same two QA
  benchmarks and Qwen backbones as the main method; no isolated measurement
  of how much over-abstention this alone removes is described in the slice
  read here.
- The noise documents are sampled, not adversarially generated; the paper
  itself notes that "in more complex settings where noise sampling is
  difficult, one could instead train an adversarial searcher" — i.e. the
  technique's own authors treat it as a stand-in, not the general solution.

## Related

[[dac-cross-agent-abstention-reward]] · [[abstention]] · [[awa-rl]]

[^c1]: park-2026 — "limited exposure to sufficient evidence may cause it to learn an overly conservative verification boundary and abstain even on evidence that is sufficient but imperfect."
[^c2]: park-2026 — "Since E is already sufficient, the added noise preserves answerability while making the input harder."
