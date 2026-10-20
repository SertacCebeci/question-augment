---
description: "The same false premise is adopted at very different rates depending on its claimed source (its own prior output, a retrieved expert, an instruction), and the gradient differs by model."
aliases: ["epistemic policy divergence", "session-level contamination", "state contamination"]
sources: ["doi-10-48550-arxiv-2609-35308"]
---
# Framing-dependent premise adoption

When a false claim sits in a conversation's history, a model may take it as fact and build on it. The mechanism the work isolates is that the rate of this adoption depends on where the claim is said to come from, not only on what it says. The authors call the failure session-level contamination: "in which false premises injected into prior conversational turns are adopted as fact in".[^c1] The injection is silent. In their design, "the genuine turn 4 assistant response is silently replaced with the protocol specific injected content",[^c2] and the replacement carries "no metadata, labels, or markers indicating modification".[^c3]

The design holds the false premise fixed and varies only its framing along five protocols, ordered by source authority.[^c4] One protocol attributes the falsehood to the model's own earlier answer; another presents it as a fabricated retrieval block citing a named journal; another is an explicit system-level instruction to treat it as true; another is a plausible but invalid reasoning chain; the last is a user-cited newly published paper, with a request for a stated confidence. The test case is arithmetic, where "the synthetically injected false premise asserts that 1 plus 1 equals 1."[^c5]

The claimed effect is that identical content gives different rates: "an identical false premise yields radically different adoption rates depending on its origin."[^c6] The authors report this per model over 500 sessions each. The profiles differ. Gemini-3.1 Flash-Lite shows a steep gradient, with "near-zero adoption for self-attributed falsehoods (0.1%)"[^c7] against strong deference to system-injected authority at 68.2%, and adoption under instruction override at 94.0%. GLM-4.5-Air shows a shallower one, "resisting system-injected authority (15.8% adoption)"[^c8] while adopting instruction overrides at 84.2%. GPT-5.4 Mini "exhibited zero adoptions across all 500 sessions and all five protocols under our experimental conditions."[^c9] The authors read the Gemini and GLM gap between authority and instruction as "consistent with authority deference and instruction compliance engaging distinct mechanisms within a single architecture."[^c10]

Persistence is a second measure. Among affected sessions, "26.1% of affected Gemini sessions did not return to factual accuracy within the observation window".[^c11] So adoption is not only a single-turn event; in the paper's design it can persist across later turns.

**Transfer to asking and answering (this wiki's inference, not measured by the work).** For an answerer, the claimed origin of a premise is part of the evidence about whether it holds, and a fluent answer gives no outward sign of which framing the model acted on. For an asker, a claim introduced as coming from a published source may carry more weight with some answerers than the same claim stated bare. The work does not test human askers or human answerers; it tests language models given a modified history.

## Limits

- The evidence is three API-accessed models at temperature zero. The authors say so directly: "Our behavioral findings derive from three API-accessed models."[^c12] They also ask for more: "Future replication on additional architectures".[^c13]
- The binary adoption scores come from one LLM judge. Human validation covered 120 turns, and the reviewer's corrections were all on severity: "with zero modifications to Track 1 binary labels."[^c14] The reliability figures are for that sample, not for the 22,500 turns.
- The instruction-override protocol cannot be separated from genuine adoption in this design. The authors write that "our API-based dual-track evaluation cannot distinguish" the two mechanisms, since both produce a Track 1 score of 1.[^c15] So the high override rates do not show that the model believed the premise.
- The GPT zero is for the deployed Mini variant, and the authors note that "the deployed Mini variant does not expose log-probabilities", so its internal state was not examined in the main experiment.[^c16]
- The "authority" and "instruction" labels are the paper's own classification of framings. The work does not show that the models represent source or authority internally, only that the adoption rates differ by framing.
- The sessions cover ten knowledge domains, and the example is arithmetic. Whether the gradient ordering holds for questions with contested facts, or for claims the model cannot check, is not tested here.
- The adoption patterns come from a single preprint's pipeline. Replication of the gradient on other models or other premises is not in the work.

## Related

- [[false-premise-question]] — the question-side failure: an answer in the requested type endorses the premise. This note adds that the premise's claimed origin changes whether it is adopted.
- [[self-answering-injection-compliance]] — untrusted text that supplies both the question and the answer, in a QA pipeline rather than a chat history.
- [[presupposition-accommodation]] — the pragmatic update that explains endorsement by answer; the framing gradient asks what a model admits into its context in the first place.
- [[debate-elicits-sycophancy]] — sycophancy is alignment with a user's stated opinion; the work separates it from adopting a falsified history.

[^c1]: doi-10-48550-arxiv-2609-35308 — "in which false premises injected into prior conversational turns are adopted as fact in"
[^c2]: doi-10-48550-arxiv-2609-35308 — "the genuine turn 4 assistant response is silently replaced with the protocol specific injected content"
[^c3]: doi-10-48550-arxiv-2609-35308 — "with no metadata, labels, or markers indicating modification"
[^c4]: doi-10-48550-arxiv-2609-35308 — "We define five contamination protocols arranged along a source authority gradient, from lowest to highest"
[^c5]: doi-10-48550-arxiv-2609-35308 — "the synthetically injected false premise asserts that 1 plus 1 equals 1"
[^c6]: doi-10-48550-arxiv-2609-35308 — "an identical false premise yields radically different adoption rates depending on its origin"
[^c7]: doi-10-48550-arxiv-2609-35308 — "near-zero adoption for self-attributed falsehoods (0.1%)"
[^c8]: doi-10-48550-arxiv-2609-35308 — "resisting system-injected authority (15.8% adoption)"
[^c9]: doi-10-48550-arxiv-2609-35308 — "exhibited zero adoptions across all 500 sessions and all five protocols under our experimental"
[^c10]: doi-10-48550-arxiv-2609-35308 — "and instruction compliance engaging distinct mechanisms within a single architecture"
[^c11]: doi-10-48550-arxiv-2609-35308 — "26.1% of affected Gemini sessions did not return to factual accuracy within the observation window"
[^c12]: doi-10-48550-arxiv-2609-35308 — "Our behavioral findings derive from three API-accessed models"
[^c13]: doi-10-48550-arxiv-2609-35308 — "Future replication on additional architectures"
[^c14]: doi-10-48550-arxiv-2609-35308 — "with zero modifications to Track 1 binary labels"
[^c15]: doi-10-48550-arxiv-2609-35308 — "our API-based dual-track evaluation cannot distinguish"
[^c16]: doi-10-48550-arxiv-2609-35308 — "the deployed Mini variant does not expose log-probabilities"
