---
description: "Standard BLEU-4 scores an exact match of a short answer below 1 because its higher-order precisions are undefined; truncating the n-gram order to the answer length fixes that."
aliases: ["short-form BLEU", "length-aware BLEU", "dynamic n-gram weight BLEU"]
sources: ["arxiv-2512-07478"]
---
# Length-truncated BLEU

Standard BLEU averages modified n-gram precisions up to a fixed order, with a brevity penalty for candidates shorter than the reference. The paper writes it with "where N = 4, pn is the modified n-gram precision".[^c7] The trouble sits at the short end. A candidate of fewer than four tokens has no 3-grams or 4-grams to count, so the higher-order precisions are undefined, and the product cannot reach 1 even when every available n-gram matches. The paper's claim is direct: "even an exact match results in BLEU < 1 due to undefined higher-order n-gram precisions."[^c1]

The consequence it draws is that the artifact lands on correct answers and tilts the model's output: "This artificially penalizes short answers and biases the model toward" generating longer responses.[^c2] Used as a reward rather than a report, that is a direct incentive to lengthen answers, not only a scoring quirk (my inference from the paper's framing).

The fix changes which orders count, not how matches are found. Let max_n = min(N, c), where c is the candidate length. Only the first max_n orders get weight, each 1/max_n, and higher orders get zero. The paper says this rule "dynamically adjusts the n-gram weights wn according to the prediction length c."[^c3] An exact match of a short answer then reaches the top score: "achieve BLEU = 1, avoiding unintended reward degradation."[^c4] The precisions themselves are unchanged. The score is still a count of overlapping n-grams, only averaged over the orders the answer can actually have.

In Progressive Reward Shaping this length-truncated score is the answer term for short-form QA, where the authors replace the binary exact-match reward: "we design a denser reward based on BLEU".[^c5] The denser reward is therefore a surface-overlap reward with a length correction, not a graded judgment of meaning.

## Limits

- The paper establishes the scale fact: the modified score equals 1 on an exact match. Whether it trains better than exact match is a claim about the experiments, which I did not read in full.
- The fix does not change what counts as a match. A correct paraphrase of a short answer still shares few n-grams with the reference and scores low (my inference).
- The paper uses n-gram scores only for short answers. For long answers it names the opposite risk: an LLM judge is added for "scoring to prevent reward hacking."[^c6] The length correction does not make n-gram rewards safe for long text; it removes one artifact in the short case.
- At one token only unigram precision and the brevity penalty remain, so the score rests on a single n-gram order (my inference from the weight rule).
- The text I read does not say how length is counted (tokens, words or characters), so the threshold for "short" is not pinned down.

## Related

- [[three-test-metric-validity-audit]] — lexical metrics such as BLEU shift under rephrasing; the length correction does not address that sensitivity.
- [[staged-clarification-reward-pipeline]] — another reward assembled from cheap component scores, there used as sequential gates rather than one blended score.

[^c1]: arxiv-2512-07478 — "even an exact match results in BLEU < 1"
[^c2]: arxiv-2512-07478 — "This artificially penalizes short answers and biases the model toward"
[^c3]: arxiv-2512-07478 — "which dynamically adjusts the n-gram weights wn according to the prediction length c."
[^c4]: arxiv-2512-07478 — "achieve BLEU = 1, avoiding unintended reward degradation."
[^c5]: arxiv-2512-07478 — "we design a denser reward based on BLEU"
[^c6]: arxiv-2512-07478 — "scoring to prevent reward hacking"
[^c7]: arxiv-2512-07478 — "where N = 4, pn is the modified n-gram precision"
