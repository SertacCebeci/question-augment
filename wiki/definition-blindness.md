---
description: "A system that ignores the supplied criterion can still score high when negatives are mostly easy normals; only evaluation holding frames fixed while varying the criterion exposes it."
aliases: ["definition following", "condition-ignoring detector", "query blindness"]
sources: ["doi-10-48550-arxiv-2607-20780"]
---
# Definition blindness

In open-world video anomaly detection (OWVAD) a user supplies a definition of what counts as anomalous, and the detector should score frames accordingly. The authors call obeying the supplied definition "definition following" and its failure "definition blindness".[^c1] The general point for asking and answering: a system conditioned on a question or criterion can look good on a benchmark while never using it.

## Mechanism

The clear case is a score function that depends only on the video, S(V,z)=a(V) for every z. Such a detector localizes anomalies but cannot change which events score high.[^c2] Standard evaluation (all anomalies positive, normals negative) leaves its AUROC and AP unchanged, so it cannot detect this.[^c3]

Protocols that vary the target class (Drift@5, customizable VAD) still pool normal frames with anomalies excluded by the definition as negatives. For AUROC the score is an exact weighted average: ω times target-versus-normal plus (1−ω) times target-versus-excluded-anomaly, where ω is the share of normals in the negative pool.[^c4] Normals made up 87.9%–96.4% of the pool under Drift@5, so the score is driven mostly by the easy comparison.[^c5] Empirically, a LaGoVAD branch that never receives the definition came within 0.6–1.2 AUROC points of the full model under Drift@5 on XD-Violence and MSAD.[^c6]

## Diagnostic evaluations

Three definition-conditioned measures separate the capabilities. DC-Disc drops normals and asks whether a definition ranks target-anomaly frames above other anomalies. ΔDC-Det holds frames fixed and subtracts the mean score under non-matching definitions from the score under the matching one. ΔDC-Sel does the same for choosing the matching event in multi-event videos.[^c7] A definition-blind detector gets ΔDC-Det of exactly zero whatever its normal-versus-anomaly separation.[^c8] The authors also propose Definition-Contrastive Scoring, which scores the definition relative to competing definitions to remove evidence shared across them, and report gains on all three measures.[^c9]

## Limits

Evidence is from three video benchmarks with single-label class partitions; the transfer to text question answering or clarification is my inference, not tested here. The negative-pool argument depends on normals dominating; where they do not, the masking shrinks. I read only the diagnosis and metric sections, not the full results tables for general vision-language models, so the size of the gap in those systems is not claimed here. DeCoS is one remedy, validated by its authors only.

## Related

- [[task-ambiguity]] — an underspecified criterion is the other side: here the criterion is given but ignored.
- [[underspecbench]] — also probes whether systems respond to what was specified.

[^c1]: doi-10-48550-arxiv-2607-20780 — "We call this behavior definition following, and its failure definition blindness."
[^c2]: doi-10-48550-arxiv-2607-20780 — "Such a detector can localize anomalous events, but cannot adjust which events receive high scores to match the supplied definition."
[^c3]: doi-10-48550-arxiv-2607-20780 — "Its standard VAD AUROC and AP remain unchanged despite its definition blindness."
[^c4]: doi-10-48550-arxiv-2607-20780 — "This evaluation combines separation of target anomalies from normal frames with separation from"
[^c5]: doi-10-48550-arxiv-2607-20780 — "normal frames make up 87.9%–96.4% of the negative set under Drift@5"
[^c6]: doi-10-48550-arxiv-2607-20780 — "Thus, strong Drift@5 performance can coexist with complete definition blindness."
[^c7]: doi-10-48550-arxiv-2607-20780 — "These metrics separate definition following from generic anomaly detection."
[^c8]: doi-10-48550-arxiv-2607-20780 — "A detector satisfying Equation (3) receives zero, regardless of how well it separates anomalous"
[^c9]: doi-10-48550-arxiv-2607-20780 — "DeCoS improves all three definition-conditioned"
