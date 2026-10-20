---
description: "A verifier that rewards an answer only when the derivation is consistent with it catches lucky guesses (about 17% of responses) and yields better RLVR policies than outcome-only checking."
aliases: ["process-outcome alignment", "process-aware verification", "lucky guess detection", "reasoning-answer consistency", "RAC"]
sources: ["arxiv-2602-11570", "arxiv-2512-23511", "doi-10-48550-arxiv-2509-23140", "arxiv-2512-14944", "arxiv-2512-02699"]
---
# Process-outcome consistency verification

Outcome-centric verification compares only the final result with the ground truth. The PRIME work argues this "leads to assigning positive rewards to correct answers produced from incorrect derivations".[^c1] These are "lucky guesses": the right answer reached by a wrong route (their example cancels the 6 in 16/64 to get 1/4).

## Mechanism

Under process-outcome alignment, a verifier makes two judgments: whether the outcome matches the ground truth, and whether the derivation is logically consistent with that outcome. The training reward is the product of two indicators, so it is positive only when both hold.[^c2] This differs from step-level process reward models, which score each step; here the verifier judges the whole derivation against its conclusion.

Frequency: in human annotation of responses from several open and closed models to about 2,500 STEM prompts, the authors "identify that 16.98% of the responses exhibit" this lucky-guess pattern.[^c3] An outcome-only verifier therefore rewards roughly one response in six that is flawed.

Verifier capability: models with explicit reasoning beat their instruction-tuned counterparts (Qwen3-4B thinking over instruct by more than 8 points). The authors conclude that "strong reasoning ability appears necessary for a high-quality" verifier, because catching the flaw requires following the derivation rather than matching answers.[^c4]

Downstream effect: training Qwen3-14B-Base with a process-aware verifier gave gains over the outcome-only baseline, "achieving absolute performance gains of 8.29%, 9.12%, and 7.31% on AIME24, AIME25, and Beyond-AIME,".[^c5] The authors attribute this to reduced reward hacking via lucky guesses.

Predictiveness: across five verifiers spanning roughly 70-85% accuracy on the benchmark, they "observe a strong positive linear correlation" between verifier benchmark accuracy and policy performance, with R² of 0.937 (8B) and 0.920 (14B).[^c6] So verifier accuracy on process-outcome items serves as a selection proxy.

A formal counterpart. arxiv-2512-23511 meets the same failure, a right answer that the chain does not support, with a theorem prover instead of a learned verifier. The authors read a chain that reaches the correct conclusion without entailing it as "indicating that the answer might be coincidental."[^c7] Whether an entailment check and a learned derivation check catch the same lucky guesses is not tested in either work. The formal route needs explicit premises and a translation of the reasoning into logic, which the STEM setting described above does not supply (my reading); see [[refutation-based-entailment-check]].

A structural route to process-level supervision. TagPR (doi-10-48550-arxiv-2509-23140) writes its reasoning as tagged steps and penalizes chains that fail a check on the tags. Its motivation is close to the lucky-guess argument above: "This resolves the degeneracy of outcome-only rewards, which cannot distinguish between a model that carefully analyzes user history and one that ignores it but guesses correctly."[^c8] The checks are "format verification, ensuring that each tag is syntactically well-formed", plus a vocabulary check and a minimum tag count.[^c9] These test the shape of the chain, not whether its steps support the final answer. On the text read, a well-formed chain with a lucky answer passes them (my reading; the paper does not test lucky guesses under this reward).

A diagnostic version. PuzzleCraft measures the same gap, a rationale that does not support the emitted answer, but as a monitor rather than a reward. A fixed judge (Qwen2.5-VL-72B) is given each sampled rationale and final answer and asked "whether the rationale explicitly supports the emitted answer", scored in [0, 1].[^c10] The authors state that this score "is not used for reward shaping, sample reweighting, or gradient updates in our training pipeline."[^c11] Under vanilla GRPO the score "increases early, then degrades later even as puzzle reward continues to improve."[^c12] The authors' point is that "higher puzzle reward is not, by itself, a reliable indicator of downstream reasoning performance."[^c13] This is a claim about training dynamics in one setting, not a new verifier: it says a verifier-free judge can see a drift that outcome reward hides, and it does not say the judge catches lucky guesses.

The same failure, measured in emotion reasoning. The MIGR paper (arxiv-2512-02699) counts the cases where the explanation contradicts the emotion the answer names: "the reasoning explanation contradicts the target emotion while the predicted answer remains" correct.[^c15] On DFEW, the share of correct predictions with such an explanation is, in the paper's words, "the relative inconsistency among correct predictions decreases from 32.2% to" 7.37%, from the baseline R1-Omni to the authors' model.[^c14] The lucky-guess rate above comes from human annotation of derivations; this rate comes from the paper's own consistency metrics, whose definitions sit in an appendix not read here, so the two counts are not obviously the same measurement (my reading).

## Limits

- The domain is college-level STEM with a checkable ground-truth answer; open-ended questions, where no reference outcome exists, are untouched.
- The R² values rest on five verifiers and two base models, so they are fits on very few points; causality from verifier accuracy to policy gain is argued, not isolated. This is my reading of the design.
- The 16.98% rate comes from the authors' own sampled models and prompts and will vary with the generator and the difficulty of the questions.
- Ground truth for derivation validity is expert judgment (their annotators); disagreement among experts is not examined in what I read.
- Gains were reported on math benchmarks only (AIME24, AIME25, Beyond-AIME), not on tasks such as asking or clarification.
- The structural tag reward in TagPR is not a consistency check, and the paper reports no rate of lucky guesses under it; the two routes are not shown to catch the same failures.
- The RAC drift is measured with one judge (Qwen2.5-VL-72B) on one puzzle family and two backbone families. Whether that judge's score tracks a verifier-based lucky-guess rate is not tested in that work (my inference).
- The emotion-setting rate depends on the authors' own consistency metric, defined in an appendix not read here. The paper does not test it against a derivation verifier, so it is not shown to catch the same guesses (my inference).

## Related

- [[correct-answer-trap]] — the same lucky-correct-answer failure, found in student-misconception grading
- [[process-reward-model-hackability]] — step-level reward models and how they get exploited
- [[accuracy-masks-unstable-reasoning]] — correct accuracy hiding unsound reasoning
- [[cot-judge-detection-localization-gap]] — judges that detect flaws but cannot place them
- [[user-embedding-reward-model]] — the same TagPR pipeline's user-level reward term, which scores whose answer it is rather than whether the derivation holds
- [[rollout-dispersion-curriculum]] — the PuzzleCraft curriculum, which is reported to slow the late RAC decline; the consistency measure there is a monitor, not the weight
- [[multi-hop-trace-error-score]] — the same lucky-guess failure in multi-hop QA traces, filtered by counting erroneous sub-steps rather than by a consistency product

[^c1]: arxiv-2602-11570 — "This leads to assigning positive rewards to correct answers produced"
[^c2]: arxiv-2602-11570 — "𝑅 ( 𝑥 , 𝑦 , 𝑎∗ ) = I(O) · I(C)"
[^c3]: arxiv-2602-11570 — "identify that 16.98% of the responses exhibit"
[^c4]: arxiv-2602-11570 — "Overall, strong reasoning ability appears necessary for a high-quality"
[^c5]: arxiv-2602-11570 — "achieving absolute performance gains of 8.29%, 9.12%, and 7.31% on AIME24, AIME25, and Beyond-AIME,"
[^c6]: arxiv-2602-11570 — "observe a strong positive linear correlation"
[^c7]: arxiv-2512-23511 — "indicating that the answer might be coincidental"
[^c8]: doi-10-48550-arxiv-2509-23140 — "which cannot distinguish between a model that carefully analyzes user history and one that ignores it but guesses correctly"
[^c9]: doi-10-48550-arxiv-2509-23140 — "format verification, ensuring that each tag is syntactically well-formed"
[^c10]: arxiv-2512-14944 — "whether the rationale explicitly supports the emitted answer"
[^c11]: arxiv-2512-14944 — "is not used for reward shaping, sample reweighting, or gradient updates in our training pipeline"
[^c12]: arxiv-2512-14944 — "increases early, then degrades later even as puzzle reward continues to improve"
[^c13]: arxiv-2512-14944 — "higher puzzle reward is not, by itself, a reliable indicator of downstream reasoning performance"
[^c14]: arxiv-2512-02699 — "the relative inconsistency among correct predictions decreases from 32.2% to"
[^c15]: arxiv-2512-02699 — "the reasoning explanation contradicts the target emotion while the predicted answer remains"
