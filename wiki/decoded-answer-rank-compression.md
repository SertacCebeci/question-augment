---
description: "Reducing a model's answer distribution to its single decoded answer collapses inputs onto few scores; ties, not coarse order, cost most of the ranking quality, and answer probabilities restore it."
aliases: ["decoded-answer scoring vs probability-weighted scoring", "answer-probability tie-breaking", "decoding ties"]
sources: ["doi-10-48550-arxiv-2608-21244"]
---
# Decoded-answer rank compression

A generative model asked a question answers with a distribution over a finite ordered answer set, and the usual practice keeps only the most probable answer. If that answer is then used as a score for ranking inputs (anomalous above normal), every input with the same decoded answer gets the same score. The paper calls this many-to-one loss of ordering decoded-answer rank compression.[^c1] With |A| possible answers the decoded score can take at most |A| distinct values, however much the underlying distributions differ.[^c2]

## Mechanism

The comparison holds the model, input, prompt and answer probabilities fixed and changes only the conversion: decoded-answer scoring takes the anomaly value of the argmax answer; probability-weighted scoring takes the expected anomaly value under the normalised answer distribution.[^c3]

Measured result: probability-weighted scoring beat decoded scoring in all 112 model-scale-benchmark comparisons, with mean gains from 7.66 points (UCF-Crime) to 19.95 points (VisA).[^c4]

Where the gap lives: keeping the decoded ordering between different answers and using probabilities only to break ties within an answer recovered at least 95.2% of the average gap on every benchmark across seven answer scales.[^c5] So the lost information is mostly within-answer order, not between-answer order.

A finer answer scale does not fix it, because the model does not use the scale. On decimal scales allowing 11, 51 and 91 answers, decoded scoring produced only 7.5, 8.8 and 13.5 distinct scores on average.[^c6] More distinct scores alone was not sufficient for better ranking either.[^c7]

Evaluation side effect: a tied anomalous-normal pair receives half credit in AUROC, and the paper argues that scoring tied inputs one at a time makes the reported area depend on input order, so ties must be evaluated together.[^c8]

## Why it matters for asking and answering

An asker that reads an answerer's reply as one decoded label discards the answerer's confidence ordering, the same loss as turning a hedge into a bare yes/no. This transfer is my inference, not tested in the paper.

## Limits

- Evidence is from vision-language anomaly detection with open-weight models and ranking metrics (AUROC, AP); nothing tests question answering, dialogue or decision quality.
- Probability-weighted scoring needs access to answer log-probabilities; models that return only text cannot be scored this way.
- The share of the gap explained by ties is an average per benchmark, not guaranteed per model or category.
- That the within-tie order is useful depends on the probabilities being informative; the paper shows this for anomaly data only.

## Related

- [[verbal-probability-expressions]] — coarse verbal answers also lose ordering that a number would keep
- [[calibration]] — probabilities help ranking only if they order correctly
- [[semantic-entropy]] — another use of the answer distribution rather than one decoded answer
- [[expected-answer-utility-ranking]] — expectation over the answer distribution, as in the probability-weighted score

[^c1]: doi-10-48550-arxiv-2608-21244 — "this many-to-one loss of ordering decoded-answer rank compression."
[^c2]: doi-10-48550-arxiv-2608-21244 — "can therefore produce at most |A| distinct"
[^c3]: doi-10-48550-arxiv-2608-21244 — "Thus the two scoring rules start from the same answer distribution and differ only in how to convert"
[^c4]: doi-10-48550-arxiv-2608-21244 — "P ROB outperforms D EC in all 112 model-scale-benchmark comparisons"
[^c5]: doi-10-48550-arxiv-2608-21244 — "Across all seven scales, it recovers at least 95.2% of the average gap on every benchmark."
[^c6]: doi-10-48550-arxiv-2608-21244 — "produces only 7.5, 8.8, and 13.5 distinct scores on average, respectively."
[^c7]: doi-10-48550-arxiv-2608-21244 — "More distinct scores do not imply better ranking."
[^c8]: doi-10-48550-arxiv-2608-21244 — "Thus, a tied anomalous–normal pair receives half credit"
