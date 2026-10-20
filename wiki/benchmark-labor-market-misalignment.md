---
description: "Agent benchmarks mapped onto O*NET occupations and skills concentrate on programming and a few easily verified skills, far from where employment and wages lie, apparently driven by convenience."
aliases: ["benchmark-work distribution mismatch", "agent benchmark representativeness"]
sources: ["arxiv-2603-01203"]
---
# Benchmark-labor-market misalignment

What a benchmark asks is not a sample of what people are paid to do. Wang et al. map each task of 43 agent benchmarks (72,342 tasks) to paths in two taxonomies built only from human occupations: a domain tree (job family, occupation, task) and a skill tree (O*NET work activities, 4/9/41 nodes). An LLM assigns each task instruction to all matching paths. Benchmark effort per domain or skill is then compared with BLS employment and with capital, meaning salary times employment. Skill weights come from O*NET importance scores.[^c1]

**Coverage is lopsided.** Coverage is the share of unique taxonomy paths touched by a task set. Pooled over all benchmarks it is 56.5% of the domain tree but 85.4% of the skill tree. The authors explain the gap this way: domains are occupation-specific, whereas one task activates several cross-occupational skills.[^c2]

**Domain concentration.** Effort piles into Computer and Mathematical, mostly programming, a domain with only 7.6% of employment. Management, Legal, and Architecture and Engineering are highly digital (88%, 70%, 71% of work) yet hold 1.4%, 0.3%, 0.7% of examples. Low-paid Personal Care is also underexplored.[^c3]

**Skill concentration.** Effort concentrates on Getting Information and Working with Computers, which together cover under 5% of employment (3.1% and 2.4%). Interacting with Others pervades jobs but gets minimal coverage.[^c4]

**Stated cause.** The authors infer that effort follows methodological convenience: domains with readily specified natural-language instructions and easily verifiable rewards are favored.[^c5] This is an interpretation of the pattern, not a tested causal claim.

**Relevance is not representativeness.** Placing a task in a domain does not show it carries the scope and procedural detail of the real job. Synthesized benchmarks (e.g. ColBench) had low domain and procedural complexity, while human-annotated ones (GDPval, TheAgentCompany) spanned more domains and skills.[^c6]

For anyone writing questions or evaluation sets, the point is that the set's distribution is itself a claim about the target population. It can be audited against an external taxonomy before the scores are trusted.

## Limits

- Everything depends on LLM mapping (gpt-5) into the taxonomy, with manual quality checks. Error rates of the mapping are not given in the slices I read.
- Employment and capital weights are proxies. The authors say skill estimates are not worker counts but relative importance.[^c7]
- Only the U.S. labor market and digital agent benchmarks were studied. Physical work is retained in the taxonomy but cannot be benchmarked by these agents.
- Under-representation is not shown to be harmful. Software ability may transfer to other work, as the authors concede.
- The convenience explanation is not tested against alternatives.

## Related

- [[evaluation-choices-encode-error-priorities]] — a benchmark's design choices also fix which errors count
- [[judge-coverage-overestimation]] — another way apparent coverage overstates what an evaluation reaches
- [[agent-autonomy-as-complexity-frontier]] — the same paper's measure of what agents can do within covered work

[^c1]: arxiv-2603-01203 — "we map individual benchmark examples to domains and skills using occupational taxonomies derived from the O*NET database"
[^c2]: arxiv-2603-01203 — "Across all benchmarks, examples collectively cover a limited 56.5% of the domain taxonomy but a substantially broader 85.4% of the skill taxonomy."
[^c3]: arxiv-2603-01203 — "significantly overrepresents a domain that accounts for only 7.6% of total employment"
[^c4]: arxiv-2603-01203 — "which only occupy 3.1% and 2.4% of employment"
[^c5]: arxiv-2603-01203 — "domains with readily specified NL task instructions and easily verifiable rewards are disproportionately favored"
[^c6]: arxiv-2603-01203 — "many automatically synthesized benchmarks (e.g., ColBench) exhibit low domain and procedural complexity, capturing only simplified fragments of real work"
[^c7]: arxiv-2603-01203 — "these estimates do not represent the exact number of workers performing a given"
