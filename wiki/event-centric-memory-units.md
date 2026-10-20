---
description: "A conversation is stored as self-contained event statements that bundle participants, time and local context, not as triples or summaries that split or compress it."
aliases: ["enriched elementary discourse units", "EDU memory", "event-level conversational memory", "event-centric conversational memory"]
sources: ["arxiv-2511-17208"]
---
# Event-centric memory units

A memory of past dialogue has to choose its unit before it chooses how to search. The common units are entity–relation triples, coarse chunks (a session, a round, a turn), and summaries or extracted facts. The event-centric unit is one short statement that carries an event whole. The paper calls these enriched elementary discourse units (EDUs) and defines them as "self-contained statements with normalized entities and source turn attributions".[^c1] An LLM rewrites each session into a list of EDUs. Each EDU records "the set of turn indices in s that support e"[^c2] and a timestamp that "is a timestamp derived from the session date".[^c3] In the paper's worked example the timestamp is inferred rather than read off the text: "the timestamp is inferred based on the session timestamp".[^c4]

The motivation is fragmentation. A triple store holding one trip would keep (Bob, stay in, Tokyo) and related facts as separate edges.[^c5] The paper's complaint is that such stores "fragment the original discourse".[^c6] A retrieval step then has to "find and recombine several triples to reconstruct the event", and fine-grained constraints "can be lost or inconsistently represented".[^c7][^c8] The unit is borrowed from neo-Davidsonian event semantics, in which a sentence is "represented as an event with multiple arguments, rather than" as independent binary relations.[^c9] The transfer is partial. The paper's EDUs are not formal logical forms: it enforces no fixed role ontology ("fixed ontology of roles; the usage of rk is not explored in"),[^c10] and a second LLM pass "returns an event type t(e) and a set of role–argument pairs" for each EDU.[^c11] The arguments become nodes in a heterogeneous graph that also links EDUs to their sessions.

What is measured is the end result, not the representation alone. On LoCoMo with gpt-4o-mini, "the overall LLM score improves from 0.744 for Nemori to 0.780" for both EMem and EMem-G, and "The gains concentrate on" temporal, open-domain and multi-hop questions.[^c12][^c13] The answerer sees little text: EMem "passes only 509–1039 tokens to the backbone (average 738.2)", which is "far below the 23,653-token full-context baseline".[^c14][^c15]

The mechanism of the gain is less certain than the headline. The ablations in §4.4 remove the LLM EDU filter, the mention-to-argument seeding, the QA chain-of-thought and the graph. In the part of §4.4 I read, none replaces EDUs with triples or raw turns, so the text does not show EDUs beating triples; it shows that EDUs with filtering do well. The paper's own verdict on the LoCoMo ablation is that "the LLM-based EDU filter is the most critical piece".[^c16] The filter is therefore doing much of the work that the event unit is credited with. (my reading)

## Limits

- Two benchmarks only. LoCoMo "contains 10 multi-session dialogues between" two speakers,[^c17] and LongMemEvalS "consists of 500 multi-session dialogues between user and assistant".[^c18] The scores are LLM-judged, and the judge "runs three times with mean and standard" deviation reported.[^c19]
- The representation is weaker where the signal is a user's manner rather than a fact. The authors write that "weaker performance on single-session preference questions highlights a limitation" of "a purely event-centric representation for capturing finegrained user attitudes and styles".[^c20][^c21]
- An EDU is not a transcript. The extractor may "include lightly inferred information", so an extraction error is stored as a fact and retrieved as one.[^c22] The text does not measure the extractor's error rate. (my inference)
- "Non-compressive" holds for the store, not for the answering context. The paper says it "intentionally avoids lossy compression",[^c23] but only 509–1039 tokens reach the answerer, so selection at query time is a compression of a different kind. (my inference)
- The graph is sparse: "EDU nodes connect to only a handful of arguments".[^c24] The authors guess that "producing more normalized, atomic arguments could form a more dense graph", and do not test it.[^c25]
- The indexing cost of running an LLM over every session and every EDU is not reported in the part read. The token figures concern the QA prompt only. (my inference)

## Related

- [[candidate-set-narrowing-recall]] — the recall-biased EDU filter is a narrowing step, and the same recall ceiling applies to it.
- [[spreading-activation-retrieval]] — the graph step in EMem-G is personalized PageRank over the event graph, a relative of spreading activation.

[^c1]: arxiv-2511-17208 — "self-contained statements with normalized entities and source turn attributions"
[^c2]: arxiv-2511-17208 — "the set of turn indices in s that support e"
[^c3]: arxiv-2511-17208 — "is a timestamp derived from the session date"
[^c4]: arxiv-2511-17208 — "the timestamp is inferred based on the session timestamp"
[^c5]: arxiv-2511-17208 — "(Bob, stay in, Tokyo)"
[^c6]: arxiv-2511-17208 — "they fragment the original discourse"
[^c7]: arxiv-2511-17208 — "find and recombine several triples to reconstruct the event"
[^c8]: arxiv-2511-17208 — "lost or inconsistently represented"
[^c9]: arxiv-2511-17208 — "represented as an event with multiple arguments, rather than"
[^c10]: arxiv-2511-17208 — "fixed ontology of roles; the usage of rk is not explored in"
[^c11]: arxiv-2511-17208 — "returns an event type t(e) and a set of role–argument pairs"
[^c12]: arxiv-2511-17208 — "the overall LLM score improves from 0.744 for Nemori to 0.780"
[^c13]: arxiv-2511-17208 — "The gains concentrate on"
[^c14]: arxiv-2511-17208 — "only 509–1039 tokens to the backbone (average 738.2)"
[^c15]: arxiv-2511-17208 — "far below the 23,653-token full-context baseline"
[^c16]: arxiv-2511-17208 — "the LLM-based EDU filter is the most critical piece"
[^c17]: arxiv-2511-17208 — "LoCoMo contains 10 multi-session dialogues between"
[^c18]: arxiv-2511-17208 — "consists of 500 multi-session dialogues between user and assistant"
[^c19]: arxiv-2511-17208 — "The LLM-judge runs three times with mean and standard"
[^c20]: arxiv-2511-17208 — "single-session preference questions highlights a limitation"
[^c21]: arxiv-2511-17208 — "of a purely event-centric representation for capturing finegrained user attitudes and styles"
[^c22]: arxiv-2511-17208 — "include lightly inferred information"
[^c23]: arxiv-2511-17208 — "intentionally avoids lossy compression"
[^c24]: arxiv-2511-17208 — "EDU nodes connect to only a handful of arguments"
[^c25]: arxiv-2511-17208 — "producing more normalized, atomic arguments could form a more dense graph"
