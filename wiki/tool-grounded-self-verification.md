---
description: "A model's verifier re-runs tools on its own reasoning step and turns the checked verdict into a reward, so self-critique rests on executable evidence rather than text alone."
aliases: ["tool-grounded verification", "tool-grounded generative verification", "tool-checked self-evaluation", "tool-augmented self-verifier"]
sources: ["arxiv-2511-19900", "arxiv-2511-18760"]
---
# Tool-grounded self-verification

Text-only self-evaluation is the setting the paper starts from. A model that critiques its own reasoning in prose is weak where the reasoning is computational or perceptual: the authors say that purely text-based self-evaluation "struggles to verify complex visual reasoning steps and often suffers from evaluation hallucinations."[^a1] Tool-grounded self-verification keeps the same model in the judging seat but lets the judgement call a tool before it is given.

The mechanism, concretely. The paper splits one vision-language model into two modes over shared weights. A Solver "performs multi-turn reasoning and selectively invokes external tools," and a Verifier re-reads each step as a triple of state, action and tool observation.[^a9] For each step the Verifier emits a score of factual correctness, an epistemic confidence and a natural-language critique.[^a4] The distinguishing part is that the Verifier can act on its own critique: it "can also re-invoke tools to crosscheck correctness," so a claim about a length or an angle can be tested by the same kind of computation the Solver used (my illustration, not the paper's example).[^a2] The authors describe the effect as turning "verification from a static correctness check into a" procedure in which language-level reflection is paired with "executable tool-derived evidence."[^a3]

The verdict is not only a report. It enters a per-step process reward that adds a tool-correctness term to the product of score and confidence, and subtracts a divergence penalty that keeps the Verifier's distribution close to a reference (the paper's Eq. 2). The step rewards are summed into a trajectory return, and the policy is updated with a group-relative policy gradient. So the verdict is used as a training signal, which is what separates this from a filter applied at inference time.

What was measured. Removing tools from both reasoning and self-evaluation drops average performance: "performance declines by 6.5%" across the benchmarks.[^a5] Removing the outer reinforcement loop, and keeping only supervised training, is larger: "with an average decrease of 8.7% across all benchmarks."[^a6] When the Verifier is used as a process reward model to score another model's trajectories, it "significantly improves Best-of-8 (BoN) performance when used as a reward scorer," and across open models the authors report "an average gain of 7.3%."[^a7][^a8]

For the asker's side of the wiki, the transferable point is narrow. A verdict on an answer is only as grounded as the check behind it. Where a check can be run by the judge itself, the judgement has something to be right about. My inference, not the paper's claim: the same shape would apply to answer evaluation in any domain where a calculator, a parser or a lookup can test a stated fact, and the paper gives no evidence outside its geometry and visual-science benchmarks.

A nearby case keeps the check inside generation and does not turn it into a reward. HERMES has the model pass each critical step to a Lean prover during inference, and "Our agent returns one of three states: (1) proof succeeded, (2) counter-proof found, or (3) verification failed."[^a10] The first two states steer the next step, since the LLM "either revises its reasoning when hallucination is detected" or moves on.[^a11] My inference, not the paper's: a kernel verdict is a different kind of evidence from a model's critique of its own step, but it is evidence about a translation of the step, not the step itself, so the grounding question moves to whether the translation is faithful; see [[back-formalization-round-trip-check]].

## Limits

- Tool use is optional. The Verifier "can" re-invoke tools; the read text does not report how often it does, or how often a tool-checked verdict differs from a text-only one. The benefit is therefore not located in the verification step alone.
- The ablation is confounded. Removing tools removes them from reasoning and from verification together, so the 6.5% is the value of tool use overall, not of tool-grounded critique in isolation.
- The judge shares its weights with the solver. The paper's answer to shared-judgement bias is a divergence term that aligns the two roles, not an independent judge. Whether the Verifier's verdicts are right when the Solver and Verifier agree is not tested in the slices read; see [[self-reward-interface-decoupling]] for the shortcut this design does not remove.
- The reported verifier quality is usefulness as a reward (Best-of-N selection and step-level correlation), not its error rate on labelled steps.
- The domains are geometric problem solving and visual scientific analysis. The 12.5% headline is over the base model on those benchmarks; open-ended answers are not tested.
- The thresholds and weights (the confidence cut-off, the tool weight, the divergence weight, the repair cost) are not varied in the slices read, so the sensitivity of the verdict to them is unknown.

## Related

- [[tool-integrated-reasoning]] — the same tool loop, but there the tool sits in the solver's generation; here it sits in the critique of a finished step.
- [[evidence-grounded-step-reward]] — a generative step verifier grounded in retrieved evidence, but an external verifier scoring other models' steps, with no tool calls of its own.
- [[inline-step-critique]] — a per-step verdict written in one generation with no tools; the text-only counterpart of this mechanism.
- [[self-reward-interface-decoupling]] — the shared-weights checker problem that a dual-role design runs into.
- [[confidence-triggered-reflection]] — a low confidence triggers a repair of the step; the verdict's confidence plays that gating role here.
- [[meta-verification]] — a second check on a verifier's analysis; another remedy for a verifier whose reasons go unchecked.
- [[back-formalization-round-trip-check]] — a compiler-and-LLM check on the translation of a step into a formal statement, the part a formal verdict depends on.

[^a1]: arxiv-2511-19900 — "struggles to verify complex visual reasoning steps and often suffers from evaluation hallucinations"
[^a2]: arxiv-2511-19900 — "The Verifier can also re-invoke tools to crosscheck correctness"
[^a3]: arxiv-2511-19900 — "transforms verification from a static correctness check into a"
[^a4]: arxiv-2511-19900 — "measures factual correctness"
[^a5]: arxiv-2511-19900 — "performance declines by 6.5%"
[^a6]: arxiv-2511-19900 — "with an average decrease of 8.7% across all benchmarks"
[^a7]: arxiv-2511-19900 — "Best-of-8 (BoN) performance when used as a reward scorer"
[^a8]: arxiv-2511-19900 — "an average gain of 7.3%"
[^a9]: arxiv-2511-19900 — "alternates between two internal modes"
[^a10]: arxiv-2511-18760 — "Our agent returns one of three states: (1) proof succeeded"
[^a11]: arxiv-2511-18760 — "the LLM either revises its reasoning when hallucination is detected"
