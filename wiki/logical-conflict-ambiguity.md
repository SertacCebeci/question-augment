---
description: "A query is ambiguous iff two of its valid answers cannot both be true under one interpretation; this logical-conflict test, not answer diversity, is the criterion (Lee et al. 2026)."
aliases: ["ambiguity via logical conflict", "four-class ambiguity taxonomy", "ARCHIVE taxonomy"]
sources: ["lee-2026-diversity"]
---
# Logical-conflict ambiguity criterion

> A query is ambiguous exactly when two of its valid answers cannot both be true under one interpretation — not when its answers merely vary in wording.

## Definition / Mechanism

Lee, Park, Hong & Kang (2026) define: "A query q is ambiguous if its valid
answers include ai , aj that cannot be jointly satisfied under a single
interpretation of q; it is unambiguous if all valid answers are compatible."
[^c1]

They then divide queries into four mutually exclusive classes: "queries are
first classified as ambiguous or unambiguous based on logical conflict, then
divided into four classes." Surface-detectable [[efe-planning-as-variational-inference|ambiguity]] — a malformed or
unanchored query whose plausible repairs give conflicting answers.
Knowledge-dependent ambiguity — a well-formed query with more than one
interpretation whose answers conflict ("capital of Georgia": Tbilisi vs.
Atlanta). Closed unambiguity — answers converge to one fact or bounded set
(Colosseum: Rome, Italy). Open unambiguity — one interpretation admits
several compatible answers (advice on organizing a desk).[^c2]

## Why it matters

Diversity-based detectors — [[entropy]] over sampled answers, or clustering by
mutual entailment — cannot tell these last two classes apart, because both
produce a high-entropy answer set: "Diversity is not ambiguity. Both
queries yield diverse answers, but only the first reflects genuinely
conflicting interpretations." The distinguishing signal the criterion
needs is the presence of a **contradiction** between two valid answers, not
the size or spread of the answer set.[^c3]

## Limits

- The criterion runs over a *generated* candidate-answer set, not the true
  space of valid answers: if the interpretation that would conflict with the
  others is never sampled, the query scores unambiguous by omission, not by
  genuine convergence.
- "Cannot be jointly satisfied" is operationalized as NLI contradiction; the
  criterion inherits every failure mode of the NLI model used to judge it
  (equivalent facts phrased differently scoring as unrelated rather than
  entailing, for instance).
- Proposed and tested by the same paper that proposes it (QUIREQA, built by
  the authors from four re-annotated sources); the four-class split has not
  been independently replicated.

## Related

[[semantic-entropy]] · [[ambiguity-taxonomy]] · [[expected-information-gain]] · [[uncertainty-decomposition]]

[^c1]: lee-2026-diversity — "A query q is ambiguous if its valid answers include ai , aj that cannot be jointly satisfied under a single interpretation of q; it is unambiguous if all valid answers are compatible."
[^c2]: lee-2026-diversity — "queries are first classified as ambiguous or unambiguous based on logical conflict, then divided into four classes"
[^c3]: lee-2026-diversity — "Diversity is not ambiguity. Both queries yield diverse answers, but only the first reflects genuinely conflicting interpretations."
