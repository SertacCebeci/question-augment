---
description: "Deep research agents tend to produce plausible but unsupported terms, methods and references that mimic scholarly rigor, and this fabrication is the largest failure share in the generation stage."
aliases: ["illusion of academic rigor", "SCF", "unfounded scholarly constructs"]
sources: ["arxiv-2512-01948"]
---
# Strategic content fabrication

A research report can fail without containing one obviously false fact. The failure the DEFT taxonomy calls strategic content fabrication (3-5-SCF) is a generation-stage error: the agent writes constructs that have the form of scholarship but no grounding in what it retrieved. The paper describes it as "the agents tend to generate seemingly professional but factually unsupported terms, methods, or references in order to create an illusion of academic rigor."[^c1] The category is defined as an agent "generating plausible but unfounded academic or empirical constructs" that "mimic scholarly rigor to create a false impression of credibility."[^c2]

What makes it a distinct object is where it sits. The constructs are methods, data sources, case narratives or citations. Each one is locally plausible, so the failure is visible only when the construct is checked against the evidence the agent actually gathered. A check on the surface of the text, on whether it reads like a serious report, passes it. This is my inference from the definition, not something the paper tests.

The paper gives the category weight. The generation category "exhibits the highest proportion of failures, particularly in 3-5-SCF."[^c3] Within the taxonomy the share is listed as "Strategic Content Fabrication (3-5-SCF, 18.95%)."[^c4] The same section links it to a second generation failure, redundant content piling, because both "lead to outputs that are verbose, loosely structured, and lacking in substantive insight."[^c8] The paper's remedy is a generative-stage check: "Strengthening the constraints and verifications in the generative process is an important approach to" improving output quality,[^c5] and "post-verifications should extend beyond the retrieval stage to include generative dimensions such as text organization."[^c6] That is a recommendation drawn from the taxonomy. The paper does not run a verification step and measure its effect.

A related idea sits in [[semantic-illusion]]: plausible text that keeps the meaning of its evidence is placed with faithful text by similarity-based detectors. A fabricated method that keeps the form of its surrounding evidence would face the same blind spot (my inference). Fabrication that continues after the model has signalled doubt is measured in [[ungrounded-reasoning-gap-ratio]], a reasoning-trace measure that is a different object: it counts tokens, not constructs in a report.

## Limits

- The label comes from a codebook built by LLM coders and refined with human experts. The boundary of the category was checked on small samples: the paper's inter-coder check used a subset of 24 or 54 execution records, and the human-LLM comparison covered two agents, WebThinker and OpenManus.[^c7][^c9]
- "Strategic" implies a purpose. The text does not test intent. In this note it names the output's function, creating a false impression of credibility, and makes no claim about motive (my inference).
- The percentage is a share of coded failures within one benchmark of 100 tasks. It is not a rate of fabricated claims per report, and the text I read reports no check of whether the cited references exist.
- The paper does not measure whether readers are misled by these constructs, so the harm is asserted through the phrase "illusion of academic rigor" rather than observed.

## Related

- [[semantic-illusion]] — plausible text that similarity-based detectors pass; the same blind spot at the level of a report's constructs (my inference)
- [[ungrounded-reasoning-gap-ratio]] — a trace-level measure of continued fabrication after uncertainty, a different unit from a report's constructs
- [[failure-mode-taxonomy]] — the DEFT taxonomy in which this category is one of the generation-stage modes

[^c1]: arxiv-2512-01948 — "the agents tend to generate seemingly professional but factually unsupported terms, methods, or references in order to"
[^c2]: arxiv-2512-01948 — "The agent engages in strategic content fabrication by generating plausible but unfounded academic or"
[^c3]: arxiv-2512-01948 — "The Generation Category exhibits the highest proportion of failures, particularly in 3-5-SCF."
[^c4]: arxiv-2512-01948 — "Strategic Content Fabrication (3-5-SCF, 18.95%)"
[^c5]: arxiv-2512-01948 — "Strengthening the constraints and verifications in the generative process is an important approach to"
[^c6]: arxiv-2512-01948 — "post-verifications should extend beyond the retrieval stage to include generative dimensions such as text organization"
[^c7]: arxiv-2512-01948 — "we engaged three domain experts to independently annotate a"
[^c8]: arxiv-2512-01948 — "lead to outputs that are verbose, loosely structured, and lacking in substantive insight"
[^c9]: arxiv-2512-01948 — "We invited four domain experts to evaluate the report-generation outputs produced by WebThinker and OpenManus"
