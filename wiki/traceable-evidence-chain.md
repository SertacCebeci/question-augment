---
description: "Tying each claim of an answer to a retrieved source yields an audit trail; in one physician study it rated more transparent than a chain of thought but slower to review."
aliases: ["chain of evidence", "evidence trail", "glass box reasoning", "auditable retrieval trace", "action-level provenance"]
sources: ["doi-10-48550-arxiv-2508-15746", "openalex-org-w7128864259"]
---
# Traceable evidence chain

An agent that answers by acting on a corpus can write its work as a sequence of typed actions: reason, look up a guideline, match a similar case, search the literature, then diagnose. The mechanism that matters is that each retrieval's output goes back into the context before generation continues. The paper's inference loop halts on a tool token, retrieves, and "This feedback is appended to the context" before resuming.[^c1] The final answer is therefore conditioned on a record of which sources it consulted and in what order, and that record can be read against the answer. The authors call it a trail: the system "provides a verifiable trail of medical literature for every claim."[^c2]

The contrast is with the chain of thought of a reasoning model, whose steps are internal and are not tied to sources. The paper compares the two in a physician-in-the-loop study. On reasoning transparency Deep-DxSearch scored above DeepSeek-R1, "in reasoning transparency (4.2 vs. 3.3)," and on clinical utility it scored 4.5 against 3.2.[^c3] The same comparison gives the trail's cost: the system "received lower scores for time efficiency (2.0 vs. 4.0)," which the authors attribute to "the time load required to review the retrieved evidence."[^c4][^c5]

Accuracy was measured in the same study. Across "a validation involving 150 real-world cases," physicians' average accuracy rose "from 45.6% to 69.1%" when the system assisted them.[^c6][^c7] That number bundles the trail with everything else the assistant supplies, so it does not isolate the trail's share.

## What the trail is made of

The retrieved documents do not enter the context raw. A separate model reads them first: the pipeline uses "a dedicated summarization model (Qwen-3-235B) to synthesize the retrieved documents" before the feedback is appended.[^c8] The object a reader audits is therefore a summary of a source, one step removed from the source text. The trail links each claim to a retrieval action, not to a passage in the original document.

The same property is asked for in a search proposal, at the level of each conclusion rather than each action. There, "comparison, or quantitative result should be supported by explicit evidence that can be inspected and validated."[^c12] That is a demand the proposal sets, not a result it reports, and it does not say how a trail would cover a multi-step computation (my reading).

## Limits

- A trail shows what was retrieved and in what order. It does not show that the diagnosis depends on the cited step. The paper's step-level review covers "942 distinct action steps" drawn from 110 sampled cases, rated by three clinicians.[^c9] The passages read grade each step's grounding, not whether the final diagnosis is causally drawn from it. That causal link is not measured in the passages read (my inference from the review's design).
- Absence leaves no link. The authors list "database knowledge gaps" among the causes of error, identified "as a contributing factor to errors."[^c10] A trail records what the corpus returned; a source the corpus never held cannot appear in it (my inference).
- The transparency and time ratings compare one system with one reasoning model, on one rating protocol. The authors argue the cost is acceptable: "we argue this is a necessary trade-off" in high-stakes medicine.[^c11] That is their argument for the trade-off, not a measured result.
- The paper's own accuracy gains are reported for one clinical domain and a text-only corpus; the transfer of the trail to non-clinical answering is not tested in the passages read.

## Related

- [[provenance-gated-assertion]] — caps how strongly a claim may be asserted by how it was obtained; a trail is the record that makes "obtained how" checkable.
- [[grounding-answer-dual-axis-audit]] — crosses evidence localization with answer correctness to catch lucky answers; a trail is the input such an audit needs.
- [[reader-facing-evidence-rendering]] — the same evidence can move a reader's score depending on how it is rendered; a trail is one rendering.
- [[two-tiered-reward-architecture]] — the retrieval actions that build the trail are rewarded inside the same objective as the diagnosis.
- [[premature-closure]] — a trail with no lookup before the diagnose action makes an early commitment visible (my inference).

[^c1]: doi-10-48550-arxiv-2508-15746 — "This feedback is appended to the context"
[^c2]: doi-10-48550-arxiv-2508-15746 — "a verifiable trail of medical literature for every claim"
[^c3]: doi-10-48550-arxiv-2508-15746 — "in reasoning transparency (4.2 vs. 3.3)"
[^c4]: doi-10-48550-arxiv-2508-15746 — "although it received lower scores for time efficiency (2.0 vs. 4.0)"
[^c5]: doi-10-48550-arxiv-2508-15746 — "due to the time load required to review the retrieved evidence"
[^c6]: doi-10-48550-arxiv-2508-15746 — "a validation involving 150 real-world cases"
[^c7]: doi-10-48550-arxiv-2508-15746 — "accuracy from 45.6% to 69.1%"
[^c8]: doi-10-48550-arxiv-2508-15746 — "to synthesize the retrieved documents"
[^c9]: doi-10-48550-arxiv-2508-15746 — "decomposed into 942 distinct action steps"
[^c10]: doi-10-48550-arxiv-2508-15746 — "as a contributing factor to errors"
[^c11]: doi-10-48550-arxiv-2508-15746 — "we argue this is a necessary trade-off"
[^c12]: openalex-org-w7128864259 — "comparison, or quantitative result should be supported by explicit evidence that can be inspected and validated."
