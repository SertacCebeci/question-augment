---
description: "Cross-domain personalization is limited by integrating evidence from several behavior domains: extra domains help only models that can combine them, and some hurt weaker ones."
aliases: ["cross-domain behavioral personalization", "multi-domain evidence integration", "cross-domain personalization"]
sources: ["doi-10-48550-arxiv-2608-05246"]
---
# Cross-domain evidence integration

A query is cross-domain when the behavioral records that could personalize its answer fall in two or more domains: the set of relevant domains has size at least two.[^c1] Personalizing such a query means finding the few relevant records in a long multi-domain log, ignoring the rest, and combining evidence from different domains into one answer. LUNAR builds this setting from 150 users, each with a 12-week history over four domains (clothing, food, housing, mobility), and 188 of its 300 queries need at least two domains.[^c2]

The benchmark separates two things that are easy to run together: whether the model is given the right records, and whether it can use records from several domains at once. The first is tested by comparing Full Context (the whole log) with Curated Context (only the query-relevant evidence, as an oracle). Curated Context "consistently outperforms Full Context, indicating that models struggle to retrieve relevant evidence in noisy behavioral histories."[^c3] Even then, scores "still range from 2.41 to 4.07 even though all models receive the same filtered evidence," so the authors read the remaining gap as reasoning over evidence: "Cross-domain information integration is the true bottleneck beyond retrieval."[^c4]

The second is tested by removing domains. On multi-domain queries, the authors compare Full-E (evidence from every relevant domain) with Single-E (evidence from one randomly sampled relevant domain), over seven models. Reducing Full-E to Single-E "lowers performance for every model, with drops ranging from 0.39 for Qwen3-0.6B to 1.03 for Kimi-K2.6."[^c5] The two ends behave differently. Strong models score above their own single-domain baselines with full evidence, but once evidence is cut to one domain, their scores "fall below some single-domain baselines."[^c6] Weak models have the opposite pattern: the smallest model scores lower on multi-domain queries with full evidence than on single-domain ones (2.32 vs. 2.56), so "additional domains serve as noise rather than supplementation for them."[^c7] The authors' summary: "the value of cross-domain evidence is not intrinsic but is critically contingent upon the model’s information integration capability in cross-domain scenarios."[^c8]

A third test adds evidence one record at a time, on 58 multi-domain queries with exactly four records. "All models improve monotonically with more evidence, but gain patterns diverge sharply by capability tier."[^c9] Top-tier models show "classic diminishing returns", with the first record giving the largest gain. Mid-tier models have unstable trajectories, and the weakest model's curve is nearly flat.

So the mechanism the work supports is this: a model gains from a second domain only if it can hold both in view and weigh them against each other. Retrieval of the right records is a separate difficulty, and it is the easier one in the authors' data.

## Limits

- The ablations cover a subset of the work: seven models for Full-E versus Single-E, and one 58-query scaling set. The 19-model results are for Full Context and Curated Context, not for the ablations.
- The logs are synthetic. The authors measure distributional fidelity against real behavior with a Jensen–Shannon divergence and report that anchoring lowers it, but the cross-domain structure that the integration tests depend on was produced by the same pipeline. Whether the same integration gap appears in real multi-domain histories is not tested.
- Relevance is itself a judgment: domains are kept when they "can improve the response", using a generic answer as the baseline, so the domain set that defines "cross-domain" comes from an LLM analysis before any scoring.[^c10]
- Scoring is an LLM judge comparing a personalized response against a generic one on a 1–5 scale. Human–LLM exact agreement on personalization was 76.6%, on a subset.[^c11]
- The work locates a bottleneck; it does not test an intervention that improves integration. Any claim about how to train or prompt for it goes beyond this text.

## Related

- [[same-user-history-gating]] — a gate that decides whether stored history settles a request before any of it is used; the same problem of choosing evidence first, in a coding setting.
- [[compressed-memory-versus-raw-retrieval]] — how the evidence reaches the model: raw records versus atomic facts, with the gap sensitive to model scale.
- [[personalization-privacy-tradeoff]] — the same cross-domain evidence that lifts personalization is what a privacy judge penalizes when a response over-discloses.

[^c1]: doi-10-48550-arxiv-2608-05246 — "We define a query as cross-domain when"
[^c2]: doi-10-48550-arxiv-2608-05246 — "LUNAR comprises 150 users and 300 evaluation queries, with each user associated with a 12-week behavioral history"
[^c3]: doi-10-48550-arxiv-2608-05246 — "Curated Context consistently outperforms Full Context, indicating that models struggle to retrieve relevant evidence in noisy behavioral histories"
[^c4]: doi-10-48550-arxiv-2608-05246 — "Cross-domain information integration is the true bottleneck beyond retrieval"
[^c5]: doi-10-48550-arxiv-2608-05246 — "reducing Full-E to Single-E lowers performance for every model, with drops ranging from 0.39 for Qwen3-0.6B to 1.03 for Kimi-K2.6"
[^c6]: doi-10-48550-arxiv-2608-05246 — "once evidence is reduced to Single-E, their scores not only plummet but even fall below some single-domain baselines"
[^c7]: doi-10-48550-arxiv-2608-05246 — "additional domains serve as noise rather than supplementation for them"
[^c8]: doi-10-48550-arxiv-2608-05246 — "the value of cross-domain evidence is not intrinsic but is critically contingent upon the model’s information integration capability in cross-domain scenarios"
[^c9]: doi-10-48550-arxiv-2608-05246 — "All models improve monotonically with more evidence, but gain patterns diverge sharply by capability tier"
[^c10]: doi-10-48550-arxiv-2608-05246 — "Domains that can improve the response are retained for evidence grounding, while irrelevant domains are discarded"
[^c11]: doi-10-48550-arxiv-2608-05246 — "agreement reaches 76.6%, and 71.1% for personalization score (avg.) and privacy protection score, respectively"
