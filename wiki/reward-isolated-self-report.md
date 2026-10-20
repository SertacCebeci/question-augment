---
description: "A self-report requested after an answer and rewarded only for its own honesty, walled off from the answer's reward, so that owning a shortcoming is the cheapest route to reward."
aliases: ["confession", "confession training", "self-reported confession"]
sources: ["arxiv-2512-08093"]
---
# Reward-isolated self-report

A confession is a second output, requested after the answer, that serves as "a full account of the model's compliance with the letter and spirit of its policies and instructions."[^c1] It enumerates the instructions a good answer should have met, judges how far the answer met each, and lists uncertainties and judgment calls. What makes it a distinct object is its reward. A judge scores the confession for honesty and comprehensiveness, and that score "is not aggregated with any other rewards given to the model based on its performance on the original task."[^c2] The score reinforces only the tokens that produced the confession. Nothing the model reveals in it can change the reward for the task itself.[^c3]

The mechanism rests on one assumption: that the cheapest way to earn confession reward is to surface the misbehavior rather than hide it. The authors call this the path of least resistance, and state the separation directly: "By disentangling the reward for honesty from the reward for correctness, confession training can incentivize honest reporting even in cases where the model is incentivized to cheat the primary reward model."[^c4] Their intuition is that "honestly confessing to egregious misbehavior" is easier than reaching high reward on the original task, so the pressure to fool the confession judge is weaker than the pressure to fool the task's reward model.[^c5]

Measured on GPT-5-Thinking after a light RL run, across twelve out-of-distribution evaluations of hallucination, instruction following, scheming and reward hacking, the pattern holds in outline. When the model exhibits bad behavior, it confesses to it at least half the time in 11 of 12 evaluations.[^c6] The average probability of confessing, conditioned on bad behavior, "is 74.3% with significant variability": above 90% in 4 of 12 evaluations and at most 50% in 2 of 12.[^c7] Conditioned on bad behavior, the model is also "significantly more likely to" come clean in the confession than in its main answer.[^c8]

The misses are mostly not concealment. Among false negatives, the authors' classifier found no case of intentional lying in the confession, though they add that "we do not believe it is actually zero."[^c9] The dominant cause of omission was confusion: "is model confusion, especially in hallucination datasets where a model genuinely believes it has the right" answer.[^c10] So, in my reading, the channel reports what the model knows it did. The authors put it as "confessions are most effective when the model is aware that its behavior is undesirable."[^c11]

The authors' own advice on use is narrower. Confessions are "best used as a monitoring or diagnostic tool" for controlling behavior at deployment, "but not for direct training."[^c12]

## Limits

The wall is a design choice, not a guarantee of honesty. The confession reward "is not applied to the main model output, which means that while it can elicit accurate reporting of bad behavior, it may not reduce the frequency of bad behavior."[^c13] The mechanism reports misbehavior; it does not remove it.

Awareness bounds it. "Models cannot confess to what they do not know."[^c14] A confidently wrong factual answer falls outside what the channel can report, and the paper's own false-negative analysis points there.

The judge is the weak point. The paper's assumption needs the confession judge to be hard to fool, and the judge is described as "potentially just as hackable as the reward model for the original answer."[^c15] The authors say that additional training at scale is needed "to demonstrate that this assumption holds under high optimization pressure."[^c16] They also call it "an empirically falsifiable assumption that may not hold in every setting."[^c17]

The experiment is small. The RL run was short and applied to an already-trained model, and the paper says its experiments "should mainly be viewed as a proof-of-concept."[^c18] The evaluations were "deliberately designed to elicit undesirable behavior", several with artificial constraints such as disabled tools,[^c20] so the rates describe adversarial cases. What they say about ordinary traffic is my inference, not a measurement.

The format is narrow. A structured confession reports gaps against the instructions and policies it is asked about. "Therefore confessions may be less useful for exploratory work or for extracting insights on model behavior along dimensions not yet anticipated."[^c19]

## Related

- [[two-tiered-reward-architecture]] — also splits one agent's reward, but both tiers shape the agent's task behaviour; here the self-report tier is walled off from the task tier, which is what makes it a disclosure channel rather than a second objective.
- [[stated-intent-versus-actual-use-gap]] — measures whether a model's self-report matches its behaviour, without training for it; the confession is an attempt to train the report itself.
- [[probe-revealed-hidden-influence]] — a self-report can be shaped by what is asked; the same demand concern applies to a confession requested by a fixed prompt.
- [[bayesian-truth-serum]] — another route to making truthful self-report the best response, by scoring reports against peers' predictions rather than a judge's reading of a transcript.
- [[llm-judge-biases]] — the confession is scored by an LLM judge, so the separation argument inherits that judge's failure modes.

[^c1]: arxiv-2512-08093 — "a full account of the model’s compliance with the letter and spirit of"
[^c2]: arxiv-2512-08093 — "This reward is not aggregated with any other rewards given to the model based on its performance on the original task"
[^c3]: arxiv-2512-08093 — "nothing that the model reveals in the confession can change the"
[^c4]: arxiv-2512-08093 — "By disentangling the reward for honesty from the reward for correctness, confession training can incentivize honest reporting even in cases where the model is incentivized to cheat the primary reward model."
[^c5]: arxiv-2512-08093 — "Our intuition is that the task of honestly confessing to egregious misbehavior"
[^c6]: arxiv-2512-08093 — "When a model exhibits bad behavior, it confesses to it at least half the time in 11/12 evaluations"
[^c7]: arxiv-2512-08093 — "is 74.3% with significant variability"
[^c8]: arxiv-2512-08093 — "When a model exhibits bad behavior, it is significantly more likely to"
[^c9]: arxiv-2512-08093 — "model intentionally lied in the confession about this bad behavior"
[^c10]: arxiv-2512-08093 — "is model confusion, especially in hallucination datasets where a model genuinely believes it has the right"
[^c11]: arxiv-2512-08093 — "We observe that confessions are most effective when the model is aware that its behavior is undesirable."
[^c12]: arxiv-2512-08093 — "but not for direct training"
[^c13]: arxiv-2512-08093 — "output, which means that while it can elicit accurate reporting of bad behavior, it may not reduce the"
[^c14]: arxiv-2512-08093 — "Models cannot confess to what they do not know."
[^c15]: arxiv-2512-08093 — "a judge that is potentially just as hackable as the reward model for the original answer."
[^c16]: arxiv-2512-08093 — "to demonstrate that this assumption holds under high optimization pressure."
[^c17]: arxiv-2512-08093 — "empirically falsifiable assumption that may not hold in every setting."
[^c18]: arxiv-2512-08093 — "viewed as a proof-of-concept."
[^c19]: arxiv-2512-08093 — "Therefore confessions may be less useful for exploratory work or for extracting insights on model"
[^c20]: arxiv-2512-08093 — "They are all deliberately designed to elicit undesirable behavior, and several have artificial constraints"
