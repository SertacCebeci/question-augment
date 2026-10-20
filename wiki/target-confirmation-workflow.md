---
description: "A multi-agent system scores its own grounding of a user instruction against candidate targets and asks the user to clarify only when that score falls below a fixed threshold."
aliases: ["Target Confirmation Workflow"]
sources: ["ge-2026-understanding"]
---
# Target Confirmation Workflow

> Before an interactive segmentation agent acts, a dedicated agent grounds
> the instruction against detected candidates and scores its own
> confidence; only a score below a fixed threshold opens a clarification
> turn — every other instruction is acted on silently.

## Definition / Mechanism

Ge et al. (2026) give EgoMed-Agent's
Confirmation Agent a scoring step: given instruction $I$ and candidate
targets $O$ from a Detection Agent, it outputs a target result and a
[[calibration|reliability]] score, $\theta^*, s = A_{con}(I, O)$. "Given a grounding
reliability threshold τ1, if s ≥ τ1, the grounding result is considered
reliable, and θ∗ is directly confirmed as the user-intended target...If s
< τ1... the Confirmation Agent proactively requests clarification from the
user and updates the grounding result according to the user's
clarification response."[^c1]

The threshold is fixed, not learned online: "The grounding reliability
threshold in Target Confirmation is set to τ1 = 0.8."[^c2]

## Why it matters

This is a binary, score-gated instance of stall 2's "whether to ask at
all" decision, structurally close to an [[entropy]]-threshold trigger but
scored by an LLM's own grounding confidence rather than a predictive
distribution's entropy. On the paper's full pipeline, EgoMed-Agent reaches
"71.34% average Dice, far above the best text-prompted baseline (11.70%)"
across twelve segmentation targets (p < 0.001 on every target against the
strongest baseline, MedSAM3).[^c3]

The gate's own decision quality was validated separately: on a 200-sample
set balanced across four instruction types, "with DeepSeek-V4-Flash the
Confirmation Agent attains 100% GSA and 100% TCA... On the same set, a
lighter LLM (DeepSeek-Chat) reaches only 80% GSA and 70.5% TCA, with
errors concentrated on organ-relative spatial instructions." GSA measures
whether the agent correctly judges an instruction as directly groundable
or clarification-needing; TCA measures whether the eventually confirmed
target (direct or post-clarification) matches ground truth.[^c4]

## Limits

The reliability score s is produced by prompting a single LLM
(DeepSeek-V4-Flash) to output it, not by a calibrated probabilistic model,
so the 0.8 threshold has no guarantee of meaning the same thing across
instructions or models — the paper's own ablation shows a weaker LLM at
the same threshold degrades GSA/TCA sharply. The 100%/100% validation
figure is on one 200-sample, self-constructed, class-balanced set (four
instruction types, 50 each) for one domain (egocentric medical image
segmentation); it is not evidence the threshold transfers to open-ended or
higher-cardinality candidate sets. The paper does not isolate the
Confirmation Agent's contribution to the 71.34%-vs-11.70% Dice gap from
the system's second workflow (mask propagation), so that headline number
is a whole-system result, not a clean measure of the confirmation gate
alone.

## Related

[[entropy-threshold-clarification-trigger]] · [[missing-input-clarification-gate]] · [[clarification-request]] · [[value-of-information]]

[^c1]: ge-2026-understanding
[^c2]: ge-2026-understanding — "The grounding reliability threshold in Target Confirmation is set to τ1 = 0.8."
[^c3]: ge-2026-understanding
[^c4]: ge-2026-understanding — "with DeepSeek-V4-Flash the Confirmation Agent attains 100% GSA and 100% TCA, judging whether an instruction is directly groundable and, when ambiguous, determining the user-intended target through clarification. On the same set, a lighter LLM (DeepSeekChat) reaches only 80% GSA and 70.5% TCA, with errors concentrated on organ-relative spatial instructions"
