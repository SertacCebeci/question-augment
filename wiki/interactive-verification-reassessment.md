---
description: "Follow-up questions drafted from automated rubric scores are answered by the student, and the score is recalculated on those answers as process evidence rather than fixed by the text alone."
aliases: ["interactive verification", "score-driven follow-up verification", "scalable oral defense", "follow-up reassessment"]
sources: ["arxiv-2512-12592"]
---
# Interactive verification reassessment

A submission can be scored in two passes. The first pass grades the text against an analytic rubric. The second pass asks the author questions about the text, and the answers are fed back into the score. The second pass is what carries information the text alone cannot. In the design of arxiv-2512-12592, the system "drafts up to three customized follow-up questions designed to elicit further evidence of the student" understanding.[^c1] The questions come from the first-pass scores. The paper names two kinds: evaluative questions that "resolve ambiguous scores by requesting examples, elaborations" and citations tied to one criterion, and authenticity questions that probe transfer, rephrasing and contextual adaptation.[^c2]

The reassessment step is the mechanism that makes the answers count. The model receives the original submission, the rubric, the initial scores and justifications, and the question–response pairs, and is prompted to "recalculate the score for each criterion based on the" totality of this evidence, generating new justifications wherever a score changes.[^c3] The first-pass score is therefore treated as provisional. Its criteria select where to ask, and only an answer that supplies evidence on a criterion can move that criterion's score. The paper's premise is that a text which is AI-generated or shallowly understood shows its weakness in the second pass: "its limitations are likely to become apparent during this" stage.[^c4]

The pattern is an operational form of a validity argument. The authors read the two passes against Messick's framework: the first stage supports content validity and internal structure, the second provides "response process evidence".[^c5] What is new relative to a one-shot grader is that the evidence is elicited on demand, scoped to a criterion, and recorded so that a human can see which answer moved which score. The paper keeps a human in that loop: "Instructors approve and modify AI outputs" at each stage, including the questions before they reach the student.[^c6]

## Limits

The pilot is small and exploratory. "The findings are exploratory, based on a small" sample of nine university instructors.[^c7] The submissions were instructor-authored exemplars, and the reassessment ran on instructor-written proxy answers, so the loop was simulated: "a reassessment using instructor-authored proxy" responses, not student work.[^c8] The paper does not measure whether the second pass detects AI authorship, whether it changes final scores in a way that tracks understanding, or whether students answer the questions honestly under time pressure. The evidence is instructor perception of fairness and validity, not a measured gain in validity.

The gap in the questioning itself is open. Instructors rated the questions as relevant and consistent, yet asked for the difficulty to be "differentiated according to the student’s level", which the authors read as a call for adaptive questioning.[^c9] A single difficulty for all students is a known weak point of this design.

The mechanism also depends on the first pass. The follow-up questions are drafted from its scores and justifications, so a first pass that rewards surface features sends the second pass to the wrong criteria. The paper's own survey shows that the first pass was the weakest rated stage on construct validity; see [[fairness-construct-validity-tension]].

## Related

- [[code-fact-grounded-socratic-assessment]] — its follow-up is triggered when a grader flags an answer as vague; here the trigger is the score on each rubric criterion, and the answer revises that score.
- [[argument-grounded-socratic-questioning]] — also Socratic follow-up, but gated on the writer's own verbalization of a fix, not on a rubric score.
- [[on-demand-follow-up-generation]] — follow-up questions generated when requested in an interview, with no reassessment of an earlier judgment.
- [[fairness-construct-validity-tension]] — the gap that motivated the second pass: automated scoring alone was rated fair but weak on construct validity.

[^c1]: arxiv-2512-12592 — "drafts up to three customized follow-up questions designed to elicit further evidence of the student"
[^c2]: arxiv-2512-12592 — "Evaluative supplementary questions to resolve ambiguous scores by requesting examples, elaborations"
[^c3]: arxiv-2512-12592 — "recalculate the score for each criterion based on the"
[^c4]: arxiv-2512-12592 — "its limitations are likely to become apparent during this"
[^c5]: arxiv-2512-12592 — "Stage 2 (interactive verification and reassessment) provides response process evidence"
[^c6]: arxiv-2512-12592 — "Instructors approve and modify AI outputs"
[^c7]: arxiv-2512-12592 — "The findings are exploratory, based on a small"
[^c8]: arxiv-2512-12592 — "a reassessment using instructor-authored proxy"
[^c9]: arxiv-2512-12592 — "the difficulty of the questions needs to be differentiated according to the student"
