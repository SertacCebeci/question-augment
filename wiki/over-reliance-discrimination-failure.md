---
description: "Students given ChatGPT solutions, 6/11 wrong, adopted ~61% of wrong ones; d' near zero shows they could not tell wrong from right, and confidence rose with over-reliance."
aliases: ["over-reliance on AI answers", "signal detection of false AI answers", "adoption of incorrect AI solutions"]
sources: ["openalex-org-w7162267323", "doi-10-48550-arxiv-2505-01106"]
---
# Over-reliance as failure to discriminate

Over-reliance on an AI answer is defined as accepting it without hesitation, which leads to errors in information processing and related tasks.[^c1] The study separates two things that a raw adoption rate mixes: how often a wrong answer is taken, and whether the asker can tell wrong from right at all.

**Design.** Estonian secondary students did critical-thinking tasks. The control group (n = 341) solved them alone. The test group (n = 325) received ChatGPT-generated solutions to use if they judged them suitable, and near half of them (6/11) were incorrect.[^c2] Over-reliance was the share of wrong solutions adopted. Under-reliance, the opposite extreme, was the share of correct solutions ignored. Both were then analysed with Signal Detection Theory, where the wrong answer is the "signal" and d' measures how well it is detected.[^c3]

**Findings.** The test group out-performed the control group, so access to AI helped on average. Yet over-reliance was widespread: three quarters of students used at least half of the incorrect answers, and the average adoption of wrong solutions was 60.6%.[^c4] The average d' was essentially zero (about 3.3 x 10^-16), meaning students were not discriminating wrong from correct outputs. Their adoption was close to indiscriminate acceptance rather than selective use.[^c5] The reported over-reliance pattern is therefore not a threshold set too loose over a working signal. In this sample the signal itself was absent.

**Confidence.** A medium-sized significant correlation (rS = 0.408, p < 0.001) linked over-reliance to confidence ratings.[^c6] Students who accepted more wrong answers were more confident, so confidence did not flag the errors. Per-task mean confidence was not related to d' (rS = 0.037, p = 0.504), so confidence also did not track the ability to discriminate.[^c7]

**Why it matters for asking and answering.** Receiving an answer is not the same as using it well. An answerer that is right about half the time, without any marker of which half, produces adoption of its errors at about the rate of its outputs. A confidence display that the receiver reads as assurance may add to this. This is my inference from the correlations above, not a causal result.

**Replication with ChatGPT in middle school.** French students aged 14-15 (N=63) rated every ChatGPT answer in six science tasks against expert-coded quality. Their d' for answer quality was near zero (M=0.07, SD=1.2, indistinguishable from chance), and only 16 students reached evaluation accuracy above 70%.[^c8] The same students also failed to separate efficient from inefficient suggested prompts (d'=0.19) and rarely repaired a poor answer: only 14 students asked any follow-up question.[^c9] Self-reported prior knowledge did not protect them; it was negatively associated with answer-evaluation sensitivity, which the authors read as high confidence lowering epistemic vigilance.[^c10] Task success (mean 0.51) was predicted by high-level answers received, sensitivity to answer quality, and follow-up after low-level answers.[^c11] So the missing signal appears in a younger sample and with a free-form asker, and the failure extends past acceptance to non-regulation (premature stopping).

## Limits

- Correlational: confidence and over-reliance rise together, direction unknown.
- One country, one age group, one tasks set, one model; the study itself notes that adoption rates differ from earlier work.
- Subgroups with different reliance styles may exist; a single d' per person can hide them.
- Wrong solutions were presented with no uncertainty cues; whether cues, warnings or verification prompts change d' was not tested here.
- The text is a student thesis-style report; its d' near zero is an aggregate and may partly reflect task design (proportion wrong, forced choice of use).

## Related

- [[warning-as-debiasing]] — a possible intervention on adoption, not tested in this study
- [[sycophantic-capitulation]] — another route by which wrong content gets accepted
- [[hard-easy-effect]] — confidence decoupled from accuracy in human judgment
- [[human-model-uncertainty-dissociation]] — human confidence and model uncertainty diverge

[^c1]: openalex-org-w7162267323 — "Liigtuginemist tehisaru tehnoloogiate kontekstis defineeritakse tehisaru vastuste"
[^c2]: openalex-org-w7162267323 — "While the control group (n = 341) solved tasks on their own, the test group (n ="
[^c3]: openalex-org-w7162267323 — "Analysis in light of Signal Detection Theory (SDT) indicates"
[^c4]: openalex-org-w7162267323 — "widespread: ¾ of students used at least half of the incorrect answers, using on average"
[^c5]: openalex-org-w7162267323 — "ones, as shown by a near-zero average d’ index."
[^c6]: openalex-org-w7162267323 — "Additionally, a significant correlation (rS"
[^c7]: openalex-org-w7162267323 — "vahel ei esinenud olulist seost (rS = 0,037; p = 0,504)."
[^c8]: doi-10-48550-arxiv-2505-01106 — "Only 16 students achieved an evaluation accuracy exceeding 70%."
[^c9]: doi-10-48550-arxiv-2505-01106 — "only 14 students asked follow-up questions (totaling"
[^c10]: doi-10-48550-arxiv-2505-01106 — "rather, high confidence appeared to"
[^c11]: doi-10-48550-arxiv-2505-01106 — "showed that the success rate across tasks was predicted by three variables: the frequency of satisfying"
