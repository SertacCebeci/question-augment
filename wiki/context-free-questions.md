---
description: "[[gause-1989|Gause & Weinberg, *Exploring Requirements* (1989)]], ch. 6. Questions askable"
aliases: ["Gause–Weinberg questions", "domain-independent questions"]
sources: ["gause-1989"]
---
# Context-free questions

> Gause & Weinberg, *Exploring Requirements* (1989), ch. 6. Questions askable
> without domain knowledge, valid in every project.

## Definition / Mechanism

A question is context-free when its answer set is defined over the[^s1]
**interaction** (process), the **artefact's value dimensions** (product), or
the **question set itself** (meta) — none of which require knowing the
domain's vocabulary. Gause & Weinberg define them as "high-level questions
that can be posed early in a project to obtain information about *global*
properties of the design problem and potential solutions," appropriate "for
any product to be designed, whether it's an automobile, airplane, ship,
house, a jingle for a one-minute television commercial for chewing gum, a
lifetime light bulb, or a trek in Nepal" (p. 59). In their own decision-tree
image, such questions "help you decide which limb to climb, rather than
which branch or twig" (p. 59) — they cut high in the tree, before the
vocabulary of the branches exists ([[optimal-decision-tree]]).

**Process questions** (p. 65)
> "Who is the client?" · "What is a highly successful solution really worth
> to this client?" · "How much time do we have for this project?" · "What is
> your trade-off between time and value?" · "Where else can the solution to
> this design problem be obtained?"

**Product questions** (p. 65)
> "What problems does this product solve?" · "What problems could this
> product create?" · "What environment is this product likely to encounter?"
> · "What kind of precision is required or desired in the product?"

**Metaquestions** (pp. 62–65)
> "Am I asking you too many questions?" · "Do my questions seem relevant?" ·
> "Are you the right person to answer these questions?" · "Is there anything
> else I should be asking you?" · "May I return or call you with more
> questions later, in case I don't cover everything this time?"

## Why "context-free"

They require no domain knowledge — the same battery is offered for an
elevator information device and for "Trekking in Nepal" (p. 59), and the
authors' claimed advantage is precisely that the questions "can be prepared
in advance, before much is known about the project" (p. 64).

## Why it matters

Gause & Weinberg's set is the human-side existence proof that a question
battery can be domain-independent: the same three categories were applied
across projects with no shared domain, prepared before the domain was known.
What it does not show is that domain-independent questions are the *most
informative* ones ([[blackwell-informativeness]]) — they are universally
*applicable*, not universally *better*.

The metaquestion category covers the closing question
("Is there anything else I should be asking you?") — the cheapest instrument
for hunting [[unknown-unknowns]], and the one the authors say "you can ask at
the end of every interaction" (p. 63).

## Limits

- Applicability is not informativeness ([[blackwell-informativeness]]).
- One source, one field; the evidence for "it works" is the authors'
  practice report, not a controlled comparison.
- Question wordings above are verbatim from ch. 6 of the 1989 Dorset House
  edition (pp. 59–65), checked against a scanned chapter; the source is still
  carried at `verified: prior` in `meta/sources.json` and the rest of the
  book has not been checked page-by-page.
- Several questions presuppose a cooperative informant who knows why they are
  answering; the authors themselves flag that "are your answers official?"
  is one many people will not answer accurately (p. 63). They fail where the
  answerer is adversarial or unaware.

## Related

[[grand-tour-question]] · [[unknown-unknowns]] · [[blackwell-informativeness]] · [[optimal-decision-tree]]

[^s1]: gause-1989
