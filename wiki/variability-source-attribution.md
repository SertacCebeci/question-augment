---
description: "Variability alone does not justify an autonomous agent; sorting it by source (model, tool, or workflow) shows whether adaptive decision-making is needed at all."
aliases: ["dynamism attribution", "True Dynamism Score"]
sources: ["arxiv-2512-02228"]
---
# Variability-source attribution

Outputs that vary from run to run do not, by that fact alone, call for an
autonomous agent. The STRIDE paper makes the source of the variability the
deciding term. It sorts variability into three kinds: model-induced, from
prompt ambiguity and stochastic sampling; tool-induced, from API volatility
and changing tool responses; and workflow-induced, from conditional branching
and environmental change that alter the path through a task.[^c1] The paper
says model-induced variability "typically resolves through improved prompt
engineering, temperature controls, or deterministic sampling" rather than
through agentic capabilities.[^c2] Tool-induced variability "typically require[s]
robust error handling", with retries and adaptive parsing, and not autonomous
decisions.[^c3] Only the third kind "strongly indicates agentic solution needs,
as it requires dynamic decision-making and" adaptive planning.[^c4]

The mechanism is a score. The paper's True Dynamism Score counts workflow
variability and tool volatility in favour of adaptivity and model instability
against it, "where W (s) is workflow variability, V (s) tool volatility, and
M (s) model instability", and "A high TDS implies that autonomy and adaptivity
are required."[^c5] The distinction is drawn against a plain-variance trigger.
A stochastic model asked for a random greeting varies its output "due to model
stochasticity", and the paper holds that this needs no agent.[^c6] What the
attribution changes is the diagnosis: an output that varies can vary for
different reasons, and the reason, not the amount of variation, is what the
paper ties to the need for autonomy. This reading is mine; the paper states
the three kinds and the rule, and does not test the rule apart from its
composite score.

The paper gives the score a measured role. Removing it from the full system
"Without the True Dynamism Score, accuracy fell by 12%" on the paper's 30
tasks, and the authors attribute this to borderline cases such as "meeting
summarization versus compliance verification" that the system could not
separate.[^c7]

## Limits

- The three-way split and the rule that only workflow variability needs
  autonomy are the authors' argument. The only evidence offered is the
  ablation of the whole composite score, which cannot isolate the attribution
  from the decomposition, reflection and expert-tuned weights around it.[^c7]
- The text I read gives no values for the score's coefficients, so the
  attribution cannot be reproduced from it. The paper says the weights were
  refined "through grid search optimization on labeled historical" task data,
  and later "Adjusted weights in the True Dynamism Score to better separate
  model-," after expert feedback.[^c8] The labels and the adjustment are the
  authors' own.
- Errors concentrated where "where dynamism was underestimated", in borderline
  cases such as multi-document summarization.[^c9] The attribution misses
  exactly the cases where the split is least clear.
- The evidence is 30 tasks, "Evaluated across 30 real-world tasks spanning SRE,
  compliance, and enterprise", judged by the authors' experts.[^c10] The paper
  calls its scoring functions "heuristic by design".[^c11] Its extension to
  multimodal tasks is stated as future work: "we will extend evaluation beyond
  the 30 tasks to include multimodal tasks (vision/audio)."[^c12]
- Only the distinction is carried here. The paper's decision rule, with its
  threshold and weights for the agentic suitability score, is a method for
  choosing a deployment and is not part of this note.

## Related

- [[agentic-rag-autonomy-principles]] — defines agency by who controls the
  loop; workflow variability is the case in which that control has work to do
  (my reading)
- [[search-necessity-filter]] — also asks whether a task needs an external step
  before it is run, but measures the need from a no-search answer rather than
  from the variability in the task's structure

[^c1]: arxiv-2512-02228 — "Workflow-induced variability, involves systemic execution complexity, including conditional"
[^c2]: arxiv-2512-02228 — "through improved prompt engineering, temperature controls, or deterministic sampling"
[^c3]: arxiv-2512-02228 — "These challenges typically require robust error handling"
[^c4]: arxiv-2512-02228 — "strongly indicates agentic solution needs, as it requires dynamic decision-making and"
[^c5]: arxiv-2512-02228 — "where W (s) is workflow variability, V (s) tool volatility, and M (s) model instability"
[^c6]: arxiv-2512-02228 — "may produce different outputs each time due to model stochasticity"
[^c7]: arxiv-2512-02228 — "Without the True Dynamism Score, accuracy fell by 12%"
[^c8]: arxiv-2512-02228 — "STRIDE continuously refines these weights through grid search optimization on labeled historical"
[^c9]: arxiv-2512-02228 — "where dynamism was underestimated"
[^c10]: arxiv-2512-02228 — "Evaluated across 30 real-world tasks spanning SRE, compliance, and enterprise"
[^c11]: arxiv-2512-02228 — "scoring functions are heuristic by design"
[^c12]: arxiv-2512-02228 — "we will extend evaluation beyond the 30 tasks to include multimodal tasks (vision/audio)"
