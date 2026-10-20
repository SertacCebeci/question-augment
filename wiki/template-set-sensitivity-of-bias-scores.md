---
description: "Template-based bias scores move with template wording and with which templates are drawn; CALM reports small shifts under rewording and subsampling, crediting its template diversity."
aliases: ["template perturbation sensitivity", "template-subset sensitivity of bias benchmarks", "template robustness of bias measures"]
sources: ["doi-10-48550-arxiv-2308-12539"]
---
# Template-set sensitivity of bias scores

A template-based bias benchmark fills one sentence frame with a name or pronoun from each social group and compares the model's accuracy across groups. The reported number therefore depends on the frames as well as on the model. Selvam et al. showed that "seemingly innocuous perturbations such as synonym substitution, can significantly impact bias scores and change the" relative ordering of models in earlier benchmarks.[^c1]

CALM's response changes where the frames come from. Its authors did not write them by hand: they took templates from sixteen existing question-answering, sentiment and natural-language-inference datasets, kept those containing person names or pronouns, and replaced the names with placeholders.[^c2] Their stated aim was to address the reliability problem "by selecting templates from a diverse set of existing dataset, in place of manually designing" them.[^c3] The working hypothesis was that "a template-based approach for measuring bias could be developed" that would be "robust and reliable through greater diversity of templates."[^c4]

## What was perturbed, and what moved

The sensitivity test rebuilt the templates in three ways: "them through synonym substitution, addition of clauses, and addition of adjectives."[^c5] The perturbed constructions made a dataset five times the size of CALM. Across five language models, "CALM showed minimal sensitivity to these semantic perturbations, with a maximum" variance "of less than 10% across all models."[^c6] The comparison figures for earlier datasets are taken from Selvam et al. rather than rerun: "BiasNLI (Dev et al., 2020) showed a 70% variation in bias score, dropping from 41.6 to 13.4."[^c7]

The subset test drew random proportions of prompts, "with a different proportion of randomly selected prompts (75%, 50%, and 25%)," over six runs and four models. The authors report that "CALM exhibits only minimal deviations in these" conditions.[^c8] The same paper cites Selvam et al. for the opposite case, in which "subset selection can produce as much as a 40% change in bias measurement."[^c9]

Template diversity was measured by the average BERTScore between template pairs, where a lower value means less semantic overlap. CALM has "the lowest average BERTScore of 0.388, indicating lower" similarity, against values such as "UnQOVER (0.660), BITS (0.617), and BEC-PRO (0.594)."[^c10] The authors attribute the stability to "larger size and greater diversity of CALM prompts."[^c11]

## Averages hide template-level spread

The paper observes two things at once. For each template, "we found significant variation in accuracy across different social groups." Yet across the whole template set, "the accuracy for each social group over all templates varies within a narrow range of 0-3%."[^c12] My inference: a stable average over templates can sit on top of large per-template swings. A claim that the benchmark is robust is a claim about the average. Whether a single template drives a group difference is a separate question, which the paper answers only for one model (Table 5).

## Limits

- The perturbations are the authors' own (synonym, clause and adjective edits), applied to five models in the sensitivity test. The comparison numbers come from a different benchmark and a different study, so "less sensitive" is a comparison of reported figures, not of matched experiments.[^c13]
- The template pool was not produced purely by filtering. After automatic extraction, "we manually verified each template, which led to discarding examples such as" stories with animal characters.[^c14] Human selection is reduced, not removed.
- Diversity is measured by BERTScore and length. The paper does not test whether low BERTScore predicts low sensitivity; the link from diversity to stability is the authors' attribution. Size and diversity are not separated by any ablation (my inference).
- The subset test resamples prompts from one fixed pool; it does not test templates drawn from a different distribution or domain.
- The authors state a belief, not a result, that "models having lower CALM bias scores are likely to exhibit" reduced bias in practice.[^c15]
- The templates are English only: "the templates used in our dataset are in English."[^c16]

## Related

- [[multi-seed-bias-score-averaging]] — the same worry for generation seeds: single runs scatter, which is a different source of instability from template wording.
- [[answer-format-dependent-bias-measurement]] — answer format is another part of the instrument that changes scores and even model rankings.
- [[rule-gated-behavior-gate]] — resampling by template family, not by task, because tasks share templates; the unit that keeps uncertainty honest.
- [[baseline-relative-group-deviation-score]] — the per-template score that these template sets are fed into, and how that score is aggregated.

[^c1]: doi-10-48550-arxiv-2308-12539 — "seemingly innocuous perturbations such as synonym substitution, can significantly impact bias scores and change the"
[^c2]: doi-10-48550-arxiv-2308-12539 — "NLP tasks, question answering, sentiment and natural language inference, from sixteen"
[^c3]: doi-10-48550-arxiv-2308-12539 — "selecting templates from a diverse set of existing dataset, in place of manually designing"
[^c4]: doi-10-48550-arxiv-2308-12539 — "that would be robust and reliable through greater diversity of templates."
[^c5]: doi-10-48550-arxiv-2308-12539 — "them through synonym substitution, addition of clauses, and addition of adjectives."
[^c6]: doi-10-48550-arxiv-2308-12539 — "CALM showed minimal sensitivity to these semantic perturbations, with a maximum"
[^c7]: doi-10-48550-arxiv-2308-12539 — "BiasNLI (Dev et al., 2020) showed a 70% variation in bias score, dropping from 41.6 to 13.4;"
[^c8]: doi-10-48550-arxiv-2308-12539 — "CALM exhibits only minimal deviations in these"
[^c9]: doi-10-48550-arxiv-2308-12539 — "subset selection can produce as much as a 40% change in bias"
[^c10]: doi-10-48550-arxiv-2308-12539 — "UnQOVER (0.660), BITS (0.617), and BEC-PRO (0.594) showed higher average"
[^c11]: doi-10-48550-arxiv-2308-12539 — "larger size and greater diversity of CALM prompts."
[^c12]: doi-10-48550-arxiv-2308-12539 — "group over all templates varies within a narrow range of 0-3%."
[^c13]: doi-10-48550-arxiv-2308-12539 — "compared with prior datasets, as reported in (Selvam et al., 2023)"
[^c14]: doi-10-48550-arxiv-2308-12539 — "we manually verified each template, which led to discarding examples such as"
[^c15]: doi-10-48550-arxiv-2308-12539 — "We believe that models having lower CALM bias scores are likely to exhibit"
[^c16]: doi-10-48550-arxiv-2308-12539 — "the templates used in our dataset are in English."
