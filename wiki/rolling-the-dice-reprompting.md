---
description: "Reissuing a prompt with the same intent and no new information turns refinement into a fresh draw; with stochastic generation, the asker's knowledge stops entering the loop."
aliases: ["rolling the dice", "method-redundant prompting", "reprompting with unchanged intent"]
sources: ["arxiv-2512-22418"]
---
# Rolling the dice reprompting

When generation is stochastic, an asker who gets an unwanted result has two options: send the request again, or send a request that contains something new. The first is another draw from the same distribution. The second changes what the model is conditioned on. The vibe-coding study calls the first pattern "rolling the dice" and codes it operationally. A prompt was counted as method-redundant "if it repeated a prior intent without introducing new information, such as simple rewording, copying an identical error message, or rejecting an output without further explanation."[^c1] The authors describe the phenomenon as "developers reissue the prompts with similar intent without adding new information."[^c2]

The pattern starts from a mismatch in expectations. Debugging or feature refinement is expected to be deterministic, and it "can feel stochastic, like “throwing a dice”".[^c3] A single attempt that fails, then a second with the same wording, is treated as sampling when the asker expected a diagnosis. One coder contrasted this with image generation: "[With images], you can just reroll, since an entire class of outputs can fit the problem."[^c4] A reroll is useful there because many outputs are acceptable. For code, the same coder said, "But in programming, one pixel off is a bug."[^c5] A redraw of an almost-right program is not closer to the target by its own momentum.

The paper measures the share of such prompts within each coder's session. Two live-stream coders, V5 and V4, put a large share of their prompts into this class: "40% of their prompts to rolling-the-dice".[^c6] One of them sent a run of error messages with no added hypothesis: "V5 sent 31 consecutive prompts containing only error messages".[^c7] The authors connect the larger shares to lower technical background and high reliance on AI, in their coding of the sessions.[^c8] Prompts that added a detail or a hypothesis were not counted: "Prompts that introduced new details or hypotheses were not".[^c9]

Why this matters for asking, in my own voice: a repeat with no new detail gives the model the same conditioning as before, so the answer is another sample from a distribution the asker has not narrowed. The asker's knowledge of the fault does not grow across the attempts. The paper reports the same thing in its debugging description, where some high-reliance coders "resolved their errors completely by repeating requests with the same or derived error messages without providing".[^c10] That is a description of the pattern, not a demonstration that it fails.

## Limits

- The count is made by the authors on 254 prompts from seven live-streamed sessions, about 16 hours.[^c11] It is one sample of one kind of session.
- The paper calls the analysis exploratory: it "served as deepening understanding for prior qualitative analysis rather than generalization of all" vibe coding practices.[^c12]
- The label depends on coding intent, and "simple rewording" counts as redundant. A reworded prompt that changed the model's conditioning would be miscounted, and the paper does not check for that.
- The paper counts repeats; it does not test whether a repeat made less progress than a new detail would have. The claim that the repeat carries no knowledge forward is my inference from the coding rule.

## Related

- [[design-fixation-first-output]] — the first draw is kept and resampled rather than replaced by alternatives; the two patterns share the same first result.
- [[artifact-mental-model]] — a repeated error message is a request without a hypothesis about the fault; how much the asker can add depends on the picture of the artifact they hold.

[^c1]: arxiv-2512-22418 — "A prompt was coded as method-redundant (or rolling the dice) if it repeated a prior intent without introducing"
[^c2]: arxiv-2512-22418 — "developers reissue the prompts with similar intent without adding new information"
[^c3]: arxiv-2512-22418 — "Debugging or feature refinement—expected deterministic—can feel stochastic, like “throwing a dice”"
[^c4]: arxiv-2512-22418 — "an entire class of outputs can fit the problem"
[^c5]: arxiv-2512-22418 — "But in programming, one pixel off is a bug."
[^c6]: arxiv-2512-22418 — "40% of their prompts to rolling-the-dice"
[^c7]: arxiv-2512-22418 — "V5 sent 31 consecutive prompts containing only error messages"
[^c8]: arxiv-2512-22418 — "Vibe coders with less relevant"
[^c9]: arxiv-2512-22418 — "Prompts that introduced new details or hypotheses were not"
[^c10]: arxiv-2512-22418 — "completely by repeating requests with the same or derived error messages without providing"
[^c11]: arxiv-2512-22418 — "7 live-streamed coding sessions (≈16 hours, 254 prompts)"
[^c12]: arxiv-2512-22418 — "served as deepening understanding for prior qualitative analysis rather than generalization of all"
