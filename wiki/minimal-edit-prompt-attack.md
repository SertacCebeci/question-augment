---
description: "Small meaning-preserving rewordings of a question, searched with MCTS against answer margin, flip a medical VLM's correct answers; low-margin items flip first, and a smaller editor flips more."
aliases: ["LLM-driven prompt attack", "prompt-edit attack", "clinically plausible prompt perturbation"]
sources: ["arxiv-2603-21047"]
---
# Minimal-edit prompt attack

A black-box way to measure how much a model's answer depends on the exact wording of a question. An LLM proposes three small edits to the current question (synonyms, punctuation, stopwords, word-order tweaks of at most four tokens, answer labels untouched). A Monte Carlo Tree Search picks which edit to extend, rewarding the drop in the target model's margin between the true answer and the runner-up. The attack succeeds when the predicted label stops matching the ground truth.[^c1]

## Mechanism

Each node is a candidate question and each edge one edit. The target model scores every candidate answer by the summed log-probability of its tokens given the question. The reward is the gap between the top-1 (true label) and top-2 options, backpropagated along the path. Selection uses UCT with exploration constant 1.4, up to 80 iterations and depth 8.[^c2] Only items the model answered correctly beforehand are attacked.[^c3]

## What was measured

On the 1,305-pair disease-diagnosis subset of U2-Bench, three medical VLMs (MedGemma-4B, LLaVA-Med-7B, QoQ-Med-7B) lost 14.89 to 26.08 points of absolute accuracy from a baseline near 40%. With Qwen-7B as editor, accuracy fell from 42.22% to 13.72% on one model.[^c4]

Most successes arrive after only two or three edits. Stopping at depth 1 (no search) leaves LLaVA-Med at 33.33% accuracy, against 13.72% with MCTS.[^c5] So a single rewording often does not suffice, but a short chain of near-synonymous rewordings does.

Attack success tracks confidence. Failed attacks sit at high logit margins, and successes concentrate at low margins. The authors read the margin as a proxy for distance to the decision boundary.[^c6]

Editor size runs the other way from what one would expect. The smaller Qwen-7B was a more effective attacker than Qwen-30B. The authors report that Qwen-30B produces more conservative, meaning-preserving rewrites that adhere more closely to the instruction.[^c7] Once successes are restricted to fluent edits (perplexity below 15, against 10.48 for the original questions), the gap narrows substantially. The authors read this as the smaller editor's extra wins coming from less natural, less minimal edits.[^c8]

## Limits

- Only multiple-choice ultrasound diagnosis, three target models and three editors. The conclusion names report generation and other modalities as future work.[^c9]
- The edit being "clinically plausible" is judged by perplexity and embedding cosine similarity (0.97 to 0.996), not by clinicians. Whether the edits are the typos and shorthand real users write is my inference, not tested here.
- The explanation for why the smaller editor wins is qualitative inspection, not a controlled test.
- Some attacker outputs drifted into other languages or gibberish; perplexity filtering removed most.[^c10]
- The margin finding is correlational. The proposed mitigations (prompt-invariance post-training, margin-aware fine-tuning) were not tested.

## Related

- [[cross-model-perplexity]] — perplexity as a fluency measure of text
- [[survey-response-model]] — human question-wording effects, the analogue the model-side result echoes
- [[retrieval-cue-disruption]] — another case where small wording changes alter model outputs
- [[interaction-vs-encoding-bias]] — wording sensitivity located in the query side

[^c1]: arxiv-2603-21047 — "Suggest minimal edits to the user's question while preserving meaning."
[^c2]: arxiv-2603-21047 — "MCTS uses up to 80 iterations, maximum depth 8, and exploration constant c = 1.4."
[^c3]: arxiv-2603-21047 — "we restrict our pipeline to instances that the model answers correctly before attack"
[^c4]: arxiv-2603-21047 — "post-attack accuracy decreases by 14.89%–26.08% in absolute terms"
[^c5]: arxiv-2603-21047 — "accuracy increases from 13.72% (with MCTS) to 33.33% without MCTS"
[^c6]: arxiv-2603-21047 — "failures dominate at higher margins, indicating that high-confidence examples are harder to manipulate"
[^c7]: arxiv-2603-21047 — "Qwen-7B produces more effective attacks (lower post-attack accuracy) than Qwen-30B"
[^c8]: arxiv-2603-21047 — "those edits are less likely to remain minimal and linguistically natural under a strict fluency constraint"
[^c9]: arxiv-2603-21047 — "Future work will extend this evaluation to tasks such as report generation"
[^c10]: arxiv-2603-21047 — "most language-confused outputs are removed by perplexity-based filtering"
