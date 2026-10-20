---
description: "Proof labels built from many verifier analyses: the lowest score that enough meta-validated analyses report, 1 if no issue survives, else discard; it replaced human annotation."
aliases: ["automated proof labeling", "verifier-based auto-labeling", "scaled verification labels", "AI-assisted annotation of proofs"]
sources: ["arxiv-2511-22570"]
---
# Scaled-verification labeling

A verifier is only as good as its training labels, and the proofs that most need labels are the ones the current generator has just produced: they are hard, and their errors are subtle. The paper says human annotation for these "becomes increasingly time-consuming as" problems get harder.[^l1] Its answer is to let the verifier label the proofs, with more verifier samples standing in for more annotator effort. The support is the observation that "Scaling verifier samples increases the probability of catching real issues in flawed proofs."[^l2]

The procedure has three steps. For each proof, generate n independent verification analyses. For each analysis that reports issues (a score of 0 or 0.5), run m meta-verification assessments to test the reported problems, and treat the analysis as valid when most of them confirm it: "An analysis is deemed valid if the majority of" the meta-assessments confirm its findings.[^l3] Then take the analyses that assign the lowest score. If at least k of them are valid, the proof gets that lowest score. If no legitimate issue survives across all attempts, the proof gets 1. Anything else is "discarded or routed to human experts for labeling."[^l4] The check on which analyses count is the one described in [[meta-verification]].

The design is asymmetric, and the asymmetry is the point. A top label is given only by absence: no issue survives across all attempts. A low label needs a threshold of validated issues, so a single unconfirmed complaint cannot lower a proof. The uncertain middle goes to humans or is dropped. The effort proxy from [[generation-verification-gap]] is what licenses the absence rule: a proof with no surviving issue after scaled checking is taken to be valid.

The paper reports that the procedure did its job in training: "In our last two training iterations, this fully automated pipeline replaced human annotation entirely."[^l5] It also reports, briefly: "Quality checks confirmed that the automated labels aligned well with expert judgments."[^l6] An earlier stage used the same verifier analyses to speed up people rather than replace them: "To boost annotation efficiency, we generated multiple verifier analyses per proof to surface potential issues for human review."[^l7]

Relative to other consensus labelling, the distinctive part is the meta-filter and the lowest-score rule. A majority vote over verifier runs labels each item by the crowd of runs; here the runs are first filtered for whether their issues are real, and the proof's label is set by the worst analysis that survives that filter. A proof with one real, serious issue is therefore labelled low even if most runs missed it, provided k valid analyses agree.

## Limits

- The agreement with experts is reported only as "aligned well." The text read gives no agreement rate, sample size, or error rate for the automated labels.
- The values of n, m and k are symbols in the parts read. I did not find the settings used, so the cost of the procedure and the sensitivity to these choices are not established.
- Discarded proofs are removed from the data, and the text does not report what share that is. My inference: if the discard rule removes the hardest cases, the training set is biased toward proofs that are easy to check, which is the bias the labels were meant to avoid.
- The "no issue survives" rule makes a verifier's blind spot into a positive label. A flaw the verifier cannot surface is never named, so the proof is labelled 1. My inference: the procedure can only be as good as the verifier's coverage of the flaw types it is run on.
- The analyses and meta-assessments come from models of the same family being trained, so shared errors can pass both filters. The text does not test this.
- The procedure is described for olympiad-style proofs. Whether it transfers to tasks without a rubric the verifier can apply is not tested.

## Related

- [[step-level-consensus-labels]] — majority vote over independent verifier runs labels steps with no ground truth; the procedure here adds a meta-filter and sets the label by the lowest surviving analysis
- [[meta-verification]] — the filter that decides which verifier analyses count as valid
- [[generation-verification-gap]] — the premise that effort spent on checking is a usable proxy for proof quality
- [[sound-verifier-self-play]] — the other route to labels for self-generated training data, using a sound formal checker instead of sampled judgments
- [[faithful-self-assessment-reward]] — uses the same verifier as the label source for a generator's own self-analysis

[^l1]: arxiv-2511-22570 — "Manual annotation, while straightforward, becomes increasingly time-consuming as"
[^l2]: arxiv-2511-22570 — "Scaling verifier samples increases the probability of catching real issues in flawed proofs."
[^l3]: arxiv-2511-22570 — "An analysis is deemed valid if the majority of"
[^l4]: arxiv-2511-22570 — "is discarded or routed to human experts for labeling"
[^l5]: arxiv-2511-22570 — "In our last two training iterations, this fully automated pipeline replaced human annotation entirely."
[^l6]: arxiv-2511-22570 — "Quality checks confirmed that the automated labels aligned well with expert judgments."
[^l7]: arxiv-2511-22570 — "To boost annotation efficiency, we generated multiple verifier analyses per proof to surface potential issues for human review."
