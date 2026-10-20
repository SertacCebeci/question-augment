---
description: "A deterministic non-LLM verifier checks the latest tool result's decision status and overrides a generated answer with a grounded refusal when the model omits abstention or error."
aliases: ["status-preserving answer synthesis", "status fidelity check"]
sources: ["dey-2026"]
---
# Status-preserving verification

> Fluent generation can turn a fragile or refused estimate into a confident
> recommendation; this checks the generated answer against the decision that
> was actually made and overwrites it if the two disagree.

## Definition / Mechanism

Dey (2026) separates *what to say* from *whether advice
exists*: "The language model is not the final decision authority... A
deterministic verifier then inspects the most recent tool result. If the
model fails to acknowledge error, no-solution, or abstain status, the
verifier replaces the answer with a refusal grounded in that status." The
system contract additionally forbids the model from fabricating effects,
claiming live action, suppressing uncertainty, or converting an [[abstention]]
into advice.[^c1]

The paper defines the corresponding evaluation metric narrowly: "Status
fidelity is defined only for abstention/error cases and requires the answer
to preserve the underlying refusal or failure" — it is not a general
faithfulness score, only a check that a categorical upstream status survives
generation unchanged.[^c2]

On 24 live conversational questions routed through this verifier, the system
reported 100.0% tool-routing accuracy, 100.0% status fidelity and 0.983 mean
groundedness; on ten adversarial questions carrying injected instructions it
"resisted all injected instructions."[^c3]

## Why it matters

This is a concrete mechanism for stall 10's second half — not just deciding
to abstain (that is [[f-dace]]'s job here) but guaranteeing the abstention is
what the asker actually receives, by checking the final text against a
machine-readable status rather than trusting the generator to phrase it
faithfully.

## Transfer

| | |
|---|---|
| Home field | LangGraph tool-using conversational agent over a causal decision-support engine |
| Here | any answerer where an upstream module has already decided to decline, and a separate language layer produces the words |
| What survives | the two-stage separation — an LLM chooses and explains, a deterministic check decides whether advice exists at all; grounding a refusal in the actual upstream status rather than the model's own restatement |
| What does not | the implementation (JSON tool-result inspection tied to this LangGraph architecture); the dependence on a categorical status field — an answerer with no discrete upstream decision has nothing for this verifier to check against |

## Limits

- Evaluated on 24 live and 10 adversarial questions in one system with one
  upstream decision layer ([[f-dace]]); no claim is made about scale or about
  other agent architectures.
- Status fidelity as measured only covers abstention/error cases; the paper
  reports it "is defined only for" those, so it says nothing about whether
  non-abstained *recommendations* are represented faithfully by the same
  mechanism.
- The verifier is deterministic pattern-checking against a known status
  field, not a general hallucination detector; it works only because the
  upstream module already emits a discrete, machine-readable decision.

## Related

[[f-dace]] · [[abstention]] · Commitment

[^c1]: dey-2026 — "The language model is not the final decision authority."
[^c2]: dey-2026 — "Status fidelity is defined only for abstention/error cases and requires the answer to preserve the underlying refusal or failure."
[^c3]: dey-2026 — "On 24 live questions it achieved 100.0% tool-routing accuracy, 100.0% status fidelity, and 0.983 mean groundedness. On ten adversarial questions it resisted all injected instructions."
