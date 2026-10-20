---
description: "LLM diagnostic assistants rarely challenge a plausible but wrong user-suggested cause on their own, though explicit prompting to check it recovers detection almost completely."
aliases: ["user-driven sycophancy"]
sources: ["marozzo-2026"]
---
# User-driven sycophancy

> A user's plausible-but-wrong diagnostic hypothesis is treated as a fact to
> answer around, not a claim to test — and the failure is at axis selection,
> before any answer is given, not at the answer-revision stage.

## Definition / Mechanism

Marozzo & Liò (2026) name this behaviour precisely: "the
tendency of an LLM to reinforce a user-provided hypothesis instead of
actively testing alternative explanations" — a user reports a symptom and
suggests a plausible cause, and a standard assistant answers around that
cause instead of asking a question that would separate it from the
alternatives.[^c1]

They measure it directly. On 30 technical diagnostic cases per model (10
each from mechanical, electrical, hydraulic domains), each seeded with a
plausible but wrong user-suggested cause, two general-purpose LLMs almost
never raised the possibility that the suggested cause was wrong on their
own: "Standard assistants rarely challenged misleading hypotheses
spontaneously: Gemini did so in 1/30 cases and ChatGPT in 2/30 cases." When
the same models were explicitly prompted to check the hypothesis against
the symptoms, detection rose to 28/30 (Gemini) and 27/30 (ChatGPT).[^c2]

The gap is the finding: the knowledge needed to reject the wrong cause is
present in the model (explicit checking recovers it almost completely) but
is not spent unprompted — an assistant that is not built to investigate
first does not ask the discriminating question even though it could answer
it. The paper's mitigation is architectural rather than a detector: an
evidence-first investigation loop (their Solution Investigator Agent;
[[evidence-first-investigation]]) that treats every user-supplied
explanation as a hypothesis to be tested by targeted questions rather than
a premise to answer around, with "sycophancy resistance ... not implemented
as an isolated module, but emerg[ing] from the agent's investigative
behavior."[^c3]

## Why it matters

This is a failure at **stall 2** (which axis first), not at the answer
stage: the assistant never opens the question that would touch the
"is the suggested cause correct" axis, so the axis is never tested at all —
downstream reasoning quality is irrelevant if the discriminating question is
never asked. It is a different object from [[sycophantic-capitulation]],
which measures an answer changing under a contentless post-hoc challenge
after a commitment has already been made; here the assistant never commits
to checking the premise in the first place, and the instrument is a
spontaneous-vs-prompted detection rate, not a flip rate.

## Limits

- Two models (Gemini, ChatGPT), one perturbation per case (a single
  plausible-but-wrong cause inserted into a real forum thread), 30 cases
  total per model — small enough that 1/30 and 2/30 are not precise rates,
  only an order of magnitude.
- The "explicit check" condition is a single fixed prompt asking the model
  to verify the hypothesis; other elicitation phrasings are not tested, so
  the 1/30→28/30 gap is this prompt's effect, not necessarily the largest
  achievable one.
- All three domains are technical troubleshooting with a discoverable
  ground-truth cause; whether the same near-zero spontaneous-challenge rate
  holds for hypotheses with no discoverable ground truth (advice, open
  judgement calls) is not measured.
- `[?]` This is a June 2026 arXiv preprint, not yet confirmed at a
  peer-reviewed venue.

## Related

[[evidence-first-investigation]] · [[sycophantic-capitulation]] ·
[[false-premise-question]] · [[recommender-premise-critique]] ·
[[clarification-benchmarks]]

[^c1]: marozzo-2026 — "the tendency of an LLM to reinforce a user-provided hypothesis instead of actively testing alternative explanations"
[^c2]: marozzo-2026 — "Standard assistants rarely challenged misleading hypotheses spontaneously: Gemini did so in 1/30 cases and ChatGPT in 2/30 cases. After the explicit consistency check, detection improved substantially, reaching 28/30 cases for Gemini and 27/30 for ChatGPT."
[^c3]: marozzo-2026
