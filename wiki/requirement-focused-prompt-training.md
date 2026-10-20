---
description: "Training novices only on articulating complete, correct requirements, with defect-targeted feedback against reference requirements, beat standard prompt-engineering training (19% vs 1% gain, n=30)."
aliases: ["Requirement-Oriented Prompt Engineering", "ROPE", "requirement articulation training"]
sources: ["doi-10-1145-3731756"]
---
# Requirement-focused prompt training

Ma et al. argue that what a human must supply when prompting an LLM for a complex task is the customized requirements (for example "start the response with a tl;dr"), not tricks such as role-play or "think step-by-step", which optimizers can add automatically.[^c1] Their paradigm, Requirement-Oriented Prompt Engineering (ROPE), trains only that skill.

## Mechanism

Training separates requirement articulation from peripheral prompting work such as persona crafting or paraphrasing. Learners describe an app (Tetris, an email proofreader) from interaction examples, only as accurate and complete requirements, and never write a full prompt during training.[^c2]

Feedback is anchored in expert reference requirements, not in the model's own judgment. The LLM compares the learner's requirements with the reference and picks the most critical defect: mismatched first, then missing, then ambiguous. Three feedback types follow. A tutor chat hints at omissions or commissions, for example asking "What's on top of the board?". Matching reference requirements are revealed progressively. A counterfactual output shows the flawed program the learner's vague or wrong requirement would produce.[^c3] An annotated sample of the feedback had a correct rate of 88.6%.[^c4]

## What was measured

In a randomized pre/post study, the ROPE group's overall prompt score rose from 21.9% to 40.9% (p<0.001) on isomorphic tasks, where learners wrote full prompts.[^c5] The paper reports a gain of about 19% against about 1% for a control that got a standard prompt-engineering tutorial plus self-practice with ChatGPT.[^c6] Requirement quality and LLM output quality were scored separately. They correlated strongly (Spearman rho = 0.71 with GPT-4o outputs, 0.80 with o3-mini), so better stated requirements produced outputs that met more of the needed features.[^c7]

Two robustness checks bear on the claim. An automatic prompt optimizer improved requirement quality but did not close the gap between the control and the trained group. A stronger reasoning model followed explicit requirements more faithfully instead of making them obsolete.[^c8]

## Why it bears on asking well

The training moves the learner's effort to the part of a request that only the asker knows. This is the same gap that clarification work targets from the model's side. The note's own inference: training the asker to state omitted requirements is the human-side counterpart of a model asking about them.

## Limits

- 30 novices, one 1.5-hour session, immediate post-test; retention and transfer to real, self-chosen tasks were not tested.
- Tasks were game and GPTs-app replication from examples, with reference requirements known to the experimenters. Open-ended tasks without a reference are not covered, and the feedback depends on having one.
- Scoring against a grading rubric of needed features rewards recall of the reference. It does not test whether requirements the rubric lacks would also help.
- The requirement-to-output correlation is not uniform. Connect4 showed none with GPT-4o outputs until split by implementation type.[^c9]
- No ablation separates the three feedback types, so which one carries the gain is unmeasured.

## Related

- [[prompt-coach]] — a rubric-and-Socratic prompt tutor with a single-arm gain; this study adds a randomized control and a single-skill focus
- [[specification-channel-redundancy]] — what the user states versus what the model infers
- [[underspecbench]] — benchmark of underspecified requests, the failure the trained learner avoids
- [[information-need-reification]] — making an unarticulated need explicit

[^c1]: doi-10-1145-3731756 — "existing prompt engineering instructions often lack focused training on requirement articulation and instead tend to emphasize increasingly automatable strategies"
[^c2]: doi-10-1145-3731756 — "we deliberately avoided having"
[^c3]: doi-10-1145-3731756 — "we always have GPT-4o to compare the current user requirements to the reference, and select the most critical defect to provide feedback on"
[^c4]: doi-10-1145-3731756 — "The final analysis revealed a correct feedback rate of 88.6%."
[^c5]: doi-10-1145-3731756 — "from 21.9% ± 14.6% to 40.9% ± 18.4%"
[^c6]: doi-10-1145-3731756 — "ROPE training leads to greater learning gains (19%) than Control training (1%)"
[^c7]: doi-10-1145-3731756 — "We found a strong positive correlation,"
[^c8]: doi-10-1145-3731756 — "optimizers can indeed improve requirement quality, but they cannot close the gap between the baseline and the"
[^c9]: doi-10-1145-3731756 — "Connect4 showed no correlation when"
