---
description: "Topic difficulty read from outcomes, not complexity: the share of posts or issues left without an answer or closure, and the median hours to resolve, both right-censored and indirect."
aliases: ["unresolved rate", "median resolution time", "time to accepted answer", "observed difficulty"]
sources: ["doi-10-48550-arxiv-2607-19621", "arxiv-2512-19727"]
---
# Observed resolution difficulty

Difficulty can be measured without touching the problem itself, by reading what happened to the requests about it. The paper uses two outcome measures per topic, defined separately for each platform. On Stack Overflow, the first is "the percentage of posts in each topic without an accepted answer," and the second is the median time until an answer was accepted. On GitHub, the first is the share of issues and pull requests that remained unresolved, and the second is their median resolution time, computed as "the median resolution time, in hours, as the time between when" the artifact was opened and closed.[^c1][^c2]

The two measures can separate two different situations, and the paper reads them that way. A topic with a high unresolved share has requests that go unanswered or stay open, which the paper takes to indicate developers "may struggle to obtain sufficient support." A topic with few unresolved requests but very long resolution times has requests that do get closed, slowly, which the paper takes to indicate "deeply complex problems that require significant effort to resolve."[^c3] The figures show the split is real in the data. Several topics "exhibit high unresolved rates and long resolution times, suggesting shortcomings in tooling, documentation, and" debugging support.[^c4] A third pattern is the extreme: one federated-learning topic on GitHub has no unresolved issues at all, "In contrast, Federated Feature Engineering and SecureBoost Issues shows no unresolved issues," yet a median resolution time of about 1,650 hours.[^c5]

The mechanism that makes the measures informative is also what confounds them. The median is taken over resolved artifacts only, because open ones have no closing time; "Unresolved artifacts are right-censored because their eventual outcome and resolution time" is unknown, so "median resolution time is calculated only from resolved artifacts and" may understate what the open ones will eventually need.[^c6][^c7] This is the survival-analysis sense of censoring, borrowed without its estimator: the paper does not fit a survival curve, so the medians are conditional on resolution and the true time for slow topics is not recovered.

## Limits

- The paper says these are not complexity. "they do not directly measure the inherent technical" difficulty of a problem; they are "indirect indicators of observed resolution difficulty rather than direct measures of technical complexity."[^c8][^c9]
- An unanswered Stack Overflow question can reflect the asker, not the problem: "A Stack Overflow question may lack an accepted answer because the asker did not return to accept" a solution that was offered, or because the question was unclear or the topic drew little attention.[^c10]
- A GitHub artifact can stay open for reasons unrelated to difficulty: "a GitHub artifact may remain open because it has low priority, depends on external work," or lacks maintainer resources.[^c11] Closure is not success either: the paper notes that closure "does not necessarily" mean the problem was solved, since issues are closed as duplicates or invalid. The phrase it uses is "indicate that the reported problem was successfully resolved."[^c12]
- The observation window matters. A long time to resolution "may therefore reflect the state of a framework or community during a particular period rather" than a stable property of the topic.[^c13]
- Small topics are unstable. "Topic-level percentages and median resolution times may be less stable for topics containing relatively few artifacts."[^c14]
- The two platforms are not commensurable on these measures: the paper treats them "examined separately", so a topic cannot be ranked across Stack Overflow and GitHub on either number.[^c15]
- This note's inference, not the paper's: because the medians exclude open artifacts, the slowest topics are the ones where the reported time is most biased downward. The paper does not quantify this, and no sensitivity analysis is reported.

## Related

- how-why-what-intent — the intent split the paper reports alongside these outcomes; the two are kept separate in the analysis
- [[answer-avoidance-collapse]] — another rate of non-answers whose cause the rate alone cannot show: a fall in answered share can come from refusing more often rather than from worse answers
- [[right-censoring-recency-bias]] — the same one-sided censoring in launch-indexed lifetimes: recent cohorts look worse because their long-lived members have not ended yet, and the fix is to index by end time.[^c16]

[^c1]: doi-10-48550-arxiv-2607-19621 — "the percentage of posts in each topic without an accepted answer"
[^c2]: doi-10-48550-arxiv-2607-19621 — "We calculated the median resolution time, in hours, as the time between when"
[^c3]: doi-10-48550-arxiv-2607-19621 — "resolution times suggest deeply complex problems that require significant effort to resolve."
[^c4]: doi-10-48550-arxiv-2607-19621 — "exhibit high unresolved rates and long resolution times, suggesting shortcomings in tooling, documentation, and"
[^c5]: doi-10-48550-arxiv-2607-19621 — "In contrast, Federated Feature Engineering and SecureBoost Issues shows no unresolved issues"
[^c6]: doi-10-48550-arxiv-2607-19621 — "Unresolved artifacts are right-censored because their eventual outcome and resolution time"
[^c7]: doi-10-48550-arxiv-2607-19621 — "median resolution time is calculated only from resolved artifacts and"
[^c8]: doi-10-48550-arxiv-2607-19621 — "but they do not directly measure the inherent technical"
[^c9]: doi-10-48550-arxiv-2607-19621 — "However, these metrics are treated as indirect indicators of observed resolution difficulty rather than"
[^c10]: doi-10-48550-arxiv-2607-19621 — "A Stack Overflow question may lack an accepted answer because the asker did not return to accept"
[^c11]: doi-10-48550-arxiv-2607-19621 — "a GitHub artifact may remain open because it has low priority, depends on external work,"
[^c12]: doi-10-48550-arxiv-2607-19621 — "indicate that the reported problem was successfully resolved."
[^c13]: doi-10-48550-arxiv-2607-19621 — "time may therefore reflect the state of a framework or community during a particular period rather"
[^c14]: doi-10-48550-arxiv-2607-19621 — "Topic-level percentages and median resolution times may be less stable for topics containing relatively few artifacts."
[^c15]: doi-10-48550-arxiv-2607-19621 — "represent different resolution mechanisms and are therefore examined separately in RQ3."
[^c16]: arxiv-2512-19727 — "shows a downturn in recent years due to recency bias from right censoring"
