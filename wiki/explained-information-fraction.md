---
description: "EIF divides an explanation's certified mutual-information bound by the model's own predictive information; conditioning on correct answers separates explanation fidelity from prediction error."
aliases: ["EIF", "EIFcond", "conditional EIF", "explained information fraction"]
sources: ["arxiv-2512-11614"]
---
# Explained information fraction

The explained information fraction (EIF) asks what share of a model's own predictive information an explanation certifies. It is "the ratio of the certified mutual information" lower bound "to the empirical mutual information of the baseline model."[^c1] The numerator is the bound from the [[merlin-arthur-protocol]]. The denominator is approximated from the model's coverage C, the mass of inputs it answers correctly, through I ≈ 1 − H_b(C). The paper says this approximation "holds specifically in our setting."[^c2]

The authors call EIF "an information-theoretic analogue to the coefficient" "of determination." R² is the share of variance a regression explains. EIF is the share of the classifier's predictive signal "captured by the explanation features."[^c3]

Why condition. When the base model is weak, a low certified bound can reflect the model's error rather than a poor explanation. The paper says "In such cases, poor explanation scores may reflect model" error, and on noisy or hard benchmarks this is common.[^c4] The fix is to restrict the evaluation: "we restrict evaluation to the inputs on which Arthur produces reliable predictions." Completeness and soundness errors are then computed over correctly predicted inputs, which gives EIF_cond ≈ 1 − H_b(ε_eff), where ε_eff ≈ ε̃_c + ε̃_s/(1 − ε̃_c + ε̃_s), with the tilde marking the conditioned errors.[^c5] Conditioning on the answered region is the same move that selective risk makes for abstaining systems (my reading; see [[abstention]]).

What the numbers look like. The paper reports that the conditional score improves "EIFcond by 0.1-0.4 over instructed LLMs" and by 0.33 to 0.38 over vanilla training.[^c6] The arithmetic gives a sense of scale. With 90 percent completeness and soundness on a balanced binary label, the certified bound is about 0.28 bits. At 90 percent model coverage the denominator is about 0.53 bits, and the paper gives "EIF = 0.52."[^c7] My arithmetic: at coverage 0.6 the denominator falls to about 0.03 bits, so the same certified bound would yield an EIF near 9.

## Limits

- The denominator is an approximation that the paper says holds for its setting. It uses the binary framing of the answer and an accuracy-based coverage, so EIF inherits the error of that estimate.[^c2]
- The numerator is a lower bound, so the reported EIF values are lower bounds too. The paper calls its numbers "conservative," which is a statement about the bound, not a measured fidelity.[^c8]
- The denominator shrinks as the model gets less accurate. The arithmetic above shows EIF can rise when the model gets worse, with the explanation unchanged. The conditional version avoids this partly, but it does so by discarding the inputs the model gets wrong (my inference).
- The conditional score measures fidelity only on inputs the model already answers correctly. It says nothing about explanations on wrong answers, which is the region where a faithfulness check would matter most (my inference).
- The authors' own caveat applies: "While high accuracy does not guarantee entropy flow from context to answer."[^c9]
- The slices read do not compare EIF with other faithfulness metrics, so its advantage over them is not established here.

## Related

- [[merlin-arthur-protocol]] — the certified bound in the numerator
- [[mutual-information]] — the quantity that both numerator and denominator estimate
- [[abstention]] — conditioning on the answered region is the selective-risk move
- [[supported-faithfulness-score]] — a verifier-based claim-level faithfulness score; EIF is information-theoretic and does not use a verifier (my reading)

[^c1]: arxiv-2512-11614 — "We define EIF as the ratio of the certified mutual information"
[^c2]: arxiv-2512-11614 — "holds specifically in our setting"
[^c3]: arxiv-2512-11614 — "captured by the explanation features"
[^c4]: arxiv-2512-11614 — "In such cases, poor explanation scores may reflect model"
[^c5]: arxiv-2512-11614 — "we restrict evaluation to the inputs on which Arthur produces reliable predictions"
[^c6]: arxiv-2512-11614 — "EIFcond by 0.1-0.4 over instructed LLMs"
[^c7]: arxiv-2512-11614 — "would almost double this value to EIF = 0.52"
[^c8]: arxiv-2512-11614 — "The numbers reported in this paper are thus conservative"
[^c9]: arxiv-2512-11614 — "While high accuracy does not guarantee entropy flow from context to answer"
