---
description: "Truncating a reference text in steps, factual accuracy holds until a breakpoint; the largest compression level still above a threshold (HOC) measures resilience to information loss."
aliases: ["HOC", "hallucination onset", "compression breakpoint", "breakpoint under information loss"]
sources: ["arxiv-2512-23850"]
---
# Hallucination onset compression

Give a model a reference text about a concept, cut the text to a prefix, and ask about the concept again. Repeat at several cut sizes. The quantity recorded is not whether the answer is right at one length but where, along the cut axis, factual accuracy gives way. The authors call that point hallucination onset compression: the largest compression level c at which the factual accuracy rate stays at or above a threshold θ, set to 0.70 (HOC = max{c | FAR(c) ≥ θ}).[^h1]

Compression is deterministic. The model receives the first W × (1 − c) characters of the reference text, so c = 0 is the full text and c = 1 is no text, leaving the model to rely on what it already knows.[^h2] Because the cut is at a character count and not at a sentence boundary, the model at c = 0.75 sees roughly a quarter of the text, and that prefix often ends mid-sentence.[^h13] The authors chose prefix truncation over summarisation on purpose: it is a reproducible, fixed form of load, not a rewritten text.

**Why a breakpoint and not a score.** A single answer at one context length cannot say where a model fails. The protocol is built to show "when (not just if) they fail."[^h3] The authors contrast HOC with binary pass/fail assessment: it reports "thresholds (HOC) rather than binary pass/fail assessment."[^h4] The transferable concept is this. Any capability measured under progressive removal of its support has a point at which it gives way, and that point, not the accuracy at one level, is the comparable quantity between models.

**What the breakpoint is read as.** The paper reads HOC as the break point of a checking component. It separates a semantic system that produces fluent text from an epistemic verifier that judges factual accuracy, and reports that "HOC captures V break-point while SAS remains stable," where SAS is a score for coherence and relevance regardless of truth.[^h5] On this reading, the same response can stay fluent after it has stopped being accurate, and the breakpoint marks where the two come apart. The authors are explicit that the decomposition is a description of behaviour: it is "behavioral and functional, not a claim about explicit neural modules."[^h6] The word verifier names a pattern in the scores, not a part of the network that was observed.

**Scale of the measurement.** The protocol was run over nine models, eight concepts from different fields, and five levels, c in {0.0, 0.25, 0.5, 0.75, 1.0}.[^h14][^h8] A composite index, Comprehension Integrity, multiplies HOC by a comprehension resilience term and divides by a dissociation term; the paper names it the "Comprehension Integrity (CI) metric."[^h7] The composite is the paper's own construction, and this note does not rely on it.

Inference, not from the paper: with five compression levels, HOC can take only five values, so its resolution is set by the grid as much as by the model.

## Limits

- **The threshold is a choice.** θ = 0.70 is the authors' default. Their footnote says a stricter θ = 0.80 gives "findings are qualitatively similar."[^h9] That is one alternative, not a sweep. The breakpoint moves with θ, and the paper does not report how far.
- **Prefix truncation is one compression.** The authors state that comparing truncation with other strategies is future work: "Future work may compare truncation against alternative" compression strategies such as sentence removal or extractive summarisation.[^h10] A cut can also remove the end of a definition, so the breakpoint may partly measure truncation artefacts rather than loss of the concept. This is an inference; the paper does not separate the two.
- **Eight concepts, one reference text each.** The domain check is an ANOVA, and the paper reports that it "confirms no significant domain stratification."[^h11] A non-significant test across eight domains does not show that breakpoints are equal across domains. It shows that this sample did not separate them.
- **The scores come from a jury.** Factual accuracy and coherence are scored by three LLM judges. The paper flags a family-overlap risk: "Jury family-bias note: The subject model set includes GPT-5 and Claude-Haiku-4-5, whose families" overlap with judge families.[^h12] A breakpoint is only as stable as the judging that locates it.
- **Behaviour, not mechanism.** Nothing here locates a verifier inside a model. The claim is about where a response curve bends, and about the paper's reading of that bend.
- **Not established here:** that the breakpoint predicts behaviour outside a text-cut setting, that it is the same for models in different families beyond the nine tested, or that the CI composite is the right way to combine it with other terms.

## Related

- [[presupposition-accommodation]] — a related failure: an answerer accepts a context it has not checked. Here the question is how far that acceptance survives the loss of the source text.
- [[cot-hallucination-trap]] — fluent but ungrounded output; the separation of coherence from accuracy under compression is the same dissociation in a different setting.
- [[detection-correction-gap]] — a model can detect a flawed claim without rejecting it; the protocol's fabrication step measures the detection side of that gap.
- [[medium-context-sweet-spot-for-numeric-prediction]] — context amount can help and then hurt, which is not the monotone loss a breakpoint presumes; the two readings should not be merged.

[^h1]: arxiv-2512-23850 — "Hallucination Onset Compression (HOC):"
[^h2]: arxiv-2512-23850 — "Compression is hard prefix truncation at the character level."
[^h3]: arxiv-2512-23850 — "revealing when (not just if) they fail."
[^h4]: arxiv-2512-23850 — "thresholds (HOC) rather than binary pass/fail assessment."
[^h5]: arxiv-2512-23850 — "HOC captures V break-point while SAS remains stable"
[^h6]: arxiv-2512-23850 — "this decomposition is behavioral and functional, not a claim"
[^h7]: arxiv-2512-23850 — "Comprehension Integrity (CI) metric"
[^h8]: arxiv-2512-23850 — "The DDFT protocol was executed for each model-concept pair across five levels"
[^h9]: arxiv-2512-23850 — "findings are qualitatively similar"
[^h10]: arxiv-2512-23850 — "Future work may compare truncation against alternative"
[^h11]: arxiv-2512-23850 — "ANOVA confirms no significant domain stratification"
[^h12]: arxiv-2512-23850 — "Jury family-bias note: The subject model set includes GPT-5 and Claude-Haiku-4-5, whose families"
[^h13]: arxiv-2512-23850 — "frequently producing mid-sentence"
[^h14]: arxiv-2512-23850 — "We evaluated 9 models"
