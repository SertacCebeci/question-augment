---
description: "Reward for fine-tuning an LLM's interaction policy by the drop in Shannon entropy over its own sampled recommendation lists, with no ground-truth target."
aliases: ["entropy-reduction reward", "uncertainty-driven interaction reward", "turn-level entropy reduction", "conversation-level entropy reduction"]
sources: ["bai-2026"]
---
# Recommendation-entropy reward

> Score a conversational turn not by an LLM judge's interactivity rating
> but by how much it concentrated the assistant's own recommendation
> distribution — no candidate set to enumerate, no ground truth needed.

## Definition / Mechanism

Bai et al. (2026) define recommendation uncertainty as the
[[entropy|Shannon entropy]] of the assistant's own output distribution: given a
conversation $C$, sample $n$ top-$m$ recommendation lists from the same
prompt, form the empirical item frequency $p(r)$ over the union $R$ of
items that appear, and take $H(C) = -\sum_{r\in R} p(r)\log_2 p(r)$; a
rank-weighted variant $H_w(C)$ discounts items by list position with
weight $1/\log_2(j+1)$. Turn-level information gain is the entropy drop
across one exchange, $I_T(A_1) = H_w(C_1) - H_w(C_2)$; conversation-level
gain unrolls the same subtraction to the end of the dialogue. Across 300
INSPIRED conversations, mean weighted entropy fell at $-0.040$ bits/turn
on average.[^c1]

This entropy-reduction score is then used directly as a training reward:
for SFT, conversations are selected by high reward score; for DPO, of two
sampled assistant responses the higher-reward one is preferred. Both
mechanisms require only the model's own recommendation samples — no
ground-truth recommendation and no enumerated candidate/hypothesis set are
needed to compute the label.[^c2]

On INSPIRED and ReDial with Llama-3.2-1B-Instruct, DPO trained on
turn-level entropy reduction gave the best INSPIRED Hit@1 (3.32%), Hit@5
(5.21%) and simulated-conversation hit rate (27.94%) among all tested
variants, and DPO on conversation-level entropy reduction gave the best
ReDial simulated hit rate (32.83%) and the fewest turns to ground truth
(2.74); both entropy-reward DPO variants beat a CollabLLM baseline whose
reward mixes ground-truth hit rate with an LLM-judge interactivity score,
despite using no ground truth at training time.[^c3]

## Known as

| Field | Name there | Match |
|---|---|---|
| conversational recommendation (Bai et al.) | entropy-reduction reward / uncertainty-driven interaction reward | exact |
| this paper, §3.2.1 | turn-level entropy reduction | exact — the per-turn form |
| this paper, §3.2.2 | conversation-level entropy reduction | exact — the whole-dialogue form |

**Not this concept.** [[preference-optimization-for-questions|EIG-rewarded
questioning]] (Mazzaccara et al. 2024) also turns an entropy-based score
into a DPO/SFT training signal, but its entropy is over an *enumerable,
closed hypothesis set* $\Omega$ that the model itself annotates — a
question is optimal when it halves $\Omega$. Here there is no $\Omega$: the
entropy is over the assistant's *own free-form output distribution*,
estimated empirically by repeated sampling. The two measure different
quantities on different objects (candidate-answer-set entropy vs.
generation-output entropy) and are recorded as `close`, not the same
concept.

## Why it matters

It supplies exactly the piece [[preference-optimization-for-questions]]
could not: a way to reward informative turns when the answer space is open
and no ground-truth target exists — the case this wiki's other EIG-reward
note flags as needing "a surrogate of unstated quality." Sampling the
model's own output and scoring by how much a turn concentrates that
distribution is a concrete, tested surrogate for that gap, at least for
list-style recommendation.[^c4]

## Transfer

| | |
|---|---|
| **Home field** | Predictive-uncertainty estimation via entropy over a sampled output distribution, used as a proxy for ranking [[calibration|reliability]] (Kweon et al., cited by the authors as their inspiration) |
| **Here** | The same entropy measure taken over *sampled generations at successive dialogue turns*, and its turn-over-turn drop used as a training reward |
| **What survives** | The core move — entropy of repeated model output as an uncertainty proxy that needs no ground truth — and its use as a reward signal for both SFT (select by score) and DPO (prefer by score) |
| **What does not** | Any claim about candidate-set structure: there is no enumerable world set here, so the reward cannot be compared on the same scale as EIG over a closed $\Omega$; results are one 1B model, two movie-recommendation datasets, and an LLM user simulator, not human dialogue |

## Limits

- Evaluated with one small model (Llama-3.2-1B-Instruct) on two movie
  datasets and an LLM-simulated user (Claude Sonnet 4 role-playing), not
  human conversation partners — the authors name this as their own
  limitation.[^c5]
- The uncertainty estimate assumes the base LLM can *name* candidate items
  directly from its own generation; a retrieval-backed or large, dynamic
  catalog would need entropy computed over retrieved rankings instead,
  which the authors flag as unvalidated future work.
- Sampling parameters are fixed ($m=n=5$) and not varied; sensitivity of
  the reward to these choices is untested.

## Related

[[preference-optimization-for-questions]] · [[expected-information-gain]] · [[entropy]] · [[semantic-entropy]] · [[cross-type-eig]]

[^c1]: bai-2026 — "We define uncertainty as the Shannon entropy over the distribution of recommendations induced by repeated sampling of a fixed prompt given a conversation 𝐶."
[^c2]: bai-2026 — "We fine-tune LLMs using the proposed entropy-reduction score as the reward. We use standard SFT and DPO [17] as optimization mechanisms; the proposed component is the entropy-reduction reward used to select SFT examples or define DPO preferences. For SFT, we select training examples with high reward scores. For DPO, among two generations sampled from the recommender, the higher-reward one is preferred."
[^c3]: bai-2026 — "The entropy-reduction variants show the strongest gains on the main conversational metrics: DPO (Turn Entropy) obtains the best INSPIRED Hit@1, Hit@5, and simulated conversation hit rate, while DPO (Conv Entropy) obtains the best ReDial simulated conversation hit rate and the lowest ReDial turn count."
[^c4]: bai-2026 — "This assigns credit to interactions according to recommendation-relevant information gain rather than an LLM judge’s general assessment of interactivity"
[^c5]: bai-2026 — "Our evaluation uses automatic recommendation metrics and an LLM-based user simulator rather than human judgments, and we fix 𝑚 = 𝑛 = 5; conversational usefulness and sensitivity to these sampling parameters remain to be validated."
