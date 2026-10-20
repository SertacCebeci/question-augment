---
description: "A design space for exposing a spoken-query system's committed interpretation (candidates, context, confidence, scope) so users can inspect and repair it, rather than resolving ambiguity silently."
aliases: ["externalizing query interpretation", "interpretation state externalization", "post-commitment transparency"]
sources: ["lee-2026-player"]
---
# Interpretation externalization

> When a system must commit to one reading of an ambiguous query, the open
> question is not only which reading to pick but **how much of that
> commitment to reveal** — this design space names the dimensions of that
> reveal.

## Definition / Mechanism

Lee et al. study spoken queries in XR sports viewing that omit which
player, time window, field region, or metric is meant. Rather than
resolving the [[efe-planning-as-variational-inference|ambiguity]] implicitly and returning only a final answer, the
system externalizes the interpretation it committed to, along three
dimensions: **ambiguity type** (referential / spatial / temporal / metric —
what is underspecified), **interpretation state** (why the commitment
warrants exposure: the system considered *alternatives*, relied on
*context*, has variable *confidence*, or assumed a *scope*), and
**externalization strategy** (how it is shown: an operation — emphasize,
explain, compare, link — placed as situated, multi-view or overlay, on a
target of objects, stats or timeline, rendered as line, area, volume or
panel).[^c1]

The framework's contribution is explicitly not resolving ambiguity earlier
in the pipeline, but choosing **what to reveal after the system has already
committed to one reading**, shifting the design question from prevention to
post-commitment transparency.[^c2]

## Why it matters

For the answerer side of asking, this names the missing move between
"the system decided" and "the user can act on that decision": a taxonomy of
what a committed interpretation can show (which alternatives were
considered, on what basis, with what confidence, over what scope) so a
downstream repair loop has something concrete to correct.[^c3]

## Limits

Built and evaluated in one domain (soccer spectating in XR) with four
predefined [[ambiguity-taxonomy|ambiguity types]]; the paper itself states that generalization to
other domains needs new mappings from ambiguity types to visual cues and is
untested. The interpretation states (alternatives/context/confidence/scope)
were derived from one formative study (5 participants, 215 utterances), not
validated as an exhaustive or minimal set.[^c4]

## Related

[[visibility-action-gap]]

[^c1]: lee-2026-player
[^c2]: lee-2026-player — "Our framework instead addresses what to reveal after the system commits to one reading, shifting the design challenge from preventing ambiguity to making post-commitment interpretations transparent."
[^c3]: lee-2026-player — "The intended benefit of externalizing system interpretations is that users can inspect what the system decided, not just what it returned."
[^c4]: lee-2026-player — "Generalization would require sport-specific tracking/event data, entity identities, and mappings from ambiguities to visual cues and repair actions. Evaluation beyond soccer is needed to test this transfer."
