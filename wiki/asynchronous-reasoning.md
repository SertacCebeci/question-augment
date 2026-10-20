---
description: "A reasoning LLM can write its visible answer while still thinking, by re-indexing positions over one shared cache; the writer pauses when a self-asked probe says the thoughts are not ahead."
aliases: ["AsyncReasoning", "asynchronous thinking", "concurrent thinker and writer streams"]
sources: ["arxiv-2512-10931"]
---
# Asynchronous reasoning

A reasoning model runs one sequence: it reads the input, thinks, and only then writes. The paper's point is that this makes the model non-interactive. When new information arrives mid-thought, the model can either "interrupt their reasoning to react, sacrificing any incomplete thought tokens" or keep reasoning while the input waits.[^c1] Asynchronous reasoning keeps the thinking and the visible answer as concurrent streams, with user input, private thoughts and public response all updatable in real time.[^c2] The motivation is human: "we begin thinking about the problem while reading it".[^c3]

The mechanism is positional rather than architectural. The premise is that a transformer's only sense of order is its positional encoding: "the only thing that makes them aware of sequence order is positional encoding".[^c4] So the method leaves tokens where they sit in memory and changes their positional relations: "it is sufficient to change positional relations between tokens".[^c5] Under rotary embeddings the paper applies "stream-specific query rotations so that the same stored keys and" values are read under two views.[^c24] The response sees the partial thoughts "as if they were generated in a standard read-think-answer cycle", and the thoughts see the response as if it came in an earlier turn.[^c25] Each generated token is encoded once.[^c6] The approach works "without additional training".[^c26]

Synchronisation is left to the model. The paper states it plainly: "we periodically ask the model if its private thoughts are still ahead of the public" response.[^c7] The question is inserted "at the end of every paragraph or after every" 20 thinking tokens, and its yes/no probabilities decide: "is more likely, we keep thinking asynchronously", and otherwise the response stream pauses until the next yes.[^c8][^c27] The probe is then hidden from the cache, "we remove this prompt from its view (by hiding the corresponding key-value entries)", so it does not disturb the chain of thought.[^c9]

What was measured. On MATH-500 with Qwen3-32B on one A100, the default criterion "offers nearly the same accuracy as fully synchronous thinking" and at a significantly lower real-time delay.[^c10] The abstract reports the time to first non-thinking token falling "first non-thinking token from minutes to ≤ 5s and the overall delays by up to 12×".[^c11] Biasing the probe toward writing cuts delay further, at a cost: "cost of some accuracy loss, which comes from the writer answering too early".[^c12] That trade is the part this wiki needs: committing a visible answer early buys responsiveness and pays in accuracy.

Late input is the second measurement. The paper takes up the case where "additional inputs may arrive after decoding begins", inserting them as shards at paragraph boundaries.[^c28] "inserting each shard into all three blocks recovers accuracy on both" of the two datasets, approaching the case where all shards come up front.[^c13] The shards are built so that "We verify the first shard alone is insufficient".[^c14] Timing matters: "Accuracy drops as ksteps increases because more information arrives later".[^c15]

Transfer to the asker and answerer. In my reading, what survives is the timing structure: an answer can begin before the question is complete, and a constraint that arrives after the answer has been committed costs more to absorb. This is my inference, not the paper's claim. The paper's impact statement names the benefit as something that can "reduce the need to interrupt and discard partial reasoning when new information arrives".[^c16] What does not survive is the mechanism. Re-indexing a shared key-value cache is a property of RoPE transformers; a human answerer has no cache to re-read. The probe is also the model's self-report of its own lead. Whether human answerers judge their lead this way is not measured in the text, and I do not claim it.

## Limits

- The method is training-free but prompt-dependent: "this decision is implemented through prompting".[^c17] The paper says "Weaker models may switch too early, producing answers before sufficient reasoning has accumulated".[^c18] Small models lose more: "models such as Qwen3-0.6B lose substantially more accuracy".[^c19]
- Shards that arrive after generation has finished are outside the setup: "we do not handle shards" in that case, and accuracy may fall further at large insertion delays.[^c20]
- The late inputs are synthetic. The paper builds them as a "dataset from MATH-500 by using GPT-5 to rewrite each problem into two shards".[^c21] They are not spoken interruptions from people.
- Safety is not guaranteed: "race conditions remain an inherent failure mode of asynchronous safety verification", and the method "should not be treated as a complete" guarantee.[^c22][^c23]
- Delay is measured as silence through a TTS pipeline on one GPU, and accuracy by an LLM judge. No human listener study appears in the text read for this note.

## Related

- [[clarification-request]] — the answerer's move when information is missing; asynchronous reasoning is a mechanism for absorbing such information without ending the turn.
- [[pre-committed-answer-before-cot]] — an answer fixed before the chain of thought; here the visible answer and the thought run concurrently instead.
- [[mid-turn-post-turn-protocol]] — user interruption as a trigger for reopening a task; the same arrival-during-work problem at the dialogue level.
- [[feedback-timing-error-derailment]] — the timing of feedback relative to where errors propagate; the same question of when new information is worth most.
- [[interleaved-reasoning]] — a visible answer during thought reached by training discrete intermediate responses, not by re-indexing a shared cache

[^c1]: arxiv-2512-10931 — "sacrificing any incomplete thought tokens"
[^c2]: arxiv-2512-10931 — "user inputs, private thoughts, and a public response, all of which can be updated in"
[^c3]: arxiv-2512-10931 — "we begin thinking about the problem while reading it"
[^c4]: arxiv-2512-10931 — "the only thing that makes them aware of sequence order is positional encoding"
[^c5]: arxiv-2512-10931 — "it is sufficient to change positional relations between tokens"
[^c6]: arxiv-2512-10931 — "to encode each generated token exactly once"
[^c7]: arxiv-2512-10931 — "we periodically ask the model if its private thoughts are still ahead of the public"
[^c8]: arxiv-2512-10931 — "is more likely, we keep thinking asynchronously"
[^c9]: arxiv-2512-10931 — "we remove this prompt from its view (by hiding the corresponding key-value entries)"
[^c10]: arxiv-2512-10931 — "Our default criterion offers nearly the same accuracy as fully synchronous thinking"
[^c11]: arxiv-2512-10931 — "first non-thinking token from minutes to ≤ 5s and the overall delays by up to 12×"
[^c12]: arxiv-2512-10931 — "cost of some accuracy loss, which comes from the writer answering too early"
[^c13]: arxiv-2512-10931 — "inserting each shard into all three blocks recovers accuracy on both"
[^c14]: arxiv-2512-10931 — "We verify the first shard alone is insufficient"
[^c15]: arxiv-2512-10931 — "Accuracy drops as ksteps increases because more information arrives later"
[^c16]: arxiv-2512-10931 — "reduce the need to interrupt and discard partial reasoning when new information arrives"
[^c17]: arxiv-2512-10931 — "this decision is implemented through prompting"
[^c18]: arxiv-2512-10931 — "Weaker models may switch too early, producing"
[^c19]: arxiv-2512-10931 — "models such as Qwen3-0.6B lose substantially more accuracy"
[^c20]: arxiv-2512-10931 — "we do not handle shards"
[^c21]: arxiv-2512-10931 — "dataset from MATH-500 by using GPT-5 to rewrite each problem into two shards"
[^c22]: arxiv-2512-10931 — "race conditions remain an inherent failure mode of asynchronous safety verification"
[^c23]: arxiv-2512-10931 — "it should not be treated as a complete"
[^c24]: arxiv-2512-10931 — "stream-specific query rotations so that the same stored keys and"
[^c25]: arxiv-2512-10931 — "as if they were generated in a standard read-think-answer cycle"
[^c26]: arxiv-2512-10931 — "without additional training"
[^c27]: arxiv-2512-10931 — "at the end of every paragraph or after every"
[^c28]: arxiv-2512-10931 — "additional inputs may arrive after decoding begins"
