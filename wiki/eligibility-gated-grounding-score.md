---
description: "A grounding score that only checks whether claims are supported can be raised by short, evasive answers; an eligibility judge that marks non-responsive answers as inaccurate closes that gap."
aliases: ["eligibility-adjusted factuality score", "ineligible-response disqualification", "relevance-gated grounding", "disqualifying evasive answers"]
sources: ["arxiv-2512-10791"]
---
# Eligibility-gated grounding score

A grounding metric asks one question of a response: is each claim in it supported by the given document? In the FACTS Grounding v2 setup the response is labelled "accurate" only under a strict conjunction. A response is marked accurate "if all the claims in the response are grounded in the contents of the prompt, or do not require grounding", and marked "not accurate" "if at least one claim that bears information is deemed to be not grounded in the contents of the prompt".[^c1] Each judge gives a binary label per full response, the score for each judge is the share of accurate responses, and the unadjusted score is the average over the two judges.[^c2]

That per-claim check has a hole the authors name directly. "Metrics that are focused on evaluating the factuality of the generated text with respect to a context document can be" gamed, because "shorter responses" that avoid saying much leave fewer claims that could be found ungrounded.[^c3] The paper's example is a question about the main causes of the Great Depression answered with "The Great Depression was a difficult time in history with many causes and effects." Every claim in that reply is trivially supported. It names no cause, and the paper marks it ineligible because it "provides no substantive information on the causes" the document discusses.[^c4]

The mechanism is therefore two judgements, not one. A second judge asks a different question, whether the response answers the request at all, and returns "eligible" or "ineligible". "Ineligible responses are disqualified from factuality evaluation" and "the final factuality score is adjusted such that ineligible responses are deemed as inaccurate."[^c5] A response can thus be fully grounded and still score zero. The same two judge models serve both roles.[^c6] What the gate changes is the scored population: a short answer no longer earns the grounding credit that a complete answer earns, so the score cannot be raised by saying less.

This is a measurement point about evaluation, not a claim about how to answer. Read as a general principle: any score that counts only the errors a response makes, and not the parts of the request it leaves out, rewards omission. My inference, not a result of the paper, is that the same gap appears in any per-claim precision measure where the number of claims is under the answerer's control.

## Limits

- The human check the paper reports, a comparison of judges against human ratings on a held-out set of N=320, is given for the grounding judges and their prompt variants.[^c7] In the passages read, the eligibility label has no separate human validation, so how reliably the gate separates "vague" from "adequate" is not shown.
- Table 11 gives three hand-picked examples of ineligible responses. They illustrate the category; they are not a measured rate of evasive answers, and no before-and-after score with and without the gate is given in the passages read.
- The gate marks a response as inaccurate; it does not say how much of the request was met. The eligibility label is binary, so a half-answer and a non-answer fall on the same side.
- Grounding here means support in the supplied document. It does not check whether a grounded claim is true of the world, and the paper's own scope keeps this separate from its parametric benchmark. A fully grounded answer to a wrong document still scores as accurate; that boundary is my inference from the definition.
- Both judges are LLMs. The paper uses two of them partly to reduce self-preference bias,[^c8] which reduces but does not remove the judge's own biases.

## Related

- [[grounding-fabrication-dissociation]] — a separate case where a grounding-type score and a second behaviour come apart; there the second behaviour is refusal, here it is responsiveness.
- [[llm-judge-biases]] — the judge-side biases that the paper's use of two judge models is meant to dilute.
- [[pessimistic-min-judge-aggregation]] — another way of combining several LLM judges, by taking the strictest verdict rather than averaging.
- [[benchmark-drift]] — a fixed automatic judge can drift from human judgment; the eligibility gate is one more judge whose validity must be checked over time.

[^c1]: arxiv-2512-10791 — "response are grounded in the contents of the prompt, or do not require grounding"
[^c2]: arxiv-2512-10791 — "the unadjusted factuality score is the average of all judge scores"
[^c3]: arxiv-2512-10791 — "by providing shorter responses that evade conveying adequately comprehensive information,"
[^c4]: arxiv-2512-10791 — "provides no substantive information on the causes"
[^c5]: arxiv-2512-10791 — "the final factuality score is adjusted such that ineligible responses are deemed as inaccurate"
[^c6]: arxiv-2512-10791 — "The judge models used are the same two models used for checking grounding."
[^c7]: arxiv-2512-10791 — "we compared them to human-ratings on a heldout evaluation set (N=320)"
[^c8]: arxiv-2512-10791 — "We use two different judge models in order to reduce"
