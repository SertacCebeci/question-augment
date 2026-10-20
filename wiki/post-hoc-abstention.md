---
description: "Crossing a tool-trace signal with a verbal-response signal on should-abstain tasks isolates agents that act irreversibly and only then claim to have refused."
aliases: ["post-hoc abstention", "act-then-discover"]
sources: ["liu-2026-agentabstain"]
---
# Post-hoc abstention

> An agent that says "I shouldn't have done that" after doing it has not
> abstained — measuring only its words would say it had.

## Definition / Mechanism

Liu et al. (2026) cross two independent signals
on every should-abstain agent run — whether a critical (state-mutating)
tool fired, and whether the terminal response verbally refuses — into a
2×2 outcome space: "Successful [[abstention|Abstention]] (59.9%, both axes abstained);
Implicit Abstention (17.8%, action abstained but words did not; no harm
but no actionable signal); No Abstention (19.7%, neither abstained; user
receives a confidently wrong deliverable); and Post-hoc Abstention (2.6%,
n = 115, agent acts and verbally claims to have abstained; the most
dangerous mode, combining irreversible side effects with false assurance
of restraint)."[^c1]

The mode is named for its timing, not its final words: "We identify
failure modes such as post-hoc abstention, in which agents execute
irreversible actions before recognizing abstention triggers." Combining
the two signals rather than scoring the response alone is what surfaces it:
requiring agreement between the commit check and the judge "blocks 98 of
115 Post-hoc cases."[^c2]

The mode concentrates unevenly by model provider rather than spreading
evenly across the roster: "These rarer modes concentrate by provider:
GPT-5.1 and GPT-5.2 produce Post-hoc Abstention on roughly one in ten
operational abstain runs (10.1% and 8.6%), OpenAI accounts for 51% of all
Post-hoc cases (n = 59 of 115, 1.45× over-representation on 35% of the
roster)." Trajectory inspection finds a recurrent sub-mechanism the paper
calls act-then-discover: "models commit irreversibly before noticing the
trigger (seven models cancel a flight before flagging contradictory
rebooking constraints ... )."[^c3]

## Why it matters

This gives stall 2's irreversibility criterion ([[reversibility]]) a
measured failure mode rather than a hypothetical one: an agent can pass a
naive "did it refuse in words" check while having already taken the
one-way-door action the refusal was supposed to prevent. A single verbal
abstention rate cannot distinguish this from a genuine refusal; the
tool-trace signal is what makes the two separable.

## Transfer

| | |
|---|---|
| In its home field | detection theory's confusion matrix: two independent binary readings (a physical/instrumented signal and a declared verdict) crossed into a 2×2 table of outcome classes |
| Here | one axis is a deterministic tool-call trace (did a commit-class action fire), the other an LLM judge's reading of the terminal text; crossed on should-abstain tasks only |
| What survives | the logic that two independent signals separate outcomes invisible to either alone — a verbal-only check conflates Post-hoc with Successful Abstention |
| What does not | no sensitivity/specificity or [[roc-curve|ROC curve]] is computed; the four cells are reported as raw proportions over one benchmark's 115 qualifying should-abstain runs, not a calibrated detector with a tunable threshold |

[^c4]

## Limits

- The commit-check axis exists only for operational tasks (those with
  state-mutating tools); on the 132 informational tasks in the benchmark
  the taxonomy collapses to the judge signal alone, so Post-hoc Abstention
  as defined here cannot occur outside operational tasks.
- The reported rate (2.6%, $n=115$) comes from one benchmark's 42
  sandboxed environments and 17 evaluated models; the paper does not claim
  the rate transfers to other tool sets or task distributions.
- Provider concentration (GPT-5.1/5.2, OpenAI) is reported descriptively
  over 115 cases and is not tested for statistical significance in the
  extract read here.

## Related

[[agentabstain-paired-benchmark]] · [[reversibility]] · [[abstention]] · [[selection-abstention-asymmetry]]

[^c1]: liu-2026-agentabstain — "Successful Abstention (59.9%, both axes abstained); Implicit Abstention (17.8%, action abstained but words did not; no harm but no actionable signal); No Abstention (19.7%, neither abstained; user receives a confidently wrong deliverable); and Post-hoc Abstention (2.6%, n = 115, agent acts and verbally claims to have abstained; the most dangerous mode, combining irreversible side effects with false assurance of restraint)."
[^c2]: liu-2026-agentabstain — "We identify failure modes such as post-hoc abstention, in which agents execute irreversible actions before recognizing abstention triggers."
[^c3]: liu-2026-agentabstain — "These rarer modes concentrate by provider: GPT-5.1 and GPT-5.2 produce Post-hoc Abstention on roughly one in ten operational abstain runs (10.1% and 8.6%), OpenAI accounts for 51% of all Post-hoc cases (n = 59 of 115, 1.45× over-representation on 35% of the roster)"
[^c4]: liu-2026-agentabstain — "We decompose every abstain run along two axes: whether the agent executed a critical action (commit check) and whether it verbally refused (judge verdict)."
