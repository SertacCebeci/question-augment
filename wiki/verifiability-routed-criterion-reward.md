---
description: "A rubric criterion goes to a deterministic verifier when an extracted value can be checked against a known target, and to a text-only LLM judge otherwise, so one RL reward mixes both."
aliases: ["criterion-level verification", "verifier-tag routing", "extract-then-verify rubric reward", "RLR3 execution routing"]
sources: ["doi-10-48550-arxiv-2605-30244"]
---
# Verifiability-routed criterion reward

Task-level RLVR scores a whole response with one verifier, which works only when the whole task has a checkable answer. The routing idea moves verifiability down to the criterion. A rubric is a list of criteria, and each criterion carries a verifier tag that decides how it is scored. If the content can be pulled out of the response and compared with a known target, a text-only LLM acts as an extractor that returns a value and some reasoning, and a deterministic function computes the score from that value. Otherwise a text-only LLM judge assigns a discrete credit, 0, 0.5 or 1, against a textual reference. The paper's wording is that fuzzy criteria are those that "cannot be reduced to deterministic matching."[^c1]

For the extractor path the paper states the design rule as "check a value extracted from the response, not a judgment produced by the extractor."[^c2] The verifier should never receive a yes/no judgment the extractor has already made, because then the deterministic check would only certify the extractor's judgment. The rubric generator sees only the verifier tags allowed for the task, which the authors say "prevents the rubric generator from abusing verifiers."[^c3]

The scheme nests RLVR. "When every criterion is verifiable, RLR3 reduces to standard RLVR."[^c4] The mixed case is therefore a single GRPO loop over rewards that differ only in which path scores each criterion, not two training stages.

What the routing buys is measured in one place: an audit of the reward model that executes the rubric (the GenRM). On constructed abnormal responses, the row without the deterministic verifier shows higher false positives on no-final-answer responses, "raises FPRs on no-final-answer responses (15.1% vs. 11.5%)."[^c5] The authors' reason for caring is that such errors do not stay put: "exploitable false positives can be repeatedly reinforced" once they become reward in online training.[^c6] Regular-response accuracy barely moves (95.3% without the verifier, 95.0% with it), so the gain is in what the reward refuses to credit, not in what it gets right.

## Limits

- The audit uses 1,000 constructed abnormal responses, built from the GenRM test set. The text says "we keep their regular responses and construct 1,000 abnormal responses across four categories."[^c7] The false-positive gaps are small, which the authors themselves flag: "Although the absolute gaps are modest."[^c8] One base model family (Qwen3-VL-30B-A3B) was used.
- The text I read does not say what replaces the verifier in the "w/o Verifier" row. I take it to be the model's own judgment on the same criteria (my inference), so the row shows the value of a deterministic check against a model check, not against any other scorer.
- The 1 to 2 point macro-average gains reported over RLVR come from the full method, which also includes score remapping, gating and the RLVR-trained GenRM. The routing's own share of those gains is not isolated in the text I read.
- The routing can only be as faithful as the extraction step. A verifier checks whatever the extractor pulled out; if the extractor misreads the response, the deterministic check is exact on the wrong value (my inference).
- The rubrics come from frontier models outside the optimization loop, and the authors say "rubric quality can become a bottleneck."[^c9]

## Related

- [[minimal-exposure-grading]] — the information restriction that accompanies this routing; what the extractor and judge are kept from seeing.
- [[extractive-abstractive-verifiability-tradeoff]] — the same verifiability axis, seen from cited answers: checkable spans against fluent abstraction.
- [[expert-report-derived-atomic-rubrics]] — atomic rubric items that a judge checks Y/N; the criteria this routing would send to a verifier when they are deterministic.
- [[pessimistic-min-judge-aggregation]] — what to do when several judges score the fuzzy path and disagree.
- essential-gated-reward-aggregation — how the routed criterion scores are combined into one reward.

[^c1]: doi-10-48550-arxiv-2605-30244 — "cannot be reduced to deterministic matching"
[^c2]: doi-10-48550-arxiv-2605-30244 — "check a value extracted from the response, not a judgment produced by the extractor"
[^c3]: doi-10-48550-arxiv-2605-30244 — "This restriction prevents the rubric generator from abusing verifiers."
[^c4]: doi-10-48550-arxiv-2605-30244 — "When every criterion is verifiable, RLR3 reduces to standard RLVR"
[^c5]: doi-10-48550-arxiv-2605-30244 — "raises FPRs on no-final-answer responses (15.1% vs. 11.5%)"
[^c6]: doi-10-48550-arxiv-2605-30244 — "exploitable false positives can be repeatedly reinforced"
[^c7]: doi-10-48550-arxiv-2605-30244 — "we keep their regular responses and construct 1,000 abnormal responses across four categories"
[^c8]: doi-10-48550-arxiv-2605-30244 — "Although the absolute gaps are modest"
[^c9]: doi-10-48550-arxiv-2605-30244 — "rubric quality can become a bottleneck"
