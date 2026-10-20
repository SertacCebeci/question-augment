---
description: "A question writer trained by RL on a reward for splitting a target model from a reference ensemble, so the questions that expose weaknesses surface without human labels."
aliases: ["model auditing", "disagreement-maximizing question generation", "cross-model divergence probing", "divergence-driven auditor"]
sources: ["arxiv-2512-16921"]
---
# Divergence-rewarded probe generation

A question writer can be trained on a reward that is not correctness. The reward is a split between models. In the work read here, a multimodal model is fine-tuned to write a question about an image, and to propose a counterfactual image, on which a target model and a reference ensemble give different answers. The generator is described as trained "to generate question–image exemplars maximizing response divergence among target models, thereby exposing capability gaps."[^c1] The work calls this model auditing and presents it as an annotation-free framework that "exploits cross-model divergence to discover failure modes."[^c2]

The mechanism has three parts. First, for each generated pair, a binary judge compares the two answers and returns 1 "if the two answers differ in meaning" and 0 otherwise.[^c3] Second, the generator is trained with Group Relative Policy Optimization, which "uses group-relative normalization" of this signal to form advantages within each sampled group.[^c4] Samples that split the target from the rest of their group therefore get the largest push. Third, when one target is audited, the reference is not a single model but an ensemble, and "we instead use an ensemble whose consensus serves as an oracle."[^c5] Once trained, the same generator is run in a single pass to produce exemplars that "reveal model weaknesses."[^c6]

Disagreement alone does not say which side is wrong, so the work adds two assumptions. The first is that when the ensemble agrees, the pair is "likely to be meaningful and answerable."[^c7] The second is that it is "relatively rare for target model to be uniquely correct while all models in the" ensemble are wrong.[^c8] Under these, the consensus is treated as a proxy for correctness, and the generator is updated "only on instances" where the target conflicts with it.[^c9]

What the paper measures: with prompt engineering alone (the baseline, no fine-tuning) the search finds valid errors at a much lower rate than the trained auditor, over 20K attempts.[^c10] Of the discovered weaknesses, the paper's own check found that 81.3% of the samples "expose genuine weaknesses of" the target, with the rest ambiguous or unanswerable.[^c11] Fine-tuning on the auditor's exemplars improves the target across benchmarks; the paper reports that "fine-tuning on the same data without AuditDM yields only marginal improvements on a" few benchmarks, which is the comparison used to attribute the gain to the generated data.[^c12]

What transfers to asking well is the scoring rule, not the vision setting: a question is judged by where its answerers split from a consensus, rather than by how hard it looks in the abstract. The paper's own ablation points the same way: "asking more informative, targeted questions is an especially effective way" to improve the model, and the probing-question policy gave the largest gains.[^c13]

## Limits

- Disagreement is not error. In the paper's check, 11.5% of samples were ambiguous and 7.2% unanswerable (Table 8 lists the three categories with these values).[^c11] The paper expects "a higher percentage of target failures when using a more powerful ensemble."[^c14] So the precision of the reward is set by the reference, and a weaker ensemble would make the reward noisier. This was not tested beyond the ensembles the paper used.
- Reward hacking is the expected failure. A generator rewarded for splitting models can drift toward questions that are merely ambiguous or unanswerable. The two assumptions are the guard against that, and they hold only where the ensemble is right in the disagreements. The paper's validation covers its own sample only.
- The annotation-free claim is partial. Pseudo-labels for evaluation came from strong external models, "with human reverification on disagreements."[^c15] The auditor needs no labels for training, but the check that its findings are real does.
- Image dependence. "AuditDM requires images with dense annotations to generate probing questions for studying model behavior on tasks such as grounding and segmentation."[^c16] Text and diagram OCR were also hard for the image generator.
- Cost. "we spend about 5 days on 8 H100 to generate new text–image pairs" for one target.[^c17]
- Scope. The tests are VQA-style on two model families (PaliGemma2 and Gemma3). Whether an analogous disagreement reward works for text-only questioning, or for a tool-using asker, is not tested here.

## Related

- [[query-by-committee]] — disagreement as a selection signal over a stream of inputs; here disagreement is a training reward for a generator, and the oracle is an ensemble rather than sampled hypotheses.
- [[self-evolving-visual-questioner]] — a VLM that also proposes its own questions and retrains on them, but its filter is a frozen rewriter, not a target's disagreement.
- [[adversarial-unanswerable-questions]] — the failure a disagreement reward has to avoid: questions that look answerable and are not.
- [[disagreement-retention-in-debate]] — disagreement used to choose which responses to broadcast, not to train a question writer.

[^c1]: arxiv-2512-16921 — "AuditDM trains an MLLM auditor that generates question–image exemplars maximizing response divergence among target models, thereby exposing capability gaps."
[^c2]: arxiv-2512-16921 — "an annotation-free framework that exploits cross-model divergence to discover"
[^c3]: arxiv-2512-16921 — "judge that returns 1 if the two answers differ in meaning"
[^c4]: arxiv-2512-16921 — "GRPO uses group-relative normalization"
[^c5]: arxiv-2512-16921 — "we instead use an ensemble whose consensus serves as an oracle"
[^c6]: arxiv-2512-16921 — "uncovers diverse, interpretable exemplars that reveal model weaknesses"
[^c7]: arxiv-2512-16921 — "when the ensemble models agree on an answer, the question–image pair is likely to be meaningful and answerable."
[^c8]: arxiv-2512-16921 — "it is relatively rare for target model to be uniquely correct while all models in the"
[^c9]: arxiv-2512-16921 — "update A only on instances"
[^c10]: arxiv-2512-16921 — "relying solely on prompt engineering to find failures"
[^c11]: arxiv-2512-16921 — "81.3% of the samples indeed expose genuine weaknesses of"
[^c12]: arxiv-2512-16921 — "without AuditDM yields only marginal improvements on a"
[^c13]: arxiv-2512-16921 — "asking more informative, targeted questions is an especially effective way"
[^c14]: arxiv-2512-16921 — "of target failures when using a more powerful ensemble"
[^c15]: arxiv-2512-16921 — "with human reverification on disagreements"
[^c16]: arxiv-2512-16921 — "AuditDM requires images with dense annotations to generate probing questions"
[^c17]: arxiv-2512-16921 — "we spend about 5 days on 8 H100 to generate new text–image pairs"
