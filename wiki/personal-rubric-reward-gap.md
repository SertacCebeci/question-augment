---
description: "Chosen and rejected answers that differ only in adherence to one user's rubric, with human-rated general quality equal, leave reward models at 75.94% accuracy at best."
aliases: ["personalized reward gap", "personal rubric adherence", "personalized reward modeling gap"]
sources: ["doi-10-48550-arxiv-2604-07343"]
---
# Personal-rubric reward gap

A reward model scores a response, and a reward benchmark tests it on pairs: a chosen answer and a rejected one. Most such benchmarks make the rejected answer worse in general, by taking it from a smaller model, injecting errors, or selecting low human or LLM scores.[^c1] The Personalized RewardBench construction changes the reason for rejection. Each pair is built from one user's explicit rubric. The chosen answer is generated with the rubric aspects in view; the rejected answer is generated so that it avoids them. A rejected answer is marked as rejected because it violates that user's personal rubric, whatever its general quality.[^c2]

The construction is meant to make personal fit the only variable. Human raters scored both sides high on factuality, relevance and helpfulness, and separated them on personal rubric fit, where the rejected answers do markedly worse.[^c3] Across 2,830 instances (5,660 responses) the authors read the difference as one of personal alignment, not general quality.[^c4] The reward gap in this sense is the difference a reward model must register when general quality is level and only a user's own criteria differ.

Measured that way the gap is large. The best reward model reaches 75.94% pair accuracy, and the strongest frontier judge, Gemini-3-Flash, does not pass 76% in any domain.[^c5][^c6] Scale does not close it: internlm2-20b is worse than its 7b counterpart in every domain, so the authors conclude that personalized alignment needs training objectives of its own rather than more capacity.[^c7] When the reward model is handed the ground-truth rubric aspects, accuracy is near-perfect.[^c8] The authors take the remaining gap of over 20 points to be genuinely personal preference, which is their inference from that contrast and not something the oracle run isolates.[^c9]

The benchmark also tests how a user's history should reach the reward model. The history is not a rubric. General reward models are trained on prompt-response pairs and "lack the capacity to process auxiliary profiling data", and naively injecting the profile degrades them relative to no profile.[^c10][^c11] A planner that first infers rubric aspects from the profile, and passes those to the reward model, recovers accuracy and often surpasses the no-profile baseline, by translating historical data into structured rubrics.[^c12][^c13] My reading, not a tested claim: in this paper the explicit rubric is the form in which personal history reaches the judge, and the raw profile does not. The paper tests one planner and one injection format, so the reading is about these two only.

## Limits

- One query per user. The authors note that some personalized reward models use several queries per user, and that their own dataset "contains only a single" query per user.[^c14] Personalization that accumulates over many interactions is not tested.
- The equal-quality claim comes from an iterative loop. Responses flagged in human review were regenerated: 156 unique instances in the first round and 26 in the second, after which the final checker confirmed that all responses met the quality threshold.[^c15][^c16] The read text does not say whether any pair was dropped rather than regenerated, so the Table 1 scores describe a filtered set.
- Both sides come from one generator (Gemini-3-Flash). The claim that the construction "introduces no exploitable stylistic shortcut" rests on an appendix I did not read; it is the authors' claim.[^c17]
- The rubrics are "explicit, human-validated criteria" taken from LaMP-QA.[^c18] The benchmark says nothing about preferences a user has not written down, or that shift over time, and nothing about whether a real user's dispreferred answers look like the generated rejected ones.
- The planner is described as a deliberately simple baseline, and the authors state that "absolute performance maximization is not the objective of the planner."[^c19] No claim is made that rubric inference is the best way to use a profile.
- The gap is measured on accuracy in a pairwise setting. Whether a higher pair accuracy yields a better policy is a separate question, taken up in [[reward-benchmark-downstream-correlation]].

## Related

- [[reward-benchmark-downstream-correlation]] — the same benchmark, judged by whether its accuracy ranking predicts policy outcomes under best-of-N and PPO.
- [[preference-consistency-rubric-reward]] — rubrics as the carrier of a reward, there learned from which report a preference ranks higher, not from a user's history.
- [[structured-annotator-disagreement-on-harm]] — personalized alignment to individual annotators beats aggregate labels there too, in a different domain.
- [[memory-induced-unawareness]] — a personal assistant given unstructured user facts also degrades; as I read it, the same missing-structure problem in another setting.

[^c1]: doi-10-48550-arxiv-2604-07343 — "are deliberately constructed by choosing a smaller model"
[^c2]: doi-10-48550-arxiv-2604-07343 — "solely because they violate specific personal rubrics"
[^c3]: doi-10-48550-arxiv-2604-07343 — "the rejected answers perform markedly worse"
[^c4]: doi-10-48550-arxiv-2604-07343 — "across 2,830 unique instances (totaling 5,660 responses)"
[^c5]: doi-10-48550-arxiv-2604-07343 — "which peak at an accuracy of just 75.94%"
[^c6]: doi-10-48550-arxiv-2604-07343 — "fails to surpass the 76% accuracy threshold across any domain"
[^c7]: doi-10-48550-arxiv-2604-07343 — "tailored to subjective preference distributions"
[^c8]: doi-10-48550-arxiv-2604-07343 — "with ground-truth rubric aspects attains 97.78–99.09% accuracy"
[^c9]: doi-10-48550-arxiv-2604-07343 — "The remaining gap of over 20 percentage points therefore corresponds to genuinely personal"
[^c10]: doi-10-48550-arxiv-2604-07343 — "lack the capacity to process auxiliary profiling data"
[^c11]: doi-10-48550-arxiv-2604-07343 — "naively injecting user profiles (w/ profile) degrades reward"
[^c12]: doi-10-48550-arxiv-2604-07343 — "translating historical data into structured"
[^c13]: doi-10-48550-arxiv-2604-07343 — "consistently recovering and frequently surpassing baseline accuracy across domains"
[^c14]: doi-10-48550-arxiv-2604-07343 — "our dataset contains only a single"
[^c15]: doi-10-48550-arxiv-2604-07343 — "In the first round, 156 unique instances"
[^c16]: doi-10-48550-arxiv-2604-07343 — "the final quality checker confirmed that 100% of the responses successfully met our quality thresholds"
[^c17]: doi-10-48550-arxiv-2604-07343 — "this construction introduces no exploitable stylistic shortcut"
[^c18]: doi-10-48550-arxiv-2604-07343 — "These aspects represent explicit, human-validated criteria for satisfaction"
[^c19]: doi-10-48550-arxiv-2604-07343 — "absolute performance maximization is not the objective of the planner"
