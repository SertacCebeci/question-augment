---
description: "Feedback adaptation is scored on two axes, correction lag and post-feedback performance on paraphrased related queries; retraining trades one for the other, inference-time stored patches did not."
aliases: ["feedback adaptation", "correction lag", "post-feedback performance", "PatchRAG"]
sources: ["openalex-org-w7153670862"]
---
# Feedback adaptation metrics

A deployed retrieval-augmented system is corrected by users or experts, yet it is usually scored on static overall accuracy. The work poses a separate question: once corrected, "how effectively and how quickly does this correction propagate to future queries?"[^c1] It is not about average accuracy but about the dynamics of knowledge updates under interaction.

## Two axes

**Correction lag** is the elapsed time from feedback at time t until the system consistently produces corrected outputs for semantically consistent queries. Retraining, fine-tuning or redeployment necessarily incur lag whatever final accuracy results, so lag is orthogonal to accuracy: two systems with identical post-update performance can differ in how long they keep answering wrongly.[^c2]

**Post-feedback performance** is accuracy on queries semantically consistent with earlier feedback, measured after the feedback is incorporated. A system that memorizes the feedback instance without generalizing to related queries scores low.[^c3] Feedback adaptation therefore requires generalizing the correction across surface forms, not memorizing it.[^c4]

## The reference instantiation

PatchRAG stores each feedback item as (query, corrected answer, evidence) and scores it against a new query by a mix of query similarity and evidence similarity (Eq. 1, weight lambda). Retrieved items are placed into the prompt as in-context examples, with no gradient update, so feedback acts as soon as it enters memory.[^c5]

## What was measured

Expert feedback was injected as paraphrases of the evaluation queries with minimal lexical overlap, to block keyword matching. On three QA benchmarks PatchRAG reached an average post-feedback score of 62.3, above training baselines such as Golden-only and RAFT, with the largest gain, 9.7 on average.[^c6] Training baselines showed a trade-off: cutting update steps to shorten lag sharply degraded post-feedback performance, while PatchRAG avoided it.[^c7] A stress test corrupted the feedback (top-1 retrieved evidence instead of gold, noisy, blank, vague or conflicting answers); performance decreased gradually as noise grew.[^c8]

## Limits

- Evaluation is a snapshot before and after one injection, chosen to avoid memory drift and query-distribution change; the online process, with many accumulating corrections, is not measured.[^c9]
- Lag is argued structurally for training methods; the work does not give a calibrated time unit, and my reading is that "lag" here mostly contrasts update-step budgets with zero.
- Pre-t feedback was synthetic, and feedback paraphrases were constructed, so real user feedback may be less cleanly intent-aligned.
- PatchRAG is described as intentionally minimal, not a final solution; the claim concerns the metrics' ability to separate systems, not that stored patches are optimal.
- Only QA benchmarks (NQ, TriviaQA, HotpotQA) were used.

## Related

- [[detection-correction-gap]] — noticing an error differs from changing behavior afterwards; this note measures the latter's speed and reach.
- [[stage-specific-elicitation]] — another work on where user feedback enters a system.
- [[feedback-driven-socratic-convergence]] — feedback driving behavior change over weeks, versus per-correction lag here.

[^c1]: openalex-org-w7153670862 — "once a system is corrected, how effectively and how quickly does this correction propagate to future queries?"
[^c2]: openalex-org-w7153670862 — "Correction lag is therefore orthogonal to accuracy: two systems may achieve identical post-update performance"
[^c3]: openalex-org-w7153670862 — "A system that simply memorizes the feedback instance without generalizing to related queries may exhibit low post-feedback performance."
[^c4]: openalex-org-w7153670862 — "feedback adaptation does not require memorizing the exact feedback instance."
[^c5]: openalex-org-w7153670862 — "This approach allows the generator to immediately condition its predictions on the newly provided feedback without any gradient-based updates"
[^c6]: openalex-org-w7153670862 — "PatchRAG exhibits the largest post-feedback performance gain, with an average improvement of 9.7."
[^c7]: openalex-org-w7153670862 — "training-based methods (e.g., RAFT) exhibit a fundamental trade-off"
[^c8]: openalex-org-w7153670862 — "storing both correct and incorrect feedback for the same intent (Conflict)"
[^c9]: openalex-org-w7153670862 — "we employ a snapshot-based evaluation protocol to isolate the marginal effect of feedback injection."
