---
description: "An LLM turns a text query into first-order logic once, then a symbolic evaluator scores each image's detected objects against it, so retrieval is checkable clause by clause."
aliases: ["text-to-logic retrieval", "logic-based text-to-image retrieval", "neurosymbolic image retrieval", "RUNE"]
sources: ["arxiv-2512-14102"]
---
# Neurosymbolic text-to-logic retrieval

A text-to-image retriever is usually one learned function: the query and the image are each projected into a shared embedding space and scored by similarity. This work splits the job differently. A language model is used for one step only. It rewrites the query as a first-order logic (FOL) expression over object categories and spatial relations, and a symbolic evaluator then scores each image. In the authors' words, the foundation models are used "only to generate FOL expressions, delegating reasoning to a neurosymbolic inference module."[^n1]

The image side comes from an oriented-box detector (YOLO11, trained on DOTA).[^n2] Each detection carries a category and a confidence. Every FOL predicate becomes a soft truth value in [0, 1]: a unary predicate such as ship(A) reads the detector's category confidence, and a binary spatial predicate such as left_of(A, B) is computed from the geometry of the two boxes. The truth values are then combined in a semiring. The reasoning process "is formulated in terms of semiring probabilistic logic," and conjunction multiplies: it "is modeled as the multiplication of probabilities."[^n3][^n4] Disjunction takes the maximum: it "is modeled as the maximum operation."[^n5] Over candidate object tuples the authors take the best one: "The max operator is then applied to select the highest probability among all pairs."[^n6] My reading: the score for an image is the best-supported assignment of query entities to detections, with the predicates treated as independent evidence.

The FOL itself comes from a prompt the authors call a new in-context learning technique: "we introduce a novel in-context learning technique named spatial logic in-context learning for remote sensing."[^n7] The prompt gives the model a role (a logician for remote sensing), the allowed object and relation vocabulary, and five worked examples, and asks for JSON output. The model is sampled ten times, and one expression is kept by embedding similarity to the query, with ties broken by the model's confidence and then by the fewest entities and predicates. The stated aim of that last rule is to "limit the possibility of introducing False Positive entities and predicates in the FOL expression."[^n8]

What this changes for asking and answering is that the query becomes a list of claims that can be inspected one by one. The system also reports which objects and relations produced the score: "RUNE indicates the involved objects and their relations on which the predicted probability" was based.[^n9] A joint embedding, by contrast, encodes the query's semantics implicitly, "of the query implicitly, limiting both representational power and interpretability."[^n10]

The reported evidence is on a repurposed DOTA benchmark, where the method is compared with three general-purpose LVLMs and three remote-sensing LVLMs across five query-complexity levels. The abstract's headline is that "RUNE outperforms joint-embedding models in complex RS" retrieval.[^n11] Robustness is measured by two metrics. RRQC is built from the change in P@k or R@k between complexity levels: "we calculate how increasing the complexity of the query impacts P@k and R@k."[^n12] My reading of its equation is that it averages the difference between the metric at a lower and a higher level, over level pairs a fixed distance apart. RRIU is defined over image-uncertainty bins: "the RRIU between two bins is defined as the difference in their average hit ratios."[^n13]

## Limits

- The evaluation rests on one repurposed dataset. "The repurposed DOTA dataset consists exclusively of cropped images."[^n14] Queries cannot use compass directions, because "queries cannot be formulated using cardinal directions."[^n15] The method "has not been tested on oblique images."[^n16]
- Translation errors reach the answer. The authors concede that the text-to-logic step "is not flawless," and that an error "can propagate through the neurosymbolic reasoning pipeline, potentially leading to incorrect results."[^n17] I did not check the translation accuracy numbers, which sit in results I did not read.
- The pipeline is only as good as the detector: "the overall performance of the pipeline is highly dependent on the accuracy of the object detector."[^n18] The same dependence costs it on image uncertainty: "RUNE exhibited lower RRIU than four baselines due to its dependence on object detection."[^n19]
- The speed advantage holds only when predicates are precomputed: "in case in which the predicates are precomputed, execution time is reduced at the level of" neural approaches.[^n20] The authors add that precomputation "may not always be possible as there can be cases in which the entirety of the analysis must be executed in real time."[^n21] The factorization that addresses cost is a separate note, [[clause-factorized-inference]].
- The semiring is an imported formalism. Its product rule is justified in the text by "independent pieces of information, where the overall confidence is the product of individual confidence."[^n22] Object labels and the spatial relations between them are computed from the same boxes, so they are not independent. The text does not test what that dependence costs. My inference, not the paper's claim.
- The metric definitions are the authors' own. I have not compared RRQC or RRIU with other robustness measures.

## Related

- [[clause-factorized-inference]] — how the logic is evaluated without enumerating every entity-to-detection assignment
- [[recall-only-partial-credit]] — the same precision-blind asymmetry, in multi-answer scoring
- [[reinforcement-query-refiner]] — also rewrites a query into structured logic, but for a frozen LLM to read, not for a symbolic evaluator to execute

[^n1]: arxiv-2512-14102 — "only to generate FOL expressions, delegating reasoning to a neurosymbolic inference module"
[^n2]: arxiv-2512-14102 — "To perform OBB detection, we rely on YOLO11"
[^n3]: arxiv-2512-14102 — "The reasoning process is formulated in terms of semiring probabilistic logic"
[^n4]: arxiv-2512-14102 — "is modeled as the multiplication of probabilities"
[^n5]: arxiv-2512-14102 — "is modeled as the maximum operation"
[^n6]: arxiv-2512-14102 — "The max operator is then applied to select the highest probability among all pairs"
[^n7]: arxiv-2512-14102 — "we introduce a novel in-context learning technique named spatial logic"
[^n8]: arxiv-2512-14102 — "limit the possibility of introducing False Positive entities and predicates in the FOL expression"
[^n9]: arxiv-2512-14102 — "RUNE indicates the involved objects and their relations on which the predicted probability"
[^n10]: arxiv-2512-14102 — "of the query implicitly, limiting both representational power and interpretability"
[^n11]: arxiv-2512-14102 — "RUNE outperforms joint-embedding models in complex RS"
[^n12]: arxiv-2512-14102 — "we calculate how increasing the complexity of the query impacts P@k and R@k"
[^n13]: arxiv-2512-14102 — "the RRIU between two bins is defined as the difference in their average hit ratios"
[^n14]: arxiv-2512-14102 — "The repurposed DOTA dataset consists exclusively of cropped images"
[^n15]: arxiv-2512-14102 — "queries cannot be formulated using cardinal directions"
[^n16]: arxiv-2512-14102 — "has not been tested on oblique images"
[^n17]: arxiv-2512-14102 — "step can propagate through the neurosymbolic reasoning pipeline, potentially leading to incorrect results"
[^n18]: arxiv-2512-14102 — "highly dependent on the accuracy of the object detector"
[^n19]: arxiv-2512-14102 — "RUNE exhibited lower RRIU than four baselines due to its dependence on object detection"
[^n20]: arxiv-2512-14102 — "in case in which the predicates are precomputed, execution time is reduced at the level of"
[^n21]: arxiv-2512-14102 — "always be possible as there can be cases in which the entirety of the analysis must be executed in real time"
[^n22]: arxiv-2512-14102 — "independent pieces of information, where the overall confidence is the product of individual confidence"
