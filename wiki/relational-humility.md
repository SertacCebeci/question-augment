---
description: "Whether an abstention is trusted depends on two separable properties — whether it is epistemically warranted and whether it is relationally delivered — not one."
aliases: ["relational humility", "service-oriented pivot", "epistemic humility versus relational humility"]
sources: ["arxiv-2604-17843"]
---
# Relational humility

> Declining correctly and declining well are two different problems, and a
> system that solves only the first is heard as rude.

## Definition / Mechanism

Karnatak et al. (2026) deploy AVA, a retrieval-grounded
answerer for policy analysts that abstains under a fixed evidence-verification
threshold, and observe that a correct abstention still costs trust when it is
delivered as a bare refusal. They import **relational humility** from
interpersonal psychology — there, an observer's judgment that a person shows
an accurate self-view, an other-oriented stance and non-superior behavior —
and redefine it for an AI system as the property that emerges when the system
"(1) communicates its limits; (2) remains oriented to the user's goals... by
explaining why an answer cannot be verified and suggesting constructive next
steps; and (3) adopts collaborative, non-superior language."[^c1]

They separate this from **epistemic humility**, the property [[abstention]]
already covers: "epistemic humility concerns acknowledging limits in
knowledge and deciding when to abstain," a property of the selection function
$g(x)$ itself, independent of what the system says when $g(x)=0$. "Relational
humility concerns the interactional stance through which those limits are
communicated and managed to preserve collaboration and trust" — a property of
the abstention's surface form, not its trigger condition.[^c2]

The two are independent: a correctly triggered abstention can still fail
relationally. Interview participants "interpreted abstentions as 'rude' or a
violation of partnership," wanting a more humanised persona even when the
refusal was evidentially warranted.[^c3]

The design fix they propose is a fixed transformation of the refusal's
surface form, not a change to the abstention trigger: replace the bare "I
don't know" with a **service-oriented pivot** — "I cannot verify X, but I
can help you explore Y" — pairing the epistemic refusal with a relationally
humble redirection.[^c4]

## Why it matters

[[abstention]] gives the answerer a selection function $g$ and asks what
price its output carries; it is silent on how $g(x)=0$ is *phrased*. This
framework adds a second, orthogonal axis: for a fixed $g$, the same refusal
can be received as a trustworthy boundary or as a partnership violation,
depending only on delivery. A system tuned only on selective-risk metrics can
be epistemically optimal and still lose users to the relational failure mode
this note names — abstention correctness does not certify abstention
reception.

## Limits

- Single deployment, qualitative interview evidence (20 interviews out of
  2,200+ users); the three-part definition is the authors' operationalisation
  of a psychology construct, not independently validated for AI systems.
  [?]
- The paper does not measure whether the "service-oriented pivot" phrasing
  changes actual trust or usage outcomes — only that its absence was reported
  as a complaint; the fix is a design recommendation, not a tested
  intervention. [?]
- Relational humility is defined here only for refusals; the paper does not
  test whether the same construct affects reception of a *confident* answer.

## Related

[[abstention]] · [[assistant-personality-style]] · [[calibration]] · Commitment

[^c1]: arxiv-2604-17843
[^c2]: arxiv-2604-17843 — "While epistemic humility concerns acknowledging limits in knowledge and deciding when to abstain, relational humility concerns the interactional stance through which those limits are communicated and managed to preserve collaboration and trust."
[^c3]: arxiv-2604-17843 — "some participants interpreted abstentions as ‘rude’ or a violation of partnership, expressing a desire for a ‘brother-like’ persona that felt more humanised."
[^c4]: arxiv-2604-17843 — "refusals should function as “service-oriented” pivot (e.g., ‘I cannot verify X, but I can help you explore Y’). Consequently, the design lesson is to pair rigorous abstention with relational humility as part of the end-to-end trust pipeline."
