---
description: "Generation as a state, a partial query plus its execution result, moved by extend, revise, explore and finalize steps that the executor's output triggers rather than one pass."
aliases: ["feedback-guided state transitions", "generation-state evolution", "execution-feedback revision", "dual-state reasoning"]
sources: ["arxiv-2511-21402"]
---
# Execution-feedback state revision

Hao et al. (2025) build a Text-to-SQL system, DSR-SQL, around one change of shape: the answer is not written in a single pass. The generator carries a state, and at each step that state is a pair, "where Yt is a partial query and" Rt is the result of running it.[^c1] "Rather than generating the entire SQL" in one go, the model moves this state forward.[^c2]

The move is chosen by a feedback condition, and the paper names four actions. Extend adds the next part of the query when the execution gives a usable result. Revise fires when "If execution feedback reveals a semantic or logical inconsistency": "the model revises the existing partial query, correcting the reasoning path" against the error the database returned.[^c3][^c4] Explore issues short probing queries when the result is empty or unexpected: "Explore. When execution produces unexpected" results send the model to probe value ranges and joins before it resumes.[^c5] Finalize stops the evolution "Once all sub-goals have been resolved" and the executed result matches the user's intent.[^c6]

What is new here is where the correction comes from. The paper's motivation is that prior reasoning is "a one-way process": each step "proceeds without feedback" and so cannot be corrected.[^c7] The fix is to make the trigger an observation from outside the model. A revision is then checked against a result the model did not produce: an empty set, a value outside the expected range, an error message. The model's own belief about its previous step is not the reference. The paper's single worked case shows the loop operating: "upon observing the execution feedback from the preceding sub-SQL, the LLM reevaluated the current business logic".[^c8]

The claim the paper makes for the loop is comparative. Its ablation says the state-evolution module "attains a higher performance ceiling than conventional divide-and-conquer methods" and that "feedback-guided state transitions to incrementally" align intent with the database.[^c9][^c10] The headline number is execution accuracy of "35.28%" on Spider 2.0-Snow and "68.32%" on BIRD, with no post-training and no in-context examples.[^c11]

For the wiki, the transferable concept is a revision whose trigger is an external outcome. The asker-side analogue (my inference, not tested in the paper) is that a formulation can be revised by what its first answer returns, rather than by the asker re-reading their own question.

## Limits

- The loop is not isolated numerically in what I read. The ablation shows that "Omission of any module produces measurable performance drops of varying magnitudes,"[^c10] but the GSE-only figure sits in a table I did not read, so the size of the feedback gain is not stated here.
- The trigger is a judgment made by the model from the result ("valid and informative", "unexpected or empty"). The paper gives the four actions in prose; how the prompt makes that choice is in an appendix I did not read. A miscalibrated judgment would revise a correct query or keep a wrong one.
- The mechanism needs a result that can be executed. Where the answer cannot be run against a database, the four-action scheme has no external signal to act on (my inference).
- The result is on two benchmarks with a fixed set of backbones. Gains are reported against divide-and-conquer baselines, not against a version of the same system with the loop switched off and nothing else changed.
- Self-correction is not new as such. Without an external signal, repeated self-correction is read to converge after a few rounds, and the Related note records that the convergence is measured, not guaranteed to help.

## Related

- [[intrinsic-self-correction-convergence]] — self-correction with no external signal, which plateaus; this note is the case where the signal comes from an executor.
- [[ambiguity-driven-execution-probing]] — the same executor used to choose which reading of a question is meant, rather than to revise a query already written.

[^c1]: arxiv-2511-21402 — "where Yt is a partial query and"
[^c2]: arxiv-2511-21402 — "Rather than generating the entire SQL"
[^c3]: arxiv-2511-21402 — "Revise. If execution feedback reveals a semantic"
[^c4]: arxiv-2511-21402 — "the model revises the existing partial query, correcting the reasoning path"
[^c5]: arxiv-2511-21402 — "Explore. When execution produces unexpected"
[^c6]: arxiv-2511-21402 — "Finalize. Once all sub-goals have been resolved"
[^c7]: arxiv-2511-21402 — "existing approaches treat reasoning as a one-way process"
[^c8]: arxiv-2511-21402 — "upon observing the execution feedback from the preceding sub-SQL, the LLM reevaluated the current business logic"
[^c9]: arxiv-2511-21402 — "attains a higher performance ceiling than conventional divide-and-conquer methods"
[^c10]: arxiv-2511-21402 — "Omission of any module produces measurable performance drops of varying magnitudes."
[^c11]: arxiv-2511-21402 — "reaching 35.28% execution accuracy on Spider 2.0-Snow and 68.32%"
