---
description: "Selective conformal risk control abstains on low-confidence inputs, then bounds set-valued error only on the accepted subset; a symmetric selection threshold keeps that subset exchangeable."
aliases: ["SCRC", "selective CRC", "selective conformal classification", "two-stage selective conformal risk control"]
sources: ["arxiv-2512-12844"]
---
# Selective conformal risk control

Conformal risk control (CRC) picks a threshold on exchangeable held-out data so that a loss averaged over future inputs stays under a target level ([[crc-confident-error-control]]). Selective conformal risk control (SCRC) puts a second decision in front of it. The method "abstains on low-confidence inputs and applies" conformal risk control "only to the accepted subset, where compact and informative prediction sets are most valuable."[^c1]

Two thresholds do two jobs. The first, λ1, "controls which examples are accepted for prediction," and the second, λ2, "determines the size of the prediction set for the accepted cases."[^c2] The first stage is a confidence gate; the second stage builds a set-valued answer for whatever passes the gate. The guarantees are therefore selective: they "apply to the accepted subpopulation, while rejected cases are intentionally deferred rather than assigned a possibly" uninformative set.[^c3]

The difficulty is that selection breaks the condition CRC needs. "The act of selection disrupts exchangeability between calibration and test samples."[^c4] Standard CRC sets its threshold from calibration data alone, which is independent of the test point; once the calibration points are filtered by a confidence gate, the kept calibration points are no longer a fair sample of the kept test points. The fix is to make the gate symmetric. The first threshold is computed "the empirical quantile of the feature-dependent loss values over both calibration" and test features, so it does not single out the test point.[^c5] The paper's Lemma 1 gives the condition: "a symmetric selection rule, meaning that for any dataset D," and it states that under it "to preserve exchangeability, the selection rule employed in" the first stage must be symmetric.[^c6] Conditional on the selection event, the accepted subcollection is exchangeable, so "the standard CRC procedure can be applied to this selected subset to estimate" the second threshold.[^c7]

Two variants follow from this. The transductive one, SCRC-T, "preserves exchangeability" and recomputes the gate for every test point.[^c8] The inductive one, SCRC-I, fixes the gate once from calibration data, corrects the selected fraction with a lower confidence bound, and gives a PAC-style guarantee; its analysis "does not require exchangeability after selection."[^c9] The paper reports that the two "deliver nearly identical empirical performance," with SCRC-I "slightly more conservative but substantially more practical for deployment."[^c10]

The first-stage threshold is the smallest one that meets the coverage target, and the paper notes that it "need not minimize the conditional prediction set size."[^c20] The paper therefore searches a grid of gate values for the one with the smallest empirical set size. This search is a practical refinement, and its output "is not covered by Theorem 2."[^c11] Coupling matters here: when both stages come from the same logits, "the two stages are strongly coupled,"[^c19] so admitting more inputs admits harder ones and sets grow. When the gate score is decoupled from the classifier, "the mapping between" the gate and the set size "can become non-monotone, justifying the need to perform a grid search over" the gate.[^c12]

On CIFAR-10 (a "ResNet-18 classifier"[^c21]) and diabetic retinopathy grading (where the authors "train a ResNet-34"[^c22]), both variants reach the target coverage and risk, and "selected samples by these two methods consistently exhibit substantially smaller prediction sets than unselected" ones.[^c13] The choice of confidence score changes size but not validity: the score "primarily affects efficiency" and not "the validity of the selective guarantees themselves."[^c14]

A transfer to asking and answering is my inference, not the paper's claim: a system that answers only above a confidence gate could carry a guarantee on the answers it gives, while refusals stay outside the guarantee.

## Limits

- The guarantee covers the accepted subpopulation only. Rejected inputs get no set-valued guarantee; the paper says "deferred and should be handled by a downstream fallback mechanism such as" human review or a specialist model.[^c15]
- SCRC-T needs exchangeable calibration and test points. The inductive result is stated for i.i.d. calibration: "Proposition 4 (Calibration-only variant). Assume" that the calibration points are i.i.d.[^c16]
- The set-size guarantee is weaker than the validity one. The finite-grid efficiency bound (Theorem 3) assumes i.i.d. data and a grid fixed in advance, and the grid-searched output sits outside Theorem 2.[^c17][^c11]
- The empirical evidence is two benchmarks, each with one network and repeated random splits: "Each experiment is repeated 100 times with random sampling."[^c18] Regression and ranking are named as future directions, "the approach to regression and ranking settings."[^c25] Nothing in the text tests language models; that is my reading.
- The SCRC-I gap is small, and the authors report that "the difference between the two methods is minor and decreases as the" calibration set grows.[^c23] "This conservativeness is more noticeable on smaller" calibration sets, as in the medical data.[^c24] The margin is therefore not a fixed one (my inference).

## Related

- [[conformal-prediction]] — exchangeability is the condition the gate has to keep intact
- [[crc-confident-error-control]] — the CRC threshold this builds on, here applied after a gate
- [[contamination-robust-selective-calibration]] — the other route to selected calibration: there a selector can err and contaminate the set, here the gate is symmetric by construction
- [[abstention]] — the refusal that the first threshold licenses
- [[two-stage-abstention-paradigm]] — abstention as a separate decision after prediction, as in the gate here
- [[mondrian-conformal-prediction]] — stratified calibration, another way to get conditional validity

[^c1]: arxiv-2512-12844 — "SCRC operates in a selective setting: it abstains on low-confidence inputs and applies"
[^c2]: arxiv-2512-12844 — "The first-stage threshold λ1 controls which examples are accepted for prediction, while the second-stage threshold λ2 determines the size of the prediction"
[^c3]: arxiv-2512-12844 — "rejected cases are intentionally deferred rather than assigned a possibly"
[^c4]: arxiv-2512-12844 — "the act of selection disrupts exchangeability between calibration and test samples"
[^c5]: arxiv-2512-12844 — "the empirical quantile of the feature-dependent loss values over both calibration"
[^c6]: arxiv-2512-12844 — "Lemma 1 says that to preserve exchangeability, the selection rule employed in"
[^c7]: arxiv-2512-12844 — "the standard CRC procedure can be applied to this selected subset to estimate"
[^c8]: arxiv-2512-12844 — "transductive method that preserves exchangeability"
[^c9]: arxiv-2512-12844 — "Its analysis does not require exchangeability after selection;"
[^c10]: arxiv-2512-12844 — "is slightly more conservative but substantially more practical for deployment"
[^c11]: arxiv-2512-12844 — "its output is not covered by Theorem 2"
[^c12]: arxiv-2512-12844 — "can become non-monotone, justifying the need to perform a grid search over"
[^c13]: arxiv-2512-12844 — "selected samples by these two methods consistently exhibit substantially smaller prediction sets than unselected"
[^c14]: arxiv-2512-12844 — "rather than the validity of the selective guarantees themselves."
[^c15]: arxiv-2512-12844 — "deferred and should be handled by a downstream fallback mechanism such as"
[^c16]: arxiv-2512-12844 — "Proposition 4 (Calibration-only variant). Assume"
[^c17]: arxiv-2512-12844 — "Theorem 3 (Finite-Grid Selection Efficiency). Assume the calibration sample"
[^c18]: arxiv-2512-12844 — "Each experiment is repeated 100 times with random sampling"
[^c19]: arxiv-2512-12844 — "the two stages are strongly coupled"
[^c20]: arxiv-2512-12844 — "but it need not minimize the conditional prediction"
[^c21]: arxiv-2512-12844 — "A ResNet-18 classifier"
[^c22]: arxiv-2512-12844 — "train a ResNet-34"
[^c23]: arxiv-2512-12844 — "In practice, the difference between the two methods is minor and decreases as the"
[^c24]: arxiv-2512-12844 — "This conservativeness is more noticeable on smaller"
[^c25]: arxiv-2512-12844 — "the approach to regression and ranking settings"
