---
description: "A named protocol that surveys each student a fixed, small number of times per term in randomly selected weeks; repeated use over terms measurably raises learning-related course ratings."
aliases: ["HRCF", "High-Resolution Course Feedback"]
sources: ["kim-2026-large"]
---
# High-Resolution Course Feedback

> A protocol for *how often to ask* the same open-ended axis over a fixed
> period: instead of asking everyone at a few fixed points, ask a small,
> fixed number of times per person, at randomly chosen points in time —
> trading a single high-burden elicitation schedule for many low-burden,
> desynchronized ones.

## Definition / Mechanism

High-Resolution Course Feedback (HRCF) was proposed by Kim and Piech at
Learning@Scale 2023 to resolve a measured tradeoff: as feedback requests
to a fixed group become more frequent, participation and response quality
both decline ("survey fatigue"), but a single end-of-term ask arrives too
late to change anything. HRCF's resolution is to fix the number of asks
per respondent and randomize *when* each respondent is asked, rather than
asking everyone at the same few points: "makes a fixed number of feedback
requests to every student but in randomly selected weeks of the course. As
a result, instructors receive feedback from a random subset of students
each week." In the baseline configuration each student answers at $S=2$
randomly chosen weeks, spaced at least two weeks apart, with four default
questions (one 5-point Likert, three free text).[^c1]

## Why it matters

This paper measures the downstream effect of the schedule itself, at
scale: 103 course offerings, 24,216 enrolled students, four years. First-time
adoption of HRCF showed no measurable change in end-of-term ratings. But
among small/medium courses (<250 students) that kept using it, each
additional term of use was associated with average rating increases of
0.045 (perceived learning goals achieved) and 0.048 (perceived learning
gains) points — for the two evaluation items tied to the student's own
learning, not for overall instructional quality or course organization,
and not for large-enrollment courses (≥250): "each additional term of HRCF
use is associated with average rating increases of 0.045 (GOAL) and 0.048
(LEARN) points for learning-related items. We observe no significant
associations for large-enrollment course offerings (≥ 250) or for the QUAL
and ORG items for any enrollment size."[^c2]

The effect is cumulative and instructor-mediated, not immediate: it is a
correlation with continued terms of use, not a manipulated dose the paper
randomized, and the paper reports it as an association, not the causal
effect of any single ask.[^c3]

## Limits

This is an observational, not experimental, study: course, instructor and
term are all confounded with the decision to keep using HRCF, so the
0.045–0.048 point associations are correlational, and the paper itself
frames them as such — a rating gain per term of continued use is also
consistent with self-selection (instructors who see it work keep using
it) rather than the mechanism raising ratings on its own. The measured
effect is specific to one R1 institution's computer-science offerings and
to two of four evaluation items; it does not establish that randomized,
fixed-count elicitation improves ratings anywhere the question axis or
respondent population differs.

## Related

[[bounded-rationality]] · [[reversibility]] · [[expected-information-gain]]

[^c1]: kim-2026-large — "makes a fixed number of feedback requests to every student but in randomly selected weeks of the course. As a result, instructors receive feedback from a random subset of students each week."
[^c2]: kim-2026-large
[^c3]: kim-2026-large — "we find that first-time use of HRCF is not associated with a measurable change in average student ratings. However, among small/medium-enrollment course offerings (<250) that continued using HRCF, each additional term of use is associated with average rating increases"
