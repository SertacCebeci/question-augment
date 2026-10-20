---
description: "Pretraining a sequence model on corrupted targets, each wrong token followed by a reflect token and the true token, teaches it to revise its own output; fine-tuning alone did not."
aliases: ["reflection pretraining", "reflection-based error injection"]
sources: ["arxiv-2512-20954", "arxiv-2512-20745"]
---
# Reflection token error injection

The method adds one token to the output vocabulary. The paper "augment[s] the vocabulary with a reflection token," so that a protein model's output alphabet is the twenty amino acids plus a reflect symbol.[^r1] The training targets are then corrupted on purpose. At a chosen position the true token is replaced by a wrong one, the reflect token is inserted, and the true token is restored after it. In the RPRE variant the position is drawn at random and the wrong token is a random amino acid, so a target reads as the correct sequence with one error, then reflect, then the right token.[^r2] Ordinary next-token prediction is then run on these targets. The model is thereby trained to emit a reflect token after a mistake and to write the correction that follows it.

Two details make the signal usable. First, the injected wrong token is an input the model must read, not a target it must learn to produce: the paper applies gradient blocking so that "injected errors act as contextual signals rather than learning targets."[^r3] Second, when the random token happens to be the correct one, the reflection is a no-op, and this teaches the model "to maintain confidence when no error is present."[^r4] The same mechanism thus rewards both correcting and keeping a correct token.

A second variant, RPLE, draws the wrong token from later true tokens of the same sequence instead of from the whole vocabulary. The paper says this "creates more realistic, sequence-consistent" errors, such as swapped adjacent residues, which a random substitution rarely produces.[^r5] The injection is also redrawn during training with a batch-level ratio, so the same input is not always corrupted the same way. The paper's reading of that is that "the model is forced to generalize across perturbed inputs."[^r6]

The measured effects, on de novo peptide sequencing, are these. Fine-tuning with the reflection token gave no reflection behaviour at inference, which the paper reads as "reflection behavior is not learned through finetuning alone."[^r7] Pretraining with 60% and 90% error ratios produced reflection on 2.3% and 4.5% of sequences at inference (Table 3). Most of those reflections kept the original token: "Despite most <reflect> tokens retaining the original answer," the paper says, and the corrected share was about 13% in both settings.[^r8] Without injection the validation loss rises after about 100 steps, and the paper says the model "exhibits clear signs of overfitting"; the injected runs at 90% and 99% "lead[] to more stable and monotonic decreases in validation loss."[^r9] The abstract's headline is that the method "teaches protein models to self-correct and leads to substantial performance gains compared to standard" pretraining.[^r10]

## Limits

- One task and one model family: de novo peptide sequencing with an encoder-decoder transformer over mass spectra. The benchmark across nine species is the same task, so the evidence is one task on several datasets, not several tasks.
- Reflection is rare and mostly self-affirming. At 2.3% to 4.5% of sequences, with most reflections keeping the original token, the self-correction the abstract names is a small effect in these numbers (my reading of Table 3).
- The human-in-the-loop check is ten sequences, of which two were corrected by hand-placed reflect tokens. The paper calls the approach not yet scalable, and it is too small to measure a rate.
- The counter-overfitting explanation rests on one validation-loss curve. The paper gives two sources of its accuracy gain, "enhanced thinking ability and a counter-overfitting effect," but the text I read does not separate them with an ablation (my inference).
- Injected errors are synthetic, drawn by a rule. Whether a learned reflex catches the errors a real spectrum model makes is not shown; the paper's own inference-time case study is one sequence.
- The appendix (extended benchmarks, beam size, further case studies) was not read here.
- A different route to revision training, without a reflect token. AgentMath trains on repair traces written from real execution failures: "A small fraction of these negative-to-positive corrections is injected to strengthen debugging robustness."[^r11] It reports no reflect token and no inference-time reflection rate. Its only number is a cumulative ablation in which the self-correction step adds about 2.3 points on AIME24 (my reading of Table 3), and it says of the stage only that "The subsequent integration of a self-correction mechanism" was combined with masked SFT.[^r12] So "fine-tuning alone did not" reflection here is not tested in the other paper, and the two results are not measured on the same behaviour.

## Related

- [[language-expressiveness]] — the paper's argument for why such a token is needed: an enlarged token set lets a correction be written at all.
- [[controlled-error-injection]] — the same construction, a known error at a known position, used here as training data for self-correction and there as labelled test data for hallucination localization.
- [[two-stage-decision-sampling]] — the decision to revise is the step this method trains; that note isolates self-correction as the decision stage.
- [[tool-integrated-reasoning]] — the code-execution setting in which AgentMath's repair traces arise from real interpreter errors, not injected ones.

[^r1]: arxiv-2512-20954 — "we augment the vocabulary with a reflection"
[^r2]: arxiv-2512-20954 — "we randomly sample a position t"
[^r3]: arxiv-2512-20954 — "To ensure that injected errors act as contextual signals rather than learning targets"
[^r4]: arxiv-2512-20954 — "model to maintain confidence when no error is present"
[^r5]: arxiv-2512-20954 — "creates more realistic, sequence-consistent"
[^r6]: arxiv-2512-20954 — "the model is forced to generalize across perturbed inputs"
[^r7]: arxiv-2512-20954 — "indicating that reflection behavior is not learned through finetuning alone"
[^r8]: arxiv-2512-20954 — "Despite most <reflect> tokens retaining the original answer"
[^r9]: arxiv-2512-20954 — "the model exhibits clear signs of overfitting"
[^r10]: arxiv-2512-20954 — "to self-correct and leads to substantial performance gains compared to standard"
[^r11]: arxiv-2512-20745 — "A small fraction of these negative-to-positive corrections is injected to strengthen debugging robustness"
[^r12]: arxiv-2512-20745 — "The subsequent integration of a self-correction mechanism"
