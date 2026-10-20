---
description: "Whether checking a proof is easier than producing one: theorem proving is said to lack that gap, so verification effort is proposed as a proxy for proof quality."
aliases: ["generation-verification gap", "verification gap", "generator-verifier gap", "gap between producing and checking"]
sources: ["arxiv-2511-22570", "arxiv-2511-19399"]
---
# Generation-verification gap

The gap is the difference between how hard it is to produce a solution and how hard it is to check one. Where checking is much easier, a checker can filter what a generator produces, and a generator can be trained against the checker. The DeepSeekMath-V2 paper treats the gap as the missing ingredient for natural-language proofs: "The lack of a generation-verification gap in natural-language theorem proving hinders[^g1] further improvement." Its argument starts from the reward. A final-answer reward is "an unreliable proxy for reasoning correctness",[^g2] and it is "inapplicable" to proofs, where "making final answer rewards inapplicable."[^g3] A correct number says nothing about the derivation behind it, so the model needs a verifier that finds flaws in a proof with no reference solution.

The mechanism the paper proposes rests on effort rather than on one binary check. The authors reason that "A proof is more likely to be valid when no issues can be identified despite scaled verification efforts."[^g4] They then use the effort itself as a measure: "The efforts required to identify valid issues can serve as a proxy for proof quality, which can be exploited to optimize proof generation."[^g5] On this reading, a proof that survives many independent attempts to find a flaw is more trustworthy than one that survives few, and a generator can learn to spend its own effort looking for flaws before it finalizes.

The gap is stated as a premise of the loop, and the text does not measure it as a quantity. I found no figure for how much easier checking is than generating on the same problems. The support the paper gives for the effort-based proxy is about scale: "Scaling verifier samples increases the probability of catching real issues in flawed proofs."[^g6] More verifier samples raise the chance of catching a flaw, which is what makes effort a usable signal. The same section observes a limit on the generator's side: when it both writes and analyses its own proof, "it fails to evaluate its own work with the same rigor as the dedicated verifier."[^g7] So the gap is not closed inside one model by asking it to check itself.

The term also appears in other work. [[pretraining-grounded-rubric-self-play]] uses it for open-ended self-play, where grounding a generated rubric in a source document is said to narrow the gap. The transfer is loose: there the gap is about a rubric and a grader, here it is about a proof and a verifier, and the two papers do not measure it the same way.

A reinforcement-learning paper on deep research places the same gap on the reward side. Its rubric writer, not the policy, is given the search results and several sampled answers, and the authors say that this is what opens the gap.[^g10] Removing the later rubric updates costs up to two points on average, which is the measured value of evolving the criteria beyond the search-based initial set.[^g11] See [[evolving-rubric-buffer]].

## Limits

- The gap is asserted as motivation, not measured. The paper gives no direct comparison of generation difficulty and verification difficulty.
- The effort proxy is evaluated with the paper's own instrument. Its in-house scores are "as evaluated by our verifier," and in the in-house set "Proof correctness was measured by majority voting across 8 verification analyses produced by" the paper's final verifier.[^g8] So the claim that effort tracks validity is checked through the same verifier it is meant to justify. Human grading appears only for the separate benchmark figure.
- The scope is olympiad and undergraduate mathematics written in natural language. No open-ended or non-mathematical task is covered in the parts read, so whether the gap is present elsewhere is open.
- Effort does not always close it. The authors write that "We observe that the hardest IMO-level problems remain challenging for our model."[^g9]

## Related

- [[pretraining-grounded-rubric-self-play]] — uses the same term for open-ended self-play, where grounding the rubric in a document narrows the gap
- [[verifier-gain]] — a verifier's worth as precision minus solver accuracy; the gap is one condition under which checking can carry that worth
- [[solver-verifier-similarity]] — a verifier that resembles the solver accepts more wrong answers, a way the apparent gap can be smaller than it looks
- [[hallucination-barrier]] — a model checking its own output shares noise with the generator, the same worry as the self-check failure above
- [[meta-verification]] — the check placed over the verifier's own analysis, where the paper spends further verification effort
- [[scaled-verification-labeling]] — uses the effort proxy to label proofs with no human in the loop

[^g1]: arxiv-2511-22570 — "The lack of a generation-verification gap in natural-language theorem proving hinders"
[^g2]: arxiv-2511-22570 — "First, it serves as an unreliable proxy for reasoning correctness"
[^g3]: arxiv-2511-22570 — "making final answer rewards inapplicable"
[^g4]: arxiv-2511-22570 — "A proof is more likely to be valid when no issues can be identified despite scaled verification efforts."
[^g5]: arxiv-2511-22570 — "The efforts required to identify valid issues can serve as a proxy for proof quality"
[^g6]: arxiv-2511-22570 — "Scaling verifier samples increases the probability of catching real issues in flawed proofs."
[^g7]: arxiv-2511-22570 — "it fails to evaluate its own work with the same rigor as the dedicated verifier."
[^g8]: arxiv-2511-22570 — "Proof correctness was measured by majority voting across 8 verification analyses produced by"
[^g9]: arxiv-2511-22570 — "We observe that the hardest IMO-level problems remain challenging for our model."
[^g10]: arxiv-2511-19399 — "thereby creating a generation–verification gap."
[^g11]: arxiv-2511-19399 — "Removing evolving rubrics results in up to a 2-point drop in average performance"
