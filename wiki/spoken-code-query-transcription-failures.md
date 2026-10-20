---
description: "Speech recognition of spoken code questions fails in recurring ways (phonetic drift, split identifiers, lost symbols); these degrade code QA and retrieval, and LLM post-editing recovers part of it."
aliases: ["ASR failure modes for code speech", "code-aware ASR refinement", "speech-to-text errors in code understanding"]
sources: ["arxiv-2601-15339"]
---
# Spoken code-query transcription failures

When a question about code is spoken and then transcribed, the recognizer sees a mix of natural language and tokens it has no language prior for. The work (Hindi, Bengali, Tamil, Gujarati and English speakers; CodeSearchNet, CoRNStack, CodeQA) lists the recurring ways this goes wrong, and measures what the damage costs a downstream code model.

## The failure modes

The authors' qualitative taxonomy for the speech-to-text stage:

- Phonetic drift: code tokens in regional accents are heard as other words ("async" becomes "a sink").[^c1]
- Identifier splitting: camelCase or snake_case names are "split, omitted, or substituted entirely", for example getUserInfo heard as "get use run foe".[^c2]
- Keyword ambiguity: words such as "is", "not", "in" are read by language priors, not by syntactic role.[^c3]
- Symbol loss: spoken operators ("equal equal", "not equal") are rarely kept as == or !=.[^c4]
- Identifier recall failure: user-defined names are replaced by semantically irrelevant tokens.[^c5]

Translation and speech synthesis add their own errors, for instance a grammar "over-correction" that turns "sort the data" into "It is required to sort the data", changing a request into a necessity.[^c6]

## Why plain WER under-describes it

Word error rate treats all substitutions alike. The authors add phoneme error rate and a feature-weighted phonetic edit distance, arguing that outputs "phonetically close but syntactically incorrect" (dropped underscores, split camelCase) look small acoustically yet invalidate a query for a code model. A low phonetic distance suggests a post-correction step can repair the error; a high one suggests the term lies outside the recognizer's phonetic range.[^c7] The recoverable/unrecoverable split is the authors' argument, not separately validated.

## What it costs and what refinement recovers

In code retrieval with one embedding model, original queries gave 92% recall and 87.2% MRR at k=5; ASR-transcribed queries dropped this to 87% and 81.58%; code-aware LLM refinement of the transcript restored 90% and 83.78%.[^c8] Averaged over languages, refinement (GPT-4o-mini with a code-aware prompt) cut WER by 20.95%, PER by 28.85% and WFED by 33.36%.[^c9] Degradation is larger in the lower-resource languages (Tamil, Gujarati).[^c10] Refinement is partial: even refined queries stay below the clean-text numbers.

## Limits

- Retrieval and QA were evaluated on English versions of the datasets; the speech for other languages was synthesized and transcribed, so this is not real learner speech.
- One refinement model (GPT-4o-mini) was chosen after smaller open models failed on Indic segments; generality across refiners is shown only partly.
- The taxonomy is qualitative; frequencies of each failure mode are not reported in the parts read.
- The 53-student survey motivates the setting but does not test answer quality.
- Whether the refiner could invent plausible identifiers that were not spoken was not examined here.

## Related

- [[structural-amplification-of-query-entity-corruption]] — the same upstream corruption of entities, studied in multi-hop QA; surface repair there recovered little
- [[agentic-asr]] — recognition that repairs before the answerer acts
- [[clarification-request]] — asking back as the alternative to silently correcting
- [[communication-accident]] — transcription errors as a channel failure the asker cannot see

[^c1]: arxiv-2601-15339 — "English code tokens spoken in regional accents often deviate phonetically."
[^c2]: arxiv-2601-15339 — "are often split, omitted, or substituted entirely."
[^c3]: arxiv-2601-15339 — "are interpreted according to language priors rather than"
[^c4]: arxiv-2601-15339 — "Spoken symbolic operators such as “equal"
[^c5]: arxiv-2601-15339 — "are substituted with semantically irrelevant tokens,"
[^c6]: arxiv-2601-15339 — "This Changes intent from a simple task to a necessity."
[^c7]: arxiv-2601-15339 — "ASR systems frequently produce outputs"
[^c8]: arxiv-2601-15339 — "performance drops notably to 87% Recall and 81.58% MRR"
[^c9]: arxiv-2601-15339 — "On average, we observe a 20.95% reduction in"
[^c10]: arxiv-2601-15339 — "Performance degradation is pronounced in low-resource Indic languages like Tamil and Gujarati"
