---
description: "An RL reward term that prices each ordered exam by a tiered financial-cost-plus-patient-discomfort score, penalizing unnecessary investigation alongside a diagnosis-accuracy term."
aliases: ["Exam Cost Reward", "cost penalty"]
sources: ["gao-2026-medexagent"]
---
# Exam cost reward

> Not every question or test earns its keep: price each exam ordered by
> what it would cost and hurt a real patient, and subtract that from the
> diagnosis reward.

## Mechanism

Gao, Zhou, Li, Zhao & Liu (2026) score an
investigative action — an exam ordered as a tool call — on two axes:
financial cost, grounded in CMS fee schedules, and patient discomfort,
graded by an access-and-invasiveness taxonomy. Each axis is binned into
three ordinal tiers (Low=1, Medium=2, High=3); "we sum both types of costs
for all unnecessary exams and divide by 6, which is the maximum possible
cost value for a single exam," giving $R_{cost} \in [0,1]$. The total
episode reward is a weighted sum, $R = R_{dx} + w_{tool}R_{tool} -
w_{cost}R_{cost}$, combining a Jaccard-based diagnosis-accuracy term, a
tool-call-matching term, and the cost penalty.[^c1]

An ablation isolates the term's contribution: training with $w_{cost}=0$
while keeping $w_{tool}$ active still lets "the model... learn to call much
more unnecessary exams, potentially due to a tendency to hack the diagnosis
reward by gathering as much information as possible" — average tool calls
per case on DDxPlus rise from 3.75 (full reward) to 5.65 (no cost penalty).
The same ablation also degrades diagnostic accuracy itself (Sim drops from
0.953 to 0.846 on DDxPlus, and further on the harder PMC-Patients-v2 and
AgentClinic-MedQA sets) — removing the cost term does not trade accuracy for
cheaper investigation, it lets the policy over-collect and still diagnose
worse.[^c2]

## Known as

| Field | Name there | Match |
|---|---|---|
| This paper's main text | exam cost reward | exact |
| This paper's Equation 3 / ablation tables | cost penalty ($w_{cost}R_{cost}$) | exact — same reward term, two names used interchangeably by the authors |

## Transfer

| | |
|---|---|
| **In its home field** | [[value-of-information|Value of information]] weighs an action's expected decision-relevant gain against a generic cost before asking; the cost side is usually left abstract or unmodeled. |
| **Here** | The cost side is made concrete and grounded in external, non-epistemic scales — a CMS fee schedule and an invasiveness taxonomy — rather than derived from the model's own uncertainty. |
| **What survives** | Pricing an information-seeking action against a scalar cost and combining it with a task-reward term in one weighted objective. |
| **What does not** | No expected-value-of-information computation is made; the penalty is a flat tiered charge per exam ordered, not a function of how much the exam was expected to reduce diagnostic uncertainty. |

## Limits

- The tier assignments (financial and discomfort) are the authors' own
  three-point discretization of CMS schedules and one invasiveness
  taxonomy; a different binning could change what counts as "cheap."
- The ablation's accuracy drop is confounded with reward hacking specific
  to this paper's Jaccard-based $R_{dx}$; whether a cost term prevents
  over-collection in a differently-shaped diagnosis reward is not tested.
- Read from one 2026 preprint's archived text extract only ([?] unverified
  as of this draft); the weighting hyperparameters $w_{tool}, w_{cost}$ are
  referenced but not read here.

## Related

[[interactive-diagnosis-pomdp]] · [[value-of-information]] · [[sensitivity-weighted-question-score]] · [[information-gain-reward]]

[^c1]: gao-2026-medexagent — "we sum both types of costs for all unnecessary exams and divide by 6, which is the maximum possible cost value for a single exam."
[^c2]: gao-2026-medexagent — "when wcost is removed, even if wtool still places some constraints on excessive tool calls, the model still learns to call much more unnecessary exams, potentially due to a tendency to hack the diagnosis reward by gathering as much information as possible."
