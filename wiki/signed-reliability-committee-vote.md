---
description: "Weighting each member's vote by the log-odds of its reliability is Bayes-optimal for independent binary voters; a member below chance gets negative weight, so its votes count against it."
aliases: ["reliability-weighted majority", "log-odds weighted vote", "Nitzan-Paroush committee rule", "inverted-vote aggregation", "reliability-weighted council vote"]
sources: ["doi-10-48550-arxiv-2610-02005"]
---
# Signed reliability-weighted committee vote

A committee whose members each back one candidate answer can be aggregated by a weighted majority. Each member's weight is the log-odds of its reliability, so a reliable member counts for more and a poor one counts for less. For independent binary voters with one endorsement each, picking the answer with the largest weighted sum is the Bayes-optimal committee rule. The classical form is due to Nitzan and Paroush (1982), and the paper places its own rule in that lineage: "Weighting votes by competence is classical".[^r1][^r2] Plain majority is the special case in which every weight is the same: "plurality voting is the special case" of equal positive weights.[^r3]

The weights are fitted, not assumed. Each member's reliability is estimated from labelled calibration folds, shrunk toward the council mean, and turned into a prior mean for that member's reliability, "to a prior mean with pooling."[^r6] The weight then follows from that mean. The sign is the important part. When a member's fitted reliability falls below one half, its weight is negative, and "the agent's endorsement counts against the answer it names."[^r4] An endorsement from a distrusted seat becomes evidence for the answer it rejects, not a vote for the answer it names. In the paper's adversarial runs the corrupted seat's fitted reliability was "about 0.18 to 0.24, against 0.55 to 0.66" for the genuine seats.[^r8]

Plurality cannot do this, because it has no sign to flip. The paper names the assumption it violates: plurality needs every voter to help, which is "exactly the assumption a persistent adversary violates."[^r5] The consequence is a difference in kind. A committee that weights by sign does not out-argue a persuasive adversary; it "learns not to believe" that seat.[^r7] Once the wrong voice is identified, its consistency becomes information. Outvoting it would need a majority of honest seats; inversion needs only the fitted sign.

What transfers is the rule itself: given a per-member reliability on a labelled window, the vote is a sum of signed log-odds. What the paper's optimality claim does not cover is the general case. The Bayes-optimality holds for "binary, correctly-specified, single-endorsement case."[^r12] For more than two candidates, the paper uses a tempered composite likelihood, and the general form keeps the mechanism "without the optimality claim."

## Limits

- The rule is supervised. "per-agent BDA is a supervised aggregator," and every baseline was given the same label budget for a fair comparison.[^r13] The paper reports that "about 25 labels suffice" to reach the plateau.[^r14] Without labelled calibration data there is no reliability to sign.
- Identifiability is a precondition, not a detail. "Reliability weighting requires the unreliability to be identifiable."[^r9] A member that is clean during calibration and hostile afterwards "inherits our trust until re-fitting catches it."[^r10] The paper's own attacks are constructed; their fit to a live coalition is one set of runs, one council of three models, and three seeds.
- Deliberation contributes little at K=2. The paper says that "at K=2 rounds are nearly irrelevant" to the final decision, so the binary carrier is in effect weighted first-round voting.[^r11] Whatever the deliberation adds is not what the binary result measures.
- Independence is assumed and violated in the paper's own K>2 data. A seat's several moves per task are correlated, and counting them as independent "over-counts the evidence"; a single temperature fixes the calibration.[^r17] The sign does not fix the over-count.
- The posterior ignores the members' stated confidences. "The posterior is invariant, bit for bit, to any rewriting of the per-move self-reported" confidence.[^r15] This blocks sycophantic inflation from moving the answer, and it also discards any information the stated confidence carries.
- The motivation is a measured gap, not a general law. The paper reports that "unanimous councils in our data are wrong 18% of the time," against a unanimous vote that reports 1.0.[^r16] That is one council on three datasets, not an estimate for councils in general.

## Related

- [[dawid-skene-annotator-model]] — the annotator model this rule is built on; its one-coin form is the case used here.
- [[calibration]] — the posterior's confidence is judged by calibration, and the fitted prior acts as the recalibrator.
- [[majority-vote-mode-certificate]] — the unweighted Condorcet vote over sampled answers, the equal-weight case of this rule.
- [[reliability-weighted-signal-fusion]] — a softmax over reliability scores; no log-odds and no sign, so it cannot invert a signal.
- [[rater-effects-latent-score-model]] — unreliable raters are down-weighted through a latent model rather than a signed weight.
- [[effective-independent-votes]] — what correlated votes are worth; the independence this rule assumes.
- [[consensus-criterion-retention]] — unanimity measured as agreement, which the paper's 18 % figure shows is not correctness.

[^r1]: doi-10-48550-arxiv-2610-02005 — "Weighting votes by competence is classical"
[^r2]: doi-10-48550-arxiv-2610-02005 — "the optimal rule for independent binary voters uses log-reliability-odds"
[^r3]: doi-10-48550-arxiv-2610-02005 — "plurality voting is the special case"
[^r4]: doi-10-48550-arxiv-2610-02005 — "endorsement counts against the answer it names"
[^r5]: doi-10-48550-arxiv-2610-02005 — "exactly the assumption a persistent adversary violates"
[^r6]: doi-10-48550-arxiv-2610-02005 — "to a prior mean with pooling"
[^r7]: doi-10-48550-arxiv-2610-02005 — "out-argue a persuasive adversary, it learns not to believe that"
[^r8]: doi-10-48550-arxiv-2610-02005 — "fitted reliability is about 0.18 to 0.24, against 0.55 to 0.66"
[^r9]: doi-10-48550-arxiv-2610-02005 — "Reliability weighting requires the unreliability to be identifiable"
[^r10]: doi-10-48550-arxiv-2610-02005 — "inherits our trust until re-fitting catches it"
[^r11]: doi-10-48550-arxiv-2610-02005 — "at K=2 rounds are nearly irrelevant"
[^r12]: doi-10-48550-arxiv-2610-02005 — "binary, correctly-specified, single-endorsement case"
[^r13]: doi-10-48550-arxiv-2610-02005 — "We are explicit throughout: per-agent BDA is"
[^r14]: doi-10-48550-arxiv-2610-02005 — "about 25 labels suffice"
[^r15]: doi-10-48550-arxiv-2610-02005 — "The posterior is invariant, bit for bit, to any rewriting of the per-move self-reported"
[^r16]: doi-10-48550-arxiv-2610-02005 — "unanimous councils in our data are wrong 18% of the time"
[^r17]: doi-10-48550-arxiv-2610-02005 — "over-counts the evidence"
