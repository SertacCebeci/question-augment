---
description: "Questions are iteratively rewritten to maximize disagreement between a weak model and a document-grounded expert, giving a compact gap-targeted training set that beat larger synthetic corpora."
aliases: ["adversarial question generation", "agentic adversarial QA", "TextGrad-inverted question optimization"]
sources: ["arxiv-2602-18137"]
---
# Expert-divergence adversarial question refinement

A question is worth asking, for training, where the learner and a stronger reference part ways. The method takes a domain document C, a strong "expert" model and a weak target model, both given C. For each current question it gets both answers and has a feedback model compare them for correctness, coverage and contextual reasoning. The question is then rewritten so that this disagreement grows.[^c1] The objective is stated as generating and iteratively refining questions that "maximize divergence between the responses of these models".[^c2]

## Mechanism

Each refinement step has two stages. A guidance model turns the feedback into a natural-language editing instruction on how to revise the question to accentuate weaknesses of the target. A revision model then applies that instruction to produce the next question.[^c3] This borrows TextGrad's backward and step modules but inverts the direction: TextGrad minimizes a task loss, while here the loss is interpretive disagreement and is maximized.[^c4] All three auxiliary roles are the same strong LLM under different prompts.[^c5]

After T rounds the final questions are paired with the expert's answers (the expert sees C) and the weak model is fine-tuned on them. The expert is a stand-in for a model that always holds the whole corpus, which is impractical to deploy, so the pairs transfer that expertise into a lightweight model.[^c6]

## Why it is meant to help

The authors' diagnosis is that generic augmentation reinforces what the model already knows: "much of the augmented data might reinforce knowledge the model already possesses".[^c7] A model can define a term correctly yet fail a scenario that integrates several clauses. A question aimed at that scenario exposes a limit that a definitional question would not. The authors liken this to an oral examination versus memorized written recall.[^c8]

## Measured

On three CUAD contracts in LegalBench (491 questions, 36 tasks), with LLaMA3-8b, the method reached 82.7 average accuracy at 96k tokens, against 69.5 with no extra data. EntiGraph reached 79.6 at 6.7M tokens, Knowledge-Instruct 75.0 at 159k, and uninformed model-independent questions 75.8 at 147k.[^c9] The text summarizes this as an 18.99% gain over the base model and 3.89% over EntiGraph, with "≈70× fewer training tokens".[^c10] More refinement rounds gave progressively higher accuracy: "additional refinement iterations result in progressively higher accuracy".[^c11]

The comparison with uninformed questions is the closest control for the adversarial step itself. Same-style questions without disagreement-driven refinement scored lower (75.8 vs 82.7) at comparable token counts. This is my reading of the table, not a claim the authors test separately.

## Limits

- One benchmark (three contracts), one 8B student, a workshop paper; no variance, seeds or significance reported in the text I read.
- The expert is the same family of strong LLM as the guidance and feedback roles, so expert errors are imported as training targets; no check of expert answer correctness is described.
- Disagreement is a proxy: a question can be hard or ambiguous for the weak model without the expert being right. The paper does not separate real comprehension gaps from underspecified questions.
- Token counts are not matched across baselines, so efficiency and quality are confounded; the contribution of the iteration versus the expert answers alone is only indirectly probed.
- Fine-tuning and test are on the same contract, so this measures document-specific memorization plus reasoning, not general transfer.

## Related

- [[reducible-context-gap-disagreement]] — disagreement between models as a signal of what is reducible
- [[learnability-posterior-curriculum]] — selecting what to train on by how much the learner can still gain
- [[evidence-chain-question-generation]] — another way of generating questions that force multi-step reasoning over a document

[^c1]: arxiv-2602-18137 — "which is typically instantiated as a"
[^c2]: arxiv-2602-18137 — "maximize divergence between the responses of these models"
[^c3]: arxiv-2602-18137 — "applies this instruction to update the current question"
[^c4]: arxiv-2602-18137 — "our framework inverts this direction and explicitly"
[^c5]: arxiv-2602-18137 — "using the same strong LLM, each configured with a distinct instruction prompt"
[^c6]: arxiv-2602-18137 — "our aim is to transfer domain expertise from this strong oracle model to a"
[^c7]: arxiv-2602-18137 — "much of the augmented data might reinforce knowledge the model already possesses"
[^c8]: arxiv-2602-18137 — "an adversarial question targeting this scenario reveals such interpretive limitations"
[^c9]: arxiv-2602-18137 — "Paraphrase ×6"
[^c10]: arxiv-2602-18137 — "≈70× fewer training tokens"
[^c11]: arxiv-2602-18137 — "additional refinement iterations result in progressively higher accuracy"
