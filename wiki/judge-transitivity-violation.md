---
description: "A judge's round-robin of pairwise verdicts is scored by the fewest verdicts that must flip to make it a weak total order (transitive, ties allowed); this measures global, not local, consistency."
aliases: ["weak total order violation", "TOV", "preference transitivity violation", "global logical consistency of a judge"]
sources: ["arxiv-2512-16041"]
---
# Judge transitivity violation

A pairwise judge asked about every pair among n candidate answers to one question returns a set of verdicts. Those verdicts can contain cycles (A over B, B over C, C over A), which no ranking can satisfy. The Sage suite (arxiv-2512-16041) scores this as Weak Total Order Violation, TOV: the number of verdicts that must change so the judge's preferences become a weak total order, a total order that allows ties.[^c1]

The procedure runs in two steps. For each question, every unordered pair is queried in both orders, and the two verdicts give one preference matrix. TOV is then the minimum number of entries to alter so that some valid weak order fits the matrix.[^c2] The paper's Figure 2 example has four answers, three inconsistent pairs, and an IPI of 0.5; the same example needs three alterations to reach a consistent ranking, so TOV is 3.[^c2] The paper states the rationale directly: a rational judge's preferences "should be transitive and form a weak total order".[^c3]

The measure is global in a specific sense. The local measure, intra-pair instability, counts only pairs whose verdict fails to invert under reversal. A judge can pass that test on every pair and still hold a cycle across three answers. TOV is the test that sees the cycle (this distinction is my inference from the two definitions).

What was measured: across thirteen LLMs on 650 questions, every model degraded from the easier tier to the harder one, "with an approximately 200% increase on IPI and TOV scores".[^c4] The paper reports that the top models "fail to maintain consistent preferences in nearly a quarter of difficult" cases.[^c5] The authors also applied the same measure to human annotators, where TOV "surges to 6.523 on complex tasks".[^c6] For external validity, the paper reports "their high correlation with supervised benchmarks like" LLMBar and RewardBench2.[^c7]

## Limits

- Coherence is not correctness. A judge that is consistently wrong has no cycles and a TOV of zero. The paper's accuracy claim is a correlation with benchmarks, and the text says the authors "argue that Sage can also function as an effective proxy for" accuracy.[^c8]
- Ties are allowed by the definition. A judge that calls many pairs equal can have a low TOV without discriminating between answers (my inference from the definition; not tested in the passages read).
- The score is for pairwise judging only; the scoring setting is not given a transitivity measure in this work.
- The variance bound on TOV assumes independence across judgments,[^c9] and the paper's worked example uses n = 6 answers per question.[^c10] The behaviour at other set sizes is not reported in the passages read.
- A nonzero TOV on human labels shows that cycles also occur when people judge, so TOV does not by itself locate the fault in the judge rather than in a hard task.

## Related

- [[pairwise-judge-over-scalar-reward]] — why judges are asked for pairwise verdicts in the first place
- [[restricted-domain-pairwise-majority-benchmarking]] — coherence of pairwise majority across several metrics; TOV is the single-judge version of the same concern (my reading)
- [[llm-judge-biases]] — the order-swap flip rate, the local counterpart that TOV extends
- [[situational-preference]] — the proposed cause of many of these cycles: criteria that shift from one answer pair to the next

[^c1]: arxiv-2512-16041 — "should be transitive and form a weak total order"
[^c2]: arxiv-2512-16041 — "The TOV score is defined as the minimum number of preference changes"
[^c3]: arxiv-2512-16041 — "calculating the minimum alterations required for a consistent ranking"
[^c4]: arxiv-2512-16041 — "with an approximately 200% increase on IPI and TOV scores"
[^c5]: arxiv-2512-16041 — "fail to maintain consistent preferences in nearly a quarter of difficult"
[^c6]: arxiv-2512-16041 — "TOV surges to 6.523 on complex tasks"
[^c7]: arxiv-2512-16041 — "their high correlation with supervised benchmarks like"
[^c8]: arxiv-2512-16041 — "we argue that Sage can also function as an effective proxy for"
[^c9]: arxiv-2512-16041 — "Assuming independence across judgments"
[^c10]: arxiv-2512-16041 — "Given that we generate n = 6 candidate answers"
