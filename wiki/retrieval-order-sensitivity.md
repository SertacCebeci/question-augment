---
description: "The same propositional content, concatenated in a different order into a Jang, Lee, Shin & Jung (2026,"
aliases: []
sources: ["jang-2026"]
---
# Retrieval sensitivity to content ordering

> The same propositional content, concatenated in a different order into a
> retrieval query, returns a measurably different set of documents —
> wording is not exhausted once an [[efe-planning-as-variational-inference|ambiguity]] type and a content set are
> fixed.

## Definition / Mechanism

Jang, Lee, Shin & Jung (2026, §2.1) hold the atomic content of[^s1]
a conversational-search query fixed and vary only the order in which
components are concatenated (the original utterance, a rewritten
stand-alone query, its anticipated answer, a follow-up query, its
anticipated answer). Querying the ANCE dense retriever over TopiOCQA with
the same components in different orders, the average overlap between the
retrieved document sets is 0.72 at top-10 and 0.71 at top-100 — a Jaccard
distance of about 0.28-0.29 — so roughly a third of what is retrieved
changes under reordering alone, with no change to which words are present.
The paper reports the effect as more pronounced for dense retrievers than
for sparse (lexical) ones, without giving a paired number for the sparse
case.

## Why it matters

Every existing row on Formulation treats a question's content — its
ambiguity type, its topic, the axis it touches — as the thing that
determines the answer, and treats phrasing as either free
([[ambiguity-taxonomy]]'s type-to-shape mapping does not condition on word
order) or as a confound to be tested out across many human respondents
([[survey-response-model]]'s split-ballot logic). This finding adds a
formulation variable neither treats: for an automatic answering channel,
the *arrangement* of already-chosen content is itself a lever on what
constraint comes back, independent of ambiguity type or topic. It is the
empirical premise [[compcqr]] is built on: because a machine channel can be
re-queried near-freely, this sensitivity is exploitable (generate many
orderings, aggregate) rather than merely a nuisance to be minimised.

## Transfer

| | |
|---|---|
| Home field | Dense and sparse neural/lexical retrieval, where a query is an embedding or a bag of terms and evaluation is set-overlap or ranked accuracy against a fixed corpus. |
| Here | The general formulation stall: how a question's exact form, not only its content, determines what an answering channel returns. |
| What survives | The general claim that content order is a formulation variable in its own right, additional to — and measured separately from — the ambiguity-type classification this wiki already carries. |
| What does not | The specific mechanism (embedding geometry, term-matching weights) that makes order matter is particular to today's retrieval architectures; nothing here says a human answerer's response is order-sensitive in the same way or degree. |

## Limits

- Single-paper, single-retriever (ANCE) evidence on one benchmark
  (TopiOCQA) for the headline number; the sparse-retriever comparison is
  reported only qualitatively ("less pronounced") in the source, with no
  paired number the wiki could extract this pass.
- The five components compared are specific to a conversational-search
  pipeline (utterance, rewrite, anticipated answers, follow-up); the note
  does not establish that order-sensitivity holds for arbitrarily chosen
  content pieces or in other retrieval settings.
- No claim is made here about *why* order matters mechanically; the source
  does not offer one and this note does not supply one.

## Related

[[compcqr]] · [[survey-response-model]] · [[ambiguity-taxonomy]] · [[self-ask-decomposition]]

[^s1]: jang-2026
