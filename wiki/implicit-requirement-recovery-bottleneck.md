---
description: "Stage-attributed diagnosis of real coding-agent trajectories on 163 repository tasks finds implicit-requirement recovery, not planning or code generation, is the dominant failure stage."
aliases: ["SWE-RPG", "requirement-clarification bottleneck (SWE-RPG)"]
sources: ["zhou-2026-unified", "arxiv-2512-23707"]
---
# Implicit-requirement recovery bottleneck (SWE-RPG)

> When a coding agent fails on a real repository task, stage-attributed
> diagnosis against validated ground truth finds the failure is usually in
> recovering the implicit requirement — the axis of $W$ the issue text never
> states — more often than in planning or writing the code.

## Definition / Mechanism

Zhou, Chong, Kim et al. (2026) build SWE-RPG, a
repository-level issue-resolution benchmark of 163 tasks (113 bug fixes, 50
feature additions) across 31 Python/Java repositories, mined from merged
issue-PR pairs and reduced from 2000+ candidates through test-validation and
intermediate ground-truth validation. Each task carries, beyond the executable
patch oracle, a validated **Clarification GT** and **Plan GT**: the
Clarification GT is synthesized and cross-checked against the repository,
issue, PR discussion and developer patch, then classified into a
practitioner-derived six-category taxonomy (functional intent, business
semantics, technical context, interface/protocol specification, code
structure/conventions, data-structure semantics) built from seminar-style
interviews with ten experienced software engineers.[^c1]

Running three agent frameworks (Claude Code, Codex, OpenCode) against six LLM
backends (18 configurations) on SWE-RPG gives an average resolved rate of only
31.5%. Aligning each unresolved trajectory against the Clarification and Plan
GTs attributes its failure to a stage: "Requirement failure is the largest
component for most configurations (24.5–46.0%), followed by code-generation
(7.4–37.4%) and planning (5.5–17.8%) failures. This ordering identifies
implicit requirement [[recovery-postulate|recovery]] as the most common bottleneck."[^c2]

The same diagnosis shows outcome-only pass/fail scores can hide this: two
configurations with near-identical resolve rates (Codex– and Claude
Code–DeepSeek-V4-Pro, 40.5% vs. 39.3%) have markedly different
stage-attribution profiles — requirement-failure rates of 26.4% vs. 40.5%,
implementation/verification-failure rates of 23.9% vs. 7.4% — so a single
resolved-rate number conflates distinct causes of the same end result.[^c3]

## Why it matters

This is a measurement on stall 2 (which axis first?) in a live-agent setting:
the coding agent is not scored on ranking already-enumerated candidate axes,
but on recovering, unprompted, which unstated requirement of an entire
repository-grounded issue is the one it must satisfy — the same step
[[defect-localization]] isolates from a written specification with a
single injected gap. SWE-RPG measures it instead on real merged PRs, with
agents operating end-to-end rather than answering a location-and-classify
probe, and reports the finding as a range across 18 configurations rather
than one model's best score.

The same split between stated and unstated requirements shows up on the side of plan generation. In a research-plan training study, the rubric items for each research goal include ones that test "Some rubric items test constraints explicitly stated in the research goal" and others that "check for implicit features or requirements".[^c4] The human-study comments describe the gain on the implicit side: annotators noted that the finetuned plans "often include more rigorous evaluations for implicit aspects of the goal, whereas the initial model's plans were simpler but often vague or non-compliant with explicit constraints."[^c5] This is an observation about which requirements a plan covered, not a stage attribution of failures.

## Limits

- The Clarification and Plan GTs are synthesized by an LLM pipeline
  (GPT-5.4) from the issue, repository, and developer patch, then checked by
  a validation agent and two human authors for evidential support and
  consistency — the ground truth is constructed, not independently
  double-annotated from scratch, so its practitioner-derived taxonomy and
  the resulting failure attribution inherit whatever the synthesis-and-review
  pipeline missed.
- "Requirement failure" is attributed by comparing an agent's trajectory to
  the Clarification GT information points; the paper does not report a
  method for separating "the agent never surfaced the axis" from "the agent
  surfaced it but acted on it incorrectly downstream," so the 24.5–46.0%
  range is a stage attribution, not a pure detection-versus-repair split.
- All 163 tasks are real, merged, single-issue PRs from mature Python/Java
  repositories with existing tests; the result does not establish whether
  the same ordering (requirement > code-generation > planning failure) holds
  for greenfield work, non-bug-fix feature requests without a merged
  reference PR, or languages outside Python/Java.
- The research-plan paper does not attribute failures to stages. Its
  explicit-versus-implicit split is a property of rubric items that an LLM
  wrote from each source paper, and its evidence on the implicit side is
  annotator comment, not a count of missed requirements. The two papers
  therefore do not give the same ordering of bottlenecks, and neither one
  measures how often a model fails to recover an unstated requirement in
  the other's setting.

## Related

[[defect-localization]] · Selection · [[clarification-benchmarks]] · [[clarifying-interaction-decomposition]]

[^c1]: zhou-2026-unified
[^c2]: zhou-2026-unified — "Requirement failure is the largest component for most configurations (24.5–46.0%), followed by codegeneration (7.4–37.4%) and planning (5.5–17.8%) failures. This ordering identifies implicit requirement recovery as the most common bottleneck, while planning errors are also non-negligible."
[^c3]: zhou-2026-unified — "Codex– and Claude Code–DeepSeek-V4-Pro achieve similar resolve rates (40.5% versus 39.3%) but markedly different profiles: their requirement-failure rates are 26.4% and 40.5%, whereas their implementation/verification-failure rates are 23.9% and 7.4%. Similar end-to-end performance can therefore accompany distinct stage-attribution profiles."
[^c4]: arxiv-2512-23707 — "Some rubric items test constraints explicitly stated in the research goal"
[^c5]: arxiv-2512-23707 — "often include more rigorous evaluations for implicit aspects of the goal"
