---
description: "Grounded claims the reference lacks earn attenuated credit, and recall's bonus for them is capped by the reference's uncovered count, so verbose detail cannot inflate the score."
aliases: ["reference-anchored calibration", "bounded residual credit", "reference-aware claim credit"]
sources: ["doi-10-48550-arxiv-2607-05150"]
---
# Reference-anchored residual credit

Scoring a generated text against a reference, claim by claim, has a known problem. A correct claim that the reference does not contain is either discarded, which penalizes correct detail, or counted in full, which rewards saying more. The mechanism here takes a middle path. Each candidate claim is first checked against the source (in the paper, a video; the decompose-and-verify step is the one in [[supported-faithfulness-score]]) and kept only if supported. Each supported claim is then matched, once, to at most one reference claim within its category. A matched claim earns full credit. A supported claim with no match earns an attenuated weight. The authors put the split this way: "the reference claims anchor full credit for matched claims," while unmatched supported details receive less.[^a1]

For precision, the share of candidate claims that are supported is recomputed so that matched supported claims count fully and unmatched supported claims count with a weight w_u in [0, 1]. The reported runs set w_u = 0.5.[^a2]

Recall is where the mechanism does its most specific work. The reference is the target, and recall is the share of reference claims recovered by supported candidates. On my reading of their equation, without a bound every extra supported detail would enlarge the numerator at weight w_u, and the effective target would grow with it, so volume could buy recall. The authors cap this. Residual credit is limited by δ, the number of reference claims left unmatched: "The cap operation restricts residual credit by this bound."[^a3] The stated purpose is "recall-side reward hacking through verbose unmatched claims."[^a4] They report that without the cap the captioner did exploit the recall metric, "generating correct yet redundant visual details."[^a5] The effect is that a supported extra can help recall only up to the amount the reference leaves uncovered, and only at the discounted weight.

The two sides are kept separate on purpose. The authors' ablation found that training on precision alone "loses DREAM-1K recall and VCapsBench CR," while recall alone "remains weaker" on precision, and they conclude that "faithfulness and descriptive coverage require different reward pressure."[^a6] The reference anchors what is salient; the verifier anchors what is true. Neither alone is the score.

Transfer, which is my inference and not something the paper tests: the same structure applies to any answer scored against a reference answer. A reference is a partial view of what is correct. A correct answer the reference omits should neither vanish nor count in full. The residual weight and the cap are two separate knobs. One lets verified but unlisted content in at a discount. The other stops that discount from being farmed by volume. The paper's own limits section notes that the reference here is a single source, so the knobs are tuned for one kind of anchor.

## Limits

- The reference is one caption from one proprietary model. The authors say: "While the calibration mechanism currently uses a single reference-caption source."[^a7] Multi-source or ensemble references are named as future work, so the behaviour with several references is not shown.
- The authors do not claim generality: "they do not establish universality across all backbones, verifiers, answerers, or video domains."[^a8] The main policy uses one backbone.[^a9] Everything measured is video captioning. Nothing here tests the mechanism on text answers; the transfer paragraph above is my inference.
- w_u = 0.5 and λ = 0.7 are set by the authors. In the parts of the text I read I did not find a sweep over them, so how sensitive the reward is to these values is not established here.
- The cap addresses over-selection only for supported extras. Precision's residual term, as printed in their Eq. 5, has no cap of its own. The stated guard against over-generation is a separate length penalty, "to discourage over-generation, we incorporate a length penalty."[^a10] I did not read its details in Appendix A, so I cannot say how much of the verbosity pressure it carries.
- The pipeline is expensive: "our current instantiation remains compute-intensive."[^a11] The cost limits how many verifiers and reference sources could be compared, so the mechanism is shown with one verifier configuration.

## Related

- [[recall-only-partial-credit]] — the recall-only score whose blind spot this bound addresses for supported extras; unsupported extras are a different case, handled on the precision side
- [[supported-faithfulness-score]] — the claim-level decomposition and verification step this mechanism runs before matching, scored there without any reference
- [[sparse-assignment-dense-criteria]] — how finely credit is assigned to criteria, a neighbouring design choice in checklist-style rewards
- [[excess-length-over-minimal-sufficient-baseline]] — over-generation measured against a minimal sufficient answer, the failure a length term targets

[^a1]: doi-10-48550-arxiv-2607-05150 — "the reference claims anchor full credit for matched claims"
[^a2]: doi-10-48550-arxiv-2607-05150 — "We set wu = 0.5"
[^a3]: doi-10-48550-arxiv-2607-05150 — "The cap operation restricts residual credit by this bound"
[^a4]: doi-10-48550-arxiv-2607-05150 — "recall-side reward hacking through verbose unmatched claims"
[^a5]: doi-10-48550-arxiv-2607-05150 — "correct yet redundant visual details"
[^a6]: doi-10-48550-arxiv-2607-05150 — "faithfulness and descriptive coverage require different reward pressure"
[^a7]: doi-10-48550-arxiv-2607-05150 — "While the calibration mechanism currently uses a single reference-caption source"
[^a8]: doi-10-48550-arxiv-2607-05150 — "they do not establish universality across all backbones, verifiers, answerers, or video domains"
[^a9]: doi-10-48550-arxiv-2607-05150 — "the main policy uses one backbone"
[^a10]: doi-10-48550-arxiv-2607-05150 — "to discourage over-generation, we incorporate a length penalty"
[^a11]: doi-10-48550-arxiv-2607-05150 — "Our current instantiation remains compute-intensive"
