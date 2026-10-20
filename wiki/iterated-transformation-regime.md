---
description: "Feeding an LLM's output back as its next input yields a loop whose regime the prompt sets: in one tested pair, paraphrasing settled into a region and negation did not."
aliases: ["agentic loop regime", "contractive versus exploratory loop", "prompt-set dynamical regime", "iterated LLM dynamics"]
sources: ["arxiv-2512-10350"]
---
# Iterated transformation regime

An iterated LLM system can be written as a recursion. Each step applies one prompt-wrapped model call to the previous output, so the loop is one in which "where each output becomes the next input".[^c1] The paper treats that recursion as a discrete dynamical system and observes the run as a sequence of embeddings, one per output. It then sorts the whole run into one of three regimes. In the contractive regime, "The loop stabilizes around a coherent semantic region."[^c2] In the oscillatory regime, "The trajectory alternates among a finite set of recurrent clusters" without settling on one.[^c3] In the exploratory regime, "The loop continuously generates novel semantic content without stabilization."[^c4]

The mechanism the paper proposes is that the regime follows from the operator, meaning the prompt together with the model, and not from the model by itself. In its experiment one model, deepseek-r1:8b, was run at a sampling temperature of 0.8 for 50 steps under each of two prompts.[^c5][^c6] A rewriting prompt, asking for a sentence that reads more fluently while keeping its meaning, gave consecutive similarities "in the range 0.82–0.95", and the similarity to the starting sentence settled, with clusters whose dispersion fell.[^c7] A prompt that summarizes the text and then negates it gave consecutive similarities that "fluctuates widely between 0.2 and 0.6", and no cluster under any tested setting.[^c8] The paper's summary is that "transformation operator, not the model, controls the regime."[^c9] For the exploratory run it reports that "each output resets the contextual reference frame", so each pass starts a new region instead of refining the last.[^c10]

What survives the transfer from dynamical systems is the vocabulary: trajectory, attractor, regime. What does not survive is the theory behind it. The paper says its notions "are not inherited from classical dynamical systems theory, but redefined operationally".[^c11] The reason given is that the classical stability theorems need conditions that cannot be checked for these maps: they "cannot be verified for prompt-driven text transformations".[^c12] So "contractive" names an observed pattern over a finite run. It does not name a contraction mapping with a guarantee.

The step from this to asking is mine, not the paper's. A question reformulated by repeated rewriting is itself such a loop. If the rewriting operator is contractive, the reformulations settle into one phrasing. If it is exploratory, each pass may move the question to a region that the previous pass does not predict, so further passes do not return it to the earlier wording. Whether the settled phrasing is a better question is a separate matter that the paper does not touch. The same kind of iterated self-revision is measured elsewhere as a quality curve with an interior peak, in [[refinement-quality-peak]]. That is a different measure, expert-judged quality against round number, and it does not say where the embeddings went. On the asker's side, a reissued prompt with no new content is, in this frame, a step whose operator gives no pull toward a settled phrasing. That reading is mine, and no source here tests it.

## Limits

- One model, one embedding function, one similarity measure. "All experiments use a single LLM (deepseek-r1:8b)", and "different architectures or sampling strategies may yield different dynamical signatures."[^c13][^c14] The claim that the operator, not the model, sets the regime is therefore not separated from the model: no second model was run.
- The horizon is finite. "All notions of convergence, divergence, and stability are defined operationally" over the run, and the paper "does not claim formal convergence in the limit".[^c15][^c16]
- One of the three regimes has no example in the evidence. "The prompts we designed exhibit either full convergence (Contractive) or complete divergence (Exploratory)", and the oscillatory class was not observed.[^c17]
- The prompts are archetypes. "they do not constitute an exhaustive map of the space of possible dynamical" behaviours.[^c18] The "negation" prompt is in fact a two-step instruction, which the paper describes as "the exploratory loop was designed to alternate between" summarization and negation.[^c19]
- "Observed regimes characterize the statistical behavior induced by a given prompt-model configuration".[^c20] The results describe a sampled run, not a property fixed for all runs.
- No question is asked in the experiment. The loops rewrite one sentence. Any transfer to question formulation is my inference, as stated above.

## Related

- [[attractor-cluster-trajectory]] — how the paper finds the settled region that marks a contractive run, and how it fails to find one in the exploratory run
- [[refinement-quality-peak]] — iterated self-revision scored by expert judgment, which peaks and then falls; a different measure of the same kind of loop
- [[rolling-the-dice-reprompting]] — a reissued prompt with unchanged intent, the asker-side case that the frame above reads as having no pull toward a fixed point (my reading)

[^c1]: arxiv-2512-10350 — "where each output becomes the next input"
[^c2]: arxiv-2512-10350 — "The loop stabilizes around a coherent semantic region."
[^c3]: arxiv-2512-10350 — "The trajectory alternates among a finite set of recurrent clusters"
[^c4]: arxiv-2512-10350 — "The loop continuously generates novel semantic content without stabilization."
[^c5]: arxiv-2512-10350 — "We use a sampling temperature of 0.8"
[^c6]: arxiv-2512-10350 — "The process is repeated for T = 50 iterations"
[^c7]: arxiv-2512-10350 — "in the range 0.82–0.95"
[^c8]: arxiv-2512-10350 — "fluctuates widely between 0.2 and 0.6"
[^c9]: arxiv-2512-10350 — "transformation operator, not the model, controls the regime."
[^c10]: arxiv-2512-10350 — "each output resets the contextual reference frame"
[^c11]: arxiv-2512-10350 — "are not inherited from classical dynamical systems theory, but redefined operationally"
[^c12]: arxiv-2512-10350 — "verified for prompt-driven text transformations"
[^c13]: arxiv-2512-10350 — "All experiments use a single LLM (deepseek-r1:8b)"
[^c14]: arxiv-2512-10350 — "may yield different dynamical signatures"
[^c15]: arxiv-2512-10350 — "All notions of convergence, divergence, and stability are defined operationally"
[^c16]: arxiv-2512-10350 — "The framework does not claim"
[^c17]: arxiv-2512-10350 — "The prompts we designed exhibit either full convergence (Contractive) or complete divergence (Exploratory)"
[^c18]: arxiv-2512-10350 — "they do not constitute an exhaustive map of the space of possible dynamical"
[^c19]: arxiv-2512-10350 — "the exploratory loop was designed to alternate between"
[^c20]: arxiv-2512-10350 — "the statistical behavior induced by a given prompt-model configuration"
