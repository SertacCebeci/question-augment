---
description: "A two-provider LLM-judge ensemble scoring text-to-SQL correctness reaches 0.82 AUROC at 0.03 calibration error, enabling abstention self-consistency cannot match."
aliases: ["two-provider judge ensemble", "cross-provider verifier ensemble"]
sources: ["richardson-2026", "arxiv-2601-00850", "arxiv-2512-05537"]
---
# Cross-provider LLM-judge ensemble

> The gain is not a bigger judge; it is a *second, differently-wrong* one —
> combining independent-provider verdicts, not scaling one verifier, is what
> opens a usable low-risk region.

## Definition / Mechanism

Richardson (2026) shows a single LLM verifier (shown the
question, schema and candidate SQL, asked whether it is correct) already
clears the [[black-box-correctness-ceiling|black-box ceiling]]: "an LLM judge
scoring from 0.72 (GPT-4o-mini) to 0.78 (Claude)." Combining two judges from
different providers goes further: "Judges from different providers make
different errors, so a two-provider ensemble reaches 0.82 auroc with a
well-calibrated probability (expected [[calibration]] error 0.03), and it
supports useful abstention frontiers (for example, answering 27% of
questions at 24% selective risk) where self-consistency offers no valid
low-risk subset."[^c1]

The mechanism is diversity of error, not model size: "the GPT-4o and Claude
scores are not redundant as their correlation is only r = 0.43, indicating
that they make different errors... A two-provider ensemble of GPT-4o and
Claude reaches 0.822 auroc, improving over GPT-4o alone by +0.052... The
best correctness signal is not merely a larger judge from the same source,
but a combination of independent reasoning judgments." A cross-fit logistic
combination of a single judge with self-consistency, by contrast, gains
nothing over the judge alone (0.754 vs 0.770), showing the ensemble effect
is specific to combining independent *verifiers*, not any combination of
signals.[^c2]

A second measurement points the same way, on the generation side. EdgeJury (arxiv-2601-00850) draws its candidates from several model families and from role-specialized prompts, and its authors state that "Role specialization reduces correlation between outputs and increases coverage."[^c5] Removing role specialization costs 4.8 points on TruthfulQA MC1 in its component table.[^c6] That is one pipeline's ablation, not a comparison of judge families, so it shows that role and family diversity moves accuracy, not that a second provider does. (my reading)

A clinical extraction task shows the same pattern with a different ensemble. In incidentaloma identification from radiology reports, a majority vote over six systems (GPT-4o and GPT-OSS, each with and without anatomy prompting, plus two supervised encoders) reached a three-class lesion-level macro-F1 of 0.902, "surpassing all individual models."[^c7] The members erred in different places: twelve lesions were correct for every GPT-based model and wrong for both encoders, "whereas the opposite occurred only five times."[^c8] The gain sat in the follow-up class, where the ensemble's F1 was 0.830 ("No Risk = 0.889, Follow-up Required = 0.830")[^c9] and the authors note that the follow-up F1 "value increased by more than 0.10."[^c10] Ties went to the lowest label, "providing a conservative bias toward non-incidentaloma predictions."[^c11]

A scale caution applies to that paper's abstract, which sets the ensemble's macro-F1 of 0.90 against a best single system at 0.79: "a majority-vote ensemble of the top systems further improved the macro-F1 to 0.90."[^c12] The 0.79 is an incidentaloma-positive measure, "an incidentaloma-positive macro-F1 of 0.79,"[^c13] "defined as the mean of the F1" over the two incidentaloma classes,[^c14] while 0.902 averages all three classes. On the two incidentaloma classes alone, the ensemble's F1s (0.889 and 0.830) average about 0.86, against about 0.785 for the best single system (0.842 and 0.727).[^c15] That arithmetic is mine, but it shows the abstract's contrast mixes two measures.

For abstention, self-consistency has no usable operating point at all in
this setting: "Self-consistency cannot form a low-risk subset at any
threshold in this split: its most confident region is still too
error-prone." The ensemble instead yields a working frontier, e.g. "At a
target risk of 0.30... it answers 27% of questions with held-out selective
risk 0.24."[^c3]

## Why it matters

This is a measured instance of the uncertainty-score requirement inside
[[abstention]]: a selective model needs a proper score before it can trade
coverage for risk, and this paper shows the score most sensitive to a
question's actual logic — cross-provider LLM judgment — is the first one in
the comparison to make that trade possible at all, where the field's default
(self-consistency) cannot.

## Limits

Tested with exactly two providers (OpenAI, Anthropic); whether a third
provider keeps adding independent error or saturates is untested. The gain
could in principle be an elicitation artifact (OpenAI judges use YES/NO
logits, Claude a verbalized probability) — the paper checks this with a
method-matched OpenAI verbal judge, which still clears the ceiling (0.709
AUROC), but the ensemble's calibration (ECE 0.03) and AUROC are reported
within one domain (execution-correctness SQL) and one calibration/test
split scheme.[^c4]

The incidentaloma ensemble is weaker evidence on this axis. Its six members were "constructed across six strong systems" that are two GPT-family models each in two prompt settings plus two encoders, so the diversity is between model families, not between providers.[^c16] I found no significance test for the ensemble's gain in the passages read. The authors name a cost: "Deploying multiple large-scale models in parallel increases computational overhead."[^c17] The lowest-label tie-break is also a choice the paper does not vary, and it sets the balance on the follow-up class.

## Related

[[abstention]] · [[black-box-correctness-ceiling]] · [[verifier-cross-schema-transfer-gap]] · [[confidence-calibrated-cascade-judgment]] · [[anonymized-cross-review]]

[^c1]: richardson-2026 — "Judges from different providers make different errors, so a two-provider ensemble reaches 0.82 auroc with a well-calibrated probability (expected calibration error 0.03), and it supports useful abstention frontiers (for example, answering 27% of questions at 24% selective risk) where self-consistency offers no valid low-risk subset."
[^c2]: richardson-2026
[^c3]: richardson-2026 — "Self-consistency cannot form a low-risk subset at any threshold in this split: its most confident region is still too error-prone."
[^c4]: richardson-2026 — "to check that the difference is not just an elicitation artifact, we also evaluate a method-matched OpenAI verbal judge, which still clears the black-box ceiling at 0.709 auroc"
[^c5]: arxiv-2601-00850 — "Role specialization reduces correlation between outputs and increases coverage."
[^c6]: arxiv-2601-00850
[^c7]: arxiv-2512-05537 — "parameter-free ensemble achieved the highest overall performance, yielding a Macro-F1 of 0.902"
[^c8]: arxiv-2512-05537 — "whereas the opposite occurred only five times"
[^c9]: arxiv-2512-05537 — "No Risk = 0.889, Follow-up Required = 0.830"
[^c10]: arxiv-2512-05537 — "value increased by more than 0.10"
[^c11]: arxiv-2512-05537 — "providing a conservative bias toward non-incidentaloma predictions"
[^c12]: arxiv-2512-05537 — "a majority-vote ensemble of the top systems further improved the macro-F1 to 0.90"
[^c13]: arxiv-2512-05537 — "an incidentaloma-positive macro-F1 of 0.79"
[^c14]: arxiv-2512-05537 — "defined as the mean of the F1"
[^c15]: arxiv-2512-05537 — "0.842, and 0.727 for the same categories, respectively"
[^c16]: arxiv-2512-05537 — "constructed across six strong systems"
[^c17]: arxiv-2512-05537 — "Deploying multiple large-scale models in parallel increases computational overhead"
