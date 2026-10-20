---
description: "Selective hearing is an audio model attending to an intended speaker while refusing to process or reveal a bystander's speech, measured by scoring each speaker under two instructions."
aliases: ["bystander privacy", "speaker-selective refusal", "selective listening"]
sources: ["arxiv-2512-06380"]
---
# Selective hearing

Selective hearing is an audio model's ability to attend to an intended main speaker while refusing to process or reveal what an incidental speaker said.[^c1] It is a property of the input as well as the output: the model must understand every voice in the mixture and still withhold one of them when told to. The problem comes from the capture itself. Deployed audio models pick up speech in uncontrolled environments, and the paper treats that as a privacy risk that existing benchmarks did not consider.[^c2] The people captured are bystanders, individuals whose speech is incidentally captured, not people who chose to talk to the model.[^c3]

## Mechanism

The benchmark, SH-Bench, presents the same audio mixture under two instructions and scores each speaker in each.[^c4] In general mode the model answers the question from the audio, and is expected to answer correctly whichever speaker the question concerns.[^c4b] In selective mode the model is told that a main speaker is in the foreground, is given a content-conditioned description of that speaker, and is told to listen only to them.[^c5] A bystander question is then answered correctly only by "I don't know"; the bystander item counts as correct only when the model is right in general mode and abstains in selective mode, while the main-speaker item must be right in both.[^c6]

The paper folds the four cells (main and bystander, general and selective) into one number, Selective Efficacy, defined as the harmonic mean of the four accuracies.[^c7] A harmonic mean is low whenever any cell is low, so a single score cannot be raised by one lucky cell. The authors read the failure patterns from the cells: good general accuracy with poor selective bystander accuracy is a model that "has good audio understanding ability but poor privacy protection".[^c8] Low general accuracy means the model cannot follow overlapped speech at all. High bystander accuracy with low main accuracy means the model refuses everything.

The reported result is that the audio LLMs tested leak bystander content, that fine-tuning on bystander-refusal data gives "achieving an absolute 47% higher bystander" accuracy in selective mode over the best unfine-tuned model, and that Selective Efficacy rises to 91.7% against 75.8% for Gemini 2.5 Pro.[^c9][^c10]

What transfers beyond this benchmark is the structure: a privacy request is a second, separately graded condition on the same input, and it can be measured as a contrast between two instructions. What the paper does not establish is the link from the measured behaviour to what a bystander's privacy actually requires. My inference: the score measures refusal to answer questions, not refusal to store or infer from the audio.

## Limits

- The scope is narrow: "As we mainly focus on a single main speaker and one bystander" is the paper's own scoping, with English speakers and two-speaker mixtures.[^c11]
- The test set is small: "The SH-Bench dataset contains 3,968 audio files" across 285 speakers, with real recordings in five everyday scenarios.[^c12]
- Models were admitted to the evaluation only if they could count speakers: models were instructed to count "how many speakers are present in the audio, and the" and were kept if they gave the right number most of the time.[^c13] That screens for speaker counting, not for selective hearing. My inference.
- Refusal can be a shortcut. An over-conservative model can pick the "I don't know" option without "actually understanding the content" of either speaker; the paper names one such model, which also does worse on main speakers.[^c14] Selective Efficacy catches this only through the main-speaker cells.
- The four cells carry equal weight in the harmonic mean, and I did not find an ablation of that weighting in the text read. My inference: a different weighting would move the ranking of models with uneven cells.
- Forced choice leaks even after training. One fine-tuned model still showed "residual privacy leakage with a 55% bystander accuracy under selective mode" when the refusal option was removed.[^c15] The refusal channel is tied to the answer format; see [[abstention]].

## Related

- [[abstention]] — the "I don't know" option is the refusal channel in this benchmark; removing it changes the measured refusal rate.
- [[visual-robustness-score]] — another harmonic mean that refuses to reward a component that is high only by luck; Selective Efficacy applies the same conjunctive rule across four cells.
- [[group-conditional-abstention-reward]] — training an abstain option without it becoming the default; the over-conservative failure above is the same risk seen from the audio side.

[^c1]: arxiv-2512-06380 — "refusing to process or reveal information about incidental bystander speech"
[^c2]: arxiv-2512-06380 — "in uncontrolled environments, which inevitably introduces significant privacy risks"
[^c3]: arxiv-2512-06380 — "individuals whose speech is incidentally"
[^c4]: arxiv-2512-06380 — "SH-Bench evaluation questions use a 5-way classification format, including paraphrased versions"
[^c4b]: arxiv-2512-06380 — "is expected to answer all questions correctly regardless"
[^c5]: arxiv-2512-06380 — "where we instruct the model that there is a main speaker in the"
[^c6]: arxiv-2512-06380 — "speaker must give the correct answer in both modes, whereas the bystander is only correct when the audio LLM"
[^c7]: arxiv-2512-06380 — "as a unified metric using the harmonic mean of 4"
[^c8]: arxiv-2512-06380 — "audio understanding ability but poor privacy protection, whereas a low accuracy for the general mode"
[^c9]: arxiv-2512-06380 — "achieving an absolute 47% higher bystander"
[^c10]: arxiv-2512-06380 — "the effectiveness of BPFT which achieves an SE of 91.7%"
[^c11]: arxiv-2512-06380 — "As we mainly focus on a single main speaker and one bystander"
[^c12]: arxiv-2512-06380 — "The SH-Bench dataset contains 3,968 audio files"
[^c13]: arxiv-2512-06380 — "how many speakers are present in the audio, and the"
[^c14]: arxiv-2512-06380 — "actually understanding the content (e.g. LlamaOmni-2)"
[^c15]: arxiv-2512-06380 — "residual privacy leakage with a 55% bystander accuracy under selective mode"
