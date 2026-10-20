---
description: "RPTS prices a compound-agent design choice by its mean-return gain over a baseline per kilotoken consumed, ranking context, deliberation and hierarchy choices on cost-effectiveness."
aliases: ["RPTS", "returns per token spent"]
sources: ["bogdanov-2026"]
---
# Returns per token spent (RPTS)

> A design choice that improves the outcome is not automatically worth its
> inference cost; RPTS normalizes the gain by the tokens it took to get it.

## Definition / Mechanism

Bogdanov et al. (2026) define returns per token spent as the mean return
improvement of a configuration over an observation-only baseline, per
kilotoken consumed: $\mathrm{RPTS} = (G_{\text{config}} -
G_{\text{obs}})/\mathrm{KTok}_{\text{config}}$, where $G$ is mean episode
return and $\mathrm{KTok}$ is total tokens per episode in thousands.
"RPTS identifies which design choices deliver the largest gains per unit of
inference budget; negative values indicate configurations that perform worse
than unstructured observation alone."[^c1]

Applied across twelve architecture configurations (context representation,
deliberation tools, hierarchical delegation) on six LLMs, programmatic
context abstraction had the largest RPTS of any axis, improving mean return
by up to 76% over raw observations; on the resulting cost-performance Pareto
frontier (tokens per episode vs. mean return), a context configuration was
efficient for every model, deliberation configurations reached the frontier
for only a minority of models, and hierarchy-with-deliberation
(`hier-delib`) was dominated by hierarchy-without-deliberation on every
model — higher token cost and worse return.[^c2]

## Why it matters

RPTS gives a selection criterion for *architectural* choices (which axis of
a compound agent's design — what it sees, how much it deliberates, how tasks
are split — to invest in) that is normalized by inference cost rather than by
outcome alone, playing a role for architecture selection analogous to what
[[value-of-information|value of information]] plays for query selection: not "does this help" but
"how much help per unit spent." In this study it is what exposes that adding
a self-questioning/self-critique tool is rarely on the efficient frontier,
while a cheap deterministic state-tracking layer usually is.[^c3]

## Limits

- $G_{\text{obs}}$ is a per-model baseline; RPTS values are not comparable
  across models or across environments without renormalizing to a new
  baseline.
- Defined for a non-positive, penalty-only reward (return closer to zero is
  better); the sign convention does not automatically carry over to a
  reward-positive task.
- Reported only for CybORG CAGE-2 with six models from five families; the
  paper does not test RPTS as a general-purpose architecture-selection
  metric outside this study.

## Related

[[value-of-information]] · [[deliberation-cascade]] · [[bounded-rationality]]

[^c1]: bogdanov-2026
[^c2]: bogdanov-2026 — "Programmatic state abstraction delivers the largest returns per token spent (RPTS), improving mean return by up to 76% over raw observations."
[^c3]: bogdanov-2026 — "Context configurations occupy the low-cost efficient region; hier-delib is high-cost and dominated."
