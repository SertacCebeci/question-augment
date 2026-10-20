---
description: "Whether a multi-turn asker's acquired constraints determine the target variable uniquely, scored against the problem's own ground truth and independently of whether the final answer is correct."
aliases: ["final sufficiency"]
sources: ["huang-2026"]
---
# Final sufficiency

> A stopping check that does not read the asker's answer: has the acquired
> assignment fixed the target, whatever the asker goes on to say?

## Definition / Mechanism

For sequential task solving on a [[k-underspecified-csp|k-underspecified
CSP]], the source reports final accuracy (whether the predicted value
equals the true target) *and* final [[sufficient-statistic|sufficiency]] (whether the acquired
information determines the target uniquely), computed from the problem's
constraints and the queried assignments alone.[^c1]

Separating the two exposes failures final accuracy alone hides. Across
models on Logic-Q-MT, k-prediction accuracy — a multiple-choice guess at
how many variables are missing — falls below 0.5 once $k \geq 2$, and the
errors are asymmetric: at $k=2$, where the answer choices are balanced
above and below the truth, models pick a value smaller than the true $k$
more than four times as often as a larger one — systematic underestimation
of how much is still missing, not random miscalibration.[^c2]

Final sufficiency also separates a bad first query from a bad search.
Restricting to $k\geq2$ tasks and comparing interactions whose first query
hits the minimal sufficient set against interactions that miss on the first
turn but hit on the second, the source finds the gap in final sufficiency
is small: "within 5 percentage points for 12 out of 14 models, and within
10 percentage points for all models" on Logic-Q-MT — a wrong first query is
recoverable if the asker keeps searching.[^c3]

Where the underlying task has ordered dependencies (an earlier finding
determines which later variable is relevant), final accuracy is not
explained by coverage of the sufficient set alone: "following the correct
query order consistently improves final accuracy both in MSS fully covered
and partially covered interactions," and in a regression across coverage,
order and per-query correctness, order correctness is consistently the
second-strongest predictor after coverage.[^c4]

Final sufficiency does not by itself predict final accuracy: models whose
questions carry similarly high [[expected-information-gain|expected information gain]] can still differ
substantially in final accuracy, "indicating that success also depends on
how well they use the collected answers" once they have them.[^c5]

## Why it matters

Benchmarks that score only whether the final answer is right conflate two
failures a stopping mechanism needs to tell apart: stopping too early (the
constraints do not yet fix the target) and stopping at the right point but
reasoning to the wrong answer from what was gathered. Final sufficiency is
a ground-truth check on the first failure alone, computed from the CSP
rather than elicited from the asker.

## Limits

- Computable only where the CSP's constraints and the queried variables'
  values are known to the evaluator — the four structured domains built on
  [[k-underspecified-csp]]; the source's fifth domain ([[twenty-questions|20 Questions]]) has no
  predefined variable set and final sufficiency is not reported there.
- The order-correctness finding (ClinGuide-MT) is one domain with
  LLM-simulated oracles, not a manipulated-order experiment across all four
  structured domains.
- Everything above rests on one source (huang-2026), read once; per-model
  breakdowns and the regression's full coefficients are in its appendix and
  were not read for this note.

## Related

[[k-underspecified-csp]] · [[clarification-benchmarks]] · [[sufficient-statistic]] · [[sprt]]

[^c1]: huang-2026 — "For sequential task solving, we report final accuracy, whether ŷ = y, and final sufficiency, whether the acquired information determines y uniquely."
[^c2]: huang-2026 — "in logical problems at k = 2 they under-predict the degree of missing information about four times as often as they over-predict it"
[^c3]: huang-2026 — "The gap is small for most models: it is within 5 percentage points for 12 out of 14 models, and within 10 percentage points for all models"
[^c4]: huang-2026 — "We find that following the correct query order consistently improves final accuracy both in MSS fully covered and partially covered interactions"
[^c5]: huang-2026 — "models with similar question informativeness can still differ substantially in final accuracy, indicating that success also depends on how well they use the collected answers"
