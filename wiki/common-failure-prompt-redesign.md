---
description: "In the authors' runs, revising a prompt from elements that fail across many scaled samples, then regenerating from the best seeds, kept improving where re-sampling a fixed prompt plateaued."
aliases: ["PRIS", "prompt redesign for inference-time scaling", "cross-sample prompt revision", "common-failure-aware prompt redesign"]
sources: ["arxiv-2512-03534"]
---
# Common-failure prompt redesign

When one prompt is sampled many times, its failures are often not scattered. The same element of the prompt tends to be missed across many outputs. Common-failure prompt redesign treats that recurrence as the evidence. It reads the set of scaled outputs, finds the prompt elements that keep failing, and rewrites the prompt to stress them, so the next round of sampling is aimed at what the generator actually drops. The paper calls the scheme Prompt Redesign for Inference-time Scaling (PRIS). Its stated core idea is to "identify recurring failure patterns across visuals, and redesign" the prompt before regenerating.[^c1]

The procedure, as the paper gives it, has four steps.[^c2] First, generate M candidates and check each prompt element against each candidate. Second, keep the top-k candidates, ranked by how many elements they satisfy, with ties broken by a reward model. Third, within those top-k, call an element a common failure when "elements whose success probability is below 50% within the top-k samples". Fourth, rewrite the prompt to reinforce those elements while keeping the ones already satisfied, and regenerate the remaining samples from the noise seeds of the top-k. If no element is a common failure, the paper rewrites the prompt anyway "to encourage exploration of prompt variations" [^c3]. The seeds are the part that makes the loop a scaling loop: a good draw is kept, and only the text changes.

The motivation is a plateau. The authors report that best-of-N with a fixed prompt "plateaus on held-out evaluation beyond 1e3 NFEs", while the redesigned prompts kept improving.[^c4] They locate the cause in the fixed prompt: "all prior methods share a key limitation: they expand only the visual search space while keeping the prompt fixed." [^c5] The paper also treats partial successes as feedback rather than waste: the method works by "generations as informative feedback rather than discarding" them, so the compute already spent is reused.[^c6]

The concept differs from per-sample rewriting in its unit of evidence. The paper says existing prompt-refinement work "react to individual noisy failures rather than addressing the recurring failure patterns that are revealed through" scaling.[^c7] In text-to-video, the authors report that per-sample revision "performs worse" than no revision at all, and attribute this to spreading the update over low-probability or seed-specific artifacts.[^c8] That attribution is theirs. The sections read do not test it against alternatives.

My inference, not the paper's: transferred to the asker's side, a question is a fixed object, the answers it draws vary, and the failure pattern across those answers may say which slot of the question the asker has left unspecified. The paper does not study questions in this sense; its objects are image and video prompts. What plausibly survives the transfer is the cross-sample aggregation and the reuse of good draws. What does not is any claim that a person's question behaves like a generator's prompt.

## Limits

- The reported gains are the authors' own: "a 15% improvement on VBench2.0 for text-to-video generation" and about 7% on GenAI-Bench for text-to-image.[^c9] The held-out measures are reward models, and the text read does not show human judgments of whether the revised prompt still says what the user meant. The paper reports aesthetic quality as "comparable", not as an improvement.[^c10]
- The revision is applied once in the main experiments. "In our main experiments, we apply it once, as" the authors judge a single revision already gives substantial gains.[^c11] Repeated revision adds gains, but the sections read do not show where they stop.
- Failures are found by the verifier, so the loop is only as good as that verifier. The verifier here is the paper's own element-level check, evaluated on a benchmark the authors built.[^c12]
- Whether the revised prompt drifts from the user's wording is not measured in the sections read. The paper says it preserves intent, and its example in Figure 2 shows a long rewrite. That gap is my inference, not a finding of the paper.
- The claim that prompts refined on one model "often generalize well to others" is reported in an appendix, not in the main results.[^c13]

## Related

- [[test-time-scaling]] — the compute family this sits in; the prompt is added as a scaled axis beside the noise seeds.
- [[element-level-entailment-verification]] — the per-element verifier whose failure counts drive the redesign.
- [[output-grounded-instruction-refinement]] — rewrites an instruction from the output it just produced; the contrast here is aggregation across many outputs rather than one.
- [[refinement-signal-reversal]] — a revision can lower the visible aim as well as raise it, which bounds what a rewrite can be trusted to do.

[^c1]: arxiv-2512-03534 — "identify recurring failure patterns across visuals, and redesign"
[^c2]: arxiv-2512-03534 — "Step 2. Select the top-k best-performing samples. PRIS"
[^c3]: arxiv-2512-03534 — "to encourage exploration of prompt variations"
[^c4]: arxiv-2512-03534 — "plateaus on held-out evaluation beyond 1e3 NFEs"
[^c5]: arxiv-2512-03534 — "all prior methods share a key limitation: they expand only the visual search"
[^c6]: arxiv-2512-03534 — "generations as informative feedback rather than discarding"
[^c7]: arxiv-2512-03534 — "rewrites react to individual noisy failures rather than addressing the recurring failure patterns that are revealed through"
[^c8]: arxiv-2512-03534 — "Notably, in T2V generation, where fully aligning the generated visuals with the prompt is considerably more challenging than in T2I, per-sample revision performs worse"
[^c9]: arxiv-2512-03534 — "a 15% improvement on VBench2.0 for text-to-video generation"
[^c10]: arxiv-2512-03534 — "maintaining comparable aesthetic quality"
[^c11]: arxiv-2512-03534 — "In our main experiments, we apply it once, as"
[^c12]: arxiv-2512-03534 — "we construct a new benchmark explicitly tailored for inference-time scaling"
[^c13]: arxiv-2512-03534 — "often generalize well to others (see Appendix A.6)"
