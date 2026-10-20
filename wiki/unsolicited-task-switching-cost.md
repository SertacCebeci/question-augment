---
description: "In AI-assisted expert work, extraneous load costs about three times intrinsic load, and the model's unsolicited task switching is its strongest source; sheer information volume matters less."
aliases: ["model-initiated task switching", "extraneous load in proactive dialogue", "precision proactivity"]
sources: ["doi-10-48550-arxiv-2505-10742"]
---
# Unsolicited task-switching cost

When an assistant volunteers information, the useful question is not how much it adds but whether it stays inside the subtask the user is working on. Lepine et al. applied Cognitive Load Theory to transcripts of 34 financial professionals valuing a company with GPT-4o. They estimated intrinsic and extraneous load per participant-subtask from a task decomposition and knowledge graph (1,178 observations).

## What was measured

Using AI-generated content is positively associated with output quality (beta about 0.32 to 0.35). Extraneous load has the largest negative association (about -0.47 to -0.49), roughly three times intrinsic load (about -0.15).[^c1] The interactions of content use with either load type are consistently null, so benefit and penalty add independently and do not trade off.[^c2]

Among behaviours, the model introducing subtasks not anchored in the user's immediately preceding focus is the strongest and most robust negative predictor of quality. It survives controls for task complexity, content use and background, and it is not a proxy for verbosity.[^c3] The ordering the authors report is task switching, then information sprawl, then truncation. Sprawl is largely absorbed by switching once both are modelled, and truncation does not reliably predict quality.[^c4] The authors read this as: the problem is not necessarily the amount of information, but the organizational consequences of introducing it in ways that expand or redirect task space.[^c5]

The disruption is asymmetric by speaker. Performance is most sensitive to the organizational state the user brings to the exchange: user-side dependency debt (mentioning a subtask without having engaged its prerequisites) lowers quality, while the response-side counterpart does not.[^c6]

## Persistence

Extraneous load is path-dependent. Both speakers carry load forward across turns, there is modest spillover from prompt load to the next response and none from response to prompt. Once either side enters a high-load pattern, the dialogue offers weak endogenous repair.[^c7] The authors' practical reading is to treat high extraneous-load trajectories as detectable events requiring repair.[^c8]

## Expertise

Less experienced professionals gain more per unit of AI content but suffer a larger extraneous-load penalty. Experienced ones take up more AI content as load rises, and gain less per unit.[^c9]

## Limits

- One domain (financial valuation), one model (GPT-4o), 34 participants. The authors state that porting requires rebuilding the task decomposition and knowledge graph.[^c10]
- Load is estimated from transcripts by computational indicators, not by physiological or self-report measures; the associations are observational, not causal.
- The extraneous composite mixes clutter with switching, sprawl and truncation, so the hierarchy depends on that operationalisation.
- My inference, not tested here: the same ordering would hold for clarifying questions that redirect the task. The paper studies unsolicited information, not questions.

## Related

- [[proactivity-taxonomy]] — sorts agents by whether they decide when to speak; this note measures what a spoken contribution costs
- [[net-expected-value-of-alerting]] — the benefit-versus-interruption-cost framing this paper supplies empirical cost terms for
- [[user-patience-model]] — another account of user-side cost accumulating across turns
- [[tgl-proactive-trigger]] — a trigger design that could use task-anchoring as a gate

[^c1]: doi-10-48550-arxiv-2505-10742 — "extraneous load exhibits the largest negative association (e.g., 𝛽 ≈ −0.47 to"
[^c2]: doi-10-48550-arxiv-2505-10742 — "AIGCU × EL and AIGCU × ICL interactions are"
[^c3]: doi-10-48550-arxiv-2505-10742 — "suggesting that task switching captures a distinct and"
[^c4]: doi-10-48550-arxiv-2505-10742 — "a hierarchy of harmful behaviors—task switching > information sprawl > truncation—providing"
[^c5]: doi-10-48550-arxiv-2505-10742 — "the problem is not necessarily the amount of information the model provides, but the organizational consequences of introducing that information"
[^c6]: doi-10-48550-arxiv-2505-10742 — "performance is most sensitive to the organizational state the user brings to exchange."
[^c7]: doi-10-48550-arxiv-2505-10742 — "once either speaker enters a high-load conversational pattern, that pattern tends to persist"
[^c8]: doi-10-48550-arxiv-2505-10742 — "treating high extraneous-load trajectories as detectable events requiring repair."
[^c9]: doi-10-48550-arxiv-2505-10742 — "whereas less experienced professionals show larger quality"
[^c10]: doi-10-48550-arxiv-2505-10742 — "porting to other domains requires rebuilding domain-specific"
