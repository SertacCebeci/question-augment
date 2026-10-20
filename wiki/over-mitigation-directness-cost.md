---
description: "When a safety edit makes an answer generic or drifts off the question, readers prefer the unmitigated original, flaws and all, because it engaged the question they asked."
aliases: ["over-mitigation", "safety-induced evasion", "harm removal at the cost of relevance", "directness cost of mitigation"]
sources: ["arxiv-2512-01892"]
---
# Over-mitigation directness cost

A mitigator of an AI answer has two jobs that readers weigh separately: remove the harm, and keep the answer responsive to the prompt. The study this note rests on found that the two can trade off. When a mitigator edit "sometimes generalized away from the request", it produced "safe responses that diverge from addressing the question", and participants then preferred the original answer.[^c1][^c11] The reason given is that the original was preferred "even when imperfect", and "because it engaged the question".[^c2][^c12]

The codebook names the trade-off directly. Its code for "Sacrifice relevance while removing harms" is defined as "Safety edits that make the answer less responsive."[^c3] Over-mitigation is treated as a separate failure from harm removal. Participants penalized "Over-mitigation that reframed the claim, introduced unrelated content, or removed key information", and in some cases this "sometimes triggered a preference for the original".[^c4]

Relevance carried the most weight in the participants' reasoning. The authors write that "Relevance dominated decision-making", and that when an answer did not address the prompt, the other criteria became secondary.[^c5] The rule the authors draw from the interviews is that "When any of these came at the cost of directness, preferences shifted toward the original response."[^c6]

The average result is less severe than the cases. Across the sample, "Mitigated responses were chosen 63% of the time" on relevance, and the mitigated answer was preferred on most dimensions.[^c7][^c8] So the directness cost is a tail that appears in particular prompts, not a shift in the mean. A question with a clear factual answer, asked in a form the mitigator reads as sensitive, is where the paper's examples place it. The "Which is more prestigious: Harvard or Stanford?" prompt is one such example.[^c1]

The mechanism is simple to state. A harm-removal edit that is applied to the whole answer, not to the harmful span, can remove the content that answered the question. A reader who asked for a direct answer then sees a hedged or generic one and prefers the flawed original. The paper does not separate whether the cost comes from the removal itself or from the wording that replaces it.

## Limits

- The evidence for the directness cost is codebook coding of open survey and interview answers, with named participants as examples. The text read gives no rate at which an off-question mitigation occurred, so the size of the tail is unknown.
- The criteria are not cleanly separated by the participants. The paper notes that "Participants sometimes conflated faithfulness with relevance", so "relevance" in the coding may absorb some faithfulness judgments.[^c9]
- Preference is relative. Each comparison was between an original answer that contained harm and its mitigation. The study does not include a third option, a non-harmful answer that is both direct and safe, so it does not show that such an answer is achievable or what it looks like.
- The Phase 2 sample is six items, three per metric.[^c10] Single examples such as the Harvard and Stanford prompt carry weight they cannot bear alone.
- The effect is measured with human raters on one mitigator. Whether the cost grows with stronger mitigation, or with other harm categories, is not tested in the text read.

## Related

- [[wise-refusal]] — a refusal earns credit only when it engages the trap and names what is missing; generic caution does not count. The same direction, for refusals in a different setting
- [[relevance-completeness-divergence]] — topical relevance does not measure whether an answer is sufficient; this note adds that a mitigated answer can stay on topic and still stop answering (my inference from the codebook)
- revision-exposure-rating-drop — the same study finds that a revision is scored against the original shown beside it

[^c1]: arxiv-2512-01892 — "sometimes generalized away from the request"
[^c2]: arxiv-2512-01892 — "even when imperfect"
[^c11]: arxiv-2512-01892 — "yielding safe responses that diverge from addressing the question"
[^c12]: arxiv-2512-01892 — "because it engaged the question"
[^c3]: arxiv-2512-01892 — "Safety edits that make the answer less responsive."
[^c4]: arxiv-2512-01892 — "was penalized and sometimes triggered a preference for the original"
[^c5]: arxiv-2512-01892 — "Relevance dominated decision-making."
[^c6]: arxiv-2512-01892 — "When any of these came at the cost of directness, preferences shifted toward the original"
[^c7]: arxiv-2512-01892 — "Mitigated responses were chosen 63% of the time"
[^c8]: arxiv-2512-01892 — "Overall, the mitigated responses were preferred across most dimensions"
[^c9]: arxiv-2512-01892 — "Participants sometimes conflated faithfulness with relevance"
[^c10]: arxiv-2512-01892 — "In Phase 2 participants evaluated 6 samples"
