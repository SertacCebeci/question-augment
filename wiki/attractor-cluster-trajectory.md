---
description: "A run of consecutive outputs that stay close forms a cluster whose centre is its attractor; the detector finds one in a paraphrase loop and none in an exploratory one."
aliases: ["trajectory attractor", "semantic attractor basin", "cluster centre of gravity", "dispersion of an iterated trajectory"]
sources: ["arxiv-2512-10350"]
---
# Attractor cluster in an iterated trajectory

Once the outputs of a loop are embedded, the question is whether they settle into a region. The paper's operational answer is a cluster: "a maximal contiguous temporal window" of the run in which the embeddings "maintain semantic coherence, up to a set of outliers".[^a1]

Three conditions define coherence. Consecutive outputs must be similar above a threshold λ. The cluster as a whole must stay within a dispersion radius ρ. And a bounded number κ of consecutive violations is tolerated, "allowing temporary noise", before the cluster closes.[^a2] The attractor is the normalised centre of gravity of the cluster's embeddings, and it is read as the point the run is pulled toward, "toward which the trajectory converges during" the cluster's extent.[^a3] Dispersion is the quantity that "measures the maximum deviation from the center in calibrated similarity space",[^a4] so it is the largest distance from that centre.

Applied to a paraphrase loop at ρ = 0.2, the detector returns two clusters. One covers iterations 0–18, and the other covers iterations 21–50 with lower dispersion (0.1773 and 0.1500 in the paper's table). The paper reads the second as the convergence basin, and "confirms a single transition between two stable basins around iteration 20."[^a5] At a finer radius, "five micro-clusters emerge that merge smoothly over time"; at a coarser one, "a single cluster encompasses the entire trajectory."[^a6] In the summarize-and-negate loop, "no valid cluster was detected under" any tested setting.[^a7]

What the construction gives is a signature of settling that can be read from the run as it goes. A run has a settled phase when a window of outputs stays within a radius of its own centre, and the point at which that window starts is a transition that a stopping rule could in principle detect. The paper does not propose such a rule, and the step to one is mine. Retrieval loops in the corpus summarized by [[stop-continue-criteria-in-retrieval-loops]] mostly stop at a fixed budget, so a persistence test of this kind would be a state-dependent stop of a type seldom used there (my inference). Whether it is well calibrated is not tested here.

## Limits

- The cluster and attractor are operational objects. The paper says so directly: "All notions of convergence, divergence, and stability are defined operationally with respect to finite trajectories" in the framework's assumptions.[^a9] A cluster in this sense is a finite-sample pattern, not a fixed point.
- The thresholds are the authors' choices. "The similarity threshold λ = 0.8 enforces high local coherence" is fixed across the grid, and only ρ varies.[^a10] The paper's claim that the result holds "without parameter tuning" is about the three radii it tried, not about λ or κ.[^a11]
- The observation window is 50 steps. "The trajectory shows no signs of leaving the attractor within this" window, and the paper adds that "proving long-term stability rigorously would require analyzing the probability of entering" a cluster.[^a12]
- The exploratory result is an absence in a finite run. "We cannot formally exclude the possibility that a cluster might eventually form over" a longer horizon.[^a13]
- The embedding is a single function. "Trajectories are observed through a single embedding function" and the paper expects different geometric structure under other embeddings.[^a14]
- The dispersion here is a spread over successive outputs of one loop. It is not a spread over sampled answers to one input, and the two should not be read as the same computation.

## Related

- [[iterated-transformation-regime]] — the three-way classification that these clusters are used to assign; the cluster is the evidence for the contractive class
- [[stop-continue-criteria-in-retrieval-loops]] — stopping in retrieval loops, where fixed budgets dominate and state-dependent tests are rare; a cluster-persistence test would be one of the latter
- [[refinement-quality-peak]] — another route to a stop point in iterated revision, read from a quality curve and not from embedding geometry

[^a1]: arxiv-2512-10350 — "maintain semantic coherence, up to a set of outliers"
[^a2]: arxiv-2512-10350 — "allowing temporary noise"
[^a3]: arxiv-2512-10350 — "toward which the trajectory converges during"
[^a4]: arxiv-2512-10350 — "measures the maximum deviation from the center in calibrated similarity space"
[^a5]: arxiv-2512-10350 — "confirms a single transition between two stable basins around iteration 20"
[^a6]: arxiv-2512-10350 — "five micro-clusters emerge that merge smoothly over time"
[^a7]: arxiv-2512-10350 — "no valid cluster was detected under"
[^a9]: arxiv-2512-10350 — "All notions of convergence, divergence, and stability are defined operationally with"
[^a10]: arxiv-2512-10350 — "The similarity threshold λ = 0.8 enforces high local coherence"
[^a11]: arxiv-2512-10350 — "without parameter tuning"
[^a12]: arxiv-2512-10350 — "the trajectory shows no signs of leaving the attractor within this"
[^a13]: arxiv-2512-10350 — "We cannot formally exclude the possibility that a cluster might eventually form over"
[^a14]: arxiv-2512-10350 — "Trajectories are observed through a single embedding function"
