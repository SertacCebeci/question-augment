---
description: "Rolling per-claim confidences into one response confidence: a product assumes independent claim errors, an assumption the paper finds violated; a minimum tracks the most fault-prone step."
aliases: ["product aggregation", "minimum aggregation", "claim-to-response confidence aggregation"]
sources: ["arxiv-2512-19920", "doi-10-11591-ijai-v15-i4-pp3144-3153", "arxiv-2512-05809"]
---
# Claim-confidence aggregation

A response can be flagged claim by claim: a model writes a complete answer, gives each step its own confidence, and the interface highlights the steps it doubts. Wu et al. choose this over replacing an uncertain step with a refusal token, because "Directly replacing an individual claim with a special token <IDK> often produces an incohesive response."[^c1] They keep the whole response and "output the complete response while signifying abstention behavior by visually highlighting the uncertain claim in the user interface."[^c2]

The training problem is that claim-level correctness is not labelled. "Explicit correctness annotations for the individual claims are absent," so the paper trains on the final outcome only and must turn the per-claim scores into one response-level number: "Since only the final outcome is annotated, we must aggregate the claim-level confidence scores into an overall response confidence."[^c3] That aggregated number is then trained with the Brier-type reward used at response level.[^c4]

Two aggregations are compared. The product takes p = the product of the claim confidences. It is the natural rule if the response is correct exactly when every claim is, and the claims are independent: "This method is predicated on two assumptions," namely that the claims' correctness events are independent and "the final outcome is correct if and only if all claims are correct."[^c5][^c6] The minimum takes p = the smallest claim confidence, so that the response is only as confident as its most uncertain step.[^c7]

The paper's worked example shows why the choice matters. A ten-step incorrect response with a uniform claim-level confidence of 80 percent, which is over-confident, gives a product of about 11 percent, "which is closer to a calibrated value."[^c8] The minimum reaches the same response-level number only if the most uncertain claim sits at 11 percent, so the minimum "incentivizes the model to allocate low confidence to the most fault-prone step."[^c9]

The paper finds the independence assumption fails in practice. "Empirically, we find that the independence assumption is frequently violated, as confidence estimates across different steps of the same response tend to be highly correlated." The consequence it draws is that the claim-level confidence under the product "is often over-confident," even when the response-level number is calibrated.[^c10][^c11]

The same all-or-nothing rule appears where there are no confidences at all. A Vietnamese social-news pipeline labels a post from its claim verdicts alone: "a social news article is marked verified only if all its check-worthy claims are true."[^c16] The authors call it strict and justify it by the asymmetry of errors: "This conjunctive rule makes sense because one false assertion is"[^c17] enough to mark the item unreliable. Their rule is the product's "all claims correct" condition with binary verdicts in place of confidences. My inference, not the paper's: it therefore inherits the same question about whether claim errors are independent, and the paper does not test that. The paper also reports no comparison with a graded aggregation of the same verdicts.

A third rule weighs claims by how many are supported and how sure the verifier is. In the world-model verifier ViSA, each imagined frame gets micro-claims, and each claim is checked against that frame with a verdict of ENTAILED, CONTRADICTED or INSUFFICIENT and a confidence. The frame's evidence quality score is built so that "By balancing coverage (how many claims are entailed) with certainty (how confidently they are verified), EQ rewards" frames with many verifiable claims and strong verifier confidence.[^c18] The authors call it "soft ensemble over multiple localized evidential checks within each frame" and give averaging as the reason: "averaging across multiple claims helps us stabilize the overall reliability of frame-level informativeness."[^c19][^c20] My inference: because the coverage term is a share of entailed claims, the rule is closer to a share than to the product over all claims. The extracted formula does not show cleanly how its two parts combine, so this is not confirmed.

## Limits

The 80-percent, ten-step case is an illustration, and the correlation finding is stated qualitatively in the parts read. I did not read the claim-level result tables, so how far the product's over-confidence shows up in the measured numbers is not established here.

Claim validity is set by an LLM judge, since the claims carry no human annotation, so the aggregation is only as good as that judge at the claim grain.[^c12]

The paper deliberately disregards intermediate reasoning steps: "we disregard the intermediate COT steps and focus on" the abstention behavior of the final solution.[^c13] So the aggregated score is over the answer's own claims; whether a reasoning trace's intermediate steps need their own confidence is not answered here. The paper's intermediate-step calibration is claimed through "weak supervision from the final outcome," which I did not verify in the results.[^c14]

The minimum is motivated by the fault-prone-step argument, not by a test that it is better calibrated than the product. Neither aggregation is shown to be the right one for a response with a single fault versus many, beyond the example.

The experiments read here are reasoning tasks. The paper describes its scope as "domain-specific reasoning tasks and open-domain QA," but the claim-level aggregation has not been shown on open-domain answers, where the notion of a discrete claim is looser.[^c15]

The evidence quality score is tested only as a reward for choosing world-model views, with one backbone, and the same paper reports that on MMSI-Bench "including ours, achieve consistent scaling" fails for every verifier.[^c21] So the aggregation's value is shown on one benchmark, and it is not shown to be the right rule for claim-verdict scoring in general.

## Related

- [[decoupled-claim-calibration-training]] — trains claim-level confidence by DPO on corrected pairs; the aggregation question here sits upstream of how claim scores are used.
- [[supported-faithfulness-score]] — scores a response by the mean fraction of its atomic claims that are supported; a different aggregation over per-claim verdicts, a mean rather than a product or a minimum.
- [[risk-averaged-abstention-reward]] — the Brier-type reward the aggregated confidence is trained with.

[^c1]: arxiv-2512-19920 — "often produces an incohesive response."
[^c2]: arxiv-2512-19920 — "output the complete response while signifying abstention behavior by visually highlighting the uncertain"
[^c3]: arxiv-2512-19920 — "Since only the final outcome is annotated, we must aggregate the claim-level confidence scores into an overall"
[^c4]: arxiv-2512-19920 — "post-trained using the Brier score reward function as defined in Equation (3)."
[^c5]: arxiv-2512-19920 — "This method is predicated on two assumptions"
[^c6]: arxiv-2512-19920 — "correct if and only if all claims are correct."
[^c7]: arxiv-2512-19920 — "Therefore, minimum"
[^c8]: arxiv-2512-19920 — "confidence of 11%, which is closer to a calibrated value."
[^c9]: arxiv-2512-19920 — "aggregation incentivizes the model to allocate low confidence to the most fault-prone step."
[^c10]: arxiv-2512-19920 — "estimates across different steps of the same response tend to be highly correlated"
[^c11]: arxiv-2512-19920 — "the claim-level confidence is often over-confident."
[^c12]: arxiv-2512-19920 — "which is determined by an LLM Judge"
[^c13]: arxiv-2512-19920 — "we disregard the intermediate COT steps and focus on"
[^c14]: arxiv-2512-19920 — "weak supervision from the final"
[^c15]: arxiv-2512-19920 — "on both domain-specific reasoning tasks and open-domain QA"
[^c16]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "a social news article is marked verified only if all its check-worthy claims are true"
[^c17]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "This conjunctive rule makes sense because one false assertion is"
[^c18]: arxiv-2512-05809 — "By balancing coverage (how many claims are entailed) with certainty (how confidently they are verified), EQ rewards"
[^c19]: arxiv-2512-05809 — "averaging across multiple claims helps us stabilize the overall reliability of frame-level informativeness"
[^c20]: arxiv-2512-05809 — "soft ensemble over multiple localized evidential checks within each frame"
[^c21]: arxiv-2512-05809 — "including ours, achieve consistent scaling"
