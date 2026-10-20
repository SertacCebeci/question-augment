---
description: "Whether to search is not a property of the question set (PopQA vs. For each question $q$, Kim (2026) collects two controlled traces: $N(q)$, the model's response with search disabled, and $S(q)$,"
aliases: ["search routing", "instance-level search routing", "counterfactual supervision for search routing"]
sources: ["kim-2026-when"]
---
# Counterfactual search-routing oracle

> Whether to search is not a property of the question set (PopQA vs.
> false-premise questions) — it is a property of the instance and the model
> answering it.

## The oracle

For each question $q$, Kim (2026) collects two controlled
traces: $N(q)$, the model's response with search disabled, and $S(q)$, its
response after being forced to issue a first-turn search call. A
task-specific evaluator scores each trace binary success $y_N, y_S \in
\{0,1\}$ (factual correctness for answerable questions; adequate correction,
clarification, or [[abstention]] for false-premise or underspecified ones). The
oracle label is: NO SEARCH if $y_N=1$ (search is not needed even if it would
also succeed); SEARCH if $y_N=0 \wedge y_S=1$ (search recovers a no-search
failure); UNSOLVED if both fail. UNSOLVED rows are excluded from routing
supervision and metrics — a paired double failure does not identify which
action was wrong.[^c1]

## Training on the oracle

The oracle supplies training targets for a routing policy that must decide,
given only $q$ (no forced tool call), whether to answer directly or search
first. Supervised fine-tuning imitates the oracle-consistent first action;
preference optimization (DPO with a chosen-response NLL term) prefers a
response beginning with the oracle action over one beginning with the
opposite. On held-out oracle-eligible test examples, this training raises
routing macro-F1 from a prompt-only selective-search baseline of 0.7082 to
0.8235 (Gemma E2B) and from 0.7053 to 0.8365 (Qwen3.5-4B); conditional
over-search (false SEARCH) and under-search (false NO SEARCH) both drop for
both models, though not uniformly — Gemma's gain is mostly reduced
over-search, Qwen's mostly reduced under-search.[^c2]

## Instance-dependent, not dataset-dependent

The oracle is computed per instance, not assigned by dataset: on PopQA
(answerable factual questions), forced search raises success from 0.1831 to
0.5096 for Qwen3.5-4B and from 0.1504 to 0.4813 for Gemma E2B, but not every
PopQA question gets a SEARCH label — one the model already answers correctly
without search is labeled NO SEARCH regardless. Symmetrically, a KUQ
false-premise or ambiguous question is not assumed to forbid search: if
forced search lets the model correct the premise or resolve the [[efe-planning-as-variational-inference|ambiguity]],
it is labeled SEARCH. The paper's claim is explicitly that dataset identity
predicts routing only weakly; the oracle is defined at the question level.[^c3]

## Known as

| Field | Name | Relation |
|---|---|---|
| llm-agents | search routing | exact — the paper's own term for the decision problem |
| llm-agents | instance-level search routing | exact — the paper's term emphasising the per-question grain |
| llm-agents | counterfactual supervision for search routing | exact — the paper's title, naming the oracle mechanism |

## Limits

The oracle is model-specific: because $y_N$ and $y_S$ depend on the model
being trained, a label set collected for one model does not transfer to
another, and the paper reports comparisons within a model across policies
rather than across models.[^c4]

The claim rests on two 4B-scale models, two task families (PopQA, KUQ), and
one search backend (Brave LLM Context); the 0.82-0.84 macro-F1 figures are
this experimental setup's numbers, not a general routing bound. UNSOLVED
cases (both traces fail) are excluded from the reported metric, so the
macro-F1 gain is computed only over the subset the oracle can label at all
— routing performance on the harder, unlabelable remainder is not measured
by this number.

## Related

- [[value-of-information]] — the oracle's NO SEARCH rule ("skip it if the
  no-search action already succeeds") is a task-success analogue of VoI's
  "ask only if the answer would change the decision"; the difference is
  that this oracle sets its threshold experimentally (a paired trace
  comparison), not from a formal utility model.
- [[abstention]] — NO SEARCH in the oracle includes direct answering,
  premise correction, clarification, and abstention as a single bucket;
  the oracle does not separately identify which of these four the model
  should have done.

[^c1]: kim-2026-when — "If the no-search trace succeeds, we assign NO SEARCH, since search is not necessary even if the forced-search trace also succeeds. If no-search fails but forced-search succeeds, we assign SEARCH, since search recovers a no-search failure. If both traces fail, we assign UNSOLVED."
[^c2]: kim-2026-when — "improving routing macro-F1 on oracle-eligible examples from 0.7082 to 0.8235 for Gemma E2B and from 0.7053 to 0.8365 for Qwen3.5-4B"
[^c3]: kim-2026-when — "Qwen3.5-4B improves from 0.1831 under no search to 0.5096 under forced search, while Gemma E2B improves from 0.1504 to 0.4813."
[^c4]: kim-2026-when — "Because the no-search and forced-search outcomes can differ across models, the induced oracle is model-specific rather than a fixed question-level annotation."
