---
description: "Answer verification that runs the candidate and reference through an interpreter, so numeric and algebraic equivalence is computed, not judged from the model's own arithmetic."
aliases: ["tool-augmented answer verification", "tool-augmented verifier", "computation-checked answer equivalence"]
sources: ["arxiv-2512-01224"]
---
# Executable answer verification

Answer verification asks whether a candidate response matches a reference answer. Formally it is a verifier that maps the questions, candidate answers and reference answers to binary verdicts, and the verdicts serve as the signal in data curation, evaluation and reinforcement learning with verifiable rewards.[^e1] The two standing approaches differ in what they can compute. A rule-based matcher "extract[s] the final answer via heuristics and compare[s] it against the ground truth using predefined rules".[^e2] A model-based verifier "exploit[s] the flexibility of LLMs to interpret and evaluate unpredictable output".[^e3] Each fails on the cases this note is about. Rule matchers "struggle with unstructured model outputs".[^e4] Model verifiers "are still prone to hallucination", and their errors sit in "inconsistencies in numerical or symbolic reasoning".[^e5]

The executable variant gives the verifier an interpreter. It writes code for the comparison, a sandbox runs the code, and the verdict is the one that "gives its final judgement based on the sandbox output".[^e6] In the paper's example, a response written as 97 over (21√2 − 3) and a gold value (7√2 + 1)/3 do not look alike on the page. Both evaluated in code print the same value, "3.63316 3.63316".[^e7] The equality is then the result of an execution, not of the verifier's algebra. The loop carries a unit-conversion utility next to the interpreter, "Python interpreter and a unit-conversion utility",[^e8] and the numeric check is described as "tolerance-aware".[^e9]

What the work measured. A discrepancy analysis over 63,374 disagreement cases between existing verifiers and reference labels put calculation first: "Calculation inaccuracy represents the largest proportion of verification failures".[^e10] The verifier is then trained in two stages. A cold-start supervised stage on traces that reach a correct verdict through an explicit tool call is needed, because reinforcement learning directly on the base model "yields performance degradation", which the authors attribute to "limited tool-calling capabilities".[^e11] Without the cold start the model "fails to conduct accurate function calling" and "often becomes trapped in tool-use loops".[^e12] The reinforcement stage pays for a correct verdict, plus a tool term. The paper states the term as a bonus when the verdict is correct and at least one tool was used, and a penalty when it is wrong with no tool call.[^e13] Before reinforcement learning, the paper reports that "only 76% of tool-invoked verifications are initially correct".[^e14] On the samples that carry tool trajectories, accuracy "improved markedly from 76.9% to 90.0%" after RL, which the authors read as learning "how to leverage tools for accurate verification, rather than merely to initiate a tool call."[^e15]

Against baselines, the authors report that the 4B tool model beats chain-of-thought verifiers with fewer tokens, with the gap largest "especially on harder benchmarks like VerifyBench(hard) and Sci-Bench".[^e16] When the verifier serves as the reward in RL on competition math, they report that it "consistently outperforms both rubric-based and model-based verifiers" on AIME 2024 and 2025.[^e17]

The mechanism, stated plainly: the verdict moves from the verifier's own arithmetic to a value the executor prints, and the verifier decides only when to compute and how to phrase the code. What can be checked is what the code can express: a numeric value, a symbolic identity after simplification, a quantity after unit conversion.

What transfers. The part that should survive outside these benchmarks is that any equivalence reducing to a computed value can be settled by execution rather than by reading. The part that does not transfer is any answer without a computable form. A proof, an argument or a free-text claim gives the interpreter nothing to run. Translating a response into code is still a judgment made by the language model, and the executor cannot check that translation. The paper does not test translation errors; this is my inference from the design.

## Limits

- The abstract claims generalization to "general QA, and long-form reasoning tasks".[^e18] The parts read cover the method, the main table and the RLVR setup. The long-form and general-QA results were not read.
- The training labels are model-made. The annotation used three models, "for a total of nine per sample".[^e19] The verifier was trained on the set that keeps "any disagreement among these nine annotations".[^e20] Items the annotators agreed on are absent from that training set, and no human check of the labels appears in the parts read.
- The error taxonomy is model-made as well. "We first prompted Qwen3-32B to produce" an error category per sample, and a larger model then grouped them.[^e21] The "largest proportion" claim depends on that grouping.
- The 76%-to-90% figures are on the subset of samples that invoke tools. That subset changes as training changes which items the verifier computes, so the rise is not a rate on a fixed set of items. (my inference)
- The tool-term magnitudes, 0.5 and −0.5, are not varied in the parts read. The reward gives no penalty for a wrong verdict reached with a tool call, so a verifier that calls tools and is still wrong pays nothing extra. (my reading of the formula)
- Tolerance-aware numeric checks are a source of error the paper does not analyze in the parts read. The failure list the authors give for prior verifiers includes "Precision/Boundary Error: 7.8%".[^e22]
- The RLVR experiment is one 4B model, competition math, and a short run: "60 step for reinforcement learning".[^e23]

## Related

- [[tool-integrated-reasoning]] — the same call-and-resume loop, used by an answerer to compute; here the loop is used by a judge to check a finished answer.
- [[agentic-reward-model]] — a judge that calls tools to gather evidence; this note is the computation-only case, where the evidence is a printed value.
- [[benefit-scaled-tool-reward]] — how a tool call is priced in the reward; this verifier's tool term is gated on the verdict and adds a penalty for a wrong verdict without a tool.
- [[verifiability-routed-criterion-reward]] — sends checkable criteria to a deterministic check and the rest to a judge; executable verification is a deterministic check whose value is computed at verdict time.
- [[tool-output-loss-masking]] — the interpreter output stays in context but is excluded from the loss during training, as in this verifier's cold start.
- [[verifier-gain]] — a verifier's worth in rejection sampling; the paper does not measure that quantity, so the two notes answer different questions about verifiers.

[^e1]: arxiv-2512-01224 — "is the set of binary verification results"
[^e2]: arxiv-2512-01224 — "compare it against the ground truth using predefined rules"
[^e3]: arxiv-2512-01224 — "model-based verifiers exploit the flexibility of LLMs to interpret and evaluate unpredictable output"
[^e4]: arxiv-2512-01224 — "struggle with unstructured model outputs"
[^e5]: arxiv-2512-01224 — "inconsistencies in numerical or symbolic reasoning"
[^e6]: arxiv-2512-01224 — "gives its final judgement based on the sandbox output"
[^e7]: arxiv-2512-01224 — "3.63316 3.63316"
[^e8]: arxiv-2512-01224 — "Python interpreter and a unit-conversion utility"
[^e9]: arxiv-2512-01224 — "tolerance-aware numeric checks"
[^e10]: arxiv-2512-01224 — "Calculation inaccuracy represents the largest proportion of verification failures"
[^e11]: arxiv-2512-01224 — "limited tool-calling capabilities"
[^e12]: arxiv-2512-01224 — "and often becomes trapped in tool-use loops, harming performance"
[^e13]: arxiv-2512-01224 — "We award a bonus when the model is correct and uses an"
[^e14]: arxiv-2512-01224 — "only 76% of tool-invoked verifications are initially correct"
[^e15]: arxiv-2512-01224 — "how to leverage tools for accurate verification, rather than merely to initiate a tool call"
[^e16]: arxiv-2512-01224 — "especially on harder benchmarks like VerifyBench(hard) and Sci-Bench"
[^e17]: arxiv-2512-01224 — "consistently outperforms both rubric-based and model-based verifiers"
[^e18]: arxiv-2512-01224 — "general QA, and long-form reasoning tasks demonstrates strong generalization"
[^e19]: arxiv-2512-01224 — "for a total of nine per sample"
[^e20]: arxiv-2512-01224 — "any disagreement among these nine annotations"
[^e21]: arxiv-2512-01224 — "We first prompted Qwen3-32B to produce"
[^e22]: arxiv-2512-01224 — "Precision/Boundary Error: 7.8%"
[^e23]: arxiv-2512-01224 — "60 step for reinforcement learning"
