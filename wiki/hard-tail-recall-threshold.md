---
description: "At a coverage target the threshold is set by the hardest positives, so high AUC can still flag nearly every valid output; average separation does not bound the cost at high recall."
aliases: ["worst-case tail threshold", "high-recall threshold cost", "tail-set conformal threshold"]
sources: ["arxiv-2512-15068"]
---
# Hard-tail recall threshold

A detector asked to catch a fixed share of positives turns that requirement into one number, a threshold. In the split conformal construction the paper uses, the calibration set holds only the positives ("where yi = 1"), and the threshold is the (1 − α) quantile of their scores, with a finite-sample correction. Whatever sits at the top of the positive score distribution therefore fixes the threshold. Every response on the positive side of it is flagged, and the cost falls on the negatives that land there.[^t1]

The positive class is rarely one bump. In the paper's HaluEval run, the DeBERTa entailment score gives a bimodal positive class: many hallucinations score near zero, while a tail of them achieves near-perfect entailment scores.[^t2][^t16] The class means differ, "while the means differ (0.93 vs 0.41)", but the spread of the hallucinated class is what matters for the threshold.[^t3] The quantile at 95% coverage lands in that tail. The paper reports τ̂ ≈ 0.999, which means flagging any response with less than 99.9% entailment probability.[^t4] Faithful responses nearly all lie below that line, so the false positive rate is 100%.[^t5]

The mechanism is an asymmetry between two summaries. AUC integrates over all thresholds and is dominated by the bulk of the two classes; a coverage constraint reads one place only, the tail. The paper states the consequence directly: "High AUC does not imply safety".[^t6] Its ablation shows the same thing from the other side. A learned combiner raises AUC from 0.81 to 0.83 and leaves the conformal FPR at 100%, which the paper reads as a failure of the features rather than of the aggregation.[^t7]

What survives the transfer from statistics is the construction and its guarantee: the threshold is a calibrated quantile, and coverage holds in the marginal sense. What does not survive is usefulness. The guarantee can be valid while the set it certifies rejects almost every valid output. On HaluEval the paper's table reports 94.5% actual coverage against a 95% target, with 100% FPR.[^t8] That 94.5% is within the sampling noise of a test split of roughly 400 items (my inference), so the guarantee is not what fails here; the overlap is.

The same tail-over-mean asymmetry shows up in another setting: scoring an agent trajectory by its worst step beats averaging when failures are sparse, see [[tail-focused-trajectory-risk-aggregation]].

## Limits

- One ensemble of three scores, two datasets for the real-data result, and one target (95%) are reported in the part of the text read. No curve between a 90% and a 99% target is shown, so the trade-off between coverage and FPR is not mapped; the 0% versus 100% endpoints are all the text gives.[^t9]
- The ablation on calibration size is on Natural Questions only, where the method already works.[^t10] The claim that more calibration data is "unlikely to close the 0% vs 100% gap" on HaluEval is asserted, not tested.[^t11]
- The text gives the score direction twice, and the two statements do not agree. Higher values are said to indicate hallucination,[^t12] but the flag rule is written as "assuming lower scores imply" faithfulness.[^t13] Taken literally, the rule would flag the faithful end. The reported FPRs suggest a notational slip rather than a different result, but I did not verify the sign in the code, which the paper points to but this reading did not open (my inference).
- Validity rests on exchangeability: "Validity is guaranteed by the exchangeability of the data" [^t14], and the paper itself notes that "distribution shift is inevitable as models are updated and user queries evolve".[^t15] The tail that sets the threshold is also the first place a drift in the generator would move.
- The paper's remedy, reasoning judges, is outside this note; the paper's claims about them are the subject of [[semantic-illusion]].

## Related

- [[conformal-prediction]] — the guarantee this threshold is built from; here the guarantee holds while the threshold is almost useless
- [[tail-focused-trajectory-risk-aggregation]] — the same tail-over-mean asymmetry in agent trajectories
- [[accuracy-masks-selective-reliability]] — a fixed-coverage risk reading that separates systems whose accuracy looks alike

[^t1]: arxiv-2512-15068 — "where yi = 1"
[^t2]: arxiv-2512-15068 — "many hallucinations are obvious"
[^t16]: arxiv-2512-15068 — "achieves near-perfect entailment scores"
[^t3]: arxiv-2512-15068 — "while the means differ (0.93 vs 0.41)"
[^t4]: arxiv-2512-15068 — "meaning we must flag any response with less than 99.9% entailment probability"
[^t5]: arxiv-2512-15068 — "Since virtually all faithful responses also fall below 99.9% certainty, the FPR collapses to 100%"
[^t6]: arxiv-2512-15068 — "High AUC does not imply safety"
[^t7]: arxiv-2512-15068 — "the learned combiner achieves marginally better AUC (0.83 vs 0.81)"
[^t8]: arxiv-2512-15068 — "Table 1: CRG performance at 95% target coverage"
[^t9]: arxiv-2512-15068 — "Only reasoning-based approaches break the 100% FPR barrier"
[^t10]: arxiv-2512-15068 — "Table 3 shows results on Natural Questions"
[^t11]: arxiv-2512-15068 — "unlikely to close the 0% vs 100% gap"
[^t12]: arxiv-2512-15068 — "where higher values indicate"
[^t13]: arxiv-2512-15068 — "assuming lower scores imply"
[^t14]: arxiv-2512-15068 — "Validity is guaranteed by the exchangeability of the data"
[^t15]: arxiv-2512-15068 — "distribution shift is inevitable as models are updated and user queries evolve"
