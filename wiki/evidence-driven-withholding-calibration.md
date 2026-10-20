---
description: "Four pass/fail acceptance gates plus a scripted-persona test loop that sorts every rejection by cause, not just verdict, turning an ambiguous compliance number into a fixable diagnosis."
aliases: ["measure diagnose fix loop", "cause-separated diagnostic loop", "acceptance gates for withholding"]
sources: ["pisan-2026"]
---
# Evidence-driven withholding calibration

> A single pass rate on "did the tutor withhold correctly" cannot be
> debugged; splitting each failure by its cause before fixing anything
> turns one contradictory number into a ladder of separable bugs.

## Definition / Mechanism

Pisan (2026) tunes an answer-withholding tutor (see
[[answer-withholding-supervisor-architecture]]) against four measurable
acceptance gates rather than a single score: no detector-confirmed solution
reveal (G1); an earnest-turn over-revise rate at or below 5% (G2, since
over-blocking is treated as the more harmful error); at least 95%
hint-ceiling compliance under adversarial pressure, scored by an
independent auditor (G3); and no exam passed through injection or grader
failure (G4). G1, no solution reveals: across an adversarial suite, no
detector-confirmed C++ solution reaches the student. G2, do not over-block
honest help: the earnest revise rate is at most 5%. G3, hint-ceiling
compliance: compliance is at least 95%. G4, exam integrity: no mastery exam
is passed through injection or grader failure.[^c1]

Gates G2 and G3 are exercised by a deliberately billed live loop: scripted
personas (earnest-but-stuck, answer-seeker, gate-evader, injector) drive the
production system, and every turn is re-judged by a stronger auditing
model, with no human subjects involved. "Two choices made the difference
between a number and a diagnosis." The first is sorting each rejection by
cause — a true withholding failure, a pedagogy-quality issue, or a
grounding issue — since only the first kind counts against G3, because "a
single undifferentiated pass rate mixes all three." The second is
recording the judge's stated reason and not just its allow/revise/block
verdict, since an unexplained revise "invited blind fixes."[^c2]

Applied iteratively, this surfaced a descending "over-help ladder" of
distinct failure causes rather than one stuck number: a measurement
artifact in the auditor (half of apparent ceiling violations were
grounding rejections, not over-help), then genuine code-under-pressure
leaks, then over-blocking from a mastery-only ceiling that ignored
debugging need, then fabricated citations under a "ground every claim"
instruction, each fix exposing the next cause underneath it.[^c3]

## Why it matters

For the wiki's stopping and consistency stalls, this is a concrete method
for a case where an aggregate compliance metric is uninformative by
construction — two opposite failure modes (over-blocking and leaking)
can move the same score in ways that cancel or confound — and cause
attribution, not more data, is what makes the metric usable to fix.

## Limits

- Demonstrated on one system and one evaluation harness; the "descending
  ladder" of failure causes is a report of what this deployment's fixes
  uncovered in order, not a claim that the same causal ordering
  generalizes to other tutors or domains.[^c4]
- The auditing model that re-judges compliance is itself an LLM judge with
  known biases (position, verbosity, self-preference) that the paper
  names but does not fully rule out for its own auditor.
- `pisan-2026` is an unreviewed arXiv preprint (harvested 2026-09-18) —
  `[?]` pending verifier confirmation.

## Related

[[answer-withholding-supervisor-architecture]] · [[gated-socratic-scaffolding]] · [[sprt]] · [[value-of-information]]

[^c1]: pisan-2026 — "G1, no solution reveals: across an adversarial suite, no detector-confirmed C++ solution reaches the student."
[^c2]: pisan-2026 — "Two choices made the difference between a number and a diagnosis."
[^c3]: pisan-2026 — "Sorting G3 rejections by cause (§4.4) showed that half of the apparent ceiling violations were grounding rejections, not over-help."
[^c4]: pisan-2026 — "We applied the method iteratively to the deployed tutor."
