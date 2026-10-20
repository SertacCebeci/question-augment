---
description: "An RL reward split into a dense per-turn process reward for questioning quality and a single terminal outcome reward for diagnostic correctness, with a safety veto that overrides the process score."
aliases: ["hierarchical reward mechanism"]
sources: ["lai-2025", "arxiv-2512-11930", "doi-10-48550-arxiv-2508-15746"]
---
# Two-tiered reward architecture

> Two separately-optimized reward signals for one agent — one scores how it
> asks, turn by turn; one scores whether it ends up right — so that a
> collapse in either skill cannot be papered over by the other.

## Mechanism

Lai et al. (2025) train Doctor-R1, a clinical-inquiry agent, with
GRPO in a multi-turn patient-simulation environment. Rather than a single
scalar reward, they split the signal into two tiers: a dense **process
reward** $R_\text{turn}$ after every turn, and a single terminal **outcome
reward** $R_\text{final}$ at the end of the dialogue. "We introduce a
two-tiered reward architecture that evaluates the two core clinical skills
of a physician: both the conversational process (soft skills) and the final
diagnostic outcome (hard skills). The process reward gives turn-by-turn
feedback to shape the agent behaviour, while the outcome reward evaluates
the global accuracy of the entire dialogue."[^c1]

The process reward scores eight dimensions of the turn (safety, reasoning,
medical accuracy, completeness, information gathering, faithfulness,
empathy/clarity, humility) as a weighted sum, but only after a
**hierarchical veto**. Any violation of safety, reasoning or accuracy
overrides the weighted score with a fixed large penalty: "any violation of
safety, reasoning, or accuracy triggers an immediate large negative reward,
overriding the standard score calculation. This veto system conceptually
aligned with shielded frameworks in Safe RL... ensuring that fundamental
clinical [[calibration|reliability]] is non-negotiable."[^c2]

Concretely $R_\text{turn}=-1.0$ if the safety score is below a threshold,
$-0.75$ if reasoning or accuracy is, and a weighted sum of the eight scores
otherwise. The outcome reward is discrete: $1.0$ for a correct final
diagnosis, $0.5$ for a partially correct one, $0.0$ otherwise, judged
against ground truth. The two tiers optimize different objects — the
process reward never sees whether the diagnosis was right, and the outcome
reward never scores how the questions were asked — so a policy cannot buy a
higher decision score by asking worse questions, or vice versa.

An ablation removing only the process reward ("w/o Proc. Reward") drops the
HealthBench average from 36.29 to 32.61 and the MAQuE task-success accuracy
from 60.00 to 52.00, while removing only the experience module ("w/o
Experience", a separate mechanism, see [[experience-repository]]) drops
HealthBench to 31.69 and MAQuE accuracy to 56.00.[^c3]

## Transfer

| | Safe RL (shielding) | Here |
|---|---|---|
| Home field | a shield layer blocks or overrides an unsafe action before it is taken | the veto overrides the *reward*, not the action itself, after the turn is generated |
| Survives | the hierarchical priority: a safety failure dominates every other score | same priority, applied to a scalar reward instead of an action space |
| Does not survive | the shield's hard guarantee of never executing the unsafe action | Doctor-R1's veto only penalizes after generation; it does not prevent the unsafe question from being sent |

## Limits

The decomposition and its weights ($\epsilon$, $w_i$) are chosen by the
authors, not derived from a theory of what a process/outcome split should
be; the ablation is intra-model (one architecture with a term removed), not
a comparison against other multi-objective reward designs. Evidence is one
paper, one domain (clinical dialogue), one base model family (Qwen3-8B);
generalization to non-medical question-asking agents is untested here.

## A second instance: a gate ahead of process and outcome

arxiv-2512-11930 builds the same shape for an AI tutor, and calls it "cascaded evaluation". A constraint gate runs first, and process and outcome terms are computed only for an action that passes: the gate, which "first verifies validity, pruning the action space before process and outcome" rewards are calculated.[^c4] When the gate fires, the reward is a fixed negative term in place of the weighted sum, the same replacement as the clinical veto above. The gate's first target is the Socratic rule itself, since it "which penalizes direct answer provision to" enforces guiding rather than telling.[^c6] The gate is scored by an LLM, as the process terms are.[^c9] The authors set the weights for safety, process and outcome to 5.0, 1.0 and 2.0.[^c5]

The process term is the one the paper ablates. Its "w/o PRM" variant reports Socratic Consistency of 30.20%, against 65.40% for the full model,[^c7] and the authors attribute the drop to credit assignment: "Without dense supervision, the agent suffers from the" credit assignment problem.[^c8] The gate itself is not ablated in the sections read, and every term is judged by an LLM, on one simulator and one base model, so the size of the gate's effect is not isolated.

## A third instance: the outcome term carries the process term

Deep-DxSearch, a retrieval-driven diagnostic agent, does not keep the two tiers apart. Its diagnostic reward is computed from the committed diagnosis and then adjusted by the evidence-acquisition reward, so that "This formulation explicitly links the final reward to the quality of the preceding evidence-gathering process."[^c10] The total is "a weighted sum of component rewards, gated by format" and then scaled by a trajectory-diversity term.[^c11]

The evidence term sees the ground truth. A retrieved case earns a bonus when "A positive reward (+0.5) is granted if a retrieved case matches the" correct diagnosis.[^c12] So the claim that the process signal "never sees whether the diagnosis was right" does not carry over: here the process signal is scored against the answer, and the separation the Mechanism section relies on is absent. The paper prices the coupling instead of forbidding it: "To promote efficiency, a penalty is applied for each" match, capped, so repeated matching cannot be free.[^c13]

The ablations place the weight on the process side. The largest drop is for the evidence-acquisition rewards: "rewards causes a sharp decline on accuracy (6.6% common, 10.9% rare)."[^c14] The diagnostic-accuracy ablation is the smaller one: "removing the diagnostic accuracy reward causes a further drop on" accuracy, of about 2–6%.[^c15] The authors read the first as showing "the retrieve-reason incentive is the most critical driver for navigating the complex search" space.[^c16] A multi-stage schedule that trained the evidence reward first gave, in their words, "in final diagnostic accuracy than focusing solely on the diagnostic outcome."[^c17]

What transfers is the placement: a process term can sit inside the outcome term rather than beside it, with the outcome term as the only thing the policy is finally judged on. What does not transfer is the clean separation. Limits: the passages read come from one paper and one agent family, the ablation drops are reported as single figures without spread in the passages read, and the reward weights were chosen by the authors through a staged schedule rather than derived (my inference from the schedule's description).

## Related

- [[experience-repository]]
- [[investigative-question-grpo-training]]
- [[preference-optimization-for-questions]]
- [[value-of-information]]

[^c1]: lai-2025 — "We introduce a two-tiered reward architecture that evaluates the two core clinical skills of a physician: both the conversational process (soft skills) and the final diagnostic outcome (hard skills). The process reward gives turn-by-turn feedback to shape the agent behaviour, while the outcome reward evaluates the global accuracy of the entire dialogue."
[^c2]: lai-2025
[^c3]: lai-2025
[^c4]: arxiv-2512-11930 — "first verifies validity, pruning the action space before process and outcome"
[^c5]: arxiv-2512-11930 — "The coefficients for our hierarchical reward"
[^c6]: arxiv-2512-11930 — "which penalizes direct answer provision to"
[^c7]: arxiv-2512-11930 — "Notably, the w/o PRM ablation (SC 30.20%)"
[^c8]: arxiv-2512-11930 — "Without dense supervision, the agent suffers from the"
[^c9]: arxiv-2512-11930 — "We employ an LLM-based verification to quantify penalties"
[^c10]: doi-10-48550-arxiv-2508-15746 — "This formulation explicitly links the final reward to the quality of the preceding evidence-gathering process."
[^c11]: doi-10-48550-arxiv-2508-15746 — "a weighted sum of component rewards, gated by format"
[^c12]: doi-10-48550-arxiv-2508-15746 — "A positive reward (+0.5) is granted if a retrieved case matches the"
[^c13]: doi-10-48550-arxiv-2508-15746 — "To promote efficiency, a penalty is applied for each"
[^c14]: doi-10-48550-arxiv-2508-15746 — "rewards causes a sharp decline on accuracy (6.6% common, 10.9% rare)"
[^c15]: doi-10-48550-arxiv-2508-15746 — "removing the diagnostic accuracy reward causes a further drop on"
[^c16]: doi-10-48550-arxiv-2508-15746 — "the retrieve-reason incentive is the most critical driver for navigating the complex search"
[^c17]: doi-10-48550-arxiv-2508-15746 — "in final diagnostic accuracy than focusing solely on the diagnostic outcome"
