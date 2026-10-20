---
description: "Each model gets a classifier over the task text that predicts, before any call, whether that model will succeed; tasks are dispatched to the most likely one or few models."
aliases: ["difficulty-aware dispatching", "VeriDispatcher", "pre-inference difficulty dispatch", "per-model difficulty predictor", "multi-LLM dispatch by predicted success"]
sources: ["arxiv-2511-22749"]
---
# Model-specific difficulty dispatch

A task's difficulty is not a property of the task alone. In the RTL-generation setting of this paper, "The key idea is that difficulty is model-dependent": a task hard for one model may be easy for another because of differences in training data or architecture.[^c1] The mechanism that follows is a predictor per answerer, run on the task text before any answerer is called.

Each model in a pool gets its own lightweight classifier, which the authors describe as a way to "learn its capability boundary" in place of a single global predictor.[^c2] The classifier reads a semantic embedding of the task description. Its label comes from that model's own record. Each benchmark task was expanded into prompt variants, and each variant was sampled ten times and checked by simulation and synthesis.[^c3] The score is the failure rate over those samples, "representing the empirical failure rate", and a cut at 0.5 makes the task hard or easy for that model.[^c4] The same text can therefore carry one label per model, and the authors read this as the point: "captures that difficulty varies across LLMs."[^c5]

At inference every classifier reads the new task description, and each returns a binary prediction of whether its model can produce a correct result without generating anything. These predictors "enable pre-inference difficulty assessment".[^c6] Routing then sends the task to the top-k models by predicted calibrated success, "where k models with highest predicted calibrated success probability are selected".[^c7] Calibration is a temperature scaling fitted on the validation split, "to improve probability calibration for reliable easy/hard predictions".[^c8] With k = 1 the task goes to one model. With k > 1 several models generate in parallel, "increasing success rate at higher computational cost".[^c9]

What was measured: the original benchmarks "are reserved for dispatching evaluation only",[^c10] and on them top-3 dispatch raised RTLLM pass@10 by 12.5% with no commercial model.[^c11] With commercial calls cut to 40%, the conclusion reports RTLLM gains of "up to 18.18% higher" than GPT-5, and the abstract gives the same configuration as an improvement "using only 40% of commercial calls".[^c12][^c21] On VerilogEval the reported gain over GPT-5 was 5.77%, "matching commercial models",[^c22] while the abstract says the method "maintains accuracy while reducing commercial usage".[^c23]

The commercial case shows which part of the mechanism survives when a model's internals are closed. For GPT-5 and Claude-4.5, "where internal hidden states are inaccessible", the authors use external embedding models as semantic proxies.[^c13] My reading: the features are then shared across models, and only the outcome labels stay model-specific. The authors concede that "While these cannot capture model-specific architectural biases".[^c14]

Transfer to asking and answering (my inference, not tested in the paper): a question's difficulty is a relation between the question and one answerer. Routing questions to answerers would need per-answerer outcome records, and the text alone might predict them as it does here. Whether a question-side predictor can be trained on answer outcomes for an open-ended question, where no verifier like simulation exists, is not shown.

## Limits

- The benchmarks are small, and the authors name this as the bottleneck: "small size of current RTL benchmarks, which constrains difficulty" prediction.[^c15]
- The expanded data are paraphrases, not new problems. One commercial model was used to "engineer each reference design into ten prompt variants",[^c16] so the 1,716 and 550 tasks share their reference designs. The classifier is tested on the original benchmarks, but my reading is that the training variants do not add independent problems, so the effective number of tasks is closer to the number of reference designs.
- Labels rest on one verifier (simulation and synthesis) for Verilog. The 0.5 cut and the filtering bounds are the authors' choices. My reading of the text is that it reports no sensitivity analysis for them.
- The signal is weaker where descriptions are short. "Richer task descriptions give difficulty predictors more semantic cues",[^c17] and "This semantic bottleneck explains the difference in gains" between the two benchmarks.[^c18] On VerilogEval, "improvements rely more on ensemble" diversity than on accurate prediction.[^c19]
- The cost reported is commercial calls, not total compute. Top-k dispatch multiplies calls, as quoted above.[^c9]
- One domain only. "Future work includes hierarchical dispatch" and extension to other EDA tasks are left open.[^c20]

## Related

- [[pre-generation-success-probe]] — the activation-based readout of the same per-model difficulty; the text-side classifier here needs no access to the answerer's internals, at the cost of its architecture-specific signal.
- [[learned-model-coordinator]] — a coordinator that reads its own hidden state each turn to pick a model; here the choice is made by a classifier on the task text before any call.
- [[model-orchestration]] — routes by phase to named models; here the routing key is a predicted success per model.
- [[calibrated-confidence-advantage-routing]] — routes between two models by calibrated confidence after they answer; this one routes before any answer exists.
- [[complexity-tiered-strategy-routing]] — routes by difficulty to a reasoning strategy inside one model; here difficulty is per model and picks the model.
- [[preemptive-complexity-estimation]] — estimates a question's difficulty from its text before reasoning, without naming which answerer it is for.
- [[model-dependent-benchmark-difficulty]] — the same finding that difficulty rankings shift with the model, seen there in a negotiation benchmark.

[^c1]: arxiv-2511-22749 — "The key idea is that difficulty is model-dependent"
[^c2]: arxiv-2511-22749 — "trains a lightweight classifier for each model to"
[^c3]: arxiv-2511-22749 — "we sample ten generations and verify them with simulation"
[^c4]: arxiv-2511-22749 — "representing the empirical failure rate"
[^c5]: arxiv-2511-22749 — "captures that difficulty varies across LLMs"
[^c6]: arxiv-2511-22749 — "enable pre-inference difficulty assessment"
[^c7]: arxiv-2511-22749 — "where k models with highest predicted calibrated success probability are selected"
[^c8]: arxiv-2511-22749 — "to improve probability calibration for reliable easy/hard predictions"
[^c9]: arxiv-2511-22749 — "increasing success rate at higher computational cost"
[^c10]: arxiv-2511-22749 — "are reserved for dispatching evaluation only"
[^c11]: arxiv-2511-22749 — "improves performance by 12.5% without any commercial model"
[^c12]: arxiv-2511-22749 — "achieving up to 18.18% higher on RTLLM"
[^c13]: arxiv-2511-22749 — "where internal hidden states are inaccessible"
[^c14]: arxiv-2511-22749 — "While these cannot capture model-specific architectural biases"
[^c15]: arxiv-2511-22749 — "small size of current RTL benchmarks, which constrains difficulty"
[^c16]: arxiv-2511-22749 — "engineer each reference design into ten prompt variants"
[^c17]: arxiv-2511-22749 — "Richer task descriptions give difficulty predictors more semantic cues"
[^c18]: arxiv-2511-22749 — "This semantic bottleneck explains the difference in gains"
[^c19]: arxiv-2511-22749 — "improvements rely more on ensemble"
[^c20]: arxiv-2511-22749 — "Future work includes hierarchical dispatch"
[^c21]: arxiv-2511-22749 — "improvement on RTLLM using only 40% of commercial calls"
[^c22]: arxiv-2511-22749 — "on VerilogEval compared to GPT-5, matching commercial models"
[^c23]: arxiv-2511-22749 — "VerilogEval maintains accuracy while reducing commercial usage"
