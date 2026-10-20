---
description: "Numeric answers are graded correct when within max(ε·|a|, 1) of the reference, so small targets get an absolute floor; the paper finds model rankings stable across tolerance choices."
aliases: ["hybrid absolute-relative tolerance", "relative tolerance with absolute floor", "tolerance-based numeric match"]
sources: ["arxiv-2601-02598"]
---
# Floored relative tolerance for numeric answers

A numeric answer is rarely checked for exact equality. LongDA grades an agent's number against a reference with a tolerance that is relative for large targets and absolute for small ones. Given a tolerance parameter ε and a reference answer a, the tolerance is τ(a) = max(ε·|a|, 1), and a prediction counts as correct if |â − a| ≤ τ(a), applied element-wise to list answers.[^c1] The authors give the reason for the floor directly: it ensures "that small-magnitude targets are not overly penalized."[^c2]

The mechanism is simple. Where |a| is large, the tolerance grows with the answer, so a rounding difference in a large count or a weighted total still counts. Where |a| is near zero, a purely relative tolerance would demand near-exact agreement on a number that is small for a reason unrelated to skill; the constant floor of 1 gives such targets a fixed width. The two terms together let one rule apply to counts, percentages and near-zero differences without choosing a unit per query.

The paper also varies the threshold. Match rate rises monotonically as tolerance grows, but the authors report that "the relative ranking of models and the overall performance gaps remain stable, indicating that the evaluation is not overly sensitive to the exact tolerance choice."[^c3] So the tolerance changes the level of the match rate far more than the ordering of systems. For a benchmark, that is the property that matters: a comparison between models survives a looser or tighter threshold, even though the absolute scores do not.

The point for asking and answering is that a grading rule is itself a choice about which errors count. Under this rule, a result that misses a reference by a rounding amount on a large value is correct, while a result that misses on a small value by the same absolute amount may not be. Whoever states the question and whoever answers it share that rule only if the rule is written down.

## Limits

- The value of ε is set by the paper and is not reproduced in the sections read here; the claims above hold for the rule's form, not for a specific threshold.
- The absolute floor is expressed in the units of the answer. For a quantity measured as a fraction in [0, 1], a floor of 1 would accept almost any value (my inference); whether LongDA's percentage answers are in percent units is not checked here.
- The sensitivity result covers rankings and gaps across the models evaluated, not every possible threshold, and it does not show that the floored rule matches human judgement of "close enough."
- The rule grades only the final number. The paper's own limits note that it does not measure intermediate analytical quality, so a correct number by a wrong method passes the same test.
- The rule is applied after the structural coverage check; an answer that fails the shape is not scored for value. See [[answer-structure-specification]].

## Related

- [[answer-structure-specification]] — the shape check that comes before this numeric check; tolerance applies only to answers that fit the structure.
- [[evaluation-choices-encode-error-priorities]] — the general point that an evaluation rule encodes which errors it forgives; this threshold is one instance (my framing).
- [[reference-answer-defect-audit]] — a wrong score can come from the reference rather than the answerer; a tolerance rule does not guard against a wrong reference value.

[^c1]: arxiv-2601-02598 — "The prediction is considered correct if |âq − aq | ≤ τ (aq ) (applied element-wise for list answers)"
[^c2]: arxiv-2601-02598 — "ensuring that small-magnitude targets are not overly penalized"
[^c3]: arxiv-2601-02598 — "the relative ranking of models and the overall performance gaps remain stable, indicating that the evaluation is not overly sensitive to the exact tolerance choice"
