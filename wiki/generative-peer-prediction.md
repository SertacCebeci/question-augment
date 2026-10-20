---
description: "Miller et al.'s peer prediction needs the joint law of two answerers' Lu, Xu, Zhang, Kong & Schoenebeck (2024), EC'24; arXiv 2405.15077 v4. **Model (§3.1).** An item $Z$ from an unknown prior;"
aliases: ["GPPM", "generative peer prediction mechanism"]
sources: ["lu-2024", "miller-2005"]
---
# Generative peer prediction

> Miller et al.'s peer prediction needs the joint law of two answerers'
> signals; GPPM lets a language model supply it — score answerer $i$ by the
> log-probability the model assigns to the *other* answerer's report given
> $i$'s. One question, no second-order report, free-text answers. The model
> fills the prior's seat; the peer's seat stays occupied by a second human.

## Definition / Mechanism

Lu, Xu, Zhang, Kong & Schoenebeck (2024), EC'24; arXiv 2405.15077 v4.[^s1][^s2]
**Model (§3.1).** An item $Z$ from an unknown prior; two agents receive
signals $X_i, X_j$ i.i.d. given $Z$, with stochastic relevance (Assumption
3.1). Three effort levels: high yields $X_i$; low yields $X_i^l = f(X_i)$, a
deterministic coarsening; none yields `Null`, independent of everything.
Reports $\tilde X_i$ may differ from signals.

**Original peer prediction (Definition 3.7).** Score $i$ by
$\log \Pr[X_j = \tilde x_j \mid X_i = \tilde x_i]$ — the log scoring rule on
the posterior $i$'s report induces about the peer's report. Potent (high effort
and truth form a Bayes–Nash equilibrium under a linear payment) when the prior
and $\Pr[X_i \mid Z]$ are known (Proposition 3.8, which they attribute to
Miller, Resnick & Zeckhauser 2005, Proposition 1).

**Assumption 4.1 (LLM-prediction).** There are prompts $\psi$ such that
$D_{KL}\big(\Pr[X_j \mid X_i{=}x_i] \,\|\, \Pr_{LLM(\psi)}[X_j \mid
X_i{=}x_i]\big) \le \epsilon$ for every $x_i$, and this is common knowledge.

**GPPM (Definition 4.2).** $\text{score}_i = \log \Pr_{LLM(\psi)}[X_j =
\tilde x_j \mid X_i = \tilde x_i]$.
**GSPPM (Definition 4.3) — the synopsis-conditioned variant.** The same
score with a commonly known *synopsis* $\Theta = \theta$ of the item added to
the conditioning (for a paper, its abstract):
$\log \Pr_{LLM}[X_j = \tilde x_j \mid X_i = \tilde x_i, \Theta = \theta]$.

**Proposition 4.4.** Given a high-effort, truthful peer, an untruthful report
gains at most $\epsilon$; low effort loses at least
$I(X_i; X_j \mid X_i^l) - \epsilon$; no effort loses at least
$I(X_i; X_j) - \epsilon$. **Proposition 4.6.** GPPM is $\alpha\epsilon$-potent
with $\alpha = \max\big((c_h - c_l)/I(X_i;X_j \mid X_i^l),\;
c_h/I(X_i;X_j)\big)$; Propositions 4.5 and 4.7 are the same for GSPPM with
everything conditioned on $\Theta$. **Corollary 4.8.** When the low-effort
signal is determined by the synopsis, GSPPM keeps the high-vs-low gap and
shrinks the low-vs-none gap.

**Implementations (§5).** *Token*: the log-probability of the peer's report
from an open model (Llama-2-70B) prompted with $i$'s report, after an LLM
preprocessing step that strips style — necessary, they report, against
"shortcut" correlation on surface features. *Judgment*: each report is distilled
into judgments and a black-box model (GPT-4) scores support for each.

**Measured (§7).** Yelp: 1,000 restaurants, 198,444 reviews. ICLR 2020: 300
papers, 911 reviews. $K$ = 500/1,000 paired draws, paired $t$-test on the
score drop. Replacing a review by one from another item, deleting alternate
sentences, and deleting alternate judgments all lowered scores significantly
(their Fig. 6; on ICLR random replacement, Token-Preprocess reaches
$-\log_{10} p = 78.30$ against 12.93 for a numerical-rating baseline).
Replacing a human ICLR review with a GPT-3.5 review lowered the GPPM score by
$\bar d = 10.020$ ($p = 5.0\times10^{-28}$) and with GPT-4 by 2.904
($p = 8.2\times10^{-4}$); the GSPPM variant: 9.197 and 5.357 (their Table 3).

## Known as

| Name | Field | Relation |
|---|---|---|
| GPPM | mechanism design | exact |
| generative peer prediction mechanism | mechanism design | exact |
| GSPPM (generative synopsis peer prediction mechanism) | mechanism design | close — the synopsis-conditioned variant of the same score (Definition 4.3): the same log-probability of the peer's report, with a commonly known synopsis $\Theta$ added to the conditioning; its own guarantee (Propositions 4.5, 4.7, Corollary 4.8) and its own Table 3 column. Filed here as the variant, not as an alias: the two are measured separately |
| LLM-as-a-judge | LLM evaluation | **not this concept** — a judge scores a report against the model's own view of the item; GPPM never asks the model what it thinks of the item, only how well one human report predicts another |
| peer prediction (Miller, Resnick & Zeckhauser 2005) | mechanism design | close — the same score with the known joint law replaced by a model estimate under Assumption 4.1; the family is [[peer-prediction]] |

## Why it matters

1. **The prior's seat, not the peer's.** What kept the 2005 method off real
   questions was knowing $\Pr[X_j \mid X_i]$. GPPM fills that seat with a
   model and leaves the peer's seat where it was: the score is against
   $\tilde x_j$, a second human report. The authors claim deployment "in
   single-task settings without the necessity of directly soliciting
   predictions or possessing a priori distribution knowledge" — not without a
   peer.
2. **The verification currency is conditional [[mutual-information|mutual information]].**
   Proposition 4.4 prices the full-vs-low gap as $I(X_i; X_j \mid X_i^l)$. An
   asker choosing what to put to a second source is choosing what conditional
   information the model can read off the pair.
3. **Free-text answers become scorable without a partition.** Every other
   member of the family needs categorical or scalar reports; this reads
   natural-language reviews — the format an asker actually receives.
4. **The synopsis is the lever against restatement (the GSPPM variant).**
   Conditioning the predictor on what is common knowledge about the item
   removes payment for repeating the item back — the move
   [[surprisingly-popular-algorithm]] makes by subtracting predicted from
   actual, done inside the predictor.
5. **Report quality is ordered from outside.** Human $>$ GPT-4 $>$ GPT-3.5 in
   expected score on ICLR under both the base score and the variant: a
   working, not guaranteed, ordering with no ground truth anywhere.

## Transfer

| | |
|---|---|
| **Home field** | two human reviewers of one item, signals i.i.d. given the item, a model whose conditional prediction is within KL $\epsilon$ of the true conditional and is common knowledge, a payment linear in score, and a designer who can preprocess reports |
| **Here** | an asker holding two free-text answers to one question from sources it cannot check, with a model available |
| **What survives** | the scoring rule — the log-probability of one answer given the other, from a model — as an ordering of answers by information carried; the synopsis conditioning of the GSPPM variant; and the measured direction, that degradations and generated text score lower |
| **What does not** | the $\epsilon$-equilibrium, which needs Assumption 4.1 to hold *and be common knowledge*, with an $\epsilon$ the paper does not measure; the payment; and the peer — with one answerer there is nothing to condition the prediction on and nothing to score against, and the model's own answer is not a peer, by the data-processing argument of [[mutual-information-paradigm]] |

## Limits

- The guarantee rests on Assumption 4.1 with an $\epsilon$ the authors never
  estimate; the experiments are one-sided sanity checks — degradations must
  score lower — and say nothing about whether truth is played.
- The same model family generated the synthetic reviews and, in the Judgment
  implementation, the predictions; Token uses a different model (Llama-2),
  which limits but does not remove the circularity.
- Proposition 4.4 conditions on a high-effort, truthful peer; with two
  shirking sources both score near zero and nothing flags it.
- Sentence-level degradation on Yelp reached only $-\log_{10} p \approx 1.8$:
  the ordering is robust on expert reviews and weak on short crowd reviews.
- `miller-2005` is cited as restated by Lu et al. (Definition 3.7,
  Proposition 3.8); the original was not read for this note.

## Related

[[peer-prediction]] · [[mutual-information-paradigm]] · [[correlated-agreement]] · [[tree-search-methods]] · [[surprisingly-popular-algorithm]] · [[novice-expert-problem]]

[^s1]: lu-2024
[^s2]: miller-2005
