---
description: "A hierarchical GRPO variant that scores a multi-turn clarification trajectory separately at the trajectory, turn and step levels, using candidate-set entropy reduction to price each question."
aliases: ["Hi-GRPO", "Hierarchical Group Relative Policy Optimization"]
sources: ["yang-2026-guess"]
---
# Hi-GRPO

> A GRPO variant for training an agent that must decide, turn by turn,
> whether and what to ask before it acts — split the one outcome reward
> into a trajectory term, a turn term, and a step term.

## Mechanism

Yang et al. (2026) train IC-Seg, a referring-segmentation
agent that clarifies ambiguous queries through multi-turn dialogue before
segmenting. Vanilla GRPO assigns one outcome advantage uniformly to every
token in a trajectory; the authors report that this "would lead the model
towards generating repetitive and uninformative conversation, rather than
actively resolving the [[efe-planning-as-variational-inference|ambiguity]]."[^c1]

Hi-GRPO instead "deconstructs the advantage into a hierarchical structure,
capturing optimization signals across three distinct levels" — trajectory,
turn and step — combined into one advantage that scales a step-level ratio
by the sign of the trajectory-plus-turn term.[^c2]

The turn-level term is what prices a clarifying question. Under a uniform
prior over a candidate set of size $N_k$ after turn $k$, [[entropy]] is
$H_k=\log_2 N_k$; the entropy-reduction reward is defined by "normalizing
the total entropy reduction," $R_{ent}=(H_0-H_K)/H_0$, the fraction of the
initial ambiguity removed by the whole dialogue.[^c3]

An efficiency term counts, over the $K$ questions asked, the fraction that
narrowed the candidate set: the paper states this "encourages the model to
ask concise and discriminative questions" by "normalizing the count of
informative questions by the total number of turns."[^c4]

Both $N_k$ counts are estimated by a second MLLM acting as judge, since the
candidate-set size is not directly observable during rollout: it watches
the full dialogue and outputs the sequence of residual candidate counts.
The step-level term reuses a privileged self-teacher view, conditioned on
guidance from the same judge, to give dense, token-level credit inside the
sparse trajectory/turn signal.

## Known as

| Field | Name there | Match |
|---|---|---|
| LLM training (Yang et al. 2026, abbreviation) | Hi-GRPO | exact — this note's object |
| LLM training (Yang et al. 2026, full name) | Hierarchical Group Relative Policy Optimization | exact — same object, expanded |

## Why it matters

This is a reinforcement-learning reward that operationalizes "ask the
question that shrinks the candidate set" as a trainable signal, rather than
a hand-scored preference label: the entropy term is the same uniform-prior
bit-count used elsewhere on this stall's map, applied per dialogue turn
instead of per candidate axis, and the efficiency term directly penalizes
the redundant-question failure mode that motivated the design.

## Transfer

| | |
|---|---|
| **In its home field** | GRPO estimates an advantage from the relative reward of several sampled completions for one prompt, with no learned value model, built for single-pass tasks with a checkable outcome (a proof, a [[proactive-expertise-clarification|passing]] test). |
| **Here** | The outcome reward becomes one of three levels; a second, uniform-prior Shannon-entropy term over an LLM-judge-estimated candidate set scores how much a turn's question narrowed the ambiguity, and an efficiency term scores whether it did so at all. |
| **What survives** | Group-relative advantage estimation, and the empirical motivation — an outcome-only signal under-supervises multi-turn interaction quality, so a denser signal is added rather than replacing GRPO. |
| **What does not** | GRPO's original single-level simplicity, and its reliance on a directly checkable outcome: the turn-level entropy term here is not observed but estimated by a second model simulating the elimination process, so the reward itself carries that model's own error. |

## Limits

- The entropy reward's candidate-set counts $N_k$ are never directly
  observed; they are the judge model's own simulated reconstruction of the
  dialogue, so a biased or miscalibrated judge shapes the policy without a
  reported check against ground-truth candidate counts.
- Read on one domain (referring video object segmentation, Qwen3-VL-4B/8B
  base models) with one weighting ($\alpha=0.5$) and no ablation of $\alpha$
  or $\lambda$ reported in the slices read for this note; whether the
  three-level decomposition transfers to text-only clarification tasks is
  not shown here.
- The comparison against vanilla GRPO is qualitative in the introduction
  (Figure 3, not read) before the quantitative ablation; this note does not
  cite a specific accuracy delta attributable to Hi-GRPO alone versus
  vanilla GRPO.

## Related

[[investigative-question-grpo-training]] · [[preference-optimization-for-questions]] · [[mutual-information]] · [[expected-information-gain]] · [[semantic-entropy]]

[^c1]: yang-2026-guess — "these approaches would lead the model towards generating repetitive and uninformative conversation, rather than actively resolving the ambiguity"
[^c2]: yang-2026-guess — "Hi-GRPO deconstructs the advantage into a hierarchical structure, capturing optimization signals across three distinct levels"
[^c3]: yang-2026-guess — "The entropy reduction objective, Rent , is then defined by normalizing the total entropy reduction as follows"
[^c4]: yang-2026-guess — "By normalizing the count of informative questions by the total number of turns K, this term encourages the model to ask concise and discriminative questions."
