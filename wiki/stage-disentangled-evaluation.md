---
description: "Scoring a deep-research agent's planning, retrieval and reasoning against their own gold stage annotations, not only its final report, separates a failed plan from a failed search."
aliases: ["modular evaluation of deep research", "ADRA-Eval", "disentangled deep research evaluation", "stage-wise benchmark"]
sources: ["arxiv-2512-00986", "arxiv-2511-21380"]
---
# Stage-disentangled evaluation

A deep-research system answers a question in stages. It plans sub-tasks, retrieves evidence for them, and reasons the evidence into a report. An end-to-end score reports only the product. The paper's objection is that evaluation "typically reports only aggregate success without disentangling planning, retrieval, and reasoning capabilities".[^s1] Its causal point is that "poor retrieval may be induced by an incorrect plan rather than shortcomings in the search process itself".[^s2] A low retrieval score can therefore be the symptom of a plan error, and an end-to-end number cannot say which.

The ADRA-Bank design scores each stage against its own ground truth. Planning is compared with expert plans: "we compare decomposed sub-tasks provided by agents against research plans annotated by experts based on the structural outline of papers", measuring coverage of required sub-tasks, redundancy and correctness.[^s3] Retrieval uses the paper's citations as provenance, "using the citations of papers as a verifiable ground truth".[^s4] Reasoning is scored with boolean diagnostics built from the paper's key findings. The stages can be run on their own, as "an isolated evaluation for foundational LLMs as potential backbones",[^s5] or chained so that the stage outputs feed one another and the end-to-end score is measured: they "can also be integrated into a closed loop to measure the end-to-end performance of a DR system".[^s6]

The value of the design is in the pairing. Isolated module scores say what a backbone can do alone; the closed-loop run says what the agent does when its stages feed one another. Comparing the two is what allows a stage score to be read causally, which is the step the plan-injection ablation takes.

A software-engineering study applies the same idea to an agent that adapts a research artifact to a new dataset. The authors cut the task into five stages (read the required files, edit or create them, generate and run the commands, validate and repair, compare the final output) and gate each stage on the one before it. The first stage counts as complete "only if it reads all the necessary files at the beginning."[^s7] The result shows where the chain breaks: "Step 2, which involves editing or creating the necessary files, emerges as the primary bottleneck" of the pipeline, and in most cases the agents "fail to even locate all the essential files in Step 1."[^s8][^s9] The stage gold is built from people rather than from a citation graph: two developers did the task and "recorded the files they accessed" to define the necessary files.[^s10] The gate makes a late failure readable as a symptom of an early one, which is the causal reading asked for above. The paper does not model the dependency beyond the gate.

## Limits

- The stage ground truths are tied to authored papers: the plan is the paper's outline and the evidence is its citations. A question whose sub-tasks have no such structured source has no comparable gold, so the design transfers only where such a source exists (my inference from how the gold is built).
- Citations as provenance treat the cited papers as the correct evidence. A valid source the paper did not cite is scored as a miss, so retrieval scores measure agreement with the citation graph, not evidence quality in general (my inference).
- The causal link from plan error to retrieval failure is the authors' motivating claim. The passage read does not measure how often a retrieval failure traces to the plan rather than to search.
- The benchmark is 200 instances across 10 academic domains. The result tables split the scores into research and review papers, and the passage read gives no confidence intervals, so small cells may carry wide uncertainty.
- Stage metrics are the benchmark's own (set overlap for planning and retrieval, boolean accuracy for reasoning). That they track the quality a reader of the final report would judge is not shown here.
- The software-engineering stages assume an order the authors say the agents do not keep: "the agents do not always follow a strictly linear sequence of Step 1–5."[^s11] The gate is therefore a simplification. The stage rates come from eight cases on two repositories, and the final output is reproduced in only one of them,[^s12] so the stage counts are too few to separate causes (my inference).

## Related

- [[plan-injection-bottleneck]] — the gold-plan ablation that this design makes readable; a stage score is only causal if a stage can be swapped.
- [[failure-mode-taxonomy]] — the same aim of locating deep-research errors by stage, reached by coding execution logs rather than by gold annotations.
- [[process-report-alignment-evaluation]] — another evaluation of deep-research output that looks past the final report.

[^s1]: arxiv-2512-00986 — "typically reports only aggregate success without disentangling planning, retrieval, and reasoning capabilities"
[^s2]: arxiv-2512-00986 — "poor retrieval may be induced by an incorrect plan rather than shortcomings in the search process itself"
[^s3]: arxiv-2512-00986 — "we compare decomposed sub-tasks provided by agents against research plans annotated by experts based on the structural outline of papers"
[^s4]: arxiv-2512-00986 — "using the citations of papers as a verifiable ground truth"
[^s5]: arxiv-2512-00986 — "an isolated evaluation for foundational LLMs as potential backbones"
[^s6]: arxiv-2512-00986 — "can also be integrated into a closed loop to measure the"
[^s7]: arxiv-2511-21380 — "only if it reads all the necessary files at the beginning"
[^s8]: arxiv-2511-21380 — "Step 2, which involves editing or creating the necessary files, emerges as the primary bottleneck"
[^s9]: arxiv-2511-21380 — "fail to even locate all the essential files in Step 1"
[^s10]: arxiv-2511-21380 — "attempted the dataset adaptation task and recorded the files they accessed"
[^s11]: arxiv-2511-21380 — "the agents do not always follow a strictly linear sequence of Step 1–5"
[^s12]: arxiv-2511-21380 — "the multi-agent system successfully reproduces the final results of the studied tasks"
