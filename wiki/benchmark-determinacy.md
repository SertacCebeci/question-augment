---
description: "Under Lipschitz regularity, a dense subset of benchmarks, grouped into equivalence classes, determines capability over a whole region; spread-out picks give most information per evaluation."
aliases: ["moduli space of batteries", "battery equivalence classes", "determinacy of benchmark coverage", "dense battery coverage"]
sources: ["arxiv-2512-04276"]
---
# Benchmark determinacy

A benchmark, here called a battery, is a finite or countable set of tasks with a sampling distribution, a scoring rule, and metadata about the capabilities it probes. Two batteries are treated as the same point when they differ only by symmetries that leave the evaluation statistics unchanged, such as relabelling seeds and "rescaling resource units by positive constants."[^c1] The paper says these classes are "equivalence classes of benchmarks that are indistinguishable at the" level of agent orderings and capability inferences.[^c2] The set of classes is the moduli space, and it carries a metric d, which the paper builds from a Wasserstein distance on canonical score laws.

On this space a capability functional F(π, B) becomes a field Φπ over the classes. The determinacy claim is that if that field is Lipschitz in d, then its value at any battery in a region U can be read off from nearby sampled batteries: the difference is bounded by L times the distance to the nearest sample. The paper states that "under mild regularity assumptions, a dense subset of batteries suffices to approximate" the capability on a region.[^c3] The paper states the consequence directly: "batteries in U provide coverage of the region," so "testing on all of them is unnecessary."[^c4] A second statement uses finite nets instead of a dense set: "finite ε-nets in M suffice to approximate capability fields uniformly."[^c5] The paper says the proofs "use standard covering arguments" and concentration inequalities for the empirical battery scores.[^c6]

The design rule follows from the bound. Because the error scales with distance in the metric, a suite that spreads its representatives across the region gets the most coverage for a given budget. The paper puts it this way: the design aims at suites "that provide maximal information for a given evaluation budget, by selecting representatives that are far" apart in the moduli space, while "remaining in the region of interest."[^c7] In the discussion it sets this against the usual practice: "Rather than collecting tasks ad hoc, one can aim for representatives that" are far apart.[^c8]

For a reader who asks questions, the transferable part is the reason, not the formula. A question set is a battery of sorts. The bound says that adding a question close to one already asked buys little, because the capability field changes little across a small distance; a question far from the others is what moves the estimate. My reading: this is a selection principle that needs a metric on questions and a capability field that varies smoothly in it. The paper assumes both; it does not supply them for any real question set.

## Limits

- No empirical embedding is given. The paper says that "empirical work is needed to construct practical embeddings of real-world benchmarks into approximate moduli spaces, using techniques from representation learning."[^c9] The metric d is defined on canonical score laws and is not computed for any benchmark in the text.
- The whole result rests on the Lipschitz assumption on Φπ. Where capability jumps across the metric, for example at a threshold on a family, the bound does not hold and the sample must be denser there. The paper calls the assumption "mild" and does not test it. (my reading)
- The constant L is not estimated. A coverage radius can be small in the metric and still large in the terms a practitioner cares about, since the metric is defined by the paper's symmetries and not by the questions' difficulty or wording. (my inference)
- The equivalence relation keeps only what the score laws see. Two batteries that score the same can teach or diagnose different things, and the relation does not separate them. This is an inference from what the relation ignores, not a result the paper reports.
- The results are for agent policies scored by a capability functional. Nothing here measures human answerers or checks the bound against held-out items; the claim is about the moduli-space geometry, which the paper develops in a separate work it cites.
- No datasets were generated or analysed in the study.[^c10] The determinacy statements are the paper's own results, unverified against any suite.

## Related

- [[history-free-test-set-compression]] — choosing a representative subset from item embeddings alone; a practical route to the spread-out selection this note describes, without the metric the paper assumes
- [[cluster-geometry-redundancy-diagnostic]] — reading a benchmark's redundancy from its embedding clusters; the kind of empirical measurement the paper asks for
- [[ig-redundancy-coverage-utility]] — a coverage bonus minus a redundancy penalty for choosing follow-up questions, found by search rather than by a density bound
- [[verifier-noise-self-improvement-condition]] — the same paper's dynamic side: the batteries here are where the self-improvement flow is read off

[^c1]: arxiv-2512-04276 — "rescaling resource units by positive constants"
[^c2]: arxiv-2512-04276 — "equivalence classes of benchmarks that are indistinguishable at the"
[^c3]: arxiv-2512-04276 — "under mild regularity assumptions, a dense subset of batteries suffices to approximate"
[^c4]: arxiv-2512-04276 — "batteries in U provide coverage of the region"
[^c5]: arxiv-2512-04276 — "that finite ε-nets in M suffice to approximate capability fields uniformly"
[^c6]: arxiv-2512-04276 — "Proofs use standard covering arguments"
[^c7]: arxiv-2512-04276 — "by selecting representatives that are far"
[^c8]: arxiv-2512-04276 — "Rather than collecting tasks ad hoc, one can aim for representatives that"
[^c9]: arxiv-2512-04276 — "empirical work is needed to construct practical embeddings of real-world benchmarks into approximate moduli spaces"
[^c10]: arxiv-2512-04276 — "No datasets were generated or analysed"
