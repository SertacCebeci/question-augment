---
description: "A multi-turn GRPO reward combining expected information gain and outcome reward amortises Bayesian experimental design into an LLM's weights, replacing per-turn belief search with one forward pass."
aliases: ["ASIG", "Amortised Sequential Information Gathering", "amortising BED into LLM policies"]
sources: ["hartmann-2026"]
---
# Amortised Sequential Information Gathering

> [[bayesian-experimental-design|Bayesian experimental design]] moved from an
> inference-time search to a training signal: the [[expected-information-gain|EIG]]
> of the question a rollout is about to ask becomes part of a GRPO reward, so
> the trained policy answers "which axis first?" in one forward pass instead
> of a belief-sampling search at every turn.

## Mechanism

Hartmann, Harvey, Navott et al. (2026) treat the LLM as a
sequential BED policy $\pi_{LLM}(\xi_t \mid h_{t-1})$ choosing designs
(questions) $\xi_t$ against a frozen oracle LLM that returns outcomes $y_t$.
At each turn the reward combines two terms:

```text
R_t = (α/Z_E) Σ γ_EIG^k · r_EIG(ξ_{t+k}, Θ_{t+k})   [k = 0..E-1]
    + (β/Z_O) Σ γ_out^k · r_out(y_{t+k})            [k = 0..O-1]
```

$r_{EIG}$ is computed by sampling a belief set $\Theta_t$ of candidate
targets from the Proposer LLM itself, filtering it for consistency with the
history, then scoring the proposed question by a Rao-Blackwellised EIG
estimator over that belief set (reusing the estimation method of BED-LLM,
Choudhury et al. 2025, but as a training reward rather than an inference-time
search); $r_{out}$ is a step-wise penalty plus a terminal reward for a
correct guess. The two terms use independent horizons ($E=1$, $O=3$ in the
reported experiments) and independent discounts, normalised so different
horizon lengths don't change reward scale — this is GRPO (Shao et al. 2024)
extended from a single scalar per rollout to two reward streams with distinct
temporal reach, group-averaged into one advantage per rollout to update LoRA
adapters. A learning curriculum trains with the EIG term switched off first
($\alpha=0$) because the Proposer otherwise rarely commits to a specific
guess; adding EIG afterward raises the rate of hypothesis-seeking (guess-type)
questions relative to constraint-seeking ones, in the vocabulary of
[[constraint-seeking]].[^c1]

## Why it matters

On [[twenty-questions|20 Questions]] (Qwen2.5-7B/14B-Instruct, held-out
animal/plant categories), ASIG more than doubles the 7B base model's success
rate and beats BED-LLM's inference-time belief search in one of two 7B
settings, while matching the base model's own inference cost — over 25×
cheaper per episode than BED-LLM, which re-runs belief sampling and EIG
scoring at every turn.[^c2]

Fine-tuned only on 20 Questions, the 7B model also improves accuracy,
voluntary accuracy and overconfidence on [[mediq|MediQ]] (Li et al. 2024), a
clinical-interview benchmark never seen in training; the 14B model's transfer
is mixed (voluntary accuracy drops, overconfidence rises slightly), which the
authors attribute to a stronger prior leaving less room for the fine-tuning
to change behaviour.[^c3]

## Transfer

| | |
|---|---|
| **In its home field** | Bayesian experimental design: an explicit prior $p(\theta)$ and likelihood $p(y\mid\theta,\xi)$ over a design space, EIG computed or estimated at each design-selection step, with no commitment to how the policy is implemented. |
| **Here** | The prior is not written down; it is a set of beliefs the LLM itself samples and filters for coherence, re-sampled up to three times if too small, standing in for $p(\theta)$. |
| **What survives** | The EIG scoring logic and the Rao-Blackwellised estimator for computing it under a sampled belief set; the empirical result that a policy trained against this signal transfers its information-gathering behaviour to an unrelated domain (MediQ) without in-domain fine-tuning. |
| **What does not** | Any correctness guarantee tying the sampled, filtered belief set to the true posterior — an LLM's self-generated beliefs can be systematically biased or miss the true target, and the paper reports no check of belief-set [[calibration]]; nor does the single-scalar EIG-optimal guarantee of BED itself carry over, since the trained policy also optimises a separate, differently-discounted outcome reward. |

## Limits

- Two model sizes (Qwen2.5-7B/14B-Instruct), one training domain (20
  Questions, binary yes/no outcomes chosen specifically because they make the
  Rao-Blackwellised EIG estimator tractable), one oracle model family; the
  paper does not test open-ended (non-binary) answer spaces.[^c4]
- The reward's EIG component depends on the Proposer's own sampled and
  filtered belief set as a stand-in for the true posterior; no measurement of
  how close that set is to the ground-truth hypothesis distribution is
  reported.
- MediQ transfer holds at 7B but not at 14B, so "the learned strategy
  transfers" is a scale-dependent finding, not a general property of ASIG.
- BED-LLM (the inference-time comparison) beats ASIG on the 14B plants
  category despite using far more inference compute, so the inference-time
  vs. amortised trade-off is not uniformly won by amortisation in this
  paper's own results.
- Accepted at a non-archival ICML workshop (FoGen 2026); not yet through a
  full peer-reviewed venue.

## Related

[[bayesian-experimental-design]] · [[expected-information-gain]] · [[preference-optimization-for-questions]] · [[investigative-question-grpo-training]] · [[twenty-questions]] · [[mediq]] · [[constraint-seeking]]

[^c1]: hartmann-2026 — "We extend the default GRPO formulation (Shao et al., 2024) to the multi-turn setting."
[^c2]: hartmann-2026 — "ASIG more than doubles the success rate of the 7B base model and reduces inference cost by over 25× relative to BED-LLM, a competitive inference-time baseline."
[^c3]: hartmann-2026 — "Our 7B model improves accuracy and voluntary accuracy by 0.9 and 1.7 percentage points, respectively. The overconfidence rate drops from 36.1% to 33.4%"
[^c4]: hartmann-2026
