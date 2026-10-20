---
description: "A planning-layer defense that re-injects the original root query whenever a deep-research agent generates a new subtask or follow-up question, constraining drift caused by poisoned evidence."
aliases: ["Root Query Anchoring", "RQA"]
sources: ["pan-2026"]
---
# Root Query Anchoring

> A defense that does not try to filter adversarial documents out of
> retrieval; instead it constrains the step where poisoned evidence would
> otherwise do its damage — the moment the agent picks the next question.

## Definition / Mechanism

Root Query Anchoring (RQA) targets subtask hijacking directly, since that is
what drives report-level contamination rather than per-subtask evidence
injection: "RQA stores q0 at initialization and re-injects it at two
recursive points: (i) when subtasks are generated from retrieved evidence,
and (ii) when learnings are extracted and next-round questions proposed. At
both points the prompt co-conditions on q0 and the current subtask,
anchoring new questions to the original objective while covering diverse
dimensions (temporal, geographic, mechanistic, contrastive). A poisoned
document may still enter retrieval, but it cannot steer the next subtask
away from q0."[^c1]

Against [[forge-trajectory-hijacking|FORGE]] under Network conditions at
five injected documents, on a ten-query defense subset, "RQA reduces PRISM
from 38.5% to 18.3% while raising utility from 0.5000 to 0.6173 — the only
defense that improves utility while achieving the lowest PRISM," compared
against paraphrasing-based sanitization, perplexity filtering, and
retrieval-time knowledge expansion, none of which reached as low a PRISM
score or raised utility.[^c2]

The mechanism is explicitly partial: "RQA is a lightweight planning-layer
mitigation, not a complete defense: it requires no retraining or
retrieval-time classifier, but blocks the planning channel rather than
removing adversarial documents retained in the top-m evidence."[^c3]

## Why it matters

For stall 2, RQA is a concrete counter-move against exactly the failure
FORGE names: the candidate axis that scores best from an uncontrolled
retrieval pass need not be the axis the original query actually calls for.
Re-conditioning every follow-up-question generation step on the root query
is a selection-time constraint, not an evidence-filtering one — it changes
which axis is chosen without needing to detect which evidence is poisoned.

## Known as

| Field | Name there | Relation |
|---|---|---|
| agent-security | Root Query Anchoring | exact |
| agent-security | RQA | exact — the paper's own abbreviation |
[^c4]

## Limits

- RQA does not remove poisoned documents from the retrieved evidence set;
  it constrains only what the [[planner-dynamic-stopping|planner]] does with them, so residual
  contamination remains (18.3% PRISM, not zero).[^c5]
- Evaluated mainly on one platform (gpt-researcher); Appendix E replicates
  the trend on two more platforms, but the paper cautions PRISM values are
  not directly portable across retrieval architectures.
- The comparison is against three specific alternative defenses
  (paraphrasing, perplexity filtering, knowledge expansion) under one
  attack (FORGE) at one injection scale (j=5); no claim is made about
  attacks that do not route through subtask/follow-up generation.

## Related

[[forge-trajectory-hijacking]] · [[prism-poisoning-severity-metric]] · [[adaptive-submodularity]]

[^c1]: pan-2026
[^c2]: pan-2026 — "Table 4 shows that RQA reduces PRISM from 38.5% to 18.3% while raising utility from 0.5000 to 0.6173—the only defense that improves utility while achieving the lowest PRISM."
[^c3]: pan-2026 — "RQA is a lightweight planning-layer mitigation, not a complete defense: it requires no retraining or retrieval-time classifier, but blocks the planning channel rather than removing adversarial documents retained in the top-m evidence."
[^c4]: pan-2026 — "Root Query Anchoring, a lightweight defense that ties recursive follow-up generation to the root query."
[^c5]: pan-2026 — "blocks the planning channel rather than removing adversarial documents retained in the top-m evidence"
