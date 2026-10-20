---
description: "Showing an agent its used and remaining tool-call budget at each step lets it use more calls before stopping, lifting accuracy at equal budget where the plain agent saturates."
aliases: ["budget tracker", "budget awareness", "remaining-budget signal", "budget-aware tool use"]
sources: ["arxiv-2511-17006"]
---
# Budget awareness signal

An agent that acts through tools has a cap on how many calls it may make, but the cap is not part of what it sees while it works. The paper's diagnosis is that "standard agents lack inherent budget awareness"[^b1], and that without an explicit signal they stop early, "saturating their capabilities regardless of extra budget allocated."[^b2]

The proposed fix is a status block, not a new policy. At the first step the agent gets a short guideline on the budget regimes; after that, "it appends a budget status block showing the remaining" and used counts for each tool.[^b3] The block is inserted after every tool response, and no training is involved. The authors state the premise as a hypothesis: "providing explicit budget signals enables the model to internalize resource constraints."[^b4] What is shown is that the displayed count changes behaviour; whether the model represents the budget internally is not shown.

On BrowseComp with Gemini-2.5-Pro, plain ReAct "saturates at a budget of 100 on BrowseComp",[^b5] with the agent "terminating prematurely because it believes it has" a sufficient answer or is stuck, while the context window is not full.[^b6] With the signal the curve keeps rising as the budget grows, which the authors attribute to "explicitly surfacing remaining resources."[^b7]

Across three models and three information-seeking benchmarks, the tracker gives "consistent accuracy gains" at the same budget.[^b8] The stronger practical claim is about cost: with the signal, a budget of 10 gives "comparable accuracy with less budget (10 vs. 100)",[^b9] and the average cost per question falls, "reducing overall cost by 31.3%."[^b10] The signal is placed on tool calls rather than tokens because "pre-determining an accurate token budget for multi-step agentic tasks is often impractical."[^b11] The budget therefore caps calls, and the cost of the run is measured separately (see unified-token-tool-cost).

## Limits

- The ceiling result is one model (Gemini-2.5-Pro) on one benchmark. The accuracy table covers three models, but the ceiling plot is for one of them.
- The accuracy gains are small against the reported spreads in some rows: Gemini-2.5-Pro goes from 12.6±1.2 to 14.6±1.2 on BrowseComp. The results "are averaged over 3 independent runs."[^b12] With three runs, the text read does not establish that the gains exceed run-to-run noise.
- The signal shows counts, not value. Nothing in the text read compares it with a signal that reports the expected gain of a further call; that comparison is my inference as a gap, not a tested result.
- Only search and browse tools were tested, on information-seeking tasks. A conversational benchmark is in the appendix, not in the main results.
- The stopping mechanism named (believing the answer is sufficient, or being stuck) is the authors' reading of the failure, not a measured breakdown of stop decisions.

## Related

- [[stop-continue-criteria-in-retrieval-loops]] — retrieval loops there stop at a fixed hop, token or latency budget; this is the case where the budget is visible and the agent still stops early.
- [[test-time-scaling]] — the tool-call budget is a scaling axis, and this signal is what lets that axis keep scaling.
- [[turn-efficiency-of-questioning]] — a fixed turn budget judged by trajectory; the same kind of resource, seen from the asker's side.
- [[resource-rationality]] — the cost reading of effort; this note adds the agent's knowledge of its own remaining allowance.

[^b1]: arxiv-2511-17006 — "standard agents lack inherent budget awareness"
[^b2]: arxiv-2511-17006 — "saturating their capabilities regardless of extra budget allocated"
[^b3]: arxiv-2511-17006 — "it appends a budget status block showing the remaining"
[^b4]: arxiv-2511-17006 — "providing explicit budget signals enables the model to internalize resource constraints"
[^b5]: arxiv-2511-17006 — "ReAct saturates at a budget of 100 on BrowseComp"
[^b6]: arxiv-2511-17006 — "terminating prematurely because it believes it has"
[^b7]: arxiv-2511-17006 — "explicitly surfacing remaining resources"
[^b8]: arxiv-2511-17006 — "consistent accuracy gains with Budget Tracker integration across different"
[^b9]: arxiv-2511-17006 — "Budget Tracker achieves comparable accuracy with less budget (10 vs. 100)"
[^b10]: arxiv-2511-17006 — "reducing overall cost by 31.3%"
[^b11]: arxiv-2511-17006 — "pre-determining an accurate token budget for multi-step agentic tasks is often impractical"
[^b12]: arxiv-2511-17006 — "The results are averaged over 3 independent runs"
