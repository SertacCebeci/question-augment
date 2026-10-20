---
description: "A four-factor patience score updates a simulated shopper's tolerance each turn from recommendation relevance, question relevance and redundancy, response complexity, and informativeness."
aliases: ["patience modeling", "multi-factor utilitarian patience framework"]
sources: ["harne-2026"]
---
# User patience model

> A simulated user's willingness to keep answering is tracked as a running
> score, not a fixed turn budget: it rises when a question is relevant and
> not yet asked, and falls when a question repeats, targets an attribute
> the target item does not have, or the response is hard to follow — and
> the session ends once it runs out.

## Definition / Mechanism

Patience $\pi^t$ starts at 1 and is updated after every assistant turn from
four factors: "Our model determines session abandonment based on four
factors: recommendation relevance, attentiveness, cognitive load, and
informativeness... We initialize user patience $\pi^t$ at turn $t=0$ as
$\pi^0=1$ and update it according to (8) after each assistant response
$b_t$."[^c1]

Question inattentiveness is scored by a lookup on two conditions — is the
attribute relevant to the target item, and was it already asked — with a
distinct penalty or reward for each of the four combinations: "we assign an
inattentiveness score $\pi_a$ using: $\beta_{tu}$, relevant and not asked
before; $\beta_{ta}$, relevant but already asked; $\beta_{nu}$, irrelevant
and not asked before; $\beta_{na}$, irrelevant and already asked... we
expect that $\beta_{tu} < \beta_{ta}$; $\beta_{nu} < \beta_{na}$, and
$\beta_{tu} < \beta_{nu}$."[^c2]

The four terms combine additively, with relevance and informativeness
raising patience and cognitive load and inattentiveness lowering it:
"$\pi^{t+1} = \pi^t + \lambda_r \pi_r - \lambda_a \pi_a - \lambda_c \pi_c +
\lambda_i \pi_i$."[^c3]

The conversation ends once patience is exhausted: "A session ends if
patience is exhausted, capturing realistic abandonment behavior in online
shopping."[^c4]

## Known as

| Field | Name there | Match |
|---|---|---|
| conversational-recommendation | patience modeling | exact |
| conversational-recommendation | multi-factor utilitarian patience framework | exact |

## Why it matters

This gives the selection criteria on this stall a cost side that most of
them (EIG, GBS, VoI) leave implicit: a question is not merely more or less
informative, it is more or less tolerable, and the same question (repeated,
or about an attribute the target item lacks) costs more than an equally
uninformative but novel one. Coupled with
[[d2d-attribute-informativeness-score]], reducing this modeled abandonment
rate by 6.6–16.1% is reported as a *consequence* of the informativeness
scoring, not an independent optimization target — the paper does not report
optimizing question choice directly against $\pi$.

## Limits

The four weights $\beta_{tu}, \beta_{ta}, \beta_{nu}, \beta_{na}$ and
$\lambda_r, \lambda_a, \lambda_c, \lambda_i$ are fixed by the experimenters
(not fit to human data) and only their rank order, not their values, is
argued for in the material read here. Relevance and informativeness are
themselves LLM judgments (an LLM rates each response's complexity and
informativeness 1–10), so the patience score is one LLM's model of a
simulated user's tolerance for another LLM's questions, two steps removed
from a measured human abandonment rate; the paper's separate human user
study is mentioned in the abstract but not detailed in the slices read.
[?] no independent replication found.

## Related

[[d2d-attribute-informativeness-score]] · [[bounded-rationality]] · [[value-of-information]] · [[stage-dependent-elicitation-strategy]]

[^c1]: harne-2026
[^c2]: harne-2026
[^c3]: harne-2026 — "π t+1 = π t + λr πr − λa πa − λc πc + λi πi"
[^c4]: harne-2026 — "A session ends if patience is exhausted, capturing realistic abandonment behavior in online shopping."
