---
description: "Scoring each stage of a long agent run with its own rubric, and giving each stage its own score plus the scores of the later stages it enables, gives denser credit than one terminal reward."
aliases: ["SS-GRPO", "stage-structured GRPO", "stagewise rubric credit", "stage return with causal dependence", "stage-level judged reward"]
sources: ["doi-10-48550-arxiv-2605-10899"]
---
# Stagewise judged credit

A long agent run can be cut into a few semantic stages. In the instance studied here there are four: plan, research, review and answer. An LLM judge scores each stage of each rollout against a rubric written for that stage, giving a value in [0, 1] per stage. The reward is therefore not one terminal number broadcast to every token: "Rather than broadcast a single terminal score to all tokens" the method scores each stage separately.[^b1]

The return of a stage combines its own score with those of the later stages it enables. The method uses "a causal stage-dependence matrix" Λ, which gives zero weight to a stage's earlier stages and weight one to its own score, and the stage return is the Λ-weighted sum of judge scores from that stage onward. "Thus each stage keeps its own score while receiving credit" from the downstream stages it helps produce.[^b2] Broadcasting one terminal score to all stages is the special case where the weight sits entirely on the last stage. Advantages are then normalized within each stage across the rollout group, in the way GRPO normalizes, so no critic is trained.

The stated premise is a trade-off. "intermediate judging recovers process information omitted by terminal-only rewards" but it also brings judge noise.[^b3] The paper says its Appendix E.2, Thm. 3 formalizes when the stage-weighted credit wins: when the recovered intermediate signal outweighs cumulative judge misalignment.[^b4] I did not read that appendix; what I can report is the paper's claim that, on this view, "Thus SS-GRPO needs no oracle process reward" because the stage judgments themselves supply the intermediate signal.[^b5]

The rubrics are not fixed. The judge keeps a separate rubric buffer per stage, reuses rubrics that separate trajectories well, and "removes items that no longer separate trajectory quality."[^b6] The stage score is therefore judged against a moving standard, which the paper presents as the reason the intermediate reward stays adapted to the current policy.

The measured effect is an ablation on one 8B backbone, under a 600-step budget and a fixed 100-example subset per benchmark. Against answer-only GRPO, "both SS-GRPO and Meta-Policy improve over Baseline-RL, and the full recipe performs best."[^b7] The contrast with a per-turn process reward for search is drawn in [[answerability-delta-process-reward]], which scores what the policy could already answer at each search state and so does not need a rubric per stage. [[stage-structured-visual-reward]] also splits an output into tagged parts, but scores how much unique content each part holds, not whether it is judged correct.

## Limits

- One judge. Rubric generation, stage scoring and reflection evaluation all use Gemini Flash. The paper says "A stronger or more specialized judge could likely provide more accurate stage-level credit and higher-quality reflection rewards."[^b8] The size of the judge effect is not measured.
- Staleness. The training loop is asynchronous, and interruptions "can introduce additional staleness in the asynchronous reflection branch" and the judge-feedback pipeline, beyond the one-step lag the design intends.[^b9] Stage scores may therefore come from a policy a step or more behind.
- Scale of the evidence. The stage-versus-terminal comparison is a 600-step ablation on one backbone, on subsets of each benchmark. In the sections I read, no variance across seeds is reported.
- The matrix Λ. The paper's values for Λ and a sensitivity test over them were not in the parts I read. My inference is that the matrix encodes the assumption that a stage's quality is carried forward by later stages, and that a wrong matrix would move credit to the wrong stage without the run showing it.
- The method needs stages that can be separated in the text. Whether the same credit split works for tasks where stage boundaries blur is not tested.

## Related

- [[answerability-delta-process-reward]] — another process reward with no oracle, scored per search turn by the policy's own answer rather than by a stage rubric
- [[stage-structured-visual-reward]] — a stage-by-tag reward for a vision-language model that counts unique content and does not judge correctness

[^b1]: doi-10-48550-arxiv-2605-10899 — "Rather than broadcast a single terminal score to all tokens"
[^b2]: doi-10-48550-arxiv-2605-10899 — "Thus each stage keeps its own score while receiving credit"
[^b3]: doi-10-48550-arxiv-2605-10899 — "intermediate judging recovers process information omitted by terminal-only rewards"
[^b4]: doi-10-48550-arxiv-2605-10899 — "Appendix E.2, Thm. 3 formalizes this intuition"
[^b5]: doi-10-48550-arxiv-2605-10899 — "Thus SS-GRPO needs no oracle process reward"
[^b6]: doi-10-48550-arxiv-2605-10899 — "removes items that no longer separate trajectory quality"
[^b7]: doi-10-48550-arxiv-2605-10899 — "both SS-GRPO and Meta-Policy improve over Baseline-RL, and the full recipe performs best"
[^b8]: doi-10-48550-arxiv-2605-10899 — "likely provide more accurate stage-level credit and higher-quality reflection rewards"
[^b9]: doi-10-48550-arxiv-2605-10899 — "can introduce additional staleness in the asynchronous reflection branch"
