---
description: "Iterative refinement can stop once its state changes by less than a threshold for Ω consecutive steps, measured only on items already committed, with no gold answer or verifier needed."
aliases: ["run-length stability rule", "consecutive-step stability criterion", "state-stability early termination", "KL-stability stop"]
sources: ["arxiv-2512-00670"]
---
# Consecutive-stability stop

An iterative refinement can be stopped by its own state, not by a fixed count or an outside judge. At each step, take the distribution over the items already committed, compare it with the previous step's, and record the divergence. Keep a run counter: it rises by one while the divergence stays under a threshold δ and resets to zero otherwise. Stop when the counter reaches Ω. The rule asks for a run, not one quiet step. The paper says it wants "consecutive steps of stability rather than" sporadic stable steps.[^c1] Stopping then records that the state has stopped moving. It does not record that the state is right.

In the paper the refinement is masked diffusion for a language model. Denoising fills in tokens over a fixed number of steps, so only some positions are visible at any step. The divergence is taken on that visible set: convergence is declared when the KL divergence between consecutive steps "falls below a threshold on the matched unmasked (visible) tokens."[^c2] The denoising of a block stops when the run counter reaches Ω, which the paper glosses as meaning that the reasoning alignment "has remained stable for Ω consecutive steps."[^c3] The series being thresholded is built from alignment between token activations and a reasoning map: "EDIT monitors the alignment between token activations and a reasoning map" taken from the LoRA updates of supervised fine-tuning.[^c4]

The measured effect is a trade between steps and accuracy. Against fixed 64, 128 and 256-step baselines, the paper reports that "EDIT reduces diffusion steps by 11.8% to 68.3%" across sequence lengths 128, 256 and 512.[^c5][^c6] Accuracy rises on the crisp tasks: EDIT "improves accuracy on Countdown (up to 31.6%) and Sudoku (up to 16.1%)."[^c7] The paper's account of the gain is that stopping avoids damage from later steps: "further denoising can overwrite correct intermediate states."[^c8] The same mechanism costs accuracy elsewhere. On GSM8K at length 512 accuracy "drops from 81.2% to 76.2% because long reasoning chains often stabilize before" the reasoning is finished.[^c9]

The part that transfers to answering is the shape of the rule. Stop when successive revisions no longer change what is already settled, and require the lack of change to hold for a run long enough to rule out one quiet step. It needs no forced answer at each cut, unlike the [[answer-agreement-safe-stop]] label, and no held-out gold answer. The paper's evidence concerns denoising step counts and token accuracy, so whether a human or language-model answerer gains from the same rule is not shown here. That is my inference from the shape of the rule.

## Limits

- The thresholds are not derived. δ and Ω are "task-specific thresholds," chosen on held-out validation data.[^c10] The paper itself names the gap: the dependence on these thresholds is "motivating adaptive or learned criteria."[^c11] A task that moves its thresholds moves the result.
- The guarantee is a heuristic with a fraction of misses. The paper writes "Beyond this heuristic, our analysis shows that small matched-support KL divergence" over Ω steps bounds the total variation distance.[^c12] Its calibration reports that "72.3% of early terminations satisfy Corollary 6."[^c13] So about a quarter of the early stops fall outside the bound the paper derives (my reading of the figure). The bound is conditional on the calibration, not a guarantee on every stop.
- Stability is not correctness. The GSM8K drop above is the case where the state settles before the answer does. A consecutive-stability stop can halt a chain that is still moving toward its answer.
- The visible-set restriction belongs to masked diffusion. Tokens that are already unmasked do not change later in the paper's setting, which is why the divergence is taken on them. Whether the same restriction makes sense for a model that revises committed content is not tested in this text (my reading).
- The rule as tested depends on training-time metadata. The paper says that "it requires training dynamics, often unavailable in" released models.[^c14] The parts I read do not separate the run-length rule from the map that supplies its alignment scores, so the rule's value without the map is not shown (my reading).
- The evaluation is narrow. "We use LLaDA-8B" as the one base model, fine-tuned with LoRA only, on five reasoning tasks.[^c15][^c16] The paper says "We evaluate only LoRA," and full-parameter models are left open.[^c16]

## Related

- [[answer-agreement-safe-stop]] — stops by agreement between a forced answer and the trace's own final answer; this rule needs no forced answer, only the movement of the state.
- [[stop-continue-criteria-in-retrieval-loops]] — the survey of loop stops in budget, confidence, verifier and value families; a consecutive-stability test fits none of them cleanly (my reading).
- [[in-trajectory-answer-probing]] — a probed answer trace that shows where answers plateau; the stability rule reads the state directly and needs no probe.
- [[intrinsic-self-correction-convergence]] — a fixed round count with convergence read after the fact; no stability stop is tested there.
- [[stopping-rules]] — error-controlled sequential tests with guarantees; this rule carries only the heuristic bound above.
- [[run-length]] — a different run length: a detector's average run before a false alarm, not a count of consecutive stable steps.

[^c1]: arxiv-2512-00670 — "we require consecutive steps of stability rather than"
[^c2]: arxiv-2512-00670 — "falls below a threshold on the matched unmasked (visible) tokens"
[^c3]: arxiv-2512-00670 — "has remained stable for Ω consecutive steps"
[^c4]: arxiv-2512-00670 — "EDIT monitors the alignment between token activations and a reasoning map"
[^c5]: arxiv-2512-00670 — "EDIT reduces diffusion steps by 11.8% to 68.3%"
[^c6]: arxiv-2512-00670 — "compared to fixed 64/128/256-step baselines"
[^c7]: arxiv-2512-00670 — "improves accuracy on Countdown (up to 31.6%) and Sudoku (up to 16.1%)"
[^c8]: arxiv-2512-00670 — "further denoising can overwrite correct intermediate states"
[^c9]: arxiv-2512-00670 — "drops from 81.2% to 76.2% because long reasoning chains often stabilize before"
[^c10]: arxiv-2512-00670 — "EDIT uses task-specific thresholds"
[^c11]: arxiv-2512-00670 — "motivating adaptive or learned criteria"
[^c12]: arxiv-2512-00670 — "Beyond this heuristic, our analysis shows that small matched-support KL divergence"
[^c13]: arxiv-2512-00670 — "72.3% of early terminations satisfy Corollary 6"
[^c14]: arxiv-2512-00670 — "it requires training dynamics, often unavailable in"
[^c15]: arxiv-2512-00670 — "We use LLaDA-8B"
[^c16]: arxiv-2512-00670 — "We evaluate only LoRA"
