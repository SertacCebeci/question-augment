---
description: "A refusal earns credit only if it classifies the trap, names the pivotal missing information, and declines endorsement until it is supplied; generic caution does not count."
aliases: ["grounded refusal", "informed refusal"]
sources: ["arxiv-2602-08939", "arxiv-2511-23151"]
---
# Wise Refusal

Wise Refusal is a scoring criterion for the case where a causal claim cannot be licensed by the evidence given. The CausalT5k benchmark requires three things of a valid response: classify the trap family or threat to validity, ask for the pivotal missing information, and refuse to endorse the causal link until that information arrives.[^c1] A refusal is therefore not a yes/no act but a diagnosis followed by a question.

The criterion rules out the cheap form of caution. "A generic refusal such as 'more research is needed' is not sufficient. The refusal must be grounded in the diagnosis."[^c2] The credit goes to the refusal that names what would resolve the ambiguity, so the refusal doubles as the question the asker needs to answer next.

Worked case in the paper: players using one golf-ball brand score better, but the scenario says they are also more experienced and better trained. Answering "yes" is a confounding error. The wise response names the missing comparison, for instance whether similarly skilled players were randomly assigned to brands or whether experience and training were controlled.[^c3] The benchmark stores this pivotal missing information per case, not only the final label.

Scoring is applied to the free-text justification of Level 2 (trap) cases: does it identify the trap, state the missing information, and decline endorsement.[^c4] The authors stress that the same wrong label can come from over-refusal, sycophancy, confounding, lower-rung collapse, or counterfactual hallucination, and that stored metadata separates them.[^c5]

The same criterion appears in visual grounding, where a refusal to an irrelevant query is treated as a diagnosis that must be stated. Jung et al. (2025) add an explain term that "promotes refusal answers that explain the semantic mismatch"; it is the difference of two similarities, and the similarity is one that "denotes the cosine similarity between SentenceBERT embeddings."[^c6][^c7] Naming the mismatch is credited, as the criterion requires. What the term checks is closeness of wording to a reference explanation, not whether the named mismatch is true of the video (my inference from the form of the reward; the paper does not test it). So the part of the criterion that asks for a checked diagnosis is carried by a reference, and the part that asks for the missing piece is not verified.

## Limits

The paper defines and applies the rubric but, in the text I read, gives no inter-rater agreement for Wise Refusal scoring specifically, and no measure of whether asking the pivotal question actually improves downstream answers. The criterion is defined for causal-inference traps; whether it transfers to other unanswerable-question types is my inference, not tested. Model panels differ between experiments, so cross-model comparisons are loose.

## Related

- [[skepticism-trap]] — the opposite failure: refusing valid claims; Wise Refusal applies only where the claim is truly unlicensed
- [[detection-correction-gap]] — a model can name the flaw yet still endorse the claim, which fails the "refuse" step
- [[recognition-refusal-dissociation]] — mechanistic version of recognizing a problem without acting on it
- [[sycophantic-capitulation]] — pressure variants test whether the refusal survives user insistence
- [[hard-irrelevant-query]] — the same refusal criterion for a query that is close to the video but mismatched in one element

[^c1]: arxiv-2602-08939 — "Classify: identify the trap family or threat to validity."
[^c2]: arxiv-2602-08939 — "A generic refusal such as “more research is needed” is not sufficient."
[^c3]: arxiv-2602-08939 — "A Wise Refusal should instead identify the missing comparison—for"
[^c4]: arxiv-2602-08939 — "score whether the"
[^c5]: arxiv-2602-08939 — "The same incorrect answer can arise from over-refusal,"
[^c6]: arxiv-2511-23151 — "promotes refusal answers that explain the semantic mismatch"
[^c7]: arxiv-2511-23151 — "denotes the cosine similarity between SentenceBERT embeddings"
