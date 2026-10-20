---
description: "A frozen text-only reasoner asks a small vision model for the visual details it lacks, over several turns; the reasoner's requests decide which visual facts cross into its text channel."
aliases: ["perceiver-reasoner collaboration", "multi-agent modality extension", "eyes-and-brain dialogue"]
sources: ["arxiv-2511-19417"]
---
# Reasoner-led perception dialogue

A text-only reasoner can reach an image without being retrained on it. A small vision-language model acts as the reasoner's perceiver: it reads the picture and answers in text. The reasoner does the final reasoning and drives the exchange. In the BeMyEyes setup "the reasoner agent typically initiates the dialogue by requesting relevant details about the question, including both visual and textual components."[^c1] The perceiver's job is stated as "extracts and describes relevant visual information."[^c2] The two then alternate turns until a cap is reached, and the perceiver writes the final answer from the exchange.[^c3]

The mechanism is narrow on purpose. The perceiver's replies "constitute the sole communication channel through which the reasoner can infer visual context."[^c4] Nothing else carries the picture to the reasoner, so whatever the reasoner never asks for, and whatever the perceiver does not write down, is absent from the reasoning. The reasoner is "instructed to request clarifications or additional descriptions from the perceiver agent when necessary, and to refine its reasoning based on the updated information."[^c5] The reason given is that the perceiver "may omit or overlook certain visual details."[^c6] A second round of asking is the repair for a first description that missed something.

Read in the wiki's terms, the reasoner is the asker and the perceiver is the source. The asker opens slots (which visual fact is needed), and the source fills them in text. This differs from a clarification in which the answerer asks back. Here the asker asks a source that holds facts it does not have.

What was measured. With a frozen reasoner and a Qwen2.5-VL-7B perceiver, the paper reports a text-only DeepSeek-R1 "even outperforming GPT-4o by 0.5%, 7.1%, and 12.1% on MMMU Pro, MathVista, and MathVision, respectively."[^c7] The same dialogue lifts GPT-4 toward the fully multimodal model: "GPT-4 recovers much of the performance of the fully multimodal GPT-4o."[^c8]

The number of rounds matters in the reported ablation. The authors restrict the perceiver to one reply and compare; the table caption says "performance drops are observed when removing supervised fine-tuning (SFT) or restricting the framework to single-turn conversations."[^c9] On the same ablation they conclude "that iterative communication plays an important role in improving the overall reasoning process."[^c10] So the later rounds carry information the first description did not, which is a different claim from "more turns help".

Training data. The paper builds the perceiver's conversations by role-playing both agents with a teacher model. It samples up to a set number of conversations per question and keeps "the one that leads to the correct answer,"[^c11] where the correct answer is "the answer from the singleVLM setting as the ground-truth label."[^c12] Questions "that can be answered correctly without images, since these are trivial for multimodal reasoning" are dropped.[^c13] Questions with no conversation that reaches the label are also dropped, "typically because the visual information is too complex or abstract to be effectively conveyed through textbased communication."[^c14] That last clause marks the concept's boundary in the data: what cannot be put into text under this dialogue is removed from training, not solved.

## Limits

- Vision is the only modality tested: "our experiments focus exclusively on vision as the target modality."[^c15]
- No fully multimodal reasoner of the same scale was run as an upper bound: "developing such large-scale models remains beyond our current scope."[^c16] The gap to the image-reading reasoner is therefore not measured.
- Errors use the same channel. Some items that a multimodal reasoner answers alone are lost in joint reasoning; the reasoner "is misled when reasoning jointly with the perceiver, often due to perception or communication errors."[^c17]
- The paper gives no measure of how much visual information a reply loses. Its discarded items show that some visual content does not survive this dialogue at all.
- The rounds are capped: the perceiver "is allowed up to 5 interaction turns."[^c18] Whether more rounds would keep helping, or start to plateau, is not tested here.
- The benchmarks are knowledge-intensive question sets scored with chain-of-thought. No human asker is in the loop, and the cost of the extra rounds is not reported.
- The teacher for training data is a proprietary model, and the paper reports that a weaker perceiver as teacher gave lower-quality data. How the data quality depends on the teacher is only partly examined.
- My reading, not the paper's claim: the single-turn ablation's gap is small on some benchmarks, so the case for multi-turn asking rests on a few points of accuracy in one model pairing.

## Related

- [[clarification-request]] — the answerer's question back to a user when meaning is unclear; here the asker questions a source for facts it lacks, and the source is a model.
- [[multi-agent-clarification]] — which agent in a compound system may interrupt the user; this note is the reasoner interrupting its own perceiver, not the user.
- [[perception-first-rationale-template]] — one VLM describes the image before reasoning; the single-turn ablation is the nearest form of that, with the asking taken out.
- [[multi-turn-clarification-plateau]] — extra clarification turns with a user plateau after about four; in the perception dialogue it is the one-reply restriction that loses accuracy, so the two findings point in different directions.
- [[caption-utility-gap]] — a caption as a text stand-in for an image, scored by a text-only reader; the perceiver's replies are a caption built under the reasoner's questions.
- [[text-answerability]] — the text-only screen that removes items a model answers without the picture; the dialogue paper uses the same filter when it builds its training set.
- [[mcts-training-trace-generation]] — keeping the generated paths that reach the correct answer as training traces, the same answer-matched retention used to build the perceiver's conversations; not separately ablated here.

[^c1]: arxiv-2511-19417 — "The reasoner agent typically initiates the dialogue by requesting relevant details about the question, including both visual and textual components."
[^c2]: arxiv-2511-19417 — "The perceiver agent extracts and describes relevant visual information"
[^c3]: arxiv-2511-19417 — "agent is prompted to output the final answer based on the discussions between the two agents"
[^c4]: arxiv-2511-19417 — "constitute the sole communication channel through which the reasoner can infer visual context"
[^c5]: arxiv-2511-19417 — "the reasoner agent is instructed to request clarifications or additional descriptions from the perceiver agent when necessary"
[^c6]: arxiv-2511-19417 — "it may omit or overlook certain visual details"
[^c7]: arxiv-2511-19417 — "even outperforming GPT-4o by 0.5%, 7.1%, and 12.1% on MMMU Pro, MathVista, and MathVision, respectively"
[^c8]: arxiv-2511-19417 — "GPT-4 recovers much of the performance of the fully multimodal GPT-4o"
[^c9]: arxiv-2511-19417 — "Performance drops are observed when removing supervised fine-tuning (SFT) or restricting the framework to single-turn conversations"
[^c10]: arxiv-2511-19417 — "This suggests that iterative communication plays an important role in improving the overall reasoning process"
[^c11]: arxiv-2511-19417 — "retaining the one that leads to the correct answer"
[^c12]: arxiv-2511-19417 — "We treat the answer from the singleVLM setting as the ground-truth label"
[^c13]: arxiv-2511-19417 — "can be answered correctly without images, since these are trivial for multimodal reasoning"
[^c14]: arxiv-2511-19417 — "typically because the visual information is too complex or abstract to be effectively conveyed through textbased communication"
[^c15]: arxiv-2511-19417 — "our experiments focus exclusively on vision as the target modality"
[^c16]: arxiv-2511-19417 — "developing such large-scale models remains beyond our current scope"
[^c17]: arxiv-2511-19417 — "is misled when reasoning jointly with the perceiver, often due to perception or communication errors"
[^c18]: arxiv-2511-19417 — "is allowed up to 5 interaction turns"
