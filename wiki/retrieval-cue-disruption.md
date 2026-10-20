---
description: "Removing a constraint or vaguing a domain term from a code-generation prompt can raise correctness, when the removed wording had anchored the model to a memorized but wrong solution."
aliases: ["misleading retrieval cue", "over-fitted retrieval cue", "less-is-more prompt mutation"]
sources: ["arxiv-2604-24712"]
---
# Retrieval-cue disruption

> "Less is more": removing an important constraint leads to correct code
> because the constraint, not the missing information, was the problem.

## Definition / Mechanism

On a structurally rich benchmark (LiveCodeBench), Akli, Papadakis, Cordy & Le Traon (2026)
find that under-specification and lexical-vagueness mutations do not only
degrade correctness — degradations and improvements occur in near-equal
proportion (Fail→Pass to Pass→Fail ratio 0.99 on LCB against 0.40 on
HumanEval), so the near-zero *net* effect reported for rich prompts
([[specification-channel-redundancy]]) is two large opposing effects
canceling, not insensitivity.[^c1]

69 LCB tasks improve consistently across multiple models under mutation.[^c2]

Manual root-cause analysis of the improving cases locates the mechanism:
specific words, identifier names or constraint values in the *original*,
well-specified prompt act as **retrieval cues** that anchor the model to a
memorized solution pattern for a superficially similar, but different,
problem. Renaming a variable from a suggestive name breaks that retrieval
and forces reasoning from the problem description instead — 27% of
improving cases on lexical-vagueness mutations.[^c3]

Under under-specification, the dominant mechanism (39% of improving cases) is a
removed constraint line that had been priming a specific, incompatible
I/O-handling pattern (e.g. LeetCode-style parsing applied to a
competitive-programming stdin format); removing it forces a correct rewrite.[^c4]

A second mechanism (35%) is a numerical bound that activates a memorized
algorithmic shortcut misapplied to the actual problem — the source's
running example removes a `1 <= C_i <= 10^9` bound paired with a "beware
overflow" note that primed a `max_weight`-based formula; without the bound
the model runs the general two-BFS diameter algorithm and passes.

## Why it matters

This is a different failure mode from missing information: the model does
not fail to answer because it lacks a constraint, it fails because the
*wording carrying* the constraint or a domain term retrieves the wrong
memorized template, and the correct behavior — reasoning from the stated
problem structure — only appears once that wording is gone. For anyone
deriving how to phrase a task or question, this says specification
completeness is not sufficient for specification quality: a term or a
constraint can be simultaneously informative and actively misleading if the
answerer over-associates it with an unrelated, superficially similar
pattern. The design implication the source draws is not "under-specify" but
"neutralize each cue's associative pull" — the same effect that motivates
softening domain vocabulary is achieved without dropping the constraint's
information if the wording carrying it is chosen to avoid an existing
strong association.

## Limits

- Root-cause taxonomy percentages come from manual annotation of one
  model's transitions (Qwen-7B for the LV taxonomy, n=52; Claude-Sonnet-4
  for the US taxonomy) — not validated as the same distribution across all
  ten models tested for Pass@1.
- The mechanism is diagnosed retrospectively from cases that already
  improved; the source does not show a prospective rule for predicting,
  before mutation, which cues will turn out to be misleading versus
  load-bearing.
- Improvement is specific to benchmarks built from problems that resemble
  other, previously-seen problems closely enough to trigger memorized
  retrieval (competitive-programming platforms); a domain without a large
  corpus of near-duplicate solved problems may show no such effect.
- The label "retrieval cue" is the paper's own inferential account of *why*
  the mutation helps, inferred from manual reading of pass/fail transitions
  and code diffs, not from an interpretability method that inspects the
  model's internal retrieval.

## Related

[[specification-channel-redundancy]] · [[format-restriction-effect]] · [[mcq-answer-position-bias]] · [[presupposition-hallucination-gap]]

[^c1]: arxiv-2604-24712 — "Under-specification both harms and improves correctness, with these effects canceling out in rich prompts."
[^c2]: arxiv-2604-24712 — "we identify 69 LCB tasks that consistently improve pass rate under prompt mutations across multiple models, indicating that certain elements of the original specification can hinder correct code generation."
[^c3]: arxiv-2604-24712 — "Renaming key variables (e.g. s→seq, n,x→a,b) prevents retrieval of a memorised incorrect solution, forcing reasoning from the problem description."
[^c4]: arxiv-2604-24712 — "constraint-triggered wrong input parsing as the dominant mechanism (39%): specific constraint lines prime the model to write LeetCode-style I/O handling incompatible with the actual stdin format, and removing them forces a correct rewrite."
