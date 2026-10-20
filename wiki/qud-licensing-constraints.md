---
description: "[[presupposition-accommodation|Accommodation]] stops being a stipulation when the candidate questions are"
aliases: ["QUD constraints", "information-structural constraints on QUDs", "QUD-tree annotation principles"]
sources: ["dekuthy-2018", "riester-2019"]
---
# QUD licensing constraints

> [[presupposition-accommodation|Accommodation]] stops being a stipulation when the candidate questions are
> filtered: an implicit question may be built only out of material the
> discourse has already given, and must use as much of it as possible.

## Definition / Mechanism

**Riester (2019, "Constructing QUD trees")** attacks the problem that[^s1][^s2]
identification of implicit questions "has often been dismissed as a hopeless,
or at least highly speculative, task": considered in isolation, a sentence has
as many candidate questions as it has constituents. His procedure is
segmentation of the text into atomic assertions, then, for each assertion, a
question that it answers, filtered by constraints Riester derives from the
focus literature (he cites Rooth 1992, Schwarzschild 1999, Büring 2008):

| Constraint | Statement (Riester's wording) |
|---|---|
| **Q-A-Congruence** | QUDs must be answerable by the assertion(s) that they immediately dominate |
| **Q-Givenness** | Implicit QUDs can only consist of given (or at least highly salient) material |
| **Maximize-Q-Anaphoricity** | Implicit QUDs should contain as much given (or salient) material as possible |
| **Parallelism** | The background of a QUD with two or more parallel answers consists of the (semantically) common material of the answers |
| **Back-to-the-Roots** | An incoming QUD attaches to the right of the lowest antecedent of its given content, but otherwise as high as possible |

The load-bearing asymmetry is between explicit and implicit questions: an
**explicit** question may introduce new material into the discourse, an
**implicit** one may not, because reconstructing it must not change the
discourse. Riester states that Q-Givenness is the flipside of Schwarzschild's
Givenness, which on his rendering requires discourse-new material to be
focus-marked: since the focus of an answer corresponds to the *wh*-expression
of its question, new material is banned from inside the question.

Riester is explicit about what the filter does and does not deliver. It makes
the identification task "tractable and deterministic" in the sense that
candidate questions are ruled out (his example: after *his condition was
extremely bad*, the assertion *He literally suffocated* cannot have the QUD
*Who literally suffocated?* — it would introduce *literally suffocated* as new
— and *What happened?* is ruled out for containing no given material, leaving
*How bad was his condition?*). It does **not** deliver a unique string:
synonymous formulations abound, and what is identified is a QUD "as an object
of *meaning*".

**How reproducible it is, measured.** De Kuthy, Reiter & Riester (LREC 2018)
had two trained annotators apply these principles with the *TreeAnno* tool to
two sections of an English Snowden interview transcript (60 and 69 segments)
and one German interview (158 segments). Agreement, computed as $\kappa$ over
the span-matrix method of Marcu et al. (1999): **.50, .53 and .45** —
"moderate agreement between the annotator pairs", which the authors themselves
decline to interpret further for lack of a baseline.

## Known as

| Name | Field | Relation |
|---|---|---|
| QUD constraints, QUD principles | formal pragmatics | exact — the set as a whole, as used by Riester and by De Kuthy et al. |
| information-structural constraints on QUDs | formal pragmatics | exact — Riester's own section heading for them |
| QUD-tree annotation principles | corpus linguistics | exact — the same set as an annotation guideline |
| Q-Givenness, Q-A-Congruence, Maximize-Q-Anaphoricity, Parallelism, Back-to-the-Roots | formal pragmatics | *not* this concept — individual members; each rules out a different class of candidate and none is a test on its own |
| Givenness (Schwarzschild 1999, as reported by Riester) | information structure | close — *not* this concept: a condition on focus marking in the *answer*, of which Riester says Q-Givenness is the flipside |

## Why it matters

Points 1–4 are this wiki's inferences from the two sources, not claims either
source makes; neither addresses an answerer facing a received question.

1. **The answerer gets a negative test it can run on its own reading**
   (*this wiki's transfer*). A candidate reading of a received question that
   contains material the exchange never supplied is not licensed. In
   [[question-under-discussion]] accommodation just happens; here a reading
   that invents a goal is rejected before it is answered.
2. **It prices the [[recovery-postulate|recovery]] step** (*this wiki's inference*). Two trained
   analysts working offline with an explicit manual reach $\kappa \approx .5$
   on tree structure. This wiki reads that as reason to doubt any design that
   treats "what is being asked" as recoverable to a single answer; neither
   source draws that conclusion, and the figure is agreement on spans, not on
   the question written (see *Limits*).
3. **Under-specification is the licensed direction** (*this wiki's
   inference*). Maximize-Q-Anaphoricity prefers the question carrying the most
   given material; combined with Q-Givenness, this wiki reads the licensed
   readings as sitting *below* the wording in specificity — the opposite of the
   direction an over-eager answerer elaborates in. The alignment with the
   deformation [[levels-of-information-need]] describes is this wiki's
   analogy, not Riester's or Taylor's claim.
4. **Two parallel answers determine their shared question** (*this wiki's
   inference*). Riester's Parallelism constrains the background of a QUD in a
   text being analysed; this wiki reads it as a check an answerer could run
   whenever the asker supplied more than one example, which is a use neither
   source describes or tests.

## Transfer

| | |
|---|---|
| **Home field** | offline analysis of transcribed monologue and interview text by trained linguists, with the whole text available and unlimited time per segment |
| **Here** | an answerer choosing among candidate readings of a received question, and having to justify the one it accommodated |
| **What survives** | the explicit/implicit asymmetry (a reconstructed question may not introduce new material); Q-Givenness as a rejection test; the preference for maximal given material; Parallelism as a joint constraint from two answers; the finding that trained humans agree only moderately |
| **What does not** | the offline setting and the assumption that the text is already segmented and its focus–background split determined — Riester states Q-A-Congruence applies only "once its information structure has been determined", so the constraints presuppose an analysis step this wiki has no procedure for; and the direction, which is again from assertion to question, not from a received question to the question meant |

## Limits

- The constraints filter candidates; they do not generate them, and they do not
  pick one formulation. Riester says so directly — there is no single way of
  formulating an implicit QUD.
- Q-Givenness is overruled by presupposition triggers (e.g. clefts), for which
  Riester says the approach "must be enhanced by language-specific rules";
  Parallelism can override Q-Givenness too. The filter is therefore not a
  decision procedure over arbitrary text.
- The $\kappa$ values are agreement on **whole tree structures** (whether a
  question spans each pair of segments), not on whether two analysts wrote the
  same question. They bound the reproducibility of the procedure, not its
  correctness; there is no gold standard.
- Three documents, two annotator pairs, two languages, spoken-interview genre.
- Points 1–4 in *Why it matters* are this wiki's transfer of an offline
  monologue-analysis constraint set to an answerer facing a dialogic question.
  Neither source addresses an answerer; the $\kappa$ bounds agreement on tree
  spans rather than on the question recovered, so the step from it to a ceiling
  on single-answer recovery is this wiki's; and nothing measures whether the
  filter improves a reply.
- Rooth (1992), Schwarzschild (1999) and Büring (2008) are cited here **through
  `riester-2019`** and were not read; the rendering of Schwarzschild's
  Givenness, and the claim that Q-Givenness is its flipside, are Riester's.
- `riester-2019` was read in the author's manuscript copy (University of
  Stuttgart); the published chapter is in *Questions in Discourse* Vol. 2
  (Brill, 2019), pp. 163–192.

## Related

[[question-under-discussion]] · [[qud-parsing]] · [[qud-tree]] · [[levels-of-information-need]] · [[presupposition-accommodation]] · [[recovered-question-check]]

[^s1]: dekuthy-2018
[^s2]: riester-2019
