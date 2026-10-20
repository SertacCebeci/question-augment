---
description: "When two retrieved contexts conflict, LLMs consistently favor institution-attributed facts (government, newspaper) over person or social-media ones, with transitive rankings shared across models."
aliases: ["source preference under knowledge conflict", "LLM credibility hierarchy"]
sources: ["arxiv-2601-03746"]
---
# Source credibility hierarchy in knowledge conflicts

In a controlled setup, two equally plausible tables about the same entity disagree, and each is attributed to a synthetic source (government, newspaper, social-media user, or person). Message plausibility is held equal, so only the source label varies. The study measures a source-preference score from answer probabilities across 13 open-weight LLMs.[^c1]

Findings: every model prefers corroborated (attributed) information over unattributed information. When both sides carry sources of different types, preferences are strictly transitive, and model rankings agree strongly (average Kendall's W of 0.74). Eleven of 13 models rank both institutional source types above both individual ones.[^c2] Within-type cues (popularity such as circulation or followers) also shift preference toward popular sources.[^c3] The authors frame this with human credibility research: presumed credibility (assumptions about a source type) versus reputed credibility (third-party signals such as popularity).

So an answerer given conflicting evidence does not weigh it neutrally; a source label acts as a prior that decides the winner. For an asker building a context, who the information is attributed to is itself an input to the answer. (This sentence is my inference from the finding.)

## Limits

English only, open-weight models only, one synthetic table-conflict task, so transfer to free-text documents or closed models is untested. Synthetic sources avoid real-world bias but may not reflect cues in real documents. Preference is not accuracy: the paper does not show that institutions are more often right. The hierarchy is also fragile: see repetition-bias-overrides-source-credibility.

## Related

- [[institutional-authority-halo]] — a citation-side observation of the same institution-over-individual tilt, in a deployed system.
- repetition-bias-overrides-source-credibility — the same preferences can be reversed by repeating content.

[^c1]: arxiv-2601-03746 — "we find that LLMs prefer institutionallycorroborated information"
[^c2]: arxiv-2601-03746 — "11 of 13 models prefer both institutional sources"
[^c3]: arxiv-2601-03746 — "Models prefer popular sources."
