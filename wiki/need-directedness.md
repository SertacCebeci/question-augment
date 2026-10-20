---
description: "A need is evaluable only if it is directed enough to tell valid answers from invalid ones; a latent need cannot be checked, so sufficiency is judged on its expressed form."
aliases: ["directedness", "directedness of insight needs", "directed versus loosely directed need", "sufficient specification of a need"]
sources: ["doi-10-48550-arxiv-2609-07629"]
---
# Need directedness

An insight need can be more or less directed. A highly directed need targets "highly directed, targeting specific phenomena, entities, or" relationships, as in a question about how one quantity relates to another. A loosely directed need leaves "where the analytical perspective remains open", as in a question about what patterns a dataset holds.[^d1][^d2] The dimension is not a matter of tone. It decides whether an answer can be judged at all: the need is directed enough when "it is determinable whether candidate analytical knowledge satisfies the need."[^d3]

The reason is that the need itself is hidden. The paper says that "no party can check this condition directly", so the test has to be run on what the person actually wrote or said.[^d4] The expressed form can fall short of the need. The need "may not be entirely specified in their" expression of it, and the gap runs between "latent need and expressed need", a gap the paper traces to Taylor's model of how information needs form.[^d5][^d6]

## Mechanism

The paper makes the test concrete as sufficient specification. An expressed need is sufficient when it lets a system separate realizations that satisfy the need from those that do not, which requires its data, method and output components to be "specified or can be inferred".[^d7] Two examples mark the boundary. "What is the average temperature in Amsterdam in January?" is sufficient, because "implicit methodological details can be resolved through conventions and reasonable defaults."[^d8] "How does construction waste compare?" is not, because "no convention fixes what to compare against", so valid and invalid answers cannot be told apart.[^d9]

The same section adds a second condition that the wording cannot repair. A need can be fully specified and still have no answer in the corpus: "the insight need cannot be resolved, an instance of insufficient data coverage."[^d10] So an unanswerable question and an underspecified one are different failures. The first lacks data; the second lacks a convention for judging the answer. Only the second can be fixed by the asker rewording the question.

For the asker this gives a usable split. Before asking, one can check whether the question fixes what would count as a correct answer, and separately whether the data for it is likely to exist. For the answerer, a directed need is one where candidate answers can be scored against the same criterion; a loose one needs the answerer to choose the criterion first, which is where the answer can drift from what was meant.

## Limits

- The paper gives the dimension with two examples and no scale. The text does not say how to rate a given question's directedness, so a reader cannot score a question from the paper alone.
- Sufficiency is defined conceptually and "operationalized" on the expression of the need. The text gives examples, not a threshold or a measured rate of sufficient questions.
- The temperature example depends on "reasonable defaults". Whether an asker's default matches the answerer's is not tested here.
- The setting is tabular data and analytical systems. Carrying the split to open-domain or conversational questions is my inference, not the paper's claim.
- Nothing in the text measures whether asking for more direction improves answers. The claim is that a need without a criterion cannot be checked, not that adding one raises answer quality.

## Related

- [[analytical-information-need]] — sorts needs by analytical depth; directedness is a separate axis about whether an answer can be judged at all.
- [[structural-versus-semantic-underspecification]] — splits gaps by which failure they cause (execution or correctness); sufficiency here covers data, method and output together and does not split by failure type.
- [[levels-of-information-need]] — Taylor's ladder for how a need is formed in words; the latent-expressed gap above draws on the same model.

[^d1]: doi-10-48550-arxiv-2609-07629 — "highly directed, targeting specific phenomena, entities, or"
[^d2]: doi-10-48550-arxiv-2609-07629 — "where the analytical perspective remains open"
[^d3]: doi-10-48550-arxiv-2609-07629 — "it is determinable whether candidate analytical knowledge satisfies the need"
[^d4]: doi-10-48550-arxiv-2609-07629 — "no party can check this condition directly"
[^d5]: doi-10-48550-arxiv-2609-07629 — "may not be entirely specified in their"
[^d6]: doi-10-48550-arxiv-2609-07629 — "This gap between latent need and expressed need mirrors the classical"
[^d7]: doi-10-48550-arxiv-2609-07629 — "Sufficient specification describes the expressed need"
[^d8]: doi-10-48550-arxiv-2609-07629 — "implicit methodological details can be resolved through conventions and reasonable defaults"
[^d9]: doi-10-48550-arxiv-2609-07629 — "no convention fixes what to compare against"
[^d10]: doi-10-48550-arxiv-2609-07629 — "the insight need cannot be resolved, an instance of insufficient data coverage"
