---
description: "Retrieved encyclopedia passages placed in a teacher's prompt when it writes training rationales, so the student learns the facts through its traces, not through retrieval at answer time."
aliases: ["grounded reasoning traces", "retrieval-augmented rationale generation", "knowledge-grounded trace distillation", "RAG-based trace distillation"]
sources: ["arxiv-2512-05658"]
---
# Retrieval-grounded rationale distillation

The generation step of a rationale-distillation pipeline can take retrieved text as input. The multilingual medical work builds a knowledge base from Wikipedia pages in its medical project, split into sections. For each question and options pair, "We select the top five most similar chunks as context," by cosine similarity of embeddings, and an LLM rewrites them to reduce redundancy.[^r1] The retrieved passages are "pre-pended" to the model input before prompting.[^r2] The teacher then receives the retrieved context "to provide factual knowledge on the medical topic," together with the question, the options and the correct answer, and writes the trace.[^r3]

The mechanism is a change of route. The knowledge is not given to the student at test time. It is written into the training targets: the student is fine-tuned on question, reasoning, answer triplets, and the retrieved facts reach its weights through the rationale text. This differs from putting the same text in the prompt when answering. The wiki's [[knowledge-injection-mechanism-comparison]] note reports, on a different setup, that supplying text at answer time moves accuracy on post-cutoff questions while training on the same text barely does. A grounded trace is a third route, between those two: retrieval is used once, at data-generation time, and its output is distilled. The work does not compare its route with answer-time retrieval, so which route delivers more per fact is not known from it. That comparison is my inference from the design.

The measured effect is an ablation on Llama-3.1-8B. Standard SFT on question-answer pairs is the baseline. Adding reasoning traces distilled without retrieved context gives a gain, and the paper reports the grounded traces as a further gain: "grounding traces in Medical-Wikipedia provides an additional +3.3 points gain."[^r4] Reading the layout-extracted Table 5 myself, the +3.3 figure is the step from reasoning-only traces (54.3 average) to the configuration that also trains on traces from all three languages together (57.6). The single-language grounded configuration sits at 56.7. On that reading, the grounding step alone is about 2.4 points, and the remainder of the headline gain comes from joint multilingual training. This is my reading of a table, not a number the authors state, and it should be checked against the source before it is relied on.

What the work does show is narrower. Grounded traces were evaluated in-domain and out-of-domain, and the paper's abstract reports "consistent performance gains in both few-shot in-context learning and supervised fine-tuning settings."[^r5] The gains are on multiple-choice accuracy, so the mechanism is measured for that answer format only.

## Limits

- The grounding step is confounded in the headline figure. By my reading of Table 5, the grounded single-language configuration gains about 2.4 points over reasoning-only traces, and the +3.3 figure includes multilingual training.
- The ablation runs on one student: "we constrain the analysis to one model."[^r6] Other student sizes and families are covered only by the main results, which do not isolate the grounding step.
- The knowledge source is Wikipedia, which the authors call a choice made for cross-lingual parallelism: "more authoritative medical sources could further strengthen grounding."[^r7] They also note that "The use of Wikipedia may introduce Wikipedia-derived biases into the multilingual training."[^r8]
- The retrieval settings (five chunks, one embedding model, LLM rewriting) are not varied in the parts read. Whether a different retriever or chunk count changes the result is not shown here.
- The paper's own error analysis points upstream of the trace. Eleven medical doctors reviewed a random sample of 75 question-option-reasoning triplets, and the authors report that "the most salient reasoning inconsistencies arise from difficulties in integrating relevant clinical information rather than from flawed reasoning per se."[^r9] This suggests that supplying facts addresses a real bottleneck. It does not show that the supplied facts were the ones the student needed. The sample is not a comparison of grounded and ungrounded traces, so it does not measure the grounding step.
- A grounded rationale can look sourced without being sourced. The rationale is written by a teacher that sees the passages and the answer; the paper does not check whether a student's use of a trace depends on the passages it cites. That the traces are "not faithful explanations" of a model's process is stated by the authors themselves, as in answer-conditioned-rationale. Fluent rationales that do not rest on what they cite are the failure in [[cot-hallucination-trap]].

## Related

- [[knowledge-injection-mechanism-comparison]] — answer-time retrieval and training on text are the two routes this note sits between
- answer-conditioned-rationale — the generation step this note extends with retrieved context
- [[knowledge-distillation]] — rationale distillation as a form of teacher-student transfer; this is its retrieval-augmented teacher
- [[cot-hallucination-trap]] — a fluent rationale is not evidence it rests on the context it was given

[^r1]: arxiv-2512-05658 — "We select the top five most similar chunks as context."
[^r2]: arxiv-2512-05658 — "we pre-pended the retrieved passages to the model input prior to prompting"
[^r3]: arxiv-2512-05658 — "to provide factual knowledge on the medical topic"
[^r4]: arxiv-2512-05658 — "grounding traces in Medical-Wikipedia provides an additional +3.3 points gain"
[^r5]: arxiv-2512-05658 — "demonstrating consistent performance gains in both few-shot in-context learning and supervised fine-tuning settings"
[^r6]: arxiv-2512-05658 — "we constrain the analysis to one model"
[^r7]: arxiv-2512-05658 — "more authoritative medical sources could further strengthen grounding"
[^r8]: arxiv-2512-05658 — "The use of Wikipedia may introduce Wikipedia-derived biases into the multilingual training"
[^r9]: arxiv-2512-05658 — "the most salient reasoning inconsistencies arise from difficulties in integrating relevant clinical information rather than from flawed reasoning per se"
