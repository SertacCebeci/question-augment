---
description: "A reasoning scaffold that works alone can fail inside a long prompt because style directives like 'lead with specifics' force the conclusion out before the scaffold runs."
aliases: ["instruction dilution", "prompt complexity dilution", "conclusion-first ordering failure"]
sources: ["arxiv-2603-13351"]
---
# Instruction dilution of structured reasoning

A structured-reasoning instruction (here STAR: Situation, Task, Action, Result) helps only if it runs before the answer is emitted. Inside a long production prompt, other directives can reverse that order. The scaffold still runs, but as a rationalisation of an answer already given.

## What was measured

The test question was the car wash problem: the car wash is 100 m away, walk or drive? The correct answer is drive, because the car must be at the wash. In a 10-line STAR-only prompt on Claude Sonnet 4.6, 20 of 20 trials passed. A later 100-trial run gave 100 of 100.[^c1] The same STAR block inside a 60+ line production prompt for an interview-coaching product passed 0% with one user profile and 30% with another, 20 trials each.[^c2] The author calls this instruction dilution.

## Mechanism claimed

The author's account is conclusion-first ordering. Directives such as "Lead with specifics" and communication-style rules push the model to state an answer first. In one manual run the model wrote "Short answer: Walk." and then a full STAR breakdown that found the constraint ("you have to drive the car there"). It ended with "Drive your car to the wash".[^c3] The author reads this as showing that the reasoning worked but the answer was already committed. In his words the STAR breakdown "is not genuine inference but post-hoc rationalization of an already-committed conclusion."[^c4]

A second, weaker claim is attention competition: a 10-line prompt gives STAR near-exclusive weight, while a 60-line prompt spreads it over many instructions, with STAR sitting mid-prompt. This is borrowed from the lost-in-the-middle literature and not tested here.[^c5]

## Context matters, not only length

The two profiles shared the same base prompt, yet scored 0% and 30% (Fisher p = 0.020). The author takes this to mean that "the semantic content of surrounding context modulates which instructions the model prioritizes."[^c6] So dilution is not a pure count of instructions.

## Implication for asking and answering

Order of reasoning and conclusion is a design variable. "Answer first, then explain" and "reason first, then conclude" decide whether a scaffold functions at all.[^c7] A scaffold validated alone must be re-tested inside the real prompt. The author also reports that the same STAR-only prompt rose from 85% on Sonnet 4.5 (20 trials) to 100% on Sonnet 4.6, so model upgrades helped only the isolated prompt.[^c8]

## Limits

- One question, one model family, one production prompt, one time point. Whether other implicit-constraint problems or other models dilute the same way is untested.
- Only two prompt lengths were tried (10 and 60+ lines). No degradation curve exists, and historical prompt versions were not rebuilt.
- Conditions A and B had n = 20 each. The ordering mechanism rests on one anecdotal transcript and was not isolated by an experiment that removes "Lead with specifics" while keeping the rest. Treat it as a hypothesis. The attention-competition account is my reading of cited work, not a result.
- The 100-trial run disabled extended thinking, since setting temperature turns it off. Results may not carry to thinking mode.
- Scoring is pattern-matching on the final answer. The author is a single independent researcher, and the report corrects his own earlier paper.

## Related

- [[deferred-answer-exposure]] — also about information order, where an answer revealed early becomes something the reasoning rationalises
- [[separated-thinking-response-training]] — separating thinking from the response, the structural form of reason-then-conclude

[^c1]: arxiv-2603-13351 — "100/100 (100.0%)"
[^c2]: arxiv-2603-13351 — "Conditions A and B scored 0% and 30%, respectively."
[^c3]: arxiv-2603-13351 — "** Short answer : Walk .**"
[^c4]: arxiv-2603-13351 — "is not genuine inference but post-hoc rationalization of an already-committed conclusion."
[^c5]: arxiv-2603-13351 — "In InterviewMate’s production prompt, STAR instructions are positioned mid-prompt—potentially in"
[^c6]: arxiv-2603-13351 — "the semantic content of surrounding context modulates which instructions the model prioritizes."
[^c7]: arxiv-2603-13351 — "The order in which a model reasons and concludes is a first-class design variable."
[^c8]: arxiv-2603-13351 — "The STAR-only prompt improved from 85% (Sonnet 4.5) to 100% (Sonnet 4.6) without any prompt"
