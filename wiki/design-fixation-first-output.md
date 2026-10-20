---
description: "Askers who refine the first generated output instead of requesting alternatives show design fixation; the paper finds this in all live-stream coders and offers one contrasting example."
aliases: ["design fixation", "first-output anchoring in iterative prompting", "accepting the first generated result"]
sources: ["arxiv-2512-22418"]
---
# Design fixation on the first output

In iterative prompting the asker meets a generated result and must decide what to say next: ask for a change to the result in hand, or ask for another result. The vibe-coding study reports that its coders mostly took the first option. They "typically accepted or refined the first generated outputs rather than seeking alternatives, signaling design fixation."[^c1]

The pattern follows from how the sessions were opened. Coders began with loosely defined requests, such as "Build a modern website UI".[^c2] Once a result existed, they "iterated on the first result instead of prompting the model for alternative directions."[^c3] The study places this inside a wider habit of improvising the requirements as the output arrives. Many coders "formulated new requirements in response to outputs"[^c4], which the authors describe as improvising requirements and design "in ways that resemble exploratory programming".[^c5] The first output then becomes the object the next request is about.

That is the mechanism as I read it, not as the paper states it. A request to fix something already on screen is a different request from one that asks for a second design. Once the first design is the reference, a prompt that does not ask for alternatives will not produce them, and the asker's sense of what is possible is set by the one result they have seen. The paper does not measure this step.

The contrast is one coder, who ran "the same prompt across two different tools and then, as they explained, “pick[ing] which one I like better.”"[^c6] This is a practice the study reports, not a tested remedy. The authors' label for the main pattern is also explicit that it dominated the live streams: "While this pattern dominated live-streamed sessions".[^c7]

## Limits

- "Signaling design fixation" is the authors' reading of observed behaviour. No condition compares askers who request alternatives with askers who refine, so the label is not measured against a baseline.[^c1]
- The contrasting case rests on one coder (O7). Whether asking the same prompt across tools leads to better results is not tested.
- The paper does not say that refining the first output produced worse code. When the first output is close to what is wanted, refining it may be the right move. That qualification is mine, not the paper's.
- The pattern is attributed to the seven live-stream coders, marked "All Vs" in the text. Its reach to the opinion videos is not stated.

## Related

- [[artifact-mental-model]] — the picture of the generated artifact on which a refining request is built; a thin picture makes a fresh alternative harder to ask for.
- [[rolling-the-dice-reprompting]] — the other way the same first draw keeps being used: resampled with a repeated request instead of replaced by alternatives.

[^c1]: arxiv-2512-22418 — "seeking alternatives, signaling design fixation"
[^c2]: arxiv-2512-22418 — "Build a modern website UI"
[^c3]: arxiv-2512-22418 — "result instead of prompting the model for alternative directions"
[^c4]: arxiv-2512-22418 — "many formulated new requirements in response to outputs"
[^c5]: arxiv-2512-22418 — "requirements and design (x) in ways that resemble exploratory programming [12], refining"
[^c6]: arxiv-2512-22418 — "pick[ing] which one I like better."
[^c7]: arxiv-2512-22418 — "While this pattern dominated"
