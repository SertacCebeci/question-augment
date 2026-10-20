---
description: "Min-aggregating parallel LLM judges into one reward favors false negatives over false positives, because RL amplifies high-scoring invalid proofs; disagreement is never resolved upward."
aliases: ["minimum-judge reward", "pessimistic aggregation", "min aggregation of judges", "conservative verifier score", "pessimistic verification", "any-flag rejection"]
sources: ["doi-10-48550-arxiv-2606-13473", "arxiv-2511-21522"]
---
# Pessimistic min-aggregation of judges

When the reward for a long free-form answer comes from an LLM judge, one judge can be talked into a high score by a flawed but persuasive argument. The M3 proof verifier answers this by running several judges in parallel and taking the lowest score as the reward for the whole proof. Three judges score each candidate: two rubric-based judges for calibration and one no-rubric judge for direct error finding.[^c8] "The final reward is the minimum judge score," so a candidate is rewarded only as far as its most skeptical judge allows.[^c1]

The reason given is an asymmetry of cost. A false positive is a wrong score that the policy is then trained to reproduce; a false negative is a correct proof scored too low, which costs one sample. In the authors' words, "policy learns to reproduce, while a false negative usually only discards one candidate among many."[^c2] The paper states the design goal in these terms: the aim of an RL-time verifier "is not maximum accuracy on a static benchmark" but "minimum false-positive rate on a long-running training stream."[^c3]

The mechanism is simple. Because min is monotone in each judge, a flaw that any one judge detects lowers the reward, and the policy would have to fool all three judges at once to be rewarded for it. The group-relative advantage then compares these conservative scores across rollouts of the same problem. The authors' warning about the alternative is direct: "a flawed but persuasive argument, RL will amplify that flaw; this is the same basic reward-gaming" risk that reward-modelling work studies.[^c4] The same aggregator is reused outside training. In the test-time search, the fitness of a candidate is "the minimum score across these verifier samples,"[^c5] and the critique kept with it is the one that goes with that pessimistic score.

The same rule appears in a second setting, with binary verdicts and no reward. A 2025 study of math proof verification defines "pessimistic verification" as a workflow that "rejects a solution if any of multiple parallel verifiers identifies a flaw."[^c9] Its justification is detection, not reward hacking: "an error during multi-round verification is inherently a lowprobability event."[^c10] Repeated checks that reject on any flag therefore raise the chance of catching it, and the authors state that "Pessimistic verification methods effectively amplify the probability of this detection."[^c11] The cost side is argued as rare false rejections, since "current language models typically provide sound reasoning and explanations before pinpointing an error."[^c12] On GPT-5-mini, the progressive variant's balanced F1 on the 1,000-item verification set is reported as 0.833 against 0.768 for a single standard check (Table 1, "Comparison of the evaluation metrics of GPT-5-mini on").[^c13] The authors' summary is that "Progressive pessimistic verification not only boosts performance across these datasets but also shows better scaling."[^c16] How the span of each check changes this is in [[verification-scope-granularity]].

The motivation comes from the authors' own training history. They report that a long RL run with a single-judge rubric verifier "will, with high probability, end in a reward-hacking plateau, not in real capability gains."[^c6] The min over judges is the cheapest response in their design: it does not make any single judge more accurate, it only requires agreement before reward.

## Limits

- The slices I read contain no ablation of min against mean, majority vote or a learned aggregator. The claim that min lowers false positives is a design rationale, not a measured effect. (my reading)
- Min trades false positives for false negatives and the cost of that trade is not reported. Disagreement is always resolved downward: on USAMO 2026 P3 the population reaches 6/7 but never 7/7, a case the authors describe as "disagreement (one judge sees a 6, the other sees a 7) that the min aggregation cannot resolve."[^c7]
- The protection holds only if the judges have partly independent blind spots. Three judges drawn from one model family may share the same blind spot, and then min buys little. The paper does not test this. (my inference)
- A pessimistic aggregator bounds the error of the judges, not of the rubric. A grading scheme derived from a wrong reference solution would be enforced by all three judges together. (my inference)
- The experiments are on one model family (MiniMax-M3) and on the paper's own judge set; no transfer to other judges is shown in the parts I read.
- In the verification setting the false-rejection premise holds only for stronger models. The same paper reports that "many smaller models do indeed produce a large number of unwarranted False Negative judgments."[^c14] Rejecting on any flag therefore spends its cost where the verifier is weakest.
- The paper's accuracy figures on strong models are themselves unreliable. It argues that "decrease in TPR is largely an illusion caused by dataset" annotation, so a pessimistic rule's measured gain on the standard benchmarks understates it and cannot be read off them directly.[^c15] The benchmark defects are audited in [[reference-answer-defect-audit]].

## Related

- [[cot-judge-detection-localization-gap]] — judges flag a broken chain more often than they name the broken step; a conservative aggregator does not address that gap, it only lowers the score when any judge flags a flaw
- [[reasoning-judge-adversarial-policy]] — RL against a single judge is hacked; min over judges is one response to the same failure
- [[judge-master-key-false-positives]] — reference-based judges accept content-free openers; a pessimistic aggregator is a candidate defence against that class of false positive, untested here
- [[process-reward-model-hackability]] — a step-level reward model that RL drives to high reward without correct logic
- [[population-search-under-noisy-verifier]] — the same min score serves as the fitness function of a population search
- [[verification-scope-granularity]] — the any-flag rule over binary proof verdicts; the progressive variant applies it across proof chunks of shrinking size, a separate axis
- [[reference-answer-defect-audit]] — a defective reference makes a correct verifier look weak, the same account the verification paper gives for its benchmarks

[^c1]: doi-10-48550-arxiv-2606-13473 — "The final reward is the minimum judge score,"
[^c2]: doi-10-48550-arxiv-2606-13473 — "policy learns to reproduce, while a false negative usually only discards one candidate among many."
[^c3]: doi-10-48550-arxiv-2606-13473 — "but minimum false-positive rate on a long-running training stream."
[^c4]: doi-10-48550-arxiv-2606-13473 — "a flawed but persuasive argument, RL will amplify that flaw; this is the same basic reward-gaming"
[^c5]: doi-10-48550-arxiv-2606-13473 — "Its fitness is the minimum score across these verifier samples,"
[^c6]: doi-10-48550-arxiv-2606-13473 — "verifier will, with high probability, end in a reward-hacking plateau, not in real capability gains."
[^c7]: doi-10-48550-arxiv-2606-13473 — "disagreement (one judge sees a 6, the other sees a 7) that the min aggregation cannot resolve."
[^c8]: doi-10-48550-arxiv-2606-13473 — "Three judges score in parallel: two rubric-based"
[^c9]: arxiv-2511-21522 — "workflows that rejects a solution if any of multiple parallel verifiers identifies a flaw."
[^c10]: arxiv-2511-21522 — "an error during multi-round verification is inherently a lowprobability event."
[^c11]: arxiv-2511-21522 — "Pessimistic verification methods effectively amplify the probability of this detection."
[^c12]: arxiv-2511-21522 — "since current language models typically provide sound reasoning and explanations before pinpointing an error, actual"
[^c13]: arxiv-2511-21522 — "Comparison of the evaluation metrics of GPT-5-mini on"
[^c14]: arxiv-2511-21522 — "a large number of unwarranted False Negative judgments."
[^c15]: arxiv-2511-21522 — "decrease in TPR is largely an illusion caused by dataset"
[^c16]: arxiv-2511-21522 — "Progressive pessimistic verification not only boosts performance across these datasets but also shows better scaling"
