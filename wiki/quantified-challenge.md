---
description: "A second request recovers what the first one missed only if it does two Study 3: 295 MBA students listed objectives for choosing a summer internship (unaided mean 6.39 objectives,"
aliases: ["quantified challenge", "add-n request", "target request"]
sources: ["bond-2010"]
---
# Quantified challenge

> A second request recovers what the first one missed only if it does two
> things: assert that the list is incomplete, and name how many more to add.
> "Anything else?" bought 0.55 items; "research demonstrates most people can
> add at least nine" bought 4.87.

## Finding (Bond, Carlson & Keeney, *Decision Analysis* 2010)

Study 3: 295 MBA students listed objectives for choosing a summer internship[^s1]
(unaided mean 6.39 objectives, not differing across conditions), then were
randomly assigned to one of six second-stage requests.

| Second request | Objectives added | % who added any |
|---|---|---|
| simple review — "review your list … add any" | 0.55 | 20.0 |
| deeper review — "research demonstrates … add any" | 2.77 | 87.7 |
| add three | 3.08 | 86.5 |
| add six | 3.90 | 94.0 |
| add nine | 4.87 | 86.7 |
| categories — "research demonstrates …" + four category headings | 3.56 | 81.4 |

Two separable effects. (a) The **message** does the first and largest share of
the work: simple and deeper review differ only in a preamble stating that
people typically list under 50% of their significant objectives and that most
can generate more — 0.55 against 2.77, $t(103) = 5.46$, $p < 0.01$. (b) The
**number** scales the yield: regressing objectives added on the target
requested gives $\beta = 0.30$, $F(1,145) = 9.27$, $p < 0.01$. The additions
were not padding: their mean importance was 7.23 against 7.28 for the initial
list ($t(465) = 0.32$, $p = 0.76$).

This note is the message **plus a target** — the add-three/six/nine cell of
that table. The message alone is a different and smaller quantity (2.77), and
is [[warning-as-debiasing]].

**Cueing with examples backfires.** In Study 2 (158 participants, three
*initial-stage* formats), category headings raised the raw list from 9.2 to
12.7 objectives, and four sample objectives raised it to 12.2 (10.45 adjusted
for the four given) — but neither reduced the objectives later recognised from
the master list as relevant-but-omitted: 7.9 standard, 7.9 categories, and
**10.8 for the examples condition**, reliably worse than both ($F(1,155) =
8.26$ and $7.57$, $p < 0.01$). A longer list, less complete. The authors read
this as part-list cueing — retrieving the given items suppresses the rest.

Study 1 (20 doctoral students, dissertation topic) shows the second-chance
form: a category-aided second opportunity added 4.5 objectives to an initial
7.25, of which 2.9 mapped uniquely onto master-list entries, raising the
self-generated set by over 30%.

## Why it matters

[[objectives-generation-deficit]] establishes the shortfall; this establishes
its price and its shape. For an asker that must obtain the axes of $W$, or the
relevance variable a distillate serves, the finding constrains the *wording*
of the follow-up, not merely its existence:

1. The default follow-up — an open "anything else?" — is measured at
   approximately nothing (0.55 items, 80% of respondents adding none). A
   procedure that counts it as a completeness check is checking nothing.
2. The two active ingredients are an assertion of incompleteness and an
   attainable numeric target, and the target is a dial: ask for more, get
   more, over the range 3–9.
3. What may be supplied, and when, is measured separately for two different
   materials. **Before** generation: four sample objectives lengthened the
   list and worsened coverage (10.8 recognised-but-omitted against 7.9),
   while bare category headings — slots, not answers — cost nothing (7.9).
   **After** generation: category headings at the second stage added 3.56,
   and a recognition list exposes what was omitted, but it is a measuring
   instrument rather than an aid ([[objectives-generation-deficit]]). So the
   rule the data support is about sample answers specifically: do not supply
   them before the respondent generates.

## Known as

| Field | Name there | Same object? |
|---|---|---|
| Decision analysis (Bond et al. 2010) | direct challenge / target request | close — the authors' "direct challenge" family covers both the bare warning (deeper review, +2.77) and the numbered request (+3.08 to +4.87); this note is the numbered variant only, and the bare form is [[warning-as-debiasing]] |
| JDM debiasing | warning | close — [[warning-as-debiasing]] is the bare message with no action target; the *deeper review* condition here is that warning, and it is the weaker half of this intervention |
| Memory research | part-list (part-set) cueing | **not this** — that names the *harm* from supplying examples, a different phenomenon measured on recall of studied lists; it is invoked by the authors as an explanation, and no primary source for it was read here |
| Creativity methods | question quota | close — [[question-burst]] fixes a count of questions to produce in a fixed time; here the count is a supplement to an existing list and is measured against a completeness criterion, not a time box |

## Transfer

| | |
|---|---|
| **Home field** | a person who has just written a list of objectives for their own decision, receiving a printed or e-mailed second request |
| **Here** | an asker re-opening an axis-elicitation turn after the respondent has stopped volunteering |
| **What survives** | the ordering of the three wordings (bare re-ask ≪ warning ≪ warning + number), the monotone dependence on the target, and the null on importance — the extra items are not junk |
| **What does not** | the numbers as constants. 6.39 initial and 4.87 added belong to one decision domain with a ~30-item master list; and the preamble's claim ("people list less than 50%") is true *of this population* — an asker repeating it to a respondent for whom it has not been measured is asserting something unverified |

## Limits

- **The claim rests on one experiment's between-condition contrasts**
  (Study 3, n = 295 across six cells; roughly 50 per cell). Study 1 (n = 20)
  has no control condition, and its category effect is confounded with the
  second chance itself, as the authors say.
- **The additions are scored against the same master list that defines the
  deficit**, so "recovered" means "matched an experimenter-written candidate".
  Whether a numeric target recovers objectives *outside* the list is not
  measured.
- **The stage-one/stage-two asymmetry is untested for the same material.**
  No condition in this paper offered *sample objectives* at the second stage:
  Study 3's six second requests are review, deeper review, add three/six/nine
  and categories, and the examples manipulation is Study 2's initial stage
  only. That examples would help after generation and hurt before it is this
  wiki's inference from two separate designs, not a measured contrast.
- **Compliance is not comprehension.** The add-nine condition asked for nine
  and got 4.87; the $\beta = 0.30$ slope means most of the request is not met.
  Nothing here says what happens above nine, or whether a target large enough
  to close the ~50% gap would still yield important items.
- **The warning's content is an empirical claim about the audience.** It
  worked partly by being credible; an asker that issues it to a respondent
  who rejects it has an untested intervention.
- No source here runs any of this with a machine asker or in dialogue; the
  transfer to a conversational turn is this wiki's.

## Related

[[objectives-generation-deficit]] · [[warning-as-debiasing]] · [[question-burst]] · [[unknown-unknowns]] · [[five-whys]] · [[distillation-input-debt]]

[^s1]: bond-2010
