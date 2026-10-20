---
description: "Two choice objects are comparable only **with respect to** some Walasek & Brown (2023) define a **covering value** as \"a value that provides a context-specific common currency that enables comparis…"
aliases: ["no common currency of value", "no universal value scale", "value incommensurability"]
sources: ["arrow-1951", "walasek-2023"]
---
# Value incommensurability

> Two choice objects are comparable only **with respect to** some
> context-specific value; when a choice depends on more than one such value
> at once, there is no higher scale to trade them against each other — and
> combining them by rank alone reproduces Arrow's voting paradox inside one
> mind.

## Definition / Mechanism

Walasek & Brown (2023) define a **covering value** as "a value that provides[^s1][^s2]
a context-specific common currency that enables comparison of attributes of
choice objects" — e.g. *research value* lets two job candidates' h-indices be
compared, *teaching value* lets their student ratings be compared. They
separate two properties: **comparability** is a relation between objects,
always *relative to* a named covering value; **commensurability** is a
relation between covering values themselves — whether a higher-order scale
exists that would let research value and teaching value be traded off. Their
claim is that no such higher scale generally exists: "the h-index difference
of 22 cannot be said to outweigh (or not to outweigh) the difference of 3 in
teaching rating — because there is no common covering value to enable the
trade-off to be made." Stated generally: "there is no universal value scale,
[and] incommensurable values pervade everyday choice."

They classify multiattribute choices into four types by how many covering
values are in play: none relevant (Type I), exactly one relevant (Type II),
several relevant but only one live in the current choice (Type III), and
several simultaneously relevant (Type IV). Difficulty is confined to Type IV:
"if there is just one covering value with respect to which two choice
objects differ, then no difficulty associated with trading off different
covering values arises" — attributes serving the *same* covering value (e.g.
conscientiousness and extraversion, both feeding "teaching value") can still
be weighed against each other.

**The consequence they derive.** If incommensurable covering values can only
be combined by rank (win/lose per value, not a cardinal trade rate), the
combination problem is formally the one Arrow (1951) posed for aggregating
many voters' orderings into one social ordering under unrestricted domain,
independence of irrelevant alternatives (IIA), the Pareto principle and
non-dictatorship — no rule satisfies all four for three or more alternatives.
Walasek & Brown read the several covering values relevant to one choice as
playing the role of Arrow's voters and suggest "Arrow's impossibility
theorem will also apply at the level of the individual." They demonstrate
the two Arrovian failure modes on a three-apartment example varying in rent
and two other attributes: ranking by "wins" across attributes produces an
**intransitive** triple (Apartment 1 beats 2, 2 beats 3, 3 beats 1 — Table
1), and removing one apartment from the choice set **reverses** which of the
remaining two wins (Tables 2–3), an IIA violation. Their conclusion: "preference
reversals and intransitivity are an inevitable consequence of
incommensurability" once rank-based combination is the only option.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Philosophy of value (Chang, Levi, Raz — cited by walasek-2023, not read this pass) | incommensurability of values | close — the same absence of a common scale, but the philosophical debate is about evaluative and practical reasoning generally and predates the covering-value formalisation this note is about |
| Classical political economy (Smith, Ricardo, Marx — cited by walasek-2023, not read this pass) | use value vs. exchange value | close — a historical precursor distinguishing what a thing is worth for its own sake from what a common metric (money) says it is worth; not the same formal object |

**Not this concept.** *Covering value* is the object the claim is about — the
context-specific scale within which comparison works — not a name for the
incommensurability claim itself, so it is not carried as an alias (per the
rule that a name for the operand is not a name for the concept). *Arrow's
impossibility theorem* is the imported theorem (home field: social choice
theory); naming it here would conflate the transfer target with what is
transferred — it is treated in `## Transfer`, not in this table.

## Why it matters

Selection's own unanswered question is: "Between a question on game
mechanics and one on the market loop there is no common prior and no
exchange rate." This note gives the formal reason why not. [[expected-information-gain]]
and [[value-of-information]] both score candidate questions inside one
parameterisation — one covering value, in this paper's terms (Type II). Once
more than one covering value is simultaneously live (Type IV), a numeric
score computed under one is not wrong on its own terms, but comparing it to
a score computed under another crosses a boundary neither theory claims to
bridge — there is no procedure, EIG-based or utility-based, that outputs a
single number spanning both. Walasek & Brown's own demonstration goes
further than "no common unit exists": if an asker nonetheless combines the
two rankings by counting wins, the resulting preference over candidate
questions can be intransitive and can reverse depending on which other
candidates are in the pool at the time — so the failure mode of forcing a
cross-covering-value comparison is not merely an uninformative number but an
unstable one.

## Transfer

| | |
|---|---|
| In its home field | Arrow (1951): aggregating $n \geq 3$ voters' complete orderings of $\geq 3$ social alternatives into one ordering, subject to unrestricted domain, IIA, the Pareto principle and non-dictatorship; no aggregation rule satisfies all four. |
| Here | Walasek & Brown read the several covering values simultaneously relevant to one person's one choice as playing the role of Arrow's voters, each contributing its own rank-ordering of the choice objects, combined into a single choice. |
| What survives | The impossibility structure: once options are ranked separately per covering value and combined by rank alone, the same forces that block a universally satisfying voting rule produce, on their worked example, both an intransitive triple and a menu-dependent reversal. |
| What does not | The formal correspondence is asserted, not derived: the paper does not show that Arrow's four axioms hold, or must hold, for one mind combining covering values the way they hold for separate voters combining ballots — "Arrow's impossibility theorem will also apply" is stated as an application, with no proof that the individual-choice aggregation problem satisfies Arrow's precise hypotheses. Relaxations known to weaken Arrow's conclusion in social choice (restricted/single-peaked domains) are named only as open questions for the individual case. |

## Limits

- **Not a proof.** The authors say so directly: "it is difficult to 'prove a
  negative'"; their case is that assuming incommensurability makes otherwise
  puzzling choice phenomena less surprising, not that a common scale is
  shown impossible.
- **Scope is ordinary multiattribute choice.** The paper explicitly excludes
  choice among risky gambles/lotteries and extreme philosophical trade-offs
  (rights vs. welfare, money vs. a body part); its claims should not be
  extended to those without separate support.
- **The Arrow transfer is the paper's own conjecture, not a corollary.** As
  `## Transfer` says, no derivation shows the individual case meets Arrow's
  axioms; treat the intransitivity/reversal claim as argued, not proved.
- **Which covering value governs when several are live is left open by the
  source itself**: "we must assume that any ordering is produced in some
  other way" — the paper does not supply that ordering, so this note cannot
  either (logged as a gap rather than answered here).
- `arrow-1951` is queued/unverified in `wiki/meta/sources.json` at the time
  of writing; this note relies on Walasek & Brown's restatement of Arrow's
  theorem rather than a direct reading of Arrow (1951) [?].

## Related

[[expected-utility]] · [[value-of-information]] · [[blackwell-informativeness]] · [[bounded-rationality]] · [[values-and-preferences]]

[^s1]: arrow-1951
[^s2]: walasek-2023
