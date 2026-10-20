---
description: "Across six long-horizon search agents, answer accuracy tracks cumulative retrieval recall almost perfectly but is nearly unrelated to how much the agent searched."
aliases: ["search-effort-accuracy decoupling"]
sources: ["liu-2026-diagnosing", "arxiv-2603-04403", "doi-10-48550-arxiv-2603-07853"]
---
# Search-effort/accuracy decoupling

> How much a search agent searches predicts almost nothing about whether
> it gets the answer right; how much of the needed evidence it actually
> retrieves predicts almost everything.

## Definition / Mechanism

Across six agents on BrowseComp-Plus, with retriever and evaluation
harness held fixed, "search effort and answer quality are only weakly
aligned. Answer accuracy is better correlated with the quality of
retrieved evidence, especially cumulative retrieval recall, than with the
number of searches or the amount of context consumed."[^c1]

Measured directly: "cumulative recall at 𝐾 = 25 is the strongest
correlate, with Pearson 𝑟 = 0.99; visit precision is moderate at 𝑟 =
0.50... final context size is essentially unrelated at 𝑟 = 0.16." At the
query-volume level the same decoupling shows up as a negative sign:
"volume runs the wrong way for an effort story, anti-correlated with
accuracy at 𝜌 = −0.77."[^c2]

## Why it matters

Evidence does not arrive late and get missed for lack of trying: "useful
evidence often appears early in the trajectory, yet agents tend to
continue searching, producing a long tail of low-yield retrieval steps."
Capping trajectories at episode $K=20$ "retains 86.3–92.4% of each agent's
accuracy, and $K=40$ retains 97.0–99.8%," against median rollouts of
14–33 search calls — so a hard search budget well below what agents
actually use would cost little accuracy.[^c3]

For a stall about which axis to pursue next, this wiki reads the finding
as a reframing: past the point where cumulative recall saturates, issuing
more queries is not caution, it is waste the outcome metric does not
reward.[^c4]

A single agent shows a version of the same decoupling at its first move. In FinRetrieval, Claude Opus with reasoning averages 3.5 structured-data calls on correct answers and 5.5 on incorrect ones, but the authors state that "However, this correlation is not causal" and tie it to the first lookup: when the first series search returns the target, accuracy is 92.9%; when it fails, 76.6%.[^c5][^c6] Within one agent, effort tracks outcome only through whether that first lookup hits. The paper's introduction also reads the same correlation as question difficulty, and the two readings are not separated by any test in the text.[^c7] In my reading, the first miss is what the effort count registers, and the calls after it are a symptom rather than the cause.

## Limits

The $r=0.99$ correlation is over only six agents (a descriptive, not an
inferential, statistic by the paper's own statement); the paper reports a
within-question panel and bootstrap to support the direction of the
effect, but the headline correlation itself should not be read as a tight
population estimate. The recall metric requires gold/evidence qrels
unavailable outside a benchmark like BrowseComp-Plus, so "cumulative
recall" cannot be observed mid-trajectory in a deployed agent, only
reconstructed after the fact against a held-out relevance judgment.

A training-time result points the other way. In SynPlanResearch-R1, cutting the RL tool budget from 8 to 6 steps lowers accuracy, and the authors read this as a positive link between performance and how deeply the agent explores.[^c8] That budget is set during training and applies to agents still being trained, not to a finished agent capped at test time, so it is a different test from the one behind the decoupling. I read the two as in tension and not resolved by either paper: one measures finished agents, the other the depth an agent is trained toward. See [[initialization-bounded-exploration]].

## Related

[[retrieval-utilization-gap]] · [[query-discipline]] · [[fiscal-period-label-mismatch]]

[^c1]: liu-2026-diagnosing — "search effort and answer quality are only weakly aligned. Answer accuracy is better correlated with the quality of retrieved evidence, especially cumulative retrieval recall, than with the number of searches or the amount of context consumed."
[^c2]: liu-2026-diagnosing
[^c3]: liu-2026-diagnosing — "useful evidence often appears early in the trajectory, yet agents tend to continue searching, producing a long tail of low-yield retrieval steps."
[^c4]: liu-2026-diagnosing — "useful evidence often appears early in the trajectory, yet agents tend to continue searching, producing a long tail of low-yield retrieval steps."
[^c5]: arxiv-2603-04403 — "However, this correlation is not causal"
[^c6]: arxiv-2603-04403 — "or failure on the first discover_company_series (DS) call."
[^c7]: arxiv-2603-04403 — "this reflects question difficulty"
[^c8]: doi-10-48550-arxiv-2603-07853 — "indicating a positive correlation between performance and the depth of tool-based exploration"
