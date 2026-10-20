---
description: "Re-checking a first-person plan from a third-person view of the same video, with no second input, preserved exocentric accuracy; removing that check cost about 1.7 points on Video-MME."
aliases: ["plan-then-verify", "exocentric verification", "ego-exo verification", "cross-perspective verification"]
sources: ["arxiv-2511-18242"]
---
# Cross-perspective plan audit

A model answering a question about a first-person video can first write what the camera wearer will do, then audit that plan from a third-person reading of the same footage. EgoVITA makes this a structured process: the output is split into an egocentric plan, an exocentric verification and a final answer, and the framework is described as decomposing reasoning "into a structured plan-then-verify process".[^c1] The audit is not given another video. It reads the same video "to verify its spatiotemporal and logical consistency, without exocentric video input".[^c2] The point of the switch is stated by the authors as "rather than relying solely on first-person prediction": the plan has to survive a second description of the same evidence before it reaches the answer.[^c3]

The mechanism, as the paper sets it out, is that the plan is checked against scene properties a first-person account does not state. The verifier asks whether the planned actions fit the scene layout, object affordances and observable context, and a plan is kept or changed on that basis.[^c2] My inference, not the paper's claim: a first-person plan can be fluent while placing an object outside the wearer's reach or sequencing actions the visible state does not allow. Restating the scene from outside the wearer's position forces the model to name objects and their relations again, and a conflict between the two readings is then a usable signal. The paper gives the two stages different jobs: the plan carries procedural reasoning, and the audit keeps third-person ability in place.[^c4]

What was measured is the framework against its base model, with the audit removed as an ablation. The headline gains over Qwen2.5-VL-7B are "+7.7 on EgoBlind and +4.4 on EgoOrient".[^c5] Removing the verification stage and keeping the rest lowers exocentric performance, by the paper's figure "−1.7 on Video-MME", and the authors read this as the stage "suggesting that the verification stage" keeping general reasoning intact.[^c6] Removing the plan instead costs egocentric accuracy, "−1.8 on EgoPlan".[^c7] In this setup the audit's measured contribution is therefore to the exocentric side, not the egocentric one; the paper's summary is that the verification "helps retain broader cross-view generalization".[^c8]

The audit is trained as well as prompted. The verification stage is supervised on third-person rationales generated from human-labelled timestamps and filtered by a second model. A confidence reward is added that "reinforces consistent third-person validation of the predicted plan".[^c9]

## Limits

- One policy writes the plan and performs the audit. The paper formulates the system so that "a multimodal large language model (MLLM) acts as a policy", and the same weights produce both stages.[^c10] An auditor that shares the planner's blind spots can accept the planner's errors. This is the self-agreement problem that [[solver-verifier-similarity]] describes; the paper does not test an independent verifier, so whether the gain comes from a distinct check or from more structured output is not separated here.
- The audit never sees the other perspective. Exocentric video is excluded at verification time by design, which is what lets the method avoid paired data.[^c11] It follows that the audit cannot catch an error that only an external camera would reveal. The paper establishes improved exocentric retention, not that the third-person reading is accurate against real exocentric footage.
- The third-person rationales come from a larger model (Qwen2.5-VL-72B) and are filtered by another (Seed1.5-VL).[^c12] Part of the audit's quality is therefore borrowed from teacher data. My inference: the ablation removes the stage, not the teacher, so the share due to the teacher is not isolated.
- The ablation numbers are for one base model and one training recipe, on a 52k-sample corpus.[^c12] Whether a cross-perspective audit helps other models, or helps without the reinforcement learning, is not shown in the part of the paper read here.
- The reported exocentric change is about 1.7 points on one benchmark. A gain that small on one benchmark does not establish a general effect on exocentric reasoning.

## Related

- [[self-other-planning-asymmetry]] — the same egocentric versus exocentric reference-frame distinction, treated there as a source of planning difficulty; this note treats the switch as a check on a plan.
- [[decoupled-modality-verification]] — verifies generated output against a second modality; the audit here switches perspective over one modality instead.
- [[solver-verifier-similarity]] — why a verifier drawn from the solver's own distribution accepts more wrong answers, the main risk for a single-policy audit.
- [[verifier-gain]] — the measure of what a verifier adds, against which an audit's gain would need to be stated.

[^c1]: arxiv-2511-18242 — "decomposes egocentric video reasoning into a structured plan-then-verify process"
[^c2]: arxiv-2511-18242 — "to verify its spatiotemporal and logical consistency, without exocentric video input"
[^c3]: arxiv-2511-18242 — "rather than relying solely on first-person prediction"
[^c4]: arxiv-2511-18242 — "<ego_plan> supports task-specific procedural reasoning"
[^c5]: arxiv-2511-18242 — "outperforming Qwen2.5-VL-7B by +7.7 on EgoBlind and +4.4 on EgoOrient"
[^c6]: arxiv-2511-18242 — "(e.g., −1.7 on Video-MME), suggesting that the verification stage"
[^c7]: arxiv-2511-18242 — "(e.g., −1.8 on EgoPlan), indicating the importance of modeling action sequences before answer generation"
[^c8]: arxiv-2511-18242 — "<exo_verify> helps retain broader cross-view generalization"
[^c9]: arxiv-2511-18242 — "reinforces consistent third-person validation of the predicted plan"
[^c10]: arxiv-2511-18242 — "a multimodal large language model (MLLM) acts as a policy"
[^c11]: arxiv-2511-18242 — "achieves scalable cross-view consistency without requiring paired data"
[^c12]: arxiv-2511-18242 — "with only 52k training samples"
