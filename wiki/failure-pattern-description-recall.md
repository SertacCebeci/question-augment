---
description: "Descriptions of where a model fails are scored by how many known failure groups they recover: prompting nears a strong match (about 4 of 5), while an embedding-cluster method reaches 3.25."
aliases: ["recall of known failure patterns", "failure-pattern discovery recall", "Stage 2 recall", "failure-pattern generation quality"]
sources: ["arxiv-2512-21422"]
---
# Failure-pattern description recall

Before a model's failure group can be taught to a user, someone has to describe it in words. The paper treats that description step as a measurable stage and scores it by recall. Take the failure groups that meet the error-ratio threshold, computed from human meta-labels, as the known patterns. Each generated natural-language description is compared with every known pattern, and its best match is kept. Recall is the average of those best matches across the known patterns.[^c1] The match is rated by an LLM judge on a 1-to-5 scale, from "No Match" to "Perfect Match," and the paper reports that its judge agreed with a human on the same method's outputs: the mean absolute difference was 0.051 and the quadratic-weighted Cohen's kappa 0.838.[^c2]

The paper compares two families of automatic methods. Prompting methods give the model the wrongly answered instances and ask for their shared properties; one variant contrasts the wrong instances with the correct ones. The embedding method, IntegrAI from Mozannar et al. (2023), clusters instances into regions where humans and the model differ, describes each region with an LLM, and refines the description against counterexamples.[^c3]

The results split by family. The simple direct prompt "reaches recall scores close to 4," which the rubric calls a strong match, and the paper says it nearly recovers the known patterns.[^c4] IntegrAI "reaches only 3.25 at best," and the authors suggest that noise in its descriptions may have contributed to the ineffective teaching found earlier.[^c5] The paper's reading is that the description stage is the weak link: "Stage 2 remains a key bottleneck." Recall also did not depend on how many patterns there were: "no connection between recall and the number of" patterns could be found.[^c6]

Adding the model's chain of thought to the wrong instances did not help uniformly. In some settings it lowered recall, and on manual review the descriptions "more strongly feature general statements about the level of complexity or number of steps required" instead of concepts.[^c7] 

What transfers is the separation between generating a description and having it matched to a real group. A description can be fluent and still fail to name the group a user needs to avoid. The rating scale also shows how coarse the match is: the authors judged a score of 4 as "generally describes the pattern in sufficient detail," and a 3 as one whose descriptions "often omit key aspects" and can mislead.[^c8] By that standard IntegrAI's best value falls below the level the authors regard as usable for teaching.

## Limits

- Recall is scored against known groups, and the known groups are meta-labels, not independently verified failure causes. A generated description that names a real cause the labels do not capture would score low. The paper says the method "assesses methods only by" the match to known patterns.[^c9]
- The paper notes that "We do not yet have an automatic way to" compare methods on the full set of patterns they produce, so recall is a partial view.[^c10]
- Two datasets (MathCAMPS and MMLU), five models for MathCAMPS and one for MMLU, and one judge model. The judge's averages are over three runs, and the text gives no spread for the judge itself.
- Recall says nothing about whether a description helps a user. The downstream test of that is [[error-anticipation-accuracy]], which the paper runs for only one of the description methods on MMLU.
- The paper reports that chain-of-thought effects vary across methods and models. The result that prompting is near 4 is for the settings tested; it is not shown for other tasks or other models.

## Related

- [[failure-group-coverage-and-error-ratio]] — the measures that decide which groups count as known patterns in this scoring.
- [[error-anticipation-accuracy]] — the teaching metric that a recovered description would feed into.
- [[over-reliance-discrimination-failure]] — the answerer-side failure that teaching of this kind is meant to address.

[^c1]: arxiv-2512-21422 — "Recall is computed by scoring each generated pattern against all ground-truth patterns"
[^c2]: arxiv-2512-21422 — "quadratic weights and 0.744 for linear weights indicate high agreement."
[^c3]: arxiv-2512-21422 — "clusters instances into regions where performance of humans and AI models differs"
[^c4]: arxiv-2512-21422 — "prompting method reaches recall scores close to 4"
[^c5]: arxiv-2512-21422 — "reaches only 3.25 at best, suggesting that noise"
[^c6]: arxiv-2512-21422 — "no connection between recall and the number of"
[^c7]: arxiv-2512-21422 — "strongly feature general statements about the level"
[^c8]: arxiv-2512-21422 — "patterns scoring 3 often omit key aspects,"
[^c9]: arxiv-2512-21422 — "it assesses methods only by"
[^c10]: arxiv-2512-21422 — "We do not yet have an automatic way to"
