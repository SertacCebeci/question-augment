---
description: "Bundling two related axes into one jointly-scored question halves the number of questions asked but measurably lowers label-recovery accuracy, a quantified trade-off with a non-inferiority bootstrap."
aliases: ["symptom-cluster elicitation", "fixed three-cluster policy", "joint symptom-cluster questioning"]
sources: ["wang-2026-scale"]
---
# Clustered-question elicitation

> Instead of one question per axis, ask one question that names two axes at
> once and scores each independently from the single response — fewer
> questions, at a measured and bounded cost in label-[[recovery-postulate|recovery]] accuracy.

## Definition / Mechanism

Wang (2026) compares, on a six-axis daily symptom-rating
task, a **fixed six-item policy** (one question per axis) against a **fixed
three-cluster policy** that pairs two axes per question. The pairing is
fixed in advance by linguistic distinctness of the paired axes (e.g., mood
swing paired with stress), not chosen adaptively per respondent: "A cluster
response used a joint prompt that named both target symptoms and required
two independent JSON scores; the prompt explicitly prohibited transferring
one symptom's severity to the other."[^c1]

On a locked 36-participant, 360-day evaluation set, the six-item policy
reached the higher agreement, and the three-cluster policy reached lower
agreement at half the question count, with higher recall on the more severe
end of the scale: "Fixed six-item questioning produced the highest label
agreement (QWK 0.976; MAE 0.087; exact agreement 91.30%). The fixed
three-cluster policy halved the question count, with QWK 0.913, MAE 0.251,
exact agreement 77.45%, and within-one agreement 97.45%." Its recall for
moderate-or-higher severity was 80.94%, against 76.87% for the fixed
six-item policy.[^c2]

A participant-clustered bootstrap sizes the cost rather than leaving it as a
single point estimate: "The participant-cluster bootstrap estimated a QWK
difference of −0.0623 (95% CI −0.0761 to −0.0483, two-sided p = 0.001) for
fixed three clusters versus fixed six items. The confidence interval crossed
the −0.05 non-inferiority margin."[^c3]

## Why it matters

For stall 2 this is a second axis of the selection question beyond *which*
axis to ask about next: *how many* axes one question can carry at once, and
what that costs. The paper's own comparison condition shows that the
alternative — letting the respondent open with a free narrative and
following up only on unresolved axes — does not buy back the accuracy
either: "Open-first dialogue performed worse than direct cluster
elicitation. An unrestricted opening exposed only a small fraction of the
six target domains, forcing almost complete follow-up while also
introducing evidence-gate errors."[^c4]

A fixed, pre-declared bundling of axes beat an adaptive attempt to discover
which axes needed asking about at all — for this practitioner, that is a
reason to treat "how many axes per question" as a design choice made before
the conversation, not one adapted during it.

## Limits

One arXiv preprint (2026), not independently verified by this wiki [?];
one narrow domain (six-axis daily premenstrual symptom ratings, Simplified
Chinese, a 1.5B-parameter local scorer) and one fixed pairing of axes chosen
by the authors for linguistic separability — the paper itself reports that a
pairing without a clean linguistic boundary (fatigue and sleep) produced
more confusable scores than the mood-swing/stress pairing, so the
mechanism's cost is pairing-dependent, not a single constant. The comparison
runs on deterministic, label-conditioned synthetic follow-up utterances, not
live respondents, so any cost from real conversational drift or [[efe-planning-as-variational-inference|ambiguity]] is
untested.

## Related

[[adaptive-ema-item-timing-selection]] · [[gap-monitoring-burden]] · [[expected-information-gain]] · [[value-of-information]]

[^c1]: wang-2026-scale
[^c2]: wang-2026-scale
[^c3]: wang-2026-scale
[^c4]: wang-2026-scale — "Open-first dialogue performed worse than direct cluster elicitation. An unrestricted opening exposed only a small fraction of the six target domains, forcing almost complete follow-up while also introducing evidence-gate errors."
