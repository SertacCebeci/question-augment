---
description: "A symbol carries a secondary, conventional meaning added to what it shows; a feature that expresses emotion through its primary content is not one, though VLMs often call it a symbol."
aliases: ["emotion symbol", "conventionalized symbol", "secondary-meaning sign"]
sources: ["arxiv-2511-22929", "arxiv-2511-21752"]
---
# Conventional symbol versus expressive feature

A symbol, in the sense the case study uses, is a sign with a meaning added on top of what it depicts. The paper takes the definition from Cassirer: symbols are "signs with a secondary conventionalized level of meaning."[^c1] A heart stands for love because a culture has agreed that it does; the depicted object is not itself the emotion. The contrast is with features that express emotion through what they show directly: a raised mouth, a drooping posture, a dark palette. Those carry the emotion as part of their primary meaning.

The paper draws the line on that basis. Its objection to the models' answers is that the emotional content of a face or a palette "is part of the primary meaning and not added through a secondary conventionalized relationship," so calling it a symbol is a category error.[^c2] The authors say of such cases: "these are not genuine (emotion) symbols, since".[^c3] The line matters for the question asked. "Does this artwork use a symbol to visualize emotion, and if it does, how?" asks for a secondary, learned reading; a model that answers from the expressive features answers a different question while using the same word.

The models do both things. Where a conventional symbol is clearly present, they tend to find it: "clear symbols are present in the images, they are often recognized", with the book read as wisdom and the skull as mortality.[^c4] Where the image lacks one, they describe expressive features as symbols. The paper says this happens "Particularly in less symbolic images", with facial expressions, postures, the colour palette and the contrast of light and shadow as the usual candidates.[^c5] The verb "symbolize" then means little more than "express".

A third group is the dubious one. The models identify symbols "that are not conventionalized and therefore somewhat" doubtful, such as a figure in water read as loneliness.[^c6] The paper also reports the reverse error: "some clear symbols" such as a dagger are "overlooked when they do not fit a simple" reading.[^c7]

The distinction has a practical use for asking. A question about symbols that does not separate the two routes will be answered by whichever route the model finds easier, and a yes will be counted as a symbol reading when it is an expressive one. My inference, not the paper's: a question that names the conventional secondary meaning, or asks which cultural code the image uses, asks for the thing the definition describes.

## Limits

- The classification is the authors'. The labels "not genuine" and "not conventionalized" are their judgments, and the paper states that its quality assessments "largely correspond, so the results" are a consensus between them.[^c8] No agreement statistic is given in the sections read.
- Symbol items are one question of eight, over 38 images. The class is small in this text.
- The definition is philosophical (Cassirer, 1923), not an operational test. The text does not show how to decide, for a new image, whether a motif is conventional or expressive, beyond the authors' own reading.
- Whether specifying the distinction in a prompt reduces the over-reading is not tested. The paper reports the error, not an intervention.
- The text's own term "emotion symbol" is narrower than symbol in semiotics; transfer of the notion to other fields is not checked here.

## Related

- [[concrete-cue-grounding]] — expressive features are read reliably when they are concrete; the symbol errors are where the cue is a convention rather than a visible object.
- [[support-skew-in-claim-verification]] — the same affirmative default, here pushing a verifier toward finding a symbol or a support where the stricter reading would not.
- [[perception-cognition-gap]] — a model can read a figure's values yet fail to interpret the symbolic rules it encodes; a related split between seeing a mark and reading its convention.
- [[alias-label-remapping]] — the conventional secondary meaning of a colour used as a label: a green or red label carries polarity without being taught, which the paper offers as the reason one alias pair recovers accuracy and others do not.[^c9]

[^c1]: arxiv-2511-22929 — "conventionalized level of meaning"
[^c2]: arxiv-2511-22929 — "meaning and not added through a secondary conventionalized relationship"
[^c3]: arxiv-2511-22929 — "these are not genuine (emotion) symbols, since"
[^c4]: arxiv-2511-22929 — "clear symbols are present in the images, they are often recognized"
[^c5]: arxiv-2511-22929 — "Particularly in less symbolic images, the models"
[^c6]: arxiv-2511-22929 — "are not conventionalized and therefore somewhat"
[^c7]: arxiv-2511-22929 — "are overlooked when they do not fit a simple"
[^c8]: arxiv-2511-22929 — "The quality assessments largely correspond, so the results"
[^c9]: arxiv-2511-21752 — "the conventional symbolic meanings of green (positive, permitted, good) and red (negative, prohibited, bad)"
