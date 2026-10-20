---
description: "Model-internal uncertainty and retrieval-based verification miss different factual errors, so combining them beats either one alone on the same LLM outputs."
aliases: ["HD-FV complementarity", "hallucination detection and fact verification complementarity", "orthogonal error boundaries", "hybrid factuality detection"]
sources: ["arxiv-2512-02772"]
---
# Intrinsic-extrinsic signal complementarity

A factuality judgment about an LLM answer can draw on two sources. The first is the model's own generation process: token uncertainty, activation patterns, agreement across sampled answers. The second is outside evidence, retrieved and compared with the claim. The paper calls the first family hallucination detection (HD) and the second fact verification (FV). Run on the same generated outputs, the two families do not fail on the same items: "HD and FV methods consistently succeed on different subsets of factual errors."[^i1]

The paper gives a mechanism for the split, though it is an analysis of cases rather than a count. FV "is fundamentally limited by its reliance on retrieval quality."[^i2] When the retriever misses the relevant passage, the verifier either rejects a true claim or accepts a false one. HD fails another way. On expressive answers, where the same fact can be phrased many ways, a detector that reads uncertainty as error flags correct output: the paper reports that "the high entropy caused by diverse phrasing is misinterpreted as hallucination."[^i3] The two sources are blind in different places, and that is the precondition for a combination to gain.

The roles the paper assigns follow from this. FV "functions as a precision-oriented anchor" when it retrieves evidence, and HD "functions as a recall-oriented safety net" that can flag errors without any outside knowledge.[^i4][^i5] The authors summarize the case analysis as the claim that "HD and FV operate with orthogonal error boundaries."[^i6]

The complementarity is also measured, on pairs of methods. Three pairwise statistics are used. The average complementarity score (ACS) is the share of samples that exactly one of the two methods gets right, which is "the classical disagreement rate between two classifiers."[^i7] The average synergy gain (ASG) is the headroom of an oracle that is right whenever either method is.[^i8] The average error correction rate (AECR) is how often one method is right on the cases where the other fails; it "quantifies the capacity of one method to compensate for" another's errors.[^i17] The paper reports that cross-paradigm pairs, one HD and one FV, score higher on ACS than pairs within a paradigm: "ACS for cross-paradigm pairings indicates that their successes are" more mutually exclusive than within-paradigm pairs.[^i9]

Two integrations follow. Score-level fusion averages the normalized HD and FV scores, "effectively taking the average of" the two, with no tuning.[^i16] An evidence-aware pipeline accepts FV when retrieval returns a definite verdict, Supported or Contradicted, and falls back "to internal signals" when the verdict is Not Enough Information.[^i10] Both are reported to beat each input: "hybrid strategies consistently establish a new upper bound for performance across diverse datasets and model architectures."[^i11] The paper states the design rule as conditional: an optimal hybrid "should not assign equal importance to both," but should trust the outside check when it returned evidence on point and rely on the internal signal when it did not.[^i18]

## Limits

- Disagreement is not gain. ACS counts where two methods differ; it does not say a combination will profit from the difference. ASG is an upper bound, "an ideal oracle ensemble over the best-performing individual method," not a realized improvement.[^i12]
- The split depends on the model and the task. "performance varies significantly with" the underlying LLM and the task, and on one family the paradigms are close: "the two paradigms split the victories evenly."[^i13][^i14]
- The labels are the framework's own. Correctness comes from an automated judge: the framework "employs an automated labeling system to determine correctness by comparing" the output with reference answers.[^i15] The complementarity is measured against that judge's verdicts, not against independent human labels.
- The mechanism is qualitative. The orthogonality claim rests on illustrative cases in the error tables; I did not find a per-error count of how often the two sources fail on disjoint items beyond the ACS statistic itself. The reading that the failure modes are "orthogonal" is the authors', and I have not checked it against more cases.
- The FV side is retrieval-based. Complementarity is claimed against verifiers that consume retrieved evidence. A verifier that reads no evidence, such as [[retrieval-free-fact-checking]], is an HD-type signal and is not tested here as the FV partner.
- The fusion weight is fixed at 0.5 and the pairs tested are a few named methods on two model families. Whether a learned weight or other pairings do better is not tested.

## Related

- [[analytic-llm-detection-complementarity]] — a rule-based checker and an LLM judge also miss different errors; there the sources are a pattern matcher and a model, here they are the model's internals and retrieved evidence.
- [[retrieval-free-fact-checking]] — the internal-signal side with no evidence at all; this note's complementarity needs the retrieval side.
- [[semantic-entropy]] — an intrinsic signal, and the one whose false alarm on phrasing variety this paper also reports.
- [[uncertainty-band-corroboration-gate]] — uses internal uncertainty to decide whether to retrieve, the reverse order of the fallback described above.
- [[evidence-insufficiency-regimes]] — the ways retrieved evidence falls short, which is where the FV side loses.
- [[uncertainty-hallucination-relevance-gap]] — a broad finding that uncertainty estimators are weak, task-dependent triggers for hallucination; this note asks what they add beside retrieval rather than alone.

[^i1]: arxiv-2512-02772 — "HD and FV methods consistently succeed on different subsets of factual errors"
[^i2]: arxiv-2512-02772 — "is fundamentally limited by its reliance on retrieval quality"
[^i3]: arxiv-2512-02772 — "by diverse phrasing is misinterpreted as hallucination"
[^i4]: arxiv-2512-02772 — "FV functions as a precision-oriented anchor"
[^i5]: arxiv-2512-02772 — "HD functions as a recall-oriented safety net"
[^i6]: arxiv-2512-02772 — "HD and FV operate with orthogonal error boundaries"
[^i7]: arxiv-2512-02772 — "ACS corresponds to the classical disagreement rate between two classifiers"
[^i8]: arxiv-2512-02772 — "performance improvement of an ideal oracle ensemble over the best-performing individual method"
[^i9]: arxiv-2512-02772 — "ACS for cross-paradigm pairings indicates that their successes are"
[^i10]: arxiv-2512-02772 — "falling back to internal signals"
[^i11]: arxiv-2512-02772 — "hybrid strategies consistently establish a new upper bound for performance across diverse"
[^i12]: arxiv-2512-02772 — "an ideal oracle ensemble over the best-performing individual method"
[^i13]: arxiv-2512-02772 — "performance varies significantly with"
[^i14]: arxiv-2512-02772 — "the two paradigms split the victories evenly"
[^i15]: arxiv-2512-02772 — "employs an automated labeling system to determine correctness by comparing"
[^i16]: arxiv-2512-02772 — "effectively taking the average of"
[^i17]: arxiv-2512-02772 — "quantifies the capacity of one method to compensate for"
[^i18]: arxiv-2512-02772 — "should not assign equal importance to both"
