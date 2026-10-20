---
description: "Tool use does not uniformly shift agent confidence: evidence tools such as web search inflate confidence on wrong answers, verification tools such as code interpreters lower it."
aliases: ["confidence dichotomy", "tool-induced overconfidence", "evidence versus verification tools"]
sources: ["arxiv-2601-07264"]
---
# Tool-type confidence dichotomy

Whether giving an agent tools hurts its [[calibration]] depends on what the tool returns. Xuan et al. (2026) split tools into two kinds. Evidence tools (web search) "retrieve external information laden with noise and uncertainty" and push verbalized confidence up. Verification tools (code interpreters) "provide deterministic execution feedback" and pull it down.[^c1]

## What was measured

The pilot compares three configurations on one backbone (Qwen2.5-3B-Instruct): direct prompting, prompting-based tool use, and RL-trained tool use. Search agents are Search-R1-style; code agents follow SimpleTIR on AIME2024/2025 and MATH-500. The statistic is Mean Confidence on Incorrect Predictions (MCIP), taken over the questions all three settings got wrong: the average stated confidence on those items. A lower value means less overconfidence. Differences between configurations were tested with t-tests.[^c2]

Result: on search tasks, adding the tool raised MCIP under both prompting and RL, and the differences were significant between direct prompting and RL-based tool use. On code tasks the order reverses: RL-based tool use reached the lowest MCIP, significant in the reverse order.[^c3] On MATH-500, for example, MCIP falls from 0.971 (direct) to 0.913 (prompted tool use) to 0.890 (RL tool use), while accuracy rises from 63.4 to 77.0 for the direct and RL settings.[^c4]

## Proposed mechanism

The authors attribute the split to the signal: noisy, ambiguous retrieved text lets the agent feel evidence-supported without being right, whereas a deterministic execution result either confirms or contradicts the reasoning, so the agent "ground[s] the reasoning process and temper[s] unwarranted certainty".[^c5] This is the authors' explanation; the pilot varies tool type but does not isolate noise from other differences between search and code tasks. The paper states the dichotomy persists under prompting and standard tool-use RL, so it is not removed by prompt engineering alone.[^c6]

## Limits

One small backbone for the pilot; two tool families, each confounded with a task domain (open QA versus math). MCIP looks only at wrong answers on the intersection of questions, so it says nothing about underconfidence or ranking quality. The noise explanation is untested by manipulating retrieval noise. The training remedy was built only for the evidence-tool side.

## Related

- [[calibration]] — the property that tool type moves.
- [[log-score-verbalized-confidence-reward]] — a reward-side route to better verbalized confidence.
- [[margin-separated-calibration-reward]] — the training fix the same paper proposes for evidence-tool agents.
- [[reasoning-contamination-of-verbalized-confidence]] — another way the surrounding trace distorts stated confidence.

[^c1]: arxiv-2601-07264 — "systematically induce severe overconfidence"
[^c2]: arxiv-2601-07264 — "We measure the Mean Confidence on Incorrect"
[^c3]: arxiv-2601-07264 — "tool usage mitigates"
[^c4]: arxiv-2601-07264 — "63.4"
[^c5]: arxiv-2601-07264 — "ground the reasoning process"
[^c6]: arxiv-2601-07264 — "This dichotomy persists across both promptingbased strategies and standard tool-use-oriented RL"
