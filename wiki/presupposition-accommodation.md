---
description: "The wording of a question inserts propositions into the shared context, and **Stalnaker (1974).** Presupposition is not a property of sentences but a speaker attitude: taking $P$ for granted and as…"
aliases: ["accommodation", "rule of accommodation"]
sources: ["grice-1975", "hu-2023", "karttunen-1973", "kim-2021", "kim-2023", "lewis-1979", "loftus-1975", "stalnaker-1974"]
---
# Presupposition accommodation

> The wording of a question inserts propositions into the shared context, and
> a cooperative hearer *repairs the context to make the question askable*
> rather than challenging it. Wording is therefore a constraint channel that
> nobody asked for and no information measure counts.

## Definition / Mechanism

**Stalnaker (1974).** Presupposition is not a property of sentences but a[^s1][^s2][^s3][^s4][^s5][^s6][^s7][^s8]
speaker attitude: taking $P$ for granted and assuming the audience recognises
that you do. The shared background is modelled as a set of worlds that
accepted utterances shrink.

**Lewis (1979).** The rule of accommodation: if at time $t$ something is said
that requires presupposition $P$ to be acceptable, and $P$ is not presupposed
just before $t$, then — *ceteris paribus and within certain limits* — $P$
comes into existence at $t$. Acceptance is the default; objection is the
marked move.

**Grice (1975).** Under the Cooperative Principle, asking a question whose
felicity requires $P$ implicates that the asker believes $P$ and takes it as
settled. The implicature is defeasible but must be actively defeated.

**Karttunen (1973).** Presuppositions of embedded clauses project according to
the embedding environment: *holes* let them through, *plugs* block them,
*filters* let them through conditionally. Negation and interrogative
environments are holes — which is why a presupposition survives being
questioned at all, and why the phenomenon exists for questions and not only
for assertions.

The chain, for one question (the trigger examples below are illustrative, not
a sourced inventory — see Limits):

```text
wording triggers P      e.g. definite description, factive verb,
                        change-of-state verb, wh-restrictor
                        ("which linguist …")
hearer accommodates     P enters the common ground unless challenged
answer is conditioned   every subsequent reply is computed under P
```

**Empirically, accommodation is the default rather than the exception.**
Loftus & Zanni (1975) found that the definite article ("*the* broken
headlight") produced more reports of an event that never occurred than the
indefinite version; the reported rates differ between secondary accounts
(15% or 17% against 7%) and are marked `[?]` here — the direction, not the
magnitude, is what this note uses. In question answering, Kim et al. (2021)
attribute ~21% of unanswerable Natural Questions to unverifiable
presuppositions; Kim et al. (2023) show models answer questionable-assumption
queries as if the assumption held; Hu et al. (2023) show that ~256 fine-tuning
examples suffice for a model to start rejecting false premises — so the
knowledge is present and the *default behaviour* is accommodation.

## Known as

| Name | Field | Relation |
|---|---|---|
| rule of accommodation | philosophy of language (Lewis) | exact |
| common ground update | formal pragmatics (Stalnaker) | close — the state the rule edits, not the rule |
| questionable assumption / false premise | NLP evaluation | close — the false-$P$ subset the datasets measure |
| loaded question, *plurium interrogationum* | informal logic | close — names the fallacy, not the update mechanism |
| leading question | law, eyewitness psychology | close, not an alias — measured as answer/memory distortion, a different object |

## Why it matters

1. **A question adds constraints that were never asked.** [[expected-information-gain]] scores the answer set; accommodation moves $W$ before any answer exists. Two phrasings of the same partition ([[question-as-partition]]) install different $P$ and therefore leave different residual spaces.
2. **It inverts the presupposition failure case.** Partition semantics says a false presupposition leaves no true answer, so the question is defective. Accommodation says the update succeeds anyway: the hearer adopts a false $P$ and answers under it. The defect is silent.
3. **This wiki's inference** (no source cited here states it): for an agent that asks its own sub-agents, this is contamination. The asker's belief $P$ would arrive at the answerer as settled context, and the reply would confirm a model rather than test it — the mechanism behind the ethnographic warning in [[grand-tour-question]], now with a named update rule.
4. **A formulation step therefore has a checkable job**: mark each $P$ the draft carries as verified / unverified / false, and either drop the trigger or ask $P$ itself first. Kim et al. (2021) implement exactly this pipeline — generate presuppositions, verify, explain — for incoming questions, with verification the bottleneck.

## Transfer

| | |
|---|---|
| **Home field** | pragmatics of two cooperative human speakers; a common ground of mutually recognised propositions, updated utterance by utterance |
| **Here** | an agent formulating one question to a user, tool or sub-agent whose belief state it does not observe |
| **What survives** | the trigger → accommodate → condition chain; the default-acceptance asymmetry; the projection fact that questioning $P$'s carrier does not cancel $P$ |
| **What does not** | the identification of the common ground with $W$ — the common ground is the *answerer's* accepted background, [[possible-worlds]] is the asker's hypothesis space, and accommodation corrupts the first while leaving the second unchanged, which is precisely why the error is invisible to the asker; also mutual recognition, which no tool or API answerer has |

## Limits

- No source cited here establishes a *complete* inventory of presupposition
  triggers. The list in the mechanism block is illustrative; Karttunen (1973)
  gives projection behaviour, not an enumeration. A formulation step that
  claims to check "all" triggers is claiming more than this note supports.
- Lewis's rule holds "within certain limits" that he does not specify. There is
  no model of when accommodation fails, and hence no way to predict which
  triggers are safe. The rule is a description of a tendency, not a bound.
- `[?]` The Loftus & Zanni magnitudes could not be verified against the primary
  text; the verifier rejected a specific rate for `loftus-1975`. Only the
  direction of the effect is claimed here.
- The NLP evidence (kim-2021, kim-2023, hu-2023) is about questions posed *to*
  a model. That an agent's *own* questions contaminate an answerer the same way
  is **this wiki's inference**; no source cited states it (point 3 above).
- [[conversational-maxims|Grice's maxims]] idealise a cooperative speaker. A strategically silent or
  adversarial answerer accommodates for reasons the framework does not model
  ([[dialectic-red-team]]).
- Nothing here says which presuppositions are worth removing. Removing all of
  them yields [[context-free-questions|context-free questions]], which cost more turns
  ([[question-budgets]]).

## Related

[[question-as-partition]] · [[survey-response-model]] · [[grand-tour-question]] · [[ambiguity-taxonomy]] · [[possible-worlds]] · [[question-budgets]]

[^s1]: grice-1975
[^s2]: hu-2023
[^s3]: karttunen-1973
[^s4]: kim-2021
[^s5]: kim-2023
[^s6]: lewis-1979
[^s7]: loftus-1975
[^s8]: stalnaker-1974
