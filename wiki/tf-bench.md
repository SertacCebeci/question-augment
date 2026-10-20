---
description: "A benchmark scoring pre-question research assistance on tacit, unarticulated inputs by novelty, feasibility and impact, split by domain-related versus domain-unrelated ambiguity."
aliases: ["TF-Bench", "tacit-to-explicit benchmark"]
sources: ["yu-2026-more"]
---
# TF-Bench

> Existing research-idea benchmarks start from an already-stated question;
> TF-Bench starts one step earlier, from a vague expression of unease, and
> scores the proposal that eventually gets asked — an outcome measure for
> the whole stall, not for any one selection rule.

## Definition / Mechanism

TF-Bench is built because "existing datasets cannot be directly applied to
this setting because they typically presuppose that the input is already
an actionable research question rather than an inchoate intuition
fragment."[^c1]

It partitions its 52 stimuli (4 domains × 13 items) into two ambiguity
types — domain-related prompts that "already carry scientific domain
signals yet remain under-specified" and domain-unrelated prompts that
"carry only weak metaphorical or conceptual cues" — across four scientific
modes chosen to cover core empirical-science tasks: prediction, discovery,
attribution and causality.[^c2]

Proposals are scored by novelty, feasibility and impact (1–5 scale, LLM
judges, 5 runs, mean ± s.d.). On the paper's own InciteResearch system
versus a direct-prompting baseline: "the novelty and impact of
InciteResearch reach 4.172 / 4.378, while Prompt-based LLM achieves 3.888 /
3.978" under domain-related inputs, and "under the condition of
domain-unrelated human inspiration, the novelty and impact of
InciteResearch are instead higher than under the domain-related condition,
increasing to 4.328 / 4.416, while Prompt-based LLM drops to 3.454 /
3.626."[^c3]

LLM-judge scores are checked against 26 human-rated proposals in one
domain: "the agreement between LLM evaluators and human experts reaches
κ = 0.624, indicating moderate agreement, while the agreement between the
human professors reaches κ = 0.748."[^c4]

## Why it matters

TF-Bench's domain-related/domain-unrelated split is itself a finding about
selection under unknown axes: a system that only recombines within a given
frame (the baseline) loses novelty and impact once the frame is weakened,
while a system that first elicits the axis before selecting a question
(InciteResearch, via [[friction-point-elicitation]]) gains instead — the
benchmark locates the value of axis-discovery specifically in the
low-signal regime where which-axis-first is hardest to answer.[^c5]

## Limits

- Novelty/feasibility/impact are LLM-judge scores; the only human check
  is 26 proposals in one of four domains, with moderate (κ = 0.624) rather
  than high LLM-human agreement, so the headline numbers are not
  independently confirmed at benchmark scale.
- 52 stimuli total (13 per domain, 10 domain-related + 3 domain-unrelated
  each); small enough that a single hard item can move a domain's mean.
- Stimuli were LLM-generated (Grok 4.3) and human-refined rather than
  drawn from real, dated researcher friction; whether they reproduce the
  distribution of tacit unease actual scientists start from is untested.
- Single arXiv preprint (2026), not peer reviewed.

## Related

[[friction-point-elicitation]] · [[expected-information-gain]] · [[clarification-benchmarks]]

[^c1]: yu-2026-more
[^c2]: yu-2026-more — "The former comprises prompts that already carry scientific domain signals yet remain under-specified; the latter comprises prompts that carry only weak metaphorical or conceptual cues."
[^c3]: yu-2026-more — "the novelty and impact of InciteResearch reach 4.172 / 4.378, while Prompt-based LLM achieves 3.888 / 3.978"
[^c4]: yu-2026-more — "the agreement between LLM evaluators and human experts reaches κ = 0.624, indicating moderate agreement, while the agreement between the human professors reaches κ = 0.748"
[^c5]: yu-2026-more — "under the condition of domain-unrelated human inspiration, the novelty and impact of InciteResearch are instead higher than under the domain-related condition"
