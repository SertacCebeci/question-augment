---
description: "A metric that takes the best score over all gold answers for one prediction lets a single correct answer earn full credit on a multi-answer question; set-match and answer-level F1 do not."
aliases: ["max-over-references scoring", "best-match over gold answers", "SQuAD-style max scoring", "any-reference credit"]
sources: ["doi-10-48550-arxiv-2311-09821"]
---
# Max-over-references scoring

When a question has several correct answers, the usual string metrics compare a prediction with every gold answer and keep the best match. The score is the closest single hit. SQuAD's exact match and token F1 work this way, and the temporal QA benchmarks that followed SQuAD adopted them without change. The Complex-TR authors state the consequence: "the metrics in SQuAD are computed by using the maximum scores with all references, which significantly overestimate the performance for multi-answer questions."[^m1]

The mechanism is simple. On this rule, a prediction that matches one of several gold answers scores the same as one that matches all of them. The measure does not register how many of the gold answers were found, and it does not charge for extra answers that are not gold. My inference from the definition is that the score therefore rises with the number of gold answers a question has, whether or not the model handles the full set. The paper does not test that inference directly.

The paper's measurement is the clearest evidence. On the same model outputs, token F1 for multi-answer questions came out higher than for single-answer questions: "Tok. F1 scores for multi-answer questions are even higher than those of single-answer questions."[^m2] A harder class of question scored better under the metric, which is the sign the authors read as an overstatement. They summarise it as "EM and Tok. F1 can significantly overestimate the performance of multi-answer questions."[^m3]

The repair replaces the best-match rule with two stricter measures. Set accuracy (Set Acc.) counts a prediction as correct only when it is "identical to the ground truth set": "This metric will only return correct if the prediction set is identical to the ground truth set."[^m4] Answer-level F1 (Ans. F1) counts a true positive only on an exact match in the answer set, and it does not let extra answers pass: "if the prediction contains extra answers, it will also be penalized."[^m5] The two measures do different work. Set accuracy asks for the whole set. Ans. F1 gives partial credit for the set but charges for each element that is not gold. Both give lower numbers on multi-answer questions than EM or token F1 do, and the authors recommend them for temporal QA benchmarks: "it is better for temporal QA benchmarks to adopt Set Acc. and Ans. F1 for evaluation."[^m6]

What the stricter measure shows that the looser one hides is a difference in kind. In the paper, GPT-4 finds valid answers under time constraints, and its answer F1 is high, yet "it cannot find all correct answers when multiple answers are presented."[^m7] A best-match score reads that model as nearly correct. The set-level score reads it as incomplete. The two readings differ, and only the set-level one matches what the question asked for.

## Limits

- All the evidence is from temporal QA: Complex-TR and ReasonQA. Whether the size of the overestimate carries over to other multi-answer tasks was not tested in the text I read.
- The paper compares metrics on the same outputs. It shows that the stricter measures give lower numbers on multi-answer questions. It does not show that they rank systems more correctly, or that they match human judgments of answer quality.
- Ans. F1 penalises extra answers but weights every gold answer alike. It does not say which answers matter more. That is the same blind spot named in [[recall-only-partial-credit]], viewed from the other side.
- The metric definitions are taken from earlier work (Zhong et al. for set accuracy, Amouyal et al. for answer F1). I read the paper's descriptions of them, not the originals.
- The sections I read do not spell out how a predicted answer is matched to a gold answer (string identity or normalised form). The strictness of the set-level measure depends on that choice, and I did not verify it.

## Related

- [[recall-only-partial-credit]] — the mirror failure: a recall-type overlap score ignores extra answers, while the best-match rule ignores how many gold answers were found
- [[atomic-fact-f1-evaluation]] — precision and recall over matched facts, which applies the same charge for over-claiming that Ans. F1 applies to extra answers
- [[alias-tolerant-answer-matching]] — exact-string scoring also fails on equivalent names, a separate way the same metric family misreads a correct answer

[^m1]: doi-10-48550-arxiv-2311-09821 — "the metrics in SQuAD are computed by using the maximum scores with all references, which significantly overestimate the performance for multi-answer questions"
[^m2]: doi-10-48550-arxiv-2311-09821 — "Tok. F1 scores for multi-answer questions are even higher than those of single-answer questions"
[^m3]: doi-10-48550-arxiv-2311-09821 — "EM and Tok. F1 can significantly overestimate the performance of multi-answer questions"
[^m4]: doi-10-48550-arxiv-2311-09821 — "This metric will only return correct if the prediction set is identical to the ground truth set"
[^m5]: doi-10-48550-arxiv-2311-09821 — "if the prediction contains extra answers, it will also be penalized"
[^m6]: doi-10-48550-arxiv-2311-09821 — "it is better for temporal QA benchmarks to adopt Set Acc. and Ans. F1 for evaluation"
[^m7]: doi-10-48550-arxiv-2311-09821 — "it cannot find all correct answers when multiple answers are presented"
