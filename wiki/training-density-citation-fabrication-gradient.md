---
description: "LLM citation fabrication rises where the requested literature is thinly represented in training data: recent versus seminal framing and field both shift it, with field the larger effect."
aliases: ["temporal framing effect on citation hallucination", "domain effect on citation fabrication"]
sources: ["arxiv-2603-03299"]
---
# Training-density gradient of citation fabrication

In a 10-model audit, how a citation request is framed and what field it is in change the fabrication rate far more than any single model quirk. Asking for "recent and influential" references gave a hallucination rate of 74.1%, against 55.0% for "seminal and foundational" ones; every one of the 10 models was worse under the recent framing, by 12 to 24 points.[^c1] Field mattered more (Cramér's V 0.193 against 0.115 for framing): 26.6% for NLP and AI, 39.4% for biomedicine, 41.8% for climate, 50.1% for structural engineering.[^c2]

The authors' account is training-data availability: seminal works are widely discussed and appear in many documents, whereas recent ones may postdate the cutoff or be too rare to encode, leaving the generator "fewer grounded anchors".[^c3] Fields with open, preprint-heavy literature are represented more densely. Confirmed citations also skew toward open-access and highly cited works (77.3% to 91.8% open access against a 50 to 55% baseline), so correct answers come from the densest part of the distribution.[^c4]

The consequence for questions: the same request, "give me references", has a different failure risk depending on its temporal wording and field. A request that asks for recent, niche material is a request the model is least able to ground, and it will still answer. This is the authors' interpretation; the density mechanism was not tested by manipulating training data.

## Limits

- The density explanation is inferred from the ordering, not measured; the paper lists it as what "we believe".
- Only two framings and four domains; no test of other wordings or of retrieval-equipped models.
- Hallucination here means no match in the authors' verification pipeline, which misclassified about 10.7% of a sampled set.
- Model-level differences (11.4% to 56.8%) are a separate effect not explained by this gradient.

## Related

- [[citation-recurrence-authenticity-signal]] — a check that exploits the same instability of ungrounded output
- [[underspecified-question-eager-answering]] — models answer even when they cannot ground the answer
- [[phantombench]] — abstention on non-existent entities versus rare real ones
- [[presupposition-hallucination-gap]] — another case where the question's wording drives hallucination

[^c1]: arxiv-2603-03299 — "This 19.1% gap"
[^c2]: arxiv-2603-03299 — "NLP and AI exhibited the lowest rate at 26.6%, followed by biomedical research at 39.4%"
[^c3]: arxiv-2603-03299 — "LLMs face a generative task with fewer grounded anchors"
[^c4]: arxiv-2603-03299 — "ranges from 77.3% (haiku-4.5) to 91.8% (GPT-5-mini)"
