---
description: "A harmful request carried inside a benign story or persona got past two LLMs more often than the same request stated directly, which the paper reads as the frame diluting the safety trigger."
aliases: ["context manipulation", "use-mention loophole", "narrative-frame request", "benign-frame embedding"]
sources: ["arxiv-2511-17666"]
---
# Frame-embedded request

A request for content a model should refuse can be carried inside a benign frame, a scene in a novel or a character's voice, instead of being stated plainly. In the one study that compares the two forms head to head here, the framed form did better. Perel (2025) tests four attack vectors on two LLMs, and "Context Manipulation emerged as the most potent attack vector."[^c2] The vector is defined by the embedding itself: "The strategy involves embedding a harmful request within a complex and seemingly innocent scenario."[^c1] The plain form was the control, and it failed: Direct Injection "yielded a near-zero success rate for both models".[^c5]

The paper's account of why the frame works is about what the model takes the request to be. It says models "struggle to differentiate between discussing harm in a" fictional or educational context, which is mention, from giving instructions for harm, which is use.[^c3] It then says the model is likely to comply "because the safety trigger is diluted by the surrounding benign text."[^c4] That is the authors' hypothesis. The study does not separate the frame from the request in a run that would isolate the dilution, so the mechanism is inferred from the pattern of success rates, not measured.

In the wiki's terms the frame changes the surface category of a request while the underlying principle stays the same. [[principle-isomorphism-across-category]] describes this structure: a judgment keyed to surface category can be moved across a boundary by a change that leaves the principle alone. A benign context that pulls a risk score down is the same weakness at the scoring level. [[monotone-risk-aggregation]] gives the design that resists it, a floor that benign context cannot lower once a risk item is detected. The frame is also a larger case of the phrasing effect in [[request-form-compliance-effect]], where declarative, consultative and imperative wording shifts how often models comply. What the paper adds is that the change can be a whole scenario rather than a grammatical form.

The concept matters for asking and answering because it says the same content can be answered or refused depending on how the question arrives. The answerer's commitment is then partly a function of the framing of the question, and not only of what it asks. The paper uses this on the defending side. The same fact could be read by a questioner as a reason to check whether a frame changes what a given answer is.

## Limits

- One paper, one author, and a small design. The text states "The experiment consisted of 320 total distinct attack trials."[^c6] That is 20 trials per vector per strategy on two models, so each vector comparison rests on a small cell.
- The success judgment is the author's own. Outcomes are scored with "a graded Severity Score (1-5) was employed to quantify the extent of"[^c7] the safety failure. The sections read give no second rater and no agreement figure, so the reported rates depend on one scale applied by one person.
- The mechanism is not tested. The use-mention account is offered as an explanation after the success pattern is seen. Nothing here shows that a different frame, with the same request, would be answered differently for the reason the paper gives.
- The models are named inconsistently in the text: the abstract says GPT-4 "specifically the GPT-4o mini model", while the research-problem section says "the free-tier GPT-4o model". Read as one model family, the comparison may not be as specific as the paper's title suggests.
- The claim is about refusal of harmful content. It says nothing about whether a framed question gets a worse or better answer on ordinary tasks.

## Related

- [[llm-red-teaming]] — the wider practice of finding inputs on which a model fails; a frame is one kind of input such a search can vary.
- [[script-level-obfuscation]] — another surface change that keeps intent and moves the safety judgment; there the change is orthographic, here it is narrative.
- [[principle-isomorphism-across-category]] — the general form of a judgment that follows surface category.
- [[monotone-risk-aggregation]] — how a risk score can be built so benign context cannot dilute it.
- [[request-form-compliance-effect]] — the same question of how phrasing alone shifts compliance, at the level of grammatical form.

[^c1]: arxiv-2511-17666 — "The strategy involves embedding a harmful request within a complex and seemingly innocent scenario."
[^c2]: arxiv-2511-17666 — "However, Context Manipulation emerged as the most potent attack vector."
[^c3]: arxiv-2511-17666 — "Models struggle to differentiate between discussing harm in a"
[^c4]: arxiv-2511-17666 — "the safety trigger is diluted by the surrounding benign text"
[^c5]: arxiv-2511-17666 — "yielded a near-zero success rate for both models"
[^c6]: arxiv-2511-17666 — "The experiment consisted of 320 total distinct attack trials."
[^c7]: arxiv-2511-17666 — "a graded Severity Score (1-5) was employed to quantify the extent of"
