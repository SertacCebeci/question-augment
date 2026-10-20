---
description: "Turning extended reasoning on for the same weights cut a multi-turn attack's success from 97% to 42% in one paired test; the mechanism is conjectured, not shown."
aliases: ["thinking mode", "deliberative inference", "reasoning mode as a safety lever"]
sources: ["arxiv-2512-07059"]
---
# Extended reasoning under framed requests

Extended reasoning, the mode in which a model works through a long intermediate deliberation before it commits to an answer, lowered how often a multi-turn adversarial attack succeeded. The study states the result in its abstract: "enabling extended reasoning on identical architecture reduced ASR from 97% to 42%".[^c1] The pair is Kimi K2 in standard inference and Kimi K2 Thinking, run under the same attack on the same behaviours, and the paper reports the gap as "Thinking mode reduces ASR by 55 percentage points but 42% of attacks still succeed".[^c2]

The attack behind the number is a branching search over conversation turns, not a single prompt. The search "Detects 11 resistance types and dynamically selects from 7 attack strategies"[^c3], so each branch is pushed by a framing chosen from how the target has just responded. The measure is therefore how often an answerer that deliberates first is still moved by a framed request that a standard answerer was moved by. Standard inference was moved 97% of the time, thinking inference 42%.

The paper's reading of the framing effect is that "The exceptional effectiveness of academic and research framing indicates that models lower safety thresholds when"[^c4] a request is presented as research. The thinking result is given a conjectured mechanism in the same discussion: "may reflect deliberative alignment: extended reasoning allows models to identify adversarial" framings that bypass a quick answer.[^c5] The authors add that this "benefit disappears against reasoning-aware attacks", citing an earlier study.[^c6]

The literature disagrees on the direction. The paper reports that "that thinking mode degrades safety [33, 35], while others report improvement [36, 37]."[^c7] Its reconciliation is a difference in attacks: "studies reporting degraded safety often use reasoning-specific attacks, while studies reporting improvement"[^c8] used general adversarial strategies. The pair measured here used general strategies, which is the condition under which the paper finds the benefit.

This wiki infers, without a test of its own, that the answerer's inference mode is a lever on whether a framed question gets the answer its framing invites. The structure may transfer: the same request can draw a different commitment depending on how much the answerer deliberates before committing, much as [[sycophantic-capitulation]] shows commitment moving under rebuttal across turns, and [[framing-dependent-premise-adoption]] shows premise acceptance moving with the claimed source. What does not transfer is the number. 97% and 42% are rates of a judged harmful output on a fixed behaviour set, not rates of good answers to questions. The same spend of inference compute that [[test-time-scaling]] studies for accuracy is here measured against a framing, which is a different object.

## Limits

- One pair. "Only one model pair (Kimi K2 standard vs. thinking)" was tested, so whether the drop holds for other thinking-enabled models is not known.[^c9]
- The behaviour set is small. "comprises 100 behaviors that may not capture the full range of harmful content", and the most sensitive categories are excluded, so the numbers may understate vulnerability there.[^c10]
- The mechanism is open. The authors ask: "Does extended reasoning enable identification of adversarial intent, or does it simply increase the probability of triggering safety-trained responses?"[^c11] No ablation of reasoning depth or visibility was run.
- The attacks were not built to exploit reasoning. The benefit may not survive an attack designed against the trace, as the paper's own citation suggests.[^c6]
- The judge sets the rate. "The two evaluators achieved κ = 0.537 (moderate agreement) with 78.8% raw agreement."[^c12] The primary judge was also the attacker's model family, a point the paper raises itself.[^c13]
- The count in the abstract is of evaluations, not of distinct behaviours: "with all 1,000 behavior evaluations (100 behaviors per model)".[^c14] Ten models on one hundred behaviours give the 1,000; the abstract's "1,000 harmful behaviors" reads, on this text, as a count of evaluations.
- The results describe models accessed in one month. "The specific vulnerabilities documented here apply to models accessed in December 2025".[^c15]
- The source is a single-author v1 preprint, not a refereed version.[^c16]

## Related

- [[llm-red-teaming]] — the automated attack family this measurement sits in; the search loop is the same kind of generate-and-judge cycle
- [[sycophantic-capitulation]] — commitment moved across turns, by rebuttal rather than by a harmful request
- [[framing-dependent-premise-adoption]] — acceptance of the same content depends on the framing it arrives in
- [[test-time-scaling]] — extra inference compute for accuracy; here the same kind of lever measured on resistance
- [[deliberative-misalignment-gap]] — a model's stated verdict need not match its conduct, so a deliberation trace is not by itself evidence of safe behaviour

[^c1]: arxiv-2512-07059 — "enabling extended reasoning on identical architecture reduced ASR from 97% to 42%"
[^c2]: arxiv-2512-07059 — "Thinking mode reduces ASR by 55 percentage points but 42% of attacks still succeed"
[^c3]: arxiv-2512-07059 — "Detects 11 resistance types and dynamically selects from 7 attack strategies"
[^c4]: arxiv-2512-07059 — "The exceptional effectiveness of academic and research framing indicates that models lower safety thresholds when"
[^c5]: arxiv-2512-07059 — "may reflect deliberative alignment: extended reasoning allows models to identify adversarial"
[^c6]: arxiv-2512-07059 — "though this benefit disappears against reasoning-aware"
[^c7]: arxiv-2512-07059 — "that thinking mode degrades safety [33, 35], while others report improvement [36, 37]."
[^c8]: arxiv-2512-07059 — "studies reporting degraded safety often use reasoning-specific attacks, while studies reporting improvement"
[^c9]: arxiv-2512-07059 — "Only one model pair (Kimi K2 standard vs. thinking)"
[^c10]: arxiv-2512-07059 — "comprises 100 behaviors that may not capture the full range of harmful content"
[^c11]: arxiv-2512-07059 — "Does extended reasoning enable identification of adversarial intent, or does it simply increase the probability of triggering safety-trained responses?"
[^c12]: arxiv-2512-07059 — "The two evaluators achieved κ = 0.537 (moderate agreement) with 78.8% raw agreement."
[^c13]: arxiv-2512-07059 — "To address potential evaluator bias from using DeepSeek V3.1 as both attacker and evaluator"
[^c14]: arxiv-2512-07059 — "with all 1,000 behavior evaluations (100 behaviors per model)"
[^c15]: arxiv-2512-07059 — "The specific vulnerabilities documented here apply to models accessed in December 2025"
[^c16]: arxiv-2512-07059 — "arXiv:2512.07059v1 [cs.CL] 8 Dec 2025"
