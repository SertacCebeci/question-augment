---
description: "Each layer's True/False lean, read through the output head and weighed as supporting or attacking arguments, reproduces the model's answer; middle-layer disagreement tracks hallucination."
aliases: ["latent debate surrogate", "structured surrogate of LLM thinking", "single-inference internal debate"]
sources: ["arxiv-2512-01909"]
---
# Latent debate

A latent debate is disagreement that one model carries inside a single inference, instead of between several models. The authors define it as an "inconsistency inside the model that simultaneously carries" supporting and attacking arguments toward a claim.[^c1] The arguments are not sentences. They are the model's own hidden states, each read as an opinion: "We treat each hidden state hn as a" latent argument.[^c2]

The framework has three parts, and the paper instantiates them for True/False questions. First, an argument interpreter turns each hidden state into a stance. It projects the state onto the output vocabulary, and "This produces a probability distribution over vocabulary" tokens.[^c3] The probabilities of the True and False tokens then give the state's opinion on the claim: "and False, we can quantify the opinion of each latent" argument.[^c4] A state that leans True is a supporting argument; one that leans False attacks it.

Second, a thinking module aggregates these arguments. The authors choose "a symbolic approach, Quantitative Bipolar Argumentation" framework (QBAF).[^c5] Each argument starts from its normalized probability, and a gradual semantics propagates the attacks and supports into a final strength. That semantics is the authors' own: "We define a new semantics."[^c6] The output of the top-right node, which summarises the last layer, is the decision: "we use its output as this binary classifier."[^c7]

Third, the surrogate is checked against the model. The argument graph is laid out per layer and token, so a claim of N tokens over L layers gives N × (L − 1) arguments. The result the authors report is agreement with the model's own output, not with the truth: "Empirical studies demonstrate that our latent debate is a faithful structured surrogate model" of the LLM.[^c8] Consistency is measured as the share of items where the two decisions match, "instances on which the decision derived via the latent debate" equals the model's answer.[^c9] On Llama-13B the table gives 97.11% average consistency, where "method reaches 97.11% average consistency, while the best" non-debate baseline is lower.[^c10]

The same features carry a hallucination signal. The authors summarise each QBAF with the number of attacks and the mean and variance of initial and final strengths, computed separately for lower, middle and upper layers: "into three regions for better understanding internal mechanisms: lower, middle, and upper."[^c11] In a SHAP attribution over decision trees, the variance of initial strengths in the middle region is the strongest contributor: "(VarInit) shows the strongest influence in the task of hallucination detection, especially in the middle region, which" suggests middle-layer disagreement matters.[^c12] The paper's summary is that "high debates within a model tend to generated hallucinated" answers.[^c13] The motivating picture is the same: "More controversy leads to hallucination."[^c14]

## Limits

- The claim is tested on True/False claims only: "on three balanced true/false prediction datasets: common" claims, counterfact, company, plus three QA sets recast as binary claims.[^c15] The framework is described as model-agnostic, but one instance was measured, on three open-weight models: "meta-llama/Llama-3.1-8B, mistralai/Mistral7B-Instruct-v0.3, and meta-llama/Llama-2-13B."[^c16]
- Agreement with the model is not correctness. A surrogate that matches a wrong answer scores well. The authors say their "approach is not intended to improve the target" model's factuality.[^c17] The consistency result says the surrogate is faithful, and nothing about whether the model is right.
- "Hallucination" here means lack of factuality against world knowledge: the authors take the term to refer "to their (lack of) factuality, in the spirit" of earlier work.[^c18] Labels come from outside the model, and the detector is supervised: it is trained "to distinguish hallucinated from non-hallucinated outputs using features extracted from latent debate."[^c19] The surrogate itself is different: it works "without any tuning and training samples."[^c20] Do not carry the training-free claim over to the detector.
- The detection result is modest. The authors say the detector "can achieve a decent AUROC compared to baselines", not that it dominates them.[^c21]
- The SHAP analysis is association on a fitted tree. "to determine which features most strongly contribute to hallucination" is what it measures.[^c22] My inference: nothing in the text intervenes on middle-layer disagreement and checks that the output changes, so "linked to" is as far as the evidence goes.
- The gradual semantics is a new construction, and its formal guarantees live in an appendix this reading did not cover. My inference: whether another gradual semantics would give the same surrogate is not tested.
- Transfer to asking and answering. The mechanism is inside an open model's layers, which a human asker or answerer, or a closed model's user, cannot read. My inference: what survives is the bookkeeping idea, that a claim can be weighed by its reasons for and against and the balance read as a signal of commitment. The paper tests no human, no prompting strategy and no question-asking.

## Related

- [[logit-lens]] — the argument interpreter is the same readout, applied per layer to the True and False tokens rather than to the top token.
- [[grounded-argument-acceptance]] — Dung-style acceptance gives a unique status over an attack graph; the QBAF here is weighted and gradual, so its output is a strength, not a status.
- [[disagreement-retention-in-debate]] — debate among several models; latent debate is the single-inference analogue, where the arguments are layers, not agents.
- [[cross-layer-probe-ensemble]] — also draws on middle layers, but through learned probes combined by regression; latent debate reads the model's own head and trains nothing.

[^c1]: arxiv-2512-01909 — "inconsistency inside the model that simultaneously carries"
[^c2]: arxiv-2512-01909 — "We treat each hidden state hn as a"
[^c3]: arxiv-2512-01909 — "This produces a probability distribution over vocabulary"
[^c4]: arxiv-2512-01909 — "and False, we can quantify the opinion of each latent"
[^c5]: arxiv-2512-01909 — "a symbolic approach, Quantitative Bipolar Argumentation"
[^c6]: arxiv-2512-01909 — "We define a new semantics."
[^c7]: arxiv-2512-01909 — "we use its output as this binary classifier"
[^c8]: arxiv-2512-01909 — "Empirical studies demonstrate that our latent debate is a faithful structured surrogate model"
[^c9]: arxiv-2512-01909 — "instances on which the decision derived via the latent debate"
[^c10]: arxiv-2512-01909 — "method reaches 97.11% average consistency, while the best"
[^c11]: arxiv-2512-01909 — "into three regions for better understanding internal mechanisms: lower, middle, and upper."
[^c12]: arxiv-2512-01909 — "(VarInit) shows the strongest influence in the task of hallucination detection, especially in the middle region, which"
[^c13]: arxiv-2512-01909 — "high debates within a model tend to generated hallucinated"
[^c14]: arxiv-2512-01909 — "More controversy leads to hallucination."
[^c15]: arxiv-2512-01909 — "on three balanced true/false prediction datasets: common"
[^c16]: arxiv-2512-01909 — "meta-llama/Llama-3.1-8B, mistralai/Mistral7B-Instruct-v0.3, and meta-llama/Llama-2-13B."
[^c17]: arxiv-2512-01909 — "Our approach is not intended to improve the target"
[^c18]: arxiv-2512-01909 — "refers to their (lack of) factuality, in the spirit"
[^c19]: arxiv-2512-01909 — "to distinguish hallucinated from non-hallucinated outputs using features extracted from latent debate"
[^c20]: arxiv-2512-01909 — "without any tuning and training samples"
[^c21]: arxiv-2512-01909 — "We can see that our latent debate detector can achieve a decent AUROC compared to baselines"
[^c22]: arxiv-2512-01909 — "to determine which features most strongly contribute to hallucination."
