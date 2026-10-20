---
description: "Reasoning written as short typed symbolic steps (OPERATION: expression;) instead of free text; SFT on such traces shortens them but costs accuracy that RL then recovers in part."
aliases: ["Mentalese", "Mentalese chain-of-thought", "symbolic chain of thought", "compressed symbolic reasoning trace"]
sources: ["arxiv-2511-22891"]
---
# Mentalese symbolic reasoning trace

A Mentalese trace is a sequence of canonical steps, each an operator with an expression. The operator set is given as "e.g., SET, EQ, CASE, SOLVE, CALC, DIFF," with a final ANS step, and a valid trace "culminates in exactly one terminal ANS:e; step".[^c1][^c2] The prompt rules add that there is no natural language between steps and that "Every step must be necessary" for solving the problem.[^c3] The format is therefore a restricted notation, checked by its rules, rather than a looser style of prose.

The format is set against free-form chain of thought. "Unlike traditional CoT, which uses free-form text, Mentalese encodes reasoning in canonical steps" joined by semicolons.[^c4] The authors claim three gains from this. The first is compression, "eliminating redundant tokens for up to" roughly tenfold shorter reasoning.[^c5] The second is faithfulness, which they state as "each step is necessary and sufficient".[^c6] The third is cognitive alignment, the resemblance to structured mental representation.

The traces were not written by hand. The authors "used GPT-4.1" with a structured prompt (a definition, syntax rules and examples) to rewrite the question-and-answer pairs of an existing math set, and then removed "65 malformed cases" before supervised fine-tuning.[^c7][^c8]

The format borrows its motivation from the Language of Thought hypothesis. The paper describes human cognition as operating in an internal system "characterized by" "compact, symbolic structures".[^c9] From that it hypothesises that verbose natural-language explanations "are not essential for reasoning".[^c10] Transferring the idea from cognitive science to a language model keeps one thing: the claim that a small set of symbolic primitives can carry the logical steps a problem needs, and that the trace can be much shorter than prose. It does not keep the cognitive claim itself. The hypothesis concerns human minds, and the paper measures token counts and benchmark accuracy for a trained model. Nothing in the parts I read tests whether the model's internal computation resembles a mental language, so "cognitive alignment" is an analogy here and not a result (my reading).

What the format costs and what recovers it. Training a model to produce these traces by supervised fine-tuning alone has a price: "aligning models to Mentalese by supervised fine-tuning alone leads to a substantial drop in performance relative to the base model."[^c11] Reinforcement learning on top is what restores accuracy (see relative-length-preference-reward). The authors also report that training through the format "stabilizes optimization and reduces training time by 7-9× compared to" direct verifier-based RL on the base model.[^c12] The headline result for the resulting ORION models is that they keep "maintaining 90-98% of the baseline accuracy" while producing shorter traces on math benchmarks.[^c13]

## Limits

- The compression and faithfulness claims are not separately tested in the text I read. The "necessary and sufficient" property is a rule given to the generator. I did not find a check that the 40k traces satisfy it, or an ablation that removes steps and measures the effect (my reading).
- The traces come from one generator (GPT-4.1) on one math source. Whether the notation transfers to other domains is not shown. The out-of-domain tests (GPQA, LSAT, MMLU) evaluate the trained model, not symbolic traces on non-math tasks.
- The main models are about 1.5B parameters. Larger models may not need the format, and the paper does not test that.
- The accuracy retention is against the authors' chosen baseline on their benchmarks. The headline is an aggregate. The per-step error analysis that would show where the symbolic trace loses information is not in the parts I read.
- The cognitive motivation is an analogy. No human reasoning data are compared with the traces.

## Related

- relative-length-preference-reward — the within-group length reward the paper pairs with this format to recover the accuracy lost in symbolic fine-tuning
- [[concise-reasoning-mode]] — the short-rationale option in natural language, which shortens output without a symbolic notation

[^c1]: arxiv-2511-22891 — "e.g., SET, EQ, CASE, SOLVE, CALC, DIFF,"
[^c2]: arxiv-2511-22891 — "culminates in exactly one terminal ANS:e; step"
[^c3]: arxiv-2511-22891 — "Every step must be necessary"
[^c4]: arxiv-2511-22891 — "Unlike traditional CoT, which uses free-form text, Mentalese encodes reasoning in canonical steps"
[^c5]: arxiv-2511-22891 — "eliminating redundant tokens for up to"
[^c6]: arxiv-2511-22891 — "each step is necessary and sufficient"
[^c7]: arxiv-2511-22891 — "We used GPT-4.1"
[^c8]: arxiv-2511-22891 — "removing 65 malformed cases"
[^c9]: arxiv-2511-22891 — "compact, symbolic structures"
[^c10]: arxiv-2511-22891 — "are not essential for reasoning"
[^c11]: arxiv-2511-22891 — "aligning models to Mentalese by supervised fine-tuning alone leads to a substantial drop in performance relative to the base model"
[^c12]: arxiv-2511-22891 — "stabilizes optimization and reduces training time by 7-9× compared to"
[^c13]: arxiv-2511-22891 — "maintaining 90-98% of the baseline accuracy"
