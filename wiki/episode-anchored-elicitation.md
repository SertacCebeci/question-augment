---
description: "Asking about one dated, located episode, rather than a general state of affairs, is meant to draw out time-, place- and body-specific detail that a general question leaves open."
aliases: ["story-based prompting", "episodic prompting", "event-anchored question"]
sources: ["arxiv-2601-04201"]
---
# Episode-anchored elicitation

A general question asks the respondent for a summary: how is the public transit here? The respondent answers with a generalization, and a generalization drops particulars. An episode-anchored question asks for one occasion, a time, a place and what happened. An occasion carries slots a summary does not: when it was, where, what the body did, who was there. My reading of the mechanism: the question fixes the form the answer must take, so the particulars are requested instead of left out.

The Collective Narrative Grounding workshops built this into their protocol. Facilitators "ask participants to share stories or experiences about specific events."[^e1] One prompt the paper gives as an example is "Tell me about the last time you visited this area."[^e2] The stated aim is narrow: "These prompts aim to elicit details,"[^e3] "such as specific time-, place-, and body-based experiences."[^e4] The aim is tied to the later schema, which was designed for "enabling entity, time, and place extraction."[^e5] A story that carries a time and a place gives the schema something to extract.

The workshop also framed its questions as assets rather than deficits, "instead of deficit-based prompts."[^e6] That is a separate choice about framing, and this note does not treat it.

For someone asking, the concept is that the form of the question sets which slots the answer will fill. A question about an occasion requests the slots; a question about a state requests a judgement, and the judgement can be given without the slots. For someone answering, the slots are a check: an answer that names a time and a place can be compared against a second source, which a summary cannot. The check is mine; the paper does not test it.

## Limits

The paper states an aim and does not measure it. It does not compare episode prompts with general prompts, and it reports no count of details per prompt type. The claim that these prompts elicit more time-, place- and body-based detail is the design intent, not a result.

The evidence base is one community. The workshops were three sessions with 24 residents, and "participants from a single community Atlanta."[^e7] Ages ran from 18 to 55. Nothing here shows that the approach holds where community members are not in a workshop setting, or where the question is asked in a different language.

Specificity has a cost the paper names. In its discussion of privacy: "the more specific the story, the" more useful it is, and in the same breath more re-identifiable.[^e8] The same property that makes an episode informative makes the person behind it easier to find. The paper treats this as an open tension and does not resolve it.

The paper's support that narratives hold the facts a model lacks is indirect. It comes from checking 20 pilot questions against the workshop narratives; see [[local-knowledge-blind-spot]]. It does not test whether episode prompts yield more of those facts than general prompts would.

## Related

- [[local-knowledge-blind-spot]] — the missing facts these prompts are meant to surface, and the pilot that checks whether the narratives hold them
- [[subjective-contextual-incompleteness]] — the contextual kind of gap is omitted context that later matters; an episode prompt may be one way to reach context an informant would not volunteer (my reading, not the paper's)
- [[tacit-knowledge]] — knowledge an informant holds and cannot state on request; asking for a remembered occasion asks for an instance rather than a rule, which may suit that kind of knowledge (my inference)
- [[elicitation-protocols]] — the protocol-level view of how the way of asking shapes what is elicited

[^e1]: arxiv-2601-04201 — "facilitators ask participants to share stories or experiences about specific"
[^e2]: arxiv-2601-04201 — "Tell me about the last time you visited this area"
[^e3]: arxiv-2601-04201 — "These prompts aim to elicit details"
[^e4]: arxiv-2601-04201 — "such as specific time-, place-, and body-based experiences"
[^e5]: arxiv-2601-04201 — "enabling entity, time, and place extraction"
[^e6]: arxiv-2601-04201 — "instead of deficit-based prompts"
[^e7]: arxiv-2601-04201 — "participants from a single community Atlanta"
[^e8]: arxiv-2601-04201 — "the more specific the story, the"
