---
description: "Cost per usable output is nominal cost divided by the share of calls that parse on the first attempt, so schema and JSON failures raise the price of each answer a model actually gives."
aliases: ["reliability-adjusted cost", "ECR@1", "evaluation completion rate", "first-attempt completion rate", "cost per valid output"]
sources: ["arxiv-2512-01232"]
---
# Retry-adjusted cost

A call to a language model has a price, but a call whose output is used as a judgement, an extraction or a structured answer is worth that price only when the output parses and meets the required schema. The work this note rests on measures the failure side as a count. Its Evaluation Completion Rate is the "percentage of evaluations that produce valid, parseable output" on the first attempt.[^r1] The failures it counts are "API timeouts, malformed JSON, or schema violations".[^r2] The paper pairs the rate with mean attempts, total API calls divided by valid evaluations obtained, and with a cost scaled by the rate. "To account for retry overhead during deployment, we define an adjusted cost metric," which is the nominal cost multiplied by 100 over ECR@1 (its eq. 9).[^r3] The paper's own gloss is that this "captures the effective deployment cost when retries are required due to incomplete or failed evaluations."[^r4]

The mechanism is arithmetic. A failed attempt is paid for and yields nothing, so the price of a usable output is the price of an attempt divided by the probability that an attempt is usable. If attempts are independent and cost the same, the expected number of attempts per valid output is 1/p and the nominal cost is multiplied by 1/p. (my inference: the paper's formula has this form, but the text does not state the independence assumption.) What transfers from this paper is the division. The value of p is specific to one structured-output task and one set of models.

The adjustment bites only at the low end of reliability. Three models reach 100% ECR@1, and for them the two costs coincide: "models with perfect reliability (GPT-4o, GPT-4.1, GPT-5 low)" have "identical nominal and adjusted costs."[^r5][^r6] Where the rate falls, the price rises. GPT-OSS 20B at high effort, with 85.4% ECR@1, goes "up from $0.53 nominal" to $0.63 per 1K evaluations, an increase of 18.1%.[^r7] The same paper reports the other end: the cheapest open-weight models are at the bottom of the price range and in the moderate reliability tier, where "the reliability degradation manifests primarily as JSON parsing errors and occasional schema violations."[^r8]

This matters for choosing a model on price alone. A ranking by nominal price per call can differ from a ranking by price per valid output, and the paper treats the two as separate axes: it names "reliability-aware metrics" that "capture deployment-critical robustness beyond accuracy alone."[^r9] The same division appears in [[tokens-per-correctness]], where the denominator is correct answers. Here the denominator is valid outputs, so format failure is priced in the same way that an incorrect answer would be.

## Limits

- One benchmark: 100 expert-written Jira-ticket scripts for one billing platform, each model run five times.[^r10] The spread across runs is large for some models. GPT-OSS 20B high is reported at "85.4±5.7%" ECR@1, and the paper calls that variance a production problem.[^r11]
- The adjustment assumes each retry costs what the first attempt cost and succeeds at the same rate. The text read does not test whether failures cluster within a run or cost more on retry. The mean attempts reported for the more reliable models are close to one, for example "requiring minimal retries (mean attempts: 1.00–1.04)" for the high-reliability tier,[^r13] so the correction is small there; it is not tested where failures are correlated. (my inference)
- ECR@1 counts failures to produce parseable output, not failures of content. It does not say whether a retried output is as accurate as a first-attempt one, and the text read does not say whether retried outputs enter the accuracy figures separately.
- Latency is the other cost of a retry. The paper names "predictable costs and latencies" as the reason for perfect reliability but measures tokens and calls, not time.[^r12]
- Prices are the list prices of the study period, and the reported 175× span depends on them.

## Related

- [[tokens-per-correctness]] — the same division by a success count, applied to correct answers rather than valid outputs
- [[judge-reasoning-effort-tradeoff]] — the same paper's reasoning-effort results; effort changes how often a judge's output parses, not only its accuracy and price

[^r1]: arxiv-2512-01232 — "percentage of evaluations that produce valid, parseable output"
[^r2]: arxiv-2512-01232 — "malformed JSON, or schema violations"
[^r3]: arxiv-2512-01232 — "To account for retry overhead during deployment, we define an"
[^r4]: arxiv-2512-01232 — "retries are required due to incomplete or failed evaluations."
[^r5]: arxiv-2512-01232 — "models with perfect reliability (GPT-4o, GPT-4.1, GPT-5 low)"
[^r6]: arxiv-2512-01232 — "have identical nominal and adjusted costs."
[^r7]: arxiv-2512-01232 — "GPT-OSS 20B (high) reaches $0.63/1K (up from"
[^r8]: arxiv-2512-01232 — "the reliability degradation manifests"
[^r9]: arxiv-2512-01232 — "capture deployment-critical robustness beyond accuracy"
[^r10]: arxiv-2512-01232 — "on 100 expert-annotated scripts"
[^r11]: arxiv-2512-01232 — "The high variance (±5.7%) indicates inconsistent behavior across runs,"
[^r12]: arxiv-2512-01232 — "predictable costs and latencies in"
[^r13]: arxiv-2512-01232 — "requiring minimal retries (mean attempts: 1.00–1.04)"
