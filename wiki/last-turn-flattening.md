---
description: "A benchmark harness that passes only a conversation's last user turn to the answerer drops context the rubric grades; passing full history raised one agent's score about 5 to 6 points."
aliases: ["last_user flattening", "last-user-turn truncation", "multi-turn flattening", "simple-evals last-turn harness"]
sources: ["doi-10-48550-arxiv-2605-24699"]
---
# Last-turn flattening in multi-turn evaluation

A multi-turn conversation can be scored only after the harness decides what the answering agent is shown. The reference simple-evals harness shows it only the last user turn. The paper's claim is that this "flattens conversations to the last user turn only" and so "silently drops follow-up context that the rubric grades against".[^c1] The question the agent must answer is then not the question the rubric was written for: a follow-up such as "give me a table" has its referent in an earlier turn, and an answerer that sees only the follow-up has no signal that the first turn defined the topic.[^c2]

In HealthBench Professional, the paper counts 115 of 525 cases (22%) whose conversation includes a second user turn that refines the question.[^c3] The remaining cases are single-turn, so the two harnesses hand the agent the same input there. The paper compares four flattening strategies: last_user (the reference), a role-tagged plain prefix, XML turn blocks, and multiturn, which passes the whole message list. Under multiturn the agent receives the prior user turn and its own earlier reply, and "resolves the follow-up against its own prior reply".[^c4] The paper makes multiturn the default.

The measured effect is the part that transfers. With the agent held fixed, switching from last_user to multiturn raised the Pro-graded score from 0.6102 to 0.6598 (+5.0 pp) and the GPT-5-graded score from 0.5220 to 0.585 (+6.3 pp) at n = 525.[^c5] On the single-turn cases the two strategies are the same input: the scores match "within bootstrap noise, because the agent receives byte-equivalent input".[^c6] So the difference is carried by the multi-turn slice, which the paper reads as the agent being able to "address rubric-relevant anchors that are not present in the final user turn alone".[^c7]

What the paper draws from this is a reporting rule rather than a method for answering. The flattening is "not an architectural change" to the agent; it is a change to what the harness passes in.[^c8] The paper argues that "last_user understates any agent that supports multi-turn", and that every report should state the strategy used, because a choice of about six points is as large as the architectural gains it reports against a flagship baseline.[^c9]

## Limits

- One agent family (a multi-agent pipeline on Gemini models) and one benchmark were measured. The claim that last_user "understates any agent that supports multi-turn" is argued from this case; it is not tested on other agents.
- The paper's own figures do not agree. The text gives a last_user base of 0.6102; its Table 7 gives 0.594 and reports a Pro gain of "+6.6 pp".[^c10] The abstract's "approximately 6 pp" covers both. Which base is right is not settled in the text.
- The multiturn strategy also passes the agent its own prior reply. The gain therefore bundles the user's earlier context with the agent's earlier output, and the paper does not separate the two. My inference: a carried reply can be copied as much as it is used, which is the risk described in [[contextual-inertia]].
- The effect on the paper's headline comparison with ChatGPT for Clinicians is unknown, because OpenAI's flattening strategy is not documented. The paper says the nominal 3.72 pp gap "may shrink or disappear" under one reading.[^c11]
- Both graders in the paper show a gain in the same direction. Absolute scores move with the grader, though: the same agent scores higher under Gemini 2.5 Pro than under GPT-5.4.[^c12] The size of the flattening effect under other graders was not measured. See [[llm-judge-biases]].
- Whether a richer context can also hurt (a noisy history crowding out the final question) is not tested here; the paper reports only the case where the added turns carry rubric-relevant content.

## Related

- [[non-standalone-question-retrieval-gap]] — the same dependence on earlier turns, measured as retrieval recall rather than answer score; query rewriting recovers part of that gap there, and the paper does not test rewriting.
- [[context-dominates-model-choice]] — another measurement where the context supplied, not the model, sets the score.
- [[contextual-inertia]] — how a carried prior reply can be repeated in later turns, the risk of passing full history.
- [[llm-judge-biases]] — the grader dependence the same paper reports next to the flattening effect.

[^c1]: doi-10-48550-arxiv-2605-24699 — "flattens conversations to the last user turn only"
[^c2]: doi-10-48550-arxiv-2605-24699 — "a multi-turn case, the agent receives only the second turn"
[^c3]: doi-10-48550-arxiv-2605-24699 — "include a second user turn that refines the question"
[^c4]: doi-10-48550-arxiv-2605-24699 — "and resolves the follow-up against its"
[^c5]: doi-10-48550-arxiv-2605-24699 — "lifts the Pro-graded score from 0.6102 → 0.6598 (+5.0 pp)"
[^c6]: doi-10-48550-arxiv-2605-24699 — "noise, because the agent receives byte-equivalent input"
[^c7]: doi-10-48550-arxiv-2605-24699 — "the agent to address rubric-relevant anchors that are not present in the final user turn alone"
[^c8]: doi-10-48550-arxiv-2605-24699 — "This is not an architectural change to MDIA"
[^c9]: doi-10-48550-arxiv-2605-24699 — "that last_user understates any agent that supports multi-turn"
[^c10]: doi-10-48550-arxiv-2605-24699 — "+6.6 pp"
[^c11]: doi-10-48550-arxiv-2605-24699 — "may shrink or disappear"
[^c12]: doi-10-48550-arxiv-2605-24699 — "when using Gemini 2.5 Pro, MDIA scored 0.6585"
