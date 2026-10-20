---
description: "Difficulty set before items exist, by two generation parameters (chain length and target output size), so hardness is known by construction rather than measured after the fact."
aliases: ["generator difficulty knobs", "construction-time difficulty control", "parametric difficulty control"]
sources: ["arxiv-2512-10713"]
---
# Construction-parameter difficulty dial

Most benchmark difficulty is measured after the items exist: by the failure rate of a reference model, by the length of a reasoning path, or by a fitted ability curve. PACIFIC writes difficulty into the generator instead. Its design criteria include a requirement that "The framework must provide explicit mechanisms for controlling the difficulty of the generated benchmarks."[^c1] Two parameters carry it. "Number of Instructions: Serves as a quantitative difficulty regulator."[^c2] "Targeted Output Length: Acts as a qualitative difficulty regulator."[^c3]

The second parameter is held by a length-aware selection rule. Instructions are grouped by whether they lengthen or shorten the output, and "By monitoring intermediate expected lengths during benchmark construction, the system selects subsequent instructions to keep the overall output length close to the targeted length."[^c4] The first parameter is simpler: the generator stacks the chosen number of instructions, and a type constraint keeps the chain well formed: "The input type of each instruction must match the output type of the previous instruction."[^c5] So the item's difficulty is a function of two targets the author sets, and not of any model's response to it.

The paper's grid shows the dial moving outcomes. It crosses instruction counts of 3, 5, 8, 10 and 15 with target output lengths of 3, 5 and 10, giving fifteen benchmarks, and reports "a clear negative correlation between difficulty" with correctness across the models it tested.[^c6] The stated purpose is that the dial "enables systematic scaling of benchmark difficulty, ensuring applicability across a wide range of models, from current models to future state-of-the-art ones."[^c7] It also lets a user "select difficulty levels appropriate for the model under evaluation or to probe the model's capability limits."[^c8]

Other routes set difficulty differently. [[hop-depth-difficulty-with-entropy-check]] takes difficulty from the length of a knowledge-graph path and checks it with a probe's entropy. [[difficulty-enriched-item-sampling]] makes items hard by keeping those a reference model fails, so part of the hardness belongs to the sampler. [[difficulty-conditioned-evolving-item-generation]] conditions generation on a measured ability boundary and keeps moving as models improve. The dial differs from all three in being fixed in advance by the author for each benchmark. It is also not tied to a model's failures, so it does not inherit a sampler's confound.

## Limits

The parameters set the size of the item, not its difficulty for a solver. The authors state that the building blocks "are made to be easily dry-run by a first year computer science major, while being complex for an LLM as demonstrated in our experiment."[^c9] That an instruction count of ten is hard for a model is an empirical finding about the models, not a consequence of the dial's definition.

The two dimensions are not shown to be separable. "The difficulty of a PACIFIC benchmark may be affected by additional factors beyond the number of instructions and output size."[^c10] The paper adds that "there may be combined affects of the two factors that we control."[^c11] A dial with two settings can be read as two axes only if they do not interact, and the text does not test that.

The mapping from setting to difficulty is measured on a grid of three output lengths and five counts. The shape between grid points, and beyond them, is not reported.

The dial is also set over the authors' own instruction pool. The paper says the benchmarks "may be influenced by the seed instructions or by the initial algorithms to evaluate," and that it has "not observed such an influence in our experiments."[^c12] A different pool could move the same settings to different difficulties, and the text does not measure one.

## Related

- [[hop-depth-difficulty-with-entropy-check]] — difficulty by path length, checked by a probe.
- [[difficulty-enriched-item-sampling]] — difficulty by sampling failures, confounded with the sampler.
- [[difficulty-conditioned-evolving-item-generation]] — generation conditioned on measured ability, not fixed in advance.
- [[orthogonal-difficulty-decomposition]] — difficulty split into independent axes; the paper's two dials are a similar split, though the paper does not claim orthogonality.

[^c1]: arxiv-2512-10713 — "The framework must provide explicit mechanisms for controlling the difficulty of the generated benchmarks"
[^c2]: arxiv-2512-10713 — "Number of Instructions: Serves as a quantitative difficulty regulator"
[^c3]: arxiv-2512-10713 — "Targeted Output Length: Acts as a qualitative difficulty regulator"
[^c4]: arxiv-2512-10713 — "By monitoring intermediate expected lengths during benchmark construction, the system selects subsequent instructions to keep the overall output length close to the targeted length"
[^c5]: arxiv-2512-10713 — "The input type of each instruction must match the output type of the previous instruction"
[^c6]: arxiv-2512-10713 — "a clear negative correlation between difficulty"
[^c7]: arxiv-2512-10713 — "This design enables systematic scaling of benchmark difficulty, ensuring applicability across a wide range of models, from current models to future state-of-the-art ones"
[^c8]: arxiv-2512-10713 — "allows to select difficulty levels appropriate for the"
[^c9]: arxiv-2512-10713 — "are made to be easily dry-run by a first year computer science major, while being complex for an LLM as demonstrated in our experiment"
[^c10]: arxiv-2512-10713 — "The difficulty of a PACIFIC benchmark may be affected by additional factors beyond the number of instructions and output size"
[^c11]: arxiv-2512-10713 — "there may be combined affects of the two factors that we control"
[^c12]: arxiv-2512-10713 — "may be influenced by the seed instructions or by the initial algorithms to evaluate"
