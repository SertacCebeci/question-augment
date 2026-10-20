---
description: "A shared encoder with one output head per annotator, each trained only on that annotator's labels, keeps individual perspectives until prediction and can beat majority-label training."
aliases: ["multi-annotator model", "annotator heads", "multi-task annotator modelling", "per-annotator classifier heads", "disaggregated annotator training"]
sources: ["doi-10-48550-arxiv-2110-05719"]
---
# Per-annotator prediction heads

Training on majority labels reduces the several labels an item received to one target, so the record of who said what is gone before the model sees anything. A per-annotator head design keeps that record. A shared pretrained encoder produces one representation of each input, and a separate output layer is attached for each annotator. Each head is fitted only to the items its annotator labelled, while the shared layers take gradient from every labelled item, whichever annotator provided it.[^c1]

The design has a variant for each way of attaching the heads. In the ensemble variant, one whole classifier is trained per annotator, and nothing is shared. In the multi-label variant, one sigmoid output per annotator sits on a shared layer. In the multi-task variant, each annotator has its own fully connected layer on the shared representation. At test time the heads are combined by majority vote, so the model still emits a majority-style label, and the head outputs remain available as a set of predicted annotations.[^c2]

The mechanism that the paper credits is the shared layer. Each head "benefits from the updates to the shared layers" driven by instances it never labelled.[^c3] The paper reads its result on this basis: fitting each annotator head and then taking the vote "performs better than taking the majority vote first and then training on that noisier label."[^c4]

What was measured: on the Gab Hate Corpus (27,665 posts, 18 annotators), the multi-task variant scored F1 59.49 against a 57.32 majority-label baseline, and the paper says the per-annotator layer is why it "posted a significantly higher F-score."[^c5] The ensemble scored 53.54 and the multi-label variant 56.94, both at or below the baseline. The paper's explanation for the ensemble is that "each base model in the ensemble is trained using" only its own annotator's examples, which are few.[^c6] Against raw annotations the multi-task model reached 63.20, which "achieved the highest F1 -score" of the three variants.[^c7] Training cost stayed close to the baseline, 22.3 against 20.5 minutes on 80 percent of the corpus, and the paper notes "Impressively, multi-label and multi-task" models add little time.[^c8]

## Limits

- The gain is not uniform. On GoEmotions (82 annotators, six binary emotion tasks) the multi-task model "underperformed the baseline for the other four" emotions on the full data.[^c9] Restricting to 53 annotators with more than 1000 labels reversed the result on four of six, and the paper says the multi-task model "fares significantly better when there are enough instances" per head.[^c17] Annotator volume decides much of the outcome.
- Heads need enough labels each. Many annotators contributed few labels, and on the skewed emotion labels some heads had no positive instances; the paper says this "makes the corresponding learning tasks in the multi-task setting hard or even impossible on this dataset."[^c10]
- Cost grows with the annotator pool. The paper notes that "separate annotator heads will be computationally expensive" at the scale of thousands of annotators, and proposes clustering annotators, "clustering annotators based on their agreements and aggregating annotator labels into cluster labels could address this issue."[^c11] Whether that works is a separate result, see [[agreement-based-annotator-clustering]].
- The data must carry annotator identity. The paper observes that "datasets contain only per-instance majority labels" for most multiply annotated corpora.[^c12] The method is not applicable to those.
- The encoder is one model. "While our experiments are all performed with BERT-base," the authors claim the method is not tied to BERT, which was not tested.[^c13]
- The stability claim is a hypothesis. The paper says that per-annotator modelling "could lead to more stable prediction results," and adds that "this hypothesis requires further investigation."[^c14]
- The two F1 columns answer different questions. The majority-label and individual-label scores are on different targets, and the paper itself warns they are "not directly comparable."[^c15]
- No correctness check on the labels themselves. The method reproduces annotator behaviour, including bias; the paper says it can "adjust predictions to be conditioned on different value systems" but does not test that claim.[^c16]

## Related

- [[annotator-distribution-target]] — supervises on the annotator label distribution; the per-annotator heads supervise on each annotator's own label instead
- [[agreement-based-annotator-clustering]] — groups annotators to avoid one model per person; the scale fix this design's authors suggest
- [[dawid-skene-annotator-model]] — infers a single label while estimating each annotator's reliability; the heads here keep labels apart instead of resolving them
- [[annotation-disagreement-sources]] — why annotators split; per-annotator heads keep the split that a majority label erases
- annotator-head-spread-uncertainty — reads the spread across these heads as an uncertainty estimate

[^c1]: doi-10-48550-arxiv-2110-05719 — "treats predicting each annotators’ judgements as separate"
[^c2]: doi-10-48550-arxiv-2110-05719 — "explicitly fine-tuned for each annotator"
[^c3]: doi-10-48550-arxiv-2110-05719 — "annotator head benefits from the updates to the"
[^c4]: doi-10-48550-arxiv-2110-05719 — "performs better than taking the majority vote first"
[^c5]: doi-10-48550-arxiv-2110-05719 — "fine-tuned for each annotator, posted a significantly higher F-score"
[^c6]: doi-10-48550-arxiv-2110-05719 — "each base model in the ensemble is trained using"
[^c7]: doi-10-48550-arxiv-2110-05719 — "achieved the highest F1 -score of 63.20"
[^c8]: doi-10-48550-arxiv-2110-05719 — "Impressively, multi-label and multi-task"
[^c9]: doi-10-48550-arxiv-2110-05719 — "it underperformed the baseline for the other four"
[^c10]: doi-10-48550-arxiv-2110-05719 — "tasks in the multi-task setting hard or even impossible on this dataset"
[^c11]: doi-10-48550-arxiv-2110-05719 — "clustering annotators based on their agreements and aggregating annotator labels into cluster labels could address this issue"
[^c12]: doi-10-48550-arxiv-2110-05719 — "datasets contain only per-instance majority labels"
[^c13]: doi-10-48550-arxiv-2110-05719 — "While our experiments are all performed with BERT-base"
[^c14]: doi-10-48550-arxiv-2110-05719 — "this hypothesis requires further investigation"
[^c15]: doi-10-48550-arxiv-2110-05719 — "note that these are different tasks, and"
[^c16]: doi-10-48550-arxiv-2110-05719 — "adjust predictions to be conditioned on different value systems"
[^c17]: doi-10-48550-arxiv-2110-05719 — "fares significantly better when there are enough instances"
