---
description: "Planting known-excluded items among a blinded review set estimates how many relevant items a screen dropped: the rate at which reviewers include the controls is the screen's miss rate."
aliases: ["known-exclude controls", "concealed negative controls", "control-inclusion miss rate", "planted-negative recall estimate"]
sources: ["doi-10-48550-arxiv-2608-25071"]
---
# Concealed-control miss rate

A screen that drops items before review cannot report what it dropped, because nobody looks at the dropped items. One way to recover an estimate of that loss comes from the review itself. Items the screen already excluded are mixed, as controls, into the set that reviewers judge. The reviewers see one seeded random order, "in a single seeded random order with screen labels withheld",[^c2] so they cannot tell a control from a candidate.

The estimate rests on a simple sampling step. The controls come from the screen's excluded pool, so a control that a reviewer majority includes is a relevant item the screen missed. "Because the controls are drawn from the screen’s NOT _ RELEVANT pool, the rate at which the majority included them estimates the screen’s miss rate."[^c1] The inclusion rate is therefore read as the share of the excluded pool that reviewers would count as relevant, not as a count of misses.

The paper uses it as a stopping rule. In its first round, 791 conversations were reviewed, 641 screened in and 150 concealed controls. The majority included 9 of the 150 controls, "a control-inclusion rate of 6.0%, which exceeded the 5% decision rule".[^c3] The rule is explicit: "A control-inclusion rate above 5% triggered a recall round; below it, the included set is accepted as comprehensive and the cycle terminates."[^c9] Above the threshold, a second screen re-examined the excluded pool with a recall-oriented rubric; that round used 25 fresh controls, and the majority included 1 of them. "a control-inclusion rate of 4.0%, below the stopping threshold, terminating the loop."[^c4] The paper's recall round also checks its own rule: its controls "re-apply the recovery decision rule", so the test covers the rule that produced the new candidates, not only the first screen.[^c5]

What makes the rate usable is the separation of roles. The screen proposes; the controls are hidden from the reviewers; the reviewers' majority decides. The screen never sees its own controls, and the reviewers never learn which items the screen rejected. The estimate is only as good as that separation.

## Limits

- The rate is an estimate over a sample, and the sample is small in the second round. One control in 25 is 4.0%, so a single reviewer's leniency moves the number by a visible step. The paper reports the round-2 agreement as lower, AC1 0.49, "driven by one reviewer’s greater leniency on controls, which the majority rule absorbed."[^c6] The majority rule absorbs that disagreement; it does not measure it away.
- The estimate measures what the reviewers accept, not what the screen was meant to find. The paper says so directly: "The concealed controls estimate roughly 6% residual mental-health content in the excluded pool by liberal clinician standards; the recovery pass targeted high-precision misses, so some conversations may remain unrecovered."[^c7][^c8] A stricter reviewer standard would give a lower rate, and a rate near zero under one standard does not mean zero misses under another.
- The 5% threshold is the authors' choice. The paper gives no sensitivity analysis for it. My inference: the threshold trades extra recall rounds against the risk of stopping early, and nothing in the study says where it should sit for another task.
- The method assumes the controls are a random draw from the excluded pool. If the screen dropped some relevant items in a way that also makes reviewers reject them, the control rate would underestimate misses. The study does not test for that. This is my inference.
- One domain, one benchmark, one screen (an LLM rubric with clinician review). Whether the same estimate holds when the screen is a classifier, a retrieval ranker, or a human filter is untested here.

## Related

- [[unknown-relevant-total-recall]] — recall needs the total count of relevant items; a control rate is one way to estimate the part of that count that an exclusion step hid
- [[chance-corrected-agreement]] — the reviewers' agreement behind a control rate is a chance-corrected statistic; the paper uses Gwet's AC1 because the high prevalence of relevant items deflates kappa
- [[llm-judge-biases]] — the reviewers here were blinded human clinicians; the control method needs independent review of the controls, and an LLM judge that shares the screen's biases would not give an independent rate

[^c1]: doi-10-48550-arxiv-2608-25071 — "the rate at which the majority included them estimates the screen’s miss rate"
[^c2]: doi-10-48550-arxiv-2608-25071 — "in a single seeded random order with screen labels withheld"
[^c3]: doi-10-48550-arxiv-2608-25071 — "a control-inclusion rate of 6.0%, which exceeded the 5% decision rule"
[^c4]: doi-10-48550-arxiv-2608-25071 — "a control-inclusion rate of 4.0%, below the stopping threshold, terminating the loop"
[^c5]: doi-10-48550-arxiv-2608-25071 — "whose controls re-apply the recovery decision rule"
[^c6]: doi-10-48550-arxiv-2608-25071 — "driven by one reviewer’s greater leniency on controls, which the majority rule absorbed"
[^c7]: doi-10-48550-arxiv-2608-25071 — "The concealed controls estimate roughly 6% residual mental-health content in the excluded pool by liberal clinician standards"
[^c8]: doi-10-48550-arxiv-2608-25071 — "the recovery pass targeted high-precision misses, so some conversations may remain unrecovered"
[^c9]: doi-10-48550-arxiv-2608-25071 — "A control-inclusion rate above 5% triggered a recall round"
