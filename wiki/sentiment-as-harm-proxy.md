---
description: "Bias tests often read harm off the sentiment of text about a group, a proxy that misses positive-but-harmful stereotypes and whose link to harm is rarely examined."
aliases: ["sentiment-based bias measure", "sentiment gap between groups"]
sources: ["doi-10-48550-arxiv-2305-12757"]
---
# Sentiment as a proxy for harm

A common way to operationalise a bias test is to generate text about a group and compare sentiment. The paper counts 23 of its 90 bias tests (26 per cent) that "operationalise bias by checking whether generated text referencing marginalised groups yields lower sentiment than text not referencing such groups."[^c1] The score is a difference in sentiment: if text about one group is more negative, the test reports bias.

The mechanism assumes that negative sentiment about a group is the harm. The authors note that this link is seldom checked: "The link between low sentiment and harm is rarely explored, but left unexamined; a threat to predictive validity."[^c2] The assumption fails in both directions. A sentence can carry a stereotype and still read as positive. The paper's example is that "GROUP likes partying will yield positive sentiment but potentially negative regard."[^c3] So a sentiment score can rate a harmful stereotype as favourable, and the test then reports no bias.

The paper offers regard as the replacement. Sheng et al. (2019) "introduce the concept of regard as a more sensitive measure of attitudes towards a marginalised group."[^c4] Regard is scored by a single classifier, and that fixed instrument is what makes regard-based tests comparable across papers. The same fixity is the weakness the paper flags: once a paper's domain departs from what the classifier was built for, validity erodes.[^c5] The contrast is the one in [[validity-reliability-tradeoff]].

The sentiment measure is not useless. The authors note that sentiment and toxicity "have the advantage of having many available classifiers in different languages," which makes them the practical choice for multilingual work, at a reliability cost once the classifiers differ or are updated.[^c6]

A concrete failure of this kind appears in the paper's own review. Where a sentiment comparison was used without defining the harm, the paper found it unclear whether the comparison measured the harm at all.[^c7] That is a content-validity mismatch in the sense of [[measurement-modelling]]: the conceptualisation names a harm, and the operationalisation measures a different quantity.

## Limits

- The 23-of-90 count comes from one annotated taxonomy, and the paper does not report how many of those tests checked the sentiment-harm link themselves.
- The argument that sentiment is a poor proxy for harm is the authors' argument, drawn from the regard literature. The paper does not measure how often sentiment and harm diverge on generated text, so the size of the failure is unknown here.
- Regard's own validity is not evaluated in this work; the paper notes only that its comparability holds while the domain stays fixed.
- The paper's critique concerns bias tests. Whether the same holds for sentiment used as a quality signal in other tasks is not addressed.

## Related

- [[measurement-modelling]] — the framework in which this is a content-validity mismatch between a named harm and a measured sentiment.
- [[validity-reliability-tradeoff]] — the regard-versus-sentiment contrast is the paper's instance of the tradeoff.
- [[metric-criterion-decoupling]] — the same pattern at the level of NLG papers: a metric chosen without its named criterion.

[^c1]: doi-10-48550-arxiv-2305-12757 — "operationalise bias by checking whether generated text referencing marginalised groups yields lower sentiment than text not referencing such groups."
[^c2]: doi-10-48550-arxiv-2305-12757 — "The link between low sentiment and harm is rarely explored, but left unexamined; a threat to predictive validity."
[^c3]: doi-10-48550-arxiv-2305-12757 — "GROUP likes partying will yield positive sentiment but potentially negative regard."
[^c4]: doi-10-48550-arxiv-2305-12757 — "introduce the concept of regard as a more sensitive measure of attitudes towards a"
[^c5]: doi-10-48550-arxiv-2305-12757 — "validity is increasingly threatened"
[^c6]: doi-10-48550-arxiv-2305-12757 — "sentiment and toxicity have the advantage of having many available classifiers in different languages"
[^c7]: doi-10-48550-arxiv-2305-12757 — "without defining the anticipated harm, it is unclear if comparing sentiment is an appropriate measure of that harm"
