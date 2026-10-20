---
description: "A why-chain climbed one rung at a time until the answer stops being a Taiichi Ohno, who built the Toyota Production System, states the rule as *repeating \"why\" five times*,"
aliases: ["5 whys", "laddering"]
sources: ["ohno-1988", "gutman-1982", "reynolds-1988", "card-2017"]
---
# Five whys

> A why-chain climbed one rung at a time until the answer stops being a
> mechanism. **Where it stops** is the decision this note is about.

## The Toyota form — Ohno (1988)

Taiichi Ohno, who built the Toyota Production System, states the rule as[^s1][^s2][^s3][^s4]
*repeating "why" five times*, and his worked example runs exactly five rungs:
the machine stopped → an overload blew the fuse → the bearing was
under-lubricated → the lubrication pump was not pumping → the pump shaft was
worn → no strainer was fitted and metal scrap got in. The English text is
Productivity Press's 1988 translation of the 1978 Japanese original.

Two properties of this form: the chain is **unidirectional** (it climbs
toward cause, never descends toward mechanism) and **single-track** (one
answer per rung). "Five" is Ohno's number; reading five as a heuristic depth
rather than a count is later practice, not his wording.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Root-cause analysis / TPS | 5 whys | **exact** — the same object under Ohno's own name |
| Consumer research (Gutman 1982; Reynolds & Gutman 1988) | laddering | **close** — the same climb from a concrete attribute to the reason behind it, but a *bidirectional* in-depth interview technique with a probe protocol, aimed at eliciting an informant's hierarchy rather than at locating a fault; its evidence base is consumer interviews |
| Consumer research | means-end chain | **not this concept.** Gutman (1982) names the attribute → consequence → value *structure* that laddering elicits, not a way of asking. A structure is not a method; it wants its own note. |

## The stopping rule — two answers, not one

Both traditions climb; they terminate on different tests.

| | Terminates at | Test at each rung |
|---|---|---|
| Ohno (1988) | a cause a countermeasure can be attached to | can you act on this one? |
| Gutman (1982); Reynolds & Gutman (1988) | a terminal value — a desirable end-state | is the answer an end-state rather than a means to one? |

The wiki's compressed form — *continue while the answer is a mechanism, stop
when it is a goal* — is a compression of these two, not a quotation of
either. Laddering also supplies a direction Ohno's form lacks: ladder **down**
("how will this happen?") from a value to a concrete attribute. Reynolds &
Gutman's interviews move both ways; Ohno's chain does not.

## Why it matters

The climb is the human-side counterpart of the change-a-decision test in
[[value-of-information]]: a rung is worth asking for only if its answer
would alter what you then do. This is also the same move as going up an
[[issue-tree]] — laddering up is climbing toward the root question.

**This note's own inference, not a result of any source cited here:** a rung
higher in the chain constrains more decisions below it, so a purpose question
is *plausibly* worth more than the mechanism question one rung down. Nothing
in Ohno, Gutman, or Reynolds & Gutman orders the two, and no field has put a
ratio on it; the earlier "order of magnitude" reading of this note was
unmeasured and is withdrawn.

## Its danger — climbing past the last useful rung

"Why this feature? → so the user is happy → why? → so the company earns."
At that rung the answers converge on end-states shared by every option on the
table, so no answer discriminates between designs. In VoI's vocabulary the
climb has passed the last rung that could change an action — the reason the
stopping rule is better stated as *stop at the last rung whose answer would
change what you build* than as *stop at the value*.

## Transfer

| | |
|---|---|
| In its home field | [[value-of-information]] (Howard 1966): a utility $U$, a fixed decision set $A$, a prior. A question is worth asking iff its answer can change $\arg\max_a \mathbb{E}[U(a)]$. |
| Here | a natural-language why-chain with **no** utility and **no** enumerated decision set; the "decision" is the countermeasure (Ohno) or the design/message choice (Reynolds & Gutman). |
| What survives | the change-a-decision criterion used qualitatively as a stopping test: keep climbing while some answer at this rung would alter the countermeasure; stop at the first rung where every answer leaves it unchanged. |
| What does not | every number. Without $U$ and $A$ there is no computable $\mathrm{VoI}(q)$, no magnitude ordering between two rungs, and no literal zero — "VoI collapses" above is a verbal analogy for "no answer changes the action", and the purpose-over-mechanism ordering is this note's conjecture. |

## Limits

- Ohno's form assumes a single causal track. Card (2017, *BMJ Quality &
  Safety*), reviewing '5 whys' as promoted in healthcare, argues it is
  oversimplified and pushes teams to one root cause — often one at the end of
  the error chain — so that upstream causes and their corrective actions are
  missed; he recommends tools that carry several causes at once, such as
  fishbone diagrams. Where causes interact, the chain is the wrong instrument.
- The goal/mechanism stopping rule above is this wiki's compression of two
  different termination criteria; neither source states it in that form.
- Laddering's evidence is consumer interviews and rests on informants' own
  accounts of their reasons; Reynolds & Gutman's probe protocol manages the
  post-hoc-rationalisation risk but does not remove it.
- The purpose-vs-mechanism ordering is this note's own inference, unmeasured,
  and inapplicable wherever no utility function and no fixed decision set
  exist — exactly the exploration case [[value-of-information]]'s own Limits
  excludes.
- The four source keys were added on 2026-09-10 and have not yet been
  re-checked by the verifier; any key it cannot confirm becomes `[?]` and the
  attribution resting on it falls with it. `ohno-1988` is a translation of a
  1978 Japanese text, so wording attributed to it is the translator's.

## Related

[[value-of-information]] · [[issue-tree]] · [[context-free-questions]] · [[ambiguity-taxonomy]]

[^s1]: ohno-1988
[^s2]: gutman-1982
[^s3]: reynolds-1988
[^s4]: card-2017
