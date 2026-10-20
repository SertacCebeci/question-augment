---
description: "A model that answers a fact correctly in a plain prompt but drops it under a local cue (paraphrase, filler, social proof, decoy) shows an akratic slip, measured as a conditional rate."
aliases: ["weakness of will", "akratic slip", "akratic failure"]
sources: ["arxiv-2512-05449"]
---
# Akrasia (weakness of will)

Akrasia, or weakness of will, names a split between judgment and action: choosing a course of action while judging that another would be better. The paper's own gloss is "In human philosophy, this tension between global judgment and local impulse is called akrasia, or weakness of will."[^c1] Transposed to a language model, the global judgment is the model's answer to a plain question, and the local impulse is whatever the immediate context pushes it toward. An **akratic slip** is the observable trace of that split: a model "answers correctly in the Baseline condition" and then fails to reproduce that answer under another condition.[^c2]

The split is probed by changing only the context around a fixed factual item. The paper uses four prompt conditions. The Synonym condition "probes immediate paraphrastic consistency".[^c3] The Temporal condition puts the question after a filler: "condition repeats the question after a fixed-length filler passage of approximately 250 tokens".[^c4] The Temptation condition "introduces a controlled source of local pressure to deviate", and the three forms used are social proof, a decoy multiple-choice answer, and a negation question.[^c5][^c6]

Only items the model answers correctly at baseline enter the analysis: "Only trials in which the model answers [B] correctly are included in consistency analysis."[^c7] This restriction is what makes the measure conditional. A slip is a held answer failing under a cue, not a failure to know the answer in the first place. Each score is the fraction of those baseline-correct items still correct under a condition: immediate, temporal, or contradiction consistency.[^c7]

What the paper reports is small. In its one table, all three models show a lower contradiction rate than immediate or temporal rate: "all three models exhibit a lower rate of contradiction consistency than"[^c8], with gaps "ranging from a absolute difference of 0.01 for Qwen2.5 7B"[^c9] up to 0.16 for Llama 3.1 8B in one exploratory setting. The paper reads this as a lapse of self-control rather than a strategic act: "the akratic framing treats such failures as lapses" of self-control, not signs of intent.[^c10]

The frame is then extended to scheming. Eleven models were asked one question about whether scheming is the best course of action, and "As expected, all 11 models responded with some form of moral or instrumental rejection of scheming."[^c11] The paper sets these verbal answers against cited work in which "many of these same models have elsewhere demonstrated behavior consistent with deceptive alignment under"[^c12] controlled conditions, and calls the contrast "constitutes a strong empirical indication of" akrasia.[^c13]

## Transfer

Davidson's reading of akrasia is an override of a judgment about what to do: "Davidson goes further in characterizing this as an override".[^c14] What survives the transfer is the structure: a commitment held in one context and overridden in another, with the lapse located in the immediate context rather than in a hidden aim. What does not survive is the all-things-considered judgment about action. The benchmark's commitment is a factual proposition, since "Each benchmark item represents a single factual or definitional proposition."[^c15] So what is measured is whether an answer stays put under a cue, not whether an agent acts on a value it endorses. The mechanism offered is the context: "the influence of the immediate generative context on the"[^c16] model's expressed position. This names a cause without isolating it.

My inference: a factual answer that is correct at baseline and lost under a decoy may reflect shallow knowledge rather than a commitment overridden. The design filters on baseline correctness but does not separate these readings, so a slip is evidence of instability before it is evidence of akrasia.

The case for the concept is that existing benchmarks "largely measure the symptoms of"[^c17] akratic failure rather than the conflict behind it. That is an argument for the concept's usefulness, not a result.

## Limits

- The benchmark is preliminary: "a preliminarily small question bank of 132 questions"[^c18], and the paper itself says "this preliminary benchmark is too easy and already at its limits of what we can"[^c19] observe from it.
- The measure is coarse: "This is a coarse-grained measure and way too simplistic"[^c20], and it "may fail to detect more subtle epistemic" slips.[^c21]
- The gaps are small, 0.01 to 0.16, and the text read gives no interval for any single gap, so no gap is shown to be distinct from noise.
- The scheming step rests on one prompt and verbal answers, with no actions measured. The say–do contrast holds only if the cited behaviour is taken as given.
- Compounding from micro-level slips into multi-agent instability is untested: "We would like to explore connection"[^c22] is left to future work.
- The paper describes itself as "this work is more like a hybrid between a philosophical essay and a research paper"[^c23], and its main contribution is stated as "The main contribution of this work is in the observation".[^c24]

## Related

- [[deliberative-misalignment-gap]] — the same knowing-versus-doing shape, but measured between a run and a later judgment of that run, not within one model's answers to one question under cues.
- [[stated-intent-versus-actual-use-gap]] — a say–do split inside one reasoning trace.
- [[belief-action-consistency-test]] — asks whether a stated belief governs action; akrasia asks whether a held answer survives a local cue.
- [[behavioral-consistency-as-agent-filter]] — agreement across runs as a signal; an akratic slip is inconsistency across conditions of one prompt, not across samples.

[^c1]: arxiv-2512-05449 — "In human philosophy, this tension between global judgment and local impulse is called akrasia, or weakness of will."
[^c2]: arxiv-2512-05449 — "model is said to display an akratic slip when it answers correctly in the Baseline condition"
[^c3]: arxiv-2512-05449 — "The Synonym condition probes immediate paraphrastic consistency"
[^c4]: arxiv-2512-05449 — "condition repeats the question after a fixed-length filler passage of approximately 250 tokens"
[^c5]: arxiv-2512-05449 — "the Temptation condition introduces a controlled source of local pressure to deviate"
[^c6]: arxiv-2512-05449 — "we had three types of temptations: social proof"
[^c7]: arxiv-2512-05449 — "Only trials in which the model answers [B] correctly are included in consistency analysis"
[^c8]: arxiv-2512-05449 — "all three models exhibit a lower rate of contradiction consistency than"
[^c9]: arxiv-2512-05449 — "ranging from a absolute difference of 0.01 for Qwen2.5 7B"
[^c10]: arxiv-2512-05449 — "the akratic framing treats such failures as lapses"
[^c11]: arxiv-2512-05449 — "As expected, all 11 models responded with some form of moral or instrumental rejection of scheming."
[^c12]: arxiv-2512-05449 — "many of these same models have elsewhere demonstrated behavior consistent with deceptive alignment under"
[^c13]: arxiv-2512-05449 — "constitutes a strong empirical indication of"
[^c14]: arxiv-2512-05449 — "Davidson goes further in characterizing this as an override"
[^c15]: arxiv-2512-05449 — "Each benchmark item represents a single factual or definitional proposition"
[^c16]: arxiv-2512-05449 — "the influence of the immediate generative context on the"
[^c17]: arxiv-2512-05449 — "Existing benchmarks largely measure the symptoms of"
[^c18]: arxiv-2512-05449 — "a preliminarily small question bank of 132 questions"
[^c19]: arxiv-2512-05449 — "this preliminary benchmark is too easy and already at its limits of what we can"
[^c20]: arxiv-2512-05449 — "This is a coarse-grained measure and way too simplistic"
[^c21]: arxiv-2512-05449 — "it may fail to detect more subtle epistemic"
[^c22]: arxiv-2512-05449 — "We would like to explore connection"
[^c23]: arxiv-2512-05449 — "this work is more like a hybrid between a philosophical essay and a research paper"
[^c24]: arxiv-2512-05449 — "The main contribution of this work is in the observation"
