---
description: "Quickest change detection fixes a false-alarm budget and minimises detection delay; Lorden's worst-case and Pollak's conditional delay are different criteria, and one threshold trades the costs."
aliases: ["quickest change detection", "sequential change detection", "WADD and CADD"]
sources: ["tartakovsky-2021"]
---
# Detection delay versus false alarm

Quickest change detection (QCD) watches a stream whose law switches from $f_0$ to $f_1$ at an unknown time and asks for a stopping time that alarms soon after the switch without alarming before it.[^c1] A single threshold sets both costs at once: a larger threshold gives fewer false alarms and a longer delay, and a smaller one the reverse.[^c2] The survey's own example is a mean shift from 0 to 0.1 that cannot be seen by eye in the samples, caught by a [[cusum]] statistic that hovers near zero before the change and drifts upward after.[^c3] Lowering the threshold to $b=1$ detects sooner but, in that run, raised a false alarm at $k=112$.[^c4]

## Two ways to price the false alarm, two ways to price the delay

In the non-Bayesian setting the change time is an unknown constant. False alarms are priced by the average run length to false alarm, $E_\infty[\tau]$, and its reciprocal, the false-alarm rate; the constraint set is all stopping times with rate at most $\alpha$.[^c5] (See [[run-length]] for how this "run length" differs from the windows other literatures call by that name.)

Delay has two standard measures, and they are not the same quantity:

- Lorden's worst-case average delay takes the supremum over change times of the essential supremum over pre-change histories. The survey calls this a pessimistic measure because it considers the worst-case pre-change samples.[^c6]
- Pollak's conditional average delay, $\sup_n E_n[\tau-n\mid\tau\ge n]$, is never larger than Lorden's and is the less pessimistic one.[^c7]

Page's CUSUM is exactly optimal for Lorden's problem for every $\alpha>0$, in a slightly modified form.[^c8] With threshold $b=|\log\alpha|$ it is first-order asymptotically optimal for both criteria: delay approaches $|\log\alpha|/D(f_1\|f_0)$ as $\alpha\to0$, where $D$ is the [[kl-divergence]] between post- and pre-change laws.[^c9] That quantity is the floor: Lai's lower bound for Pollak's delay shows no procedure in the class does better to first order.[^c10]

## Why accumulation beats the single-sample rule

The Shewhart chart alarms when one observation's log-likelihood ratio crosses a threshold. It is optimal for a different criterion, the probability of detecting at the instant of the change, but it ignores past observations when deciding, and so loses on the delay-versus-false-alarm criterion, especially for small shifts.[^c11] Which criterion is chosen therefore decides which procedure is "optimal".

The Shiryaev–Roberts procedure sits beside CUSUM: where CUSUM maximises over the unknown change time (a maximum-likelihood plug-in), SR replaces the maximum by a sum of likelihood ratios.[^c12] It is also asymptotically optimal, with threshold $1/\alpha$, with a constant correction $\xi$ to the delay.[^c13] The Bayesian variant instead gives the change time a prior and trades average delay against probability of false alarm.[^c14]

## Limits

- Everything above assumes i.i.d. observations with known $f_0$ and $f_1$; the survey treats dependence and unknown post-change laws as extensions, which this note does not cover.
- Asymptotic optimality is as $\alpha\to0$; the note says nothing of finite-$\alpha$ behaviour beyond CUSUM's exactness for Lorden's criterion.
- Whether any question-asking system has a stream with a defined likelihood ratio is not shown by this source. Any reading of "asker watches answers drift" as QCD is this wiki's inference, not the survey's.
- The survey's change-in-mean figure is a single sample path, an illustration, not a measurement.

## Related

- [[cusum]] — the procedure whose optimality here is stated
- [[sprt]] — the fixed-law sequential test the likelihood ratio comes from
- [[likelihood-ratio]] — the statistic every procedure above accumulates or thresholds
- [[run-length]] — ARL as the false-alarm measure
- [[e-detector]] — a rival procedure with a different guarantee

[^c1]: tartakovsky-2021 — "the aim is to detect a possible change in the data generating distribution of a sequence of observations"
[^c2]: tartakovsky-2021 — "A larger threshold incurs"
[^c3]: tartakovsky-2021 — "such a small mean shift cannot be detected through"
[^c4]: tartakovsky-2021 — "we set a lower threshold, for instance b = 1, we can detect"
[^c5]: tartakovsky-2021 — "the average run length (ARL) to false"
[^c6]: tartakovsky-2021 — "detection delay since it considers the worst-case pre-change"
[^c7]: tartakovsky-2021 — "Pollak’s formulation is less pessimistic."
[^c8]: tartakovsky-2021 — "is exactly optimal for (9) for all α > 0."
[^c9]: tartakovsky-2021 — "It can be shown that the CUSUM procedure with a threshold"
[^c10]: tartakovsky-2021 — "Lai in [96] proved the lower bound to"
[^c11]: tartakovsky-2021 — "observations in making a decision about the change"
[^c12]: tartakovsky-2021 — "In the SR procedure, the maximum"
[^c13]: tartakovsky-2021 — "where ξ is a constant that can be characterized using the"
[^c14]: tartakovsky-2021 — "the change-point is assumed to follow a certain distribution."
