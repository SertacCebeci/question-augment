---
description: "A quasi-online DPO variant that turns the discrete clarify-vs-answer choice, not a ranked question, into the preference pair, updated with on-policy trajectory simulation."
aliases: ["ACT", "action-based contrastive self-training", "quasi-online DPO for dialogue actions"]
sources: ["chen-2024"]
---
# Action-based contrastive self-training

> Not which question ranks highest, but which of two discrete actions — ask
> or answer — the model should have taken; the preference pair is built on
> the action, and updated against the model's own on-policy sample.

## Mechanism

Chen, Sun, Pfister & Arık propose ACT, a quasi-online extension of Direct
Preference Optimization (DPO) for teaching a conversational LLM to choose
between two dialogue actions, $S = \{\text{CLARIFY}, \text{ANSWER}\}$,
rather than to implicitly guess a user's intent under [[efe-planning-as-variational-inference|ambiguity]].[^c1]

Two-phase construction, per conversation turn $t_i = (p_i, r_i, g_i, a_i)$:

```text
1. Infer the ground-truth action a_i = G(p_i, r_i) (an annotator: human label or LLM classifier)
2. Set the rejected action a_i' = S \ a_i
3. Winning response y_w = r_i (ground truth); losing response y_l sampled from
   a high-capacity model conditioned on the rejected action a_i'
4. During training, sample an on-policy response y_i from the current policy;
   if its classified action disagrees with a_i, replace y_l with y_i
   (else simulate the multi-turn trajectory and keep whichever outcome — sampled or
   default — met the task heuristic as the winner)
5. Update with the DPO objective on the resulting (y_w, y_l) pair
```
[^c2]

On PACIFIC (tabular QA), Abg-CoQA (reading comprehension) and AmbigSQL (a new text-to-SQL disambiguation task built by perturbing Spider queries), ACT with 50 conversations outperformed SFT with 50 and matched or exceeded SFT with 250: e.g. on PACIFIC, Macro F1 (implicit ambiguity recognition) rose from 69.0 (SFT, 50 conversations) to 82.2 (ACT, 50 conversations), a result SFT needed 250 conversations to only just exceed (86.9).[^c3]

Ablations isolate three necessary components: action-based pairing (random action pairing drops Macro F1 to 63.2 from 82.2), on-policy sampling (off-policy DPO on the same data reaches only 74.8), and trajectory simulation (sampling without simulation reaches 81.4, short of the full 82.2 — and post-clarification F1 drops further, from 57.2 to 50.1).[^c4]

Action supervision can be replaced by a zero-shot LLM classifier with negligible loss: pseudo-labels from Gemini 1.5 Pro agreed with ground-truth action labels 98.5% of the time on PACIFIC, and ACT tuned on pseudo-labels reached 80.1–89.0 Macro F1 across data settings versus 82.2–89.6 with crowdsourced labels.[^c5]

## Transfer

| | |
|---|---|
| **In its home field (LLM alignment)** | DPO trains a policy from offline preference pairs over whole responses, usually ranked by human or model judgment of general quality. |
| **Here** | The preference pair is not two competing answers to the same question but two competing *actions* (clarify vs. answer) to the same ambiguous turn, with the losing member resampled on-policy each batch and, when the sampled action matches ground truth, replaced by a simulated multi-turn trajectory outcome instead of a single-turn response. |
| **What survives** | The DPO loss and its gradient form (Eq. 1–2 of the paper) are unchanged; what moves is only the source of the preference pair and its update schedule (quasi-online rather than fully offline). |
| **What does not** | DPO's single-turn framing does not survive — ACT needs a user simulator and a task heuristic to score a whole trajectory, machinery DPO itself does not require; nor does the paper's evidence transfer past its three tasks and one base model (Zephyr-7B) family — no result here shows the action-preference signal ranking a candidate *question*, only the binary clarify/answer choice. |

## Limits

- Single paper (arXiv 2406.00222, checked at Findings-level detail, not independently replicated); base model results are reported for Zephyr-7B/Mistral-7B and Gemma-2B only — the 82.2 vs 69.0 Macro F1 comparison above is this model family, this task, this data size.
- The action space tested is binary (CLARIFY/ANSWER); the paper states the method "can be extended to a broader action space" but does not test one.
- ACT decides *whether* to ask, not *which* question to ask among alternatives — it is a different training target from the EIG-ranked candidate-question preference of [[preference-optimization-for-questions]], not a replacement for it.
- The trajectory-simulation component depends on a user simulator and a task-specific success heuristic; both are themselves LLM-prompted and unverified independently in the paper.

## Related

[[preference-optimization-for-questions]] · [[clarification-benchmarks]] · [[preference-signal-against-asking]]

[^c1]: chen-2024
[^c2]: chen-2024
[^c3]: chen-2024
[^c4]: chen-2024
[^c5]: chen-2024
