---
description: "In Bayesian testing, severity lives in the choice of hypotheses: specific, contrastive predictions raise the expected absolute log-Bayes factor, so a test is likelier to give strong evidence."
aliases: ["Bayesian severity", "risky predictions", "specific hypotheses", "expected evidential value"]
sources: ["dongen-2022"]
---
# Specificity and contrastivity in hypothesis tests

A Bayes factor looks only at the data actually observed, so after the fact it cannot tell a severe test from a lenient one. The paper agrees with this and moves severity elsewhere: "the proper place for severity in statistical inference is in the choice of the tested hypotheses (are they specific? are they sufficiently contrastive?), and in the experimental design."[^c1]

## Mechanism

Two design questions are asked before data exist. Evidential value asks whether it is probable that the experiment yields strong, discriminatory evidence. Error control asks whether the design limits the probability of misleading evidence.[^c2] Two properties of the hypotheses feed these. Specificity: do H0 and H1 "rule out, or make implausible, a large proportion of possible outcomes?" Contrastivity: are their predictions different enough that the experiment can discriminate between them?[^c3]

Specificity can be read off the prior predictive distribution. Outcomes outside a hypothesis's core predictions count as inconsistent with it, and a test is severe only if those excluded outcomes include plausible ones, not only possible ones. A theory that can fit any data gives a meaningless fit.[^c4] Strong support needs a narrow range of consistent values, data inside that range, and precise measurement.[^c5]

The quantity is the expected absolute log-Bayes factor over the prior predictive of the data. Values near zero mark uninformative tests, where the hypotheses predict similarly.[^c6] More restrictive hypotheses have higher expected evidential value: it is easier to find evidence against them when false and for them when true. A point null is typically, though not always, the most severely testable hypothesis.[^c7]

A hypothesis cannot be tested alone. Declaring it refuted because data fall outside its core predictions repeats Fisher's disjunction and the inverse-probability fallacy; "A theory must always be tested against a competitor."[^c8] This is the reason contrastivity is a separate requirement.

## For asking

The practical reading (mine, not the paper's): a question is worth more when its candidate answers predict different, narrow outcomes. A vague hypothesis, or two hypotheses that predict alike, make the expected information of the answer near zero before anyone looks.

## Limits

- The paper argues conceptually and with a fictitious binomial PTSD-treatment example; it reports no empirical test that severity-aware designs find truth more often.
- It criticizes Vanpaemel for not saying how many plausible outcomes must be excluded and for leaving "plausible" unreconciled with the model's data prior; the paper does not settle either.[^c9]
- The expected absolute log-Bayes factor is contested: it is infinite when H0 logically excludes an outcome and ignores prior probabilities of the hypotheses (Nelson 2005, as recounted here).[^c10]
- It is a design-stage quantity and depends on the encompassing model and priors chosen; the paper's claim that error-statistical severity is flawed is not examined here.
- The application to questions asked by language models is my inference and untested.

## Related

- [[evidence-gap-agent]] — asks to close an evidence gap; this note says which hypotheses make an answer informative

[^c1]: dongen-2022 — "proper place for severity in statistical inference is in the"
[^c2]: dongen-2022 — "Evidential Value Is it probable to obtain strong, discriminatory evidence from this particular experiment?"
[^c3]: dongen-2022 — "Contrastivity Are the predictions of hypothesis H0 and H1"
[^c4]: dongen-2022 — "if a theory did not constrain possible outcomes, the fit is"
[^c5]: dongen-2022 — "These three criteria can be summarized as specificity of"
[^c6]: dongen-2022 — "values close to Ey |log BF10 | = 0 constitute uninformative"
[^c7]: dongen-2022 — "Testing simple, restrictive hypotheses is thus valuable"
[^c8]: dongen-2022 — "A theory must always"
[^c9]: dongen-2022 — "specification of how many plausible outcomes, relative to"
[^c10]: dongen-2022 — "lack of sensitivity to"
