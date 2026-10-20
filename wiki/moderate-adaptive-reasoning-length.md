---
description: "On hard theory-of-mind tasks longer reasoning lowers accuracy; capping thinking length or stopping on repeated 'wait' beat unconstrained reasoning, and the best cap varies by model and task."
aliases: ["slow thinking collapse", "Slow-to-Fast reasoning", "adaptive reasoning budget"]
sources: ["arxiv-2602-10625"]
---
# Moderate, adaptive reasoning length

In a study of nine LLMs on three theory-of-mind benchmarks, reasoning models did not consistently beat non-reasoning ones and sometimes did worse; accuracy dropped as responses grew longer and larger reasoning budgets hurt.[^c1]

Capping length helps. Forcing thinking to end at a token threshold (appending the end-of-think tag) made Qwen3-8B-Reasoning reach 0.706 on HiToM at 1,500 tokens, above both reasoning and non-reasoning modes; Qwen3-32B-Reasoning at 1,000 tokens scored 0.728 on ToMATO against 0.714 unconstrained.[^c2] The best cap differs across models and across benchmarks for the same model, so no single limit exists and adaptive control is needed.[^c3]

Reasoning and non-reasoning modes are complementary: at HiToM order 4 the reasoning model uniquely solved 49 items, the non-reasoning model 39, and they agreed on 58.[^c4] Light chain-of-thought prompting on non-reasoning models also helped (DeepSeek-V3 0.665 to 0.723; Qwen3-32B 0.525 to 0.647).[^c5]

Slow-to-Fast (S2F) uses the count of "wait" tokens as a trigger: past a threshold, the slow trace is terminated and the model must answer intuitively.[^c6] Gains scale with difficulty: R1-Distill-Qwen-32B rose from 0.571 to 0.701 on HiToM, while on first-order ToMBench the effect was negligible.[^c7] The authors conclude models "do not lack ToM capabilities, but their wrong reasoning strategy damages performance."[^c8]

## Limits

Open-source models only for S2F; the threshold and benchmark-specific caps were tuned per setting, and how to choose effort dynamically is left open by the authors. Correlation of length with error may reflect harder items producing longer traces (my caveat; length-capping experiments partly address it). Only theory-of-mind tasks.

## Related

- [[reasoning-trap]] — more reasoning degrading outcomes
- [[thinking-stagnation]] — unproductive extended thinking
- [[deep-thinking-ratio]] — measures of thinking quality beyond length
- [[option-matching-shortcut]] — the paper's companion failure mode
- [[planning-theory-of-mind-elicitation-gap]] — theory of mind in LLMs

[^c1]: arxiv-2602-10625 — "accuracy significantly drops as responses grow longer, and larger reasoning budgets hurt performance."
[^c2]: arxiv-2602-10625 — "by restricting Qwen38B-Reasoning to think up to 1,500 tokens, we achieved a score of 0.706, surpassing both the non-reasoning and reasoning modes."
[^c3]: arxiv-2602-10625 — "Even for the same model, the best token length limits also vary across benchmarks"
[^c4]: arxiv-2602-10625 — "the Reasoning model uniquely solves 49 samples and the Non-Reasoning model uniquely solves 39, while they only agree on 58."
[^c5]: arxiv-2602-10625 — "the performance of DeepSeek-V3 and Qwen3-32B increases substantially from 0.665 to 0.723 and from 0.525 to 0.647, respectively."
[^c6]: arxiv-2602-10625 — "S2F uses the frequency of “wait” as a direct trigger for our dynamic intervention."
[^c7]: arxiv-2602-10625 — "the R1-Distill-Qwen-32B model’s performance surges from 0.571 to 0.701."
[^c8]: arxiv-2602-10625 — "They do not lack ToM capabilities, but their wrong reasoning strategy damages performance."
