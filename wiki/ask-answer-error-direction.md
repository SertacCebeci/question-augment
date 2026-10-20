---
description: "A clarification decision can fail in two directions: answering when the request still needs a question, or asking when an answer was already warranted; one accuracy score hides which."
aliases: ["under-clarification and over-clarification", "under-clarify / over-clarify", "premature answer versus unnecessary question"]
sources: ["arxiv-2512-21120"]
---
# Ask-answer error direction

At each turn of a clarifying dialogue a system makes one binary choice: ask a clarifying question, or answer now. ClarifyMT-Bench assigns every dialogue turn a reference action, Clarify or Answer, derived from its construction pipeline, and scores a prediction against it.[^c1] A mismatch has a direction, and the work names both. **Under-clarify** is a prediction of Answer where the reference is Clarify, and the text reads it as the model answering prematurely.[^c2] **Over-clarify** is the reverse, a prediction of Clarify "when an answer is already warranted."[^c3]

The headline score is the rate of matching decisions across all turns and instances.[^c4] The two error categories are kept for qualitative analysis. The distinction matters because a single accuracy figure cannot tell a model that always answers from a model that always asks. The paper shows both patterns. Its main finding is that "most LLMs prefer to answer prematurely rather than engage in sufficient clarification."[^c5] It also reports that Qwen-2.5-7B-It "tends to answer directly regardless of uncertainty," which "boosts its scores on Precise and Refusal cases" while causing "sharp drops on ambiguity-heavy types where clarification" is needed.[^c6] Refusal-style inputs are the reverse case: their performance is "uniformly low, reflecting a widespread tendency toward over-clarification."[^c7] A model can therefore post a high average while erring in opposite directions on different user types.

The mechanism, in the sense the work supports, is that the two errors have different costs and different causes. An under-clarify error gives an answer built on an assumed reading. An over-clarify error spends a turn on a question the user has already answered or declined to answer. Which error dominates depends on how the model reads the user, which is why the paper reports the split by user persona as well as by turn ([[user-response-persona-simulation]]).

## Limits

- The reference action is not gold. The paper states that "we do not explicitly annotate slots" for each instance, so Clarify and Answer are labels from the construction pipeline, not a measured set of required information.[^c8]
- The text I read gives the two error categories a definition and a qualitative role, and I did not find per-category error rates reported in the sections read. The direction-level claims above rest on the authors' summaries, not on a published table.
- Accuracy counts the decision only. Whether a clarifying question is good is a separate evaluation in the same paper, by LLM-as-judge and manual review, and it is not folded into the error direction.
- The 2–3 turn limit means the error direction is measured on short dialogues; the paper's depth result is discussed in [[underspecified-question-eager-answering]] and is not a measurement of long conversations.

## Related

- [[underspecified-question-eager-answering]] — the same answer-eagerness on underspecified questions in a different benchmark (MTRAG-UN), where the miss is under-clarification
- [[ambiguity-taxonomy]] — what a request can be ambiguous about, which determines whether a question is the right move
- [[user-response-persona-simulation]] — the simulated user replies whose behaviour sets which direction a model errs in

[^c1]: arxiv-2512-21120 — "each dialogue turn in ClarifyMT-Bench is associated with a reference action"
[^c2]: arxiv-2512-21120 — "model answers prematurely"
[^c3]: arxiv-2512-21120 — "model asks when an answer is already warranted"
[^c4]: arxiv-2512-21120 — "We primarily report overall decision accuracy"
[^c5]: arxiv-2512-21120 — "most LLMs prefer to answer prematurely rather than engage in"
[^c6]: arxiv-2512-21120 — "causes sharp drops on ambiguity-heavy types where clarification"
[^c7]: arxiv-2512-21120 — "reflecting a widespread tendency toward over-clarification"
[^c8]: arxiv-2512-21120 — "we do not explicitly annotate slots"
