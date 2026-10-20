---
description: "Once the missing part of a specification is pointed out, deciding *how* to Task 3 of Ma, Zhao, Wu,"
aliases: ["clarification action generation"]
sources: ["ma-2026"]
---
# Clarification action generation

> Once the missing part of a specification is pointed out, deciding *how* to
> resolve it — ask the author, or go look at existing artifacts — is a
> comparatively easy, well-solved step; almost none of the measured
> difficulty in asking about a broken specification sits here.

## Definition / Mechanism

Task 3 of Ma, Zhao, Wu, Patwardhan & Cohan's (2026) IdeaAMBIG[^s1]
benchmark hands a model a research-method specification together with its
annotated defect (category and description, the output of
[[defect-localization]]) and asks it to generate a clarification action:
either a **ClarificationQuestion** — a question addressed to the paper's
author or implementer — or **EvidenceSeeking** — an instruction to inspect
an existing artifact such as code or documentation. Success — Macro
Clarification Action Success Rate (Macro-CAS) — requires the generated
action to "address the blocker, obtain sufficient information, and avoid
unsupported assumptions" (Ma et al. 2026, Appendix F). Across 13 LLMs, the
best model reaches 80.6% Macro-CAS on real-world instances *given* the
defect's location — against 9.6% for locating that defect unaided
([[defect-localization]]).

## Why it matters

This is a direct, if narrow, empirical instance of the choice
[[uncertainty-decomposition]] poses on stall 4: once an unresolved point is
known, is it resolved by asking the user (here, the paper's author) or by
searching (here, inspecting the codebase, issue thread or documentation)?
IdeaAMBIG measures exactly that binary choice, in a domain — coding-agent-facing
research specifications — where both sources are usually available, and
finds it comparatively tractable once the location is given. Read together
with [[defect-localization]], the pairing says that for this domain almost
all of an asking pipeline's measured failure is upstream of the source
decision — in finding what to ask about, not in deciding who to ask or how
to phrase the request.

## Transfer

| | |
|---|---|
| In its home field | an LLM given a specification and an annotated implementation-critical gap, graded on whether its proposed question-or-evidence-seeking action would in fact resolve that gap |
| Here | the stall-4 choice [[uncertainty-decomposition]] already names between two concrete sources — ask the user, or search the world — now measured end-to-end as a generation task with a pass/fail criterion instead of assumed as a classification |
| What survives | the two-way source split (ask vs. seek evidence) as something a model can be scored on directly, and the finding that, given the location, the split itself is not the hard part |
| What does not | [[uncertainty-decomposition]]'s third branch (aleatoric — accept and proceed) is not modelled at all, since every instance here is constructed to have a resolvable gap, so nothing in this result bears on when *not* asking is correct; nor does the 80.6% figure separate wording quality from the ask-vs-search choice itself |

## Limits

- This is a single-paper, single-benchmark finding (ma-2026), not yet
  independently replicated; the 80.6% figure for real-world instances rests
  on the smaller real-cases subset of IdeaAMBIG (163 of 660 instances), not
  the full benchmark, and that subset is not separated out further in the
  abstract-level numbers used here.
- Macro-CAS is graded by an LLM judge validated against human annotations
  (per the source); no inter-annotator agreement figure was read here, so
  the 80.6% number carries whatever noise that judge has.
- The task is conditioned on a correct, given defect location; in the
  unconditioned pipeline (locate, then act) end-to-end success is bounded
  by the 9.6% localization figure, not by 80.6% — the two numbers describe
  different, non-composable stages, a point the abstract itself makes but
  that is easy to read past.
- Only two action types are scored (ClarificationQuestion, EvidenceSeeking);
  whether a real coding agent has other resolution moves available — e.g.
  proceeding under a stated assumption — is outside what this task measures.

## Related

[[uncertainty-decomposition]] · [[defect-localization]] · Source · [[clarification-request]] · [[self-ask-decomposition]]

[^s1]: ma-2026
