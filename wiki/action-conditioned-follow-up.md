---
description: "A follow-up whose correct answer depends on the answerer's own earlier choice needs one key per branch, and scoring it jointly with that choice exposes errors single-stage accuracy hides."
aliases: ["two-stage action-induced reasoning", "stage-conditioned follow-up", "joint stage correctness", "decision-conditioned question", "branch-indexed answer key"]
sources: ["arxiv-2511-20022"]
---
# Action-conditioned follow-up

A follow-up question can be asked after the answerer has committed to a first answer, and its correct answer may depend on that commitment. WaymoQA builds this into driving question answering. Stage 1 asks for the primary hazard, its likely motion and a feasible safe action. Stage 2 asks about the risk that the Stage 1 action itself induces. The paper frames the whole task this way: it "frames safety-critical reasoning as a two-stage task".[^c1]

The dependency is causal, not incidental. "the Stage 2 answer cannot be inferred from the current scene alone; it depends causally on the Stage 1 maneuver."[^c2] The paper's example is a maneuver that avoids a parked motorcycle by crossing the center line, and that crossing can create a new conflict with oncoming traffic. Stage 2 is therefore not one question with one key. Different first answers lead to different correct second answers, which the paper describes as counterfactual branching, where "different Stage 1 actions induce different Stage 2 risks."[^c3]

**The mechanism.** What separates this from an ordinary follow-up is the answer key. A plain follow-up has one correct answer whatever came before it. Here the key is indexed by the first answer, so the second question is graded against the branch the answerer actually took. The paper's joint criterion makes this explicit: a two-stage instance "counted as correct only if both Stage 1 and Stage 2" answers match the ground truth.[^c4]

Scoring this way is what gives the format its diagnostic force. A model can answer the second question well as a standalone item and still fail once it must hold its own first commitment fixed. On a subset of 245 key frames, the paper pairs 394 Stage 1 and Stage 2 instances.[^c7] Against the single-stage accuracy of the same models, the joint score falls for the generic baselines. The text reads this as "difficulty in maintaining stage-to-stage consistency when the dependency is enforced," with drops "typically 7–14%".[^c5] Table 5 gives the individual drops, from -6.9 to -14.1 points for the five generic models. The fine-tuned Qwen2.5-VL-7B shows "a markedly smaller degradation",[^c6] a drop of -2.4 points in the same table.

The structure is distinct from chaining where output feeds input. In an interconnected assessment the later problem receives the earlier solution as context, and the load is memory and multi-step reasoning. Here the later key itself changes with the earlier answer, so a correct second answer under a wrong first answer is not a correct response to the item. The useful unit is the pair (first answer, second answer) scored against a branch, not the second answer alone.

## Limits

- The joint criterion is strict. Under the paper's equation a Stage 2 answer that is sound given a wrong Stage 1 answer scores zero, and the sections read give no partial credit for it. The paper names partial scoring as a next step: "By transforming our existing annotations into multi-stage, chain-structured questions".[^c8] Whether partial credit changes the size of the drop is not tested here.
- The consistency test covers ImageQA only. "is excluded from this evaluation because equivalent" paired chains were not built for the video subset.[^c9]
- The main evaluation is a single human-written multiple-choice format, which the paper itself says "cannot fully capture open-ended safety-critical reasoning".[^c10]
- The drop compares two-stage accuracy with single-stage accuracy. I did not verify, from the sections read, that the single-stage column is computed over the same instances. If it is not, part of the drop is a difference of item sets.
- The one model with a small drop is fine-tuned on this same data. The matched-control analysis in the sections read concerns accuracy, not the two-stage drop, so the gap cannot be read as an effect of the branch-indexed format alone (my reading).
- The work does not measure how much harder a branch-indexed key is to write than a fixed key. Its annotations are human-written, and the cost of building the chains is not reported in the sections read.
- The driving setting is one domain. Transfer to other chains whose second key depends on the first answer is a conjecture of mine, not tested in this text.

## Related

- [[interconnected-problem-chaining]] — output-as-input chaining studied as context load; this note adds that the later key is indexed by the earlier answer and scored jointly.
- [[cross-question-answer-consistency]] — linked questions about one item whose answers must agree; here the second answer is keyed to the first, not only required to match it.
- [[top-down-conditional-consistency-audit]] — the same conditioning move for root and sub-claims: a lower-level accuracy is computed only where the level above is correct.
- [[descriptive-versus-interventional-question]] — Stage 2 asks what an action does to the risk, the interventional side of that split.

[^c1]: arxiv-2511-20022 — "frames safety-critical reasoning as a two-stage task"
[^c2]: arxiv-2511-20022 — "the Stage 2 answer cannot be inferred from the current scene alone; it depends causally on the Stage 1"
[^c3]: arxiv-2511-20022 — "induce different Stage 2 risks"
[^c4]: arxiv-2511-20022 — "counted as correct only if both Stage 1 and Stage 2"
[^c5]: arxiv-2511-20022 — "for generic baselines (typically 7–14%), indicating difficulty in maintaining stage-to-stage consistency when the dependency is enforced"
[^c6]: arxiv-2511-20022 — "exhibits a markedly smaller degradation"
[^c7]: arxiv-2511-20022 — "The evaluation contains 394 paired instances"
[^c8]: arxiv-2511-20022 — "By transforming our existing annotations into multi-stage, chain-structured questions"
[^c9]: arxiv-2511-20022 — "is excluded from this evaluation because equivalent"
[^c10]: arxiv-2511-20022 — "cannot fully capture open-ended safety-critical reasoning"
