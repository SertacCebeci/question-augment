---
description: "Three stopping literatures say \"run length\" for three different objects: two $R$ and $k$ are inputs and cannot be estimated from the data they will stop. $N$ *is* the stopping time."
aliases: ["run length"]
sources: ["champ-1987", "guest-2020", "nelson-1984", "page-1954"]
---
# Run length

> Three stopping literatures say "run length" for three different objects: two
> are windows the analyst fixes before any data arrives, one is the stopping
> time the rule produces. Reading the chosen one as the measured one turns a
> cost into a guarantee that was never computed.

## The name and what it covers

| Use | What it is | Chosen or measured | Member note |
|---|---|---|---|
| **Confirmation run length $R$** — [[qualitative-saturation|qualitative saturation]] (Guest, Namey & Chen, 2020) | width of the window over which new information is scored after the base; written into the result as the "+2" of $6^{+2}$ | chosen, before collection | `confirmation-run-length` (draft dropped) |
| **Runs-rule length** — Shewhart charts (Nelson, 1984, extending the Western Electric rules) | the $k$ of "$k$ consecutive points on one side of the centre line", a supplementary alarm pattern | chosen, at chart design | none yet |
| **Run length $N$, average run length (ARL)** — sequential detection and SPC (Page, 1954) | the random number of samples until the rule alarms; ARL is its expectation, in control (false alarms) or out of control (detection delay) | measured — a property of rule and process together | carried inside [[cusum]], [[e-detector]], [[scan-b-statistic]] |

## The difference, and what it costs to miss it

$R$ and $k$ are inputs and cannot be estimated from the data they will stop.[^s1][^s2][^s3][^s4]
$N$ *is* the stopping time. This wiki reads the sequential-detection quantity
as the analogue of the whole reported count $B{+}R$, not of $R$; no cited
source makes the correspondence.

The asymmetry that follows is in what each literature can say about its own
window. Champ & Woodall (1987) obtained exact run-length distributions by
Markov chain for Shewhart charts with supplementary runs rules, and showed
that the rules detect small shifts sooner only at a large cost in in-control
ARL — the plain $3\sigma$ chart's $1/0.0027 \approx 370$ samples between false
alarms falls to roughly a quarter of that once the four Western Electric rules
are added. In SPC the price of a run rule is therefore quoted as a false-alarm
rate. No [[saturation]] source read for this wiki attaches a probability that a
qualifying window is a false stop: guest-2020 recommend a longer $R$ as "more
conservative" with no rate behind it. A derivation that reads across from ARL
to $R$ and imagines it has imported the guarantee has imported nothing it can
cite.

## Why it matters

Stall 7 carries notes from both families, and the bare word appears in both.
A stopping rule for asking that speaks of "tuning the run length" is doing one
of three different things: deciding how much of the budget to spend confirming
($R$), choosing an alarm pattern ($k$), or naming a target false-alarm rate
(ARL). Only the third is a statement about error, and only the first two are
choices an asker actually makes.

## Limits

- **The missing false-stop rate for $R$ is an absence in the sources read
  here, not a proved absence in the literature.** The search behind this note
  was not exhaustive over qualitative methodology; whether anyone has computed
  the probability that an $R$-window scores below threshold before the theme
  space is exhausted — the saturation analogue of in-control ARL — is the open
  question this note leaves, and a single such computation would remove the
  asymmetry the section above rests on.
- **The identification of $N$ with $B{+}R$ rather than with $R$ is this
  wiki's reading.** If the correspondence is wrong — if the right analogue of
  the stopping time is some other functional of the saturation procedure —
  then the chosen/measured column mislabels the first row and the "imported
  nothing" conclusion loses its argument, though the three uses remain
  distinct objects.
- The three uses are uncontested inside their own fields; the collision is in
  this wiki, where saturation and change-detection notes share stall 7. The
  disambiguation is this wiki's housekeeping, not a dispute in the literature.
- ARL summarises a skewed distribution by its mean. Two rules with equal
  in-control ARL can behave very differently early on. This note uses ARL as
  the SPC member's headline quantity, the way the cited sources use it, not as
  a sufficient description of the run-length distribution.
- The exact in-control ARL under the four Western Electric rules is quoted in
  the secondary literature at slightly differing values in the low 90s; this
  note uses Champ & Woodall's qualitative result and the arithmetic $3\sigma$
  baseline rather than committing to one figure.
- The runs-rule row has no member note, so its claim rests here on a single
  reading of nelson-1984 and champ-1987 and has not been through the four
  questions on its own.

## Related

`confirmation-run-length` (draft dropped) · `early-stopping-patience` (draft dropped) · [[cusum]] · [[e-detector]] · [[scan-b-statistic]] · [[stopping-rules]]

[^s1]: champ-1987
[^s2]: guest-2020
[^s3]: nelson-1984
[^s4]: page-1954
