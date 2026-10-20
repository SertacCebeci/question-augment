---
description: "Abstention earns partial credit scaled by how likely the evidence was unreliable (one minus that probability), while a confident wrong answer earns nothing."
aliases: ["partial credit for abstention under unreliable evidence", "reliability-discounted abstention credit"]
sources: ["doi-10-48550-arxiv-2607-13920"]
---
# Reliability-discounted abstention credit

A score for a search run has to say what a withheld answer is worth. DeepStress (Rousseau, Damnati and Béchet, 2026) makes that worth depend on the evidence the run was given. Its simulator fixes, for each condition, the probability that the returned documents are trustworthy, relevant and factual, and the paper multiplies the three into one number for the condition: "we define the reliability of condition γ as the product" of them.[^a1] Call that number ρ.

The per-run score has three cases. A correct answer gets full credit. An incorrect answer, or a run that ends without an answer tag, gets none. An abstention, or a run that exhausts its tool budget, gets partial credit, and the amount follows the evidence: "partial credit when reliable evidence is unlikely".[^a2] The paper's reason is that when relevance or factuality is set to 0%, "the agent should not be expected to recover the answer from the provided documents."[^a3] So as ρ falls, withholding is worth more. My reading of the case formula is that the partial credit is 1 − ρ, which makes it close to a full answer when ρ is near zero. The per-run values are averaged over runs; the cost-normalised version is CoPRAS, which divides total cost by this sum instead of by correct answers (see [[tokens-per-correctness]]).

The paper tests several search agents on HotpotQA and BrowseComp-Plus.[^a4] At 0% document quality, averaged over the three settings, "average correctness drops to 0.30, while average RAS remains much higher at 0.61."[^a5] The gap is not uniform. GPT-5-nano (medium) falls from 0.83 to 0.41 in correctness while its RAS stays stable; Search-R1 falls from 0.80 to 0.35 in correctness and from 0.80 to 0.37 in RAS.[^a6] The paper's reading is that "RAS better separates robust non-answer behavior from overconfident failure when document quality is low."[^a7]

The mechanism, concretely: under degraded evidence, correctness stops being a proxy for good behaviour. An answerer that withholds when its evidence is broken and an answerer that guesses confidently both lose correctness. The discounted score separates them, because withholding is credited and a confident wrong answer is not. The credit is a function of the condition the run was in, so the same abstention scores differently under a reliable and an unreliable scenario.

## Why it matters

[[abstention]] treats "I don't know" as a third output whose price has to be named before a reject rule can be judged. This score names the price in advance, from the scenario: the probability that the evidence was usable. That is a different price from the cost of rejection in selective classification. There the abstention is optimised against a threshold; here it is credited by a fixed rule, and the rule is the experimenter's choice.

## Transfer

What survives the move out of a simulated search loop is the principle that a non-answer has a value that depends on the state of the evidence it was given, and that a grader has to know that state to score it. What does not survive is the specific numbers. The values come from one simulator, and ρ is a probability the experimenter sets, not something observed in a deployed search.

## Limits

- The paper says that "RAS and CoPRAS reflect a particular scoring choice," and discusses alternatives in an appendix that this note did not read.[^a8]
- ρ is the expected reliability set by the experimenter, not the realised one. The paper notes that "the realized number may differ because each document is sampled independently."[^a9] A given run can therefore have evidence better or worse than ρ suggests.
- The partial credit assumes every question is answerable in principle: "every question is answerable in principle, but the simulator can make the available evidence unreliable or uninformative."[^a10] Where a question has no answer at all, withholding is correct and the formula is not the right grader. This is my inference from the setup, not a test in the paper.
- The product form treats the three dimensions as independent. The sampling is independent, but whether the product is the right way to combine them was not tested. This is my inference.
- Correct, incorrect and abstention labels come from a judge: "we use GPT-4.1 as an LLM-as-a-judge to classify the answer." The score inherits that classification.[^a11]
- Budget exhaustion gets the same credit as abstention. My reading is that an exhausted budget is not a stated refusal, and the score cannot separate the two beyond the grouping it assigns.
- The evidence is synthetic: "DeepStress is not a replacement for real search benchmarks but acts as a controlled laboratory for stress testing of search-agent behavior."[^a12]
- The acronym collides with [[reliability-aware-score]], which names a different metric: partial credit for placeholder spans in speech transcription. The two are not the same concept, and their numbers are not comparable.

## Related

- [[abstention]] — the reject option whose price has to be named; here the price is the scenario's probability of usable evidence.
- [[reliability-aware-score]] — same acronym, different metric; partial credit per span in ASR rather than per run under evidence degradation.
- [[tokens-per-correctness]] — the cost-side counterpart; CoPRAS divides cost by this reliability-aware sum instead of by correct answers.
- [[evidence-reliability-axes]] — the three degradations whose product sets ρ.
- [[search-induced-abstention-degradation]] — abstention on questions with no answer is also a search-agent behaviour that depends on the retrieved text; this note is about crediting it when the evidence is broken.

[^a1]: doi-10-48550-arxiv-2607-13920 — "we define the reliability of condition γ as the product"
[^a2]: doi-10-48550-arxiv-2607-13920 — "partial credit when reliable evidence is unlikely"
[^a3]: doi-10-48550-arxiv-2607-13920 — "the agent should not be expected to recover the answer from the provided documents"
[^a4]: doi-10-48550-arxiv-2607-13920 — "Testing several search agents on HotpotQA and BrowseComp-Plus"
[^a5]: doi-10-48550-arxiv-2607-13920 — "average correctness drops to 0.30, while average RAS remains much higher at 0.61"
[^a6]: doi-10-48550-arxiv-2607-13920 — "GPT-5-nano (medium) drops from 0.83 to 0.41 in correctness, but its RAS remains stable"
[^a7]: doi-10-48550-arxiv-2607-13920 — "RAS better separates robust non-answer behavior from overconfident failure when document quality is low"
[^a8]: doi-10-48550-arxiv-2607-13920 — "RAS and CoPRAS reflect a particular scoring choice"
[^a9]: doi-10-48550-arxiv-2607-13920 — "the realized number may differ because each document is sampled independently"
[^a10]: doi-10-48550-arxiv-2607-13920 — "every question is answerable in principle, but the simulator can make the available evidence unreliable or uninformative"
[^a11]: doi-10-48550-arxiv-2607-13920 — "we use GPT-4.1 as an LLM-as-a-judge to classify the answer"
[^a12]: doi-10-48550-arxiv-2607-13920 — "DeepStress is not a replacement for real search benchmarks but acts as a controlled laboratory for stress testing of search-agent behavior"
