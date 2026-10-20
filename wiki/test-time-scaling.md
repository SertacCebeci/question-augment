---
description: "Spending extra inference computation (sampling, selection, self-critique) to raise accuracy without changing weights; the gain depends on the model and the task, not on the method alone."
aliases: ["TTS", "inference-time scaling", "test-time compute", "inference-time compute scaling"]
sources: ["arxiv-2512-11109", "arxiv-2512-05809", "arxiv-2512-05542", "arxiv-2512-03534", "arxiv-2512-02008", "doi-10-48550-arxiv-2602-10329", "arxiv-2511-21762", "arxiv-2511-18649", "arxiv-2511-17006"]
---
# Test-time scaling

Test-time scaling (TTS) is raising a fixed model's accuracy by spending more computation at inference, without touching its parameters. The study read here defines the idea as "allocating additional computation at inference".[^t1] It compares chain-of-thought prompting, Best-of-N sampling, self-consistency, beam search and iterative-self-refinement, "applied across both open-source and closed-source VLMs on the MathVista, MMMU, and MMBench benchmarks".[^t2]

Each method turns extra samples or steps into one answer by a different rule. Best-of-N needs a score per candidate: "The final answer is then selected based on a reward mechanism".[^t3] Self-consistency needs no score; it takes the answer that "appears most frequently across all reasoning paths".[^t4] Beam search keeps the top partial paths at each step under a score. So the selection step, not the sampling, decides whether extra compute helps. Sampling only produces candidates; a gain appears when the chosen candidate is more often right than the default.

The study's clearest finding about that step concerns the score. For open-source models the internal signal is weak: the "confidence score is not a reliable indicator of correctness".[^t5] An external verifier did better: "external verification is more effective than relying solely on the" model's own confidence.[^t6] In the Best-of-N comparison, the verifier-scored version beat the confidence-scored one across the open models tested.

The gain is also conditional on the model and the task. The authors conclude that "TTS is not a universal solution and must be tailored to both model capabilities and task characteristics".[^t7] On closed models, the TTS methods other than beam search "generally lead to noticeable improvements (relative to CoT)" on the math benchmark.[^t8] On MMBench, a perception-heavy benchmark, classical methods "produce minimal or no improvement" over zero-shot prompting.[^t9] The authors hypothesize the reason is that "errors in MMBench are primarily rooted in visual perception, not abstract logic".[^t10] This is their hypothesis, not a tested result. A reading of it: if most samples share one perception error, a vote over them keeps that error, which is the shape of failure described in [[shared-error-pattern]]. That step is my inference from the hypothesis, not the paper's.

A second axis is the prompt, not the samples. The PRIS study treats "the prompt as an equally critical and previously underexplored axis of inference-time scaling".[^t17] Its reported contrast is with a fixed prompt, whose best-of-N "plateaus on held-out evaluation beyond 1e3 NFEs" while the revised prompts kept improving.[^t18] The revision is driven by failures that recur across the sampled outputs, not by one output at a time; see [[common-failure-prompt-redesign]]. The comparison is on text-to-image and text-to-video generators, not on the language and multimodal reasoning tasks that the rest of this note covers.

A large study of language reasoning models adds a model-side dependence. Across eight open models it reports that "no single TTS strategy universally dominates"[^t19], and that the best strategy depends on the model's effective horizon ([[effective-reasoning-horizon]]). Beam search is its clearest case: it "exhibits a consistent inverse-scaling pattern: performance degrades monotonically as" the beam widens, in the short-horizon and non-reasoning families.[^t20] Unlike the verifier comparisons above, this study does plot accuracy against the width of the search, for language models on AIME and GPQA Diamond. Its summary claim is that "the optimal TTS performance scales monotonically with compute budget" for a given model type.[^t21] Whether that holds beyond these benchmarks is not tested in the text read.

A controlled test on a synthetic causal-attribution task, where the answer is a Boolean rule over candidate variables, separates instruction-tuned models from reasoning models. Instruction-tuned models "show a performance drop on XOR/XNOR" as the number of candidates grows, while reasoning models stay near-perfect; a direct-answer baseline "fails almost immediately".[^t22][^t23] The authors read the longer reasoning chain as a way to "stabilize latent representations of non-linear relationships", a reading they do not test mechanistically.[^t24] The same study finds that "character counts scale linearly with both N and T across all logic",[^t25] which is how the effort is observed; see [[resource-rationality]] for the cost reading and [[permutation-elimination-strategy-switch]] for the strategy shift inside those traces.

The same lever can be pulled for conformity to a stated goal rather than for accuracy. A rapid review of LLM alignment sorts methods by lifecycle phase; its inference-time class changes generation without touching weights, through reward-guided decoding, contrastive scoring or self-evaluation that steers which tokens are chosen.[^t27] Its examples are decoding-side. RAIN is described as "implementing a self-evaluation and rewind mechanism at inference",[^t28] and ARGS "adjusted token probabilities using a reward-guided scoring function".[^t31] The selection target here is a principle or preference, not a correct final answer, so the accuracy gains reported above do not carry over by default; that transfer is my inference, not a tested result. The review concludes that these methods "required fewer computational resources than training-based techniques".[^t29]

## Reasoning effort as a provider-side dial

Reasoning effort is a provider's setting rather than a sampling rule, and in one measured case it moved accuracy and cost together. On the 2026 Korean CSAT mathematics items, raising GPT-5 from minimal to high effort "raised performance from 82.6 to 100.0 (+17.4)".[^t32] The price was in tokens: usage went from about 60 to "tokens/problem to 240–268 tokens/problem, a four- to five-fold increase."[^t33]

The gain is not monotone at the bottom. "Notably, minimal or low reasoning sometimes reduced performance relative to the baseline,"[^t34] and the authors read this as extra reasoning being counterproductive for a model that already infers strongly. That reading is theirs, not a tested mechanism. At the top of the dial, accuracy rises only slightly while "token usage and cost rise by roughly 4–5 times."[^t35]

Their proposed remedy is configuration rather than a fixed maximum: "Achieving an optimal balance of reasoning depth therefore requires adaptive configuration based on model capability and problem difficulty."[^t36] The paper does not test such an adaptive policy (my inference from the text). Here no selection step is involved: the extra compute is spent inside one answer. The same effort-for-cost trade appears for judges in [[judge-reasoning-effort-tradeoff]].

When the scaled resource is the number of tool calls rather than tokens, a plain agent can leave its extra allowance unused. For Gemini-2.5-Pro on BrowseComp, "ReAct saturates at a budget of 100 on BrowseComp."[^t38] Under sequential scaling, where the agent is reminded "Wait, you still have remaining tool budget" when it proposes an answer,[^t39] the plain loop levels off; the authors report that showing the remaining budget "sustains gains beyond this plateau."[^t40] This is one model on one benchmark in the ceiling plot, and the limits of the awareness mechanism are in [[budget-awareness-signal]].

## Limits

- Three benchmarks and six models. The closed models were "Gemini 2.0 flash, GPT-4o mini, and Claude-3-Haiku" and the open ones were InternVL2.5 8B, Mulberry-8b and Qwen2.5-VL-7B-Instruct.[^t11] A pattern across these is not a law about VLMs in general.
- The methods varied across models "due to practical limitations". The confidence-based Best-of-N results "are omitted for closed-source models", so the closed-model comparison has fewer cells than the open-model one.[^t12]
- The sections read report one accuracy figure per cell and no interval. Whether the differences between methods exceed sampling noise is not established in them.
- The sections read give methods and accuracy, not a curve of accuracy against the number of samples. The name "scaling" is therefore not backed by a measured scaling law here.
- The authors' "adaptive TTS strategies" are proposed as future work. Nothing in the text tests a strategy that chooses a method per input.
- A verifier-scored world-model variant of test-time scaling does not scale on every benchmark. On SAT-Real a claim-based verifier improves accuracy, but on MMSI-Bench none of the verifiers, "including ours, achieve consistent scaling" with more imagined views.[^t15] The authors put the cause in the imagined evidence: "when imagined evidence lacks physical or relational fidelity, verification offers little benefit."[^t13] Their generator is one world model, "Camera (Zhou et al., 2025) as our world model"[^t14], so the claim is about that generator, not about world models in general.
- The causal-attribution result is one synthetic task, and its effort proxy is trace length. The authors offer a competing reading of that length: "reasoning length reflects limitations in attention-based state maintenance rather than deliberate resource allocation".[^t26]
- The review's cost ranking is not measured in it: it gives no cost figures of its own, and its own example shows cost moving rather than vanishing, since RAIN "increased inference time due to its inner loop".[^t30] A method that needs no training is not thereby cheap at answer time; the review does not separate the two costs.
- The reasoning-effort result comes from one model family on one exam of 46 items. The paper itself says its reasoning conclusions are "specific to GPT-5 and should be generalized to other architectures only with caution."[^t37]

## Related

- [[population-search-under-noisy-verifier]] — a verifier-scored population search is one TTS design, and it targets the same selection step.
- iterative-self-refinement — the sequential member of this family, whose gain also depends on the base model.
- [[verification-weighted-voting]] — a majority vote where verified answers carry more weight, a change to the selection rule.
- [[modal-centroid-selection]] — selection among N samples with no evaluator, a score-free alternative to the confidence and verifier signals here.
- [[shared-error-pattern]] — why voting fails when most candidates share one error.
- [[sufficiency-gated-imagination]] — world-model imagination on SAT-Real; that work gates whether to imagine, while the verifier work here scores the views once imagined.
- [[cross-model-best-of-n]] — the sampling side varied across models: one best-of-n budget drawn from several LLMs in sequence, selected by a reward-plus-agreement score.[^t16]
- [[common-failure-prompt-redesign]] — scales the prompt beside the samples, revising it from failures that recur across the scaled outputs.[^t17]
- [[effective-reasoning-horizon]] — the model-side cause the language-model study gives for which TTS strategy and trace length pay off.[^t19]
- [[judge-reasoning-effort-tradeoff]] — the same effort-for-cost trade, for LLM judges rather than answerers.

[^t1]: arxiv-2512-11109 — "allocating additional computation at inference"
[^t2]: arxiv-2512-11109 — "applied across both open-source and closed-source VLMs on the MathVista, MMMU, and MMBench benchmarks"
[^t3]: arxiv-2512-11109 — "The final answer is then selected based on a reward mechanism"
[^t4]: arxiv-2512-11109 — "appears most frequently across all reasoning paths"
[^t5]: arxiv-2512-11109 — "confidence score is not a reliable indicator of correctness"
[^t6]: arxiv-2512-11109 — "external verification is more effective than relying solely on the"
[^t7]: arxiv-2512-11109 — "TTS is not a universal solution and must be tailored to both model capabilities and task"
[^t8]: arxiv-2512-11109 — "generally lead to noticeable improvements (relative to CoT)"
[^t9]: arxiv-2512-11109 — "produce minimal or no improvement"
[^t10]: arxiv-2512-11109 — "errors in MMBench are primarily rooted in visual perception, not abstract logic"
[^t11]: arxiv-2512-11109 — "Gemini 2.0 flash, GPT-4o mini, and Claude-3-Haiku"
[^t12]: arxiv-2512-11109 — "The Best-of-N (confidence-based) results are omitted for closed-source models"
[^t13]: arxiv-2512-05809 — "when imagined evidence lacks physical or relational fidelity, verification offers little benefit"
[^t14]: arxiv-2512-05809 — "Camera (Zhou et al., 2025) as our world model"
[^t15]: arxiv-2512-05809 — "including ours, achieve consistent scaling"
[^t16]: arxiv-2512-05542 — "a sequential multi-LLM alternative to the prevailing single-model best-of-n"
[^t17]: arxiv-2512-03534 — "the prompt as an equally critical and previously underexplored axis of inference-time scaling"
[^t18]: arxiv-2512-03534 — "plateaus on held-out evaluation beyond 1e3 NFEs"
[^t19]: arxiv-2512-02008 — "no single TTS strategy universally dominates"
[^t20]: arxiv-2512-02008 — "exhibits a consistent inverse-scaling pattern: performance degrades monotonically as"
[^t21]: arxiv-2512-02008 — "the optimal TTS performance scales monotonically with compute budget"
[^t22]: doi-10-48550-arxiv-2602-10329 — "IT models show a performance drop on XOR/XNOR"
[^t23]: doi-10-48550-arxiv-2602-10329 — "The direct answer baseline fails almost immediately, with accuracy quickly approaching chance levels or zero"
[^t24]: doi-10-48550-arxiv-2602-10329 — "it allows the model to stabilize latent representations of"
[^t25]: doi-10-48550-arxiv-2602-10329 — "character counts scale linearly with both N and T across all logic"
[^t26]: doi-10-48550-arxiv-2602-10329 — "reasoning length reflects limitations in attention-based state maintenance rather than deliberate resource allocation"
[^t27]: arxiv-2511-21762 — "Inference-time strategies modify generation behavior without updating model parameters"
[^t28]: arxiv-2511-21762 — "implementing a self-evaluation and rewind mechanism at inference"
[^t29]: arxiv-2511-21762 — "required fewer computational resources than training-based techniques"
[^t30]: arxiv-2511-21762 — "The method increased inference time due to its inner loop"
[^t31]: arxiv-2511-21762 — "args adjusted token probabilities using a reward-guided"
[^t32]: arxiv-2511-18649 — "raised performance from 82.6 to 100.0 (+17.4)"
[^t33]: arxiv-2511-18649 — "tokens/problem to 240–268 tokens/problem, a four- to five-fold increase."
[^t34]: arxiv-2511-18649 — "Notably, minimal or low reasoning sometimes reduced performance relative to the baseline,"
[^t35]: arxiv-2511-18649 — "token usage and cost rise by roughly 4–5 times"
[^t36]: arxiv-2511-18649 — "Achieving an optimal balance of reasoning depth therefore requires adaptive configuration based on model capability and problem difficulty."
[^t37]: arxiv-2511-18649 — "specific to GPT-5 and should be generalized to other architectures only with caution."
[^t38]: arxiv-2511-17006 — "ReAct saturates at a budget of 100 on BrowseComp"
[^t39]: arxiv-2511-17006 — "Wait, you still have remaining tool budget"
[^t40]: arxiv-2511-17006 — "Budget Tracker sustains gains beyond this plateau"
