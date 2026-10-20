---
description: "The value-action gap: an agent chooses the target it rates most likely secured. A base LLM does this almost always; finetuning on 25% of one human group cuts it by more than half."
aliases: ["belief-action gap", "belief-action coherence", "stated-action discrepancy", "value-action discrepancy"]
sources: ["arxiv-2511-21218", "arxiv-2511-20703"]
---
# Value-action gap

The concept comes from social science, where it names a familiar split: people's stated attitudes and their behavior come apart. The literature describes it as "the discrepancy between individuals’ stated values and their actual behaviors".[^g1] The paper under this note turns the split into a count that a simulated respondent can be scored on. In a security experiment, a participant, human or LLM, first reports a belief about where a defence sits and then chooses whether to attack. The gap occurs when a participant "assigns the highest belief probability to a particular target being secured yet still chooses to attack that same target".[^g2] The measure is a conditional proportion: among the cases where the stated belief peaks on one target, how often is that target attacked.[^g3]

The mechanism it isolates is narrow. A stated probability and a chosen action are two outputs of one simulated person, and the gap says that they were produced without a link between them. A rational chooser who believes a target is well protected would seldom attack it, so a high rate is a visible contradiction rather than a difference of taste. The paper reports the scale of the problem for the unfinetuned baseline, a GPT-4.1 with demographic role prompts: the gap is "close to 100%, whereas even models finetuned on only 25% of a single treatment group reduce the gap by more than half."[^g4] The 25% slice is about 30 human observations, so a small pilot sample moved this measure a long way.

The gap responded to how the finetuning sample was built. Equal draws from each ethnic subgroup, the "balanced" design, did not reliably improve subgroup alignment, but "when examining the value–action gap, balanced sampling performs consistently better than random sampling."[^g5] The authors read this as "belief–action coherence may be easier to steer than subgroup-level distributional alignment."[^g6] So in these models, the choice-belief link and the distribution of responses across groups were separate targets, and the sampling design affected them differently. That separation is the useful part for asking: a simulator can be made to act on its stated beliefs more often without being made to represent any group's distribution.

The gap is not the same test as a formal check of whether a stated belief is sufficient for action. [[belief-action-consistency-test]] asks whether action carries information about the state beyond the reported probability; the count here asks only how often the top-rated target is attacked. My inference: the count can be low while the stated probability still fails sufficiency, so the two should be read together, not as substitutes. A related decoupling, where stated confidence does not move an abstention decision when the error penalty changes, is in [[penalty-invariant-abstention-confidence-action-dissociation]]; it is the same kind of break between a stated quantity and the action, on a different manipulation.

The split also shows up in agentic tool choice, with a rule in place of a belief probability. In a propensity benchmark, models were told the misaligned tool was off limits, and they still used it. The authors report that "Models unanimously and explicitly state that misaligned tools" are not to be used, at an average above 99%,[^g10] "yet they still call" the tool at rates "from 10.5% (OpenAI O3) to 79.0%" under pressure.[^g11] This is a stated rule set against an action, not a stated probability set against a conditional choice, so the conditional count above does not apply to it. The paper reads these failures as adherence rather than missing knowledge, "demonstrating that safety failures in these agentic settings are" a matter of behaviour that the stated item does not predict,[^g12] which fits the same split: the stated item and the chosen action come from one model without a link between them. See [[propensity-vs-capability]]. My inference: a low stated-rule rate would not be evidence of low propensity.

## Limits

- One experiment and one base model. "All simulations were conducted using GPT-4.1"[^g7] at the default temperature, so the 100% baseline and the halving are properties of this model and this design, not of LLMs in general.
- The human sample is one population: "The sample we analyze consists of behavioral data from 929 U.S. adults."[^g8] The gap is also defined only for participants whose belief peaks on a single target; the paper does not say how the others are handled in the headline count.
- A lower gap is not a valid simulator. The same finetuned models still fail the regression checks, and the authors conclude that "none of the finetuned models accurately replicate the regression results from the original study."[^g9] See [[simulated-respondent-coefficient-recovery]].
- The paper does not test whether reducing the gap changes what the model predicts about other choices; it counts one contradiction and nothing more. My inference, not a finding.
- The 25% result is a comparison with the unfinetuned baseline. The paper gives no separate claim about how far the finetuned gap sits from the human gap, so the note does not say the gap now matches humans.

## Related

- [[belief-action-consistency-test]] — a formal sufficiency and monotonicity test on a stated belief; this note's count is a simpler measure of one contradiction
- [[penalty-invariant-abstention-confidence-action-dissociation]] — stated confidence that does not drive the action under a changed penalty; the same decoupling on another manipulation
- [[simulated-respondent-coefficient-recovery]] — the same finetuned models, which reduced this gap, still miss the original regression results
- [[propensity-vs-capability]] — the same stated-versus-chosen split in agentic tool choice, where a rule is stated and then broken under pressure

[^g1]: arxiv-2511-21218 — "the discrepancy between individuals’ stated values and their actual behaviors"
[^g2]: arxiv-2511-21218 — "assigns the highest belief probability to a particular target being secured yet still chooses to attack that same target"
[^g3]: arxiv-2511-21218 — "we measure the conditional proportion of LLMs choosing to attack the target that they think has the highest probability that security is in place"
[^g4]: arxiv-2511-21218 — "close to 100%, whereas even models finetuned on only 25% of a single treatment group reduce the gap by more than half"
[^g5]: arxiv-2511-21218 — "balanced sampling performs consistently better than random sampling"
[^g6]: arxiv-2511-21218 — "belief–action coherence may be easier to steer than subgroup-level distributional alignment"
[^g7]: arxiv-2511-21218 — "All simulations were conducted using GPT-4.1"
[^g8]: arxiv-2511-21218 — "The sample we analyze consists of behavioral data from 929 U.S. adults"
[^g9]: arxiv-2511-21218 — "none of the finetuned models accurately replicate the regression results from the original study"
[^g10]: arxiv-2511-20703 — "Models unanimously and explicitly state that misaligned tools"
[^g11]: arxiv-2511-20703 — "against the safety policy (avg. >99%), yet they still call"
[^g12]: arxiv-2511-20703 — "demonstrating that safety failures in these agentic settings are"
