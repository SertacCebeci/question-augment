---
description: "Coherence, correctness under the governing law and stabilization are three separate premises; coherence alone supports the forecasting meaning of probability but no frequency claim."
aliases: ["Role Separation Principle", "coherence versus frequency", "two roles of probability", "coherence and frequency separation"]
sources: ["doi-10-48550-arxiv-2609-04115"]
---
# Coherence–frequency role separation

Probability is asked to do two jobs. As a forecast it is a conditional assessment: a value fixed by the information available at issue, optimal under a proper loss, and internally consistent under an assessment law Q. As the basis of an empirical claim it must also deliver a frequency: that long-run averages behave the way the probability says, under the law P that governs the data and a declared repetition regime. The paper's point is that these are different premises, and the first does not supply the second. It opens by saying that "Probability plays two distinct roles in modern data-analytic practice".[^c1]

The mechanism is a chain of three premises, each adding what the one before lacks. Internal coherence under Q makes a forecast a conditional assessment. The paper says it "provides an interpretation of probability as conditional assessment", and that it "does not establish evaluation-law correctness, specify repetition, or ensure that empirical averages stabilize".[^c2] The second premise is conditional-mean correctness under the governing law P, the same identity with P in place of Q. It makes the innovations (outcome minus forecast) P-martingale differences, so that "forecast errors cancel on average along a P-typical trajectory". The paper calls this validity in the large. It is the most that coherence plus correctness can give: it does not yield [[calibration]] over rich checking classes, and it does not yield a limit for the empirical average.[^c3] A specified frequency guarantee needs a third premise, the target-specific reference and stability conditions, which the paper packages as a [[reference-structure]].

The paper writes the combined implication schematically: conditional-mean correctness plus a target-specific reference and stability condition, under a declared repetition regime, gives a specified frequency guarantee. Coherence sits upstream of that implication as the interpretation layer. The useful reading is that a coherent forecast is the right thing to say given what was used to make it; whether any repetition makes it come true in the long run is a separate question.

Two separation results make the gap precise. First, a proper coarsening of the limiting-frequency law need not identify the governing law. Within the exchangeable class the single-atom probability P(L = p) can be shared by distinct laws, so one realized limit does not fix the law: "can be shared by distinct exchangeable laws".[^c4] Second, conditional correctness does not force stabilization. The paper builds a non-degenerate law under which the forecasts are conditionally correct and the average fails to converge almost surely: "Thus conditional-mean correctness and validity in the large do not imply stabilization".[^c5] The mechanism is that innovations can cancel while the predictable drift keeps moving, which is what the [[reference-drift-decomposition]] isolates.

Exchangeability is the one setting the paper proves outright in which the premises line up: "Exchangeability aligns forecasts and frequency", so a conditionally correct forecast is a mixture-based object whose limit is the frequency.[^c11] Outside it, the paper's message is that "Frequency meanings, however, require more than coherence", so each frequency claim has to be earned by naming its reference structure. That last step is this note's reading of the paper rather than a quoted result.[^c12]

## Limits

- The results are stated for countably additive probability. The paper notes that "throughout we use countably additive probability", although coherence is often discussed in finitely additive terms.[^c6]
- The separation results are logical, not empirical. "Both results are logical rather than empirical." They show that the gap can exist, not how often real systems fall into it, and "Neither result suggests that nonconvergence is typical."[^c7]
- The feedback example is a stylised simulation: "We include a stylized reinforcement-learning (RL) simulation in a one-state, two-action environment." The infinite-horizon claim rests on a separate construction in an appendix, not on measured deployments.[^c8]
- The synthesis is deliberately not new mathematics: "This novelty is deliberately synthetic."[^c9] The novelty claimed is the unified account of when coherence can be read as a frequency guarantee.
- The paper does not establish a universal cause for the failures it links to AI reliability: "do not establish a universal empirical cause or remedy."[^c10]

## Related

- [[reference-structure]] — the third premise: what is held fixed under repetition
- [[reference-drift-decomposition]] — where the reference structure enters the stabilization argument
- [[calibration]] — a frequency property that needs the second and third premises, not the first alone
- [[conformal-prediction]] — its guarantee rests on exchangeability, a reference structure that these premises would need stated

[^c1]: doi-10-48550-arxiv-2609-04115 — "Probability plays two distinct roles in modern data-analytic practice"
[^c2]: doi-10-48550-arxiv-2609-04115 — "Internal coherence provides an interpretation of probability as conditional assessment"
[^c3]: doi-10-48550-arxiv-2609-04115 — "forecast errors cancel on average along a P-typical trajectory"
[^c4]: doi-10-48550-arxiv-2609-04115 — "can be shared by distinct exchangeable laws"
[^c5]: doi-10-48550-arxiv-2609-04115 — "Thus conditional-mean correctness and validity in the large do not imply stabilization"
[^c6]: doi-10-48550-arxiv-2609-04115 — "throughout we use countably additive probability"
[^c7]: doi-10-48550-arxiv-2609-04115 — "Both results are logical rather than empirical."
[^c8]: doi-10-48550-arxiv-2609-04115 — "We include a stylized reinforcement-learning (RL) simulation in a one-state, two-action environment"
[^c9]: doi-10-48550-arxiv-2609-04115 — "This novelty is deliberately synthetic."
[^c10]: doi-10-48550-arxiv-2609-04115 — "do not establish a universal empirical cause or remedy"
[^c11]: doi-10-48550-arxiv-2609-04115 — "Exchangeability aligns forecasts and frequency"
[^c12]: doi-10-48550-arxiv-2609-04115 — "Frequency meanings, however, require more than coherence"
