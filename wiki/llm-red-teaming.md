---
description: "Using one LM to find the inputs on which another fails. The most mature Perez et al. (2022), *Red Teaming Language Models with Language Models* (DeepMind),"
aliases: ["automated red teaming", "red-teaming LMs with LMs"]
sources: ["perez-2022", "li-2024-rtpe", "arxiv-2512-20806", "arxiv-2512-20677", "arxiv-2512-10172", "arxiv-2512-07059", "arxiv-2511-17666"]
---
# Automated red teaming

> Using one LM to find the inputs on which another fails. The most mature
> worked example of fuzzing a question space, and the source of the
> breadth/depth split.

## Approach (Perez et al., 2022)

Perez et al. (2022), *Red Teaming Language Models with Language Models*[^s1][^s2]
(DeepMind), had a language model generate test questions for a 280B-parameter
Dialogue-Prompted Gopher chatbot and scored the replies with a trained
offensive-content classifier. What was measured: the rate at which generated
test cases elicited classifier-flagged offensive replies, and the diversity of
the generated cases, across generation methods running from zero-shot
prompting through few-shot and supervised learning to RL. The RL end of that
range maximised hit rate and lost diversity; the zero-shot end did the
reverse. Also surfaced: leaked training data, generated private phone numbers,
and harms that only appear over multiple turns.

The target is therefore not one perfect attack:

```text
diverse test cases  +  difficult test cases  +  high coverage
```

## Known as

| Field | Name there | Relation |
|---|---|---|
| LLM safety evaluation | automated red teaming | exact |
| Perez et al. 2022 | red-teaming LMs with LMs | exact — the paper's own name for the method |
| Software testing | fuzzing | close — same generate-and-check loop, no learned generator or classifier-defined failure |

**Not this concept.** *RTPE* (below) is one named framework inside automated
red teaming, not another name for it; *red teaming* in the organisational
sense ([[dialectic-red-team]]) is a human role assignment, measured
differently and stopped differently.

## RTPE — two axes, two mechanisms

RTPE (**Red Teaming Prompt Evolution**), Li et al. (2024), *Be a Multitude to
Itself: A Prompt Evolution Framework for Red Teaming* (Findings of EMNLP
2024), evolves red-teaming prompts along two explicitly separate operations:

```text
IN-BREADTH   enhanced in-context learning generates new prompts  →  new attack types
IN-DEPTH     transformation operations rewrite a found prompt    →  deepen one type
```

The paper reports gains on both attack success rate and diversity over prior
automatic methods, and uses 4,800 generated prompts to analyse 8 LLMs across
8 sensitive topics. The load-bearing structural fact for this wiki is that
breadth and depth are implemented as **different operators**, not as more of
the same operator.

## Transfer

| | In its home field (LLM safety evaluation) | Here (asking) |
|---|---|---|
| Object probed | a target LM's safety behaviour under adversarial input | the world-set $W$ a task leaves open ([[possible-worlds]]) |
| Success signal | a triggered failure, scored by a classifier | a world eliminated, or a distinct axis opened |
| **What survives** | the split into two modes with different operators — breadth discovers axes, depth exhausts one — and the metric lesson: count *distinct* modes, not attempts | |
| **What does not** | automatic scoring of a hit (asking has no classifier that says "that question landed"), the classifier that *defines* the failure taxonomy, and every efficiency or success-rate number, which is relative to that classifier and target | |

## A lesson about metrics

Both papers report not "how many attacks were tried" but how much of the
failure space was covered — diversity alongside success rate. Translated to
asking: not question count but **the number of distinct axes**. This is the
same warning as in [[possible-worlds]]: counting misleads, weight matters.

## This wiki's conjecture

The cited evidence is that in these systems breadth is a *separately built*
operator: RTPE implements it as its own stage, and in Perez et al. the
diversity-maximising and hit-rate-maximising ends of the method range are
different methods. **This wiki infers** — it is not a finding about
questioning, and no study cited here tested it — that a questioner optimising
a per-question payoff will likewise do depth, and that breadth needs a
mechanism placed there on purpose. See [[divergent-convergent]].

## A trained attacker as the red-teamer

Perez et al. generated test questions with a model trained for the purpose. Paulus et al. (AdvGame) train an attacker jointly with a defender, online, and then keep the attacker as a probe for other models. The abstract's claim is that "the resulting Attacker LM converges into a strong, general-purpose red-teaming"[^s3] agent that can probe arbitrary targets. The attacker runs no search: "our Attacker does not run any"[^s4] special iterative algorithm, and its prompts come from ordinary sampling. Against the paper's own defended model, an input counts as broken if at least one of ten sampled prompts is judged successful, and the authors report that "our Attacker achieves performance comparable to strong adaptive"[^s5] attacks such as PAIR, GCG and TAP. The payoff this attacker is trained on is the one in [[non-zero-sum-attacker-reward]], and its rewordings are gated as in [[faithfulness-gated-attack-reward]].

The measure is hit rate per input. It does not count distinct attack types, so the diversity lesson above is not tested by this line; whether a jointly trained attacker covers more than it hits is open.

A later framework states the diversity lesson as a constraint on the candidate set rather than as a report. It holds the set to a diversity floor and a category-coverage floor, and during selection "redundant or lowimpact variants are discarded."[^s10] The ablation that removes the diversity floor shows the set collapsing: "diversity collapses (0.81→0.42), accompanied by"[^s7] a fall in novelty. Its conclusion is that "The key empirical lesson is that discovery count alone is not enough."[^s8] The mechanism is set out in [[set-level-diversity-floor]].

## Multi-turn search with a judge (TEMPEST, 2025)

The same loop has a multi-turn form. TEMPEST keeps a tree of conversation branches, each pushed by a framing, and prunes the branches a judge scores low: "Pruning: BFS exploration with adaptive pruning of low-scoring branches."[^s12] Across ten models the study reports that "six models achieved 96% to 100% attack success rate".[^s13] The stop condition is a judged harm score, so the rate measures the judge as well as the target. The judge here is a language model, and its agreement with a second judge is reported as moderate.[^s14]

The search also bears on a scale question the field often asks. The paper finds "no relationship between model scale and adversarial robustness" in its figure of ASR against parameter count.[^s15] That is a finding about this search on this behaviour set, not a general law. The thinking-mode result from the same study, a 55-point drop on one model pair, is in [[extended-reasoning-framing-resistance]].

## Self-generated attacks (Perel, 2025)

A variant has the target red-team itself. Perel (2025) gives the target model a system instruction "designed to override its safety alignment, effectively asking it to 'red-team' itself by generating a prompt that would elicit a specific harmful output."[^s17] The same study has the other model of the pair write the prompt for the target (cross-generated). On 320 trials across two models, the two routes came out level: "the average success rate for both methods converged at 35.625%."[^s18] The vectors do not split evenly. "Self-Bypass proved superior for semantic attacks like Role-Playing and Context Manipulation."[^s19]

This is a parity between two generators, not a test of the blind-spot limit below. A shared blind spot would predict that a model's own prompts find fewer failures than another model's, and the study measures rates, not which failures were found, so it neither confirms nor rules that out. The paper's step from this to replacing human-led red-teaming is the author's inference; no run in the text tests a self-generated loop used in training.

## Limits

- The results are about attacks on safety behaviour, not about questioning;
  the extension in *This wiki's conjecture* is untested and is a conjecture,
  not a finding.
- Every reported rate is defined by a classifier over a fixed harm taxonomy;
  "distinct failure modes" needs a clustering that is itself a modelling
  choice, so a coverage number is not comparable across taxonomies.
- Both studies red-team a *known* behaviour class. Neither shows that either
  operator finds a failure mode outside the classifier's vocabulary — which
  is exactly the [[unknown-unknowns]] case.
- A red-teamer sharing a base model with its target shares its blind spots.
- The trained-attacker result is scored by success per input, and the paper restricts itself: the approach "focuses exclusively on natural-language attacks that humans"[^s6] can read, so token-level attacks are outside it.

- The constrained-set framework was run on one target model, GPT-OSS-20B, and its detector's scores are offered as audit input rather than ground truth: "detection scores should be interpreted as audit signals"[^s9]. A count of validated findings on one model says nothing yet about whether the constraint transfers.
- The same generate-and-judge loop, aimed at a user's own custom instruction rather than at safety behaviour, is [[custom-instruction-adherence-audit]]. Its authors say that prior audits "both focus on adherence to provider-specified behavioral guidelines rather than user-specified custom instructions."[^s11] There the hit is an instruction deviation confirmed by human review, not a classifier's flag, so the scoring lesson above does not carry over unchanged.
- The multi-turn TEMPEST figures rest on one judge family and a 100-behaviour set. The paper's own check finds the primary judge more conservative than the secondary one, so the reported rate may be high;[^s16] the scale finding is a reading of one figure, not a test of a general law.

## Related

[[dialectic-red-team]] · [[metamorphic-probes]] · [[divergent-convergent]] · [[unknown-unknowns]] · [[possible-worlds]] · [[non-zero-sum-attacker-reward]] · [[faithfulness-gated-attack-reward]]

[^s1]: perez-2022
[^s2]: li-2024-rtpe
[^s3]: arxiv-2512-20806 — "the resulting Attacker LM converges into a strong, general-purpose red-teaming"
[^s4]: arxiv-2512-20806 — "our Attacker does not run any"
[^s5]: arxiv-2512-20806 — "our Attacker achieves performance comparable to strong adaptive"
[^s6]: arxiv-2512-20806 — "focuses exclusively on natural-language attacks that humans"
[^s7]: arxiv-2512-20677 — "diversity collapses (0.81→0.42), accompanied by"
[^s8]: arxiv-2512-20677 — "The key empirical lesson is that discovery count alone is not enough"
[^s9]: arxiv-2512-20677 — "detection scores should be interpreted as audit signals"
[^s10]: arxiv-2512-20677 — "while redundant or lowimpact variants are discarded"
[^s11]: arxiv-2512-10172 — "both focus on adherence to provider-specified behavioral guidelines rather than user-specified custom instructions"
[^s12]: arxiv-2512-07059 — "Pruning: BFS exploration with adaptive pruning of low-scoring branches"
[^s13]: arxiv-2512-07059 — "six models achieved 96% to 100% attack success rate"
[^s14]: arxiv-2512-07059 — "The two evaluators achieved κ = 0.537 (moderate agreement) with 78.8% raw agreement."
[^s15]: arxiv-2512-07059 — "from left to right indicates no relationship between model scale and adversarial robustness."
[^s16]: arxiv-2512-07059 — "This conservative tendency suggests the reported ASR may slightly overestimate attack"
[^s17]: arxiv-2511-17666 — "For the Self-Bypass condition, the target model was prompted with a system instruction designed to override its safety"
[^s18]: arxiv-2511-17666 — "the average success rate for both methods converged at 35.625%"
[^s19]: arxiv-2511-17666 — "Self-Bypass proved superior for semantic attacks like Role-Playing and Context Manipulation."
