---
description: "RL on a composite task finds new reasoning paths only when the base model already has the atomic skills; without them its pass@k curve merges with SFT's, so RL only amplifies."
aliases: ["RL synthesizer versus amplifier", "SFT generalization paradox", "atomic-first recipe", "atomic prerequisite for RL generalization"]
sources: ["arxiv-2512-01970", "doi-10-48550-arxiv-2609-12230"]
---
# Atomic sufficiency for RL synthesis

Two readings of reinforcement learning after supervised training are in dispute. One holds that RL can produce new reasoning skills. The other, which the paper attributes to Wu and Choi and to Yue et al., characterizes RL "as an amplifier of probability mass already present in the post-SFT distribution."[^b0] The paper's proposal is to settle the question on a task where the parts of a composite are known. Its claim is conditional: RL synthesizes a composite only when the base model has the atomic parts. "RL synthesizes new complex skills only when the base model possesses sufficient atomic skills."[^b1]

The composite is the task defined in [[complementary-reasoning]], a chain that needs a stored fact and a contextual fact. The two atomic skills are trained by supervised fine-tuning first. The recipe then runs RL on composite data. The comparison arm trains supervised fine-tuning directly on composites and then runs the same RL. The measured difference is in how RL behaves on the two starting points.

The clearest evidence is the pass@k curve, which the paper uses to separate synthesis from amplification. Synthesis predicts that the RL model keeps pulling ahead as k grows, because it reaches paths the base model cannot sample. Amplification predicts convergence. For the atomic-first start, the RL model "remains significantly higher than SFT (blue) even at maximal k = 29", and the authors read the persistent gap as "RL has synthesized a robust, novel mechanism". For the composite-only start the curves meet: "the SFT model effectively matches the RL model."[^b2][^b3] The authors' summary is "Without sufficient atomic skills, RL merely amplifies."[^b4]

The same split shows up in what RL adds to each start. Composite-only SFT "gains almost nothing from RL" on the composite task, while the atomic-first model "nearly doubles its performance across all levels."[^b5][^b6] Removing one atomic skill also removes the effect: "Removing any atomic skill collapses generalization."[^b7] Further supervised training on composites does not substitute for RL in the paper's comparison, where the RL arm "more than doubles SFT/LoRA" on unseen combinations.[^b8]

Read for training, the result says that in-distribution accuracy after supervised training is not the quantity that predicts RL gains. The authors' own statement is that "underlying atomic skills, not initial performance, are the true predictor of RL success."[^b9] A model can match another on seen composite paths and still differ in whether RL can extend it; that gap between seen and unseen performance is the part of the result that seems to carry over to answerers (my reading). Its relation to asking and answering is indirect: it says what kind of training lets an answerer combine known parts on paths it has not seen.

A second measurement points the same way on a different base, though it varies a different thing. A Qwen3-14B study of disease knowledge graphs starts RL either from an SFT checkpoint or from one repaired on its one-hop errors ([[failure-triage-before-repair]]). For Gastroparesis, RL from the unrepaired checkpoint added little: the gain was "+0.29 percentage points across 3-hop, 4-hop, and 5-hop QA, whereas CGModel-Repaired-RL improves over", and the repaired start gained "CGModel-Repaired by an average of +2.35 points".[^b10][^b11] The authors read this as RL being limited by "Hence, improvement can be limited by errors inherited" from the SFT stage.[^b12] In the atomic-skill study the missing ingredient was a skill absent from the base; in this one it is a lower-hop fact the base gets wrong (my reading of the two setups). Whether the two results are one mechanism is not established by either text; I read them as parallel (my inference).

## Limits

- Pass@k convergence or divergence at k up to 29 is the authors' operational test of "new skill". A finite-k gap does not show that a skill is absent from the base distribution at larger k; the amplifier reading of the converging curve is the paper's interpretation.
- The necessity test removes atoms within one setup: synthetic biographies, one composite family, and atomic skills learned by supervised fine-tuning. Whether partial atomic skill gives partial synthesis is not established by the comparison read; the baselines with deficient atoms are the endpoints only.
- The RL arm uses a fixed composite budget (12.8k samples in the necessity comparison). The text read does not show how the gap changes with much larger RL budgets or with other reward designs.
- The work is one paper. The two literatures it cites disagree on the same question, and this paper's result is one side of that disagreement under its own setup, not a resolution across tasks.
- The claim concerns training. Whether a prompted or retrieval-augmented answerer has an analogous prerequisite is not tested here, and I do not carry it over (my inference).

## Related

- [[complementary-reasoning]] — the composite task whose atomic parts are trained here; this note is about how RL behaves on it
- [[post-training-recipe-contamination-transfer]] — the same SFT-memorizes, RL-generalizes split, measured with a contamination counterpart rather than pass@k
- [[question-asking-skill-transfer]] — RL on one skill (question generation) improving another (answering), a transfer result of a related kind on different tasks

[^b0]: arxiv-2512-01970 — "characterize RL as an amplifier of probability mass already present in the post-SFT distribution"
[^b1]: arxiv-2512-01970 — "RL synthesizes new complex skills only when the base model possesses sufficient atomic skills"
[^b2]: arxiv-2512-01970 — "remains significantly higher than SFT (blue) even at maximal"
[^b3]: arxiv-2512-01970 — "the SFT model effectively matches the RL model"
[^b4]: arxiv-2512-01970 — "Without sufficient atomic skills, RL merely amplifies"
[^b5]: arxiv-2512-01970 — "gains almost nothing from RL"
[^b6]: arxiv-2512-01970 — "nearly doubles its performance across all levels"
[^b7]: arxiv-2512-01970 — "Removing any atomic skill collapses generalization"
[^b8]: arxiv-2512-01970 — "more than doubles SFT/LoRA"
[^b9]: arxiv-2512-01970 — "underlying atomic skills, not initial performance, are the true predictor of RL success"
[^b10]: doi-10-48550-arxiv-2609-12230 — "+0.29 percentage points across 3-hop, 4-hop, and 5-hop QA, whereas CGModel-Repaired-RL improves over"
[^b11]: doi-10-48550-arxiv-2609-12230 — "CGModel-Repaired by an average of +2.35 points"
[^b12]: doi-10-48550-arxiv-2609-12230 — "Hence, improvement can be limited by errors inherited"
