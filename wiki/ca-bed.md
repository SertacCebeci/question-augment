---
description: "Inference-time question selection for multi-turn dialog agents that scores a simulated conversation tree by expected information gain with LLM-estimated, confidence-smoothed answer likelihoods."
aliases: ["CA-BED", "Conversation-Aware Bayesian Experimental Design"]
sources: ["arnould-2026"]
---
# CA-BED

> An agent picks its next question by growing a simulated conversation tree
> of candidate questions and possible answers, scoring branches with
> [[expected-information-gain]], and choosing the branch that maximises it
> — rather than scoring one question at a time.

## Definition / Mechanism

CA-BED keeps a belief $B_k(h_i)=P(h_i\mid E_{1:k})$ over a fixed hypothesis
set and, at each turn, has an LLM generate $M_q$ candidate questions and
estimate each answer's likelihood $P(E\mid h_i)$ as text (not from token
log-probabilities). The agent then expands an alternating
QuestionNode/EvidenceNode tree $D_{sim}$ steps deep and scores it
recursively: a QuestionNode's reward is the probability-weighted average of
its EvidenceNode children; an internal EvidenceNode's reward is the max over
its follow-up questions; a terminal EvidenceNode's reward is the [[entropy]]
drop $H(B_0)-H(B_v)$. The agent asks the question at the root of the
highest-reward branch, observes the real answer, updates $B_k$ by Bayes'
rule under a naive-Bayes (conditionally independent evidence) assumption,
and repeats until a hypothesis crosses a confidence threshold $\tau$ or the
turn budget $D_{ask}$ is exhausted.[^c1]

To keep hard binary elimination from discarding a correct hypothesis on one
ambiguous answer, likelihoods are pulled toward uniform before use:
$P'(E_k\mid h_i)=\epsilon P(E_k\mid h_i)+(1-\epsilon)$, an estimator-confidence
parameter that softens the partition instead of eliminating hypotheses
outright.[^c2]

## Why it matters

On two entity-deduction benchmarks ([[twenty-questions|20 Questions]], Detective Cases;
DeepSeek-V3.2 as both questioner and answerer, 3 seeds), CA-BED gives an
average 21.8% absolute success-rate gain over direct prompting at a cost of
1.8 extra turns on average, and a 17.0–22.5 point absolute gain over UoT
(Hu et al. 2024) — the deterministic-likelihood, hard-elimination special
case of the same tree ($\epsilon=1,\tau=1$) — with the gap attributed to
ambiguous answers being down-weighted instead of eliminating a plausible
hypothesis outright.[^c3]

## Transfer

| | |
|---|---|
| **Home field** | [[bayesian-experimental-design]]: rank a candidate design/question by [[expected-utility|expected utility]] computed from a known likelihood, usually one step ahead. |
| **Here** | multi-turn natural-language dialog: the likelihood is elicited from an LLM as text, not written down; the "design space" is a tree of candidate questions and candidate answers grown $D_{sim}$ steps deep. |
| **What survives** | scoring by expected entropy drop before the answer is known, and the recursive expectation-over-children / max-over-questions bookkeeping needed to propagate that score through a multi-step plan. |
| **What does not** | any optimality guarantee — the reward is computed on an LLM-elicited, temperature-calibrated likelihood, not a modelled one, so ranking candidate branches carries no accuracy bound; tree expansion is exponential ($O((M_qK)^{D_{sim}})$) and only tractable because per-node likelihoods are cached as independent of dialog history. |

## Limits

- Reported in a workshop paper (ICLR 2026 workshop track), not yet a
  peer-reviewed venue result; the claims below rest on that single
  publication.
- Both questioner and answerer are the same LLM (DeepSeek-V3.2) — this is
  self-play, not a human-in-the-loop evaluation, and the improvement could
  partly reflect the two roles sharing a model family rather than the
  method generalising to a genuinely external answerer.
- Benchmarks are small and closed-hypothesis (111 items in 20 Questions,
  100 scenarios in Detective Cases) with a fixed, enumerable hypothesis set
  known in advance — the setting [[bayesian-experimental-design]] already
  flags as required for EIG to be computable at all.
- Branching width ($M_q=3$) and lookahead depth ($D_{sim}=2$) are fixed
  hyperparameters shared with the UoT baseline in the reported comparison,
  so the measured gain is attributable to the smoothed/soft likelihood
  ($\epsilon<1$), not to lookahead depth itself — the paper does not report
  a no-lookahead ablation of CA-BED.
- The reward is entropy reduction, not a downstream decision's value: it
  answers "which question teaches the most" but not "which question is
  worth asking," the [[value-of-information]] gap this wiki already notes
  for EIG generally.

## Related

[[bayesian-experimental-design]] · [[expected-information-gain]] · [[value-of-information]] · [[optimal-decision-tree]] · [[semantic-entropy]]

[^c1]: arnould-2026 — "the agent maintains a belief distribution over candidate hypotheses, generates candidate questions, expands an alternating QuestionNode/EvidenceNode conversation tree over possible answers, and estimates answer likelihoods with an LLM to score branches by expected information gain. After observing the real user response, the posterior belief is updated and the process repeats until the confidence threshold is met or the conversation budget is exhausted."
[^c2]: arnould-2026 — "we also apply a confidence-weighted smoothing to these likelihoods, pulling them toward a uniform baseline P′ (Ek |hi ) = ϵP(Ek |hi ) + (1 − ϵ)."
[^c3]: arnould-2026 — "Across two structured entity-deduction benchmarks, CA-BED yields an average 21.8% improvement in success rates over direct prompting, with comparable gains relative to alternative information-seeking methods. It achieves these gains with an average increase of only 1.8 conversational turns compared to direct prompting."
