---
description: "A model that binds a question's slot to an entity can follow salience (position, emphasis, tone) instead of relevance; when the two are decoupled with facts intact, wrong bindings follow."
aliases: ["salience-relevance conflation", "salience channel"]
sources: ["doi-10-48550-arxiv-2607-17535"]
---
# Salience-relevance decoupling

When a language model must decide which entity fills a slot in a question, it has no schema to look the answer up in. It reconstructs the binding from the text around the candidates, and that text carries two things that usually agree but need not. One is relevance: how well a candidate's relation to the document's subject matches the slot. The other is salience: how the candidate is presented, through position, structural emphasis, tonal certainty and closeness to query terms.[^d1] The source calls the second dimension the salience channel, the way assertions are presented rather than what they assert.[^d2]

The source writes the binding as a score that adds the two terms, with weights it calls the model's implicit weighting. The argument is that a candidate wins the slot when its combined score is highest.[^d3] The two terms are normally correlated: "Under normal authorship, salience and relevance are correlated:" important facts are placed early, put under headings, and stated with confidence.[^d4] A model that treats salience as a heuristic for relevance therefore does well on ordinary documents.[^d5]

The break comes when the two are pulled apart on purpose. The source calls this salience-relevance decoupling: "the agent can follow the salient entity instead of the relevant one."[^d6] The mechanism is concrete. A candidate's relevance is fixed by its relation to the slot. An edit that changes only presentation, with every factual claim left true, can change the salience term and leave relevance untouched. The source states the flip condition as a comparison of a relevance gap with a salience gap, and it says the attacker can flip the binding "whenever" the weighted salience gap exceeds the weighted relevance gap.[^d7]

The source reports the prediction it tested. Attack success should fall as the relevance margin between the true entity and the decoy grows. On its test set the success rate was "ASR drops from 95.8%" where the decoy's relationship to the slot was compatible, and it fell to 68.8% where it was not, a gap the source reports as "a 27.0 pp gap significant at" p<0.001.[^d8] The decoupling has a precondition. The source says the surface exists "when two conditions hold at the target hop:" a type-compatible decoy must sit in a comparable relational role, and the relevance margin must be small enough for presentation to overcome.[^d9]

The reason it resists the usual remedy is also the source's argument. Salience cues "to be stable under deterministic decoding," so repeated sampling of the same reading tends to return the same wrong binding rather than reveal it.[^d10]

My inference, not the source's claim: the same confusion applies to an answerer who chooses among true statements by where they sit in the text. [[situational-relevance]] makes the same separation at the retrieval end, between closeness to a query and usefulness for a task. [[salience-control]] measures a prompt moving which evidence a fixed model foregrounds; this note is the binding-level case, where the moved cue sits in the document rather than the prompt. [[reader-slot-zero-primacy]] measures position alone as a cue that decides which evidence a reader uses. [[entity-attribute-transfer-from-retrieved-text]] shows a look-alike entity lending its attributes to the right one; here the look-alike is made more prominent. [[anchor-salience-bias]] is the same channel on the asker's side, where a question generator picks spans by surface presentation.

## Limits

- The score is an abstraction. The source says it does "not claim that LLMs internally compute a linear combination of these terms," and that the model "remains a structured abstraction rather than a mechanistic account of internal representations."[^d11]
- The test set is 144 samples over two domains. A 30-sample news pilot is reported, and "and geopolitical verticals remains future work."[^d12]
- The decoupling was produced by adversarial edits with black-box query access. The claim that salience "behaves correctly on benign documents" is the source's assertion; in the parts I read I found no separate measurement of benign error rates.[^d5]
- The evaluation is a single snapshot of models: "the evaluation captures a snapshot of current frontier" models.[^d13]
- Whether human readers bind entities the same way under the same edits is not tested. The note's claim is about the model in the source's experiments.

## Related

- [[binding-error-cascade]] — what a single decoupled binding does downstream in a multi-hop chain
- [[situational-relevance]] — relevance separated from semantic closeness at retrieval time
- [[salience-control]] — a prompt moves which evidence is foregrounded; the prompt-side analogue
- [[entity-attribute-transfer-from-retrieved-text]] — look-alike entities lend attributes in retrieval-augmented VQA
- [[reader-slot-zero-primacy]] — position alone changes which evidence a reader uses
- [[anchor-salience-bias]] — surface presentation steers question generators toward a span

[^d1]: doi-10-48550-arxiv-2607-17535 — "structural emphasis, tonal certainty, and semantic-proximity to"
[^d2]: doi-10-48550-arxiv-2607-17535 — "to this dimension of the retrieved context as the salience channel,"
[^d3]: doi-10-48550-arxiv-2607-17535 — "an operational framework whose value lies in organizing the attack surface into independently manipulable factors"
[^d4]: doi-10-48550-arxiv-2607-17535 — "Under normal authorship, salience and relevance are correlated:"
[^d5]: doi-10-48550-arxiv-2607-17535 — "relevance therefore behaves correctly on benign documents."
[^d6]: doi-10-48550-arxiv-2607-17535 — "the agent can follow the salient entity instead of the relevant one."
[^d7]: doi-10-48550-arxiv-2607-17535 — "The attacker can flip the binding whenever:"
[^d8]: doi-10-48550-arxiv-2607-17535 — "ASR drops from 95.8%"
[^d8b]: doi-10-48550-arxiv-2607-17535 — "a 27.0 pp gap significant at"
[^d9]: doi-10-48550-arxiv-2607-17535 — "when two conditions hold at the target hop:"
[^d10]: doi-10-48550-arxiv-2607-17535 — "to be stable under deterministic decoding"
[^d11]: doi-10-48550-arxiv-2607-17535 — "but it remains a structured abstraction rather than a mechanistic account of internal representations."
[^d12]: doi-10-48550-arxiv-2607-17535 — "and geopolitical verticals remains future work."
[^d13]: doi-10-48550-arxiv-2607-17535 — "the evaluation captures a snapshot of current frontier"
