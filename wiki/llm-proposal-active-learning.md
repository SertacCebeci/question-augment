---
description: "An LLM proposes the next experiment from a text history of prior results; on four materials datasets it reached the optimum in fewer iterations than UCB-driven ML baselines in most scenarios."
aliases: ["LLM-AL", "training-free LLM active learning", "LLM as surrogate in pool-based active learning", "LLM-driven pool-based active learning"]
sources: ["arxiv-2511-19730"]
---
# LLM proposal active learning

Pool-based active learning picks the next experiment from a set of unlabeled candidates. The classical version scores each candidate with a model fitted to the data seen so far, "predictive models trained on data seen so-far and" an uncertainty estimate, and then applies an acquisition rule.[^c1] The baselines in the study use the upper confidence bound, "used the upper confidence bound (UCB) acquisition function across all models", computed as µ + ασ from the predicted mean and uncertainty of each surrogate.[^c2]

The LLM variant replaces the fitted surrogate with a pretrained language model that reads the history as text. The prompt carries the dataset context, the optimization objective and the observed points: "For each dataset, we designed a prompt that includes the dataset context, the optimization objective, and the observed data points".[^c3] At each iteration "the LLM proposes a new experimental input".[^c4] The proposal is a string, not a label. It is matched to the nearest unlabeled point in the pool, the matched point returns its known value, and that point joins the observed set: "input string is matched to the closest data point" in the pool.[^c5] The loop stops once the dataset's best value is found.[^c6]

Nothing is fitted. The paper calls the method training-free, operating "with fixed pretrained weights and relying solely on prompt engineering to guide experimental selection".[^c7] What changes between iterations is the prompt, which grows by one observation. The motivation the paper gives is that classical surrogates "rely heavily on task-specific feature engineering and sufficient labeled data".[^c8] The transferable idea is that the record of experiments can itself be the representation, so no per-domain feature design is needed before the first proposal.

## What was measured

Four pool-based benchmarks: matbench_steels (yield strength, maximized), P3HT/CNT (electrical conductivity, maximized), Perovskite (instability index, minimized) and Membrane (elastic modulus, maximized). The pools hold 73 to 323 points.[^c25] Each dataset was run with two prompt formats: a parameter format of feature–value pairs, and a report format in which the same inputs are rewritten as a narrative. The baselines were GPR, RFR, XGBoost and a Bayesian neural network, each with UCB and α swept from 0 to 5.

On matbench_steels the parameter format reached the best candidate "identifying the best candidate using only 18%" of the data, while the report format "the performance dropped noticeably".[^c9][^c10] On P3HT/CNT, Perovskite and Membrane both formats "converge to the optimal candidate using fewer iterations compared to traditional ML models", including in their worst runs.[^c11] The abstract summarizes the gain as a reduction "of experiments needed to reach top-performing candidates by over 70%".[^c12]

The trajectories show a second thing. In standardized feature space the LLM travels about as far as a random walk, yet on Membrane "moves as extensively as a random walk yet is able" to find the optimum far sooner than the models.[^c13] The authors suggest the proposals follow semantic priors rather than learned feature correlations, and they add that "These interpretations remain hypothesis-driven and require further validation."[^c14] For a reader this separates two properties a search can have: how far it moves and how soon it reaches the target. Here the two come apart.

The prompt format matters, and the best format depends on the data. "datasets containing many independent variables (e.g., compositions) favor parameter-format" prompts, while the narrative format was the stronger one on the procedural Membrane data.[^c26][^c27] See [[medium-context-sweet-spot-for-numeric-prediction]] for the same pattern in another setting.

## Variability

Non-determinism is a real source of spread. The paper states that LLM responses "can vary even when using identical input prompts and a temperature of 0".[^c15] Comparing repeated runs at one seed with runs across five seeds, the paper finds the repeated-run variance "is of magnitude similar to the variance across different seeds", and reads most of the spread as "intrinsic to the LLM itself rather than" to the initial pool.[^c16][^c17] The report-format prompts varied more, which the authors attribute to length: "Longer, narrative-style prompts may amplify sensitivity to small changes in token generation".[^c18] The sampling is small: each setting was run as "five random seeds and five repeated runs", ten runs in all, and the sections read report no significance test. A single run cannot carry a difference; see [[run-to-run-spread]].

## Limits

- Four datasets, one model (the study used "claude-3.7-sonnet [39] at temperature = 0"), batch size one, and small pools.[^c21] The paper's own scope is narrow: LLM-AL is "particularly effective in problems with low-to-moderate dimensional search spaces".[^c19] Behaviour in large, high-dimensional pools is not shown here.
- The stopping rule uses the known optimum: "The AL loop terminates once the optimized target value is reached."[^c6] The reported iteration counts measure time to a known best. A real campaign has no such stop, so these numbers do not by themselves give a rule a lab could apply. My inference.
- Pretraining contamination is not excluded. The paper says that some benchmarks, "particularly matbench_steels, may appear in the scientific literature and thus be included in the model".[^c20] Only Membrane is claimed to be unpublished: "is fully original and has never".[^c24]
- The matching step ties every proposal to the pool. The sections read do not report how far proposals sit from their matches; the similarity scores are said to be in the supplement, which was not read here. My inference: when a proposal lies far from every pool point, the outcome depends on the reranker as much as on the LLM.
- Prompt design is itself a tuning choice. The paper concedes that "form of hyperparameter selection, its conceptual" simplicity is the contrast with the ML baselines.[^c22] Both formats were run on every dataset and the better one was known afterwards, while the baselines' α was swept over a range. The comparison is therefore not like for like. My inference.
- The mechanism is the authors' hypothesis, not a tested account (see the trajectory paragraph above).

## Related

- [[active-in-context-learning]] — a frozen in-context predictor where a query rule chooses which labels to add; here the model itself proposes the next point and no acquisition rule is applied.
- [[run-to-run-spread]] — the same warning that one run is one draw, here for repeated LLM runs at temperature 0.
- [[medium-context-sweet-spot-for-numeric-prediction]] — added narrative context can help or hurt, and the sign depends on what the added text carries.

[^c1]: arxiv-2511-19730 — "predictive models trained on data seen so-far and"
[^c2]: arxiv-2511-19730 — "used the upper confidence bound (UCB) acquisition function across all models"
[^c3]: arxiv-2511-19730 — "For each dataset, we designed a prompt that includes the dataset context, the optimization objective, and the observed data points"
[^c4]: arxiv-2511-19730 — "In each iteration, the LLM proposes a new experimental input"
[^c5]: arxiv-2511-19730 — "input string is matched to the closest data point"
[^c6]: arxiv-2511-19730 — "The AL loop terminates once the optimized target value is reached"
[^c7]: arxiv-2511-19730 — "with fixed pretrained weights and relying solely"
[^c8]: arxiv-2511-19730 — "rely heavily on task-specific feature engineering and sufficient labeled data"
[^c9]: arxiv-2511-19730 — "identifying the best candidate using only 18%"
[^c10]: arxiv-2511-19730 — "the performance dropped noticeably"
[^c11]: arxiv-2511-19730 — "converge to the optimal candidate using fewer iterations compared to traditional ML models"
[^c12]: arxiv-2511-19730 — "of experiments needed to reach top-performing candidates by over 70%"
[^c13]: arxiv-2511-19730 — "moves as extensively as a random walk yet is able"
[^c14]: arxiv-2511-19730 — "These interpretations remain hypothesis-driven and require further validation"
[^c15]: arxiv-2511-19730 — "responses can vary even when using identical input prompts and a temperature of 0"
[^c16]: arxiv-2511-19730 — "is of magnitude similar to the variance across different seeds"
[^c17]: arxiv-2511-19730 — "intrinsic to the LLM itself rather than"
[^c18]: arxiv-2511-19730 — "Longer, narrative-style prompts may amplify sensitivity to small changes in token generation"
[^c19]: arxiv-2511-19730 — "particularly effective in problems with low-to-moderate dimensional search spaces"
[^c20]: arxiv-2511-19730 — "may appear in the scientific literature and thus be included in the model"
[^c21]: arxiv-2511-19730 — "claude-3.7-sonnet [39] at temperature = 0"
[^c22]: arxiv-2511-19730 — "form of hyperparameter selection, its conceptual"
[^c24]: arxiv-2511-19730 — "is fully original and has never"
[^c25]: arxiv-2511-19730
[^c26]: arxiv-2511-19730 — "datasets containing many independent variables (e.g., compositions) favor parameter-format"
[^c27]: arxiv-2511-19730 — "report-format prompt is particularly effective"
