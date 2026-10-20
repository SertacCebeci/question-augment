---
description: "The first procedure that actually computes an implicit question from text — **Ko, Wu, Dalton, Srinivas, Durrett & Li (Findings of ACL 2023)** define the task. Given a document $D = (s_1,\\dots,s_n)$,"
aliases: ["QUD dependency parsing", "QUD parser"]
sources: ["ko-2022", "ko-2023"]
---
# QUD parsing

> The first procedure that actually computes an implicit question from text —
> and it computes each question *from the sentence that answers it*, never from
> a question that was sent.

## Definition / Mechanism

**Ko, Wu, Dalton, Srinivas, Durrett & Li (Findings of ACL 2023)** define the[^s1][^s2]
task. Given a document $D = (s_1,\dots,s_n)$, return
$T = ((a_1,q_1),\dots,(a_n,q_n))$: for every sentence $s_i$, an **anchor**
$a_i \in \{1,\dots,i-1\}$ — the earlier sentence the question arose from — and
a free-form question $q_i$ that $s_i$ answers. The first sentence is the root
($a_1 = 0$, $q_1 = \emptyset$). The model factorises as

$$P(T \mid D) = \prod_i P_a(a_i \mid D, i)\, P_q(q_i \mid D, i, a_i)$$

— **anchor prediction** (a Longformer QA model predicting the span of the
anchor sentence over the whole article) then **question generation** (GPT-2
fine-tuned on prior context + marked anchor + answer sentence, ten samples
reranked by a BERT classifier). Named entities in the answer sentence are
replaced by their entity type before generation, because the generator
otherwise writes questions that "foresee" details not inferable from prior
context.

Training data is **DCQA** (Ko, Dalton, Simmons, Fisher, Durrett & Li, EMNLP
2022): 22,430 crowdsourced question–answer pairs over 600+ English news
articles, collected by having annotators read sentence by sentence and, for
each sentence, write the question it answers and mark the anchor.

**What was measured.** Three trained crowdworkers judged 380 generated
questions from 20 test articles on two graded scales: is the question
reasonable given the article up to and including the anchor (Q1), and does the
target sentence answer it (Q2). Full model: 71.5% "yes" on Q1; among
good-quality questions, 78.8% "yes" on Q2. Without the reranker, 66.7 / 71.8;
without entity masking, 54.8 / 76.7. On out-of-domain simplified text
(Newsela), 60.2 / 75.2.

Two structural facts carry as much as the numbers. **(a)** Every question is
generated conditioned on the sentence that answers it — the authors call this
the *reactive* model of processing. **(b)** Question–question relations are
left to future work: the output is a dependency over sentences with no
entailment between questions, i.e. not Roberts's stack. Attachment agreement
with RST trees on the overlapping documents is 0.30.

A side result: showing two annotators the QUD raised Krippendorff's $\alpha$
on RST relation labelling from 0.158 to 0.216 (7 documents) — naming the
implicit question reduced disagreement about what a sentence is doing.

## Known as

| Name | Field | Relation |
|---|---|---|
| QUD dependency parsing, QUD parser | computational linguistics | exact — the authors' terms for this task and system |
| QUD dependency structure | computational linguistics | *not* this concept — the output object, which also exists as human annotation in DCQA without any parser |
| DCQA | NLP resources | *not* this concept — the crowdsourced dataset the parser is trained and evaluated on |
| QUD tree | formal pragmatics / NLP | ambiguous across the two fields — see [[qud-tree]] |
| discourse parsing (RST, PDTB) | NLP | close — *not* this concept: edges carry labels from a fixed relation taxonomy rather than generated text, and the two structures agree on only 0.30 of attachments |

## Why it matters

1. **Stall 9's missing computation exists, in one direction.**
   [[question-under-discussion]] states that a reader must have inferred a
   question and never says how; this is a running procedure that outputs one,
   with a measured plausibility rate.
2. **The direction is backwards for an answerer.** $P_q$ is conditioned on
   $a_i$ and $s_i$; the question is recovered from material that already
   answers it. Nothing here takes a received question as input and returns the
   question meant. What it can do is name the question a *produced* text
   answers — the inference this wiki draws from that is
   [[recovered-question-check]].
3. **Free-form beats taxonomy for lay annotation.** The reason to generate a
   question instead of a relation label is that relation taxonomies need
   trained linguists; questions are crowdsourcable, which is why the training
   set is two orders of magnitude larger than QUD-annotated corpora built by
   analysts ([[qud-licensing-constraints]]).
4. **The ceiling is public.** 28.5% of generated questions are judged not
   plausible at their anchor (Q1 = 71.5%), and among those judged good a
   further 21.2% are not answered by the sentence they were generated for
   (Q2 = 78.8%). A design that assumes a recovered question is correct is
   assuming something the parser's own evaluation contradicts on more than a
   quarter of its edges.

## Transfer

| | |
|---|---|
| **Home field** | offline document-level discourse analysis of written English news monologue, evaluated by crowdworkers who see the whole article |
| **Here** | an answerer that must state which question a stretch of text answers, before or after committing to a reply |
| **What survives** | the task shape (anchor + free-form question per unit); the factorisation into anchor selection and question generation; the two-part evaluation protocol — is the question reasonable at its anchor, is it answered by the target |
| **What does not** | use at comprehension time on a received question: the conditioning on the answer sentence is not removable without retraining, and no paper reports the reverse task; the stack and its entailment relations; the domain — quality drops ~11 points on simplified text of the same articles |

## Limits

- 71.5% is human approval of **plausibility**, not agreement with a gold
  question. The authors chose human evaluation because automatic open-ended
  generation metrics correlate poorly with judgement, so there is no
  reproducible score for this system.
- Three crowdworkers, 380 questions, 20 English news articles; both modules are
  2019-era models (Longformer, GPT-2, BERT). Nothing here shows the ceiling is
  a property of the task rather than of these models.
- The entity-masking patch is load-bearing on one of the two scales only:
  without it Q1 falls from 71.5% to 54.8% — roughly a quarter of the otherwise
  plausible questions foresee material not inferable from prior context —
  while Q2 is close to the full model (76.7% against 78.8%). Every number
  reported above is post-patch.
- Point 2 — that the answer-anchored conditioning makes the parser unusable as
  a comprehension-time detector — is this wiki's reading of the model's
  factorisation; Ko et al. never consider an answerer's situation.
- DCQA annotators wrote each question after seeing the sentence that answers
  it, so the dataset carries the same directionality; a parser trained on it
  cannot be assumed to generalise to prospective questions.

## Related

[[question-under-discussion]] · [[qud-licensing-constraints]] · [[qud-tree]] · [[recovered-question-check]] · [[clarification-request]] · [[levels-of-information-need]]

[^s1]: ko-2022
[^s2]: ko-2023
