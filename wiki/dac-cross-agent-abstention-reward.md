---
description: "Splits agentic search into a searcher and a generator trained jointly by RL, where the generator's abstention on insufficient evidence becomes the searcher's reward signal."
aliases: ["DAC", "Divide and Cooperate", "role-decomposed multi-agent training", "cross-verification reward", "cross-agent learning signal"]
sources: ["park-2026", "arxiv-2512-18745"]
---
# DAC (cross-agent abstention reward)

> A training-signal fix for a credit-assignment problem: when one agent
> searches and another answers, whose fault is a wrong answer? DAC answers
> by making the answering agent's [[abstention]] decision the reward for the
> searching agent, instead of scoring both from final-answer correctness.

## Definition / Mechanism

DAC decomposes agentic search into a searcher $S$ that iteratively issues
queries and a generator $G$ that receives the aggregated evidence $E$ and
answers or abstains. Assigning both agents the same answer-level reward
"creates a credit assignment problem, as each agent may be penalized for
failures caused by the other," and a fixed [[sufficient-statistic|sufficiency]] oracle for the
searcher is hard to define because "such notion of sufficiency itself
should depend on the generator, as evidence that is sufficient for one
generator may not be sufficient for another."[^c1]

DAC's fix gives the generator an abstention action and routes that
decision into the searcher's reward. With $s(Q,E)$ an external verifier's
judgment of evidence sufficiency, $v(A)$ whether the generation is a
non-abstention, and $a(Q,A)$ whether it is a correct answer: "$r_S(Q,E,A) =
\mathbb{I}[s(Q,E)=1 \wedge v(A)=1]$" and "$r_G(Q,E,A) = \mathbb{I}[a(Q,A)=1
\vee (s(Q,E)=0 \wedge v(A)=0)]$" — the searcher is rewarded only for
evidence that is both externally sufficient and accepted by the generator,
and the generator for answering correctly or correctly abstaining on
insufficient evidence.[^c2]

The searcher is trained with PPO and the generator with GRPO, both as
LoRA adapters over a shared Qwen [[backbone-of-a-formula|backbone]], on NQ/HotpotQA-derived training
data; abstention is disabled at test time, forcing the generator to answer
every example.[^c3]

The same coupling, with a different signal, appears in InSight-o3
(arxiv-2512-18745). There the answering side does not abstain; it rates
each search result, binary, by "whether the prediction is relevant to the
assigned task and can help vReasoner" answer the user query, obtained "by
asking vReasoner to rate each" result.[^c6][^c7] The source treats that
rating as a weak signal: "as this rating is not always reliable (vReasoner
may sometimes make mistakes)", so it "incorporate[s] outcome supervision as
a safeguard", and a result is rewarded only when the rating and the final
answer's correctness both hold.[^c8] The margin this buys is small: "The
originally proposed setting outperforms all the variants with a small
average lead on the three benchmarks."[^c9] My inference: the explicit
helpfulness rating removes the over-abstention failure named under Limits,
and substitutes a rater that errs; the conjunction with outcome is the
source's own guard against that second failure, and the work reports no
case in which the guard was needed on its own terms.

## Why it matters

Against Search-R1 baselines (which have no explicit abstention — DAC's
paper treats "continuing to search until the last turn as an abstention"
for that comparison), DAC "consistently improves over Search-R1 across
most benchmarks, including both general and multi-hop QA tasks," using two
rank-32 LoRA adapters (about 2.12% of full fine-tuning parameters) against
fully fine-tuned baselines.[^c4]

## Transfer

| | Home field (multi-agent RL) | Here (asking) |
|---|---|---|
| Formalism | role-specific reward decomposition to fix credit assignment between cooperating policies | the axis-selection agent (searcher) and the stopping/answering agent (generator) are split and cross-reward each other |
| What survives | the coupling itself — one agent's insufficiency judgment prices the other agent's action, without a fixed external oracle for "enough evidence" | |
| What does not | the guarantee: this is an empirical RL training recipe on two backbones and seven QA benchmarks, not a proof that the coupling converges to a well-calibrated stopping/selection policy in general | |

## Limits

- The searcher's reward depends on the generator's own abstention judgment,
  which "may become overly conservative, abstaining even on sufficient
  evidence" — the paper's own named failure mode (over-abstention), fixed
  only partially by a separate augmentation step ([[hard-positive-evidence-augmentation]]).[^c5]
- Evaluated only on two Qwen backbones (7B/8B) with a Wikipedia-dump
  dense retriever and EM-based sufficiency verification; no result is
  reported for sufficiency judged any other way, or for backbones this
  size does not represent.
- Abstention is disabled at test time, so the deployed system never
  exercises the very action whose training signal DAC depends on.

## Related

[[abstention]] · [[awa-rl]] · [[value-of-information]] · [[hard-positive-evidence-augmentation]] · [[generalized-visual-search]] — the searcher in InSight-o3 is a region locator, and its rating-gated reward is the variant described above

[^c1]: park-2026 — "creates a credit assignment problem, as each agent may be penalized for failures caused by the other. An alternative is to define a separate evidenceacquisition reward for the searcher. However, evidence sufficiency is often difficult to verify exactly. Furthermore, such notion of sufficiency itself should depend on the generator, as evidence that is sufficient for one generator may not be sufficient for another."
[^c2]: park-2026 — "rS (Q, E, A) = I s(Q, E) = 1 ∧ v(A) = 1 ,"
[^c3]: park-2026 — "the searcher is trained with PPO (Schulman et al., 2017), since it receives intermediate turn-level rewards, while the generator is trained with GRPO (Shao et al., 2024)."
[^c4]: park-2026 — "Our method consistently improves over Search-R1 across most benchmarks, including both general and multi-hop QA tasks, as well as both in-domain and out-of-domain evaluation settings."
[^c5]: park-2026 — "This design, however, introduces a predictable failure mode: the generator may become overly conservative, abstaining even on sufficient evidence."
[^c6]: arxiv-2512-18745 — "whether the prediction is relevant to the assigned task and can help vReasoner"
[^c7]: arxiv-2512-18745 — "by asking vReasoner to rate each"
[^c8]: arxiv-2512-18745 — "as this rating is not always reliable (vReasoner may sometimes make mistakes)"
[^c9]: arxiv-2512-18745 — "The originally proposed setting outperforms all the variants with a small average lead on the three benchmarks."
