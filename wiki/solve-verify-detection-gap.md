---
description: "Models asked to compute a tax answer ignore injected factual contradictions 63-76% of the time, yet the same models flag 75-83% of those same contradictions when asked only to verify the input."
aliases: ["solve-verify gap", "solving versus verifying asymmetry"]
sources: ["sadowski-2026"]
---
# Solve-verify detection gap

> Computing an answer and checking the same input for a defect are different
> tasks put to the same model, and a model that fails the first can pass the
> second on the identical case.

## Definition / Mechanism

Sadowski & Chudziak (2026) evaluate six LLMs on SARA tax
cases perturbed with an injected categorical contradiction (e.g. "file
jointly" alongside "file separately"), under two task framings on the same
input: **solve** (return the tax liability or abstain) and **verify**
(return only none / missing / contradiction, no computation). "On injected
contradictions the four high-accuracy models abstain on at most 15% while
solving (three of the four under 5%), and return the clean-input answer
63-76% of the time instead, with no signal that the input was defective.
Asked to verify the same inputs rather than solve them, the same models flag
75-83% of those identical contradictions, so the detection is recoverable."[^c1]

The asymmetry is contradiction-specific, not general over-confidence: "on
missing facts the same models almost never return the clean answer
(preservation under 2%), so the failure to abstain on contradictions is
selective."[^c2]

A worked case makes the mechanism concrete: "GPT-5 mini returns the
clean-input $6,621 on the contradicted case while solving, but the same
model, asked to verify that same input, returns contradiction and names the
conflict: 'the facts state both that Alice and Bob file jointly in 2017 and
that they file separately in 2017.'"[^c3]

## Why it matters

On stall 10 this locates the failure precisely: it is not that the answerer
lacks the fact-conflict signal, and not that it never surfaces — it is that
the *solve* task framing never asks the model to surface it. The signal
exists and is legible under a different framing of the same call, which
turns "the model didn't notice" into "the pipeline never asked," a
routing question rather than a capability question.[^c4]

## Limits

- Measured on one domain (91 SARA tax cases, LegalBench), one perturbation
  type (a single injected categorical contradiction per case, three
  categories: marital/filing status, dependents), and six models across four
  providers; the 63-76%/75-83% bands are this benchmark's, not a general
  constant.[^c5]
- The two low-clean-accuracy models (GPT-5.2, Claude Sonnet 4.6) are
  excluded from the diagnosis itself: their error sizes on contradicted
  inputs match their clean-input error sizes, so their [[abstention]] reflects
  general uncertainty rather than targeted detection, and only the four
  high-accuracy, chain-of-thought models establish the gap.[^c6]
- The verifier is the same weights as the solver, so the two calls share
  failure modes the paper cannot separate from a genuinely independent
  check.[^c7]

## Related

[[abstention]] · [[recognition-refusal-dissociation]] · [[contradiction-gate]] · Commitment

[^c1]: sadowski-2026 — "On injected contradictions the four high-accuracy models abstain on at most 15% while solving (three of the four under 5%), and return the clean-input answer 63-76% of the time instead, with no signal that the input was defective. Asked to verify the same inputs rather than solve them, the same models flag 75-83% of those identical contradictions, so the detection is recoverable."
[^c2]: sadowski-2026 — "on missing facts the same models almost never return the clean answer (preservation under 2%), so the failure to abstain on contradictions is selective."
[^c3]: sadowski-2026
[^c4]: sadowski-2026 — "Asked instead to verify the input (§3.6), the four high-accuracy models flag 75-83% of these contradictions as inconsistent, well above the 0-15% they abstain on while solving."
[^c5]: sadowski-2026 — "We use 91 tax cases taken from the SARA (StAtutory Reasoning Assessment) subset of the LegalBench benchmark"
[^c6]: sadowski-2026 — "The two direct-answer models are interpreted only for the gate, as noted above (§4.1). Their error magnitudes on contradictions match their clean-input errors (Claude Sonnet: median 0.282 vs. 0.271; GPT-5.2: 0.218 vs. 0.189), so the abstention they show (Claude Sonnet 43.2%, GPT-5.2 7.4%) reflects general uncertainty rather than targeted detection."
[^c7]: sadowski-2026 — "The verifier is the same model as the solver: this holds the model fixed (same weights, solve versus verify), at the cost of correlated errors (§6)."
