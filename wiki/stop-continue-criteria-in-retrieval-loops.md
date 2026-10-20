---
description: "A multi-hop retrieval loop mostly stops at a fixed hop, token or latency budget; adaptive confidence or verifier stops are rare in the corpus and poorly calibrated under distribution shift."
aliases: ["stop/continue criteria", "stopping criteria for retrieval loops", "resource-constrained stopping", "hop budget"]
sources: ["arxiv-2601-00536", "arxiv-2512-20618", "arxiv-2512-20237", "arxiv-2512-13573", "arxiv-2512-05371", "openalex-org-w7128864259", "doi-10-48550-arxiv-2609-23986", "doi-10-48550-arxiv-2606-29090", "doi-10-48550-arxiv-2607-24800", "doi-10-48550-arxiv-2609-16453", "doi-10-48550-arxiv-2606-21553"]
---
# Stop/continue criteria in retrieval loops

A retrieve-reason loop has to decide when to stop asking. The paper states the trade plainly: "stopping too early misses necessary evidence, while stopping too late inflates prompt length and latency and increases exposure to distractors."[^c1] Stopping is therefore a decision with two failure modes, and the paper treats it as axis D of the procedure described in [[retrieval-reasoning-procedure]].

The paper sorts stop criteria into families. The first is resource-constrained stopping, and here "many systems ignore the detailed state and instead impose hard budgets on search."[^c2] It has three subtypes. A rollout budget caps the number of steps: Self-Ask, ReAct, IRCoT and DRAGIN "restrict the number of reasoning or tool-use steps" and must answer when the budget runs out.[^c3] A token budget fixes the maximum retrieved or prompt tokens per question and truncates extra evidence or thoughts when the limit is reached.[^c4] A latency budget ends web or tool agents once "a wall-clock or API-call budget is consumed".[^c5]

The second family is confidence- or uncertainty-based. The model, or a small auxiliary head, is asked how confident it is in the current answer, and the loop "stops once uncertainty falls below a threshold". Signals include "logit margins, entropy, and disagreement across self-consistent samples".[^c6] The third family is verifier- or prompt-based. A checker "delegates the stop / continue decision to a verifier": a draft answer's claims are checked against the retrieved evidence, and a positive verdict ends the loop while unsupported claims trigger more retrieval.[^c7] Learned sufficiency critics in multi-round RAG are, in the paper's words, "viewed as learned verifiers".[^c8]

How common each family is in the corpus is the most concrete measurement the paper offers. Of the 104 systems, "97/104 systems (93.3%) impose explicit hop, token, or latency budgets".[^c9] Verifier- or PRM-based stopping "remains less common but growing (15/104, 14.4%)", and "only 2 systems (1.9%) explicitly use uncertainty- or confidence" stopping.[^c10][^c11] In this corpus, then, the stop decision is mostly a fixed budget rather than a state-dependent test.

On what budgets do, the authors write: "Static hop/token budgets can be competitive when tuned in-domain, but they transfer poorly" across datasets with different hop and distractor profiles.[^c12] On what adaptive stops do, the cross-paper tendency is that "uncertainty- or value-based stopping (Axis D) helps controllers avoid both over- and under-search".[^c13]

A stop of a different kind appears in MemR3, which keeps a tracked evidence and gap state and stops on that state rather than on a count. Its router answers once the gap is empty, and a hard iteration budget forces an answer when the loop runs out.[^c17][^c18] This is a state test, not a confidence or verifier test; the state itself is described in [[evidence-gap-state]], and the paper does not separate the state stop from the budget in its reported results.

One controlled sweep of a hard cap exists outside the retrieval-loop corpus. In LongVideoAgent the master decides when to answer, and a step cap K bounds the loop. Varying K with the other settings at their defaults, answer accuracy goes "from 68.30 to 73.67" between K=2 and K=5, and "K=10 yields no additional gain in answer accuracy."[^c17][^c18] The authors take K=5 as the default. The judged stop is the primary rule and the cap is its backstop: "the loop terminates when the master judges the accumulated visual evidence sufficient," which the paper states in those words.[^c19] The sweep shows where the backstop stops binding on one benchmark. It does not compare a fixed budget against an adaptive stop, so it does not settle the transfer question above.

A second cap sweep comes from MMhops-R1, a multimodal search agent trained with reinforcement learning on a benchmark of multi-hop image questions. There the maximum number of retriever interactions was varied over 2, 3, 4 and 5. The paper reports that "overall performance consistently improves" as the cap rises from 2 to 4, and that "increasing to 5 yields no significant" gain, at more computational cost.[^c20][^c21] The authors take four steps as the setting for their benchmark. This sweep is on a benchmark built to need several retrieval turns, and it shows the same pattern as the one above: the cap binds until it stops mattering. It does not compare the cap with an adaptive stop, so the transfer question above stays where it was.

A third kind of stop is value-based in a stricter sense: it measures how much a new batch of evidence changes the model's belief. ChipMind's retrieval is expanded in increments, and the marginal information gain of each increment is defined through the Kullback-Leibler divergence between the model's belief over answers with and without the new documents.[^c22] The divergence cannot be computed directly, so the paper approximates it: "we approximate Marginal Information Gain (MIG) by prompting the LLM to summarize" the context with and without the new nodes, and the gain is "estimated as the cosine distance between their embeddings".[^c23][^c24] The loop ends once the gain falls below a threshold τ, "indicating diminishing returns".[^c25] The motivation is that a fixed K fails both ways: "a small K misses crucial information, while a large K introduces noise."[^c26] In the paper's ablation, the adaptive-K mechanism is "the most critical for cross-module configuration localization tasks".[^c27] Its System Recall@20 is "99.2%, significantly outperforming" the single-pass baselines, HippoRAG 2 at 86.8% and BGE-M3 at 70.5%, though that comparison is the paper's own system against baselines it ran on its own benchmark.[^c28]

Jev-Mem replaces a count with a state test on four quantities that its controller estimates after each retrieval round: sufficiency, the expected utility of further retrieval, missing required evidence, and unresolved contradiction.[^c52] Retrieval ends with sufficient evidence when sufficiency clears its threshold while missing evidence and contradiction both stay below theirs.[^c53] A second exit needs no sufficiency. The loop also ends when expected utility falls under its threshold, which the paper reads as "indicating that additional traversal is unlikely to" improve the evidence, even when it is not fully sufficient.[^c54] The paper names the trade the two exits are meant to balance: stopping too early "risks missing necessary evidence, whereas uncontrolled expansion introduces irrelevant memories."[^c55]

A search proposal in the analytical direction draws the same line from the task side, not the controller side. It describes deep research as having "stopping criteria that are implicit, heuristic, or user-driven," and analytical search as explicitly structured with "well-defined termination" conditions, "conditions-such as satisfying evidential requirements or completing" a reasoning chain.[^c29][^c30] The proposal gives no stopping rule and no measurement, so it does not decide between the budget and state tests above (my reading).

A confidence-gated stop of this kind has also been measured on single-hop and two-hop question answering. AB-RAG starts with a small evidence set, answers, and scores its confidence; it returns the answer once confidence reaches a threshold, and otherwise enlarges the evidence set by a fixed step, stopping at a retrieval budget whatever the confidence.[^c38] The confidence is a weighted sum of three signals, and the model's own certainty carries the largest weight: on open models it is read from token probabilities, and on closed APIs it is the fraction of sampled answers that agree with the modal answer.[^c39][^c42] Used as a gate, the score separates correct from incorrect answers. On a closed model with TriviaQA, high-confidence answers reach 57.6% Exact Match while low-confidence answers reach zero.[^c40] On a closed model with HotpotQA the split is 36.5% against zero, and on a mid-sized Llama model it is 51.6% against 22.2%.[^c41] A threshold stop with an explicit cap is therefore also a point where the answer's correctness is informative, on these datasets; the stop is not only a cost cap.

A cap on steps can also be tested on a single controller, and there the cap is not a repair. In a knowledge-graph retrieval agent the authors run a version with "a lower step budget and tighter caps on global and neighborhood" calls.[^c47] Their abstract reports that stricter interaction budgets "shorten trajectories without repairing the policy."[^c45] The body states the same finding as "a stricter budget reduces trajectory length without recovering accuracy."[^c46] The cap changes how long the controller searches, not which nodes it chooses to search. That reading is mine, and the result is one controller on three graphs, not a sweep over budgets.

A further kind of stop reads the answer state itself. In one recent paper a predictor estimates, from the trajectory so far, the quality of the answer the loop would return at each iteration and the change that iteration brings. The rule stops when the current iteration reaches the high-quality, still-improving state; the paper's own words for that step are "if the current iteration reaches State 0, we stop".[^c59] The two predictions are used together, since the paper stops "only when they" give a clear and consistent signal.[^c60] Its reported result is that early stopping "reduces average iteration count by about 11%" while "preserving about 98% of the final answer quality achieved by" natural stopping.[^c61][^c62] Those figures come from sweeping two thresholds, so they describe a trade-off curve, and the quoted point depends on the operating point chosen (my reading).[^c63] The baselines are fixed caps: "As reference baselines, we use fixed-cap stopping".[^c64] The part of the paper that describes the controller evaluates it on the Search-R1 pipeline.[^c65] Because the predictors can read the trajectory alone, the stop need not probe an answer at every step: "stopping decision does not require probing at every iteration during" inference.[^c66]

The same kind of cap sweep appears in a text-only multi-hop QA ablation, run on a local 7B model. Its pipeline writes the sub-questions up front and runs the retrieval loop over them, with a default depth of five steps.[^c67] On 5,000 HotpotQA distractor questions, a single retrieval step costs 7.1 EM against the full loop, two steps come within 0.3 EM, and three steps are statistically indistinguishable from it.[^c70][^c71] The paper reads this as "Performance plateaus after 2 steps, capturing 95% of the gain from the full loop",[^c68] and concludes that "limiting the loop to two or three steps yields negligible" accuracy loss on this benchmark.[^c69] The comparison is between caps, with no adaptive stop in it, so the sweep shows where a fixed cap stops binding and does not test whether a state-based stop would do better. The depth is also entangled with decomposition: disabling decomposition "also collapses the loop to a single retrieval", so the decomposition ablation cannot be read apart from depth (the authors' caveat, and a single greedy run per condition).[^c72]

## Limits

The AB-RAG split is one paper's measurement on two QA sets, and the low-confidence groups are small in places: "the low-confidence group is large at sixtyone questions" is the paper's own phrase for the largest case, and the small Qwen model gives almost no low-confidence answers, which the paper sets aside.[^c43] Its calibration is within distribution. The paper does not test distribution shift, so it does not answer the calibration worry the paragraph above reports (my reading).

The budget result is about transfer, and the evidence for it is synthesis across papers with different retrievers and backbones, not a controlled sweep. The authors call such cross-paper comparisons "suggestive rather than definitive".[^c14] The adaptive-stop claim is weaker still: adaptive stopping "is evaluated on limited benchmarks and remains poorly calibrated under distribution shift".[^c15]

The count of two uncertainty-based systems says what was published, not whether uncertainty stopping works. Why so few use it is not in the text; cost of calibration and the lack of calibration evidence are my guesses, not the paper's finding.

The paper also reports a tendency that the most robust designs "pair an adaptive controller" with verifier or sufficiency triggers.[^c16] This is a pattern in the surveyed corpus, not a measured ranking of stop rules, and no stop rule is shown to be best in a matched comparison here.

A verifier stop has a cost the text does not quantify: the verifier is often another LLM or an NLI-style model, so each stop check adds calls. The paper gives no per-step cost figures for any family.

The information-gain stop has limits of its own that the parts of ChipMind read do not resolve. The gain it thresholds is not the KL divergence it stands for; it is a cosine distance between LLM summaries, so the stop inherits the summarizer's variance. The value of τ is not given in the parts read, and no sensitivity to τ is reported there. The adaptive-K result comes from one system on one benchmark built by its authors, and the 99.2% recall figure is not a comparison against a fixed budget tuned on the same data (my reading).

The word "stop" here carries no statistical guarantee. The sequential-test notion in [[stopping-rules]] controls error probabilities; the loop criteria above do not.

The Jev-Mem stop is not separated from the rest of its system in the reported results. The paper credits it along with routing, batching and a cheaper controller, saying that "stopping further avoids unnecessary traversal once sufficient evidence has been collected."[^c56] The build-time and latency figures are whole-system numbers, so they do not isolate the stop. The thresholds for the four tests are named but not given, and no ablation of this stop against a fixed hop or node budget appears in the parts read (my reading). The setup names two benchmarks, but the table reports LoCoMo alone,[^c57][^c58] so the evidence for this stop is one benchmark and the authors' own system. Calibration of the four estimates is not described, and the calibration gap named above applies here too (my reading).

## Related

- [[retrieval-reasoning-procedure]] — the four-axis frame in which stop/continue is axis D.
- [[stopping-rules]] — error-controlled sequential tests; the same word for a different object, a test of error, not a retrieval loop.
- [[multi-turn-conformal-stopping]] — a per-turn stopping threshold with an end-to-end coverage guarantee; in my reading it addresses the calibration gap the paper names, though it is not tested on multi-hop retrieval here.
- [[remaining-budget-penalty-in-action-scoring]] — a remaining-budget penalty inside action scoring, a budget that shapes choices rather than setting a hard cutoff.
- [[coverage-driven-retrieval-control]] — a control that stops from element coverage and marginal retrieval gain.
- [[uncertainty-guided-retrieval-triggering]] — the same uncertainty signal used on the trigger side, deciding whether to retrieve at all.
- [[anchor-guided-candidate-filter]] — the typed gate that prunes what an adaptive expansion pulls in, in the same paper.
- [[in-trajectory-answer-probing]] — the probed answer trace that the state-based stop above is trained to predict.
- [[decisive-iteration-sparsity]] — the per-iteration utility whose small, early non-zero values make a stop on utility plausible.

[^c1]: arxiv-2601-00536 — "stopping too early misses necessary evidence, while stopping too late inflates prompt length and latency and increases exposure to distractors"
[^c2]: arxiv-2601-00536 — "Many systems ignore the detailed state and instead impose hard budgets on search"
[^c3]: arxiv-2601-00536 — "restrict the number of reasoning or tool-use steps"
[^c4]: arxiv-2601-00536 — "fix the maximum retrieved or prompt tokens per question and truncate extra evidence or thoughts"
[^c5]: arxiv-2601-00536 — "agents terminate once a wall-clock or API-call budget is consumed"
[^c6]: arxiv-2601-00536 — "stops once uncertainty falls below a threshold"
[^c7]: arxiv-2601-00536 — "delegates the stop / continue decision to a verifier"
[^c8]: arxiv-2601-00536 — "viewed as learned verifiers"
[^c9]: arxiv-2601-00536 — "97/104 systems (93.3%) impose explicit hop, token, or latency budgets"
[^c10]: arxiv-2601-00536 — "remains less common but growing (15/104, 14.4%)"
[^c11]: arxiv-2601-00536 — "only 2 systems (1.9%) explicitly use uncertainty- or confidence"
[^c12]: arxiv-2601-00536 — "Static hop/token budgets can be competitive when tuned in-domain, but they transfer poorly"
[^c13]: arxiv-2601-00536 — "helps controllers avoid both over- and under-search"
[^c14]: arxiv-2601-00536 — "we treat cross-paper comparisons as suggestive rather than definitive"
[^c15]: arxiv-2601-00536 — "remains poorly calibrated under distribution shift"
[^c16]: arxiv-2601-00536 — "the most robust designs in our corpus pair an adaptive controller"
[^c17]: arxiv-2512-20237 — "a maximum iteration budget nmax that forces an answer action once the budget"
[^c18]: arxiv-2512-20237 — "the agent has accumulated adequate evidence and can safely"
[^c17]: arxiv-2512-20618 — "from 68.30 to 73.67"
[^c18]: arxiv-2512-20618 — "K=10 yields no additional gain in answer accuracy"
[^c19]: arxiv-2512-20618 — "terminates when the master judges the accumulated"
[^c20]: arxiv-2512-13573 — "overall performance consistently improves"
[^c21]: arxiv-2512-13573 — "increasing to 5 yields no significant"
[^c22]: arxiv-2512-05371 — "We quantify this impact using the Kullback-Leibler"
[^c23]: arxiv-2512-05371 — "we approximate Marginal Information Gain (MIG) by prompting the LLM to summarize"
[^c24]: arxiv-2512-05371 — "estimated as the cosine distance between their embeddings"
[^c25]: arxiv-2512-05371 — "indicating diminishing returns"
[^c26]: arxiv-2512-05371 — "a small K misses crucial information, while a large K introduces noise"
[^c27]: arxiv-2512-05371 — "mechanism is the most critical for cross-module configuration localization tasks"
[^c28]: arxiv-2512-05371 — "System Recall@20 of 99.2%, significantly outperforming"
[^c29]: openalex-org-w7128864259 — "with stopping criteria that are implicit, heuristic, or user-driven"
[^c30]: openalex-org-w7128864259 — "conditions-such as satisfying evidential requirements or completing"
[^c38]: doi-10-48550-arxiv-2606-29090 — "loop until the answer is confident enough or until a retrieval"
[^c39]: doi-10-48550-arxiv-2606-29090 — "This is why the final weights give Signal 1 the largest share at"
[^c40]: doi-10-48550-arxiv-2606-29090 — "reach 57.6% Exact Match while the low-confidence answers"
[^c41]: doi-10-48550-arxiv-2606-29090 — "closed model with HotpotQA the split is 36.5% against zero,"
[^c42]: doi-10-48550-arxiv-2606-29090 — "self-consistency [41]: the model is sampled k times at a nonzero temperature, and the signal is the fraction of samples that"
[^c43]: doi-10-48550-arxiv-2606-29090 — "the low-confidence group is large at sixtyone questions, so this is not a small-sample artefact."
[^c52]: doi-10-48550-arxiv-2609-23986 — "expected utility of further retrieval"
[^c53]: doi-10-48550-arxiv-2609-23986 — "Retrieval terminates with sufficient evidence when"
[^c54]: doi-10-48550-arxiv-2609-23986 — "indicating that additional traversal is unlikely to"
[^c55]: doi-10-48550-arxiv-2609-23986 — "risks missing necessary evidence, whereas uncontrolled expansion introduces irrelevant memories"
[^c56]: doi-10-48550-arxiv-2609-23986 — "stopping further avoids unnecessary traversal once sufficient evidence has been collected."
[^c57]: doi-10-48550-arxiv-2609-23986 — "memory on two widely used benchmarks."
[^c58]: doi-10-48550-arxiv-2609-23986 — "Performance on the LoCoMo benchmark evaluated using the LLM-as-a-Judge metric."
[^c59]: doi-10-48550-arxiv-2609-16453 — "if the current iteration reaches State 0, we stop"
[^c60]: doi-10-48550-arxiv-2609-16453 — "We therefore combine the two predictions and stop only when they"
[^c61]: doi-10-48550-arxiv-2609-16453 — "for early stopping reduces average iteration count by about 11%"
[^c62]: doi-10-48550-arxiv-2609-16453 — "while preserving about 98% of the final answer quality achieved by"
[^c63]: doi-10-48550-arxiv-2609-16453 — "We sweep the quality and utility thresholds"
[^c64]: doi-10-48550-arxiv-2609-16453 — "As reference baselines, we use fixed-cap stopping"
[^c65]: doi-10-48550-arxiv-2609-16453 — "we evaluate the controller on the Search-R1 pipeline using"
[^c66]: doi-10-48550-arxiv-2609-16453 — "stopping decision does not require probing at every iteration during"
[^c45]: doi-10-48550-arxiv-2607-24800 — "stricter interaction budgets shorten trajectories without repairing the policy"
[^c46]: doi-10-48550-arxiv-2607-24800 — "a stricter budget reduces trajectory length without recovering accuracy"
[^c47]: doi-10-48550-arxiv-2607-24800 — "a lower step budget and tighter caps on global and neighborhood"
[^c67]: doi-10-48550-arxiv-2606-21553 — "default T = 5"
[^c68]: doi-10-48550-arxiv-2606-21553 — "Performance plateaus after 2 steps, capturing 95% of the gain from"
[^c69]: doi-10-48550-arxiv-2606-21553 — "limiting the loop to two or three steps yields negligible"
[^c70]: doi-10-48550-arxiv-2606-21553 — "Reducing the retrieval loop to a single step (steps-1) incurs a"
[^c71]: doi-10-48550-arxiv-2606-21553 — "steps-3 is statistically indistinguishable from the"
[^c72]: doi-10-48550-arxiv-2606-21553 — "decomposition also collapses the loop to a single"
