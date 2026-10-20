---
description: "A separate context generator writes intent, ambiguity and risk for a prompt; training it against a frozen decoder lets the snippet transfer to other answering models."
aliases: ["context-aware inference", "context snippet", "ContextLens", "context generator"]
sources: ["arxiv-2512-11986"]
---
# Transferable context snippet

A single model can be asked to reason and answer in one pass. This design splits the job in two. A context generator reads the user prompt and writes a short text, the snippet, that describes what the request may mean: the user's probable intent, whether the request is ambiguous, what risks it carries, and a plan for a safe reply. The snippet is appended to the original prompt, and the enriched input goes to whichever model writes the final answer. The generator is a separate model. The paper states the separation as a definition: "By definition, a context generator is independent of the model that will consume the context in order to produce the final answer."[^c1]

The mechanism rests on one assumption: a fuller description of the request changes the decision to comply, refuse or ask. The authors write that "The assumption is that LLMs can more accurately decide whether to refuse or comply to the user prompt (or ask for more information) given a more complete description of it."[^c2] The description is meant to carry the parts of a request that the prompt leaves implicit, such as "potential intents, risks, or even relevant technical background knowledge."[^c3]

Even without training, the idea has an effect. The zero-shot version is a fixed template that "instructs it to output five sections" (user intent, ambiguity, potential risks, an action decision, and a safe response plan).[^c4] The paper reports that this template, applied to an off-the-shelf model, gives "contextualization that substantially improves refusal accuracy on ambiguous harmful requests."[^c5]

The trained version, ContextLens, is a small model (Qwen2.5-3B in the main experiments) optimised with GRPO. The snippet is given "to a different frozen decoder model d", and the generator is rewarded for the decoder's behaviour, not for a model it is co-trained with.[^c6] The authors argue this is what allows transfer. The design choice is stated as "promotes transferability of the generated context across models," and it "prevents co-adaptation between context snippet and response."[^c7] The reasoning-trace alternative is contrasted directly: traces from a reasoning model are "not explicitly optimized to be transferable across models" and carry no objective that keeps them informative about the prompt.[^c8]

What was measured. On safety and over-refusal benchmarks (SafetyInstruct, AdvBench, WildJailbreak and XSTest), zero-shot context from Llama-3-8B-Instruct helps a stronger closed model: "the Llama-3-8B-Instruct model provides substantial benefits for GPT-4o", up to a 22.93% gain on WildJailbreak.[^c9] The trained 3B generator is reported to do better on the base models: "a 4.21% gain on GPT-4o and a 10.55% gain on Llama-3-8B-Instruct compared to the base models."[^c10] The mechanism on over-refusal is that the snippet helps the answerer separate harmless from harmful requests that look alike: "the model can better distinguish benign requests, thereby improving the compliance rate without" lowering the safety rate.[^c11]

## Limits

- Transfer is shown across a small set of decoders (Llama-3.2-3B, Llama-3-8B, GPT-4o, and the Qwen models as generators). Whether it holds for other families, or for answerers far from these, is not shown in the text I read.
- The decoder is frozen during training, and the paper reports that "variations in decoder type exhibit minimal impact on downstream performance."[^c12] This is a result about the training decoder, not a test of what a snippet trained against one decoder does with a very different answerer.
- The safety rewards and the reconstruction check are scored by an LLM judge. The text I read defines the similarity term as "determined by an LLM-as-a-judge."[^c13] Judge bias is not tested in the slices read.
- The gains are reported as averages and as single benchmark numbers. The text I read gives no intervals, so the size of the transfer effect is not established beyond these points.
- Context changes what is refused and what is answered, and the paper's outcome measures are attack success and compliance. The snippet is not scored for correctness of the intent it names; a wrong intent that happens to lead to a safe answer would count as a success in these measures (my inference).
- Cost is not measured in the text read. The snippet adds a model call and tokens; the trade against a single pass is not quantified here.
- The paper's choice of training against a frozen decoder is one way to prevent co-adaptation. Whether it is necessary for transfer, or whether the reconstruction term does the work, is not isolated in the ablations I read (my inference).

## Related

- [[question-reconstructability-reward]] — the reconstruction objective that scores the snippet in this design, with its own copy control
- [[latent-intent-before-answer]] — also writes an unstated intent before answering, but in one model, with reward on the answer only and no separate frozen decoder
- [[wise-refusal]] — credits a refusal that names what is missing; a snippet's "ask for more information" plan is a related form, not scored against that rubric here
- [[dual-use-context-cue]] — a context cue that helps in distribution and misleads under shift; the snippet's effect on mismatched prompts is not measured in this paper

[^c1]: arxiv-2512-11986 — "By definition, a context generator is independent of the model that will consume the context in order to produce the final answer."
[^c2]: arxiv-2512-11986 — "The assumption is that LLMs can more accurately decide whether to refuse or comply to the user prompt"
[^c3]: arxiv-2512-11986 — "including potential intents, risks, or even relevant technical background knowledge"
[^c4]: arxiv-2512-11986 — "that instructs it to output five sections"
[^c5]: arxiv-2512-11986 — "contextualization that substantially improves refusal accuracy on ambiguous harmful requests"
[^c6]: arxiv-2512-11986 — "to a different frozen decoder model d to reconstruct prompt pd"
[^c7]: arxiv-2512-11986 — "promotes transferability of the generated context across models"
[^c8]: arxiv-2512-11986 — "they are not explicitly optimized to be transferable across models"
[^c9]: arxiv-2512-11986 — "the Llama-3-8B-Instruct model provides substantial benefits for GPT-4o"
[^c10]: arxiv-2512-11986 — "a 4.21% gain on GPT-4o and a 10.55% gain on Llama-3-8B-Instruct compared to the base models"
[^c11]: arxiv-2512-11986 — "the model can better distinguish benign requests, thereby improving the compliance rate without"
[^c12]: arxiv-2512-11986 — "variations in decoder type exhibit minimal impact on downstream performance"
[^c13]: arxiv-2512-11986 — "determined by an LLM-as-a-judge"
