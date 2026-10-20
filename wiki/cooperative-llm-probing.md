---
description: "An abstain decision is produced by asking several LLMs, each specialised into a domain, to critique a proposed answer, then having a judge LLM synthesise their feedback."
aliases: ["COOPERATE", "cooperative probing"]
sources: ["feng-2024"]
---
# Cooperative LLM probing (COOPERATE)

> Instead of a single model reflecting on its own answer, Feng et al. (2024) have several LLMs — one specialised per knowledge domain — write feedback on the answer, and a separate judge LLM turns that feedback into an abstain decision.

## Definition / Mechanism

Given a question $q$ and an LLM's answer $a = \mathrm{LLM}(q)$, the model is prompted to specialise into $k$ experts on domains $d_1,\dots,d_k$ (self-specialisation), or $k$ separate LLMs are used directly. Each expert $i$ generates a domain-focused knowledge passage $\mathrm{knowledge}_i$ about $q$, then produces feedback $f^i = \mathrm{LLM}(\mathrm{knowledge}_i, q, a)$ acting as a reviewer. A judge LLM synthesises the set of feedback $\{f^1,\dots,f^k\}$ into a binary decision, $\mathrm{LLM}(q,a,\{f^1,\dots,f^k\}) \to \{\text{accept}, \text{reject}\}$; reject means the model abstains.[^c1]

Across three LLMs (Mistral-7B, LLaMA2-70B, ChatGPT) and four QA datasets (MMLU, Knowledge Crosswords, Hellaswag, Propaganda), COOPERATE and its competitive counterpart [[competitive-llm-probing|COMPETE]] together beat the strongest of 11 prior single-model abstain baselines ([[calibration]], training, prompting, self-consistency) in 9 of 12 model/dataset settings on reliable accuracy, an average improvement of 10.1%, and up to 19.3% on abstain accuracy against the strongest baseline.[^c2]

COOPERATE's advantage grows with base-model strength: it works better with ChatGPT than with the two weaker open models, which the authors attribute to the multi-step feedback-generation process needing a capable base model to execute reliably.[^c3]

## Why it matters

This is a named mechanism for stall 2's "whom to ask next" question answered with **another model, not a human or a document**: the constraint that decides whether to answer or abstain is elicited by querying peer LLMs rather than by thresholding the model's own confidence (as calibration-based [[abstention]] does) or its own self-reflection (which the paper's introduction reports is unreliable due to confirmation bias). It gives the asker-selection literature on this stall a concrete alternative to both static thresholds and single-model self-critique: distribute the question about "do I actually know this" across several differently-specialised copies of the asking model itself.

## Limits

- The claim that COOPERATE beats single-model baselines rests on evaluation against 11 baselines the authors themselves re-implemented and adapted for abstention; none is a purpose-built multi-model baseline, so the comparison is COOPERATE against single-model methods, not against other multi-model methods.
- The domain specialisation $d_1,\dots,d_k$ is prompted, not learned or verified — nothing here checks that a "domain expert" prompt actually produces domain-relevant knowledge, only that the resulting feedback improves the downstream abstain accuracy.
- Results are reported only for the four tested QA datasets and three tested LLMs; the paper's own analysis notes several single-model baselines collapse outside MMLU (propaganda detection, long-context multi-hop), so generalisation of COOPERATE's advantage to other question formats (open-ended generation rather than QA) is untested here.

## Related

[[abstention]] · [[competitive-llm-probing]] · [[calibration]] · [[semantic-entropy]]

[^c1]: feng-2024 — "the LLM employs other models to provide feedback on the proposed answer and reasoning, and synthesizes the outputs into an overall abstain decision"
[^c2]: feng-2024 — "C OOPERATE and C OMPETE achieve the best performance in 9 of the 12 settings in terms of reliable accuracy."
[^c3]: feng-2024 — "We find that C OOPERATE works better with stronger models such as ChatGPT: we hypothesize that the complexities of the multi-step feedback generation warrant a stronger base LLM."
