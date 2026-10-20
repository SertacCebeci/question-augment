---
description: "The answerer's contract, as Grice wrote it — and three of its four clauses **Grice (1975)** states the **Cooperative Principle**: \"Make your conversational contribution such as is required,"
aliases: ["Gricean maxims", "Grice's maxims", "maxims of conversation", "conversational maxims"]
sources: ["engelhardt-2006", "frank-2012", "grice-1975", "sperber-1987"]
---
# Conversational maxims and the Cooperative Principle

> The answerer's contract, as Grice wrote it — and three of its four clauses
> take a parameter the answerer does not observe, so comprehension is what
> makes the contract evaluable at all.

## Definition / Mechanism

**Grice (1975)** states the **Cooperative Principle**: "Make your[^s1][^s2][^s3][^s4]
conversational contribution such as is required, at the stage at which it
occurs, by the accepted purpose or direction of the talk exchange in which you
are engaged." Under it, four categories:

| Category | Maxims (Grice's wording) |
|---|---|
| **Quantity** | 1. as informative as is required (for the current purposes of the exchange); 2. not more informative than is required |
| **Quality** | supermaxim: try to make your contribution one that is true. 1. do not say what you believe to be false; 2. do not say that for which you lack adequate evidence |
| **Relation** | a single maxim: "Be relevant." |
| **Manner** | supermaxim: "Be perspicuous." Avoid obscurity; avoid [[efe-planning-as-variational-inference|ambiguity]]; be brief; be orderly |

Three structural facts, all Grice's own, carry more than the list does:

1. **The set is ordered, not a checklist.** "Other maxims come into operation
   only on the assumption that this maxim of Quality is satisfied." Quality is
   a precondition; the other three range over contributions already believed
   true and adequately evidenced.
2. **Grice doubts Quantity-2.** He calls the second Quantity maxim
   "disputable" and suspects "its effect will be secured by a later maxim,
   which concerns relevance" — the ban on over-informing may be redundant.
3. **The maxims are indexed to a purpose the answerer must supply.** Quantity
   is explicitly relative to "the current purposes of the exchange"; Relation
   is relevance *to* something Grice declines to fix; and he warns "I have
   stated my maxims as if this purpose were a maximally effective exchange of
   information; this specification is, of course, too narrow." So Quality can
   be checked against the answerer's own evidence alone, while Quantity,
   Relation and Manner are predicates on (reply, *question*): until the
   question is fixed there is no fact of the matter about how much is
   "required". Roberts's move of defining Relevance against the top of the QUD
   stack ([[question-under-discussion]]) is one way of supplying that argument.

Grice also distinguishes **four ways of failing a maxim**: quiet and
unostentatious violation, opting out, a clash between maxims, and *flouting* —
blatant failure that is itself the message.

**People are only moderately Gricean.** Engelhardt, Bailey & Ferreira (2006),
three experiments on referring expressions: speakers over-described almost a
third of the time and listeners did not judge over-descriptions any worse than
concise ones, but in the Visual World Paradigm over-descriptions triggered eye
movements interpretable as confusion. The maxim describes neither production
nor explicit judgement, yet leaves a processing trace.

**Quantity becomes computable once the alternative set is fixed.** Frank & Goodman (2012) model referential communication games by assuming speakers try
to be informative and listeners invert that by Bayesian inference, and report a
close, parameter-free fit to human judgements.

## Known as

| Name | Field | Relation |
|---|---|---|
| conversational maxims, maxims of conversation, Gricean maxims | philosophy of language, linguistics | exact |
| Cooperative Principle, CP | philosophy of language | close — the general principle the maxims implement, not the maxim set itself; Grice's maxims are the specific rules "the following of which will, in general, yield results in accordance with the Cooperative Principle" |
| conversational implicature | pragmatics | *not* this concept — the inference a hearer draws when a maxim is flouted; the output of the framework, measured separately |
| principle of relevance | relevance theory (Sperber & Wilson) | *not* this concept — a generalisation about cognition, not a norm, and one principle where Grice has nine; see *Limits* |
| Q- and R-principles | neo-Gricean pragmatics (Horn) | *not* this concept — a proposed reduction of the maxim set, a different object with different predictions |

## Why it matters

1. **Stall 9 has a reason internal to answering.** By Mechanism 3, three
   quarters of the contract is unevaluable without a fixed question:
   comprehension supplies the argument the maxims take.
2. **Quality's priority orders the two answerer stalls.** "Do not say that for
   which you lack adequate evidence" is a commitment rule ([[calibration]]),
   and the other maxims are operative only where it holds — so an answerer
   maximising worlds removed ([[constraint-as-information]]) under Quantity
   does so inside a region Quality has already bounded.
3. **Flouting is a channel, not a failure.** An answerer that can only comply
   has no way to say anything by conspicuously not saying it.
4. **This wiki's inference** (no source cited here states it): the four maxims
   are not commensurable, so "how Gricean is this answer" has no value — but an
   answerer that reports which question it took converts three of them from
   unfalsifiable norms into checkable ones.

## Transfer

| | |
|---|---|
| **Home field** | philosophy of language: two cooperative humans in a talk exchange with a mutually recognised purpose; the maxims are norms whose *violation* is the explanandum, since flouting them generates implicature |
| **Here** | an answerer — human, model or tool — producing one reply to one received question, to an asker whose purpose it does not observe |
| **What survives** | Mechanism 1–3: Quality's priority, the doubt about Quantity-2, the indexation stall 9 must supply; and flouting as a signalling channel |
| **What does not** | the implicature machinery, which needs a hearer who assumes cooperation and runs the inference — a downstream program consuming a tool's answer does not; the *ceteris paribus* in the CP, which Grice never bounds; and any procedure — nothing in Grice computes "as informative as is required" |

## Limits

- **The priority claim is this wiki's.** Grice states the indexation and the
  ordering of Quality; that this makes comprehension logically prior to three
  maxims is an inference drawn here, marked in place.
- **Only flouting-as-signal is used here.** The four-way taxonomy of failing a
  maxim is named above but not developed; the clash case in particular is left
  untouched, and nothing in this note distinguishes an answerer that opted out
  from one that violated quietly.
- **The maxims are norms without a metric.** No source cited here lets one say
  that reply A observes Quantity better than reply B. Any scoring of answers
  "against the maxims" imports a measure Grice does not supply.
- **The quantitative result does not scale to answering.** Frank & Goodman fit
  games with small, enumerated alternative sets. An open-ended answer has no
  such set, so the informativeness term is undefined there.
- **The empirical result is about reference, not about answers.** Engelhardt
  et al. measured referring expressions describing objects in a visual display;
  extending their rate to the length of an answer is not supported.
- **A rival account denies the set is needed.** Sperber & Wilson (1987) hold
  that a single principle of relevance "is thus enough on its own" to account
  for disambiguation, reference assignment and the [[recovery-postulate|recovery]] of implicatures. If
  they are right, the four-way structure this note leans on is an artefact.
- **Grice's frame is cooperative by construction.** An answerer with an
  interest in the asker's belief state is outside it, and the maxims give no
  way to detect one ([[dialectic-red-team]]).

## Related

[[question-under-discussion]] · [[presupposition-accommodation]] · [[conclusive-answer]] · [[constraint-as-information]] · [[calibration]] · [[dialectic-red-team]]

[^s1]: engelhardt-2006
[^s2]: frank-2012
[^s3]: grice-1975
[^s4]: sperber-1987
