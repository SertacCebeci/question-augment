---
description: "A model runs a serial counting procedure only when the prompt obligates or permits it; with no counting cue, none of the LLMs tested counted spontaneously."
aliases: ["counting-strategy cue", "spontaneous versus cued enumeration", "prompt-licensed counting", "serial enumeration under instruction"]
sources: ["arxiv-2512-04727"]
---
# Enumeration cue dependence

Answering "how many" can run through a serial procedure: a one-to-one pairing of items with number symbols, a fixed order, and a count read off at the end. It can also run through an approximate estimate that never walks the items one by one. Hou, Zorzi and Testolin hold the sequence fixed and vary only the sentence that frames the count, across four conditions.[^e1] In the explicit condition the model "is obligated to count carefully and to use any" supportive strategy. In the spontaneous condition "the model receives no guidance regarding counting".[^e9] In the mental condition it "is allowed to count, but only" covertly, with no visible symbols. In the forbid condition it "is explicitly instructed not to count or use any" structure that aids counting.[^e10]

The cue decides which procedure, if any, runs. Without a cue, no tested model ran one. The abstract states that "none of them spontaneously engage in counting when simply asked" to enumerate a sequence,[^e2] and the authors call spontaneous counting "extremely rare and inconsistent" across tasks.[^e3] Under the explicit cue the top proprietary models reach "near-ceiling accuracy and minimal MAE, but only in the production task".[^e4] The task form matters here too: the cue lifts [[naming-production-asymmetry]] in one direction only. The mental cue falls between the two. Its accuracy is higher than in the spontaneous and forbid conditions, "suggesting that the models can" somehow improve their encoding of numerosity when they are told to count, even without marks.[^e5]

The cue also changes the mechanism, not only the output. In Llama 70B, principal components of the last-layer states show a step-tracking signal only under mental counting: "In the mental counting condition, PC1 and PC2 show a strong correlation with the" generated steps.[^e11] Under explicit counting the first component instead has "a periodic trend with large dips at steps that are multiples of ten", and "this gradual accumulation disappears during explicit counting".[^e6] The authors read explicit counting as one that "rather exploits an associative chaining mechanism that" carries the previously generated symbol forward, not an internal counter.[^e12] That reading rests on one model and one projection, and I give it as theirs.

The paper's own gloss is about framing: "most models appear to be sensitive not just to the operational" structure of a task "but also to the cognitive stance implied by the prompt".[^e7] For someone formulating a count question, the material is this. Whether an answer comes from a procedure or from an estimate depends on what the sentence licenses the answerer to do. "You may count, but only in your head" is a different licence from "count, with markers". My inference, not the paper's: the same split should hold for any task whose correct answer needs a serial pass over the input. The paper tests only counting.

## Limits

- The stimuli are repeated single items: one letter, or one five-letter word that is one token. Heterogeneous sequences are reported in a supplement, and the paper says "Performance is qualitatively similar, though homogeneous sequences seem slightly" harder.[^e13] I did not read that supplement.
- The cue is one section of a four-part system prompt. The paper does not isolate the cue sentence from the rest of the prompt.
- The mental-counting advantage is described as slight. The claim that models improve their encoding of numerosity is the authors' suggestion, not a measured mechanism.
- The mechanistic account (accumulation versus associative chaining) comes from one model, Llama 70B. The authors themselves say their signals "are not precise enough to guarantee accurate enumeration performance".[^e8]
- Nothing here shows the cue effect outside counting, or that every cue-free question fails in every domain.

## Related

- [[naming-production-asymmetry]] — the same cue lifts accuracy in production far more than in naming; task form and cue are two axes of one result.
- [[generic-meta-prompt]] — an instruction about how to reason; the counting cue is a sharper case, where the instruction decides whether a procedure runs at all.
- [[task-conditional-prompt-gain]] — prompt gains that change sign across tasks; here the gain is shown within one task family.

[^e1]: arxiv-2512-04727 — "The model is obligated to count carefully and to use any"
[^e2]: arxiv-2512-04727 — "none of them spontaneously engage in counting when simply asked"
[^e3]: arxiv-2512-04727 — "such behavior is extremely rare and inconsistent"
[^e4]: arxiv-2512-04727 — "near-ceiling accuracy and minimal MAE, but only in the production task"
[^e5]: arxiv-2512-04727 — "spontaneous and forbid counting conditions, suggesting that the models can"
[^e6]: arxiv-2512-04727 — "this gradual accumulation disappears during explicit counting"
[^e7]: arxiv-2512-04727 — "most models appear to be sensitive not just to the operational"
[^e8]: arxiv-2512-04727 — "signals are not precise enough to guarantee accurate enumeration performance"
[^e9]: arxiv-2512-04727 — "The model receives no guidance regarding counting"
[^e10]: arxiv-2512-04727 — "The model is explicitly instructed not to count or use any"
[^e11]: arxiv-2512-04727 — "In the mental counting condition, PC1 and PC2 show a strong correlation with the"
[^e12]: arxiv-2512-04727 — "rather exploits an associative chaining mechanism that"
[^e13]: arxiv-2512-04727 — "Performance is qualitatively similar, though homogeneous sequences seem slightly"
