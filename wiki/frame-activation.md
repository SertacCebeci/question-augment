---
description: "With the input fixed, a prompt can make one semantic relation the criterion of judgment, moving labels toward the relation it foregrounds; undirected sensitivity is a separate measure."
aliases: ["prompt frame activation", "frame-oriented prompting", "relation-criterion prompting"]
sources: ["arxiv-2512-12688"]
---
# Frame activation

Frame activation is the first of three levels at which a natural-language prompt can act on a fixed model: the interpretive structure under which an input is judged. The paper's definition is direct: "Frame activation concerns the interpretive structure under which an input is judged."[^c1] A frame makes some relations in a situation relevant and others not, so a prompt can make "one semantic relation more prominent than another while leaving the input unchanged."[^c2] The input does not change; the criterion applied to it does.

The paper's test case is natural language inference. One premise–hypothesis pair is shown under a neutral prompt and under entailment-, contradiction- and uncertainty-oriented prompts, and the model still returns one of three labels. Because the pair and the output space are fixed, any difference across conditions is attributed to the frame. The stated expectation is directional, not merely variable: "The expected effect is directional rather than merely variable."[^c3] An entailment frame should move decisions toward entailment, a contradiction frame toward contradiction, and an uncertainty frame toward neutral. The measures follow from that expectation. Target-frame recall gain compares each frame's recall for its own label with the neutral prompt's recall. Bias shift compares the rate at which the frame's label is predicted under its prompt with that rate under the neutral prompt. A separate frame-sensitivity score counts examples whose label changes across any two prompts. The paper keeps the two apart: its diagnostics "distinguish undirected prompt sensitivity from movement toward the relation foregrounded by the prompt."[^c4]

The movement is not the same across models. The paper reports that one small model's "predictions often shift toward the label foregrounded by the prompt", and that this responsiveness "reduces balanced classification performance in several conditions."[^c5] A prompt can therefore move the label distribution in the stated direction while making the classifier worse on balance. A directional shift is evidence about where the judgment went, not about whether it went well.

Frame activation sits at the bottom of the paper's hierarchy. "Frame activation is the most direct form because it changes the evaluative criterion applied to a fixed input."[^c6] The paper places it closest to ordinary prompt engineering, since "a natural-language instruction can specify a role, criterion, perspective, or label relation."[^c7] [[salience-control]] and [[construal-selection]] are the deeper levels; each is treated in its own note.

## Limits

- The paper studies three English-language benchmark tasks: "The present study focuses on three English-language benchmark tasks". Whether frame movement appears in open-ended generation, dialogue or other languages is not shown.[^c8]
- The frames were hand-written. The paper says "manually designed prompts, so future work should test paraphrased prompt families and broader prompt" — the study cannot yet separate a semantic category from the particular wording used for it.[^c9]
- The frame concept is borrowed from frame semantics, where "expressions" are "understood relative to structured background situations."[^c10] What survives the transfer is the notion that a background structure makes some relations relevant to a judgment. What does not survive is any lexical or role structure: the paper uses prompt conditions, not FrameNet annotations, and it does not test a frame's internal content.
- The paper measures label distributions and recall, not the internal use of the relation. That a frame is "used" as a criterion is the paper's reading of directional movement, not something observed inside the model. This is my reading of the measures.

## Related

- [[mandate-incentive-framing-split]] — another case where the wording alone, with the input fixed, changes the answerer's behaviour; there an incentive, here a relation criterion
- [[task-conditional-prompt-gain]] — accuracy gains from a prompt can change sign across tasks; a directional frame measure asks where the judgment moved, which accuracy does not report
- [[salience-control]] — the next level: the same prompt family acting on which evidence is foregrounded
- [[construal-selection]] — the deepest level: the organization of the task as a whole

[^c1]: arxiv-2512-12688 — "Frame activation concerns the interpretive structure under which an input is judged."
[^c2]: arxiv-2512-12688 — "one semantic relation more prominent than another while leaving the input unchanged"
[^c3]: arxiv-2512-12688 — "The expected effect is directional rather than merely variable."
[^c4]: arxiv-2512-12688 — "distinguish undirected prompt sensitivity from movement toward the relation foregrounded by the prompt"
[^c5]: arxiv-2512-12688 — "its predictions often shift toward the label foregrounded by the prompt"
[^c6]: arxiv-2512-12688 — "Frame activation is the most direct form because it changes the evaluative criterion applied to a fixed input."
[^c7]: arxiv-2512-12688 — "a natural-language instruction can specify a role, criterion, perspective, or label relation"
[^c8]: arxiv-2512-12688 — "The present study focuses on three English-language benchmark tasks"
[^c9]: arxiv-2512-12688 — "manually designed prompts, so future work should test paraphrased prompt families and broader prompt"
[^c10]: arxiv-2512-12688 — "Frame semantics treats expressions as being understood relative to structured background situations"
