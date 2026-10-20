---
description: "Lifetimes indexed by start date look shorter for recent cohorts, because long-lived members have not yet ended; indexing by end time removes the one-sided downward drift."
aliases: ["recency bias from right censoring", "launch-year lifetime bias", "cohort right-censoring bias"]
sources: ["arxiv-2512-19727"]
---
# Right-censoring recency bias

When lifetimes are plotted against the date an item began, and only items that have already ended can report a lifetime, the most recent cohorts look worse than they are. A spacecraft launched last year that will run for thirty years has not failed yet, so it contributes nothing to the lifetime data for its launch year. Only the short-lived recent launches are in the sample. The average lifetime against launch year then falls at the right edge of the plot, even when every cohort is equally durable. The paper states the selection directly: "the more recent the launch dates, the shorter the lifetimes of the spacecraft that have failed and can thus contribute lifetime data."[^r1] It says the distortion runs one way, "by biasing lifetime estimates for recent launch dates downward."[^r2]

The paper shows the effect in its own data. Plotted by launch year, lifetimes fall sharply for recent years; plotted by failure year, the same lifetimes show no such downturn.[^r3] Its conclusion is that the drop is an artifact of the index, not a fact about the vessels: "This downward trend does not imply that newer vessels are less reliable."[^r4]

The mechanism is a selection on the outcome. Items with long lifetimes are the ones most likely to still be running, so they are the ones most likely to be missing from a recent cohort's sample. The sample is therefore not a random draw from the cohort, and a trend fitted to launch-indexed data carries the bias into any extrapolation to later launches. This is why a forecast of lifetimes by launch date can look like a decline in quality when only the observation window has moved.

The remedy the paper uses changes the index, not the data. It rewrites the lifetime relation as a function of end time, "into a function of the end time," where each completed lifetime is observed in full.[^r5] It fits that relation on the completed lifetimes, then maps the fitted relation back to launch time so that the output is still a prediction from launch date.[^r6] In the neural version, the failure-indexed model's predictions serve as training targets for a launch-indexed model, a transfer the paper describes as leveraging failure data "free from a critical source of bias inherent in launch time data."[^r7]

What transfers beyond spacecraft is the principle: when completion is conditioned on the outcome, model the outcome on the axis where completion is not conditioned on it, then translate back. The specific form the paper uses, an exponential trend with a doubling time, is a choice made for this data and is not part of the principle. (My inference; the paper does not claim it generalises.)

## Limits

- One domain. The correction is shown on spacecraft lifetimes. The paper itself names the data as the first limit: "One limitation of this study is the availability and scope of the data used."[^r8] Nothing here shows the same reindexing repairs a different censored outcome.
- The reindexed route is a chain. The paper notes that an alternative could avoid "training a second LSTM on the predicted lifetimes from the first LSTM, potentially reducing the associated errors."[^r9] The two-stage transfer can carry error from the first stage into the second.
- The index needs a defined end. The paper's failure time is the date a spacecraft "ends operation," which it admits "could end operation for another reason."[^r10] Where the end event is ambiguous, the end-time axis is ambiguous too.
- The method uses only completed lifetimes; it does not estimate the lifetimes of items still running. It avoids the bias by not using the censored observations, not by recovering them. (My inference from the design; the paper does not compare against a survival estimator, and I did not find one in the text read.) Whether a censoring-aware estimator would do better is not established here.
- The bias depends on the observation window. A cohort's apparent lifetime moves with when the sample was taken, so a recent-year drop read in one snapshot may be smaller or larger in another. The paper's figures are a single snapshot.

## Related

- [[observed-resolution-difficulty]] — the same one-sided censoring on time-to-resolution: open items are left out of the median, so the most recent or slowest cases are reported with the most downward bias

[^r1]: arxiv-2512-19727 — "the more recent the launch dates, the shorter the lifetimes of the spacecraft that have failed and can thus contribute lifetime data"
[^r2]: arxiv-2512-19727 — "curves by biasing lifetime estimates for recent launch dates downward"
[^r3]: arxiv-2512-19727 — "when the same lifetime data are plotted by failure year instead of launch year"
[^r4]: arxiv-2512-19727 — "This downward trend does not imply that newer vessels are less reliable"
[^r5]: arxiv-2512-19727 — "into a function of the end time"
[^r6]: arxiv-2512-19727 — "reverts the results back to the original launch time-based framework"
[^r7]: arxiv-2512-19727 — "free from a critical source of bias inherent in launch time data"
[^r8]: arxiv-2512-19727 — "One limitation of this study is the availability and scope of the data used"
[^r9]: arxiv-2512-19727 — "potentially reducing the associated"
[^r10]: arxiv-2512-19727 — "which for convenience we will call the failure time, although it could"
