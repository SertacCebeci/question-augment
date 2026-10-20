---
description: "Mean dialogue-turn index at which each missing premise is first resolved; paired with recall in a log-discounted score it separates lazy from inefficient questioners that accuracy alone conflates."
aliases: ["ATC", "Average Turns to Clarify", "Efficiency-Adjusted Recall", "EAR", "Missing Premises Recall"]
sources: ["arxiv-2603-00187"]
---
# Average turns to clarify

A way to score a questioner's efficiency, not only its coverage. For each
premise the user left out, record the dialogue turn in which the agent first
resolved it; the average of those turn indices is the Average Turns to
Clarify (ATC), lower being better.[^c1] It is computed only over premises that
were actually clarified, so an agent that clarifies nothing has ATC
undefined (NaN), not zero.[^c2]

## Two quantities that must be read together

ClarEval (code agents given HumanEval tasks with injected missing goals,
missing premises or vague terminology) defines Missing Premises Recall
(MPR) as the share of the golden premise set the agent had clarified by the
end of the dialogue.[^c3] Because ATC ignores the unclarified premises, an
agent that asks one cheap question and stops can show a low ATC with a low
MPR. The paper names this the "Lazy Agent" bias, and its opposite, high MPR
bought with many turns, the "Inefficient Agent" bias.[^c4]

To close that gap the appendix defines Efficiency-Adjusted Recall (EAR): each
premise contributes a log-discounted credit of its turn index, summed over
recovered premises and divided by the size of the golden set, with
unclarified premises contributing 0. Immediate recovery of everything gives
EAR = 1.0, recovery spread across turns gives less, and failure gives
about 0 — "a soft penalty for delayed clarification".[^c4] The exact
discount is garbled in the text extract; I read it as 1/log2(Turn+1)
per premise, which is my reconstruction, not a verified quote.

## What was measured

Across eleven code agents in a scripted multi-turn dialogue, GPT5-Coder had
the lowest ATC (1.493) and Qwen2.5-Coder the highest (2.396), "nearly 60%
more turns" to clarify the same premises.[^c5] The authors read high ATC as
fragmented, serial questioning that leaves the user to supply one
dependency at a time, and the efficient agent as one that asks several
critical questions in a single turn.[^c6] Ambiguous terminology (words such
as "fast" or "clean up") gave the lowest Pass@1 and the highest ATC for most
models.[^c7]

The same suite shows that single-turn recognition and dialogue-aware
clarification are different skills: single-turn and multi-turn performance
correlate only weakly (Pearson r = 0.32), and Aider-GPT5 falls from second
in single-turn KQC to tenth in multi-turn KQC.[^c8] Without clarification,
GPT-4o's Pass@1 fell from 89.02% on clarified tasks to 8.94% under
ambiguity in this benchmark.[^c9]

## Limits

- ATC is defined over resolved premises only, so it is meaningless alone;
  the paper's own EAR is the repair, and EAR's formula is not recoverable
  verbatim from the extract.
- The user is a pre-written script ("operated deterministically"), so a
  turn index partly measures how the script releases information, not how a
  real user would answer.[^c10]
- Premises and key intents come from LLM-injected ambiguity on HumanEval
  (algorithmic, single-function tasks) with human review; the claim that
  this transfers to repository-scale clarification is the authors' argument,
  not a measurement.
- Turn count is not a cost: the metric treats a long compound question and a
  short one as one turn, so it rewards batching regardless of how much
  burden each message puts on the user.
- Model rankings depend on 2025 model versions and one prompt; no human
  users were run.

## Related

- [[turn-discounted-key-question-rate]] — a similar early-coverage discount, applied to key questions in ClarifyCodeBench
- [[optimal-round-adherence]] — scores closeness to an optimal round count rather than speed to each premise
- [[clarification-benchmarks]] — ClarEval's place among the benchmarks that score asking
- [[regret-based-clarification-evaluation]] — whole-dialogue cost-aware scoring of the same trade-off
- [[elicitation-burden-tradeoff]] — why fewer user turns matter

[^c1]: arxiv-2603-00187 — "let Turn(pi ) denote the dialogue turn index in which it was first successfully resolved."
[^c2]: arxiv-2603-00187 — "ATC is considered undefined and treated"
[^c3]: arxiv-2603-00187 — "Let R ⊆ P be the set of premises successfully clarified by the agent by the dialogue’s end."
[^c4]: arxiv-2603-00187 — "This metric effectively addresses the trade-off between the “Lazy Agent” bias (low ATC but low MPR) and the “Inefficient Agent” bias (high MPR but high ATC)."
[^c5]: arxiv-2603-00187 — "requiring nearly 60% more turns on average to clarify the same set of premises."
[^c6]: arxiv-2603-00187 — "indicating a tendency to ask fragmented questions"
[^c7]: arxiv-2603-00187 — "showing lowest Pass@1 and highest ATC for terminology"
[^c8]: arxiv-2603-00187 — "This suggests that intent inference in isolation and dialogueaware clarification are distinct skills"
[^c9]: arxiv-2603-00187 — "its performance plummets to 8.94% under ambiguity."
[^c10]: arxiv-2603-00187 — "The User Simulator operated deterministically based on the generated scripts."
