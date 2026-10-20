---
description: "A scalar uncertainty report can give identical values for paradox, ignorance and contingency; asking the model to also declare what it cannot evaluate and why separates them."
aliases: ["declared losses", "absorption problem", "tensor-structured epistemic output", "S4 tensor extension"]
sources: ["arxiv-2604-09602"]
---
# Declared-loss uncertainty typing

Scalar uncertainty reports (here neutrosophic Truth, Indeterminacy, Falsity, each in [0,1]) say how much a model doubts, not what kind of doubt it is. The work defines the "Absorption problem": a model maps several distinct epistemic states to the same vector, typically T=0, I about 1, F=0.[^c1] Mistral Medium 3.1 gave (0, 1, 0) as its modal answer for the liar paradox (4/5 repetitions) and for ignorance (3/5).[^c2] The paper reports GPT-4o, the original study's flagship, showing the same pattern.[^c3]

## The mechanism

The remedy is an extended output (strategy S4): beside T/I/F, the model must list at least one "loss", a triple of what it cannot evaluate, why that limits the assessment, and a severity in [0,1].[^c4] Under Absorption the scalars are identical, but the "what" fields differ. Mistral's paradox losses were self-reference, formal-system dependency and grounding of "this sentence". Its ignorance losses were the unknowability of the number of stars and the definition of "universe".[^c5]

Across all five models (Claude Sonnet 4.6, Llama 4 Maverick, DeepSeek V3, Qwen3-235B, Mistral), the word-level Jaccard overlap of loss descriptions for paradox versus ignorance was below 0.10, whether or not the scalars separated the two.[^c6] The scalar Manhattan distance between those two phenomena was 0.000 for Mistral and 0.040 for Llama.[^c7] Losses also carried graded information: vagueness got lower severity (0.510) than paradox or ignorance (0.748 to 0.795).[^c8]

## Is it only instruction-following?

The author tested this. Across 125 S4 responses, the maximum declared severity correlated with I (Pearson r = 0.78) although the prompt does not ask for that coupling.[^c9] The mean-severity correlation was a stimulus-level confound and vanished after residualizing by stimulus (r = 0.02). Max severity survived it (r = 0.54).[^c10]

## What this means for asking and answering (my reading)

This is my inference, not a result of the paper. A single confidence or uncertainty number is a lossy channel. A respondent who also states which part of the question it cannot resolve gives the asker something to act on. Ignorance points to a fact that can be supplied. Paradox points to a premise that must be rewritten. Contingency points to a future that cannot be known. The paper does not test whether such typed reports change what an asker does next.

## Limits

- Five repetitions per cell, five phenomena and five models. The author calls the statistics exploratory.[^c11]
- Word-level Jaccard is crude. It could miss similar concepts in different words, or overstate differences between synonymous phrases.[^c12]
- Losses are self-reports. The paper offers no independent check such as logprobs, so models might produce plausible but generic text.[^c13]
- Prompts were rebuilt from descriptions, not the originals, so comparison with the earlier 35% hyper-truth rate (84% here) is cross-study and not an effect size.[^c14]
- The Absorption pattern is not shown to be general across models. Claude and DeepSeek separated paradox from ignorance on scalars alone.
- The paper does not test whether declared losses improve downstream decisions, abstention or clarification.

## Related

- [[sense-of-ignorance]] — a model's awareness of what it does not know, the internal state that losses try to report
- [[clarification-only-aleatoric-uncertainty]] — another case where the type of uncertainty, not its amount, decides the right response
- [[reasoning-contamination-of-verbalized-confidence]] — a limit on trusting verbalized self-reports
- [[log-score-verbalized-confidence-reward]] — scalar verbalized confidence, the format whose ceiling is argued here

[^c1]: arxiv-2604-09602 — "We define the Absorption problem as the case where a model maps multiple distinct epistemic states to the same scalar T/I/F vector, typically (T=0, I≈1, F=0)."
[^c2]: arxiv-2604-09602 — "Mistral Medium 3.1 predominantly exhibits Absorption across multiple phenomena in S1"
[^c3]: arxiv-2604-09602 — "The original study’s flagship model (GPT-4o) shows the same pattern: (T=0, I=1, F=0) for"
[^c4]: arxiv-2604-09602 — "The prompt explicitly requires at least one declared loss and states that “honesty about limits"
[^c5]: arxiv-2604-09602 — "The scalars are identical. The losses are domain-specific, accurate, and completely different."
[^c6]: arxiv-2604-09602 — "Every model produces nearly disjoint loss vocabularies for paradox vs. ignorance (Jaccard < 0.10)"
[^c7]: arxiv-2604-09602 — "Scalars identical; losses"
[^c8]: arxiv-2604-09602 — "Vagueness has markedly lower severity (0.510 vs 0.748–0.795)"
[^c9]: arxiv-2604-09602 — "Pearson r = 0.78"
[^c10]: arxiv-2604-09602 — "the mean severity relationship is a stimulus-level confound, not"
[^c11]: arxiv-2604-09602 — "should be read as exploratory evidence."
[^c12]: arxiv-2604-09602 — "Jaccard similarity on word-level tokens is a crude measure of semantic differentiation."
[^c13]: arxiv-2604-09602 — "The declared losses are the model’s self-report of its limitations, not a direct observation of internal state."
[^c14]: arxiv-2604-09602 — "this gap"
