---
description: "Reframes an abstention failure as the model answering a misinterpreted query q* instead of the user's query q, not as low confidence in the right answer."
aliases: ["Query Misalignment Framework", "answering the wrong question"]
sources: ["arxiv-2604-02230", "doi-10-48550-arxiv-2407-12216"]
---
# Query misalignment framework

> Do not ask how sure the model is of its answer; ask what question the
> answer actually answers.

## Definition / Mechanism

[[arxiv-2604-02230|Gourabathina, Padhi, Nagireddy, Chaudhury & Sattigeri
(2026)]] give a different account of why a model fails to abstain. Standard
accounts treat abstention as a *knowledge gap*: the model is asked $q$,
produces $p_\theta(y\mid q)$, and abstains when its confidence in $y$ is
low. Their framework instead treats the model as first resolving $q$ into
an internal, possibly wrong, interpretation $q^*$ and then answering that:
"Hallucinations resulting in failed abstention can be reinterpreted as LLMs
answering the wrong question (rather than answering a question
incorrectly)."[^c1]

Formally: "We frame LLMs as generative models that first resolve the user
query q into an internal interpretation q∗ before generating an answer from
pθ(y∣q∗). In this view, abstention should be triggered not by
self-evaluating errors or quantifying uncertainty in p(y∣q∗) but instead
[by evaluating] if there is misalignment between q and q∗." A large
distance between $q$ and $q^*$ is the abstention trigger, not a confidence
score on $y$.[^c2]

The framework names five ways $q^*$ can diverge from $q$, each a distinct
abstention scenario rather than one undifferentiated "unanswerable" class:

- An [[abstention|unanswerable]] question has no documented, consensus
  answer and would remain unanswerable despite added context.[^c3]
- Underspecified context: the question would be answerable given more
  detail, and the model may hallucinate the missing detail instead.[^c4]
- Underspecified aim: it is unclear what the user intended, and the model
  may hallucinate that intent.[^c5]
- False premise: the question is predicated on an incorrect statement the
  model may misinterpret as true or as a modified version of the false
  claim.[^c6]
- Subjective: the correct answer depends on personal opinion, and the
  model may misread it as asking for public opinion or a specific
  characteristic it hallucinates about the user.[^c7]

## Why it matters

This displaces the object of measurement for the answerer's commitment
(stall 10): instead of scoring $y$ against a correctness threshold, or
scoring the trace for whether it *names* the gap (as in
[[detection-to-abstention-gap]]), the framework scores the *question the
model actually answered* against the question it was asked. A knowledge-gap
account and a query-misalignment account can disagree on the same trace: a
model can be well calibrated about $y$ given its own $q^*$ and still be
answering the wrong $q^*$ entirely, a failure mode confidence-only
abstention cannot see because it never re-derives $q^*$.

The same divergence appears, unlabelled, in retrieval-augmented question answering over knowledge graphs. Mindful-RAG's error analysis of StructGPT on WebQSP attributes most failures to reasoning, and in its words "models frequently fail to grasp the question’s intent" and rely "primarily on structural cues and semantic similarity to extract" relations.[^c8][^c9] Read through this framework, a relation chosen by semantic similarity answers a q* that drifted from q. That reading is my inference; the paper does not reconstruct q*. It also tests no abstention: its outcome is answer accuracy on a fact-QA benchmark, with no measure of whether the intended question was recovered.

## Limits

- The framework is descriptive, not itself falsifiable independent of a
  measurement of $q^*$; its only instantiation the source provides is
  reconstructing $q^*$ from the reasoning trace, so the account is tested
  jointly with that reconstruction method, not on its own.
- The five scenarios are the source's own taxonomy, not shown to be
  exhaustive or mutually exclusive; a question could combine an
  underspecified aim and a false premise.
- Assumes an LLM's output is well described as answering some single
  reconstructible $q^*$; whether this holds for multi-step agentic or
  tool-using answers, rather than single-turn QA, is untested here.

## Related

[[abstention]] · [[detection-to-abstention-gap]] · [[trace-inversion]] ·
[[recognition-refusal-dissociation]] · [[judge-then-solve]] ·
Commitment

[^c1]: arxiv-2604-02230 — "Hallucinations resulting in failed abstention can be reinterpreted as LLMs answering the wrong question (rather than answering a question incorrectly)."
[^c2]: arxiv-2604-02230
[^c3]: arxiv-2604-02230 — "Unanswerable question: A question without a documented, consensus answer. The question would remain unanswerable despite added context."
[^c4]: arxiv-2604-02230 — "Underspecified context: Questions about a context which lacks key required details."
[^c5]: arxiv-2604-02230
[^c6]: arxiv-2604-02230 — "False premise: Questions predicated on an incorrect or false statement."
[^c7]: arxiv-2604-02230 — "Subjective: Questions where the correct answer depends on personal opinion or experience."
[^c8]: doi-10-48550-arxiv-2407-12216 — "Models frequently fail to grasp the question’s intent"
[^c9]: doi-10-48550-arxiv-2407-12216 — "primarily on structural cues and semantic similarity to extract"
