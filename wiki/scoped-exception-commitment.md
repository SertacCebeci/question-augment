---
description: "This wiki's inference: a non-answer is a scoped object with a direction — commit on W minus a named axis when the exception factorises; else disclaim or reject the whole and assert nothing local."
aliases: ["scoped-exception commitment", "qualified answer"]
sources: ["iaasb-2015-isa705"]
---
# Scoped-exception commitment

> **This wiki's inference, not a result.** On $W$, the qualified opinion is a
> commitment on every axis but one; "pervasive" is the exception failing to
> factorise out — disclaimer in the evidence flavour, rejection in the
> finding flavour; and the piecemeal rule makes answers and non-answers
> compose in one direction only.

## The claim

Four steps; the first two are someone else's.

1. **(Attributed.)** ISA 705 (Revised) gives a professional answerer an output that commits on the whole "except for the effects of" — or "except for the possible effects of" — a described matter, reserved for effects that are material but not pervasive, where *pervasive* includes not being "confined to specific elements, accounts or items" ([[modified-opinion-matrix]]).[^c1]
2. **(Attributed.)** Under a disclaimer or adverse opinion on the whole, no unmodified opinion on a part may appear in the same report, while any further matter that would itself have modified the opinion — a misstatement or an evidence shortfall — must still be described ([[piecemeal-opinion-prohibition]]).[^c2]
3. **(This wiki.)** Let the answer be $A \subseteq W$ with $W = \prod_k X_k$ ([[possible-worlds]]) and $P \subseteq W$ the asker's premise. A *scoped-exception commitment* is $A = A_{-k} \times E_k$: full commitment on every axis but $k$, with $E_k = X_k$ where evidence on $k$ is lacking (the "possible effects" flavour) and $E_k = X_k \setminus P_k$ where the premise is found wrong there (the "effects" flavour). The exception is *confined* exactly when $A$ factorises so — when what can be said of the other axes does not depend on $x_k$. It is *pervasive* when every candidate $A_{-k}$ changes with $x_k$, and non-factorisation has one consequence per flavour: for want of evidence no commitment on the remainder exists and the matrix's inability row forces the empty answer, $A = W$; for a finding the misstatement row forces the adverse form, $A = W \setminus P$ — a full, non-empty commitment that the premise fails on the whole. Pervasiveness, so read, is structural, not a magnitude.[^c3]
4. **(This wiki.)** The direction. A local non-answer inside a global answer is admissible; a global non-answer ($A = W$) or global rejection ($A = W \setminus P$) with local unmodified assertions is forbidden; and under either, every further axis that would itself have modified the answer — premise found false or evidence lacking — must still be named. "I don't know" is thus not the pointwise flag of [[abstention]]'s selection function $g$ but a scoped object — whole or named part — composing asymmetrically with answers.[^c4]

In a derived procedure the output space becomes {answer; answer except $k$ for want of evidence; answer except $k$ because the premise fails there; reject; disclaim}, chosen by two judgements — where the defect lies, whether it factorises — with a per-question uncertainty score at most an input to the second.[^c6]

## Known as

Not a term of art; this wiki's name for the composition. "Qualified answer" is by analogy with the qualified opinion.

## Transfer

| | |
|---|---|
| In its home field | a financial-statement whole with enumerated parts; "confined" is judged against elements, accounts and items, with a magnitude test alongside |
| Here | an answer set over declared axes; "confined" becomes factorisation of $A$ along axis $k$ |
| What survives | the scoped form; the two-flavour wording (evidence vs finding); the two whole-answer forms (disclaim, reject); the composition asymmetry |
| What does not | ISA 705's tests (ii) and (iii) — "substantial proportion", "fundamental to users' understanding" — are magnitude and audience tests with no factorisation reading, so step 3 is narrower than the standard; materiality has no analogue |

[^c5]

## Limits

- **A conjecture, typed as one.** Steps 3 and 4 appear in no source.
- Step 3 needs the axes of $W$ declared before the answer — usually unavailable (Axes) — and the reject form $W \setminus P$ needs the premise itself given as a set of worlds.
- Reading "misstated" as *the asker's premise fails on axis $k$* is the wiki's mapping; in audit the misstated object is authored by a third party, and the link to [[false-premise-question]] is analogy.
- Nothing is measured: no experiment compares the five-form output space with [[abstention]]'s two.

## Related

[[modified-opinion-matrix]] · [[piecemeal-opinion-prohibition]] · [[abstention]] · [[possible-worlds]] · [[false-premise-question]] · [[constraint-as-information]]

[^c1]: iaasb-2015-isa705 — "the auditor shall state that, in the auditor’s opinion, except for the effects of the"
[^c2]: iaasb-2015-isa705 — "the financial statements as a whole, the auditor’s report shall not also include an unmodified"
[^c3]: iaasb-2015-isa705 — "Are not confined to specific elements, accounts or items of the financial statements;"
[^c4]: iaasb-2015-isa705 — "unmodified opinion in the same report in these circumstances would contradict the auditor’s"
[^c5]: iaasb-2015-isa705 — "If so confined, represent or could represent a substantial proportion of the financial"
[^c6]: iaasb-2015-isa705 — "This ISA establishes three types of modified opinions, namely, a qualified opinion, an adverse"
