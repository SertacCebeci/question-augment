---
description: "Functionally correct programs for one specification can use very different runtime memory, and sampling temperature widens the spread; passing tests does not certify runtime consistency."
aliases: ["runtime memory divergence", "memory-profile instability", "Model Instability Score"]
sources: ["arxiv-2601-01215"]
---
# Runtime memory divergence among correct programs

Two programs can pass the same tests and still run with different memory trajectories. The authors put the risk plainly: "same tests can exhibit drastically different runtime behavior, creating hidden risks such as performance bottlenecks and memory".[^c1] The difference is treated as structural rather than noise: "Temporal instability in executiontime memory profiles is not noise; it reflects underlying algorithmic".[^c2] Their Figure 3 gives the case: two correct sliding-maximum solutions, one that materialises every window (space on the order of nk) and one that keeps a monotone deque (space on the order of k). The caption reads "Example of correct solutions with runtime divergence because of different space algorithmic strategies."[^c3]

## Why the trace needs a transform

Raw memory traces are noisy. In Python, reference counting and a cyclic garbage collector "trigger non-deterministic reclamation and brief oscillations even" for identical logic.[^c4] The authors trace current bytes with tracemalloc and replace the series by its cumulative maximum after baseline correction. They call the result a Monotonic Peak Profile (MPP); it removes "downward spikes from transient frees and GC cycles, yielding a" non-decreasing envelope.[^c5] Two profiles are then compared by shape, not by magnitude (see dynamic-time-warping-shape-distance). The pairwise distance DMPD is averaged over unordered pairs of passing solutions and over private tests, giving a problem score; the macro Model Instability Score (MIS) is the unweighted mean of those problem scores.[^c6][^c7]

The cumulative maximum is a design choice that makes the envelope monotone. It keeps peak growth and discards the dips that allocator churn and collections produce. My reading, not the paper's wording: this should make two runs of one program look more alike, which is why the transform matters for the divergence measure.

## What was measured

Across BigOBench and CodeContests the authors "find substantial runtime divergence among correct solutions".[^c8] The second finding concerns temperature: "We consistently observe that an increase in temperature widens" runtime behaviour among correct generations.[^c9] On BigOBench, GPT-o4-mini's MIS rises with temperature while pass@1 also rises: "pass@1 also rises (0.69→0.80), indicating temperature perturbs execution paths (data structures, control flow), not just surface syntax."[^c10] The paper frames this as "a controllable trade-off" "between functional success and runtime stability."[^c11]

The authors draw an operational conclusion. "In production, two correct programs can carry different memory costs."[^c12] Correctness is therefore "a necessary gate," not a full ranking of candidates.[^c13] The paper proposes stability-aware selection among passing candidates, which it has not tested in a deployment.

My inference, not the paper's claim: when two candidates tie on the tests, their memory profiles are a separate axis of comparison, and a metric that ignores that axis cannot distinguish them.

## Limits

- Only Python, instrumented through tracemalloc. "All experiments use Python," and the authors state that their scores cannot be transferred to other languages without replication.[^c14][^c15] Garbage collection and allocator behaviour differ across runtimes, so the magnitudes do not carry over.
- Competitive-programming problems, not production services. "Our findings motivate, but do not replace," validation on real systems.[^c16]
- The sampling budget is small. "We cap generations to" each problem, at five correct generations and ten private tests; this can miss long-tail behaviours and "increases the variance" of the estimates.[^c17][^c23]
- The number depends on measurement choices. "fine-grained time sampling at 0.1 ms overstates instability," and coarser line sampling "modestly raises MIS" in the authors' ablation.[^c18][^c22]
- The temperature trend rests on a small set of models. For gpt-3.5-turbo-instruct, the authors could scan temperatures only up to about 1.4, because beyond that it yields fewer than two correct generations for any problem, "precluding DMPD/MIS computation."[^c19]
- The link to maintainability is exploratory: the authors report "exploratory correlations between our stability metrics and established software-engineering indicators", and state that links "to complexity under DMPD are weak/inconsistent."[^c20][^c21]
- Correct does not mean equally good: the paper measures spread among correct programs, not which of them is preferable, and it does not establish that higher memory use causes failures in use.

## Related

- dynamic-time-warping-shape-distance — the comparison that turns two profiles into DMPD, and what it does and does not preserve
- [[coincident-failure]] — also two artifacts built from one specification; that note asks whether they fail on the same inputs, while this one asks whether the passing ones behave alike in memory
- [[accuracy-masks-unstable-reasoning]] — the same pattern at another level: a correct/incorrect summary hides variation in the route to the answer

[^c1]: arxiv-2601-01215 — "same tests can exhibit drastically different runtime behavior, creating hidden risks such as performance bottlenecks and memory"
[^c2]: arxiv-2601-01215 — "Temporal instability in executiontime memory profiles is not noise; it reflects underlying algorithmic"
[^c3]: arxiv-2601-01215 — "Example of correct solutions with runtime divergence because of different space algorithmic strategies."
[^c4]: arxiv-2601-01215 — "trigger non-deterministic reclamation and brief oscillations even"
[^c5]: arxiv-2601-01215 — "downward spikes from transient frees and GC cycles, yielding a"
[^c6]: arxiv-2601-01215 — "The problem-level instability is the mean over pairs and tests:"
[^c7]: arxiv-2601-01215 — "the macro MIS as the unweighted average of problem scores:"
[^c8]: arxiv-2601-01215 — "we find substantial runtime divergence among correct solutions"
[^c9]: arxiv-2601-01215 — "We consistently observe that an increase in temperature widens"
[^c10]: arxiv-2601-01215 — "pass@1 also rises (0.69→0.80), indicating temperature perturbs execution paths (data structures, control flow), not just surface syntax."
[^c11]: arxiv-2601-01215 — "between functional success and runtime stability."
[^c12]: arxiv-2601-01215 — "In production, two correct programs can carry different memory costs."
[^c13]: arxiv-2601-01215 — "correctness thus is a necessary gate,"
[^c14]: arxiv-2601-01215 — "All experiments use Python"
[^c15]: arxiv-2601-01215 — "Hence, our scores cannot be transferred to"
[^c16]: arxiv-2601-01215 — "Our findings motivate, but do not replace,"
[^c17]: arxiv-2601-01215 — "miss long-tail behaviors, and increases the variance"
[^c18]: arxiv-2601-01215 — "fine-grained time sampling at 0.1 ms overstates instability"
[^c19]: arxiv-2601-01215 — "precluding DMPD/MIS computation"
[^c20]: arxiv-2601-01215 — "exploratory correlations between our stability metrics and established software-engineering indicators"
[^c21]: arxiv-2601-01215 — "links to complexity under DMPD are weak/inconsistent."
[^c22]: arxiv-2601-01215 — "modestly raises MIS"
[^c23]: arxiv-2601-01215 — "We cap generations to"
