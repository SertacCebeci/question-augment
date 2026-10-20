---
description: "Outcome-only RL that rewards only a correct final verdict can make a generative verifier check its own intermediate steps inside its chain of thought, with no step labels."
aliases: ["thinking-induced process supervision", "outcome-only process supervision", "process signal from outcome reward", "TIPS"]
sources: ["doi-10-48550-arxiv-2609-36641"]
---
# Outcome-induced process verification

A generative verifier can be trained on one bit per trajectory, whether its final verdict matches the ground truth, and still come to judge intermediate steps. The mechanism sits in the training signal. The reward is 1 when the predicted outcome equals the label and 0 otherwise.[^o1] Under GRPO the group-relative advantage that this reward produces is applied to the whole sampled response, including the chain of thought, the step labels and the outcome label.[^o2] The reward never reads the step labels: "Importantly, no process label is used in the reward."[^o3]

The argument for why this induces step checking is that a thought which tests each step is more often right about the verdict. Rollouts "that accurately evaluate step validity within their thinking process are more likely to predict the correct outcome, thereby earning higher relative advantages."[^o4] Under reinforcement, such thought patterns get reinforced. The authors report that the gain is carried by the reasoning trace: a label-only variant, trained without a thought, "does not learn reliable process verification from labels alone"[^o5], and the authors read the gains as "mediated by reasoning traces that RL can shape."[^o6] At inference the generated step labels are used directly: "we use the generated process labels" as step-level judgments, so the verifier needs only outcome-labelled trajectories to train.[^o7]

The authors give an information-theoretic account. Under an assumption that the pre-reasoning representation does not fully determine the verdict, "This rules out the degenerate case where the model can infer the final verdict directly from R" [^o8], and by Fano's inequality, "low outcome error implies that the thinking chain" must carry information about the outcome.[^o9] A second inequality ties outcome information to step information through the residual uncertainty about the outcome once the step labels are known. Combined, the thought must carry information about the process "is low, and the final outcome is tightly coupled with step-level correctness, the generated thought" whenever verification is nontrivial and the outcome error is low.[^o10] The bound is a lower bound on mutual information between the thought and the step labels. It says the thought contains that information; it does not say the steps are judged faithfully (my reading).

The measured claim is on ProcessBench: a Qwen3-4B thinking model trained this way "achieves 85.2 F1 using only 3.2K outcome-labeled trajectories".[^o11] The paper argues that the coupling holds in mathematics, where once the step validity is known the correctness of the final answer is often nearly determined, so the coupling term is small there.[^o12]

## Limits

- The coupling the bound needs is an assumption about the task. The authors state that the induced signal "is weaker when final task success is only indirectly related to local step" correctness.[^o13] Where the outcome can be predicted from the input alone, the first term vanishes, and the paper names this input-level shortcut as a route where the thought need not encode process information.[^o14]
- The bound loosens when outcome optimisation fails: "if RL fails to reduce the outcome error Pe" the outcome-error term stays large and the bound becomes loose.[^o15] The label-only result shows the same dependence from the other side: "RL may improve outcome prediction without reliably yielding faithful step-level judgments."[^o16]
- The backbone matters. The authors say that "For weaker backbones or label-only prompting, outcome-supervised" RL may not yield faithful step judgments, so the method rests on the model's ability to express verification in its thought.[^o20]
- The evidence is pure text: "we focus on pure-text reasoning and agent trajectories," and multimodal settings are untested.[^o17]
- The reported lead over prompt-only judges is not a lead over the strongest model: the abstract says the verifier is "while still trailing o1-mini."[^o18]
- The induced labels are not human step annotations, and the authors warn that they "may be biased, miscalibrated, or unreliable in" domains where final success is weakly tied to local step correctness.[^o19]

## Related

- [[process-outcome-consistency-verification]] — the explicit route: a reward that checks the derivation against the answer, where this note has the consistency only induced through the answer's reward
- [[process-reward-model-hackability]] — the step-level reward models that outcome-induced labels are meant to stand in for at lower cost
- [[cot-judge-detection-localization-gap]] — judges that detect a flaw but cannot place it; ProcessBench's first-error task, on which the induced labels are measured, tests the placement
- [[reasoning-trace-behavioral-transfer]] — another case where RL shapes the reasoning trace beyond the final answer

[^o1]: doi-10-48550-arxiv-2609-36641 — "The reward depends solely on whether the predicted outcome matches the ground truth"
[^o2]: doi-10-48550-arxiv-2609-36641 — "the same outcome-derived advantage is applied to every token in the generated response, including those in the CoT, step labels, and outcome label"
[^o3]: doi-10-48550-arxiv-2609-36641 — "Importantly, no process label is used in the reward."
[^o4]: doi-10-48550-arxiv-2609-36641 — "validity within their thinking process are more likely to predict the correct outcome, thereby earning"
[^o5]: doi-10-48550-arxiv-2609-36641 — "process verification from labels alone; the gains are"
[^o6]: doi-10-48550-arxiv-2609-36641 — "mediated by reasoning traces that RL can shape."
[^o7]: doi-10-48550-arxiv-2609-36641 — "we use the generated process labels"
[^o8]: doi-10-48550-arxiv-2609-36641 — "This rules out the degenerate case where the model can infer the final verdict directly from R"
[^o9]: doi-10-48550-arxiv-2609-36641 — "low outcome error implies that the thinking chain"
[^o10]: doi-10-48550-arxiv-2609-36641 — "is low, and the final outcome is tightly coupled with step-level correctness, the generated thought"
[^o11]: doi-10-48550-arxiv-2609-36641 — "achieves 85.2 F1 using only 3.2K outcome-labeled trajectories"
[^o12]: doi-10-48550-arxiv-2609-36641 — "holds in mathematical reasoning: once the validity of the intermediate steps is known, the correctness"
[^o13]: doi-10-48550-arxiv-2609-36641 — "induced process signal is weaker when final task success is only indirectly related to local step"
[^o14]: doi-10-48550-arxiv-2609-36641 — "if the outcome can already be predicted from R"
[^o15]: doi-10-48550-arxiv-2609-36641 — "if RL fails to reduce the outcome error Pe"
[^o16]: doi-10-48550-arxiv-2609-36641 — "RL may improve outcome prediction without reliably yielding faithful step-level judgments."
[^o17]: doi-10-48550-arxiv-2609-36641 — "we focus on pure-text reasoning and agent trajectories"
[^o18]: doi-10-48550-arxiv-2609-36641 — "while still trailing o1-mini"
[^o19]: doi-10-48550-arxiv-2609-36641 — "they may be biased, miscalibrated, or unreliable in"
[^o20]: doi-10-48550-arxiv-2609-36641 — "For weaker backbones or label-only prompting, outcome-supervised"
