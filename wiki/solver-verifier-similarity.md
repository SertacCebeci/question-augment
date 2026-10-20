---
description: "A verifier tends to accept wrong answers more as its solution distribution resembles the solver's, so cross-family verification gains fall as solver-verifier similarity rises."
aliases: ["solver-verifier similarity", "solution-distribution similarity", "solver-verifier similarity bias", "verifier self-similarity bias"]
sources: ["arxiv-2512-02304"]
---
# Solver-verifier similarity

A verifier is a model that reads a problem and a candidate solution and says whether the solution is correct. The question studied here is whether the verifier's judgment depends on who wrote the candidate. The paper's answer is that it does, and that the dependence runs through how alike the two models' solutions are, not only through whether they are the same model.

The paper measures similarity as "the average cosine similarity between two models' solution embeddings across all dataset problems."[^c1] Each solver–verifier pair gets one score. The result is that "the more similar the solver and verifier distributions, the more likely the verifier is to accept incorrect answers."[^c2] In the cross-family setting, where the verifier is from a different model family than the solver, the paper finds that "cross-family gains decrease significantly as similarity increases."[^c3] The paper's summary is that "Higher similarity between solver and verifier solution distributions" increases the verifier's tendency to accept incorrect outputs and so reduces verifier gain (see [[verifier-gain]]).

The paper relates this to a human effect. "Humans tend to judge solutions that resemble their own reasoning as more likely correct. This mirrors self-enhancement bias."[^c4] The argument is by analogy: strong reasoning models gain least from self-verification and most from cross-family verification, and the authors read this as the same kind of preference for one's own output. Models also "favor solutions resembling their own reasoning", which is the claim the similarity measurement is meant to test.[^c5]

The bias is not uniform across settings. For intra-family verification, where the verifier and solver share a family, "intra-family verifier gains are too small to yield a strong correlation."[^c6] So the similarity effect is clear in the cross-family pairs and not established for the intra-family ones. The practical reading the paper gives is that "using a verifier with a meaningfully different solution distribution mitigates this bias."[^c7]

The note is about output distributions, so it sits beside the judge-bias notes. [[harmful-self-preference]] measures a judge's preference for its own answers against labels; the similarity here is measured on solutions and does not need a judge's identity. [[shared-belief-self-preference]] finds that a judge's preference follows its agreement with the content once surface style is removed. The paper's similarity score does not separate style from content, so it cannot say which of the two drives the verifier's acceptance.

## Limits

- The similarity is a correlation across pairs, not an intervention. The paper does not choose verifiers by dissimilarity and then measure a higher gain. The takeaway to use dissimilar verifiers is a reading of the correlation.
- Solver and verifier strength vary together across the pairs. A strong verifier and a dissimilar solver can both raise gain, so the design does not isolate similarity from capability.
- The score depends on one embedding model, sentence-transformers all-mpnet-base-v2, applied to solution text. The paper also computed a log-likelihood similarity with the same direction, but prefers cosine because "log-likelihood conflates distributional similarity with intrinsic predictability of the solver's text."[^c8]
- The cross-family correlations come from 108 pairs over 12 models; the intra-family analysis has 24 pairs and no strong correlation. Neither is large enough to state a threshold of similarity past which verification stops paying.
- The benchmarks are the nine exact-answer tasks named in the paper. Whether the same similarity effect holds for open-ended solutions, where the embedding measure is less stable, is not tested.
- Similarity is averaged over all problems. The paper does not show that a particular question's answer is accepted more because of similarity on that question.
- My inference, not the paper's: the cross-family result runs opposite to the handoff result in [[model-family-continuation-compatibility]], where a cross-family continuation of a partial reasoning chain looked worst. The two concern different objects (a verifier judging a finished answer, against a model continuing another's chain), so the contrast is a question for the wiki rather than a conflict.

## Related

- [[verifier-gain]] — the measure that similarity lowers in the cross-family setting
- [[harmful-self-preference]] — the judge's preference for its own answers, measured against labels; the similarity score is a distributional analogue of that tendency
- [[shared-belief-self-preference]] — preference that follows the judge's agreement with content once style is removed; the paper's similarity score does not separate style from content
- [[model-family-continuation-compatibility]] — the cross-family handoff of partial reasoning, which looked worst there while cross-family verification looks best here
- [[spontaneous-self-verification]] — the reason the paper gives for why self-verification gains are small, which is a different route from similarity

[^c1]: arxiv-2512-02304 — "average cosine similarity between two models’ solution embeddings across all dataset problems"
[^c2]: arxiv-2512-02304 — "the more similar the solver and verifier distributions, the more likely the verifier is to"
[^c3]: arxiv-2512-02304 — "cross-family gains decrease significantly as similarity increases"
[^c4]: arxiv-2512-02304 — "This mirrors self-enhancement bias"
[^c5]: arxiv-2512-02304 — "Models often favor solutions resembling their own"
[^c6]: arxiv-2512-02304 — "intra-family verifier gains are too small to yield a strong correlation"
[^c7]: arxiv-2512-02304 — "Using a verifier with a meaningfully different solution distribution mitigates this bias"
[^c8]: arxiv-2512-02304 — "we prefer cosine similarity as the primary metric"
