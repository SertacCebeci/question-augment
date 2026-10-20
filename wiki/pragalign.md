---
description: "A pre-generation decision layer that tags context as observed, inferred, or unknown, then asks at most one clarifying question only when an unknown field could change the reply."
aliases: ["PragAlign"]
sources: ["zhong-2026"]
---
# PragAlign

> Ask only when a field would change the reply — and even then, ask at most
> one question.

## Definition / Mechanism

PragAlign is a two-module decision layer inserted before a fixed reply
generator in a reply-drafting agent. The Context Reader maps the public
input $x$ (request, incoming message, supplied scenario context) to an
evidence-tagged frame $z$; the Gap Policy then selects an action $a \in
\{\text{PROCEED}, \text{ASK}\}$ and, when needed, one clarification question
$q$: "The Context Reader maps x to an evidence-tagged frame z, and the Gap
Policy selects an action a ∈ {PROCEED, ASK} and, when needed, one
clarification question q." Each field of the frame is labeled OBSERVED,
INFERRED, or UNKNOWN.[^c1]

The Gap Policy does not act on any unknown, only on one that matters: "A
consequential context gap is an unknown whose resolution could change the
reply." Gap types cover facts, audience, permission, channel, urgency,
recipient goal, and reply language; the policy targets at most one such
field per turn rather than enumerating every UNKNOWN one.[^c2]

Both modules are supervised views of the same base model (Qwen3-8B,
LoRA/QLoRA adaptation) trained on matched PROCEED/ASK counterfactual pairs
built from controlled pragmatic vignettes; the final generator itself is
not fine-tuned, so the comparison isolates the decision layer, not
generation quality. It is compared against Direct (send $x$ straight to the
generator) and Rule (Direct plus a generic relationship/channel/tone
instruction, with no evidence-status distinction and no question).

## Why it matters

In a two-language human evaluation (nine native Chinese speakers over 90
participant-case blocks, three native Japanese speakers over 30 blocks;
ten matched scenario roots, five simple and five complex; three anonymized
replies ranked 1–3 per block), PragAlign was rated most appropriate more
often than either baseline in Chinese but not decisively in Japanese: "In
the Chinese evaluation, PragAlign achieved a mean rank of 1.61 (95% CI
[1.47, 1.76]) and was ranked first in 51% of blocks. The overall difference
was significant (χ2 (2) = 22.87, p < .001, Kendall's W = 0.13)." PragAlign's
Chinese advantage held in both complexity strata and was not driven by one
rater (lowest mean rank for eight of nine Chinese participants).[^c3]

In Japanese, "Direct had the lowest mean rank, PragAlign had the highest
top-rank rate, and the omnibus difference was not significant" (Friedman
p = .497, n = 3 speakers), so the Chinese-language effect of selective
clarification did not replicate at that sample size. The two language
groups nonetheless picked the same top-ranked condition in 5 of 10 matched
scenarios, four of them PragAlign; qualitative coding of the raters'
explanations found "the Chinese data, favorable judgments emphasize
actionable commitments and social fit," while the Japanese explanations'
"favorable judgments centered on politeness" — the two language groups
converged on rewarding selective clarification in half the scenarios while
applying different criteria for what makes a reply appropriate.[^c4]

## Transfer

Not applicable in the imported-formalism sense: the paper's own
decomposition ("when to ask, what to ask, how to use the answer") is drawn
from prior clarification research already native to this wiki's subject,
not carried in from an outside field's theorem or algorithm.

## Limits

The Japanese arm has three raters and 30 blocks against nine raters and 90
blocks in Chinese, and its omnibus test is not significant — the claim that
selective clarification generalises across languages rests on the Chinese
result plus a non-significant, same-direction top-rank tendency in
Japanese, not on two positive replications. Scenarios are synthetic
vignettes built for public/withheld separation and one answerable gap, with
one LLM family (Qwen3-8B) as both trained modules; the generator is fixed
and untuned, so the result measures the decision layer's effect on a
scripted reply, not on a deployed multi-turn agent or on language pairs
beyond Chinese/Japanese.[^c5]

## Related

[[interopt-gap-guided-clarification]] · [[clarification-request]] · [[clarification-benchmarks]] · [[value-of-information]]

[^c1]: zhong-2026 — "The Context Reader maps x to an evidence-tagged frame z, and the Gap Policy selects an action a ∈ {PROCEED, ASK} and, when needed, one clarification question q"
[^c2]: zhong-2026 — "A consequential context gap is an unknown whose resolution could change the reply."
[^c3]: zhong-2026
[^c4]: zhong-2026 — "Direct had the lowest mean rank, PragAlign had the highest top-rank rate, and the omnibus difference was not significant"
[^c5]: zhong-2026 — "three native Japanese speakers judged matched Japanese versions"
