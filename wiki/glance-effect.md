---
description: "A reasoner that sees a large image once, coarsely, before reasoning writes narration rather than evidence-based inference; re-inspecting the image mid-reasoning is the proposed repair."
aliases: ["pseudo reasoning", "reasoning without evidence", "single-glance perception"]
sources: ["arxiv-2511-22396"]
---
# Glance Effect

A multimodal reasoning model asked about a large image often writes an explicit reasoning chain that does not beat its own non-reasoning answer. The remote-sensing paper that names this calls the observed pattern *pseudo reasoning*: the model "merely describe[s] a reasoning process rather than performing one."[^c1] Its account of the cause is the *Glance Effect*. The model takes one coarse perception of the whole scene and then reasons from that single view: "Current models perform only a single, coarse perception pass (a glance) before reasoning."[^c2] The result is reasoning "built on incomplete visual evidence," which then drifts toward text that is consistent with itself rather than with the image.[^c3]

The paper's Fig. 1 is the headline measurement. Explicit thinking, in the paper's comparison, "degrades performance below the non-reasoning base model."[^c4] This is the sense in which the reasoning chain adds narration but no gain: the same model, asked directly, does better.

The proposed repair changes the order of perception and reasoning. The model is trained to treat reasoning as a loop in which language decides what to look at next and the image answers: "the model continuously revisits the image, seeking new visual cues guided by the evolving reasoning."[^c5] Training is staged. A cold start on synthesized self-questioning traces raises VQA accuracy but lowers grounding; a reinforcement stage on localisation restores grounding; a further stage on VQA carries the pattern to broader questions.[^c6] Attention analysis shows the loop as a rhythm: "attention peaks on visual tokens (evidence-seeking phases) and then drops during language-based reasoning (reasoning phases)."[^c7]

The scope is stated narrowly. The paper ties the effect to remote sensing, citing "the unique properties of remote sensing (RS) imagery."[^c8] Its VQA and grounding comparison holds the base model fixed: "all competing models are built on Qwen2.5-VL-7B."[^c9]

## Limits

- The Glance Effect is an attribution, and the paper marks it as one: "We attribute this to the Glance Effect (Fig. 1b)."[^c10] The text I read does not vary the number of glances at a fixed model and show performance following it. The compared models also differ from the proposed one in training, so the single-glance story is not isolated from other causes. (My inference.)
- "Single coarse pass" describes what the baselines are assumed to do; it is not measured per model in the parts I read. (My inference.)
- The evidence is benchmark-level on remote-sensing VQA and grounding, and the attention rhythm is a descriptive analysis, not a test that the rhythm causes the gain. Nothing in the parts read tests natural images. (My inference.)
- The repair is a trained behavior, not an inference-time procedure. The text does not show that a model without the SFT and RL stages reaches the same loop by prompting alone.

## Related

- [[on-demand-resolution-zoom]] — the same coarse-first, then refine pattern, for video frames under a per-call budget; there the refinement is requested at inference, not trained.
- [[evidence-grounded-socratic-reasoning]] — re-checks each Socratic sub-question against external evidence every round; a gate outside the model, where this note's repair is a loop inside it.
- presumed-weakness-self-play — the training-data step that makes the questioner ask for the finer views the loop needs.

[^c1]: arxiv-2511-22396 — "they merely describe a reasoning process rather than performing one"
[^c2]: arxiv-2511-22396 — "Current models perform only a single, coarse perception pass"
[^c3]: arxiv-2511-22396 — "leading to reasoning built on incomplete visual evidence"
[^c4]: arxiv-2511-22396 — "explicit thinking (blue bars) degrades performance below the non-reasoning base model (red bar)"
[^c5]: arxiv-2511-22396 — "the model continuously revisits the image, seeking new visual cues guided"
[^c6]: arxiv-2511-22396 — "SFT with RS-EoT trajectories substantially improves VQA accuracy but causes a significant"
[^c7]: arxiv-2511-22396 — "visual tokens (evidence-seeking phases) and then drops during language-based reasoning (reasoning phases)."
[^c8]: arxiv-2511-22396 — "owing to the unique properties of remote sensing (RS) imagery"
[^c9]: arxiv-2511-22396 — "all competing models are built on Qwen2.5-VL-7B"
[^c10]: arxiv-2511-22396 — "We attribute this to the Glance Effect (Fig. 1b)."
