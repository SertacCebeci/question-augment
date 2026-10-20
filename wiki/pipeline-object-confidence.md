---
description: "A RAG run has three objects, the answer, the evidence and the retrieval state; one confidence score conflates them, while the three logged views carry weakly correlated signal."
aliases: ["answer, evidence and retrieval-state decomposition", "three-family analysis frame", "object-specific confidence in RAG"]
sources: ["doi-10-48550-arxiv-2606-22728"]
---
# Pipeline-object confidence

A retrieval-augmented pipeline produces more than an answer. It also produces the evidence it assembled and, for a graph-based retriever, the retrieval state it walked. A confidence score that is computed over the answer alone is a score about one of three objects, and it is silent about the other two. The paper's frame separates them: "We use three families because a KG-RAG run exposes three different objects: the answer, the assembled evidence, and the retrieval state."[^c1]

The three are not stacked as one quantity. The paper writes the run as a chain in which each object is conditioned on the ones before it: the retrieval state given the question, the evidence given the question and the state, and the answer given all three.[^c2] In the paper's words, "they are three logged views of the same KG-RAG run: generated text, retrieved evidence, and symbolic retrieval state."[^c3] The diagnostic question differs by object. For the answer, the question is "do repeated generations agree, or has the answer surface become artificially stable?"[^c4] For the evidence and the retrieval state, the question is whether the assembled support and the route entail the answer, and whether the route is empty or wrong.

The reason to keep them apart is measured, not argued. The paper's representative scores for the answer-state and the evidence-state are weakly correlated across its pooled runs, "so they carry complementary signal."[^c5] The practical consequence is that a case can be silent on one object and loud on another. On the lock-in cases, answer-state agreement is silent while "evidence- and retrieval-state checks still flag" most of the errors.[^c6] So the question a single score cannot ask, which part of the pipeline to distrust, becomes a question with an answer once the objects are logged separately. The paper's summary is "Confidence in RAG is object-specific."[^c7]

The paper also reports what a rule over the three objects does, as a measurement on its own runs. Accepting an answer only when the answer, evidence and retrieval checks all mark it low-risk gives "91.9% pooled precision at 7.7% coverage," against a 69.7% accept-all rate.[^c8] This is a result about one system and six snapshots, not a procedure to adopt; the note records the numbers and their cost, not a recommendation.

## Limits

The cost is coverage. The rule "certifies only 7.7% of answers as low-risk," so the precision is bought by abstaining on most answers.[^c9] The paper reports the same rule at "81.6% out-of-calibration," which is lower than the in-sample figure.[^c10] The paper's clinical result of 100% precision is, in its own words, an in-domain automated-label bound: "not a clinical safety claim, and still needs human" validation.[^c11]

The decomposition is not a claim that KG-RAG is more accurate. The paper says "We do not claim KG-RAG" is more accurate than dense retrieval; it finds no detectable accuracy gap, and its interest is in the failure states the answer-only view cannot see.[^c12] The dispersion score the paper builds inside the answer-state family is described as "rather than a central claim."[^c13]

The three checks do not carry equal weight across lock-in variants. The paper says: "Which signal survives depends on the variant."[^c14] For absence the route or abstention observable is the reliable flag, and for presence the evidence-level checks work only "checks, imperfectly, for presence."[^c15]

Not tested here: whether the same three objects and the same chain hold for a dense pipeline with no graph, and whether the thresholds that define "low-risk" transfer to another corpus. My inference is that the thresholds are fitted to these snapshots, since the paper's claims are scoped to them, but the paper's text does not state a transfer test.

## Related

- [[retrieval-state-lock-in]] — the failure that the evidence and retrieval checks are needed to see; in lock-in the answer-state signal is silent by construction.
- [[uncertainty-decomposition]] — a different split: the agent's uncertainty by type (aleatoric, epistemic, specification), not by the objects a pipeline logs. The two axes can be used together but are not the same.

[^c1]: doi-10-48550-arxiv-2606-22728 — "We use three families because a KG-RAG run exposes three"
[^c2]: doi-10-48550-arxiv-2606-22728 — "The three families are not independent predictors of correctness"
[^c3]: doi-10-48550-arxiv-2606-22728 — "three logged views of the same KG-RAG run"
[^c4]: doi-10-48550-arxiv-2606-22728 — "agree, or has the answer surface become artificially stable?"
[^c5]: doi-10-48550-arxiv-2606-22728 — "so they carry complementary signal"
[^c6]: doi-10-48550-arxiv-2606-22728 — "while evidence- and retrieval-state checks still flag"
[^c7]: doi-10-48550-arxiv-2606-22728 — "Confidence in RAG is object-specific"
[^c8]: doi-10-48550-arxiv-2606-22728 — "reaches 91.9% pooled precision at 7.7% coverage"
[^c9]: doi-10-48550-arxiv-2606-22728 — "it certifies only 7.7% of answers as low-risk"
[^c10]: doi-10-48550-arxiv-2606-22728 — "81.6% out-of-calibration"
[^c11]: doi-10-48550-arxiv-2606-22728 — "not a clinical safety claim, and still needs human"
[^c12]: doi-10-48550-arxiv-2606-22728 — "We do not claim KG-RAG"
[^c13]: doi-10-48550-arxiv-2606-22728 — "rather than a central claim"
[^c14]: doi-10-48550-arxiv-2606-22728 — "Which signal survives depends on the variant"
[^c15]: doi-10-48550-arxiv-2606-22728 — "checks, imperfectly, for presence"
