---
description: "A solution can run within limits and pass validity yet sit far below expert quality, so validity rates and quality scores measure different things and can diverge widely."
aliases: ["workable-versus-optimal gap", "pass-rate versus score gap", "workable but under-optimized solutions", "validity-quality gap"]
sources: ["arxiv-2512-15699"]
---
# Valid-versus-optimal answer gap

An answer can be valid, meaning it runs, respects resource limits and produces output in the required form, and still be far from the best achievable. Two measurements follow from this and they need not agree. One records whether an answer clears a floor; the other records where it lands on a quality scale. In FrontierCS, where scores are anchored by a trivial baseline and an expert reference (see [[two-anchor-graded-scoring]]), the two come apart by a wide margin. The paper observes that "Pass rates remain substantially higher than raw scores, indicating that models often produce workable but under-optimized solutions,"[^c1] and summarizes the lesson as "merely producing workable solutions is insufficient" for open-ended tasks.[^c2]

The mechanism the paper reports for the gap is not a crash but a lack of substance. Claude Sonnet 4.5 "often produces workable solutions that generate basic outputs within resource limits and avoid compilation or runtime errors, yet these solutions frequently lack the optimization strategies needed for competitive performance."[^c3] Such answers pass the validity check and then fall at or under the floor: "most of its workable solutions fall below the trivial baseline in the algorithmic track and thus get zero score."[^c4] In the algorithmic table, Claude Sonnet 4.5 has a Score@1 of 5.84 against 95.41 for human experts.[^c13]

The paper also gives a case where the gap comes from the answer's structure. On Polyomino Packing, "the model often fixates on small, low-impact optimizations while overlooking the core algorithmic choices required for" substantial gains.[^c5] Its diagnosis is that models "do not inherently recognize which optimizations are algorithmically meaningful," so they become "trapped in superficially appealing but strategically irrelevant micro-optimizations."[^c6] Here the representation chosen for the internal state made overlap checks hard, and the paper reports that "the model produces invalid code in about 30% of attempts, and in the remaining 70% achieves only low scores, i.e., 20 – 70 due to ineffective search strategies."[^c7]

The paper also reports that the gap does not close with more reasoning alone. For GPT 5 Thinking on the algorithmic track, moving from medium to high effort did not help: "performance drops from 15.336 to 12.626, suggesting diminishing returns at higher reasoning budgets."[^c8] The abstract puts the same point more broadly: "that increasing reasoning budgets alone does not close this gap."[^c9]

What the gap means for asking and answering is this: a check for validity answers whether an answer is usable, while a quality measure answers how good it is, and a request framed as "make it work" is satisfied by answers that are valid and weak. The two need separate criteria. This is my inference from the paper's numbers, not a finding it states.

## Limits

- The gap is measured on one benchmark with one floor. Pass@k counts a run as passing when it "exceed[s] the" trivial baseline, so the size of the gap depends on how trivial that baseline is.[^c10]
- The paper's explanations are case observations: one Claude model's submissions, and one problem with one model. They are not an experiment that isolates cause. The paper says "Claude Sonnet 4.5" and "Claude Opus 4.5" differ on the research track, and that "perform similarly across both tracks" for the other models.[^c11]
- The effort result comes from one model, and each point is "one attempt (3 attempts per problem)."[^c12] It is a three-sample comparison, not a sweep with confidence intervals.
- No test shows that narrowing the gap, by any prompt or method, raises quality without raising validity risk. The paper names the micro-optimization trap but does not test a repair for it in a controlled way.
- The distinction holds where a floor and a quality scale both exist. Domains with only a binary check, or with no measurable quality, do not show this split.

## Related

- [[two-anchor-graded-scoring]] — the scale on which the quality side of the gap is measured, and the source of the floor that defines validity here

[^c1]: arxiv-2512-15699 — "higher than raw scores, indicating that models often produce workable but under-optimized solutions,"
[^c2]: arxiv-2512-15699 — "merely producing workable solutions is insufficient"
[^c3]: arxiv-2512-15699 — "compilation or runtime errors, yet these solutions frequently lack the optimization strategies needed"
[^c4]: arxiv-2512-15699 — "most of its workable solutions fall below the trivial"
[^c5]: arxiv-2512-15699 — "on small, low-impact optimizations while overlooking the core algorithmic choices required for"
[^c6]: arxiv-2512-15699 — "trapped in superficially appealing but strategically irrelevant micro-optimizations."
[^c7]: arxiv-2512-15699 — "code in about 30% of attempts, and in the remaining 70% achieves only low scores, i.e., 20 – 70 due to"
[^c8]: arxiv-2512-15699 — "to high does not yield further gains; in fact, performance drops from 15.336 to 12.626, suggesting"
[^c9]: arxiv-2512-15699 — "that increasing reasoning budgets alone does not close this gap"
[^c10]: arxiv-2512-15699 — "Pass@k denotes the proportion of runs whose results exceed the"
[^c11]: arxiv-2512-15699 — "perform similarly across both tracks."
[^c12]: arxiv-2512-15699 — "Each point is one attempt (3 attempts per problem)."
[^c13]: arxiv-2512-15699 — "and 5.84 (Claude sonnet 4.5) respectively, compared to human experts"
