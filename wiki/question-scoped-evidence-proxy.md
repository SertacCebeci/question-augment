---
description: "A video the judge cannot read is replaced by a text layer of atomic facts scoped to each question; answers are checked against those facts, not against the video."
aliases: ["recap-derived fact layer", "question-scoped fact grounding", "text proxy for video evidence"]
sources: ["doi-10-48550-arxiv-2601-02536"]
---
# Question-scoped evidence proxy

When the evidence for an answer is a video, a language-model judge has no direct way to check a claim against it. The MovieRecapsQA paper builds a text stand-in instead. A film's recap summary, a voiceover that narrates key clips, is divided into segments; atomic facts are extracted from each segment, and each question is tied to the facts of its own segment.[^q1] The authors state the reason for the detour: "using the full video as “context” for a judge is computationally expensive and imprecise," and the model "would have to parse complex, multimodal signals just to find the relevant information for answer grounding."[^q2]

The layer is made of short propositions. "Each atomic fact is a short, standalone proposition about the movie," written "so that its truth can be directly verified from the recap."[^q3] For each question the judge receives the model's claims, the question's facts and the subtitles of the segment. It returns integer scores from 0 to 5 on factuality, meaning whether the claims are supported or contradicted by the facts, and on relevance, meaning whether the answer addresses the question without unsupported content.[^q4] The authors call the result "a compact, verifiable representation of the video content."[^q5] The judge is scored against the facts and not against a reference answer, so the metric is "independent of how any particular reference answer is formulated."[^q6]

Two things are scoped. The facts are scoped to a segment, so the judge reads a few dozen propositions rather than an hour of film. And the facts are scoped to a question, so a claim is judged only on the part of the source that bears on what was asked. The construction is what makes the proxy usable; the claim-against-evidence check itself is the familiar one (see [[supported-faithfulness-score]]).

In the paper's own comparison the proxy is the only measure that spreads the models. Semantic metrics "show virtually no discrimination across models."[^q7] Reference-based judges rate some models at or above the average human, which the authors read as inflation.[^q8] The factuality of the reference-free metric ranges from about 3 to 4 on its 0 to 5 scale for the seven models, against about 4 for the average human.[^q9] The paper states the spread: "our reference-free metrics produce a wider and more meaningful spread."[^q10]

## Limits

- The proxy is only as good as its extraction. Facts come from GPT-4.1 prompting, and "All dataset construction steps are performed using GPT-4.1."[^q11] A fact the extraction misses cannot be counted as missing, and a wrong fact is treated as the truth the judge checks against. The parts of the paper I read report no error rate for the fact layer. That absence is my observation, not a result.
- The recap is a voiceover, not the film. A claim that is true of the video but absent from the recap is scored as unsupported. My inference, not something the paper tests.
- The judge is GPT-4.1 mini, chosen for cost. The authors say they "verified that GPT4.1 mini produces scores comparable to GPT-4.1 on our evaluation dimensions."[^q12] That check is on the scores' agreement with another model, not on agreement with truth.
- The human-alignment claim rests on a small sample: "We randomly sampled 118 questions from our dataset" for the human study.[^q13]
- One domain (60 films, recap videos from YouTube). Whether the same layer works for other video sources is untested here.

## Related

- [[supported-faithfulness-score]] — the same claim-against-evidence check, where the evidence is given rather than built per question
- [[reference-less-source-alignment]] — the other reference-free route, which aligns triplets of a text source instead of judging extracted facts with a language model
- [[weighted-nugget-recall]] — the reference-based counterpart, scoring against a fixed set of facts
- [[text-prior-over-visual-evidence]] — the proxy is text, and the same benchmark finds text priors shaping answers; a text-only check of a visual answer can share that bias (my inference)

[^q1]: doi-10-48550-arxiv-2601-02536 — "we divide each RecapSummary into segments and use prompting to extract"
[^q2]: doi-10-48550-arxiv-2601-02536 — "computationally expensive and imprecise"
[^q3]: doi-10-48550-arxiv-2601-02536 — "short, standalone proposition about the movie"
[^q4]: doi-10-48550-arxiv-2601-02536 — "response is factually grounded in the video content"
[^q5]: doi-10-48550-arxiv-2601-02536 — "representation of the video content"
[^q6]: doi-10-48550-arxiv-2601-02536 — "independent of how any particular reference answer is formulated"
[^q7]: doi-10-48550-arxiv-2601-02536 — "Semantic metrics show virtually no discrimination across models"
[^q8]: doi-10-48550-arxiv-2601-02536 — "reference-based judges inflate"
[^q9]: doi-10-48550-arxiv-2601-02536
[^q10]: doi-10-48550-arxiv-2601-02536 — "In contrast to both prior metric families, our reference-free metrics produce a wider and"
[^q11]: doi-10-48550-arxiv-2601-02536 — "performed using GPT-4.1"
[^q12]: doi-10-48550-arxiv-2601-02536 — "We verified that GPT4.1 mini produces scores comparable to GPT-4.1 on our"
[^q13]: doi-10-48550-arxiv-2601-02536 — "We randomly sampled 118 questions from our dataset"
