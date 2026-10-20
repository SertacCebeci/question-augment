---
description: "Two respondents' additive value functions can be identified from finitely many matching queries even when answers arrive unlabeled, by pairing single-rectangle and neighboring-rectangle queries."
aliases: ["anonymous preference identifiability", "eliciting two decision-makers from anonymized answers", "UTA model identifiability from anonymous answers"]
sources: ["arxiv-2602-20638"]
---
# Anonymous multi-respondent identifiability

Setting: one asks a matching query, such as "which value of criterion j makes these two alternatives indifferent?", to two decision-makers at once. Two truthful, noise-free answers come back, but nobody knows which answer belongs to which person. The question is whether a finite query sequence suffices to recover both preference models. Here the models are additive value functions with piecewise linear, strictly increasing marginals and known breakpoints.[^c1]

## What is shown

The main result is an existence statement: both models can be elicited from anonymized answers with a finite number of indifference queries.[^c2] The identifiability question is also framed as a game: the questioner picks queries, the respondent answers truthfully, and the question is whether the questioner has a finite winning strategy.[^c3]

## Mechanism

The construction rests on two query geometries in the plane of two criteria, whose scales are cut into rectangles by the breakpoints:

- A single-rectangle query, with question and answers inside one rectangle, yields the anonymized pair of slopes on that rectangle. The pair is known, but not which slope belongs to which person.[^c4]
- A neighboring-rectangles query couples two adjacent rectangles. It supplies the constraint that assigns each slope to the right person.[^c5]

The procedure normalizes the slope on criterion 1's first segment to one. It identifies the first segment on criterion 2 with a single-rectangle query. It then iterates segment by segment, and finally repeats for every pair (1, i).[^c6] A single-rectangle query needs at most two questions, and which of three cases occurs depends on whether each indifference curve is steeper or shallower than the rectangle's diagonal. The next query is chosen from the corner that guarantees both answers land on a known side.[^c7]

My reading: the identification works because the ambiguity is a label swap, and a swap is resolved only when two answers are linked through a shared structure. Here the shared structure is that each person's curve continues across the rectangle boundary. Unlabeled answers alone carry no assignment information, so an adaptive choice of the next query is needed.

## Limits

- Only two respondents are covered. Extending the building blocks to more looks straightforward to the authors, but a procedure for n > 2 models is open.[^c8]
- It covers piecewise linear marginals with known breakpoints. The authors name general monotone marginals as future work.[^c9]
- Answers are noise-free. The adversarial-noise variant is explicitly not treated.[^c10]
- It is an existence and constructive proof, not a measurement of how many queries real respondents need or of how well it works with people. Query counts beyond the two-query single-rectangle bound were not read here.

## Related

- [[preference-elicitation-gap]] — the gap between what a respondent holds and what questioning extracts; here the extra obstacle is unlabeled sources.
- [[separation-oracle-preference-elicitation]] — another query-by-query elicitation view of a preference model.
- [[noisy-expert-channel-local-query-elicitation]] — handles noisy answers, which this noise-free result sets aside.

[^c1]: arxiv-2602-20638 — "For each query we receive two"
[^c2]: arxiv-2602-20638 — "It is possible to elicit two piecewise linear additive preference models based on anonymized preference information using a"
[^c3]: arxiv-2602-20638 — "The identifiability problem can also be formulated as a game in which a first"
[^c4]: arxiv-2602-20638 — "Single rectangle queries make it possible to elicit the anonymized"
[^c5]: arxiv-2602-20638 — "neighboring rectangles queries provide coupling constraints allowing"
[^c6]: arxiv-2602-20638 — "Finally, in order to obtain all marginal value functions, one can"
[^c7]: arxiv-2602-20638 — "Querying from the top left corner ensures"
[^c8]: arxiv-2602-20638 — "but defining an elicitation procedure to identify n"
[^c9]: arxiv-2602-20638 — "First, our work is limited to additive value functions"
[^c10]: arxiv-2602-20638 — "In another variant of the game (not considered in this"
