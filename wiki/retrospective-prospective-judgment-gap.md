---
description: "AI voters match human experts far more on retrospective breakthroughs than on prospective questions (JS distance 0.209 vs 0.352 in Stage 2); the paper ties this to ground truth."
aliases: ["retrospective versus prospective alignment gap", "backward-looking versus forward-looking judgment gap"]
sources: ["arxiv-2602-03849"]
---
# Retrospective–prospective judgment gap

When simulated-AI and human panels rank the same candidate items, how closely the two rankings agree can depend on the temporal direction of the item. Zhao, Xu, Li and Liu compare two candidate lists built from the same literature: "breakthroughs" of 2025, which describe something already achieved, and "questions" for 2026, which describe something still open. Agreement is measured as the Jensen–Shannon distance between the human and the AI vote distributions, and at the second, expert stage the distance is clearly smaller for breakthroughs: "in Stage 2 (0.209 vs. 0.352)".[^c1]

The authors' explanation is about ground truth. Breakthroughs are "grounded in retrospective facts and verifiable impacts", which gives them "a stronger objective ground truth that facilitates consensus".[^c2] Questions are "prospective and speculative, involving subjective assessments of future value and feasibility".[^c3] On this reading the AI judge is not short of a capacity to read a candidate; it lacks a fixed target that the human panel also converges on, so the two distributions have less to agree about. The two sides also weight different things: human experts put "a higher premium" on pragmatic, meta-level infrastructure such as evaluation standards, and the AI voters put more weight on theoretical capability.[^c4]

The gap is not fixed by item class. The same breakthrough list moves from 0.394 at Stage 1 to 0.209 at Stage 2 when the simulated voters are raised from graduate to professor level, and the authors read this as the professor-level agents being "more effective at capturing the nuanced criteria" that experts use.[^c5] So the agreement depends both on what is being judged and on how the simulated panel is built. What transfers is the design move: measure AI–human agreement separately for items with and without a checkable outcome, and do not read one aggregate agreement number as a property of the judge.

## Limits

- The Stage 1 numbers reverse the paper's own summary. Table 4 gives 0.394 for breakthroughs and 0.370 for questions at Stage 1, so breakthroughs are the less aligned category there. The claim that the breakthrough distance is "consistently lower" holds only at Stage 2.[^c6]
- One application: two lists, five fields, one run, one distance value per cell and no interval. Nothing here says how stable the 0.209 and 0.352 are across seeds or prompts.
- No human–human baseline is reported. How far two independent human panels diverge on the same list is not given, so 0.352 cannot be called "far" from human agreement on its own. (my reading)
- The ground-truth account is the authors' explanation and is not tested. No run holds the judges fixed and varies only how checkable the items are.
- The "AI voters" are personas generated to "match this expertise", not independent judges.[^c8] The gap measures those personas against the human panel, not AI judges in general.
- The paper says the questions are judged with "higher variance in opinion" among humans as well,[^c7] which means part of the gap may be the humans' own disagreement. The text does not separate the two.

## Related

- [[candidate-selection-gap]] — a selector's pick against the best a pool could give; here the question is narrower, which candidates a judge can agree with humans on at all.
- [[cross-provider-judge-ensemble]] — pooling judges to get a better signal; the retrospective–prospective split asks where any judge, pooled or not, is anchored to something outside itself.
- [[expert-weighted-stage-voting]] — the staged panel in which these AI and human votes are combined.

[^c1]: arxiv-2602-03849 — "in Stage 2 (0.209 vs. 0.352)"
[^c2]: arxiv-2602-03849 — "grounded in retrospective facts and verifiable impacts"
[^c3]: arxiv-2602-03849 — "involving subjective assessments of future value and feasibility"
[^c4]: arxiv-2602-03849 — "human experts placing a higher premium"
[^c5]: arxiv-2602-03849 — "AI agents are more effective at capturing the nuanced criteria"
[^c6]: arxiv-2602-03849 — "with the most significant improvement observed in the Breakthrough list (decreasing"
[^c7]: arxiv-2602-03849 — "there is likely higher variance in opinion regarding future directions"
[^c8]: arxiv-2602-03849 — "agents simulated to match this expertise"
