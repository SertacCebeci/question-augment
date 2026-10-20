---
description: "A follow-up utterance inconsistent with a still-valid earlier requirement, with no explicit revision signal; LLMs rarely detect it before responding."
aliases: ["user-side implicit conflict"]
sources: ["wang-2026-towards"]
---
# User-side implicit conflict

A three-way relation between a dialogue's current user utterance and its
history: **normal dialogue** (the utterance stays compatible with what
remains valid), **explicit revision** (the user overtly updates, replaces
or negates a prior requirement), and **implicit conflict** — the utterance
introduces a requirement that is inconsistent with a still-valid earlier
one, but the user gives no revision signal, so the incompatibility must be
inferred from the task goal, dialogue context or commonsense.

"We formulate user-side conflict detection as a three-way classification
task, where each current user utterance is classified based on its
consistency with previously established user requirements: normal
dialogue, explicit revision, and implicit conflict."
Wang et al. (2026)[^c1]

"Implicit conflict refers to cases where the user introduces a new
requirement within the same task that is inconsistent with requirements
that remain valid in the dialogue history, without explicitly updating,
replacing, or negating them. Such conflicts must instead be inferred from
the task goal, dialogue context, or commonsense expectations."
Wang et al. (2026)[^c2]

Wang et al. (2026) built UC-Bench, a human-annotated benchmark over
WildChat, LMSYS and ShareGPT dialogues, and tested 16 general-purpose LLMs
under two protocols: generating an open-ended response (no instruction to
check for conflict) and three-way classification.

Under the response protocol: "the 16 evaluated models achieve an average
accuracy of only 19.79% on implicit conflict instances, ... with the best
model reaching 31.67%." Wang et al. (2026)[^c3]

Under the classification protocol: "the 16 evaluated models achieve an
average IC recall of only 25.00%, with the best model reaching 53.33%; 9
of the 16 models achieve an IC recall no higher than 20%."
Wang et al. (2026)[^c4]

Confusion-matrix analysis showed true implicit-conflict instances are
systematically misclassified as normal dialogue — the model treats the new
requirement as a natural continuation rather than checking it against what
is still binding. The paper reads this as a bottleneck for proactive
dialogue: an agent that does not detect the incompatibility has no trigger
to ask a clarifying question before generating a response that silently
drops the earlier, still-valid constraint.

## For the wiki

For stall 2 (which axis first), this gives the selection trigger a
concrete pre-condition on the answerer's side: before choosing what to ask
about next, a system must first notice that the newest user constraint is
inconsistent with an earlier one that is still active — otherwise there is
no axis to select, only a silent overwrite. The classification protocol
(three labels, judged against the dialogue history) is a cheaper,
higher-recall check than waiting to see whether the generated response
happens to surface the conflict on its own (Finding 3: the two are
correlated, Pearson r = 0.72, but not equivalent, R² = 0.52).

## Known as

Not applicable — the alias list carries one name from one field.

## Limits

Single-domain benchmark (WildChat/LMSYS/ShareGPT English+Chinese chat
transcripts, not task-oriented or tool-use dialogue); the label is a
human-annotated three-way judgement, not a formal test of logical
inconsistency between constraints, so "implicit conflict" here is whatever
the annotators judged incompatible with the active task scope, not a
provably contradictory pair. Best model recall of 53.33% ([?] not
independently reproduced by this wiki) is still below half; the finding
that LLMs under-detect does not establish that detection, once added,
translates into an actually-asked clarifying question — the paper trains a
separate detector rather than measuring end-to-end clarification behavior.

## Related

- [[clarification-benchmarks]]
- [[synuc]]
- [[constraint-as-information]]

[^c1]: wang-2026-towards — "We formulate user-side conflict detection as a three-way classification task, where each current user utterance is classified based on its consistency with previously established user requirements: normal dialogue, explicit revision, and implicit conflict."
[^c2]: wang-2026-towards — "Implicit conflict refers to cases where the user introduces a new requirement within the same task that is inconsistent with requirements that remain valid in the dialogue history, without explicitly updating, replacing, or negating them. Such conflicts must instead be inferred from the task goal, dialogue context, or commonsense expectations."
[^c3]: wang-2026-towards
[^c4]: wang-2026-towards — "the 16 evaluated models achieve an average IC recall of only 25.00%, with the best model reaching 53.33%; 9 of the 16 models achieve an IC recall no higher than 20%."
