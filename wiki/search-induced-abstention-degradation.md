---
description: "Giving an LLM a search tool lifts accuracy on answerable questions but lowers its abstention on unanswerable ones, because retrieved text rarely says 'unknowable'; reasoning effort amplifies it."
aliases: ["over-searching", "over-searching in search-augmented LLMs", "search harms abstention"]
sources: ["arxiv-2601-05503", "arxiv-2512-23836", "doi-10-48550-arxiv-2609-37469"]
---
# Search-induced abstention degradation

Over-searching is the tendency of a search-augmented model to keep searching past the point where it already has the correct outcome.[^c1] Because the correct outcome for an unanswerable question is abstaining, extra search does not merely waste compute: it removes the right answer. The paper measures this on OverSearchQA, 1,188 queries balanced between answerable and unanswerable, in three unanswerable categories (answer unknown, false premise, underspecified context), with answerable twins drawn from similar embedding neighbourhoods and matched length so the effect is not a dataset artifact.[^c2]

## What was measured

- Across ten models, adding search raised answer accuracy by 24.0% on average and lowered abstention accuracy by 12.8%; the loss is largest on underspecified questions, where models hunt for evidence for a query that cannot be resolved.[^c3]
- With o4-mini, raising the allowed search turns from 0 to 19 gave an answer accuracy that rose early and plateaued while abstention accuracy fell steadily and cost rose.[^c4]
- Reasoning effort: low to high raised answer accuracy (74.1 to 74.6) and lowered abstention (46.6 to 45.4), while [[tokens-per-correctness]] rose from 517.1 to 1492.2.[^c5]
- Noisy retrieval: a noisy corpus gave 3.6x the cost of Wikipedia-Latest, yet the second-best abstention, so consistently poor retrieval may help models see unanswerability.[^c6]
- Evidence composition: with only negative evidence (documents indicating unanswerability) models abstain almost perfectly, but negative documents are only 13-22% of what is retrieved for unanswerable queries. The paper's reading is that corpora document what is known, so models take unknowability for inadequate search effort.[^c7]
- Multi-turn conversations amplify the effect, strongest when earlier context was answerable (stated in the paper's Figure 6 caption).[^c8]
- With search removed and the retrieved text fixed, the same failure appears on a window of irrelevant Wikipedia pages that holds no answer. Zero-shot, the model answers falsely on such windows: "model generates a false answer 54.3% of the time,"[^c10] and increasing the in-context examples from 0 to 8 gave "no significant improvement in either metric."[^c11] The paper's reading is that LLMs "force incorrect answers from irrelevant passages rather than" declining.[^c12] Set against the corpus-asymmetry account above, this is the same gap at window level; the link is my inference, not the paper's (see [[sequential-window-reading]]).
- Without any search tool, the same failure appears with the passages fixed: twelve generators told to reply unanswerable when the documents lack the answer "still answer 40.0% to 99.3% of the insufficient records," and refuse up to 29.7% of the sufficient ones; the authors' reading is that generators do not notice an evidence gap, so the check has to sit before generation.[^c13]

## Mitigations tried

Abstention-aware prompts, few-shot examples and a self-evaluation step gave an average abstention gain of 11.5 points; few-shot gave most but cost the most answer accuracy, self-evaluation was balanced but costlier. Inserting ten synthetic negative-evidence documents gave only 3.6% because they ranked poorly and were diluted.[^c9]

## Limits

The study is prompt-level and corpus-level only; no training-time fix was tested. The explanation that corpus asymmetry causes the bias is the authors' interpretation, supported by the evidence-balance table but not an intervention that succeeded. Correctness is scored by an LLM judge (84% alignment with humans). The default retriever is Wikipedia with E5-base and a 10-call cap. The reasoning-effort differences in answer and abstention accuracy are small; the cost difference is the large one.

## Related

- [[search-decision-boundary-misalignment]] — frames over-search as a mis-set stop threshold and trains it away
- [[tokens-per-correctness]] — the cost metric used to detect it
- [[hoprefusalbench]] — another benchmark of refusal under search
- [[knowledge-integration-decay]] — retrieved content failing to be integrated well

[^c1]: arxiv-2601-05503 — "We define over-searching as the tendency of models to continue searching beyond"
[^c2]: arxiv-2601-05503 — "we draw"
[^c3]: arxiv-2601-05503 — "boosting answer accuracy by an average of 24.0% while degrading abstention accuracy by"
[^c4]: arxiv-2601-05503 — "abstention accuracy drops with"
[^c5]: arxiv-2601-05503 — "TPC increases monotonically with reasoning effort"
[^c6]: arxiv-2601-05503 — "C5 also achieves the second-best abstention accuracy"
[^c7]: arxiv-2601-05503 — "negative documents comprise only 13-22% of retrieved content for unanswerable queries"
[^c8]: arxiv-2601-05503 — "Multi-turn conversations amplify over-searching behavior."
[^c9]: arxiv-2601-05503 — "achieving an average gain of 11.5"
[^c10]: arxiv-2512-23836 — "model generates a false answer 54.3% of the time,"
[^c11]: arxiv-2512-23836 — "increasing the number of shots yields no significant improvement in either metric."
[^c12]: arxiv-2512-23836 — "We find that LLMs tend to force incorrect answers from irrelevant passages rather than"
[^c13]: doi-10-48550-arxiv-2609-37469 — "still answer 40.0% to 99.3% of the insufficient records"
