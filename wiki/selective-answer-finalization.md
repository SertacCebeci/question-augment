---
description: "A finalizer that rewrites an answer only for low-risk answer-form errors and abstains on bridge or comparative errors adds a sparse gain when retrieval was already adequate."
aliases: ["risk-controlled answer finalization", "evidence-grounded finalizer"]
sources: ["doi-10-48550-arxiv-2605-05701"]
---
# Selective answer finalization

> After search, revise the answer only when the residual error looks local to answer form; otherwise keep it, because rewriting can damage a correct answer.

## Mechanism

Fang et al. (doi-10-48550-arxiv-2605-05701) observe that a search can find the right evidence and still fail on exactness: yes/no polarity, binary choice, typed slots, alias completion. Unconditional rewriting is risky because it can erase bridge structure or reverse comparative semantics.[^c1] Their finalizer compares the trajectory answer with a refined candidate and accepts the candidate only under low-risk answer-form conditions (yes/no polarity repair, binary-choice repair, typed-slot correction, supported factoid completion). It abstains when bridge ambiguity, comparative semantics or path-level uncertainty remains.[^c2] It adds no new evidence, no tool call and no extra search.[^c3]

## What was measured

Across benchmarks the finalizer's share of total gain was 13.4%, 41.9% and 27.8% on 2WikiMultihopQA, MuSiQue and Bamboogle, as the paper's own accounting of Stage 2.[^c4] Its contribution on MuSiQue is described as weaker in the text, because residual errors there more often involve unresolved bridge structure than a local answer span. The authors conclude it helps mainly when the retrieval path is already adequate.[^c5]

## Limits

- It cannot recover from wrong retrieval paths or unresolved bridge relations.
- The accept set is hand-designed for four QA benchmarks; no test on open-ended answers.
- The share figures above and the text on MuSiQue sit in tension in my reading; I did not resolve which table each comes from.
- That abstaining on uncertain cases transfers to human-facing answering is my inference.

## Related

- [[remaining-budget-penalty-in-action-scoring]] — the search-time half; it supplies most of the gain.
- [[value-of-information]] — the finalizer weighs expected exactness gain against intervention risk, a VOI-like trade.
- [[cost-priced-joint-selection-and-stopping]] — another rule for when further action is not worth taking.

[^c1]: doi-10-48550-arxiv-2605-05701 — "Unconditional answer rewriting can erase bridge"
[^c2]: doi-10-48550-arxiv-2605-05701 — "If the case still contains bridge ambiguity, comparative semantics, or path-level uncertainty, abstain."
[^c3]: doi-10-48550-arxiv-2605-05701 — "It creates no new evidence and launches no additional search or"
[^c4]: doi-10-48550-arxiv-2605-05701 — "accounts for 13.4%, 41.9%, and 27.8% of the total gain on 2WikiMultihopQA, MuSiQue, and Bamboogle."
[^c5]: doi-10-48550-arxiv-2605-05701 — "Stage 2 acts as a sparse exactness layer when the retrieved trajectory is already mostly adequate."
