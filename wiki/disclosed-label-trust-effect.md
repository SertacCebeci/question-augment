---
description: "Labelling health information as AI rather than human lowered trust in it, separately from its actual source; source and label effects added up without interacting in a 142-person survey."
aliases: ["AI-label trust penalty", "transparency label effect on trust", "disclosed authorship effect", "source-label dissociation"]
sources: ["arxiv-2512-12348"]
---
# Disclosed label effect on trust

Who a piece of health information is said to come from changes how far people trust it, and this holds apart from who actually wrote it. The study manipulated two things independently: the actual source (a human professional or an LLM) and the disclosed label (human or AI). Labels were applied across both sources, so a text could be "intentionally mismatched with the actual source (i.e., cross-labeled)".[^d2] Participants were not told that mismatches occurred, so each text was judged as presented.

In the online survey (N=142), each cue moved trust on its own. LLM-written text was trusted more than human-written text, and text labelled as human was trusted more than text labelled as AI.[^d1] The label effect is the clearer of the two: "Participants perceived significantly lower trust in health information labeled as from AI compared to that labeled as from human professionals".[^d4] The average was "4.04" for human-labelled text and "3.82" for AI-labelled text on a five-point scale.[^d13] Among human-labelled text, the human-sourced and LLM-sourced versions did not differ.[^d12]

The two effects added rather than interacted. In the within-subjects lab study (N=40) the source-by-label interaction was small: "the combined influence of source and label does not affect trust beyond their individual effects".[^d3] On this reading a text's trust score is close to a sum: one term for its actual source, one for the label it carries. The paper frames the label as an interface cue that triggers heuristics: "Labels operate as interface-level factor that invoke trust heuristics, particularly under conditions of".[^d10] That framing comes from the MATCH model the authors adopt. The study did not test the heuristic as a mechanism; it only shows the label effect in ratings.

Question type did not change this. "the type of health question did not significantly affect trust, alone or in interaction with label and source."[^d11] The label effect was the same across general, symptom and treatment questions.

My inference: a trust rating of health text is not a rating of its content alone. A design that tests AI disclosure has to hold the label and the actual source apart, or the label gets read as a property of the content.

## Limits

- The lab-study label effect is small on the scale. "the raw change (-0.15) was modest", although the authors call its standardized size medium and argue that a bounded Likert scale makes small differences meaningful.[^d5]
- Perceived source was not measured. "we acknowledge that perceived source awareness could influence trust independently of disclosed labels" — so the label may work through a participant's guess about authorship, which the study did not check.[^d6]
- One model only. "this study focused on a single LLM (GPT-4o)", so the source effect is the output of one system and may not carry to others.[^d7]
- Trust was a single self-report at one time point. No decision or follow-the-advice behaviour was observed.[^d8]
- The sample is not representative: "was not representative of the general population".[^d9]
- The label was never linked to outcomes such as following the advice; the text shows the effect on rated trust and nothing about harm.

## Related

- [[conclusion-reliance-under-low-domain-knowledge]] — a study where AI-labelled text was as helpful as human-labelled text; here the same kind of label lowers rated trust, which is a different measure
- [[source-credibility-hierarchy-in-knowledge-conflicts]] — an attributed source acting as a prior when evidence conflicts; the same kind of cue, measured on LLM answer probabilities
- [[provenance-cue-leakage]] — who produced an example as a cue correlated with its label; here the disclosed label is the cue itself
- [[implicit-trust-sensing]] — gaze and physiological signals recorded in the same study, as an implicit measure beside self-report

[^d1]: arxiv-2512-12348 — "information labeled as human was trusted more than that labeled as AI"
[^d2]: arxiv-2512-12348 — "labels could be intentionally mismatched with the actual source (i.e., cross-labeled)"
[^d3]: arxiv-2512-12348 — "the combined influence of source and label does not affect trust beyond their individual effects"
[^d4]: arxiv-2512-12348 — "Participants perceived significantly lower trust in health information labeled as from AI compared to"
[^d5]: arxiv-2512-12348 — "the raw change (-0.15) was modest"
[^d6]: arxiv-2512-12348 — "we acknowledge that perceived source awareness could influence trust independently of disclosed labels"
[^d7]: arxiv-2512-12348 — "this study focused on a single LLM (GPT-4o)"
[^d8]: arxiv-2512-12348 — "our study measured trust at a single time point and relied on self-reports rather than actual decision-making"
[^d9]: arxiv-2512-12348 — "was not representative of the general population"
[^d10]: arxiv-2512-12348 — "Labels operate as interface-level factor that invoke trust heuristics, particularly under conditions of"
[^d11]: arxiv-2512-12348 — "the type of health question did not significantly affect trust, alone or in interaction with label and source."
[^d12]: arxiv-2512-12348 — "We also observed no significant difference in trust between human-labeled"
[^d13]: arxiv-2512-12348 — "with an average trust score for information labeled as from human professionals of 4.04"
