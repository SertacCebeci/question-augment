---
description: "Timestamped forecasts submitted before the outcome exists make an evaluation leakage-free by ordering rather than curation, the forecast pre-registration protocol of TS-Arena."
aliases: ["forecast pre-registration protocol", "FPRP", "forecast preregistration", "pre-registered live evaluation", "forward-only evaluation"]
sources: ["arxiv-2512-20761"]
---
# Forecast pre-registration

A forecast can be checked against the future without any test set that could leak, if its commitment is fixed in time before the outcome exists. The TS-Arena platform does this for time series. A forecaster must submit predictions for a fixed horizon before the outcome is observed, and the paper's summary is that models must submit "predictions before the ground-truth data physically exists."[^c1] The registration window closes before the next value arrives, and "attempted after window closure is strictly rejected."[^c2] The authors take the result to be that "the test set remains logically inaccessible during the inference process."[^c3]

The paper calls this the forecast pre-registration protocol (FPRP). It "uses the evaluation time t as a strict temporal split point," which advances as real time passes.[^c4] Each round starts with a context of past observations, a registration window and a horizon. Once the horizon's true values have materialized, "the system computes the final error metrics."[^c5] A new round is opened later, so the same protocol repeats indefinitely and yields a continuing leaderboard rather than a one-off test set. The authors relate it to living benchmarks, but with one change: the evaluation targets "are generated in real-time by the unfolding future."[^c6]

The mechanism is ordering, not curation. The paper's argument is that a fixed dataset, however carefully built, "can eventually lead to information leakage," because training data for one model can overlap with test data for another, or correlated series can carry future information into a held-out test.[^c7] The protocol removes the test set from existence until commitment, so the authors claim it closes both direct contamination and indirect temporal leakage: "this protocol makes both direct and indirect information leakage impossible by design."[^c8]

What was measured. The first results come from operating the platform over one year of energy series. They report that "established TSFMs accumulate robust longitudinal scores over time."[^c9] The living benchmark "already comprises 186 different energy time series evaluated in over 5000 challenge" rounds,[^c10] "leading to over 3.9 million forecasted observations."[^c11] A newcomer can reach the top quickly, but the authors note that "their wide confidence intervals indicate a lack of statistical certainty."[^c12]

Transfer to asking and answering (my inference, not the paper's). The same ordering would apply to any question whose answer is settled later. If an answer is written with its timestamp before resolution, a later reader can tell whether it was fitted to the outcome. The paper does not study human or chat answers. It is a design for models that forecast numeric series.

## Limits

- Scope. The authors say that "the current scope of TS-Arena is intentionally narrower in terms of available datasets and configuration space."[^c13] All measurements are energy series.
- Sample size. The data is small against static benchmarks: "they are relatively small compared to the over 300 million data points in Gift-Eval."[^c14]
- Speed. A score accrues only as fast as outcomes arrive, so a model's standing needs time. The authors write that "evaluation period is necessary to distinguish between genuine generalization capability and temporary over-performance."[^c15]
- The guarantee covers the target, not the model. A model trained before commitment on related data still carries what it learned. The protocol removes only the future target. This boundary is my inference from the design.
- "Impossible by design" is the authors' phrase. In the slices I read, I did not see a controlled comparison of the same models under this protocol and under a retrospective split, so the size of the leakage it removes is not measured here.

## Related

- [[post-cutoff-corpus-benchmark-isolation]] — the retrospective route: isolate by a document-date window. Pre-registration isolates by the order of commitment and outcome and needs no cutoff date.
- [[benchmark-contamination-convergent-audit]] — the audit route: estimate exposure after the fact. Pre-registration keeps the target from existing during the commitment window.
- [[pre-committed-answer-before-cot]] — another commitment, made before the reasoning rather than before the outcome. I read only its title here, not its text.

[^c1]: arxiv-2512-20761 — "predictions before the ground-truth data physically exists"
[^c2]: arxiv-2512-20761 — "attempted after window closure is strictly rejected."
[^c3]: arxiv-2512-20761 — "the test set remains logically inaccessible during the inference process"
[^c4]: arxiv-2512-20761 — "It uses the evaluation time t as a strict temporal split point"
[^c5]: arxiv-2512-20761 — "the system computes the final error metrics"
[^c6]: arxiv-2512-20761 — "are generated in real-time by the unfolding future"
[^c7]: arxiv-2512-20761 — "can eventually lead to information leakage"
[^c8]: arxiv-2512-20761 — "this protocol makes both direct and indirect information leakage impossible by design"
[^c9]: arxiv-2512-20761 — "established TSFMs accumulate robust longitudinal scores over time"
[^c10]: arxiv-2512-20761 — "already comprises 186 different energy time series evaluated in over 5000 challenge"
[^c11]: arxiv-2512-20761 — "leading to over 3.9 million forecasted observations"
[^c12]: arxiv-2512-20761 — "yet their wide confidence intervals indicate a lack of statistical certainty"
[^c13]: arxiv-2512-20761 — "the current scope of TS-Arena is intentionally narrower in terms of available datasets"
[^c14]: arxiv-2512-20761 — "they are relatively small compared to the over 300 million data points in Gift-Eval"
[^c15]: arxiv-2512-20761 — "evaluation period is necessary to distinguish between genuine generalization capability and temporary over-performance"
