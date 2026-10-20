---
description: "An agent asked for an entity its data lacks often substitutes a similar one and answers from it instead of reporting absence; a prompt rule to assume zero raised the success counts."
aliases: ["wrong adaptation to missing values", "missing-entity substitution", "over-helpfulness under uncertainty"]
sources: ["arxiv-2512-07497"]
---
# Absent-entity substitution

When the entity a question names is not in the data, an agent can answer from a similar entity that is. The trace review in the KAMI study files this under "over-helpfulness under uncertainty, where models substitute missing entities with plausible alternatives".[^c1] The worked case: an agent searches for a requested company, establishes with a LIKE query or a company list that it does not exist, and then "autonomously decides to substitute a similar company name".[^c2] It proceeds with the substitute's figures "instead of returning 0", and the paper notes that the substitution is often visible in the reasoning ("model acknowledges the substitution in reasoning").[^c3] So the agent holds the fact of absence and still commits to an answer built on another entity.

The paper's account of why is a tuning claim. "Modern LLMs are specifically tuned to be helpful," and in agentic data work this helpfulness "can result in computed data to be incredibly misleading".[^c4] The mechanism, as the text gives it, is an answer that is completed rather than checked against the absence the agent has just found. Some runs also drop the entity condition altogether, treating a missing filter as "all" (my reading of the same passage; the paper describes it as a second pattern under the same heading).

The paper tests a remedy of the instruction kind. Scenario Q502 asks for a company's figure with no hint. Its easier twin Q602 adds to the template: "Note that if the requested company data is not present in the database, then assume the answer is 0 for the relevant question."[^c5] On my reading of the results table, the two runs give 14 and 16 successes for Q502 and 27 and 25 for Q602; the unit is not stated in the part of the text read. The stated principle is the general one: "Enterprise agents must prioritize actual data over their priors."[^c6]

## What transfers

For asking and answering, the absent case has a short list of honest outputs: report that the entity is not there (zero, or none), or ask which entity was meant. A substitute is neither. The answerer's commitment comes before the absence is reported, and the commitment is what the note tracks. Whether a question is ambiguous or its referent is missing, the answer is a choice of what to commit to; the two differ in what the honest commitment is. My inference, not the paper's: the Q602 rule supplies the honest output for absence in advance, so it shows the output can be produced when specified, not that the agent detects absence unprompted.

## Limits

- The study is qualitative. The 900 traces were reviewed by hand: "In this study, we perform the analysis manually."[^c7] The slice read gives no rate for substitution across the traces, so how common the pattern is remains unmeasured here.
- Three models were analysed, and the authors say so: "Only three models were analyzed for the study; broader model diversity may yield different behaviors."[^c8]
- The Q602 comparison changes the instruction as well as the scenario. It measures compliance with a stated rule, not spontaneous abstention.
- The text does not show whether substitution follows string similarity in the data or the model's own priors; that was not tested.
- The part of the text read covers the database and company-lookup case. Other scenario families are not established by this note.

## Related

- [[underspecified-question-eager-answering]] — the same early commitment, but there the question is ambiguous and the answer follows an assumed reading; here the referent is absent and the substitute is a different entity.
- [[referent-rejection]] — a grounding answerer fails to say that no object fits a description; the rejection step is the one that goes missing here too.
- [[recoverability-gated-ask-abstain]] — asking is right when a reply could supply the missing variable; in a batch run no reply comes, so the choice narrows to reporting absence or substituting (my inference).

[^c1]: arxiv-2512-07497 — "over-helpfulness under uncertainty, where models substitute missing entities with plausible alternatives"
[^c2]: arxiv-2512-07497 — "autonomously decides to substitute a similar company name"
[^c3]: arxiv-2512-07497 — "model acknowledges the substitution in reasoning"
[^c4]: arxiv-2512-07497 — "Modern LLMs are specifically tuned to be helpful."
[^c5]: arxiv-2512-07497 — "Note that if the requested company data is not present in the database, then assume the answer is 0 for the relevant question."
[^c6]: arxiv-2512-07497 — "Enterprise agents must prioritize actual data over their priors."
[^c7]: arxiv-2512-07497 — "In this study, we perform the analysis manually."
[^c8]: arxiv-2512-07497 — "Only three models were analyzed for the study; broader model diversity may yield different behaviors."
