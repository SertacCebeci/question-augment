---
description: "Refitting a probe per condition spread rival AUROC from 0.080 to 1.000 on identical weights, while one frozen direction cross-scored across the same conditions stayed within 0.875 to 1.000."
aliases: ["frozen-decoder control", "fixed-direction cross-scoring", "refit-versus-frozen comparison"]
sources: ["doi-10-48550-arxiv-2609-10739"]
---
# Frozen-probe cross-scoring

The default way to compare conditions (prompts, checkpoints, models) with a probe is to fit one on each condition's own compliant data and compare the resulting numbers. The paper's objection is that this conflates two things: "That conflates the representation moved with a different probe was fitted."[^c1] A difference between two refitted probes can come from the activations or from the decoder, and the refit alone does not say which.

The paper separates the two on one model with identical weights. It uses a 15-rung ladder of system-prompt directives, N = 1000 episodes per variant. One reference variant is used to fit a single direction once; the other 14 are cross-scored against that fixed direction. Refitting per variant gives rival AUROC from 0.080 to 1.000, which invites a representational reading. Scoring the one frozen direction across all 14 collapses the range to 0.875–1.000, and no variant inverts.[^c2] "The apparent prompt-driven inversion is produced by refitting."[^c3]

The disagreement is not confined to extreme pairs. Two variants match on rival deception to within 0.002 and are both negation-bearing, yet "their refit AUROCs are 0.998 and 0.080, so neither" deception rate nor negation vocabulary explains the gap.[^c4] Across 12 pairs of variants whose deception rates agree to within 0.05, "refit AUROCs differ by a median of 0.335 (largest 0.919)", while the single frozen direction differs by a median of 0.025.[^c5] "Matching prompts on behaviour does not bring the refit numbers into agreement" and the frozen number does not need it.[^c16]

The same activations can yield opposite verdicts from two decoders that both pass the usual check. On one variant, two ally-trained probes both "score 1.000 on ally validation" and read rival AUROC 0.080 and 0.986: "same activations, same layer, same fit criterion, opposite verdicts."[^c6]

The converse failure runs the other way. Across a task change, "across a task change a refit probe reads ≈1.000 while the same direction frozen reaches only 0.864," .[^c7] The paper also reports a reward-trained arm on this comparison (Fig. 13), but the sentence is ambiguous about which probe its 0.282 belongs to, so that number is not used here. My inference: a frozen score can fall well below its refit score on a shifted task, and the refit number alone would not show it.

The paper does not conclude that the activations are unchanged. A paired geometric comparison on the same 14 variants finds that "the activations differ substantially" even though the frozen decoder still reads all 14 variants in the 0.875–1.000 range, with a role-dependent component from layer 16.[^c15] Its conclusion is narrower: "The refit spread alone does not isolate representational change from a change in the fitted decoder, even when the evaluated activations differ."[^c8] The prescription is to "Fit once, cross-score the fixed direction, report both."[^c9] and not to "Do not read a difference between separately refitted probes as representational change" without that control.[^c10]

## Limits

- The frozen and refit curves are descriptive transfer comparisons on different evaluation subsets, not paired estimates on identical examples: "they are descriptive transfer comparisons, not paired estimates on identical test examples."[^c11]
- The prompts are matched only on summary variables such as deception rate and negation. "the prompts are matched on those summary variables only," so item-level differences remain uncontrolled.[^c12]
- Freezing has a cost that depends on the layer: "Freezing is not free and its cost varies eighteenfold across layers" in the transfer experiment, so a frozen direction is not automatically the right one to use.[^c13]
- The reference variant that fixes the direction is a choice. The paper notes that "the reference variant has none, being the variant the direction is fit on".[^c17] My inference: the control's baseline depends on that pick.
- One model, one task family, 14 variants. Cross-scoring shows one decoder suffices for these variants; it does not show identical representations.[^c14]

## Related

- [[perfect-aliasing]] — the other identification failure in the same paper: a fitted direction's sign depends on which labels were fitted, and a refit can move that sign silently.
- [[cross-model-domain-adaptation-probe]] — adapts a source probe to new models rather than refitting it on target labels; in the frozen-probe terms here it is the cross-scoring side of the comparison, with the direction moved by unlabeled alignment (my inference).
- [[correctness-probe-transfer-needs-joint-training]] — reads a below-chance native refit as a direction pointed elsewhere; the cross-scoring result here suggests a refit can disagree with itself within one model, so refit agreement is weak evidence about a direction (my inference).

[^c1]: doi-10-48550-arxiv-2609-10739 — "That conflates the representation moved with a"
[^c2]: doi-10-48550-arxiv-2609-10739 — "0.875–1.000: no variant inverts at all"
[^c3]: doi-10-48550-arxiv-2609-10739 — "The apparent prompt-driven inversion is produced by refitting."
[^c4]: doi-10-48550-arxiv-2609-10739 — "yet their refit AUROCs are 0.998 and 0.080, so neither"
[^c5]: doi-10-48550-arxiv-2609-10739 — "refit AUROCs differ by a median of 0.335 (largest 0.919)"
[^c6]: doi-10-48550-arxiv-2609-10739 — "same activations, same layer, same fit criterion, opposite verdicts."
[^c7]: doi-10-48550-arxiv-2609-10739 — "across a task change a refit probe reads ≈1.000 while the same direction frozen reaches only 0.864,"
[^c8]: doi-10-48550-arxiv-2609-10739 — "The refit spread alone does not isolate representational change from a change in the"
[^c9]: doi-10-48550-arxiv-2609-10739 — "Fit once, cross-score the fixed direction, report both."
[^c10]: doi-10-48550-arxiv-2609-10739 — "Do not read a difference between separately refitted probes as representational change"
[^c11]: doi-10-48550-arxiv-2609-10739 — "they are descriptive transfer comparisons, not paired estimates on identical test examples."
[^c12]: doi-10-48550-arxiv-2609-10739 — "the prompts are matched on those summary variables only,"
[^c13]: doi-10-48550-arxiv-2609-10739 — "Freezing is not free and its cost varies eighteenfold across layers"
[^c14]: doi-10-48550-arxiv-2609-10739 — "refit spread is not necessary to explain the activations; this does not imply identical representations."
[^c15]: doi-10-48550-arxiv-2609-10739 — "the activations differ substantially and one decoder still reads all 14 at"
[^c16]: doi-10-48550-arxiv-2609-10739 — "Matching prompts on behaviour does not bring the refit numbers into agreement"
[^c17]: doi-10-48550-arxiv-2609-10739 — "the reference variant has none, being the variant the direction is fit on"
