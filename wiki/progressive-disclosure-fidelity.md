---
description: "Expert review of 2,350 AI-patient messages across 207 sessions finds a scripted, disclose-only-when-asked policy held with 99.3% rated appropriate and 0.68% clear fidelity failures."
aliases: []
sources: ["yang-2026"]
---
# Progressive-disclosure fidelity

> An LLM-driven standardized patient instructed to reveal case information
> only when asked, never volunteering it ahead of the question that would
> earn it, held that policy in expert review across thousands of messages
> — with a caveat about what the [[calibration|reliability]] statistic can and cannot show.

## Definition / Mechanism

The patient agent of the platform described in
[[gated-socratic-scaffolding]], reported by Yang et al. (2026),
answers from a scripted case (chief complaint, history, exam findings,
expected diagnosis) but is built to disclose that content only in response
to the question that targets it — a controlled-commitment answerer role,
"wait to be asked" rather than "volunteer everything known"; the
disclose-only-when-asked rule is the second Quantity maxim of
[[conversational-maxims]] made into an answerer policy. Three clinical
experts reviewed every one of 2,350 patient messages across 207 sessions
for two binary fidelity judgments: whether the reply stayed consistent with
the script, and whether information was disclosed only when asked rather
than prematurely.[^c1]

Across the corpus, only approximately 0.68% of AI-SP responses were judged
to contain clear fidelity problems, and progressive disclosure was rated
as appropriate in approximately 99.3% of patient messages.[^c2]

The chance-corrected reliability statistic for the same two judgments is
weak or degenerate, and the paper's own explanation is the pass rate:
agreement was lower for AI-SP progressive disclosure (κ = 0.31), likely
reflecting the highly imbalanced distribution of labels, as nearly all
patient responses were rated as appropriate, and script adherence showed
near-zero agreement because almost all responses were classified as
adherent, leaving little between-rater variability to estimate.[^c3]
This wiki's reading is that the low κ therefore neither confirms nor
refutes the raters' strictness — see the second bullet of Limits.

## Why it matters

For stall 10 — how much an answerer commits, and how it expresses the
rest — this changes one step of the evaluation procedure. An asker's
coverage or history-taking score measured against a simulated answerer is
interpretable only if the answerer's non-volunteering is audited per
message by pass rate: a leaky answerer inflates the asker's coverage by
handing over what was never asked for. And κ cannot serve as that audit
when the labels are near-ceiling, so the audit is a separate, pass-rate
check, not a reliability statistic. The note also supplies what
[[leakage-controlled-user-agent]] lacks: that design specifies the same
kind of reveal-only-what-is-targeted policy but its paper reports no
audited leak rate, whereas here the rate is measured at the scale of
thousands of messages.

## Limits

- The 99.3%/0.68% figures rate fidelity against a fixed, author-written
  case script, not against open-world patient knowledge; fidelity to a
  scripted state machine is a narrower test than fidelity to an unscripted
  domain.
- Fleiss' κ collapses toward zero for exactly these two judgments because
  almost every message was rated appropriate — the near-ceiling pass rate
  is consistent with very high fidelity, but the reliability statistic
  cannot independently confirm the raters were applying a strict,
  discriminating standard rather than converging on a lenient one.
- No unconstrained baseline (an LLM patient prompted without a
  disclose-on-request instruction) is reported alongside this condition in
  the text available to this wiki, so the failure rate is not benchmarked
  against what an unconstrained agent would do.
- Measured on one platform and one prompt design, with three acute
  abdominal cases used for the experiment; not a general claim about LLMs'
  disclosure control elsewhere.[^c4]

## Related

[[gated-socratic-scaffolding]] · [[leakage-controlled-user-agent]] · [[conversational-maxims]] · [[abstention]]

[^c1]: yang-2026 — "all 2350 AI-SP messages were annotated for patient fidelity, including whether the response adhered to the case script and whether information was disclosed progressively rather than prematurely"
[^c2]: yang-2026 — "Only approximately 0.68% of AI-SP responses were judged to contain clear fidelity problems."
[^c3]: yang-2026 — "Agreement was lower for AI-SP progressive disclosure (κ = 0.31), likely reflecting the highly imbalanced distribution of labels, as nearly all patient responses were rated as appropriate."
[^c4]: yang-2026 — "For the present experiment, three acute abdominal cases were used"
