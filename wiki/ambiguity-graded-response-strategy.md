---
description: "Ambiguous visual questions call for four graded responses (answer, infer, list, ask) set by the count of salient referents; VLMs default to overconfident answers and need training to choose."
aliases: ["strategic response generation", "four-level ambiguity strategy", "AQuA levels", "answer-list-ask ladder"]
sources: ["arxiv-2603-07394", "openalex-org-w7203956628"]
---
# Ambiguity-graded response strategy

A question about an image can be ambiguous to different degrees, and the best reply changes with the degree. AQuA (Jang and Kim, ICLR 2026) replaces the binary choice of answering or asking with four levels, each paired with its optimal strategy.[^c1]

## The ladder

- Level 0, unambiguous: answer directly. It is a control, to check the model does not over-apply ambiguity handling.[^c2]
- Level 1, low referential ambiguity: "this" or "it" can be resolved from context, so the model should infer the referent and answer, not treat the question as ambiguous.[^c3]
- Level 2, a few valid readings (two or three): list all plausible interpretations, since asking "may be unnecessary or inefficient".[^c4]
- Level 3, high ambiguity: enumerating candidates would be inefficient, so request clarification.[^c5]

The level is set by how many objects are salient in the image. Saliency is a weighted score, 0.7 on area ratio and 0.3 on closeness to the image centre, with a cutoff of 0.6. One salient object gives Level 1, two to three give Level 2, and five or more (often similar) give Level 3.[^c6] So the same sentence, "What color is this?", warrants different replies depending on the scene. The question text alone does not fix the strategy.

## What models do

Open and closed models (GPT-5, Gemini 2.5 Flash, Qwen) tend to answer by arbitrarily picking one referent.[^c7] The base Qwen2.5-VL-3B shows "a strong bias toward Level 0 predictions", a single confident answer whatever the ambiguity.[^c8] Fine-tuning on 3.6K training items spread evenly over the levels, first SFT and then GRPO, raised overall strategic accuracy, for example Qwen2.5-VL-3B from 83.81 (SFT) to 86.28 (SFT+GRPO). The reward is 1 for the correct strategy with no factual distortion, 0.7 for the correct strategy with a distortion, and 0 for a wrong strategy.[^c9]

SFT alone leaves errors concentrated in Level 1: the model collapses toward inferring and answering. GRPO redistributes these errors, lifting Levels 2 and 3 at a small cost in Level 1.[^c10] Remaining errors come from salience or stereotype. A model answers about the horse because it is the most salient object, where the label wanted clarification.[^c11]

## Humans do not fully agree on the boundary

On 200 test items with three annotators each, Levels 0 and 1 matched the label almost perfectly (50 and 48 of 50). Levels 2 and 3 matched only 32 of 50 each.[^c12] Disagreement came from borderline scenes with three or four targets (list or ask?) and from differing judgments of saliency.[^c13] The list/ask boundary is therefore partly subjective.

## The same boundary in text retrieval

The boundary also shows up for text. A 2026 master's thesis on retrieval-augmented answering inspected ambiguous questions from its own query set, and found that its system sometimes over-refused them, or picked one reading as best. It concludes that "ambiguity is not the same as unanswerability."[^c14] Its requirement is that "hallucination-aware behaviour requires response calibration, not only binary answer-versus-refusal decisions."[^c15] This is the ladder's move carried to text: a qualified or conditional answer sits between answering and asking. The thesis gives no levels and no grading rule, and its evidence is a handful of inspected cases from one prototype, so it names the need without testing a scheme (my reading).

## Limits

- Labels are derived from COCO bounding-box counts and GPT-5-generated answers. The thresholds (0.6; 2-3 versus 5 or more) are the authors' choices, and scenes with four objects are left out of the design. Whether the counts predict what a human asker needs is only partly checked, by the 200-item study above.
- The strategies are judged by correctness of the label, not by the cost or utility of the response to the user. The claim that listing beats asking at Level 2 is assumed in the design, not measured as user outcome.
- Only two small models (3B and 2B) were tuned and the data are single-turn, so what happens after the user answers a clarification is untested. GRPO used only 60 samples; a larger run (120) is reported in an appendix but not analysed here.
- The judge is GPT-5-mini, whose agreement with humans was checked on 400 cases.
- Images are COCO photographs, so transfer to other domains is not shown.

## Related

- [[referent-match-set-ambiguity]] — also types referential ambiguity by the number of matching objects, in robot scenes
- [[intent-aware-response-strategy]] — picks a response strategy per query type, in tutoring rather than by ambiguity degree
- [[clarification-only-aleatoric-uncertainty]] — when asking is the right reply, the opposite end of the ladder
- [[strategy-conditioned-rollout-grouping]] — RL grouped by strategy, a related training device

[^c1]: arxiv-2603-07394 — "While this binary answer-or-ask strategy can be useful"
[^c2]: arxiv-2603-07394 — "This category serves"
[^c3]: arxiv-2603-07394 — "the model is expected to"
[^c4]: arxiv-2603-07394 — "offering all reasonable interpretations"
[^c5]: arxiv-2603-07394 — "enumerating all possible candidates would be inefficient, and the most appropriate strategy is to"
[^c6]: arxiv-2603-07394 — "area ratio and its normalized distance to the image center"
[^c7]: arxiv-2603-07394 — "provide answers by arbitrarily selecting"
[^c8]: arxiv-2603-07394 — "we observe a strong bias toward Level 0 predictions"
[^c9]: arxiv-2603-07394 — "if strategy is correct but factual distortion detected,"
[^c10]: arxiv-2603-07394 — "we observe a slight drop in Level 1 performance after applying GRPO following SFT"
[^c11]: arxiv-2603-07394 — "to overcommit to a single referent instead of requesting clarification or listing alternatives."
[^c12]: arxiv-2603-07394 — "Level 0 and 1 achieve near-perfect agreement"
[^c13]: arxiv-2603-07394 — "annotators may differ on whether it is preferable to enumerate all options or to request"
[^c14]: openalex-org-w7203956628 — "ambiguity is not the same as unanswerability"
[^c15]: openalex-org-w7203956628 — "hallucination-aware behaviour requires response calibration, not only binary answer-versus-refusal decisions"
