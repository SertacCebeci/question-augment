---
description: "Socratic-guidance tutoring matches prompt-refinement tutoring in-session, but predicts more independent understanding-driven prompting and greater learning gains once the tutor is removed."
aliases: ["Socratic-Guidance vs Prompt-Refinement tutoring", "SG-PR transfer effect"]
sources: ["brender-2026"]
---
# Socratic-guidance transfer effect

> Two ways of scaffolding a student's LLM use — asking reflective questions
> back, or gatekeeping the student's own prompt — look identical while the
> scaffold is on, and diverge only once it is removed: the reflective
> condition, not the prompt-quality gate, is the one that transfers to
> independent question-asking.

## Definition / Mechanism

Brender, El-Hamamsy, Uittenhove et al. (2026) compare two
LLM-tutor designs in a graduate robotics course: a [[staged-socratic-hint-policy|Socratic]]-Guidance (SG)
tutor that "structures interaction through dialogic questioning" by
generating open-ended reflective questions instead of direct answers, and a
Prompt-Refinement (PR) tutor that evaluates each incoming prompt for
clarity and learning-intent and blocks a response until the student revises
it to meet a rubric. 66 students used one tutor for a 6-week, three-session
lab intervention; 52 of them then used an *unconstrained* LLM (no
scaffold) for a 3-week course project.[^c1]

During the guided sessions the two conditions were behaviourally
indistinguishable: a cluster analysis of prompt type and quality found no
significant difference in which prompting pattern students fell into by
condition (χ²=1.12, p=0.77) — yet in the final guided session SG students,
despite a significantly lower pre-test score, showed a significantly
larger pre-to-post learning gain than PR students (interaction β=0.72,
p=0.01).[^c2]

## Why it matters

The behavioural difference the guided sessions hid appeared once the
scaffold was removed. In the unconstrained project phase, the distribution
of students across prompting-pattern clusters differed significantly by
prior condition (χ²=8.14, p=0.017): former SG students were far more
likely to become "Understanding-driven prompters" (nSG=13 vs nPR=4), and
former PR students far more likely to fall into low-quality "Debugger"
prompting (nPR=8 vs nSG=2).[^c3]

That shift mattered for outcomes: at the project-group level, groups with
more Understanding-driven prompters scored significantly higher on an
independent understanding exam than groups with more Debuggers (β=1.30,
p=0.025), while Implementer-vs-Debugger groups did not differ. So the
tutor variable that changed later, unscaffolded question quality is not
the one visible during scaffolded use.[^c4]

The trade-off runs the other way for perceived usefulness: PR students
rated their tutor as more effective for the task, for learning, and for
writing useful prompts than SG students did, even though the SG condition
produced the better downstream outcome.[^c5]

## Limits

- Small, single-domain, self-selected sample (n=66 in the intervention,
  n=52 continuing into the unscaffolded phase; one graduate mobile-robotics
  course at one institution); the authors themselves flag that unobserved
  motivation differences could confound condition.
- The project-understanding regression explains only 33% of group-level
  variance (adjusted R²=0.22) and is fit at the group (not individual)
  level with partial trace coverage of who used the chatbot — the SG→
  understanding-driven-prompting→higher-understanding chain is an
  association traced through cluster membership, not an experimentally
  isolated causal path.
- The SG condition's advantage is entirely post-intervention; during
  guided use the two tutors produced statistically indistinguishable
  prompting patterns, so this is a claim about durability after the
  scaffold is withdrawn, not about the scaffold's immediate effect.
- Both tutor designs are one implementation choice each (RAG-backed GPT-5
  agent, one prompt-quality rubric, one reflective-questioning prompt); a
  differently calibrated PR or SG tutor could shift the comparison.

## Related

[[socratic-method]] · [[gated-socratic-scaffolding]] · [[scaffolding-need-trajectory]] · [[non-advisory-dialogue]]

[^c1]: brender-2026 — "a Socratic-Guidance (SG) tutor, which structures interaction through dialogic questioning, and a Prompt-Refinement (PR) tutor that guides the formulation of effective prompts. We conducted a two-phase study in a graduate-level mobile robotics course: 66 students used either the SG or PR tutor during a 6-week intervention, followed by 52 students using an unconstrained LLM during a 3-week course project."
[^c2]: brender-2026 — "A χ2 test examining the distribution of students across prompting-pattern clusters by intervention condition revealed no significant differences between the SG- and PR-tutor conditions (χ2 = 1.12, p = 0.77)."
[^c3]: brender-2026 — "Unlike in session S3, the distribution of students across clusters differed significantly by condition (χ2 = 8.14, p = 0.017)."
[^c4]: brender-2026 — "Groups with a higher number of Understanding-driven prompters achieved significantly higher understanding grades than groups with more Debuggers (β = 1.30, p = 0.025)"
[^c5]: brender-2026 — "students in the PR condition reported more favorable perceptions of their tutor than students in the SG condition, with respect to perceived effectiveness for solving the task (Kruskal-Wallis H = 482, pcorrected = 0.09, d = 0.5), learning (H = 449, pcorr = 0.045, d = 0.5), and writing useful prompts (H = 440, pcorr = 0.045, d = 0.6)."
