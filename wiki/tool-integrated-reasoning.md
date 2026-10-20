---
description: "A reasoning model pauses at each code block, an interpreter runs it, and the output re-enters the context, so computation is delegated mid-chain and the model reasons on the returned result."
aliases: ["code-integrated reasoning", "interleaved code execution", "tool-augmented reasoning", "TIR", "generate-pause-execute-resume"]
sources: ["arxiv-2512-20745", "arxiv-2512-19287", "arxiv-2601-11556", "arxiv-2512-14040", "arxiv-2512-10999", "arxiv-2512-07407", "arxiv-2511-21591"]
---
# Tool-integrated reasoning

In tool-integrated reasoning a model's chain of thought is interleaved with executable code. The trace has three kinds of segment: natural-language reasoning, a code block, and the interpreter's output. When the model closes a code block, generation is suspended, the code runs in a sandbox, and the result is added to the context as a new segment; generation then resumes and the model conditions on what came back.[^t1] The unit is a loop rather than a single call, so the same trace can hold several blocks, an error, and a revision.

The division of labour is that the expensive operations go to the interpreter while the language model keeps the plan. The AgentMath paper describes its data pipeline as one that "substitutes computationally intensive reasoning steps with executable code blocks" and their execution outputs.[^t2] Elementary arithmetic is left in text, which the authors say is to "prevent overdependence."[^t2b] The point is a choice about what the model should keep doing itself: the trace still contains the reasoning that motivates each call, and only the calculation is handed off.

What was measured. On Qwen3-8B-Base trained on the same 20k examples, the tool-augmented supervised model beats the text-only one, "surpassing the text-based baseline by 3.4% and 4.1%" on AIME24 and AIME25.[^t3] The larger difference is in reinforcement learning: the tool-augmented model reaches "steps to reach 76.2% (AIME24) and 67.5% (AIME25)" after about 400 RL steps, where the text model after SFT needed about 1600 steps to reach lower numbers.[^t3b] Sequences were also shorter by about 4k tokens, which the authors attribute to "precise code execution replacing verbose manual calculations."[^t4]

Tool use and accuracy. The authors report that "model accuracy continuously improves with increasing tool invocations," which they read as emergent code self-correction.[^t5] During RL the average number of tool calls per problem rose "from 27 to 31 calls per problem" while the cap was raised in stages, "from 48 to 72 (step 140) and then to 96 (step 320)."[^t6] So the rise in calls is partly a consequence of the budget schedule, not a free-standing behaviour.

A second setting, outside training, uses the same interpreter as a check rather than a computation engine. In the Vibe Reasoning case study a human steered a chat with a frontier model, and the authors' verdict on the code runs is that "Without code, the AI would have accepted" the model's wrong conjectures.[^t12] Their example is a closed formula the model proposed for tile counts, which a small enumeration contradicted: "Running enumeration code immediately showed" the mismatch.[^t13] Here the code is not offloading arithmetic from the chain; it tests a claim the model made against a computation the model did not produce, the outside check described in unreliable-self-evaluation. The paper reports this qualitatively, with no counts of caught errors, so the effect is described rather than measured.

A third setting moves the same loop from computation to retrieval. In CSyMR-Bench a question about a symbolic score is answered by decomposing it into atomic operations, which are "executed through verifiable tools" and whose returned evidence completes the reasoning chain.[^t14] The paper separates the loop from the tools with an ablation: a ReAct-style controller with no musical tools does not beat chain-of-thought. The authors read this as "indicating that reasoning structure alone" is insufficient, and conclude that it "is insufficient without effective grounding."[^t15] Adding the operators gives "yielding 5–7% absolute accuracy gains" over LLM-only approaches on the 126-item set.[^t16] The interface differs from the code-in-trace pattern above. A separate Tooler runs the operators, and the reasoner receives "solely natural-language evidence summaries", so what re-enters the context is a summary written by the tool layer, not the interpreter's raw output.[^t17]

A fourth setting puts the loop over a chart image. ChartAgent builds "over a dozen visual and reasoning tools" and has the model choose among them, with each step's output written to a log.[^t22] Its ablation credits the tool library most: "Eliminating the modular tool library leads to the largest degradation, with accuracy dropping from 78.6% to 75.4%."[^t20] The log is offered as a way to replay the answer: "users and researchers can replay the reasoning trajectory step by step to verify" that each operation is evidence-based.[^t21] That replayability is a property of the design. The read text reports no user study checking whether anyone verifies an answer this way, so the auditability is asserted rather than measured. The chart setting is also where the loop's robustness to removed printed labels is tested; see [[textual-annotation-dependence]].

A fifth setting puts the loop over a knowledge base rather than a computation. In KBQA-R1 each action is executed by a Freebase executor, and the result returns to the context: the executor runs the action "over K, yielding an observation", which is a set of retrieved entities or a diagnostic message.[^t23] The ablation removes the multi-turn loop, and the authors read the drop as showing that "iterative refinement through KB feedback is essential".[^t24] The re-entering segment here is the executed answer set of one validated step, and the actions are a fixed typed set rather than free code. The read slices do not say whether the single-turn variant was trained the same way, so the drop is the effect of removing the loop within this system. See [[stepwise-validated-logical-form]].

A sixth setting compares the same interpreter placed after the answer with one used during generation. In the Prolog study the single-try and multiple-try protocols run SWI-Prolog only once the model has answered, so the model "has no visibility into the execution result and cannot revise its output in response."[^t25] Its agentic protocols send failures back into the generation, where syntax errors, unbound variables and timeouts "trigger targeted feedback and enable the language model to iterate."[^t26] The two regimes come out in different places. On the in-distribution arithmetic set, "best-of-N with external verification maximizes in-distribution accuracy", while on zero-shot MMLU tests the interactive protocols "consistently outperform Single-Try and Multiple-Try inference."[^t27] My inference: here the re-entering segment is the interpreter's error text, so the loop serves repair rather than computation. The comparison is one 3B model trained on one dataset, so it shows the ordering in that study and nothing wider.

## Limits

The clean comparison is one backbone and one 20k dataset: "8B-Base as the backbone model and an identical 20k data." The headline 30B-A3B numbers come from a different, larger pipeline, so they do not isolate the effect of code.[^t7]

The tool-augmented data is a rewrite of the text data, not an independent sample. The teacher's simulated outputs are "systematically replaced with ground-truth execution results," which means the training traces differ in more than the presence of code.[^t8] The text does not separate those effects.

The call-count result is confounded. Accuracy, call count and the cap all rise over the same training run, so the claim that more calls cause better accuracy is not tested by varying the cap alone at a fixed model. That reading is mine, not the paper's controlled result.

The paper's own headline numbers disagree on HMMT25: the abstract gives "and 73.8% accuracy respectively"[^t9], and the conclusion gives "90.6%, 86.4%, and 78.9%".[^t10] In the slices read, all evaluation is competition mathematics; nothing shows the mechanism transfers to other domains.

The retrieval result rests on one backbone for every method, since the prompting baselines and agent controllers "are implemented with GPT-4.1-mini as the backbone model".[^t18] Its questions are also partly model-made: "plausible distractor options were synthesized using" GPT-4o-mini.[^t19] A gain on this one benchmark's average does not measure how much tools help in general.

Latency is a cost the mechanism creates. Sandbox calls make long trajectories uneven: "the rollout time for ultra-long sequences causes severe long-tail effects."[^t11] The paper answers this with asynchronous scheduling and partial rollouts, which are systems fixes, not part of the reasoning mechanism itself.

A tool loop also changes what a score measures. When the tool performs the search, the score says little about the model's own planning. The 8-puzzle study leaves code interpreters out for this reason: "code-based search largely masks planning and state tracking, since an external algorithm can solve the puzzle without the model needing to devise or maintain a long-term strategy."[^t28] That study's other route, supplying legal moves without code, still solves no puzzle, so the two kinds of help are measured separately; see [[valid-move-oracle-planning-residue]].

## Related

- [[structural-versus-parametric-evidence]] — which evidence a tool can supply at all: the same loop helps where the needed fact is a property of the object the tool reads, and gains little where it is a convention held outside that object.
- [[tool-output-loss-masking]] — the training side of the same trace: interpreter tokens stay in context but are excluded from the loss.
- [[code-offloaded-distillation]] — code computes over a corpus of extracted records after the model has stopped reading them; here the code runs inside one reasoning trace and the same model reads the result back.
- [[tool-type-confidence-dichotomy]] — code interpreters as verification tools that lower confidence; this note concerns whether they improve the answer, not how confidence moves.
- [[reflection-token-error-injection]] — another way to train revision from errors; here the errors are real execution failures.
- [[textual-annotation-dependence]] — the chart setting where the tool loop is compared with end-to-end models on charts whose printed numerals are removed.
- [[accuracy-auditability-trade-off]] — the Prolog study's case where the interpreter sits after an answer that alone is rewarded, and the model moves its reasoning into prose.

[^t1]: arxiv-2512-20745 — "generation is suspended while the extracted code undergoes execution"
[^t2]: arxiv-2512-20745 — "substitutes computationally intensive reasoning steps"
[^t2b]: arxiv-2512-20745 — "prevent overdependence"
[^t3]: arxiv-2512-20745 — "surpassing the text-based baseline by 3.4% and 4.1%"
[^t3b]: arxiv-2512-20745 — "steps to reach 76.2% (AIME24) and 67.5% (AIME25)"
[^t4]: arxiv-2512-20745 — "attributable to precise code execution replacing verbose manual calculations"
[^t5]: arxiv-2512-20745 — "model accuracy continuously improves with increasing tool invocations"
[^t6]: arxiv-2512-20745 — "frequency rose from 27 to 31 calls per problem"
[^t7]: arxiv-2512-20745 — "8B-Base as the backbone model and an identical 20k data"
[^t8]: arxiv-2512-20745 — "are systematically replaced with ground-truth execution results"
[^t9]: arxiv-2512-20745 — "and 73.8% accuracy respectively"
[^t10]: arxiv-2512-20745 — "90.6%, 86.4%, and 78.9%"
[^t11]: arxiv-2512-20745 — "the rollout time for ultra-long sequences causes severe long-tail effects"
[^t12]: arxiv-2512-19287 — "Without code, the AI would have accepted"
[^t13]: arxiv-2512-19287 — "Running enumeration code immediately showed"
[^t14]: arxiv-2601-11556 — "executes them through verifiable tools"
[^t15]: arxiv-2601-11556 — "is insufficient without effective grounding"
[^t16]: arxiv-2601-11556 — "yielding 5–7% absolute accuracy gains"
[^t17]: arxiv-2601-11556 — "returns solely natural-language evidence summaries"
[^t18]: arxiv-2601-11556 — "are implemented with GPT-4.1-mini as the backbone model"
[^t19]: arxiv-2601-11556 — "plausible distractor options were synthesized using"
[^t20]: arxiv-2512-14040 — "Eliminating the modular tool library leads to the largest degradation, with accuracy dropping from 78.6% to 75.4%"
[^t21]: arxiv-2512-14040 — "users and researchers can replay the reasoning trajectory step by step to verify"
[^t22]: arxiv-2512-14040 — "over a dozen visual and reasoning tools"
[^t23]: arxiv-2512-10999 — "executed by the executor E over K, yielding an observation"
[^t24]: arxiv-2512-10999 — "iterative refinement through KB feedback is essential"
[^t25]: arxiv-2512-07407 — "The model has no visibility into the execution result and cannot revise its output in response."
[^t26]: arxiv-2512-07407 — "trigger targeted feedback and enable the language model to iterate"
[^t27]: arxiv-2512-07407 — "best-of-N with external verification maximizes in-distribution accuracy"
[^t28]: arxiv-2511-21591 — "code-based search largely masks planning and state tracking, since an external algorithm can solve the puzzle without the model needing to devise or maintain a long-term strategy"
