---
description: "In noisy agentic RL, fine-grained binary checklist criteria help, but assigning reward at finer granularity (step, turn) speeds early gains then collapses; trajectory-level assignment stays stable."
aliases: ["sparse in assignment, dense in criteria", "checklist rewards", "assignment granularity versus criteria granularity"]
sources: ["arxiv-2602-12268"]
---
# Sparse assignment, dense criteria

Reward design has two separate granularities. Assignment granularity is where along a trajectory the reward lands (final state versus intermediate steps). Criteria granularity is what is judged (one holistic verdict versus several weighted sub-dimensions).[^c1] CM2 treats them as orthogonal and finds that they should be set in opposite directions: fine-grained criteria, coarse assignment.[^c2]

## Mechanism

Each turn of a tool-use trajectory is annotated with a checklist: binary questions, each with evidence pointers, pass/fail conditions, a strictness flag, dependencies on other items and a weight.[^c3] Turning judging from open-ended scoring into a pass/fail classification is claimed to reduce judge randomness, because small stochastic score differences would otherwise be amplified by per-batch return or advantage normalization, changing within-batch rankings.[^c4] The checklists are made post hoc from existing trajectories at roughly $0.1 per trajectory.[^c5]

Strictness items gate the rollout: if all are satisfied the next user query is issued, otherwise the rollout ends early.[^c6] Items with dependencies can be credited back to earlier steps where their dependencies were already satisfied (reward backfilling), used only in step-level advantage.[^c7]

## What was measured

Three advantage variants were compared: trajectory-, turn- and step-level. Finer assignment gave faster early improvement, but finer granularities collapsed earlier and more severely, while trajectory-level kept improving.[^c8] The authors attribute this to residual judge and simulator noise entering optimization more often and being amplified by group-relative normalization.[^c9] The final configuration uses trajectory-level advantage.[^c10]

For asking and answering, the transferable point (my inference) is that a rich rubric of verifiable sub-questions can inform an evaluator without being used to localize credit finely; the checklist is a way of asking the judge better questions, not a license to score every step.

## Limits

- The noise-amplification explanation is the authors' attribution; it was not isolated by an experiment that varies noise directly. They themselves suggest that with sufficiently low-noise rewards step-level assignment may become viable.
- Evidence is from one training setup (GRPO, an LLM-simulated tool environment, an LLM judge); the collapse threshold may depend on the judge, simulator and group size.
- The claim that binary checklists reduce judge variance is argued, with the cited motivation, more than directly measured here against holistic scoring in this note's reading.
- Not tested on question-asking or clarification tasks; tool-use agents only.

## Related

- [[dependency-aware-checklist-scoring]] — checklist items with prerequisites, there used for scoring answers, here for gating and backfilling reward
- [[intermediate-action-feedback]] — step-level feedback, whose stability cost this note qualifies
- [[factored-versus-entangled-supervision]] — decomposing the supervision signal into separate parts
- [[shaped-ask-f1-reward]] — another reward design for question-asking agents

[^c1]: arxiv-2602-12268 — "where rewards are assigned along the trajectory, and what criteria are used for evaluation."
[^c2]: arxiv-2602-12268 — "Consequently, we adopt a"
[^c3]: arxiv-2602-12268 — "A binary checklist question to be answered for this item."
[^c4]: arxiv-2602-12268 — "This substantially reduces judge randomness"
[^c5]: arxiv-2602-12268 — "Each trajectory only costs approximately $0.1 on average"
[^c6]: arxiv-2602-12268 — "otherwise, we"
[^c7]: arxiv-2602-12268 — "Note that we only use backfilled reward in step-level advantage."
[^c8]: arxiv-2602-12268 — "finer granularities exhibit"
[^c9]: arxiv-2602-12268 — "We attribute this trade-off to noise amplification in agentic RL."
[^c10]: arxiv-2602-12268 — "trajectory-level advantage estimation with"
