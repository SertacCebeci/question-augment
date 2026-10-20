---
description: "Each reasoning step gets the majority verdict of independent verifier runs, with no ground truth; the labels trained a PRM to 67.5 F1 on ProcessBench, above 66.4 for a reference-guided verifier."
aliases: ["step-level self-consistency", "step-level majority voting", "step-level consistency", "per-step consensus labels", "synthetic step labels"]
sources: ["arxiv-2512-03244"]
---
# Step-level consensus labels

A process reward model (PRM) is trained on labels that say, for each step of a solution, whether that step is correct. The usual sources are human annotators or a reference answer that marks the final outcome. Step-level consensus labels are a third source: a verifier model checks the same solution many times, and the label for each step is the majority verdict of those checks. The work calls this scaling verification compute, and it compares the step-level vote with a single verification and with a verifier that is shown the reference answer.[^c1]

**Mechanism.** The verifier runs N = 16 times on each solution. Step-level consistency takes each step i and keeps the verdict, correct or incorrect, that most runs give for it. The per-step winners form "a consensus verification pattern", and one real verification whose step verdicts match that pattern is kept as the training example.[^c2][^c3] The vote is taken per step, not on the final verdict, so a run that errs at one step can be outvoted there while its other verdicts stand. My reading: the training example is still a real verification, but it need not be the one any single run would have produced.

**Measured effect.** On ProcessBench, a benchmark of erroneous-step identification in math solutions, the step-level variant gives "F1 scores of 67.5 (PRM) and 65.7 (PRM-CoT), surpassing reference-guided scores of 66.4 and 63.2".[^c4] The reference-guided arm is the one where the verifier "has ground truth answer" when it checks each step.[^c5] The authors explain its lower score as anchoring: "because the reference answer anchors the verifier" on the outcome, so flawed steps are marked correct when the final answer is right.[^c6][^c7] Step-level voting, by contrast, "votes on each step independently."[^c8]

A separate check was made against human judgement. The authors annotated "pairs (788 steps) ourselves, blind to the synthetic labels", and the step-level consensus "agrees with our annotations on 89% of steps", against 76% for a single verification.[^c9][^c10] The numbers are reported as the same ordering as the ProcessBench result, not as a separate benchmark.

The cost is visible in the design. Sixteen verifier calls replace one per solution (arithmetic from the stated N, my reading). The gain is paid for in compute, not in labels, which is the trade the title names.

## Limits

- The domain is math, where a solution's correctness can be checked. "We validated our framework exclusively on mathematical reasoning, where correctness is objectively verifiable."[^c11] Open-ended domains are untested; the limitations section names them as future work.
- The gap to the reference-guided arm is 1.1 F1 on one benchmark. The sections I read report no spread across seeds or runs, so the size of the gap relative to run-to-run noise is unknown (my reading).
- The human check covers 75 pairs annotated by the authors. Blindness to the synthetic labels guards against one bias, not against the authors' choice of pairs.
- Sixteen runs of one verifier share its blind spots. If the runs err on the same steps, voting amplifies the error rather than cancelling it. The paper does not measure correlation of errors across runs (my inference).
- The labels were used to train generative PRMs by supervised fine-tuning. Direct use of self-consistency as a reward is treated differently: the paper cites another work's finding that it "fails catastrophically" when used directly as a reward.[^c12] The paper reports its own test of that idea in a section I did not read in full, so I do not state its result here.

## Related

- [[verification-weighted-voting]] — majority vote over answers, where a tool-checked weight corrects the frequency-as-truth failure; the same vote, taken over final answers rather than steps
- [[process-outcome-consistency-verification]] — a check on the whole derivation against its outcome, where this note votes on each step
- [[single-reference-grading-confound]] — grading against one reference treats legitimate disagreement as error, the same weakness the reference-guided arm shows
- [[effective-independent-votes]] — how many votes are truly independent; the sixteen runs here are assumed independent and that is not tested
- [[process-reward-model-hackability]] — what a policy does when a step-level reward is trained against it

[^c1]: arxiv-2512-03244 — "scales verification compute as an alternative"
[^c2]: arxiv-2512-03244 — "This produces a consensus verification pattern"
[^c3]: arxiv-2512-03244 — "We then randomly select"
[^c4]: arxiv-2512-03244 — "F1 scores of 67.5 (PRM) and 65.7 (PRM-CoT), surpassing reference-guided scores of 66.4 and 63.2"
[^c5]: arxiv-2512-03244 — "verifier has ground truth answer"
[^c6]: arxiv-2512-03244 — "because the reference answer anchors the verifier"
[^c7]: arxiv-2512-03244 — "on the final outcome: the verifier marks flawed"
[^c8]: arxiv-2512-03244 — "step-level consistency votes on each step independently."
[^c9]: arxiv-2512-03244 — "pairs (788 steps) ourselves, blind to the synthetic labels"
[^c10]: arxiv-2512-03244 — "agrees with our annotations on 89% of steps"
[^c11]: arxiv-2512-03244 — "We validated our framework exclusively on mathematical reasoning"
[^c12]: arxiv-2512-03244 — "Direct use of self-consistency as rewards"
