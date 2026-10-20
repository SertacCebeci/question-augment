---
description: "An LLM judge can overscore every level yet keep the rank order of candidates; for a decision that needs only the ordering, such as where to stop, the absolute level carries no weight."
aliases: ["rank-order fidelity", "ordinal judge validity", "ordinal agreement with experts", "ordering fidelity of a judge"]
sources: ["arxiv-2512-21066", "arxiv-2512-09662"]
---
# Ordinal judge fidelity

A judge can be wrong about level and right about order. In a rice-advice study, 14 LLM judges scored 11 refinement rounds on seven criteria, as did 12 crop scientists. The judges were lenient: "every criterion was overscored by 1.4–2.3 points."[^c1] On an absolute scale their numbers mean little. Yet the order they gave the rounds tracked the experts' order closely, with "Spearman ρ = 0.58–0.90."[^c2] The correlation was computed "on round-level group means (n = 11 rounds)," so each judge panel is compared with the experts over eleven points.[^c3] "What the LLM panel largely preserved was" the ordering of rounds, including where the quality peaked.[^c4]

The mechanism is simple. A peak is found by comparing values, and a constant offset applied to every score moves none of them relative to each other. The authors note this is "ordering task that is invariant to any constant shift in scores," and conclude that "ordinal fidelity suffices and score calibration is unnecessary."[^c5][^c6] A judge that is systematically generous can therefore still locate a maximum, so long as its generosity is roughly uniform over the candidates it is compared on.

The formal point survives the transfer to other tasks: a monotone distortion of the scale preserves ranks, so a rank-based decision is unaffected by it. What does not transfer is any use that reads the absolute score against a threshold, such as "accept at 5 of 7." Such a use is exposed to the overscoring, and the ordering argument gives it no protection.

The protection is also not automatic. Judges differed widely, and the authors call relying on one "risky": "relying on a single judge is risky, because individual judges differed widely."[^c7] The best judge located the expert peak within one round on "87.5% of the score series," while the worst was the model that had generated the recommendations.[^c8][^c9] The authors' procedure is to screen candidate judges against a small expert-scored pilot, keep only those whose peak falls within ±1 round, and exclude judges from the generating model's family. This is a recommendation from one case, not a tested method.

Two things seem to make a judge's ordering usable in this sense: its order must agree with experts on the decision's own axis, and the agreement must be checked on that axis. A judge may rank rounds well and still rank completeness or truth poorly; the rank fidelity of a judge looks task-specific (my inference). Elsewhere, completeness ratings track truth only weakly (see [[judge-coverage-overestimation]]).

The same ordering test has been run on classifiers rather than refinement rounds. Hate-speech labels from several LLMs were used to rank simulated classifiers, each made by degrading an oracle that reproduces the human majority labels: "generate synthetic classifiers by randomly flipping a proportion p% of predictions."[^c11] The ranking under LLM labels was compared with the ranking under human labels by Kendall's τ. The strongest LLM labeller kept the human order with "τ ≥ 0.95" on the three datasets, while its item-level agreement with humans was low.[^c12] The authors' reading is that LLM labels "largely preserve the relative order of classifiers" even "despite low instance-level agreement."[^c13] The ordering is not the whole story. One labeller produced an inverted order on one dataset, "producing an inverted ranking relative to human judgements," and absolute scores stayed off: "absolute score estimates remain biased."[^c14] The authors also make the use conditional: LLM labels can support comparison "provided that correlation is verified on the target dataset."[^c15]

## Limits

- The agreement is over 11 round means in one task. A rank correlation over that few points is coarse, and a few misplaced rounds can move it a lot. (my inference)
- The peak is one maximum on a clean inverted U. Judges were tested on whether they found that maximum, not on whether they order arbitrary pairs of outputs well.
- Criteria disagree about the peak: Conciseness peaks early and Cost Consideration late. A judge can match experts on one criterion and not another, and the per-criterion picture is what the screen has to check.
- The authors call their stopping procedure "not a validated stopping algorithm," and state that "formal guarantees for judge-driven stopping remain future work."[^c10]
- Judges from the same family may share the biases that they are meant to detect. This is the self-preference question in [[llm-judge-biases]], which this study did not settle.
- The classifiers in the hate-speech ranking test are random degradations of one oracle, not trained systems. Whether the order holds when real classifiers share error patterns is not tested there (my inference).[^c11]

## Related

- [[llm-judge-biases]] — position, verbosity and self-enhancement; the judge-family result here sits beside them
- [[refinement-quality-peak]] — the non-monotone curve that a screened judge is asked to locate
- [[exact-match-versus-weighted-agreement]] — another case where reading scorer output as an ordinal scale changes what agreement means
- [[pessimistic-min-judge-aggregation]] — several judges against single-judge failure, by a different route (a minimum rather than a screened panel)
- [[cross-rater-reliability]] — the group-level counterpart: a labeller can mirror a human group in aggregate while diverging item by item

[^c1]: arxiv-2512-21066 — "every criterion was overscored by 1.4–2.3 points"
[^c2]: arxiv-2512-21066 — "Spearman ρ = 0.58–0.90"
[^c3]: arxiv-2512-21066 — "computed on round-level group means (n = 11 rounds)"
[^c4]: arxiv-2512-21066 — "What the LLM panel largely preserved was"
[^c5]: arxiv-2512-21066 — "ordering task that is invariant to any constant shift in scores"
[^c6]: arxiv-2512-21066 — "ordinal fidelity suffices and score calibration is unnecessary"
[^c7]: arxiv-2512-21066 — "relying on a single judge is risky, because individual judges differed widely"
[^c8]: arxiv-2512-21066 — "The best judge located the expert peak within ±1 round on 87.5% of the score series"
[^c9]: arxiv-2512-21066 — "the worst judge was the model that had generated the recommendations"
[^c10]: arxiv-2512-21066 — "formal guarantees for judge-driven"
[^c11]: arxiv-2512-09662 — "generate synthetic classifiers by randomly flipping a proportion p% of predictions"
[^c12]: arxiv-2512-09662 — "Nemo, consistently achieving τ ≥ 0.95 with minimal"
[^c13]: arxiv-2512-09662 — "they largely preserve the relative order of classifiers"
[^c14]: arxiv-2512-09662 — "absolute score estimates remain biased"
[^c15]: arxiv-2512-09662 — "provided that correlation is verified on the target dataset"
