---
description: "Search agents reach the right website but fail to keep its filters and scopes aligned, so field values look right while rows are out of scope; scope drift and criterion mismatch dominate failures."
aliases: ["retrieval-scope drift", "state-gated retrieval failure", "criterion mismatch"]
sources: ["doi-10-48550-arxiv-2605-22219"]
---
# Retrieval-state drift

On specialized data-retrieval websites, the evidence that answers a question is not shown under default settings. It appears only after the right filters, views, hierarchies or scopes are set. Li et al. (2026) call this capability state-gated retrieval (SGR) and build SGR-Bench: 100 expert-curated tasks over six source families and 12 public data ecosystems. The question does not name the website, so the agent must find the site, configure its state and return a structured answer.[^c1]

## What fails

The authors audited 156 failed trajectories from CLI-based agents. The main finding is that the failure is not in finding the source. Agents often reach a relevant site and then establish the wrong state there.[^c2] Two failure types dominate: retrieval-scope drift (37.2%) and criterion mismatch (27.6%). Together they account for 64.7% of audited failures, against 10.3% for final answer composition.[^c3]

The two types leave different traces in the scores. Under criterion mismatch the field definitions or decision rules are wrong, so item-level F1 stays moderate (52.5%) while row-level F1 is the lowest of any error type (7.3%). Agents extract many locally correct values but almost no complete rows.[^c4] Scope drift lowers both scores about equally (38.7% item-F1, 19.2% row-F1), which the authors read as a global workspace error that corrupts all downstream evidence.[^c5] Once one control drifts (period, population, product class, table universe), the agent still retrieves plausible evidence, but from the wrong slice of the site.[^c6]

Which type dominates depends on the source family. Scholarly and environmental tasks are drift-heavy, while regulatory and official-statistics tasks are mismatch-heavy.[^c7]

## Implication for asking and answering

The question's wording carries part of the state. Each task comes in a constraint-guided and a goal-oriented version of the same problem. Explicit constraints gave slightly higher item-F1 (difference 1.90), while goal-oriented tasks gave marginally higher row-F1 (2.24). The authors conclude that explicit guidance helps locate fields but does not solve scope maintenance.[^c8] My own inference: spelling out constraints in a question is not enough, because the answerer must also hold them fixed across dependent steps.

The scoring point is that an answer can be locally correct and still invalid. The authors argue for checking that retrieved rows stay anchored to the correct site slice, since answer-only scoring can mask scope drift.[^c9]

## Limits

- The benchmark uses public, relatively stable, structured sources and underrepresents dynamic web content.
- Fine-grained error analysis covers only trace-bearing CLI systems. Commercial products were not audited, and there is no unified trajectory-level scoring across agents.
- The error taxonomy is the authors' manual audit. Reliability of the labelling was not examined in the slices I read.
- The guided-versus-goal differences are small, and I did not check their significance.
- The notion of "state" is tied to web interfaces. Whether the same drift occurs in conversation, where the answerer must keep a questioner's constraints fixed, is my conjecture and is untested here.

## Related

- [[constraint-as-information]] — an explicit constraint narrows the answer space, but here it must also be kept in force.
- [[clarification-benchmarks]] — another family of evaluations that probe where agents fail on under-specified information needs.
- [[structured-output]] — final answer composition was the minor failure here, so format is not the bottleneck.
- [[state-gated-strategy-routing]] — shares the word "state-gated" only; it concerns tutor strategy selection, not website state.

[^c1]: doi-10-48550-arxiv-2605-22219 — "answer-bearing evidence becomes accessible only after establishing the correct"
[^c2]: doi-10-48550-arxiv-2605-22219 — "agents often reach a relevant web source, but establish the wrong site-specific"
[^c3]: doi-10-48550-arxiv-2605-22219 — "(27.6%) together account for 64.7% of audited failures, while final answer composition accounts for"
[^c4]: doi-10-48550-arxiv-2605-22219 — "it achieves moderate Item-F1 (52.5%) but the lowest"
[^c5]: doi-10-48550-arxiv-2605-22219 — "retrieval-scope drift depresses both metrics roughly equally (38.7% Item-F1, 19.2% Row-F1), consistent with global"
[^c6]: doi-10-48550-arxiv-2605-22219 — "download scope. Once one control drifts, agents still"
[^c7]: doi-10-48550-arxiv-2605-22219 — "tasks are criterion-mismatch-heavy."
[^c8]: doi-10-48550-arxiv-2605-22219 — "Row-F1 (∆ = 2.24), suggesting that explicit guidance helps locate fields but does not solve scope"
[^c9]: doi-10-48550-arxiv-2605-22219 — "whether retrieved rows remain anchored to the correct site slice, since answer-only scoring can mask"
