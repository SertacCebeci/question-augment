---
description: "An auditor LLM tests a target model under a user's custom instruction, in multi-turn chats, and flags apparent deviations; in a pilot, annotators confirmed 22.2% of flags."
aliases: ["Offscript", "automated instruction-adherence auditing", "custom instruction auditing", "behavioral-instruction audit"]
sources: ["arxiv-2512-10172"]
---
# Custom-instruction adherence audit

A user can write a standing instruction, such as a required answer format, a verbosity setting or a rule for when to abstain. Platforms accept it and do not check it. The audit tests whether the target model keeps to it. An auditor is a second LLM that runs the test. The target receives the user's instruction as its system prompt, and each conversation starts there.[^a1] The auditor has two roles: it "generates test inputs to query the target model with", and it "judges whether responses from the target model are consistent with the custom instruction."[^a2][^a3]

The loop has four functions: start a conversation, send a further message, flag a response for human review, and end the audit.[^a4] Its defining feature is that the next probe depends on the last answer. The auditor can "dynamically adapt the prompts it generates according to responses from the target model in current and previous conversations."[^a5] So the search for deviations is sequential, and the test set is not fixed in advance. The authors cap the loop at 20 function calls.[^a6]

The output is a set of flags, not a verdict, and the pilot shows how far apart the two are. Of the 65 instructions kept, 84.6% were flagged at least once across ten sessions.[^a7] Two expert annotators then "independently assessed whether these flags represented true violations."[^a8] "Annotators unanimously agreed that 22.2% of flagged conversations" were violations. Under the looser rule, where one annotator suffices, the share was 48.1%.[^a9] The agreement between the two annotators was only fair: "Inter-rater reliability was 0.383" by Cohen's kappa.[^a10] A flag rate of this size is therefore not evidence of violation. The confirmed fraction carries the weight, and it moves with the agreement rule.

My reading, not a tested claim: a flag measures the auditor's suspicion, and the human review measures the violation. They are two instruments with different errors, and the audit's value lies in the conjunction of the two.

Two kinds of failure appear in the flagged sessions. The first is structural. The authors find that "complex parameterized instructions designed to switch between task modes or adjust verbosity frequently experienced violations."[^a11] They suspect the cause is complexity, that the instructions "likely exceeded" the model's capacity. That is an interpretation from a few cases, not a measured effect.[^a12]

The second is a priority conflict. When the auditor asks for something the standing instruction forbids, the model "consistently prioritized the most recent message over established preferences."[^a13] The paper leaves the rule open: "should models prioritize standing preferences or context-specific requests?"[^a14] The point matters for the wiki. The audit detects more than drift from an instruction. It also exposes a question the instruction itself cannot settle, namely which of two sources wins when they conflict.

A third kind of flag is not a model failure at all. "some flagged cases represented degenerate scenarios" in which the auditor asked for American spellings against an Australian-spelling instruction and received them. "While technically a violation, such cases do not represent genuine user concerns."[^a15][^a16] A flag can therefore come from the auditor's adversarial prompting as well as from the target's drift.

## Limits

- The pilot is small and drawn from one source. The 115 Reddit instructions were narrowed, and "we retained 65 custom instructions" after roleplay and guardrail-bypass requests were removed.[^a17] The filter is the authors' choice, and it decides what a flag can mean.
- The auditor is one model, GPT-5 Mini. The paper says that "the choice of model to use as the auditor agent greatly impacts the results of the system."[^a18] No second auditor was run, so the flag rate belongs to this auditor.
- The stopping rule belongs to the auditor. The loop ends "when the auditor calls the end audit function or after the number of function calls exceeds a limit."[^a19] The auditor started 2.26 conversations per instruction on average.[^a20] Nothing shows which violations it missed, so the audit gives no recall.
- The two headline counts use different units. The abstract reports deviations "in 86.4% of conversations," while the results report 84.6% of instructions flagged at least once.[^a21] The paper does not reconcile them.
- Agreement is fair (kappa 0.383) with two annotators, and no interval is given for the 22.2%.
- The authors concede the auditor "may benefit from refinement to avoid overly adversarial testing strategies," which they leave for future work.[^a22]
- Use with real users is not tested. The authors suggest that "allowing users to supply their conversation history to the auditing agent could inform topic selection."[^a23] Their claim that automated auditing is "a viable approach" for behavioral instructions rests on this pilot alone.[^a24]

## Related

- [[llm-red-teaming]] — the same generate-and-judge loop, aimed at safety behaviour. Here the target is the user's own instruction, and the paper contrasts itself with audits of provider-set guidelines.[^a25]
- [[personal-rubric-reward-gap]] — one user's explicit criteria as the test of fit. There they sit in a reward benchmark; here they drive an audit loop.
- [[hint-adherence-without-acknowledgement]] — behavioural adherence to an instruction-like cue. The object there is an answer hint, not a standing instruction.
- [[cot-judge-detection-localization-gap]] — a judge's flags that are not yet confirmed errors, with false alarms on correct chains. It is the same flag-versus-confirmation problem.

[^a1]: arxiv-2512-10172 — "Each conversation begins with the custom instruction being provided to the target model as a system prompt"
[^a2]: arxiv-2512-10172 — "generates test inputs to query the target model with"
[^a3]: arxiv-2512-10172 — "judges whether responses from the target model are consistent with the custom instruction"
[^a4]: arxiv-2512-10172 — "it flags the conversation for human review"
[^a5]: arxiv-2512-10172 — "dynamically adapt the prompts it generates according to responses from the target model in current and previous conversations"
[^a6]: arxiv-2512-10172 — "limits the auditor to a maximum of 20 function calls for purposes of efficiency"
[^a7]: arxiv-2512-10172 — "Of the 65 custom instructions analyzed, 84.6% were flagged by the auditor agent at least once across the 10 conversation sessions"
[^a8]: arxiv-2512-10172 — "independently assessed whether these flags represented true violations"
[^a9]: arxiv-2512-10172 — "Annotators unanimously agreed that 22.2% of flagged conversations"
[^a10]: arxiv-2512-10172 — "Inter-rater reliability was 0.383"
[^a11]: arxiv-2512-10172 — "complex parameterized instructions designed to switch between task modes or adjust verbosity frequently experienced violations"
[^a12]: arxiv-2512-10172 — "The complexity of these systems likely exceeded GPT-5"
[^a13]: arxiv-2512-10172 — "GPT-5 Chat consistently prioritized the most recent message over established preferences"
[^a14]: arxiv-2512-10172 — "should models prioritize standing preferences or context-specific requests?"
[^a15]: arxiv-2512-10172 — "some flagged cases represented degenerate scenarios"
[^a16]: arxiv-2512-10172 — "While technically a violation, such cases do not represent genuine user concerns"
[^a17]: arxiv-2512-10172 — "we retained 65 custom instructions"
[^a18]: arxiv-2512-10172 — "the choice of model to use as the auditor agent greatly impacts the results of the system"
[^a19]: arxiv-2512-10172 — "The system exits from the auditing loop when the auditor calls the end audit function or after the number of function calls exceeds a limit"
[^a20]: arxiv-2512-10172 — "the auditor agent started, on average, 2.26 conversations per custom instruction"
[^a21]: arxiv-2512-10172 — "detected potential deviations from instructed behavior in 86.4% of conversations"
[^a22]: arxiv-2512-10172 — "may benefit from refinement to avoid overly adversarial testing strategies"
[^a23]: arxiv-2512-10172 — "allowing users to supply their conversation history to the auditing agent could inform topic selection"
[^a24]: arxiv-2512-10172 — "automated auditing serves as a viable approach for evaluating compliance to behavioral instructions related to information seeking"
[^a25]: arxiv-2512-10172 — "both focus on adherence to provider-specified behavioral guidelines rather than user-specified custom instructions"
