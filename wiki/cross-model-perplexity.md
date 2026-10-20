---
description: "A second model's single-forward-pass surprise at a generator's answer tokens flags confident errors that the generator's own entropy cannot see, with no labels and no verifier generation."
aliases: ["CMP", "cross-model entropy", "CME", "cross-model disagreement", "verifier surprise"]
sources: ["arxiv-2603-25450"]
---
# Cross-model perplexity

A generator model answers a prompt; a different verifier model reads the prompt and that answer in one forward pass (no generation). Cross-Model Perplexity (CMP) is the exponentiated mean negative log-probability the verifier gives the generator's answer tokens; Cross-Model Entropy (CME) is the verifier's mean entropy at those same positions. High values mean the two models disagree, and the answer is likely wrong.[^c1] CMP is the surprise at the specific tokens produced; CME is the general uncertainty at those positions.[^c2]

## Why it sees what self-uncertainty misses

A model that is wrong but certain has low entropy whatever its correctness, so any signal from the generator's own distribution is blind to confident errors.[^c3] On MMLU (OLMo-7B to Llama-8B), CMP in the "generator wrong only" case is 154 times the both-correct baseline, while generator entropy varies by at most 1.0x across the four outcome cases. Generator entropy rises whenever the generator is uncertain, whether or not the verifier agrees; CMP spikes only when the generator's error is not shared by the verifier.[^c4]

## Measured performance

On MMLU, CMP beats generator entropy on 12 of 15 model pairs by AUROC (mean 0.727 versus 0.595).[^c5] CME leads on TriviaQA with context; CMP is better where errors are localized in a few tokens (multiple choice, closed-book recall).[^c6] Among single-prefill signals, CMP or CME has the highest AUROC on every benchmark, and the explicit "is this true?" verifier prompt (P(True)) sits near chance. Generation-based baselines (verifier answer agreement, semantic entropy) reach higher AUROC on some tasks, at much higher cost.[^c7] As a routing signal, queries go to the stronger model only when disagreement is high, with no router training and no preference labels.[^c8]

## Diversity versus capability gap

On MMLU, CMP AUROC is uncorrelated with the accuracy gap between the models (rho = +0.12). The best pairs are same-size models from different families, which the authors read as models from different families making different confident errors.[^c9] On TriviaQA the correlation is positive (rho = +0.63): open-ended recall needs a verifier that knows what the generator does not, and a same-size peer may share its knowledge gaps.[^c10] The mechanism the authors name is training diversity on closed-choice tasks and verifier knowledge on open recall. The first is their interpretation, not an isolated test.

## Limits

- It needs a verifier whose distribution is a better proxy for correctness than the generator's. Every tested pair had a non-negative gap, and a Mistral to Qwen TriviaQA pair with a 1pp gap scored CMP AUROC 0.42, so the signal may degrade or invert when the gap shrinks or reverses.[^c11]
- Token-level scoring is sensitive to paraphrase: CMP can penalize wording the verifier would not have produced rather than the answer. CME is more robust.[^c12]
- Only greedy decoding on static benchmarks was tested. Sampled outputs, long chain-of-thought, and code were not. GSM8K AUROCs are modest (about 0.62).[^c13]
- Where labeled routing data exists, supervised routers remain the appropriate choice.[^c14]
- Which of CMP or CME fits which failure mode has no theory yet. The task-structure pattern is empirical.

## Related

- [[cross-model-epistemic-divergence]] — also uses other models to catch confident, self-consistent errors, but from sampled text rather than verifier token probabilities
- [[cross-model-answer-disagreement-entropy]] — disagreement across several models' generated answers, used to find ambiguous queries
- [[black-box-correctness-ceiling]] — a limit on correctness signals taken from one model's own outputs
- [[crc-confident-error-control]] — controls the same confident-error failure mode
- [[semantic-entropy]] — the generation-based within-model baseline that costs more

[^c1]: arxiv-2603-25450 — "High CMP indicates that Mv assigns low probability to M g ’s"
[^c2]: arxiv-2603-25450 — "Where CMP measures the verifying model’s surprise at the specific tokens produced, CME"
[^c3]: arxiv-2603-25450 — "Within-model uncertainty signals are blind to this case by construction, since a confident model has low"
[^c4]: arxiv-2603-25450 — "CMP selectively spikes only when the generator’s error is not shared by"
[^c5]: arxiv-2603-25450 — "On MMLU, CMP wins 12 of 15 pairs"
[^c6]: arxiv-2603-25450 — "CMP wins on tasks"
[^c7]: arxiv-2603-25450 — "P(True), despite operating in the same compute regime, performs near"
[^c8]: arxiv-2603-25450 — "zero labeled data, zero router training, one verifier prefill per query."
[^c9]: arxiv-2603-25450 — "models from different families make different confident errors, and CMP captures this disagreement regardless of"
[^c10]: arxiv-2603-25450 — "may share the same knowledge gaps, reducing the informativeness of its surprise."
[^c11]: arxiv-2603-25450 — "suggests signal degrades as the gap"
[^c12]: arxiv-2603-25450 — "Token-level scoring is also sensitive to paraphrase"
[^c13]: arxiv-2603-25450 — "Extending cross-model disagreement beyond"
[^c14]: arxiv-2603-25450 — "supervised routers"
