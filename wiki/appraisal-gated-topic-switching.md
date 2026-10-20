---
description: "A learned Appraisal Agent classifies the answerer's response in real time; that classification, not an entropy computation, gates whether the policy probes deeper or switches subtopic."
aliases: ["appraisal agent", "appraisal-gated dialogue policy", "dual hierarchical RL for inquisitive dialogue"]
sources: ["lin-2026-dual"]
---
# Appraisal-gated topic switching

> Instead of scoring the next axis by an [[entropy]] or [[mutual-information]]
> computation, a dedicated agent classifies whether the answer just given
> was evasive, incomplete or satisfactory, and that classification is what
> the policy conditions on to decide "probe deeper" or "move to the next
> subtopic."

## Definition / Mechanism

Lin, Deng, Wang & Yang model justice–attorney exchange as an MDP and split
it across two coupled RL agents. The Appraisal Agent treats the judgment of
the prior attorney response as its action, chosen from nine discretized
appraisal types (e.g. evasive, incomplete, satisfactory): "If the response
appears evasive, contradictory, or insufficiently detailed, the appraisal
agent flags the need for deeper inquiry." Its Q-network selects the
appraisal that maximizes the Q-value estimate for the current state, and
that one-hot appraisal is concatenated onto the dialogue state the second
agent, the Hierarchical Dialogue Agent, acts on — "guiding subsequent
decisions to probe further or shift to the next subtopic as needed."[^c1]

The two agents are separated deliberately so that response evaluation and
next-move planning are learned independently: "Separating response
appraisal and dialogue control into two specialized agents enables more
modular and interpretable decision-making. The Dialogue Agent focuses
exclusively on planning and generating inquisitive moves, while the
Appraisal Agent independently assesses whether the information obtained
justifies continued exploration."[^c2]

An ablation that removes the Appraisal Agent (collapsing to a single
policy conditioned on raw dialogue state) reduces performance most on the
Probing Effectiveness Score, the metric the full model wins by the widest
margin over baselines: "The appraisal agent contributes to the PES metric
the most, which is the metric where our method outperforms the baseline
the most." Across all four ablations (no appraisal agent, no succinct
reward, no novelty reward, no goal-relevance reward), "each omission
reduces at least one key metric relative to our full model, which yields
the highest overall score (4.34)."[^c3]

## Why it matters

Every criterion already on this stall for "which axis / when to move on" —
EIG, VoI, [[semantic-entropy|semantic entropy]], [[information-directed-sampling|information-directed sampling]] — scores the
*next question* from a distribution over possible answers, computed before
asking. This mechanism instead scores the *answer just received* through a
learned classifier and uses that classification, not a recomputed entropy
or information gain, as the trigger for continuing on the same axis versus
switching. It is a different, non-information-theoretic control signal for
the same stopping/switching decision on this stall.

## Limits

The claim rests on one domain (U.S. Supreme Court oral argument transcripts)
with a nine-type appraisal taxonomy built for that domain, trained offline
on a dataset the paper itself reports as noisy; the ablation isolates the
appraisal agent's contribution only on the paper's own four metrics (CS,
PS, OS, PES) against the paper's own baselines, not against an
information-theoretic switching rule. Whether a hand-built appraisal
taxonomy transfers to a domain without a comparably scripted response
structure is untested here.[^c4]

## Related

[[value-of-information]] · [[expected-information-gain]] · [[belief-state-gating-policy]] · [[information-gain-guarded-probing]]

[^c1]: lin-2026-dual — "If the response appears evasive, contradictory, or insufficiently detailed, the appraisal agent flags the need for deeper inquiry."
[^c2]: lin-2026-dual — "Separating response appraisal and dialogue control into two specialized agents enables more modular and interpretable decision-making. The Dialogue Agent focuses exclusively on planning and generating inquisitive moves, while the Appraisal Agent independently assesses whether the information obtained justifies continued exploration."
[^c3]: lin-2026-dual — "The appraisal agent contributes to the PES metric the most, which is the metric where our method outperforms the baseline the most."
[^c4]: lin-2026-dual — "Due to the quality issue of the Surpeme Court dataset, the finetuning methods are not efficient on the dataset"
