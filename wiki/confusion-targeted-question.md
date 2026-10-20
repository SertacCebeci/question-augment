---
description: "A question is aimed at the rivals a recognizer most often confuses, counted from its own misclassifications and refreshed during training, instead of at the item alone."
aliases: ["confusion-targeted prompting", "similar-class set prompting", "error-profile-targeted question", "context-aware prompter"]
sources: ["arxiv-2511-22433"]
---
# Confusion-targeted question

A question about one item can be asked alone, or it can be asked against the alternatives the answerer is most likely to mix it with. The second form needs a list of those alternatives, and the source of the list decides what the question can see. SkeletonAgent (arXiv:2511.22433) takes the list from the answerer's own errors. Its Questioner keeps a running count of which class a recognizer confuses with which. The paper's reason is that the single-turn prompt is answered "in isolation from the recognition model and receives no performance feedback."[^c1] The count is an online confusion matrix, used "to identify the current challenging actions for each class".[^c2] The top entries of each row become the rivals for that class.[^c3]

The rivals are then written into the prompt. The question changes from "what is this action?" to "what separates this action from the ones the recognizer keeps confusing with it?" The paper's example is the hand-waving class. A static description gives appearance and a generic motion list. The targeted one names a rhythmic oscillation of an open hand, "contrasting with purposeful directional or grasping movements in similar actions."[^c4] The same prompt is then used to build the distinction that is aligned with the skeleton, so the answer is shaped by the rivals, not by the class name alone.

The mechanism is close to [[hypothesis-conditioned-query-rewriting]], which also asks a question against rivals. The difference is where the rivals come from. There they are the options printed with the question. Here they are the classes the learner has measurably been mixing up, so the rival set can contain alternatives that no one wrote down, and it changes as training goes on. The paper gives the reason for measuring rather than listing: the confusion profile is treated as the signal that matters to the recognizer. It also concedes that this signal "may differ from the predictions of human visual mechanisms."[^c5] A rival list built this way describes the recognizer's errors, not the items' confusability for people.

What the mechanism buys is measured only inside the paper's ablation. On NTU-60 X-Sub with the joint modality, the baseline is 91.2 and the full model is 92.8. The paper reads the contextual stage together with the alignment stage as adding "improvements by 0.4% and 0.7%, respectively", so the confusion-fed stage carries about 0.4 points.[^c6] "By integrating all components, we surpass baseline performance by 1.6%."[^c7]

## Limits

- The ablation is a single split and modality, and the text read gives no variance across seeds. The components are added "gradually" in one table, so the 0.4 is an increment on top of the other stages, not the effect of the confusion feedback alone.[^c8]
- The number of rivals per class, the refresh interval, and the warm-up before the first refresh are design choices. The periodic refresh is motivated by efficiency and by "avoid[ing] insufficient learning in the early stages." No sensitivity result over these choices appears in the passages read.
- The feedback comes from a model in a training loop, and the answerer is an LLM that is not itself shown the rival list's accuracy. Whether a live human or a model answering a student's question would benefit from the same rival list is not tested.
- The second agent, the Selector, parses the LLM's answer into joint-level constraints for the recognizer. That is a different move, from answer to structure, and it is not what this note describes. Its contribution is also reported only inside the same cumulative ablation.

## Related

- [[hypothesis-conditioned-query-rewriting]] — the rivals there are the question's own printed options; here they are taken from the answerer's measured errors, and they can go beyond the options.
- [[contrastive-hypothesis-retrieval]] — builds from a named rival and subtracts it in score space; the rival is given in advance, not measured from errors.
- [[divergence-rewarded-probe-generation]] — scores a question by where its answerers split; here the split is used to choose which rivals a question names, not to score the question.

[^c1]: arxiv-2511-22433 — "receives no performance feedback"
[^c2]: arxiv-2511-22433 — "to identify the current challenging actions for each class"
[^c3]: arxiv-2511-22433 — "the Questioner identifies the most frequently confused classes and supplies them to the LLM as context for more targeted guidance"
[^c4]: arxiv-2511-22433 — "contrasting with purposeful directional or grasping movements in similar actions"
[^c5]: arxiv-2511-22433 — "feedback, which may differ from the predictions of human visual mechanisms."
[^c6]: arxiv-2511-22433 — "achieving improvements by 0.4% and 0.7%, respectively"
[^c7]: arxiv-2511-22433 — "By integrating all components, we surpass baseline performance by 1.6%"
[^c8]: arxiv-2511-22433 — "we gradually add each component"
