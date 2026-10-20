---
description: "A retrieval pipeline classifies a query by reasoning type, checks retrieved evidence against a per-type checklist, and turns unmet items into follow-up sub-queries."
aliases: ["diagnostic check", "evidential gap check"]
sources: ["nakarmi-2026"]
---
# Reasoning-gap-driven retrieval

> Do not ask "is this relevant" of retrieved evidence — ask "what kind of
> claim does this query need, and which piece of that is still missing."

## Mechanism

Nakarmi et al. (2026) build a RAG pipeline for consequential
scientific question answering (water-quality outreach) around a two-stage
audit of retrieved content: a prognostic check that drops low-utility chunks,
and a diagnostic check that finds what is still missing. The diagnostic check
first classifies the query into one of four reasoning strategies, each with
its own evidential requirement: "Causal queries ask why a problem exists and
require causes, mechanisms, and confounders. Regulatory queries ask which
rules or thresholds apply and require relevant policy text, compliance
status, and practical implications. Comparative queries ask how current
conditions differ from past measurements or standards and require reference
points and the significance of the difference. Explanatory queries ask about
unfamiliar terms and require definitions, analogies, and context for
non-experts."[^c1]

Each strategy is operationalized as a fixed set of diagnostic questions; the
retrieved content is checked against them, unanswered ones are flagged as
evidential gaps, and each gap becomes a targeted follow-up sub-query for a
second retrieval pass (capped at two iterations, since later rounds show
diminishing returns). This is the mechanism that selects the next axis to
query: not a similarity re-score of the whole remaining space, but a lookup
against the checklist implied by the query's own reasoning type.

Ablating this against a single-pass RAG baseline on 160 community queries,
"all variants exhibited a significant, 25-fold reduction in context size
(χ2 = 151.02, all adjusted p < 0.001)... human-rated completeness increased
from 0.60 (baseline) to 0.711–0.751 across filtered variants."[^c2]

The diagnostic check's own contribution is uneven by reasoning type: the
prognostic-only variant reached the same completeness gain as the full
diagnostic variants, and "structured regulatory queries are highly tractable
(86.4% filled), whereas causal queries remain the primary failure mode
(56.8% filled)."[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Information retrieval (this paper) | diagnostic check | exact |
| Information retrieval (this paper) | evidential gap check | exact |

## Why it matters

Stall 2 asks which axis to constrain next. This mechanism
answers it with a taxonomy over query types rather than a value function:
the next question is whichever checklist item for this query's reasoning
type is unanswered, not the item with the highest expected information gain.
It is a generator in the sense Axes already uses — a fixed
enumeration of what a causal, regulatory, comparative or explanatory query
needs — rather than a scored criterion like [[mutual-information]] or
[[expected-information-gain]].

## Limits

- Read from one deployment (water-quality outreach, GPT-5.2 generator,
  Mistral-7B diagnostic model); the four-strategy taxonomy is built from this
  community's interactions and is not shown to generalize to other domains.
- The paper's own ablation shows the completeness gain comes mostly from the
  prognostic (relevance-filtering) step, not from the diagnostic gap-check
  specifically — filling evidential gaps did not yield a statistically
  significant additional completeness gain, and the coupling to reasoning
  strategy vanished in human ratings (χ2 = 2.69, p = 0.44). The mechanism is
  reported here for its selection logic, not as an established source of the
  completeness improvement.
- No comparison to a scored selection criterion (EIG, mutual information) on
  the same task is run, so whether the checklist approach out-performs a
  value-function approach here is untested, only that it is cheaper.

## Related

Selection · [[mutual-information]] · [[expected-information-gain]] · [[clarification-benchmarks]]

[^c1]: nakarmi-2026
[^c2]: nakarmi-2026
[^c3]: nakarmi-2026
