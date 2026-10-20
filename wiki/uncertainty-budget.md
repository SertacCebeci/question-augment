---
description: "The prescribed alternative to a hedge word: residual uncertainty as an VIM3 (JCGM 200:2012, 2.33) defines an **uncertainty budget** as a \"statement of a measurement uncertainty,"
aliases: ["uncertainty budget", "measurement uncertainty budget"]
sources: ["jcgm-2008", "jcgm-2012-vim"]
---
# Uncertainty budget

> The prescribed alternative to a hedge word: residual uncertainty as an
> itemised list of components, each with a number and a named basis, combined
> by a stated rule and reported with the multiplier that was used — so a
> reader can undo the expansion and re-combine it with their own.

## Definition / Mechanism

VIM3 (JCGM 200:2012, 2.33) defines an **uncertainty budget** as a "statement[^s1][^s2]
of a measurement uncertainty, of the components of that measurement
uncertainty, and of their calculation and combination", and its NOTE fixes
the required contents: the measurement model, the estimates and uncertainties
of every quantity in it, covariances, the type of probability density
function applied, degrees of freedom, the *type of evaluation* used for each
component, and any coverage factor.

The GUM (JCGM 100:2008, clause 8) gives the procedure:

1. **Write the model.** $Y = f(X_1,\dots,X_N)$, containing "every quantity,
   including all corrections and correction factors, that can contribute a
   significant component of uncertainty" (4.1.2).
2. **Evaluate each component.** A standard uncertainty $u(x_i)$ for every
   input, by statistical analysis of repeated observations (Type A, 4.2) or
   by any other means (Type B, 4.3 — [[type-b-evaluation]]). The candidate
   sources are enumerated in advance: GUM 3.3.2 lists ten, from incomplete
   definition of the measurand to finite instrument resolution.
3. **Combine.** $u_c^2(y)=\sum_i (\partial f/\partial x_i)^2 u^2(x_i)$
   (equation 10), the *law of propagation of uncertainty*; the partial
   derivatives are sensitivity coefficients $c_i$ (5.1.3), and correlated
   inputs need covariances (5.2).
4. **Expand.** $U = k\,u_c(y)$ (equation 18), $k$ usually 2 to 3. GUM 6.3.3:
   $k=2$ gives a level of confidence of approximately 95 % only *when* the
   distribution is approximately normal and the effective degrees of freedom
   of $u_c(y)$ are of significant size.
5. **Report.** List all components and document fully how each was evaluated
   (7.1.4 b); state the value of $k$, the approximate level of confidence,
   and **how it was determined** (7.2.3 d, e).

Two clauses carry most of the weight for this wiki. GUM 6.2.3 states that
multiplying $u_c$ by a constant "provides no new information but presents the
previously available information in a different form" — the expansion is
presentation, the budget is the content. And the NOTE to 3.3.7 requires that
$k$ "is always to be stated, so that the standard uncertainty of the measured
quantity can be recovered for use in calculating the combined standard
uncertainty of other measurement results that may depend on that quantity":
the report is built to be **taken apart again** by whoever uses the answer
next. GUM 7.1.4 makes that the acceptance test of a report — "Have I provided
enough information in a sufficiently clear manner that my result can be
updated in the future if new information or data become available?"

## Known as

| Field | Name there | exact / close |
|---|---|---|
| Metrology — vocabulary (VIM3 2.33) | uncertainty budget | exact — the definitional home of the term |
| Metrology — the GUM | the detailed report of clauses 7.1.4 and 7.2.7 (each input estimate, its standard uncertainty, and how it was obtained) | close — the same object described as a reporting obligation rather than named |

Not this concept: the **expanded uncertainty** $U$ and the **coverage factor**
$k$ are an output and a parameter of the budget, not names for it (GUM 6.2.1);
the **combined standard uncertainty** $u_c$ is the budget's single-number
summary, which 6.2.3 says adds nothing the components did not already hold.

## Why it matters

On stall 10 the wiki's existing vocabulary for residual uncertainty is a
single number to be calibrated ([[calibration]]), a binary exit
([[abstention]]) or a word ([[verbal-probability-expressions]]). The budget is
a fourth thing, and it is the one an inter-organisational standard actually
*prescribes*: the GUM is issued by the JCGM for its member organisations
(BIPM, IEC, IFCC, ILAC, ISO, IUPAC, IUPAP, OIML) and VIM3 gives the term a
definitional entry, so for any measurement result the residual is required to
be **composed**, its parts individually attributable, judgement-derived parts
listed beside statistical ones, and the statement written in a form a
downstream user can decompose and reuse (3.3.7 note, 7.1.4). A hedge cannot be
re-combined; $u_c$ with a stated $k$ can. This is also what makes over- and
under-statement auditable: disagreement about an answer's uncertainty becomes
disagreement about a named line, not about a mood.

## Transfer

| | |
|---|---|
| In its home field | a measurand with a written functional model, input quantities carrying values and distributions, first-order Taylor propagation, and a result that is a number with a unit |
| Here | an answer whose residual uncertainty is reported as an enumerated list of contributions with a declared combination rule and a stated multiplier |
| What survives | the enumeration requirement and the equal standing it forces on judgement-derived components; the obligation to state the multiplier so the unexpanded quantity is recoverable; the updatability test of 7.1.4 as the criterion for whether a report is finished |
| What does not | the arithmetic. Equation (10) needs partial derivatives of a written $f$ and independence (or covariances); an answer in prose has no $f$, so $u_c$ is not computable and the budget transfers as a bookkeeping discipline, not as a calculation. The coverage reading goes with it: $k=2 \approx 95\%$ rests on approximate normality and effective degrees of freedom (6.3.3), neither of which is defined for a verbal answer |

## Limits

- **Prescribed is not observed.** Both sources read here are normative: the
  GUM states the duty and VIM3 defines the term; neither measures whether
  laboratories in fact produce budgets or comply with the reporting clauses.
  The claim above is therefore about what a standard requires, not about
  practice — the compliance question (ISO/IEC 17025:2017 and ILAC-G8's
  requirement to state a decision rule, and audits of it) is logged as a gap,
  not answered here.
- **The budget is complete only over effects someone thought of.** GUM 3.3.2
  closes its list with the observation that an unrecognized systematic effect
  "cannot be taken into account in the evaluation of the uncertainty of the
  result of a measurement but contributes to its error". The claim above —
  that a composed statement is better than a scalar — therefore rests on the
  enumeration being adequate, which is a stall-1 problem (Axes) this
  note does not solve.
- 3.4.7: blunders in recording or analysing data are explicitly out of scope —
  "measures of uncertainty are not intended to account for such mistakes".
  3.4.8 adds that the framework "cannot substitute for critical thinking,
  intellectual honesty and professional skill".
- The GUM is a consensus standard, not an experiment: nothing cited here
  measures whether budgeted intervals cover better than unbudgeted ones. Its
  own defence of realistic rather than "safe" evaluations is argued in Annexes
  E.2 and E.3, which this note did not read.
- Degrees of freedom and the Welch–Satterthwaite construction (Annex G) are
  not read here, so the note cannot say when $k=2$ is unsafe, only that the
  GUM makes it conditional.
- Reading an answerer's grounds for doubt as "input quantities" is this
  wiki's analogy; the Transfer row names the half that does not carry.

## Related

[[type-b-evaluation]] · [[guard-band]] · [[calibration]] · [[abstention]] · [[verbal-probability-expressions]] · [[uncertainty-decomposition]]

[^s1]: jcgm-2008
[^s2]: jcgm-2012-vim
