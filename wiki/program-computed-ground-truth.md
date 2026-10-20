---
description: "A question's answer is the output of a program a code model writes and simulator geometry executes, with k sampled programs required to agree, instead of a human's or a model's reading."
aliases: ["code-based ground truth", "executable ground truth", "programmatic answer computation", "code as answer key"]
sources: ["arxiv-2512-16237", "arxiv-2512-10713", "arxiv-2512-05930", "arxiv-2512-00127", "arxiv-2511-21382"]
---
# Program-computed ground truth

A spatial question about a scene usually gets its answer from someone looking at the scene: an annotator reads the picture, or a model answers and is taken at its word. SPRITE moves the answer into a program. The paper names the change directly: "The core innovation of SPRITE is to reframe the ground-truth generation problem as a code-generation task."[^c1]

The mechanism has three steps. A language model writes the question in natural language, which is where the linguistic variety comes from. A code model then writes a function that takes the scene's meta-information as input and returns the answer. The program is "programmatically executed against highprecision scene meta-information (e.g., object poses, categories, and bounding boxes) extracted from advanced simulators."[^c2] The answer is therefore arithmetic on stored oriented bounding boxes, not a reading of pixels. In the paper's case study the height question becomes a loop that keeps the largest box height among the named objects, and the closeness question compares squared horizontal distances between box centres. Those are my reading of the figure's code, not statements in the text.

The check is a vote across samples. "for each question, we instruct code LLMs (Qwen3-32B) to generate k = 3 distinct programs for the same question by using diverse prompts."[^c3] The execution results of the candidates are compared by an LLM, and "Inconsistent answers lead to the question being filtered out."[^c4] Compound questions get a different check: an LLM judges whether the final answer follows logically from the sub-answers that were already computed.[^c5]

What the paper measured is a comparison, not an audit. On a 20k-sample test set drawn from 11k scenes, the code route was set against direct natural-language inference by the same model, with the model given the question and the serialised meta-information. The code route scored higher "on benchmarks like VSIbench, ERQA, and VGbench".[^c6] The overall scores were comparable, and the paper concedes that "NL direct inference retains reasonable accuracy for simpler queries", while its cost is that it "relies on longer context chains".[^c7]

The move changes what a wrong answer can be blamed on. A wrong label now points either to the metadata, to the program, or to a question the program could not express, instead of to a human's error in reading the scene.

A different route appears in PACIFIC, where the program is written once, by hand, rather than per question. Each instruction is a fixed function, and the framework stores its implementation in several languages.[^c11] A benchmark sample is a chain of those functions applied to a seeded input, and its expected output is the result of running the same chain: the expected results "are computed by executing reference implementations of the described tasks".[^c10] My reading, not the paper's: no vote across programs is needed, since each sample has one reference chain, and the answer is compared as a plain string or number. What is lost is SPRITE's per-question flexibility, because every question is the same kind of chain. Whether the reference implementations are themselves checked is not described in the text I read.

A third instance is PRiSM, a benchmark of university-level physics and mathematics problems whose per-instance code computes the ground truth with SymPy for symbolic math and Pint for units.[^c12] Before an answer is kept, the pipeline runs two checks. "First, dimensional validation verifies that all physical quantities" are consistent, and the program's outputs are compared with the expected numerical results.[^c13][^c14] My reading: this is a unit and numeric check on one reference program per problem, not a vote across programs. It catches dimensional and arithmetic slips; it would not catch a misreading of the question that the program and the problem text share. The passages read do not report how many instances the checks reject.

Checking the reference program itself is a separate step. The code-reasoning pipeline of arxiv-2512-00127 does it by agreement between artifacts rather than between answers: each candidate solution is run against each generated test, solutions with identical pass/fail patterns form a cluster, and a cluster scores its size times the number of tests all its members pass. The stated reason is that "if many independently generated solutions" all pass independently generated tests, "is statistically unlikely that both the solutions and" the tests are wrong.[^c15][^c16] My inference: this checks a program against an independently written test, not a vote over answers to one question, so a misreading that a solution and its test share would still pass. The paper's ablation gives the step a number. With "with only one solution and one test (Minimal Execution), there is no" guarantee of correct code, Pass@1 on LiveCodeBench-Exec was 62.1 ("the gap (62.1 vs."), against 68.2 with the selection, and the paper says this "68.2 on LCB) confirms this."[^c17][^c18][^c19]

The same division appears outside spatial questions, in generating unit tests. A test has an input part, which sets up objects and calls, and an expected-output part, which is the answer key for that test. TestChain gives "input design and the calculation of expected outputs to designer and calculator agents", with the calculator running a program.[^c20] The reported reason is that "Separate calculation lets input design focus on scenarios."[^c21] The program here is an executor of a value the designer's scenario fixes; it does not choose the scenario. In the parts read, the review reports the design without a measured comparison against a single agent computing both, so whether delegating the calculation improves the key is not established (my reading).

## Limits

The ground truth is only as good as the metadata. The paper drops the 'object view orientation' subtask of ViewSpatial because "the object-orientation metadata contains substantial errors."[^c8] Nothing in the text audits label accuracy against independent human judgement; the reported evidence is downstream benchmark score for models trained on each labelling.

Questions must be expressible as code over the stored fields. The generation prompt requires that "the proposed test questions require that they can be solved through code based on the meta-information of the object."[^c9] Perceptual or relational questions the metadata does not encode are outside the method. That boundary is my inference; the paper does not discuss it.

The k-program vote checks agreement among programs written by one code model from one question. A misreading of the question that the model shares across samples would pass the vote. This is my inference, not a tested failure.

The compound-answer check is itself an LLM judgement, so the code-verified part does not cover it.

## Related

- [[ground-truth-first-corpus-generation]] — the answer key is built before the text there, as stored facts rendered into documents; here the key is a program run over simulator geometry after the question exists.
- [[consensus-criterion-retention]] — a cross-generator agreement filter for rubric items, the same kind of vote used here across programs.
- [[business-truth-rate]] — another benchmark whose ground truth is executable and generated from a pinned seed.
- template-volume-saturation — the template baseline that this method is compared against on scale.

[^c1]: arxiv-2512-16237 — "The core innovation of SPRITE is to reframe the ground-truth generation problem as a code-generation task"
[^c2]: arxiv-2512-16237 — "programmatically executed against highprecision scene meta-information (e.g., object poses, categories, and bounding boxes) extracted from advanced simulators"
[^c3]: arxiv-2512-16237 — "we instruct code LLMs (Qwen3-32B) to generate k = 3 distinct programs for the same question by using diverse prompts"
[^c4]: arxiv-2512-16237 — "Inconsistent answers lead to the question being filtered out"
[^c5]: arxiv-2512-16237 — "For compound questions, we employ LLMs to assess whether the final compound answer is a logically consistent inference"
[^c6]: arxiv-2512-16237 — "achieving higher scores on benchmarks like VSIbench, ERQA, and VGbench"
[^c7]: arxiv-2512-16237 — "NL direct inference retains reasonable accuracy for simpler queries"
[^c8]: arxiv-2512-16237 — "the object-orientation metadata contains substantial errors"
[^c9]: arxiv-2512-16237 — "The proposed test questions require that they can be solved through code based on the meta-information of the object"
[^c10]: arxiv-2512-10713 — "are computed by executing reference implementations of the described tasks"
[^c11]: arxiv-2512-10713 — "instructions are implemented in multiple programming languages"
[^c12]: arxiv-2512-05930 — "such as SymPy (for symbolic math) and Pint (for unit consistency), supporting automated verification."
[^c13]: arxiv-2512-05930 — "First, dimensional validation verifies that all physical quantities"
[^c14]: arxiv-2512-05930 — "compares the outputs against the expected numerical results specified in the Output Map."
[^c15]: arxiv-2512-00127 — "is statistically unlikely that both the solutions and"
[^c16]: arxiv-2512-00127 — "if many independently generated solutions"
[^c17]: arxiv-2512-00127 — "with only one solution and one test (Minimal Execution), there is no"
[^c18]: arxiv-2512-00127 — "the gap (62.1 vs."
[^c19]: arxiv-2512-00127 — "68.2 on LCB) confirms this."
[^c20]: arxiv-2511-21382 — "input design and the calculation of expected outputs to designer and calculator agents"
[^c21]: arxiv-2511-21382 — "Separate calculation lets input design focus on scenarios."
