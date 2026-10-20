---
description: "Inside one solution, each sub-problem is scored for difficulty and sent to fast or deliberate processing by a threshold, so the token budget concentrates on the steps that decide the answer."
aliases: ["SCALE", "selective resource allocation", "sub-problem difficulty allocation", "within-problem compute allocation", "difficulty-threshold System 1 and System 2 switching"]
sources: ["arxiv-2512-00466"]
---
# Sub-problem difficulty allocation

A per-query router decides how much reasoning a whole question receives. This mechanism decides it inside a single solution, step by step. The solver first splits the problem into an ordered list of sub-problems. Then each one is scored: "For each sub-problem si in the selected decomposition, SCALE prompts the model to assess" its complexity, given the original problem and the sub-problems already solved.[^c1] The score is compared with a threshold τ. Below it the step goes to a fast mode, called System 1; above it, to a deliberate chain-of-thought mode, called System 2. The steps are then solved in order, each carrying the earlier sub-problems and their solutions forward.[^c2]

The motivation is that a uniform budget is wasted on easy steps. The authors write that "current methods allocate comparable" budgets to an elementary operation and to a step that needs a long derivation, so extra compute on the hard step yields "diminishing returns".[^c3] The mechanism is meant to remove that dilution by spending the tokens where the score is high.

The mode switch is not a separate model. The paper says "SCALE utilizes this modeswitching capability" of models that already support two thinking modes, such as Qwen3, and for reasoning-only models it pairs them with a fast-mode counterpart.[^c4] The decomposition is also chosen, not fixed: "SCALE generates multiple alternative decompositions and selects the optimal one".[^c5]

What was measured. On AIME25 with Qwen3-32B the headline is "percentage points (57.50% to 71.25% on AIME25) while reducing computational costs by 33-53%" against uniform baselines.[^c6] The threshold sweep is the clearest mechanism check. Lower thresholds give higher accuracy: "lower thresholds consistently achieve higher accuracy across both datasets".[^c7] Tokens move the other way, and "the percentage of hard sub-problems decreases" from above 75% at low thresholds to 0% at τ = 0.9.[^c8] At τ = 0.2, about 75% of sub-problems go to System 2, so the lowest threshold is close to uniform deliberate reasoning. The scaling figure supports the allocation reading. The AIME curves rise almost linearly with the token budget, while "AMC23 shows a more gradual improvement curve that begins to plateau", and the authors attribute this to AMC having fewer hard sub-problems to absorb extra budget.[^c9]

## Limits

The evidence is mathematical. The introduction describes "challenging mathematical" benchmarks, and every reported result is on competition-style problems.[^c10] Whether the same decomposition and threshold scheme works for open-ended or non-mathematical questions is not tested in the sections I read.

The difficulty score comes from the same model that does the solving. The paper defines it as a judgement over "computational complexity, mathematical sophistication required, reasoning depth needed, and solution uncertainty".[^c11] The text never compares it with an independent measure of step difficulty. So "hard" means "the model rated it hard", and whether the rating tracks where the answer is actually lost is not shown.

The AMC-versus-AIME explanation is the authors' reading. They write that the divergence "directly reflects the underlying distribution of sub-problem difficulties", but the text does not report the share of hard steps per benchmark as a measured quantity. The explanation is plausible, not established.

The threshold was swept on the same AIME sets that are reported, and the table caption reads "Analysis on difficulty threshold values" across those datasets.[^c12] I did not find a held-out split in the sections read, so the best τ = 0.2 is a choice read off the evaluation data. The headline 71.25% is not tied to a stated τ in the slices I read.

The baselines in the sections I read are uniform chain-of-thought and InftyThink, not a per-query router. The paper therefore does not show that per-step allocation beats per-query tiering at matched cost. That comparison is open.

## Related

- [[test-time-scaling]] — the general lever of spending more inference compute; this note says how a fixed budget is split inside one solution.
- [[complexity-tiered-strategy-routing]] — the same allocation idea at the grain of the whole question, with one tier per query instead of one mode per step.
- [[preemptive-complexity-estimation]] — another way of setting a per-problem compute level; the question of when the difficulty is read is the one to compare.
- [[moderate-adaptive-reasoning-length]] — the overthinking concern that motivates shorter budgets on easy material, seen from the length side.
- [[croskerry-error-taxonomy-in-llm-agents]] — the same System 1 and System 2 split used as an error taxonomy rather than as a compute switch.

[^c1]: arxiv-2512-00466 — "For each sub-problem si in the selected decomposition, SCALE prompts the model to assess"
[^c2]: arxiv-2512-00466 — "SCALE processes sub-problems sequentially while"
[^c3]: arxiv-2512-00466 — "current methods allocate comparable"
[^c4]: arxiv-2512-00466 — "SCALE utilizes this modeswitching capability"
[^c5]: arxiv-2512-00466 — "SCALE generates multiple alternative decompositions and selects the optimal one"
[^c6]: arxiv-2512-00466 — "percentage points (57.50% to 71.25% on AIME25) while reducing computational costs by 33-53%"
[^c7]: arxiv-2512-00466 — "lower thresholds consistently achieve higher accuracy across both datasets"
[^c8]: arxiv-2512-00466 — "the percentage of hard sub-problems decreases"
[^c9]: arxiv-2512-00466 — "AMC23 shows a more gradual improvement curve that begins to plateau"
[^c10]: arxiv-2512-00466 — "Extensive experiments across challenging mathematical"
[^c11]: arxiv-2512-00466 — "The assessment considers computational complexity, mathematical sophistication required, reasoning depth needed, and solution uncertainty."
[^c12]: arxiv-2512-00466 — "Analysis on difficulty threshold values for"
