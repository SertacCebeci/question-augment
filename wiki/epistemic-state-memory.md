---
description: "Storing each record's epistemic role (decision, hypothesis, open question) and contradiction/supersession links as persistent state, so retrieval is conditioned on status, not topical relevance alone."
aliases: ["epistemic memory", "OIDA", "typed signed graph memory", "epistemic infrastructure"]
sources: ["doi-10-48550-arxiv-2604-11759"]
---
# Epistemic-state memory

A passage can be topically relevant yet misleading: it may record a superseded plan, a tentative hypothesis, an unresolved question, or one side of a later contradiction. The work argues this is a failure of representation, not of semantic retrieval.[^c1] If such status is stored only as ordinary text, the answerer must re-infer it at every query.[^c2]

## Mechanism

OIDA stores organizational memory as a typed, attributed, signed, time-indexed graph. Nodes are decisions, evidence, plans, hypotheses, constraints and open information needs; edges encode support, contradiction, dependency and supersession.[^c3] Each node type has a prior priority and a temporal behavior: a decision (1.00) is stable until superseded, an observation (0.40) decays unless reinforced, a hypothesis (0.30) decays if untested, and a question (0.30) gains urgency while unresolved. These values are design priors, not validated optima.[^c4]

Contradiction is non-destructive: a contradicted node is down-weighted or paired with its contradiction, not deleted, because organizational contradictions are often unresolved coexistences.[^c5] Retrieval multiplies semantic similarity by a modulation term over priority, type and local edges.[^c6]

Open questions are first-class objects. The paper's one derived result: with the stated parameters, an unresolved question outranks an unreinforced observation once the urgency term exceeds about 0.013, so rising priority comes from the urgency mechanism and not from the label.[^c7]

## Evidence (pilot)

On a consulting corpus, structured retrieval used 2,623 input tokens against 110,539 for full context (42.1x fewer) but scored lower (aggregate quality 0.5574 vs 0.8329).[^c8] In a single-query pilot, structured retrieval produced a dedicated knowledge-gap section in 10 of 10 runs; full context surfaced the same limitation in 5 of 10.[^c9]

## Limits

- Full-context baselines win aggregate quality when the corpus fits in the window; the authors say graph memory does not universally beat long context.[^c10]
- The gap result is small-n and one query; it does not show the priority weights caused it.[^c9]
- The update rule is a specification; no longitudinal telemetry, contradiction-edge precision, or dynamic-vs-static comparison is reported.[^c11]
- Corpora are synthetic. Structured retrieval is vulnerable to incomplete extraction or retrieval.
- Relevance to asking: my inference is that open-information-need nodes are a stored form of "what should be asked next"; the paper does not test question generation.

## Related

- [[dialogue-to-state-compilation]] — also writes answers into persistent typed state rather than transient context
- [[distribution-knowledge-gap-in-abstention]] — a related treatment of surfacing what is not known
- [[epistemic-leakage]] — another note on epistemic status of information

[^c1]: doi-10-48550-arxiv-2604-11759 — "This kind of error is not primarily a failure of semantic retrieval. It is a failure of epistemic"
[^c2]: doi-10-48550-arxiv-2604-11759 — "an agent must infer their status again at query time."
[^c3]: doi-10-48550-arxiv-2604-11759 — "Formally, OIDA is a typed, attributed, signed, time-indexed graph."
[^c4]: doi-10-48550-arxiv-2604-11759 — "Initial priorities and temporal behaviors are design priors, not"
[^c5]: doi-10-48550-arxiv-2604-11759 — "a contradicted node is down-weighted or paired"
[^c6]: doi-10-48550-arxiv-2604-11759 — "relevance should be conditioned on"
[^c7]: doi-10-48550-arxiv-2604-11759 — "the rising-priority"
[^c8]: doi-10-48550-arxiv-2604-11759 — "Structured retrieval is lower quality in this regime"
[^c9]: doi-10-48550-arxiv-2604-11759 — "surfaced the same limitation in 5 of 10 runs."
[^c10]: doi-10-48550-arxiv-2604-11759 — "If the full relevant corpus fits in context at acceptable cost, a"
[^c11]: doi-10-48550-arxiv-2604-11759 — "We do not report"
