---
description: "Scoring a research agent's process (breadth, depth, refinement, critical thinking, efficiency) and whether its report matches that process, since report quality and factual grounding diverge."
aliases: ["process-centric evaluation", "process-to-report alignment", "P→R / R→P alignment"]
sources: ["doi-10-48550-arxiv-2603-28407"]
---
# Process-report alignment evaluation

A final report can look strong while the search behind it was redundant or brittle, and a disciplined process can be only partly reflected in the write-up. MiroEval therefore scores the research process itself, separately from the report.[^c1]

The raw process log is first turned into atomic units, each one functionally distinct step (acquisition, evidence inspection, intermediate synthesis, planning, revision, error correction). Their dependency structure and key process findings are then recovered. This is only an auxiliary interface for comparing across systems, not an assumption about what a process must look like.[^c2]

Intrinsic process quality has five dimensions: search breadth, analytical depth, progressive refinement, critical thinking (judging source reliability and conflicting evidence) and efficiency (no repeated queries, circular paths or unused retrievals).[^c3]

Alignment is checked in two directions plus one consistency check. Process→Report: low scores mean useful intermediate results were left out of the report. Report→Process: low scores mean the report overstates or adds unsupported synthesis. Contradiction detection: whether conflicting evidence was resolved rather than silently passed on.[^c4] The overall score is a weighted sum, Sprocess = α·Sintrinsic + (1−α)·Salign.[^c5]

Measured results: systems ranked differently on synthesis quality and factuality. Kimi-K2.5 had the top non-MiroThinker synthesis score (75.7) but a factuality of 65.4, while Manus had the lowest synthesis (55.4) but factuality 72.6.[^c6] Process scores were broadly predictive of outcome. The top three process systems were also the top three overall, and the weakest process system had a near-bottom outcome.[^c7]

For question asking and answering, my inference is that an answer's quality cannot be read from its surface alone. Whether the answer is faithful to the investigation behind it is a separate, measurable property.

## Limits

- All scores come from LLM judges (GPT-5.2 for process), and I did not read any validation of the process judge against humans.
- The correlation between process and outcome is described as broad, with a few systems deviating. It is not causal.
- Processes were taken from commercial systems' logs, whose visibility and format differ, so the structured representation may favour some systems.
- The value of α and the dimension weights were not examined here.
- It covers deep-research reports, not short answers or clarifying questions.

## Related

- [[intermediate-action-feedback]] — supervising intermediate steps rather than only final outcomes
- [[appraisal-gated-evidence-synthesis]] — appraising evidence before synthesis, which the critical-thinking dimension scores
- [[question-evaluation-method]] — evaluation of questions and answers more generally
- [[question-based-summary-evaluation]] — another way of checking a report against its content
- [[trajectory-graph-process-metrics]] — the same "score the process, not only the outcome" move for a single agent run, read from its action graph with no report to align against

[^c1]: doi-10-48550-arxiv-2603-28407 — "A system may produce a superficially strong report through redundant exploration or brittle reasoning"
[^c2]: doi-10-48550-arxiv-2603-28407 — "We therefore decompose the process into a sequence of atomic units"
[^c3]: doi-10-48550-arxiv-2603-28407 — "Search Breadth assesses whether the process explores a sufficiently wide range of sources, perspectives,"
[^c4]: doi-10-48550-arxiv-2603-28407 — "Low R→P scores indicate that the report overstates, introduces"
[^c5]: doi-10-48550-arxiv-2603-28407 — "Sprocess = α Sintrinsic ( P) + (1 − α) Salign ( P, R),"
[^c6]: doi-10-48550-arxiv-2603-28407 — "a polished report does not"
[^c7]: doi-10-48550-arxiv-2603-28407 — "process quality is broadly"
