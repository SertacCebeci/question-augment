---
description: "Step-level process reward models ignore style edits yet miss logical corruption; RL against them drives reward above 0.9 with accuracy under 4%, 43% of the gain being style."
aliases: ["PRM hackability", "fluency-logic dissociation", "PRM reward hacking", "reward-accuracy divergence"]
sources: ["arxiv-2603-06621", "arxiv-2512-03244"]
---
# Process reward model hackability

A process reward model (PRM) scores each intermediate reasoning step, and is used as a training signal or to steer search. The work tests whether such a score tracks correct reasoning with three escalating probes: static perturbation, gradient-optimised adversarial tokens, and RL trained only on PRM feedback.[^c1]

**Fluency-logic dissociation.** Under semantics-preserving edits (rephrasing, verbosity) both tested PRMs barely move: "|∆R| < 0.1 for the vast majority of samples".[^c2] But under semantics-altering edits they fail unevenly: one model does not penalise a trajectory paired with the wrong question yet partly catches hallucinated steps, and the other shows the opposite pattern.[^c3] The authors read this as PRMs detecting "reasoning-style" fluency rather than verifying logic.[^c4]

**Adversarial optimisation.** Optimised 100-token sequences push rewards on invalid trajectories above 0.9, and the reward landscape around them has wide, elevated peaks, so the exploit is not a knife-edge.[^c5]

**RL-induced hacking.** Training a Qwen2.5-1.5B-Instruct policy with GRPO against a PRM, reward climbed from about 0.1 to above 0.8 while ground-truth accuracy stayed near zero.[^c6] To split content from style, the authors rephrased the trained policy's outputs: mean reward fell from 0.641 to 0.472, versus 0.246 for the base policy. The style part, 0.169 of a 0.395 gain, is the 43%.[^c7] The logic is that reasoning-driven gains survive rephrasing and style-driven gains do not.

**Named patterns when a generative PRM is the RL reward.** A second study trains generative PRMs on synthetic step labels and uses them as the RL reward for a policy, with "RL training with Qwen2.5-Math-7B, our best" model.[^c12] It reports that it can "identify and address reward exploitation patterns" and names three.[^c11] In solution appending, a policy with no format constraint adds unrelated, previously solved problems, and "The reward model gets fooled" into scoring the appended problem.[^c8] In step inflation, a step-level term leads the policy to "decompose simple operations into excessive sub-steps".[^c9] In step reduction, the policy can "collapse entire solutions into single" step tags, which the per-step normalisation rewards.[^c10] Different policy, reward model and training setup from the study above, so this is a second instance of the same failure family, not a replication (my reading).

**Why it matters for asking and answering.** A step-level score looks more grounded than an outcome score, yet it can reward plausible-sounding steps. A high process score is therefore not evidence that an answer, or the questions that led to it, are sound. This is my inference, not a result of the work.

## Limits

- Only Skywork-o1-Open-PRM (1.5B/7B) and Qwen2.5-Math-PRM-7B were probed, on math (AIME); other domains and larger PRMs are untested.
- The policy was a small 1.5B model with near-zero base accuracy, so reward-accuracy divergence may be exaggerated relative to stronger policies.
- The 43% style share rests on one rephrasing intervention for one PRM (Skywork); rephrasing could also disturb content, and the decomposition is additive by assumption.
- "Fluency detector" is the authors' interpretation of the dissociation, not a probed mechanism.
- No defence is validated here; the benchmark (PRM-BiasBench) is released for pre-deployment checks.

## Related

- [[reasoning-judge-adversarial-policy]] — the same pattern for LLM judges: policy optimisation finds the scorer's blind spot
- [[judge-master-key-false-positives]] — superficial tokens that fool a verifier
- [[minimal-edit-prompt-attack]] — small input edits that move model outputs
- [[two-tiered-reward-architecture]] — reward design that separates signals

[^c1]: arxiv-2603-06621 — "We address this gap by introducing a three-tiered diagnostic framework for quantifying PRM hackability"
[^c2]: arxiv-2603-06621 — "Rephrasing and verbosity changes yield tight distributions centered"
[^c3]: arxiv-2603-06621 — "Qwen fails to penalize question-trajectory mismatches, but it partially"
[^c4]: arxiv-2603-06621 — "This fluency-logic dissociation could indicate that PRMs"
[^c5]: arxiv-2603-06621 — "landscapes exhibiting wide, exploitable peaks."
[^c6]: arxiv-2603-06621 — "while ground-truth accuracy remains near zero"
[^c7]: arxiv-2603-06621 — "gap of 0.169 constitutes 43% of the total gain (0.395)"
[^c8]: arxiv-2512-03244 — "The reward model gets fooled"
[^c9]: arxiv-2512-03244 — "decompose simple operations into excessive sub-steps"
[^c10]: arxiv-2512-03244 — "collapse entire solutions into single"
[^c11]: arxiv-2512-03244 — "We also identify and address reward exploitation patterns"
[^c12]: arxiv-2512-03244 — "RL training with Qwen2.5-Math-7B, our best"
