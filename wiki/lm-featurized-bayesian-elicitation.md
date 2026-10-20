---
description: "OPEN splits preference elicitation in two: an LM supplies features and verbalizes questions, a Bayesian model picks questions by expected information gain and tracks the user's weights."
aliases: ["OPEN", "Optimal Preference Elicitation with Natural language", "LM-plus-BOED elicitation"]
sources: ["doi-10-48550-arxiv-2403-05534"]
---
# LM-featurized Bayesian elicitation

Prompted language models ask poorly targeted questions and track uncertainty badly; classical [[bayesian-experimental-design]] picks the most informative question but needs a known feature space and a structured interface. OPEN (Handa et al., 2024) assigns each side the job it is good at: the LM handles language, the Bayesian model handles uncertainty.[^c1]

## Mechanism

1. **Featurize.** The LM is given a domain description (for example, news-article recommendation) and writes natural-language features such as "whether the article discusses science". These define a feature function mapping an item to a vector.[^c2]
2. **Initialize.** The same LM call ranks the features by importance. The ranking sets the prior: each feature weight is normal with variance scaled by a rank-dependent factor, so features judged more important get wider prior spread.[^c3]
3. **Select.** The Bayesian model enumerates pairwise comparisons over binary feature vectors and picks the one maximizing [[expected-information-gain]] about the user's weights. In the experiments there were 10 features and 2 compared per query; the authors chose these in preliminary testing to balance users' mental effort against informativity.[^c4]
4. **Verbalize.** The LM turns the chosen feature vectors into a natural-language "Would you prefer A or B" question, with synthesized example items (the inverse of the featurization).[^c5]
5. **Update and predict.** The posterior over the weights is updated from the answer using a Bradley-Terry choice model. Exact posteriors are intractable, so a particle filter is used, each particle being a candidate "persona". Test-time predictions come from the Bayesian model, not from the LM.[^c6]

The authors state that the framework does not require particle filtering or even BOED: it is meant to let "any uncertainty-based preference-learning algorithm" talk to a user in natural language.[^c6]

## What was measured

In a user study on news-article preferences, accuracy on 15 held-out pairwise article comparisons was measured after every turn. The metric, time-integrated delta accuracy, integrates the gain over the initial accuracy across turns, so a method that learns earlier scores higher.[^c7]

- Same OPEN predictor, different question source: OPEN-selected pairwise questions beat LM-selected pairwise questions, which the authors read as showing value in "querying based on explicit notions of uncertainty".[^c8]
- Same OPEN questions, different predictor: OPEN's Bayesian prediction aligned better with human preferences than a prompted LM reading the same transcript. The authors read this as LMs being weak at in-context learning of preferences compared with explicit tracking.[^c9]
- Dropping verbalization (users map the raw feature vectors to descriptions themselves) left users "significantly worse at accurately specifying their preferences", so the natural-language interface is itself load-bearing.[^c10]

## Limits

- Open-ended LM questions, which the LM cannot be made to restrict, scored far higher than pairwise questions under LM prediction. They are incompatible with OPEN's predictor, so the best-performing question type was not combined with the Bayesian model.[^c11]
- Preferences are assumed linear in LM-generated features. If the LM omits a relevant feature, no question can recover it; this failure was not isolated here (my inference).
- One domain (news recommendation), a fixed feature count and question format; the prior-from-LM-ranking rule was not shown against alternatives in the slices read.
- Effect sizes are in a figure; the text gives only directional claims and one standard error bars note, so magnitudes are not reproduced here.

## Related

- [[bayesian-experimental-design]] — the home framework whose query-selection rule OPEN keeps
- [[expected-information-gain]] — the criterion used to pick the pairwise question
- [[spatial-semantic-eig-decomposition]] — another LM/VLM-plus-EIG pairing where the model supplies semantics and EIG selects actions
- [[zero-shot-active-feature-acquisition]] — nearby work on choosing which feature to query
- [[preference-elicitation-gap]] — whether a stated channel carries the preference signal at all

[^c1]: doi-10-48550-arxiv-2403-05534 — "By combining the flexibility of LMs with the rigor of BOED, OPEN can optimize the informativity of queries while remaining adaptable to real-world domains."
[^c2]: doi-10-48550-arxiv-2403-05534 — "Featurization: Using a description of the domain, D, the LM extracts a set of NL features"
[^c3]: doi-10-48550-arxiv-2403-05534 — "we assume that more important features are also more impactful for humans’ decision making about their preferences, and thus, we should model greater diversity over them compared to less important features."
[^c4]: doi-10-48550-arxiv-2403-05534 — "we set total number of features |F| = 10 and the number of features compared per query K = 2."
[^c5]: doi-10-48550-arxiv-2403-05534 — "The LM translates q ∗ into a NL question for the user"
[^c6]: doi-10-48550-arxiv-2403-05534 — "Crucially, though, OPEN does not necessitate the use of particle filtering or even BOED."
[^c7]: doi-10-48550-arxiv-2403-05534 — "This metric rewards eliciting user preferences quickly"
[^c8]: doi-10-48550-arxiv-2403-05534 — "there is value in tracking human preferences and querying based on explicit notions of uncertainty."
[^c9]: doi-10-48550-arxiv-2403-05534 — "This implies that LMs are still subpar at in-context-learning of human preferences from demonstrations"
[^c10]: doi-10-48550-arxiv-2403-05534 — "users become significantly worse at accurately specifying their preferences."
[^c11]: doi-10-48550-arxiv-2403-05534 — "this improvement is overshadowed by the benefit of being able to use OPEN prediction, which is incompatible with LM-only elicitation methods."
