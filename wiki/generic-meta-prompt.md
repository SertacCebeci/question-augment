---
description: "An instruction that says how, what or when to reason, not the answer (verify with code, enumerate small cases); in one IMO case it made a model catch its own wrong formula."
aliases: ["Socratic meta-prompt", "generic meta-prompt", "meta-cognitive prompt", "generic directive"]
sources: ["arxiv-2512-19287"]
---
# Generic meta-prompt

A generic meta-prompt is an instruction about the reasoning process rather than about the content of the problem. Examples in the Vibe Reasoning paper are "verify with code", "try small cases", "this seems wrong", "summarize into one statement" and "write this result to a file". The paper calls the category Socratic meta-prompts and defines them by what they leave out: they are "generic directives" that "prompt AI reflection without revealing solutions".[^g1] Its Table 1 sorts them into verification, specialization, challenge, simplification, output request and memory prompts, each paired with a "why generic" note such as "Standard practice" or "Common heuristic".[^g1b]

The mechanism the paper proposes is triggering of an existing capability. A model that has the skill to check its work often does not deploy it unprompted, and a short instruction to check is enough to start the check. In the case study GPT-5 was asked, with no guidance, for the tile count at n = 2025 and returned a confident wrong value. After the human wrote "Check if the code produces accurate solutions. Enumerate small cases first.", the model ran enumeration, found its formula disagreed with the exact small-case values, and revised.[^g2] The paper's reading is "The AI discovers the error itself once prompted to verify"[^g3], and the human "does not suggest a specific formula or point out" the error.[^g3b]

Timing carries weight. Comparing two GPT-5 attempts at the answer, the authors find that the successful one prompted verification early: "This caught a subtle enumeration bug that would have corrupted all subsequent observations."[^g4] The failed one "accepted initial code output without verification prompts", and a bug went undetected.[^g5] The paper's summary is "a single well-timed meta-prompt, entirely generic and transferable to any" problem involving code.[^g6]

The shift from problem-specific hints to generic ones is also reported. Early hints named the tool ("You mentioned the Erdős–Szekeres theorem, how might we use it?"), while later attempts used prompts such as "First plan your approach, propose 5 different strategies", and "The same results were achieved with generic prompts".[^g7] In the paper's account the model then chose among its own options: "The AI independently identified these from a menu of self-generated options."[^g8] So the human supplies the category of action and the model supplies the content.

What survives transfer is the procedure: check with code, sample special cases, plan alternatives before committing. What does not clearly survive is the claim of full domain-independence. The perfect-square prompt that led to the key pattern in this case is one the paper admits "seems to contain problem-specific information", and it can only be called generic "framed as a general heuristic about exploring" special number-theoretic cases.[^g9]

## Limits

The evidence is one problem (IMO 2025 Problem 6) and one authors' sequence of sessions. The paper calls itself work in progress: "This paper represents work in progress."[^g10] The dialogue excerpts are condensed, and the note says they "may not be verbatim transcriptions."[^g11]

The generic-versus-specific comparison is not controlled. The two families of prompts were used in different sessions by the same authors, who learned the method as they went, so differences in outcome cannot be attributed to the prompt wording alone. That reading is mine.

Verification prompts were tested in domains where code can run. The claim that they transfer to problems without a checkable computation is not tested in the text. The paper's own scope condition is blunt: "Weaker or insufficiently trained models cannot support Vibe Reasoning."[^g12] A generic prompt presupposes a model that can carry out what it is told to check.

The human in the loop still does the hard part, which the paper does not automate. Asked whether the human judgments can be automated, it says "some aspects may be automatable in future work", and the timing judgments, such as when to stop exploring and move to proof, are left to the person.[^g13] This is a limit on what the prompt replaces: the prompt names an action, while deciding that the action is due is still a human call.

## Related

- unreliable-self-evaluation — why a model does not check on its own, which a generic verification prompt is meant to work against.
- [[tool-integrated-reasoning]] — the code execution that a prompt such as "check with code" calls for.
- [[model-orchestration]] — the human's judgment about when to change models is a meta-level decision of the same kind.
- [[staged-socratic-hint-policy]] — a Socratic policy in tutoring, which also withholds answers; there the target is a learner, not a reasoner.

[^g1]: arxiv-2512-19287 — "that prompt AI reflection without revealing solutions"
[^g1b]: arxiv-2512-19287 — "Common heuristic"
[^g2]: arxiv-2512-19287 — "Check if the code produces accurate solutions. Enumerate small cases first."
[^g3]: arxiv-2512-19287 — "The AI discovers the error itself once prompted to verify"
[^g3b]: arxiv-2512-19287 — "the human does not suggest a specific formula or point out"
[^g4]: arxiv-2512-19287 — "This caught a subtle enumeration bug that would have corrupted all subsequent observations."
[^g5]: arxiv-2512-19287 — "The human accepted initial code output without verification prompts"
[^g6]: arxiv-2512-19287 — "a single well-timed meta-prompt, entirely generic and transferable to any"
[^g7]: arxiv-2512-19287 — "The same results were achieved with generic prompts"
[^g8]: arxiv-2512-19287 — "The AI independently identified these from a menu of self-generated options"
[^g9]: arxiv-2512-19287 — "this type of guidance can be framed as a general heuristic about exploring"
[^g10]: arxiv-2512-19287 — "This paper represents work in progress."
[^g11]: arxiv-2512-19287 — "may not be verbatim transcriptions"
[^g12]: arxiv-2512-19287 — "Weaker or insufficiently trained models cannot support Vibe Reasoning."
[^g13]: arxiv-2512-19287 — "some aspects may be automatable in future work"
