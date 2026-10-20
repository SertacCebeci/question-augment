---
description: "A model can read a figure's values yet fail to interpret the symbolic rules the figure encodes; the CSAT study names this a Perception-Cognition Gap, separate from misreading numbers."
aliases: ["Perception-Cognition Gap", "schematic misinterpretation", "symbolic-meaning failure", "perception-interpretation gap"]
sources: ["arxiv-2512-15298"]
---
# Perception-cognition gap

A multimodal model can take in the visual content of a figure and still fail to use it. The Korean CSAT study separates two perception failures that look alike from outside. One is reading quantities: misreading values on an x-y graph. The other is interpreting what a figure's marks stand for: the paper distinguishes "misreading quantitative values in x-y graphs and cases of failing to interpret symbolic rules in" schematic diagrams or atypical figures.[^c1] The second is the gap. The abstract names it a "Perception-Cognition Gap" in which models "failed to interpret symbolic meanings in" schematic diagrams "despite recognizing visual data".[^c2][^c3] In the error table, one example is a model that "Failed to interpret the rules of an atypical schematic" figure showing changes in typhoon wind direction.

The mechanism the authors propose is a broken link between recognition and concept, not a wrong reading. They describe the failure to interpret a diagram's symbolic meaning as indicating "a severed cognitive bridge connecting recognized information to scientific concepts," which they set against "simple visual errors."[^c4] The model has the data in view; what is missing is the step that maps a symbol onto the rule it carries. A question whose answer depends on reading a value and a question whose answer depends on reading a convention encoded in a symbol are, on this account, different tests, even when both sit on the same figure. That difference is the material a question-writer or answer-checker would need to see.

The measurement is a coding of wrong answers, not a rate. The authors took the 36 incorrect answers from the condition in which the test was transcribed as text and only the figures were shown, so OCR errors were removed. Even there, perception errors were "the dominant cause of failure, accounting for 43.06% of total errors."[^c5] Within that share, the schematic part (1.2) carried 6.5 cases against 9 for quantitative misreading.[^c6] So interpretation of symbols is a large part of the perception failures, though not the larger part. The authors then propose that "atypical" schematic items could probe the gap, but they did not test that proposal.[^c7]

## Limits

- The counts come from one exam (Earth Science I), three models, and one experimental condition. The authors state the limit: the study "analyzed three specific LLMs and a single exam subject."[^c8]
- The categories were built by an AI-assisted thematic analysis, with a human making the final decisions. Multi-error answers were split, each error counted as 0.5.[^c9] The text says inter-coder reliability was "secured by requesting peer validation of the final classification"[^c10]; the sections read give no agreement statistic.
- The label is assigned from the written output. A missed symbol can be a cognition failure or a failure to extract the figure at all, and output coding cannot always tell them apart. The distinction the paper draws between 1.1 and 1.2 is by content of the figure, not by where inside the model the failure happens (my inference).
- The paper does not compare with human students. Its own future-work section says it is "necessary to precisely determine whether human students also exhibit" the discrepancy patterns.[^c11] Whether the gap is specific to models is therefore open.
- The "AI-resistant" use the authors draw from the gap is their proposal, not a result. This note records the gap; it does not claim any item design avoids it.

## Related

- [[perception-substitution-gap]] — the other perception measurement: replacing the image with a text rendering measures the cost of extracting information from the picture. The symbol-interpretation failure is what can remain after extraction succeeds; a text substitution of a schematic would still require that interpretation step (my inference, not tested).
- [[definition-application-gap]] — the same split on the concept side: a correct recitation or computation that does not govern the answer.

[^c1]: arxiv-2512-15298 — "misreading quantitative values in x-y graphs and cases of failing to interpret symbolic rules in"
[^c2]: arxiv-2512-15298 — "where models failed to interpret symbolic meanings in"
[^c3]: arxiv-2512-15298 — "schematic diagrams despite recognizing visual data"
[^c4]: arxiv-2512-15298 — "cognitive bridge connecting recognized information to scientific concepts"
[^c5]: arxiv-2512-15298 — "dominant cause of failure, accounting for 43.06% of total errors"
[^c6]: arxiv-2512-15298 — "interpreting symbolic meanings (1.2: 6.5 cases)"
[^c7]: arxiv-2512-15298 — "educators and assessment experts can actively utilize atypical"
[^c8]: arxiv-2512-15298 — "analyzed three specific LLMs and a single exam subject"
[^c9]: arxiv-2512-15298 — "error was counted as 0.5."
[^c10]: arxiv-2512-15298 — "requesting peer validation of the final classification"
[^c11]: arxiv-2512-15298 — "it is necessary to precisely determine whether human students also exhibit"
