---
description: "The asker's internal model of the generated artifact sets how specific the next prompt is: coders who read the code write prescriptive prompts, those who never inspect it write vaguer ones."
aliases: ["mental model of artifacts", "internal representation of the system being built", "vibe coder mental model"]
sources: ["arxiv-2512-22418"]
---
# Artifact mental model

Someone who asks for software is holding a picture of what is being built, and the next request is written from that picture. The vibe-coding study takes the term from Norman: "In this context, we use Norman’s definition [51] of a mental model, which is simply a person’s internal representation" of the things they interact with.[^c1] Here the picture covers the generated code, the UI it produces, and the AI that produces both. The authors list where it comes from: "Vibe coders formed mental models of artifacts through prior experience (All Vs)", and also through interaction with the models, through the outputs, and directly from the code.[^c2] Coders who read the code could build a finer picture than coders who watched only the UI or the chat replies.

The paper's proposal is that this picture sets the grain of the prompt. Coders who had read the code could write "prescriptive" requests that name a file, a component or a context.[^c3] One coder, after inspecting the code, pointed at a specific element and said "information to ask a good question."[^c4] The authors note that expertise shapes "how expertise could affect the granularity or even" the correctness of prompts.[^c5] Their own summary is that "Vibe coders’ mental model around artifacts may affect prompting strategies."[^c6]

The other side is a request written without a picture of the target. "Vibe coders with limited technical backgrounds, or who never examined the code, tended to" give bare instructions, and sometimes introduce errors.[^c7] One coder who had named a single library during setup later reflected, "I just am not prompting correctly."[^c8] Another found the mismatch only late: "I thought I was making an [mobile] app, apparently, this is a website."[^c9] Coders who never looked at the code "relied on interaction with UI outputs or AI" responses, and when one lost track of what had been generated, the next prompt asked where things stood.[^c10][^c11]

Read together, the observations suggest a mechanism. A prompt can only be as specific as the asker can name the thing it is about. Where the model of the artifact is thin, the request falls back on the outer shape of the goal, and the output is then judged against a picture the asker may not share with the model. This is my inference from the paper's observations; the paper does not test it.

The picture is itself inferred. The authors did not ask coders to describe it: "We inferred these interpretations from observable actions", meaning the behaviour on screen was read as the model.[^c12]

## Limits

- The asker's model is read from behaviour in 20 videos. No coder was asked to describe it, and no comparison holds the task fixed while varying the model.[^c12]
- The link to prompt granularity and correctness is stated with "could" and "may". The paper does not score prompts against the outcomes they produced.
- Only Norman's definition is used. Other accounts of mental models are not compared with it.
- The sample is mostly Python and JavaScript, and English-language videos: "Our dataset is also dominated by Python and JavaScript"[^c13]. The picture of an artifact may differ where the code is less familiar.

## Related

- [[user-driven-verification-decision]] — the experiment there finds verification set mainly by the participant's trust. A finer picture of the artifact is one thing that would let an asker tell a wrong answer from a right one; that link is my inference and is not tested there.
- [[over-reliance-discrimination-failure]] — students who could not separate wrong AI solutions from right ones. The same separation would draw on an artifact model; that too is my inference.
- [[design-fixation-first-output]] — the refining request is built on the first output, so the picture of that output sets what alternatives can be asked for.
- [[rolling-the-dice-reprompting]] — a repeated request with no new detail is the case where the asker's picture of the fault adds nothing to the prompt.

[^c1]: arxiv-2512-22418 — "In this context, we use Norman’s definition [51] of a mental model, which is simply a person’s internal representation"
[^c2]: arxiv-2512-22418 — "Vibe coders formed mental models of artifacts through prior experience (All Vs)"
[^c3]: arxiv-2512-22418 — "coders who possessed technical knowledge or had reviewed the code could construct prescriptive"
[^c4]: arxiv-2512-22418 — "information to ask a good question."
[^c5]: arxiv-2512-22418 — "how expertise could affect the granularity or even"
[^c6]: arxiv-2512-22418 — "Vibe coders’ mental model around artifacts may affect prompting strategies"
[^c7]: arxiv-2512-22418 — "Vibe coders with limited technical backgrounds, or who never examined the code, tended to"
[^c8]: arxiv-2512-22418 — "I just am not prompting correctly"
[^c9]: arxiv-2512-22418 — "I thought I was making an [mobile] app, apparently, this is a website."
[^c10]: arxiv-2512-22418 — "relied on interaction with UI outputs or AI"
[^c11]: arxiv-2512-22418 — "when losing track of generated contents"
[^c12]: arxiv-2512-22418 — "We inferred these interpretations from observable actions"
[^c13]: arxiv-2512-22418 — "Our dataset is also dominated by Python and JavaScript"
