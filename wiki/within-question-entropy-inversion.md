---
description: "Within one question's candidates, a misleading passage lowers a frozen respondent's answer entropy, so keeping the lowest-entropy candidate picks misleading passages more often than chance."
aliases: ["confidently-wrong problem", "misleading-passage entropy trap", "minimum-entropy passage selection failure"]
sources: ["doi-10-48550-arxiv-2608-11922"]
---
# Within-question entropy inversion

Choosing among a question's retrieved candidates without gold answers is often done by keeping the candidate whose answer the respondent produces with the least uncertainty. A frozen respondent reads each passage alone and produces one answer per passage, and the answer-token entropy of that answer is the score. The rule was measured to help: over five open-domain QA benchmarks it lifts mean answer F1 from 0.4769 to 0.5148 relative to the retriever's top-ranked passage.[^i1]

The failure is that the same rule is pulled toward the wrong passages. Within a single question, a misleading passage lowers the respondent's entropy, so the minimum-entropy candidate is more likely to be a misleading one. The paper states the mechanism as a confident error: "A misleading passage makes the respondent confidently wrong," with the entropy driven down where the signal looks most trustworthy.[^i2] In its Figure 1 example the misleading passage has the lowest entropy of all ten candidates, and the rule keeps the answer that passage induces, which is wrong.[^i3]

The gap is small in its mean but consistent in direction. Pooled over the five pools, judged-misleading candidates carry a first-token entropy of 1.22 nats, against 1.33 for the rest of the set.[^i4] As a selection rate, minimum-entropy selection reads a misleading passage 30.3% of the time, against 28.9% for the pool's own rate, which is what drawing one of the ten at random gives.[^i5] Low entropy is also no guarantee: the passage this rule selects still yields an answer with zero exact match 59.6% of the time.[^i6]

The retriever does not fix it. The paper reports that bge-m3 puts a higher average share of misleading passages in the top ten than Contriever, 28.9% against 20.3%, and that "using a stronger retriever or adding a reranker drives" that rate up rather than down.[^i7]

The inversion is a within-question comparison. Prior results that low entropy does not imply correctness, and that stronger retrieval lowers predictive entropy, describe how entropy behaves across questions. The paper's point is that a selector compares only the candidates of one question, so the across-question result does not say which candidate to trust.[^i8][^i9]

My inference: this is the within-question counterpart of the across-question confidently-wrong regime, where a consistent wrong answer reads as settled. The two share a mechanism but differ in where the contrast is made.

## Limits

- The gap is reported as a mean and as a selection rate. This text does not show the within-question spread, so how often a single question inverts is not established here (my inference from the reported numbers).
- The "misleading" label is strict: a passage counts as MISLEADING only when both LLM judges agree, and otherwise it is treated as not misleading.[^i10] The judges' reliability bounds the gap that can be seen.
- The paper gives a confident-error account of why the entropy drops. It does not isolate the respondent-internal cause in the passages read here. My guess that a fluent, specific false fact gives the decoder a short settled continuation is untested.
- The entropy figures above are for the frozen respondent of the main setup, Llama-3.1-8B-Instruct.[^i11] The text does not show the same inversion for other respondents.
- The gap is stated for first-token entropy, the estimator the main results use. Whether all-token entropy inverts in the same way is not shown in the passages read.

## Related

- [[confidently-wrong-low-entropy-regime]] — the across-question form of the same blind spot, from hallucination detection
- [[first-token-entropy]] — the single-pass entropy in which this inversion is measured
- directed-entropy — a learned input intervention that moves this entropy back, so the minimum can fall on supporting passages

[^i1]: doi-10-48550-arxiv-2608-11922 — "lifts mean answer F1 from 0.4769 to 0.5148"
[^i2]: doi-10-48550-arxiv-2608-11922 — "A misleading passage makes the respondent confidently wrong"
[^i3]: doi-10-48550-arxiv-2608-11922 — "the lowest-entropy rule keeps the answer that passage induces, which is wrong."
[^i4]: doi-10-48550-arxiv-2608-11922 — "on judged-misleading candidates against 1.33 on the rest of the candidate set"
[^i5]: doi-10-48550-arxiv-2608-11922 — "reads a misleading passage more often on average than drawing one of the ten at random, 30.3% against the"
[^i6]: doi-10-48550-arxiv-2608-11922 — "still yields an answer with zero exact match 59.6% of the time"
[^i7]: doi-10-48550-arxiv-2608-11922 — "bge-m3 puts a higher average share of misleading passages in the top-10 than retrieving with Contriever"
[^i8]: doi-10-48550-arxiv-2608-11922 — "Both describe how entropy behaves across questions"
[^i9]: doi-10-48550-arxiv-2608-11922 — "only compares the candidates of one question"
[^i10]: doi-10-48550-arxiv-2608-11922 — "A passage counts as MISLEADING only when both agree that it is"
[^i11]: doi-10-48550-arxiv-2608-11922 — "The frozen respondent is Llama-3.1-8BInstruct"
