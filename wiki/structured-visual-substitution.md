---
description: "Adding machine-readable encodings of a chemical diagram beside its pixels, not in place of them, raises a model's olympiad score, and the gap is read as the cost of perception."
aliases: ["structured visual enhancement", "SVE", "machine-readable visual guidance", "symbolic visual guidance"]
sources: ["arxiv-2511-16205"]
---
# Structured visual substitution

A multimodal model that answers a question about a diagram can fail in two places: it can misread the picture, or it can reason badly once the picture has been read correctly. Structured visual enhancement (SVE), a diagnostic in the ChemO benchmark for olympiad chemistry, separates the two by adding a second input rather than removing the first. Each visual element of a problem is turned into a symbolic form by specialized tools. A molecular drawing becomes a SMILES or InChI string through optical chemical structure recognition.[^c1] A reaction scheme becomes a template of "plates with reagents, conditions, and stoichiometry".[^c2] A mechanism becomes "steps with explicit electron flow annotations".[^c3] The model then answers in one of two settings: the original text and raw images, or the same problem with these encodings supplied as well.[^c4]

The device works by giving the model a route around its own perception. The authors' hypothesis is that visual parsing "may lag behind" chemical reasoning, so that machine-readable encodings "could bypass the visual interpretation step" and show the chemistry the model can do once the picture is already read.[^c5][^c6] The difference between the two settings is then read as the share of the score lost to perception. The comparison lets the authors "isolate the contribution of visual interpretation versus chemical reasoning capabilities."[^c7]

What was measured: four reasoning multimodal models were scored on ChemO, built from the 2025 International Chemistry Olympiad theory examination.[^c8] Its problems run from sesquiterpene ozonolysis to thiamine-dependent enzyme pathways, so the set is a spread of chemistry subfields rather than one diagram type.[^c9] Adding the encodings helped across the board: SVE "improves both normalized rubric-based scores and similarity scores," with the largest gains on visually intensive problems.[^c10] For Gemini-2.5 Pro on one multi-part problem, the normalized score went from 13.3 to 19.0.[^c11] In the combined system, Gemini-2.5 Pro reached "75.4 with MAS alone, 80.3 with SVE alone" and, with both, "93.6 with SVE&MAS".[^c12] The authors conclude that "visual parsing is a primary bottleneck".[^c13]

## Limits

- The encodings add content, not only a channel. The symbolic form also carries parsed structure, such as reagents, conditions and step order, that the solver would otherwise have to infer. A gain shows that the encoded input helps; it does not by itself show that the model's perception was the cause, since the encoding also removes some of the reasoning the solver must do. The text I read does not separate the two (my inference).
- The encodings are "tool-generated and manually verified for accuracy."[^c14] The enhanced setting therefore includes human correction of the perception input. The gap it measures is the value of a checked encoding, not of a fully automatic pipeline.
- The evidence is one olympiad paper, four models, and a normalized rubric score. I did not find variance or confidence intervals in the sections read. "A primary bottleneck" is a claim about this benchmark, not about diagrams in general.
- Reading a figure's values is not the same as interpreting the rules it encodes; a model can pass the first and fail the second ([[perception-cognition-gap]]). An encoding that supplies the values does not establish that the rules are then read correctly.
- The authors frame SVE as a diagnostic. The work does not show that supplying encodings is a practical route to better scores on an unseen exam, where no expert has checked the encodings.

## Related

- [[perception-logic-decoupling]] — separates perception from reasoning inside one model's own chain, by having the model emit its perception first; SVE separates them by supplying the perception from outside.
- [[perception-cognition-gap]] — the figure-reading failure this diagnostic can be confused with: values versus rules.
- [[perception-step-faithfulness]] — scores a model's own perception claims against the image; SVE removes those claims from the loop instead.
- [[structured-motion-serialization]] — the same device for video: text serialization beside the question, without a diagnostic reading.
- [[answer-type-verifiability]] — the same benchmark's reformulation makes the answer machine-gradable; SVE makes the input machine-readable.

[^c1]: arxiv-2511-16205 — "Converted to SMILES or InChI"
[^c2]: arxiv-2511-16205 — "plates with reagents, conditions, and stoichiometry"
[^c3]: arxiv-2511-16205 — "steps with explicit electron flow annotations"
[^c4]: arxiv-2511-16205 — "Problems PAER + G where models additionally receive"
[^c5]: arxiv-2511-16205 — "parsing capabilities may lag behind their chemical reasoning abilities"
[^c6]: arxiv-2511-16205 — "could bypass the visual interpretation step"
[^c7]: arxiv-2511-16205 — "we can isolate the contribution of visual interpretation versus chemical reasoning capabilities"
[^c8]: arxiv-2511-16205 — "We evaluate four reasoning MLLMs"
[^c9]: arxiv-2511-16205 — "Thiamine-dependent enzyme pathways"
[^c10]: arxiv-2511-16205 — "improves both normalized rubric-based scores and similarity scores"
[^c11]: arxiv-2511-16205 — "Gemini-2.5 Pro on P3 improves from 13.3 to 19.0 in normalized score"
[^c12]: arxiv-2511-16205 — "75.4 with MAS alone, 80.3 with SVE alone"
[^c13]: arxiv-2511-16205 — "visual parsing is a primary bottleneck"
[^c14]: arxiv-2511-16205 — "representations are tool-generated and manually verified for"
