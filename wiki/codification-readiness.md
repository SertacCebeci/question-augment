---
description: "Whether a research-method specification says enough for someone who did not Ma, Zhao, Wu,"
aliases: ["codification readiness", "codification-ready rate"]
sources: ["ma-2026"]
---
# Codification readiness

> Whether a research-method specification says enough for someone who did not
> write it to build the intended method without guessing — and, measured by
> an oracle, almost the whole gap between "cannot be built" and "can" turns
> on a single missing answer.

## Definition / Mechanism

Ma, Zhao, Wu, Patwardhan & Cohan (2026) define a specification as[^s1]
**codification-ready** when "a competent implementer or coding agent can
construct a faithful initial implementation or experimental prototype
without unsupported assumptions about the core method" — a binary
Ready/NotReady judgement, evaluated as Task 1 of their IdeaAMBIG benchmark
(660 evidence-grounded instances: 163 real gaps mined from reproducibility
reports and GitHub issues, 497 synthetic gaps injected into references
already verified buildable). In an oracle study — the model is handed the
resolution a human annotator or reproduction artifact supplies for the one
gap present in each instance — supplying that single missing piece of
information raises the downstream codification-ready rate from 14% to 98%
(Ma et al. 2026, abstract).

## Why it matters

On stall 7 (is $|W|$ small enough?) this gives a domain where "enough" has
an outside, task-defined test — can a third party build the thing — rather
than a threshold the asker sets on its own uncertainty, alongside the four
rules in [[stopping-rules]]. The oracle number says something sharper than
"one more answer helps": for the specifications in this benchmark, closing
exactly one identified gap moves the instance almost the whole way from
unbuildable to buildable (14%→98%), which means most of the $|W|$ these
specifications leave open is concentrated on a single unresolved axis, not
spread thin over many small ones.

## Transfer

| | |
|---|---|
| In its home field | a research-method specification read by a competent implementer or coding agent trying to reproduce or build the described method, judged against whether the implementation would need an unsupported guess |
| Here | any spec-driven asking agent's stall-7 test: "have I asked enough to act" reframed as "would a third party need to guess to act on what I have" |
| What survives | the operational test itself (would an implementer have to guess), and the finding that closing one gap can flip an instance from not-ready to ready almost completely |
| What does not | the domain (ML research-method text specifically), the 14%/98% figures (measured on this benchmark's mix of real and injected single gaps, not on multi-gap or non-research specifications), and the assumption that exactly one gap is present — a real specification may carry more than one |

## Limits

- The 14%→98% figure comes from an oracle study in which the *correct*
  resolution is supplied; it bounds how much a specification's readiness
  can improve *if* the right gap is found and correctly resolved, not how
  often an agent manages that unaided — the same paper measures those two
  steps separately as [[defect-localization]] (9.6% success) and
  [[clarification-action-generation]] (80.6% success given the location).
- Ready/NotReady is one paper's operationalisation of "enough", read from
  its abstract and Task 1 description; it is a single source (`ma-2026`),
  not yet independently replicated, and its own construction assumes a
  single injected or documented gap per instance.
- The benchmark is built for research-method specifications aimed at coding
  agents; whether "would a third party need to guess" transfers to
  specifications without a competent-implementer audience — e.g. a request
  made to a human collaborator rather than to code — is not tested here.

## Known as

| Field | Name there | Relation |
|---|---|---|
| software-engineering (Ma et al. 2026) | codification-ready rate | exact — the aggregate, over a benchmark, of the same binary Ready/NotReady property |

## Related

Stopping · [[stopping-rules]] · [[defect-localization]] · [[clarification-action-generation]] · [[qualitative-saturation]] · [[abstention]]

[^s1]: ma-2026
