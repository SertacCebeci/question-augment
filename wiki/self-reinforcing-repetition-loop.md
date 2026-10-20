---
description: "Under greedy decoding a repetitive pattern raises its own next-token probability, so generation can lock into a loop with no exit; a multi-path search can keep an escape candidate alive."
aliases: ["repetition loop", "repeater problem", "LLM repetition problem", "degenerate repetition", "repetition trap"]
sources: ["arxiv-2512-04419", "arxiv-2511-21591"]
---
# Self-reinforcing repetition loop

A generator that has begun to repeat can stop being able to stop. The account in this work is a positive feedback: the probability of a repeated continuation grows with each repetition, so the repeated pattern comes to dominate the next choice. The authors describe the effect as "the probability of repetition increases monotonically with the number of historical repetitions, creating a positive feedback loop."[^c1] In their production case the loop ran until the token limit: generation "continues until reaching the maximum token limit (max_tokens)."[^c2]

The mechanism is concrete at the level of one decoding rule. Greedy decoding takes the highest-probability token at each step, so once the repeated continuation is the more probable one, it is always taken: "For greedy decoding, once pr (t) > pn (t), the algorithm will always select the repetitive" continuation.[^c2] The authors' Markov chain has a repetitive state from which the expected escape time is infinite, and they read this as the reason greedy decoding "cannot break out of repetition loops."[^c3] The reason given is structural. Greedy decoding "maintains only one candidate sequence, so once a repetitive pattern begins, there is no mechanism to explore alternative paths."[^c4]

What changes the outcome, on this account, is keeping more than one path. A beam search holds several candidates at once and ranks them by cumulative log-probability, so a repeated path is not the only one in play. The paper's claim is conditional: "With beam width B ≥ 2 and proper early stopping, Beam Search can escape repetitive" loops, but only "provided that the initial probability gap between repetitive and non-repetitive continuations is bounded."[^c5] The stopping rule matters inside this claim. With early stopping the search ends once B complete sequences exist, which the authors take to keep a non-repetitive candidate in the set "if it exists in the top-B candidates."[^c6] Their runs show the sensitivity: with the stopping rule on, the repetition rate was 0%, and with it off it was 60%.[^c7]

The same loop is reached from a different side by a token-level penalty and by fine-tuning. A penalty on tokens that "have already appeared in the generated text" lowers the chance of repeating them,[^c8] and the paper finds it works only on one of its three repetition types. The fine-tuning route changes the model's preferences rather than the search, and the paper presents it as the one covering all three. What these levers share is that each acts on a different place in the generator: the search rule, the token scores, or the weights.

The concept generalises beyond this paper only as far as the mechanism does. Any answerer whose next step is made more likely by its own previous step can, under a single-path commitment rule, fail to stop. Whether a human or a multi-step reasoner shows the same lock-in is not something this work measures.

## Limits

The Markov account is the authors' own simplification. They concede "Context-dependent effects not fully captured by the simplified Markov model,"[^c9] and their agreement table uses fixed parameters ("Markov model with γ = 0.15, rmax = 10"). I read the agreement as the same production deployment checked against its own model, not an independent test.

The escape guarantee is conditional on an initial probability gap that the paper assumes bounded, not measured. Its minimum beam width formula treats each candidate as an independent chance to escape; the text does not justify that independence, and I did not find it argued elsewhere in the sections I read.

The evidence is small and single-context. The test sets were "BC1=30, BC2=25, BC3=28" cases from one batch-code-interpretation deployment, with one serving framework and one fine-tuning setup.[^c10] The base model is not named in the passages I read. Results on open-ended text, on other tasks, or on other models are not shown. The authors themselves say the search-stopping lever "addresses symptoms" and does not change "root causes."[^c11]

A different setting shows loops outside this account. In the 8-puzzle study of arxiv-2511-21591, the models looped while sampling at "a temperature of 1.0, and identical system prompts"[^c13], and they kept looping with an explicit instruction against repeating moves and a list of legal moves in the prompt: "even when given a list of valid moves, an explicit instruction not to repeat moves, and their previous move, the models continued to loop."[^c12] That study does not run greedy decoding, so it neither confirms nor rejects the probability account. My inference: a loop can also be a failure to follow the model's own stated constraint, which the decoding argument does not describe.

## Related

- [[stop-continue-criteria-in-retrieval-loops]] — stopping rules for retrieve-reason loops; a budget stop, where this note is about a token-probability trap that a budget can cut short but not explain
- [[moderate-adaptive-reasoning-length]] — triggers a stop on repeated "wait" tokens, a reasoning-level intervention on a similar loop
- [[ungrounded-reasoning-gap-ratio]] — how far a trace keeps going after it should have stopped
- [[beam-search-context-training]] — also keeps K candidates and prunes them, but over contexts for a tool-using optimiser, not over tokens

[^c1]: arxiv-2512-04419 — "monotonically with the number of historical repetitions, creating a positive feedback loop."
[^c2]: arxiv-2512-04419 — "For greedy decoding, once pr (t) > pn (t), the algorithm will always select the repetitive"
[^c3]: arxiv-2512-04419 — "the expected escape time is infinite, explaining why greedy decoding"
[^c4]: arxiv-2512-04419 — "Single-Path Exploration: Greedy decoding maintains only one candidate sequence, so once a repetitive pattern begins, there is no mechanism to explore alternative paths."
[^c5]: arxiv-2512-04419 — "With beam width B ≥ 2 and proper early stopping, Beam Search can escape repetitive"
[^c6]: arxiv-2512-04419 — "at least one non-repetitive sequence is preserved if it exists in the top-B candidates."
[^c7]: arxiv-2512-04419 — "early_stopping=True achieves 0% repetition rate, while"
[^c8]: arxiv-2512-04419 — "have already appeared in the generated text, reducing their probability of being selected"
[^c9]: arxiv-2512-04419 — "Context-dependent effects not fully captured by the simplified Markov model"
[^c10]: arxiv-2512-04419 — "Test cases: BC1=30, BC2=25, BC3=28."
[^c11]: arxiv-2512-04419 — "though it addresses symptoms"
[^c12]: arxiv-2511-21591 — "even when given a list of valid moves, an explicit instruction not to repeat moves, and their previous move, the models continued to loop"
[^c13]: arxiv-2511-21591 — "a temperature of 1.0, and identical system prompts"
