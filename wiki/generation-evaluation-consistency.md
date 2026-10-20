---
description: "Generation-evaluation consistency is the rank correlation between how well LLMs generate and how well they judge, under one shared preference oracle; high values depend on oracle strength."
aliases: ["GE-consistency", "generation-evaluation consistency"]
sources: ["arxiv-2511-20604"]
---
# Generation-evaluation consistency

Fix a set of LLMs and one preference oracle, a judge whose verdicts count as the gold standard. Rank the models by generation: how their responses fare against a baseline's, as the oracle scores them. Then rank the same models by evaluation: how often each model's verdict on a pair of responses agrees with the oracle's verdict on that pair. The consistency is the correlation between the two rankings, "measured as the correlation between the performance rankings of LLMs when evaluated as generators" and as evaluators, computed with Spearman's rank coefficient.[^c1] The evaluation side is scored with Cohen's kappa rather than accuracy, because kappa "can better reflect model performance when the label distribution is unbalanced."[^c2]

The quantity belongs to a set of models, not to one model. The single-model relative, GV-consistency, is different: "GV-consistency is defined with a single LLM regarding its inherent consistency".[^c3] GE-consistency, by contrast, "is a ranking-level measure defined over a set of LLMs".[^c4] What it asks is whether order agrees: whether a model that evaluates better than another also generates better, "that performs better at evaluation than another also performs better at generation." Because only the order has to agree, the value can be high even where a single model's generation and evaluation disagree with each other. The paper notes that a high level "only requires a relative alignment between generation and evaluation abilities."[^c5]

The number is high only under an instance filter. The evaluation tasks are the oracle's own pairwise verdicts on each model's output against the baseline, with each pair judged in both orders. A pair is kept only when the oracle gives the same verdict in both orders, a filter "based on the self-(in)consistency of the preference oracle."[^c6] On 15 models with GPT-4o as oracle, that filter removes "58.3% and 50.7% of instances" on AlpacaEval and Arena-Hard.[^c7] The paper reports Spearman correlations of 0.839 on AlpacaEval and 0.971 on Arena-Hard after filtering.[^c8] Without the filter they are 0.743 and 0.793, and the authors say the correlation "drops significantly without it."[^c9] Their explanation is that the filter removes "two types of unreliable instances," among them "cases where the preference oracle is uncertain and effectively guessing."[^c10][^c20]

The oracle sets the level. With other models as oracles the consistency changes, "with larger, more capable LLMs leading to higher GE-consistency in general."[^c11] The paper's intuition is that a weak oracle gives little to correlate: a weaker oracle "produces random evaluations will yield zero GE-consistency."[^c12]

The use the paper makes of the pattern is to score models only as judges, against labels the oracle has already produced. Since the evaluation instances are fixed, this "allows evaluating various LLMs without requiring an LLM judge to directly assess their generated outputs."[^c13] Combined with a rule-based benchmark, the paper reports a Spearman of 0.94 with Chatbot Arena rankings "across 23 LLMs."[^c14]

## Limits

- The headline rests on one oracle, GPT-4o, and on 15 models. The paper's main claim is a rank correlation over that small set. The parts read give no confidence interval, and a Spearman over 15 points has wide uncertainty (my inference).
- The reported value is conditional on the filter. More than half the instances are discarded, and the correlation is measured on what survives. On Arena-Hard the same models give 0.793 unfiltered. The filter is what separates the strong result from a moderate one in this data.
- The gold standard is circular. The oracle produces both rankings, so a high value shows that the two roles agree under that oracle. It does not show that either ranking matches humans (my inference). The paper's own caveat about its external check is that "We note that Chatbot Arena is not a true" gold standard.[^c15]
- The pattern depends on the instructions. AlpacaEval, with more open-ended instructions, gives lower consistency than Arena-Hard, which the authors attribute to the difference in instruction type: "This makes evaluation on the latter" more objective.[^c16] The WildBench check (0.938) is still a pairwise instruction-following setting, so open-ended tasks with no clear winner are not tested.
- The benchmark built on the pattern is, in the authors' words, "a proxy evaluation by design and may be vulnerable to adversarial attacks."[^c17] They note that "fine-tuning an LLM to act as a judge could artificially boost its" ranking without better alignment.[^c18]
- The authors' larger hope is untested here: "consistency holds during training, it suggests the feasibility of self-improvement."[^c19] Training was not examined in this work, so self-improvement is a hypothesis the paper poses, not a result.

## Related

- [[generation-verification-gap]] — the same asymmetry question for proofs, whether checking is easier than producing; GE-consistency asks whether the two roles rank models alike, not whether one is easier.
- [[llm-judge-biases]] — the order swap that the filter reuses; there a verdict that flips is scored as a tie, here the pair is dropped from the evaluation set.
- [[chance-corrected-agreement]] — Cohen's kappa, the agreement statistic on the evaluation side.
- [[llm-judge-validation-gap]] — asks whether single LLM judgments are checked against humans; GE-consistency asks whether a judge's ranking of models lines up with its own generation ranking.

[^c1]: arxiv-2511-20604 — "measured as the correlation between the performance rankings of LLMs when evaluated as generators"
[^c2]: arxiv-2511-20604 — "can better reflect model performance when the label distribution is unbalanced"
[^c3]: arxiv-2511-20604 — "GV-consistency is defined with a single LLM regarding its inherent consistency"
[^c4]: arxiv-2511-20604 — "GE-consistency is a ranking-level measure defined over a set of LLMs"
[^c5]: arxiv-2511-20604 — "it only requires a relative alignment between generation and evaluation abilities"
[^c6]: arxiv-2511-20604 — "based on the self-(in)consistency of the preference oracle"
[^c7]: arxiv-2511-20604 — "58.3% and 50.7% of instances, respectively, are filtered out"
[^c8]: arxiv-2511-20604 — "demonstrate a 0.839 and 0.971"
[^c9]: arxiv-2511-20604 — "the correlation between generation and evaluation rankings drops significantly without it"
[^c10]: arxiv-2511-20604 — "the filtering process removes two types of unreliable instances"
[^c11]: arxiv-2511-20604 — "with larger, more capable LLMs leading to higher GE-consistency in general"
[^c12]: arxiv-2511-20604 — "produces random evaluations will yield zero GE-consistency"
[^c13]: arxiv-2511-20604 — "This allows evaluating various LLMs without requiring an LLM judge to directly assess their generated outputs"
[^c14]: arxiv-2511-20604 — "rankings across 23 LLMs"
[^c15]: arxiv-2511-20604 — "We note that Chatbot Arena is not a true"
[^c16]: arxiv-2511-20604 — "This makes evaluation on the latter"
[^c17]: arxiv-2511-20604 — "it is a proxy evaluation by design and may be vulnerable to adversarial attacks"
[^c18]: arxiv-2511-20604 — "fine-tuning an LLM to act as a judge could artificially boost its"
[^c19]: arxiv-2511-20604 — "consistency holds during training, it suggests the feasibility of self-improvement"
[^c20]: arxiv-2511-20604 — "cases where the preference oracle is uncertain and effectively guessing"
