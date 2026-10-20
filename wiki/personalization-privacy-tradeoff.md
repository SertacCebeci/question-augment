---
description: "Across 19 LLMs, more personalized responses tended to disclose more personal information; some models were both personalized and privacy-aware, so the trade-off is observed, not forced."
aliases: ["privacy-personalization trade-off", "privacy cost of personalization", "personalization versus privacy"]
sources: ["doi-10-48550-arxiv-2608-05246"]
---
# Personalization-privacy trade-off

A personalized response uses a user's history, and a response that uses more of that history can also expose more of it. LUNAR scores each personalized answer twice: once for personalization (coverage and depth against a rubric), and once for privacy, which "assesses inappropriate disclosure or use of personal information, capturing the privacy cost of personalization."[^c1]

Plotted across models, the two scores move together in a rough way. The authors' reading is that "models with lower personalization scores tend to preserve privacy better, while highly personalized models often fall into the aggressive region with lower privacy protection."[^c2] The abstract gives the same cost in one line: "stronger personalization can come at the cost of privacy protection."[^c3] Four models land in the aggressive region, high personalization and low privacy, among them Gemini Flash and DeepSeek-V4-Flash.

The trade-off is a tendency across systems, not a bound inside any one of them. Some models sit in the other corner, high personalization and high privacy, and the authors conclude that "strong personalization does not inevitably compromise privacy."[^c4] So the measured fact is that the two can be separated in practice, and that many of the tested models did not separate them.

Mechanically, the privacy judgment is made per response: a single personalized answer is rated on its own, independent of the others, and the privacy figure is reported under the Full Context setting, where the model sees the whole log.[^c5] So the score reflects how a model's answer uses the full history, not a retrieval or memory design. My inference, not stated by the paper: the evidence that lifts personalization (see [[cross-domain-evidence-integration]]) is the same personal material a response can over-disclose, and the results do not separate the two.

## Limits

- The privacy score is one LLM judge rating each response on a 1–5 scale for privacy offense, with gpt-5.1 at temperature 0.[^c6] Its agreement with human raters on privacy protection was 71.1%, lower than the 76.6% for the personalization score, on a subset of items.[^c7]
- The trade-off is a correlation across 19 models at one setting. It does not show that lowering a model's personalization would lower its privacy offense, and no intervention that cuts privacy offense while keeping personalization is tested.
- Privacy is judged on single responses against a synthetic log. Real disclosure risk depends on who reads the answer and what is already known to them, and none of that is modeled.
- The paper names one Pareto-optimal model (Kimi-K2.6) from these 19. It is not a general recommendation, and the paper gives no method for reaching that corner by design.

## Related

- [[cross-domain-evidence-integration]] — the evidence that improves personalization is also what the privacy score penalizes when it is misused.
- [[intent-aligned-cross-session-retrieval]] — retained cross-session histories raise privacy and consent problems in deployment; LUNAR scores the response side of that cost, not the storage side.
- [[event-level-zcdp-histogram-release]] — a formal differential-privacy guarantee for a released statistic; LUNAR's privacy is an LLM-judged offense score with no formal bound, a different object.

[^c1]: doi-10-48550-arxiv-2608-05246 — "assesses inappropriate disclosure or use of personal information, capturing the privacy cost of personalization"
[^c2]: doi-10-48550-arxiv-2608-05246 — "models with lower personalization scores tend to preserve privacy better, while highly personalized models often fall into the aggressive region with lower privacy protection"
[^c3]: doi-10-48550-arxiv-2608-05246 — "stronger personalization can come at the cost of privacy protection"
[^c4]: doi-10-48550-arxiv-2608-05246 — "strong personalization does not inevitably compromise privacy"
[^c5]: doi-10-48550-arxiv-2608-05246 — "the Full Context setting on a 1–5 scale (higher scores indicate stronger privacy protection)"
[^c6]: doi-10-48550-arxiv-2608-05246 — "rating each personalized response on a 1–5 scale for privacy offense"
[^c7]: doi-10-48550-arxiv-2608-05246 — "agreement reaches 76.6%, and 71.1% for personalization score (avg.) and privacy protection score, respectively"
