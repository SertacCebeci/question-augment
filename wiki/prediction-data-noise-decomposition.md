---
description: "An LLM eval's total noise splits into prediction noise (the model answering the same question differently) and data noise (which questions were drawn); only the first can be averaged away."
aliases: ["prediction noise vs data noise", "prediction variance and data variance", "total variance decomposition for evals", "data sampling noise"]
sources: ["arxiv-2512-21326"]
---
# Prediction noise and data noise

An eval score is a mean over N questions, and each question's score is itself random because the model samples its answer. The law of total variance separates the two sources of spread. For a model evaluated on a question drawn at random and then answered with a random prediction seed, the variance of one score is the variance of the question-level expected score plus the average variance of the answers within each question. The paper writes it as "Total variance = data variance + prediction variance."[^c1]

The second term is prediction noise: the spread that comes from the same model giving different answers to the same question. The paper says it "comes from generating different answers on a given question with the same model."[^c2] The first term is data noise, the spread that comes from which N questions happened to be drawn from a larger pool. "The eval data sampling noise comes from sampling a particular set of N questions instead of another equally good N questions from the unobservable population of questions."[^c3]

The two terms respond differently to the usual remedies. Prediction noise belongs to each question's sampling, so it can be shrunk by drawing several answers per question and averaging them. Data noise belongs to the question pool, so averaging over samples leaves it in place: "While prediction variance can be reduced by averaging, the data variance is irreducible and can be large when the questions vary in their difficulties."[^c4] Data noise also cannot be seen by re-running the fixed question set: "Unlike the prediction noise, the data noise cannot be directly measured by evaluating on the fixed, given set of questions."[^c5] Among the remedies the paper names averaging as the most general: "Averaging is the most general and effective, which we will focus on."[^c6] Fixing the seed or lowering the temperature is narrower, because "Fixing the random seed or lowering the temperature is brittle, which only works on the exact same model."[^c7]

The paper's measurements put the two terms in a typical order. On MATH500, with 1000 predictions per question, "the data standard error (SE) is typically less than 1/2 of the prediction SE between different final models."[^c8] When the prediction term is the larger one, averaging buys power. The paper's training-curve example makes the point with numbers: the data SE is about one sixth of the prediction SE, and "If we average over 36 predictions, then the total SE would be" about 0.24 in units of the prediction SE.[^c9] By my arithmetic, with data SE d and per-prediction SE p, averaging K predictions gives total SE sqrt(d² + p²/K); with d = p/6 and K = 36 this is sqrt(2)/6 · p ≈ 0.24p, while one prediction gives about 1.01p. Averaging therefore cuts the total toward the data floor, and it cannot cut below that floor.

Which term a metric reports is a choice. The paper says a metric that averages predictions per question "corresponds to the data noise after averaging away some prediction noise,"[^c10] while a metric that scores one sampled prediction per question "corresponds to the total noise."[^c11] The paper's reason for caring about data noise is that "On most evals, we care about the underlying ability measured by the eval rather than the specific questions of the eval, so the data noise must not be ignored."[^c12]

## Limits

- The split models sampling, not the whole pipeline. Prediction noise "can come from inference-time choices such as prompt formatting, hyperparameters, and answer extraction" as well as from sampling.[^c13] Averaging over samples does not average those away, and the paper reports one such case, a Llama model served on vLLM, whose predictions were "more deterministic than expected" and so showed "higher data noise than others, likely due to faulty settings."[^c14]
- Data noise is inferred, not observed. The paper says it "can be inferred using the bootstrap or the variance estimator," but "it is not observed in experiments such as the training curve (Example 2) and varying the training seeds."[^c15] A seed sweep therefore measures only the prediction term.
- The finding that prediction noise usually exceeds data noise is empirical, on the paper's evals. The paper attributes the pattern to similarity among current LLMs and says so as a guess: "We speculate that the uniformity of these results comes from the relative similarity among LLMs."[^c16] A different population of systems could have a different ratio.
- Averaging can change the target, not only the noise. The paper cautions that "there are some caveats if our goal is to improve a particular eval metric using all the best available methods."[^c17] Its example is that "This big improvement in expected accuracy might be trivially achievable by majority voting."[^c18] An average-over-samples score and a best-answer score can rank models differently, so the averaging gain is a gain in precision for the expected score, not automatically for the score a user cares about.

## Related

- [[paired-eval-comparison]] — the comparison that removes the shared data term from a difference between two models.
- [[run-to-run-spread]] — the run-level spread of agent evaluations; in this decomposition it is mostly prediction-side variation, while the question-pool part is not visible from repeated runs on the same tasks (my reading).
- [[minimum-detectable-effect]] — the variance term that this split feeds into; averaging shrinks only the prediction part of it.
- [[multi-seed-bias-score-averaging]] — averaging over many seeds as the lever on the prediction term.

[^c1]: arxiv-2512-21326 — "Total variance = data variance + prediction variance."
[^c2]: arxiv-2512-21326 — "The prediction noise comes from generating different answers on a given question with the same model."
[^c3]: arxiv-2512-21326 — "The eval data sampling noise comes from sampling a particular set of N questions instead of another equally good N questions from the unobservable population of questions."
[^c4]: arxiv-2512-21326 — "While prediction variance can be reduced by averaging, the data variance is irreducible and can be large when the questions vary in their difficulties."
[^c5]: arxiv-2512-21326 — "Unlike the prediction noise, the data noise cannot be directly measured by evaluating on the fixed, given set of questions"
[^c6]: arxiv-2512-21326 — "Averaging is the most general and effective, which we will focus on."
[^c7]: arxiv-2512-21326 — "Fixing the random seed or lowering the temperature is brittle, which only works on the exact same model."
[^c8]: arxiv-2512-21326 — "the data standard error (SE) is typically less than 1/2 of the prediction SE between different final models"
[^c9]: arxiv-2512-21326 — "If we average over 36 predictions, then the total SE would be"
[^c10]: arxiv-2512-21326 — "corresponds to the data noise after averaging away some prediction noise."
[^c11]: arxiv-2512-21326 — "and corresponds to the total noise."
[^c12]: arxiv-2512-21326 — "On most evals, we care about the underlying ability measured by the eval rather than the specific questions of the eval, so the data noise must not be ignored."
[^c13]: arxiv-2512-21326 — "Other than sampling, additional prediction noise can come from inference-time choices such as prompt formatting, hyperparameters, and answer extraction"
[^c14]: arxiv-2512-21326 — "The predictions of Llama on vLLM is more deterministic than expected and thus has higher data noise than others, likely due to faulty settings."
[^c15]: arxiv-2512-21326 — "it is not observed in experiments such as the training curve (Example 2) and varying the training seeds"
[^c16]: arxiv-2512-21326 — "We speculate that the uniformity of these results comes from the relative similarity among LLMs"
[^c17]: arxiv-2512-21326 — "there are some caveats if our goal is to improve a particular eval metric using all the best available methods"
[^c18]: arxiv-2512-21326 — "This big improvement in expected accuracy might be trivially achievable by majority voting"
