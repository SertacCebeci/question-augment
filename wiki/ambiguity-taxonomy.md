---
description: "Naming what is ambiguous determines the shape of the question. Berry, Kamsties & Krieger's handbook of ambiguity for requirements documents and contracts (2003,"
aliases: ["ambiguity types", "underspecification taxonomy"]
sources: ["berry-2003", "clamber-2024", "min-2020", "arxiv-2512-21120"]
---
# A taxonomy of ambiguity

> Naming what is ambiguous determines the shape of the question.

## Linguistic ambiguity types

Berry, Kamsties & Krieger's handbook of [[efe-planning-as-variational-inference|ambiguity]] for requirements documents[^s1][^s2][^s3]
and contracts (2003, §3.3) classifies linguistic ambiguity into four broad,
explicitly non-mutually-exclusive classes — lexical, syntactic, semantic,
pragmatic — with vagueness and generality as related phenomena (§3.3.5) and
language error as a sixth (§3.3.6). The cells below are those classes cut at
the grain an asker can act on: syntactic split into parse and ellipsis,
semantic reduced to scope, pragmatic reduced to reference.

```text
LEXICAL       homonymy or polysemy         "bank"                       §3.3.1
SYNTACTIC     more than one parse          "old books and magazines"    §3.3.2
ELLIPTICAL    omitted constituent          "do the same"                §3.3.2
REFERENTIAL   anaphor with >1 antecedent   "update it"                  §3.3.4
SCOPE         quantifier / negation scope  "every user has an account"  §3.3.3
VAGUE         admits borderline cases      "fast", "simple"             §3.3.5
```

The handbook's sharpest distinction for an asker is inside the last cell.
A **general** term (`cousin`) covers its possibilities and can be made
precise on demand; a **vague** one (`tall`) admits borderline cases and is
*inquiry resistant* — the unclarity recurses to where the unclarity begins.
Generality closes under one question; vagueness does not.

## Specification ambiguity types

The list below is joined to the one above by one criterion, not by a shared
linguistic mechanism: **more than one world stands after the utterance, and a
single clarifying question is the move that closes it.** That is the criterion
CLAMBER (Zhang et al., 2024) uses — one binary ambiguity label per query plus
one clarifying question — to put linguistic ambiguity and missing elements in
one taxonomy of ambiguous queries. Its *Aleatoric Output* dimension covers
queries whose input is well formed but whose output is confused for lack of an
essential element, split by which element is missing (whom / when / where /
what); its *Contradiction* category covers self-contradictory queries.

```text
MISSING PARAMETER   an unstated value       "deploy where?"           CLAMBER: where/when/what
MISSING GOAL        no purpose given        "why do they want it?"    this wiki's
MISSING CONSTRAINT  unstated constraint     "budget? deadline?"       this wiki's
MISSING SCOPE       no boundary drawn       "what is out of scope?"   this wiki's
CONFLICTING         incompatible wishes     "fast and cheap and now"  CLAMBER: contradiction
```

## Why a taxonomy is needed

Ambiguity is the normal case, not the pathology: Min et al. (2020) found over
half the questions in NQ-open ambiguous when annotators searched for every
plausible answer.

**The mapping below and the fork-marker rule are this wiki's inference, not
either source's** — neither Berry et al. nor CLAMBER maps a type to a form of
question:

| Type | Question shape |
|---|---|
| Lexical / referential | "By X do you mean this?" — binary choice |
| Vague | "How fast? Give a number." — quantity |
| Missing goal | "Why does this matter?" — [[five-whys]] |
| Missing scope | "What is not included?" — [[context-free-questions]] |
| Conflicting | "Which one can we give up?" — trade-off |

The practical scanning rule proposed here is a **fork-marker list**:
ambiguous pronouns, quantifiers, underspecified verbs ("handles", "manages",
"supports"), baseless comparatives, hedges.

What the lens buys: a route from a surface scan to a question form, so the
asker chooses wording rather than improvising it. What it cannot decide:
whether this fork is worth a turn at all, and — except in the vague/general
case — whether asking will close the cell.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Computational linguistics / requirements engineering | ambiguity types (lexical, syntactic, semantic, pragmatic) | close — the four classes are re-cut into six here |
| LLM benchmarks (CLAMBER) | ambiguous-query taxonomy; underspecification | close — its eight categories cover the linguistic half and the missing-element half, not missing goal/constraint/scope |
| Not this concept | **generality** (Berry et al. §3.3.5) | a general term opens no second world: one question makes it precise, so it is not a cell of this taxonomy |

## Transfer

| | |
|---|---|
| In its home field | Ambiguity is a property of a **text** that admits more than one licensed reading; the analyst enumerates readings and either disambiguates against a gold reading or rewrites the text — one rewrite per plausible answer in AmbigQA (Min et al., 2020). |
| Here | An asker classifies an underspecified **request** before wording the next question; the class selects the question's form. |
| What survives | The category set as a scanning lens over a request, and the vagueness/generality distinction, which tells the asker whether a question can close the cell at all. |
| What does not | Gold disambiguation — there is no annotated correct reading of a person's intent, only the person; measured parser- or model-level accuracy; and the assumption that the ambiguity is in the text, which the specification half violates, since a missing goal is in the speaker and no re-reading of the utterance recovers it. |

## Limits

- The six linguistic cells are a re-cut of Berry et al. (2003): they drop
  deictic ambiguity, language error (§3.3.6) and generality, so a request
  ambiguous only in those ways scans clean.
- The type→question-shape table and the fork-marker list are this wiki's own
  inference (conjecture in a `framework` note's clothing); neither source
  proposes them and neither reports precision or recall for a surface scan.
- MISSING GOAL, MISSING CONSTRAINT and MISSING SCOPE have no source behind
  them: CLAMBER's missing-element categories are whom/when/where/what.
- The two halves are one object here by the clarifying-question criterion
  alone. CLAMBER measures identification accuracy per category and omits
  syntactic and pragmatic ambiguity as rare in information retrieval, so the
  identity is this note's, not a measured one.
- Vagueness is inquiry resistant by the handbook's own definition, so the
  "give a number" shape stipulates a threshold rather than recovering one.

## An interactional cell (ClarifyMT-Bench)

ClarifyMT-Bench proposes a five-dimensional taxonomy "spanning linguistic, intent, contextual, epistemic, and" interactional ambiguity.[^s4] Its last dimension is not a property of the request: it is "Ambiguity introduced by the interaction itself when user replies are vague, off-focus, contradictory" or factually incorrect.[^s4] The types above place the missing element in the request or in the speaker. The interactional cell places it in the reply to a clarifying question, which the list above does not cover. The paper's first four dimensions are close to the lists above but are not mapped onto them here. The interactional cell is the paper's own construction, and this note has not tested it beyond that paper.

## Related

[[metamorphic-probes]] · [[uncertainty-decomposition]] · [[context-free-questions]] · [[clarification-benchmarks]] · [[clarification-request]] · [[user-response-persona-simulation]] · [[concept-deliberation]]

[^s1]: berry-2003
[^s2]: clamber-2024
[^s3]: min-2020
[^s4]: arxiv-2512-21120
