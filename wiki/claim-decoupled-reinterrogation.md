---
description: "Turns each claim of a long-form LLM answer into a context-free question, answers it in a separate session, and scores faithfulness by whether the answer contradicts the original claim."
aliases: ["Interrogative Uncertainty Quantification", "IUQ", "interrogate-then-respond paradigm", "claim-level faithfulness"]
sources: ["arxiv-2604-15109"]
---
# Claim-decoupled reinterrogation

> A model that stays self-consistent across ten resamples of the same
> prompt can still be consistently wrong — so ask it something else.

## Definition / Mechanism

Fan, Duan & Xu (2026) target a failure that inter-sample
consistency cannot see: a long-form response is generated one token at a
time, so once an early sentence commits to a wrong fact, later sentences
keep conditioning on it and the whole response stays *coherent* without
being *true* — "long-form output may differ across samples but is rarely
self-contradictory due to next-token conditioning on the preceding
context. Therefore, a critical challenge occurs when models fabricate
information for the sake of logical consistency."[^c4]

Their fix is to break that conditioning. An **interrogator** (the same
model, to avoid a systematic capability gap between asker and answerer)
decomposes the long-form response into atomic claims, and for each claim
constructs up to three short, context-free questions whose answer would
demonstrate the claim's content without ever showing the model the claim
or the original prompt's generative context. As the paper puts it: "we
first differentiate the claims in a generative context from the model's
knowledge. Specifically, we incorporate an interrogator LLM to construct
tailored short questions for each factual claim made in the long-form
output. As a result, the original long-form response is decomposed into
atomic knowledge decoupled from the generative context."
[^c1]

The model answers each question fresh, in a session that carries none of
the earlier claims, so any agreement between that answer and the original
claim reflects the model's actual knowledge rather than its tendency to
stay locally coherent: "IUQ also enforces intra-sample claims consistency
through independent question-answering. The strategy is analogous to an
interrogate-respond scenario in which the responder is continuously
questioned by the interrogator to screen untruthfulness."
[^c2]

Faithfulness for a claim is then one minus the fraction of its
context-free answers that contradict it (and everything preceding it),
defined over "all claims that precede and include ci": "We are then
interested in knowing whether the model truly possesses the knowledge of
ci or fabricates ci from the generative context. This is achieved by
using the model M to provide an estimate of the percentage of
contradiction between Aq and Ci≤."
[^c3]

Averaged over a response and over a model's outputs, this yields a
per-model fabrication tendency (0.68–0.93 on FActScore, 0.91–0.97 on
LongFact across five model families) that inter-sample consistency alone
cannot expose, because a hallucinated biography can be perfectly
self-consistent across resamples.

## Why it matters

Every [[semantic-entropy|resample-and-compare]] style [[entropy|uncertainty
estimate]] assumes disagreement across samples is the signal. Reinterrogation
adds a second, orthogonal signal — disagreement between a claim and the
same model's answer to a *decontextualized* version of it — that catches
exactly the case resample-based methods miss: confident, consistent,
wrong. The asking is not decorative; the context-free question is what
does the decoupling that a same-context follow-up cannot.

## Limits

The interrogator, the decomposer and the answerer are all the same LLM,
so a hallucination anywhere in that pipeline (bad decomposition, a
misleading question, a wrong contradiction judgment) is undetectable by
construction — the authors mitigate this only with structured-output
constraints and heuristic sanity checks, not verification. The method
also does not process refusals ("I don't know") and costs roughly 47%
more tokens than the graph-based consistency baseline it compares
against, which bounds where it is practical: "IUQ pipeline requires
multiple stages of LLM inference, and thus may incur unexpectedly large
computation cost. Specifically, IUQ requires approximately 47.3% more
tokens than Graph-Based Uncertainty."
[^c5]

## Related

- [[semantic-entropy]] — the inter-sample consistency signal this method
  supplements rather than replaces.
- [[decoupled-claim-calibration-training]] — also isolates claims from a
  long-form response, but trains a confidence per claim instead of probing
  it with a fresh question.
- [[clarification-request]] — a different actor asking a question to
  resolve uncertainty, here the model interrogating itself.
- [[entropy]] — the token-probability baseline this claim-level
  probability signal is built to complement.

[^c1]: arxiv-2604-15109
[^c2]: arxiv-2604-15109 — "Different from other UQ methods that only implement inter-sample consistency, IUQ also enforces intra-sample claims consistency through independent question-answering. The strategy is analogous to an interrogate-respond scenario in which the responder is continuously questioned by the interrogator to screen untruthfulness."
[^c3]: arxiv-2604-15109 — "Given an atomic claim ci extracted from R, we denote Ci≤ as all claims that precede and include ci . We are then interested in knowing whether the model truly possesses the knowledge of ci or fabricates ci from the generative context. This is achieved by using the model M to provide an estimate of the percentage of contradiction between Aq and Ci≤"
[^c4]: arxiv-2604-15109 — "long-form output may differ across samples but is rarely self-contradictory due to next-token conditioning on the preceding context. Therefore, a critical challenge occurs when models fabricate information for the sake of logical consistency."
[^c5]: arxiv-2604-15109 — "IUQ pipeline requires multiple stages of LLM inference, and thus may incur unexpectedly large computation cost. Specifically, IUQ requires approximately 47.3% more tokens than Graph-Based Uncertainty"
