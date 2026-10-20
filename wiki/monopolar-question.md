---
description: "A biased question proposes exactly one continuation, an addressee commitment to one proposition; neutral questions are disjunctions of such moves, and the reverse answer costs a retraction."
aliases: ["biased question", "monopolar vs bipolar question", "commitment space semantics of questions", "declarative question"]
sources: ["krifka-2015"]
---
# Monopolar question

In Krifka's commitment space semantics a conversation state is a set of commitments plus the set of licit continuations. A question is a move that does not change what is committed so far. It restricts the continuations to assertions by the other participant.

A **monopolar question** offers one such continuation. In the paper's words: "A speaker can propose just one legal continuation to the addressee. I will call such moves monopolar questions."[^c1] Answering with the proposed proposition is a direct step. Answering with its negation requires first rejecting the offered move, which is the formal trace of the question's bias. The paper's examples are the declarative question "I won the race?" and the plain polar question "Did I win the race?".

## What it replaces

The classical polar question offers a proposition and its negation as two equal alternatives (Hamblin-style; compare [[question-as-partition]]). Krifka calls that a **bipolar** question. He argues that standard theories "have problems with biased questions; they have to" add outside machinery to favour one option.[^c2] In his model the bias needs no extra device, because offering only one option is the bias.

Bipolar questions are derived from the monopolar ones: "Bipolar questions can be derived as explicit question disjunction."[^c3] Alternative questions ("Ann, Beth, or Carla?") and constituent questions are likewise disjunctions of monopolar moves. The existence of explicit alternative questions ("Did I win, or not?") is offered as evidence that the bare polar question is monopolar. Otherwise the disjunction would be redundant.[^c4] Chinese A-not-A questions are said to be neutral, while particle-*ma* questions are biased.

## Negation and bias strength

The model orders question forms by how strongly they bias.

- **No negation.** It is ambiguous between a monopolar reading, fitting contextual evidence for the proposition, and a bipolar reading, fitting a neutral context.
- **Low (propositional) negation.** It is monopolar only, "as the bipolar interpretation is blocked by the corresponding question without negation".[^c5] It therefore signals a bias toward the negated proposition and suits contexts with evidence against the positive one.
- **High negation** ("Didn't I win?"). Negation applies at the commitment level, so the question projects a non-commitment by the addressee. It is weaker than low negation: a reply of "I do not know" needs no prior rejection, whereas "yes" does. It is out of place when the context supports the positive proposition.

The paper's table pairs these forms with three contexts: evidence for, neutral, and evidence against.

## Question tags

Tags are built with the same pieces. A matching tag ("You are tired, are you?") is a conjunction of an assertion and a monopolar question: "Matching question tags can be analyzed as speech act conjunction of an assertion and a monopolar question".[^c6] If the addressee rejects it, the speaker stays committed to the proposition, unlike with a plain assertion. A reverse tag ("I have won, haven't I?") is a disjunction of the assertion and the question. The addressee may accept, or retract and assert the opposite, without contradicting any earlier commitment.

## Non-congruent answers

An answer like "I don't know" cannot sit alongside either offered commitment. It is modelled as retraction followed by a new move: "Retraction is required because the resulting commitment".[^c7] The cost sits in the move structure, not in the answer's content.

## Limits

- This is a formal-semantics proposal tested on a handful of English, German and Chinese examples and on a judgment table borrowed from Büring and Gunlogson. No behavioural data, and nothing about human or machine question-asking.
- That a questioner's choice of form signals a prior (bias) and makes one reply cheaper than another is the paper's claim about speakers. Whether LLM askers or answerers track this is untested. Any use for question design is this wiki's own inference, not a result of the paper.
- The notion of "evidence" in the context table is informal, and the paper's own remark that a "neutral" context may still carry some interest shows the categories are soft.
- The framework models only commitments of two participants; probabilistic bias strength is not modelled, only which alternatives are offered.

## Related

- [[question-as-partition]] — the bipolar, equal-alternatives view that monopolar questions generalise or replace
- [[conversational-maxims]] — the pragmatic norms on which bias and informativeness inferences rest
- [[possible-worlds]] — the set-of-worlds backdrop; here the object is a set of commitment states instead

[^c1]: krifka-2015 — "A speaker can propose just one legal continuation to the addressee. I will call such moves monopolar questions."
[^c2]: krifka-2015 — "Standard question theories have problems with biased questions; they have to"
[^c3]: krifka-2015 — "Bipolar questions can be derived as explicit question disjunction."
[^c4]: krifka-2015 — "This strategy of forming bipolar question is evident in Chinese A-not-A questions, in contrast to questions marked by the final particle ma, which have a biased, i.e., monopolar reading"
[^c5]: krifka-2015 — "The question with low negation (ii) only has a monopolar reading, as the"
[^c6]: krifka-2015 — "Matching question tags can be analyzed as speech act conjunction of an assertion and a monopolar question, as illustrated in (44) and in Figure 15."
[^c7]: krifka-2015 — "Retraction is required because the resulting commitment"
