---
description: "A component is scored by the share of time its decision in force, the answer its application still applies, is correct; a late answer loses credit as a stale decision."
aliases: ["in-force accuracy", "decision in force"]
sources: ["doi-10-48550-arxiv-2609-38612"]
---
# Decision-in-force accuracy

When an application keeps applying a model's answer until a newer one arrives, the user lives with the decision in force at each instant, not with the answer the model returned. StreamDecisionBench (SDB) therefore evaluates "an embedded decision component by its decision in force at every instant".[^c1] A response takes effect only if its source is newer than the active decision, "so an older response never overwrites a newer one".[^c2] Between arrivals the application holds each decision until the next, so the decision in force is a zero-order hold over continuous time.[^c3]

The score counts time, not calls. In-force accuracy is the fraction of observed time with a correct decision in force, with every instant weighted equally.[^c4] Latency costs accuracy because the reference keeps moving while an answer is on its way. A component that is always right but takes effect L seconds after each time step loses about L at every change of the reference decision, so its in-force accuracy depends on its judgment, its latency and how often the reference changes.[^c5] The last term is the one a single untimed accuracy number hides: "The cost of latency thus grows with the rate of reference changes."[^c6]

The primary summary is a normalized log-AUC. Accuracy is measured at update intervals from 0.5 to 8 s, the area under that curve is taken against log interval, and the result is averaged across four scenario families.[^c7] The log weighting is chosen so that "Our objective is to give equal weight to equal" multiplicative ranges of environment speed.[^c19]

The metric has a limiting case. "At zero latency each answer is in force during its own time step", so in-force accuracy reduces to untimed accuracy.[^c8] The paper also writes in-force accuracy as roughly the product of untimed accuracy U and an oracle in-force accuracy O (the in-force accuracy of the reference answers at the component's recorded latencies), with a small correction. That approximation holds when "judgment errors are unrelated to timing".[^c9] It is the paper's derivation from its own formula. The paper says a later section tests this form, since it is the step "§6.1 tests".[^c20] That section was not read for this note, so the approximation is not verified here.

Measured on the benchmark, the split separates kinds of limit. The slower, more accurate models lose "more accurate models lose 42–51% of the time" to outdated answers, while the fast model loses its share to wrong ones: "to outdated answers, a fast model 34% to wrong ones".[^c10][^c21] A hybrid in which a slow model corrects a fast one can do better: with the right pairing and configuration, a hybrid outperforms every single model.[^c12] Even so, "even the best evaluated system keeps a correct decision in force" only about two-thirds of the time.[^c11]

## Limits

- The scenarios are "controlled synthetic timelines", eight of them in four families, written so that every reference transition has a known cause.[^c13] The paper names as the needed follow-up "streams built from logged application sessions under declared rules", which would show how far the latency and judgment limits generalize.[^c22] None was run here.
- The reference decisions implement declared public rules, so the metric measures agreement with those rules. "Adjudication by human domain experts would check" the references against the rule text and test whether the rules are sound policy.[^c14] Until then the reference is a stipulation, not an independent truth.
- The number depends on choices the reader must report. "Weighting and bounds also matter": linear averaging over 0.5–8 s reverses the ordering of two of the settings the paper compares.[^c15] The paper concludes that "the score, must always be reported with that interval".[^c16]
- The interval sweep does not re-run the model at each update rate. It re-times the recorded answers, and it "assumes that changing request frequency would not change service latency".[^c17] Its evaluation at other intervals "changes only the timing of recorded answers".[^c18] A real system whose latency rises with request rate would not be captured (my reading, not tested).
- The metric says nothing about which of two components should be applied when both answer. The paper states that "Fast/slow composition additionally requires an explicit arbitration" rule, because a more accurate correction can still lower in-force accuracy by replacing a fresher decision.[^c23] See [[judgment-latency-error-attribution]].

## Related

- [[judgment-latency-error-attribution]] — splits the instants this metric counts as wrong into judgment, latency and compound errors
- [[insight-stream-metrics]] — also scores the timing of a stream of decisions, but per decision and with a timing penalty, not as a held state over time
- [[uncertainty-sampling-regime-shift-lag]] — another cost paid after the world changes: there a lag in learning, here a lag in applying the answer
- [[cost-priced-joint-selection-and-stopping]] — treats latency as a cost in choosing when to stop asking; in-force accuracy puts latency inside the score itself

[^c1]: doi-10-48550-arxiv-2609-38612 — "We therefore evaluate an embedded decision component by its decision in force at every instant"
[^c2]: doi-10-48550-arxiv-2609-38612 — "so an older response never overwrites a newer"
[^c3]: doi-10-48550-arxiv-2609-38612 — "holds each decision until the next, so, following"
[^c4]: doi-10-48550-arxiv-2609-38612 — "instants equally: it is the fraction of observed time"
[^c5]: doi-10-48550-arxiv-2609-38612 — "every change of the reference decision, so the share"
[^c6]: doi-10-48550-arxiv-2609-38612 — "The cost of latency thus grows with the rate of"
[^c7]: doi-10-48550-arxiv-2609-38612 — "families is normalized log-AUC, the area under this"
[^c8]: doi-10-48550-arxiv-2609-38612 — "At zero latency each answer is in force during its"
[^c9]: doi-10-48550-arxiv-2609-38612 — "If judgment errors are unrelated to timing"
[^c10]: doi-10-48550-arxiv-2609-38612 — "more accurate models lose 42–51% of the time"
[^c11]: doi-10-48550-arxiv-2609-38612 — "even the best evaluated system keeps a correct decision in force"
[^c12]: doi-10-48550-arxiv-2609-38612 — "and configuration, a hybrid outperforms every"
[^c13]: doi-10-48550-arxiv-2609-38612 — "controlled synthetic timelines"
[^c14]: doi-10-48550-arxiv-2609-38612 — "Adjudication by human domain experts would check"
[^c15]: doi-10-48550-arxiv-2609-38612 — "Weighting and bounds also matter"
[^c16]: doi-10-48550-arxiv-2609-38612 — "the score, must always be reported with that interval"
[^c17]: doi-10-48550-arxiv-2609-38612 — "frequency would not change service latency"
[^c18]: doi-10-48550-arxiv-2609-38612 — "changes only the timing of recorded answers"
[^c19]: doi-10-48550-arxiv-2609-38612 — "Our objective is to give equal weight to equal"
[^c20]: doi-10-48550-arxiv-2609-38612 — "§6.1 tests"
[^c21]: doi-10-48550-arxiv-2609-38612 — "to outdated answers, a fast model 34% to wrong ones"
[^c22]: doi-10-48550-arxiv-2609-38612 — "streams built from logged application sessions under declared rules"
[^c23]: doi-10-48550-arxiv-2609-38612 — "Fast/slow composition additionally requires an explicit arbitration"
