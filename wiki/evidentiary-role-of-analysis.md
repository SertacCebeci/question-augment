---
description: "An analysis should state its evidentiary role, primary, supportive, exploratory, descriptive or unsuitable for causal reading, so the same pipeline is not read as stronger than it is."
aliases: ["evidence tier", "evidentiary role", "maturity classification of evidence"]
sources: ["arxiv-2511-19735"]
---
# Evidentiary role of an analysis

The last step of the paper's roadmap is not an estimate. It is a classification of what the estimate may be used for: "A final step should classify the role of the resulting evidence as primary, supportive, exploratory, descriptive,"[^r1] "or unsuitable for causal interpretation."[^r2] The categories are the paper's. The point is that the role is stated explicitly, separately from the number the analysis produces.

The reason given is that one pipeline can serve decisions of very different weight: "the same analytic pipeline may be used for very different" decision contexts, especially in regulatory and industry settings.[^r3] Making the classification explicit "helps prevent overstatement",[^r4] and "keeps the interpretation aligned with the actual strength of the evidence".[^r5]

The mechanism is that the role follows from the design, not from the tool. The paper's cases make this visible. In AI-assisted recruitment, the treatment effect is an efficiency gain with a selected population, so it "should be interpreted as conditional on the enriched mechanism unless transportability to" the intended population can be justified.[^r6] In the randomized trial with an AI-built prognostic covariate, the role "remains primary"[^r7] because the randomization anchors the causal reading, and the AI "improves precision without altering the inferential target".[^r8] The same class of tool gets a different role in each design. A digital twin used as a control stays weaker than the randomized arm it supplements.

The paper also separates three levels of maturity, "currently credible, partially reliable, and unproven",[^r9] and it places the role check last so that it is made after the data-fitness, identification and robustness steps. A role is therefore earned by the earlier steps and cannot be claimed in advance.

What transfers, in my reading: an answer can say which role its evidence plays, for example that a finding is exploratory because it came from one sample, or descriptive because no contrast was estimated. This resembles the point in [[rung-mismatch-in-interpretability-claims]] that an answer should state which rung its evidence reaches. The paper does not discuss answers outside decisions and regulation; the transfer is mine.

## Limits

- The categories are not given with criteria that separate "supportive" from "exploratory". The text describes them in prose and offers no decision rule.
- The text reports no study in which the role check was applied and its effect measured. The applications are argued from the roadmap, as the paper frames itself: "This Perspective is written from that statistical viewpoint."[^r10]
- The role classification concerns causal interpretation. For non-causal claims the text has no equivalent scale.
- A stated role does not make the estimate correct. It caps how the estimate may be read; the upstream steps still decide whether the number is worth reading.

## Related

- [[estimand]] — the quantity whose role is being classified
- [[data-fitness-for-purpose]] — the earlier step whose result sets how far the role can go
- [[common-support-positivity]] — an overlap failure that moves an analysis toward a weaker role
- [[rung-mismatch-in-interpretability-claims]] — the same discipline of matching the strength of a claim to its evidence

[^r1]: arxiv-2511-19735 — "the role of the resulting evidence as primary, supportive, exploratory, descriptive"
[^r2]: arxiv-2511-19735 — "or unsuitable for causal interpretation"
[^r3]: arxiv-2511-19735 — "the same analytic pipeline may be used for very different"
[^r4]: arxiv-2511-19735 — "Making this classification explicit helps prevent overstatement"
[^r5]: arxiv-2511-19735 — "keeps the interpretation aligned with the actual strength of the evidence"
[^r6]: arxiv-2511-19735 — "should be interpreted as conditional on the enriched mechanism unless transportability to"
[^r7]: arxiv-2511-19735 — "role (Step 6) remains primary"
[^r8]: arxiv-2511-19735 — "improves precision without altering the inferential target"
[^r9]: arxiv-2511-19735 — "a maturity classification that distinguishes currently credible, partially reliable, and unproven"
[^r10]: arxiv-2511-19735 — "This Perspective is written from that statistical viewpoint."
