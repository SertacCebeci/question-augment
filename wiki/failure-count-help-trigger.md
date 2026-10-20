---
description: "An agent asks an expert only after n consecutive sub-task timeouts; the threshold trades success against human time, and a dialogue-synthesising asker beats forwarding the raw log."
aliases: ["impasse-triggered help request", "autonomy threshold n_max", "human expert as interactive tool"]
sources: ["arxiv-2602-22546"]
---
# Failure-count help trigger

AHCE, a Minecraft agent, decides when to ask with a deliberately simple rule. A sub-task fails when its step count exceeds a maximum, and a counter of consecutive failures is incremented. Help is requested only when that counter exceeds a configurable n_max.[^c1] Before that, the agent runs self-correction cycles, so the expert is consulted only after autonomous attempts fail. The authors say this two-stage process minimises how often humans are interrupted and the expert's cognitive load.[^c2]

## The threshold as an autonomy dial

n_max sets the trade-off between success and human burden. As it tends to infinity the framework degrades to the fully autonomous baseline.[^c3] In an ablation on two tasks, the easy-ish "craft wooden sword" stayed at 100% success until n_max exceeded 5. For the multi-stage "craft stone pickaxe" success fell sharply for any n_max above 3.[^c4] The reported reading is that excessive autonomy on chained tasks lets the agent enter an unrecoverable state that self-correction cannot escape. Raising n_max from 1 to 3 cut the human participation ratio on the pickaxe task from nearly 30% to about 10%, so most savings come at low values. Human interaction time plateaued at roughly 50-60 s rather than reaching zero, which the authors read as the irreducible cost of diagnosing a missing core fact.[^c5] Total-time variance also grew with n_max, meaning more autonomy made outcomes less predictable.[^c6]

## How the question is asked

Once triggered, the asker is not a pass-through. A Human Feedback Module, an LLM trained with GRPO, alternates reasoning, queries to the expert and the expert's replies, then emits a structured plan. The expert is treated as an interactive tool, in the manner of search-tool reasoning.[^c7] It was trained only on the MuSiQue multi-hop QA set, with no Minecraft data, to learn the skill of using an outside knowledge source rather than game facts.[^c8]

The comparison is against AHCE-log, which just shows the expert the agent's action log. On hard tasks the 32B asker reached 82% success against 68% for the log baseline, and human interaction time fell from 310.1 s to 79.4 s (human ratio 20.5% to 6.3%).[^c9] The baseline without any expert reached 10% on hard tasks.[^c10] The authors' interpretation is that a structured plan synthesised with the expert avoids errors from applying raw, unstructured advice.

## Limits

- The trigger is a fixed counter on timeouts; it does not estimate whether the failure is a knowledge gap that an expert could fix. A desert-search failure and a missing-tool failure count the same (my reading).
- The n_max ablation covers two tasks and one model; n_max = 3 is tuned to that setting.
- The "experts" were 10 players with Minecraft experience, one trial per task; the success figures come from a 15-task custom benchmark, so effect sizes may not carry to other domains or noisier experts.
- The log baseline differs from the HFM in several ways at once (trained dialogue, structured output, model size), so the gain cannot be attributed to the dialogue policy alone; no ablation separates them.
- The "when" and "how" are evaluated together; the work does not test learned "when" policies.

## Related

- [[clarifying-interaction-decomposition]] — the when-to-ask / what-to-ask / how-to-use split; here "when" is a counter and "what" a trained dialogue
- [[help-seeking-reciprocity-cost]] — the cost side of asking for help
- [[noisy-expert-channel-local-query-elicitation]] — another treatment of an expert as a queried, imperfect channel

[^c1]: arxiv-2602-22546 — "where nmax is a configurable hyperparameter representing the agent’s degree of autonomy."
[^c2]: arxiv-2602-22546 — "This two-stage process is crucial"
[^c3]: arxiv-2602-22546 — "As nmax → ∞, our AHCE framework gracefully degrades to"
[^c4]: arxiv-2602-22546 — "the success rate plummets"
[^c5]: arxiv-2602-22546 — "it plateaus at a non-zero minimum"
[^c6]: arxiv-2602-22546 — "This high variance suggests that with greater autonomy"
[^c7]: arxiv-2602-22546 — "we posit that the human expert can be"
[^c8]: arxiv-2602-22546 — "we train it exclusively on the training set of MuSiQue"
[^c9]: arxiv-2602-22546 — "the required human interaction time drops from 310.1"
[^c10]: arxiv-2602-22546 — "the fully autonomous MP5-core baseline"
