---
description: "A masked-diffusion LM settles a fact-check verdict in the first steps; forcing justification first cuts accuracy (86.2 to 71.9%) as its own noisy justification overrides the early verdict."
aliases: ["refinement drift", "delayed verdict unmasking", "early verdict anchoring"]
sources: ["arxiv-2603-01190"]
---
# Refinement drift under forced deliberation

In a masked diffusion language model (MDLM), every output position is refined together, so a verdict and its justification are not produced in reading order. In LLaDA-8B on binary fact verification (AVeriTeC dev set, N = 500), the verdict was fixed within the first few diffusion steps, "well before the justification is complete", whichever order the prompt asked for.[^c1] Output order barely mattered: verdict-first and justification-first accuracies were 86.2 vs 88.0 (Qwen3-8B) and 89.5 vs 89.0 (LLaDA), per Table 1 as extracted. The autoregressive reasoning-before-answer advantage therefore did not transfer.[^c2]

## Forced deliberation hurts

The authors blocked the verdict token from being unmasked until a set share of the 64 output tokens of justification existed. Accuracy went from 86.2% at 0% deliberation to 71.9% at 90%, with little change up to 25%. That plateau coincides with the JSON scaffold being generated in the first 10 to 16 tokens.[^c3] Verdict trajectories showed the model often reaching the right verdict early and then reversing it as justification tokens accumulated. The author calls this refinement drift: local inconsistencies in the justification override the correct global assessment.[^c4]

## Why: verdicts depend on justification quality

Two interventions use the MDLM's ability to condition on arbitrary token subsets.

- Integrity test. A wrong verdict is hard-coded and the model infills the justification. In 44% of cases the justification still contradicts the forced verdict. In the rest the model rationalizes it, by logical errors (37%), hallucinated facts (13%) or other failures (6%).[^c5]
- Reliance test. The corrupted justifications, with label words masked, are fixed as context and only the verdict is infilled. Accuracy falls to 57.3%, with supported claims at 17.2%. With the dataset's ground-truth justifications it reaches 97.1%.[^c6]

The author reads these together as the mechanism of drift. The model commits early, then conditions on the justification it writes, so errors in that text pull the verdict the wrong way.[^c7] Early commitment and causal dependence on the justification are therefore compatible. The justification can act as evidence the verdict is later conditioned on, and not only as a rationale added after the fact.

## Limits

- One model (LLaDA-8B), one task (binary verdicts, gold evidence given in the prompt), one length (64 tokens). The author says drift may depend on scale or pretraining, and may not appear in tasks where intermediate steps are strict prerequisites, such as competition math.[^c8]
- The author attributes early commitment to the low complexity of binary verification. That was not tested against harder tasks.
- The integrity categories were judged by an LLM (Qwen3-30B-A3B); no human agreement is reported in the slices I read.
- Table 1's cell alignment in the text extract is partly garbled, so the baseline figures above are my reading of it. The LLaMA values (69.7, 72.5) are the lowest in the table.
- The 64-token cap was chosen to avoid verdict leakage into the justification, so longer, richer reasoning was not examined.

## Related

- [[deferred-answer-exposure]] — a nearby question of when an answer is revealed relative to the reasoning.
- [[hint-adherence-without-acknowledgement]] — another case where stated reasoning and the actual driver of the answer come apart.
- [[reasoning-masked-sycophancy]] — reasoning text that hides what actually determined the answer.

[^c1]: arxiv-2603-01190 — "the model resolves the verdict within the first few diffusion steps, well before the justification is complete"
[^c2]: arxiv-2603-01190 — "All three models exhibit minimal sensitivity to output ordering"
[^c3]: arxiv-2603-01190 — "Interestingly, we notice no significant degredation in performance until after 25% deliberation."
[^c4]: arxiv-2603-01190 — "We refer to this phenomenon as refinement drift."
[^c5]: arxiv-2603-01190 — "in 44% of cases the model maintains logical integrity"
[^c6]: arxiv-2603-01190 — "accuracy drops sharply to 57.3%"
[^c7]: arxiv-2603-01190 — "The model commits to a verdict within the first few diffusion steps, then generates justification tokens that it subsequently conditions on."
[^c8]: arxiv-2603-01190 — "The susceptibility to refinement drift may be a function of model scale, pretraining data, or optimization procedure"
