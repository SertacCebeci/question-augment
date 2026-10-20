---
description: "A matched-token-budget retry protocol with a content-free placebo condition separates the value of merely retrying from the value of the feedback content in self-correcting code agents."
aliases: ["placebo-controlled matched-budget design", "blind resampling control"]
sources: ["verma-2026", "doi-10-48550-arxiv-2306-09896"]
---
# Placebo-controlled retry evaluation

> Comparing a self-repair loop against a no-retry baseline cannot tell you
> whether the loop's gain comes from the feedback or just from getting
> another try; this protocol adds a control condition that retries without
> any feedback, so the two are priced separately.

## Definition / Mechanism

The design compares four retry conditions at an identical output-token
budget, each differing only in what is appended to the prompt after a
failed attempt: nothing (resample), a content-free notice that the attempt
was wrong (placebo), the actual test output (feedback), and feedback plus
an instruction to diagnose the failure in prose first (reflect). "Systems
built on this idea are widespread ... and the evidence offered for them is
typically a comparison against single-shot generation. That comparison
cannot separate two mechanisms. Retrying at all raises the success rate
under stochastic decoding, independently of whether the retry is informed;
a loop that consumes k additional samples should be credited only for what
it achieves beyond k uninformed samples."[^c1]

Reading the four conditions in sequence isolates two separate effects:
"the step from resample to placebo isolates self-exposure, and the step
from placebo to feedback isolates diagnostic information."[^c2]

The protocol requires stochastic decoding for the control to be meaningful:
"Under greedy decoding the model returns a byte-identical program on every
iteration, which would reduce resample to a no-op and flatten all curves by
construction — an artifact we encountered and corrected before running the
experiment."[^c3]

## Why it matters

For stall 2, this is a check to run before crediting any "ask a follow-up
that references what was wrong" strategy: without a blind-resample control
at the same budget, an apparent gain from a diagnostic follow-up question
may be nothing but the gain of trying again. The protocol turns "does
feedback help" into two separately measurable quantities — the value of
persistence and the [[value-of-information|value of information]] — rather than one confounded
comparison.

## Transfer

| | |
|---|---|
| Home field | Clinical-trial methodology: a placebo arm isolates an active ingredient's effect from the act of receiving treatment |
| Here | Code-agent self-repair evaluation: a content-free "you were wrong" notice isolates self-exposure from the diagnostic content of execution feedback |
| What survives | The logic of the control — match everything except the one ingredient under test (here, token budget and retry count; there, dosing schedule) |
| What does not | Random assignment across independent subjects and blinding of the experimenter — the "patient" is one deterministic-except-for-temperature model, and the placebo notice is a transparent stand-in, not an indistinguishable treatment |

[^c4.1][^c4]

## A matched-sample check in another setting

The same matched control appears in a study of one-shot code repair with Code Llama, GPT-3.5 and GPT-4, where the no-repair baseline is i.i.d. sampling at the same number of programs. Its headline is that "instances in which pass rates are higher or equally high with i.i.d. sampling (without repair)," occur, so a repair loop does not reliably beat blind resampling at a fixed budget.[^c5] The study reports that at a fixed budget the factor that matters most is the diversity of the initial samples, not the diversity of the repairs.[^c6]

The study has no placebo arm, so it cannot separate self-exposure from the content of the feedback. Its finding that initial diversity dominates is consistent with the self-exposure account above, but it does not test that account (my inference).

## Limits

- Demonstrated on one task family (MBPP+ code synthesis) and one model
  family (Qwen2.5-Coder) at three sizes; the protocol's logic is general but
  its use here is not evidence it generalises to other agentic tasks
  (e.g. multi-turn dialogue or tool use) without re-running the same
  decomposition there.
- The placebo and feedback conditions are matched on prompt structure, not
  proven fully matched on token count in every cell (Table 1 shows the
  conditions' token costs differ by up to ~5×), so the "matched budget"
  claim is about the retry loop's design, not a perfectly equalised prompt.

## Related

[[self-repair-anchoring]] · [[value-of-information]] · [[bounded-rationality]]

[^c1]: verma-2026
[^c2]: verma-2026 — "the step from resample to placebo isolates self-exposure, and the step from placebo to feedback isolates diagnostic information."
[^c3]: verma-2026
[^c4.1]: verma-2026 — "We therefore treat self-repair as a treatment requiring a placebo. Our control is blind resampling: the original prompt, re-sampled, with no reference to the failed attempt."
[^c4]: verma-2026
[^c5]: doi-10-48550-arxiv-2306-09896 — "instances in which pass rates are higher or equally high with i.i.d. sampling (without repair),"
[^c6]: doi-10-48550-arxiv-2306-09896 — "determining whether self-repair will lead to a correct program or not is the diversity of the base"
