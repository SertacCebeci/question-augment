---
description: "A model critiquing its own answer against a sampled written principle, then revising, repeatedly, cuts harm; the critique step beats direct revision, and principle count changes diversity, not score"
aliases: ["Constitutional AI", "critique-revision-supervised learning", "RLAIF constitution", "AI feedback against principles"]
sources: ["bai-2022", "arxiv-2512-07141"]
---
# Principle-guided critique and revision

In Constitutional AI the only human oversight on harmlessness is a short list of natural-language principles, the constitution, plus a few few-shot examples.[^c1] In the supervised stage a helpful-only assistant answers harmful prompts. The model then critiques its own response according to one principle and revises the response in light of the critique. The loop is repeated, drawing a principle at random from the constitution at each step. A pretrained model is finetuned on the final revisions.[^c2]

## What was measured

- **Critique before revision matters.** The authors report that generating critiques improves harmlessness compared with generating revisions directly.[^c3]
- **Repetition helps.** Harmlessness and combined helpful-harmless preference-model scores improve monotonically with the number of revisions, while pure helpfulness scores fall.[^c4] The authors caution that preference-model scores are less calibrated at high values, so the trend should be taken with a grain of salt.[^c5]
- **Number of principles changes diversity, not score.** Harmlessness score did not appear to depend significantly on how many principles were in the constitution. The authors expect more principles to give more diverse revisions, which would help exploration in the later RL phase, but did not study this quantitatively.[^c6]

## The same principles as a judge

In the RL stage the model is asked a multiple-choice question: which of two responses is better according to a constitutional principle. These AI labels are mixed with human helpfulness labels to train a preference model.[^c7] Chain-of-thought prompting ("Let's think step-by-step") improves the model's identification of harms.[^c8] But chain-of-thought answers state the choice outright, so the probability targets sit near 0 or 1 and are poorly calibrated. Clamping them to 40-60 percent gave better and more robust behaviour; without clamping, RL-CAI models learned to output more extreme responses.[^c9]

The point for questioning: the quality of the check depends on posing it against one concrete criterion at a time and having the model write out its reasoning, but a reasoned verdict is overconfident and needs its certainty damped before it is used as a signal. This reading is mine; the work states the clamping result only for its RL setup.

## The same loop with a written safety policy

A December 2025 vision-language paper reuses the loop with the policy kept in view at every step. After the model writes an initial reasoning and answer, the query and the safety policy go back into the model, which writes a reflection and a revised answer. The reflection "encourages the model to critically reassess the initial output" by referring to the policy.[^c11] The paper's measurement is a safe-response rate on jailbreak images, not a preference-model score. What it adds to this note is that the critique is run on the model's own written answer, which is the object the concept in self-revealed-output-signal is about. The paper attributes its gain to the policy only tentatively: the improvement "may stem from" the policy-guided framework.[^c12]

## Limits

- Everything is for harmlessness of a language-model assistant; nothing tests critique against a principle as a way to ask or answer questions in general.
- The "critique beats direct revision" result is cited here from the contributions summary; I did not read the Figure 7 numbers or effect size.
- Principles were "chosen in a fairly ad hoc and iterative way", so no claim is made that any particular principle matters.[^c10]
- Preference-model scores are the main evidence for the revision trend and are admitted to be poorly calibrated at high values.
- The effect of principle count on diversity is an expectation, not a measurement.
- The vision-language reuse does not isolate the policy: in the sections I read there is no run with the policy removed from the reflection prompt, so whether the written rule matters beyond a second pass is untested there (my reading).

## Related

- [[specific-actionable-self-feedback]] — the same critique-then-rewrite loop without a written principle; there specificity of the critique is what counts
- [[prompted-stopping-critic-robustness]] — a model-as-critic can be fooled, so its verdicts are not ground truth
- [[dimension-aware-reward-decomposition]] — splitting a reward by dimension, as helpful and harmless labels are split here
- [[returns-per-token-spent]] — gains per extra revision
- self-revealed-output-signal — the vision-language reflection step read for what the written draft itself contributes

[^c1]: bai-2022 — "human supervision will come entirely from a set of principles that should govern"
[^c2]: bai-2022 — "We then ask the model to critique its response according to a principle in"
[^c3]: bai-2022 — "Generating critiques improves harmlessness compared to simply"
[^c4]: bai-2022 — "We find that harmlessness and HH scores improve monotonically with respect to number of revisions"
[^c5]: bai-2022 — "scores become less calibrated at higher values, so these results should be taken with a grain of salt."
[^c6]: bai-2022 — "the number of constitutions does not appear to have a significant effect on harmlessness score."
[^c7]: bai-2022 — "We then formulate each prompt and pair into a multiple choice question,"
[^c8]: bai-2022 — "chain-of-thought reasoning improves this ability"
[^c9]: bai-2022 — "clamping the CoT probabilities to lie within the 40-60 percent range led to better"
[^c10]: bai-2022 — "These principles were chosen in a fairly ad hoc and iterative way for research purposes."
[^c11]: arxiv-2512-07141 — "encourages the model to critically reassess the initial output"
[^c12]: arxiv-2512-07141 — "This improvement may stem from"
