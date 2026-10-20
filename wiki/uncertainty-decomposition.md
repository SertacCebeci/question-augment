---
description: "Separating the agent's uncertainty by type. Which uncertainty warrants a ```text ALEATORIC genuinely random in the world — questions don't help EPISTEMIC unknown but knowable — a question or search…"
aliases: ["aleatoric / epistemic / specification uncertainty", "uncertainty types for agents", "differentiated uncertainty communication"]
sources: ["hora-1996", "kendall-2017", "larocco-2026", "matsnev-2026", "suri-2026", "arxiv-2511-22567"]
---
# Uncertainty decomposition

> Separating the agent's uncertainty by type. Which uncertainty warrants a
> question?

## Three types

```text[^s1][^s2][^s3][^s4][^s5]
ALEATORIC       genuinely random in the world — questions don't help
EPISTEMIC       unknown but knowable — a question or search resolves it
SPECIFICATION   the user never said — ONLY the user can resolve it
```

## Why the split is critical

Each type calls for a **different action**:

| Type | Correct action |
|---|---|
| Aleatoric | Accept it, decide accordingly |
| Epistemic | Search / read / execute — do not ask the user |
| Specification | Ask the user, when a user is reachable and can say |

An agent that does not separate these makes one of two errors: **interrupting
the user at every uncertainty**, or **silently filling specification gaps**.

## Theoretical basis

[[data-processing-inequality]] motivates the split — it does not force it:

```text
Epistemic       →  information exists in the world; the DPI can be beaten (by searching)
Specification   →  information exists only in the user; the agent can never produce it
```

The three budgets in [[question-budgets]] line up with these three types
(this wiki's synthesis, not a result): the agent budget spends on what is
already latent, the world budget on the epistemic, the user budget on the
specification.

## Known as

| Field | Name there | Strength |
|---|---|---|
| Probability elicitation, Bayesian deep learning | aleatory / epistemic uncertainty (Hora 1996 `[?]`; Kendall & Gal 2017 `[?]`) | close — the same first two types, with no third member |
| LLM agents (Matsnev 2026) | *request uncertainty* $u$, set against *action confidence* | close — $u$ is the specification type; action confidence merges the other two |
| LLM agents (Suri et al. 2026) | *specification uncertainty* vs *model uncertainty* | close — the same cut, drawn over tool parameters rather than over the world |
| Healthcare AI, human-AI escalation (LaRocco et al. 2026) | differentiated uncertainty communication: aleatoric vs. epistemic, presented to clinicians as unlabelled scenarios | close — same two-way cut, drawn over a prescribing decision rather than over a parametric model; no specification member |

## Current research

Two 2026 works instantiate the split at the prompt level, and both draw it
two ways, not three. Matsnev (2026) separates **action confidence** (does
this action advance the task?) from **request uncertainty** $u \in [0,1]$
(is the goal fully specified?), and emits `request_clarification` whenever
$u \ge \theta$ (default $0.5$). On two clarification-augmented benchmarks in
which half the tasks are deliberately underspecified, and averaged over five
LLM backbones, the decomposition improves clarification F1 on
ALFWorld-Clarification by **73% over ReAct+UE** and by 36% over
Uncertainty-Aware Memory, and leads on WebShop-Clarification for every
[[backbone-of-a-formula|backbone]]. Suri et al. (2026) draw the same line inside a tool schema —
specification uncertainty over tool parameters and their domains vs model
uncertainty — and report 7–39% higher coverage on ambiguous tasks while
asking 1.5–2.7× fewer questions than prompting and uncertainty baselines.
See [[clarification-benchmarks]].

A survey of 136 U.S. prescribing clinicians ([[larocco-2026|LaRocco et al.
2026]], see [[clinician-veto]]) puts the aleatoric/epistemic cut to a
human-facing test rather than a model-facing one: given unlabelled scenarios
of each type, 69.6% of clinicians perceived at least some difference and
59.8% said the two require fundamentally different review approaches, with
preferred escalation content shifting from a competing-options summary
(71.0%, aleatoric) toward [[abstention]] (46.9% vs. 36.9% competing-options,
epistemic; both shifts significant after correction).

## Transfer

| | |
|---|---|
| **Home field** | a parametric model with a data-generating distribution: aleatoric is irreducible noise in that distribution, epistemic is variance over parameters that shrinks with data (Hora 1996 `[?]`; Kendall & Gal 2017 `[?]`) |
| **Here** | an agent's textual state, where neither the data-generating distribution nor a parameter posterior is defined |
| **What survives** | the reducible/irreducible distinction *as an action rule* — accept, or acquire, and from which source |
| **What does not** | (i) the measurability of the split: at home the two terms are estimated separately from one model; here there is no estimator, and the 2026 works substitute a prompted scalar; (ii) mutual exclusivity — the home pair partitions a variance, these three do not partition anything; (iii) the standing of "specification" as a member of the same taxonomy at all — it is a *source*-based category grafted onto a *nature*-based pair |

Where the split is measured rather than named, it is measured inside one
model. A mixture-density output head gives a single forward pass in which the
disagreement between mixture components is read as epistemic variance and
the spread within each component as aleatoric variance.[^s6] The two sum to
the predictive variance of the mixture. The work applies this to a
convolutional conditional neural process in sensor placement, and its authors
state that the epistemic estimate is not yet validated against error.[^s7]
My inference: this supplies the estimator the table above says is missing at
home, but it shows only that the split can be computed for a parametric
model, not that it tracks what a question can resolve. See
[[reducible-uncertainty-acquisition]].

## Limits

- Aleatoric/epistemic is standard (Hora 1996 `[?]`; Kendall & Gal 2017 `[?]`
  — both unverified in sources, no url on record); the split is quoted
  from this wiki's own record, not from the works read.
- The DPI reading and the budget correspondence are this wiki's own
  inference, not a theorem; [[data-processing-inequality]] flags the
  modelling choice they rest on (reading the agent as $Y$, and placing
  commitment outside the inequality by fiat).
- "Specification" as a third type comes from the 2026 clarification line and
  is a *source*-based, not a *nature*-based category — the three are not
  mutually exclusive.
- The action table assumes an available user who can articulate the missing
  specification. [[tacit-knowledge]] denies the second half; when it fails,
  specification uncertainty is not resolvable by asking either, and the
  remaining route is commitment ([[constraint-as-information]]).
- Neither 2026 work measures the three-way taxonomy: both collapse aleatoric
  and epistemic into one term (action confidence; model uncertainty), so the
  reported gains are evidence for the *specification / not-specification*
  cut only. `matsnev-2026` is a single-author preprint, not peer reviewed.
- Classifying a live uncertainty into one type is itself uncertain.
- LaRocco et al. (2026)'s surveyed clinicians prefer the
  agent to **abstain and escalate to a human** specifically for epistemic
  uncertainty, in tension with this table's "epistemic → search, do not ask
  the user" — a hypothetical-scenario stated preference, not evidence that
  search is unavailable or inferior there, but it names a real disagreement
  about the correct action for the epistemic case, not just its content.

## Related

[[calibration]] · [[question-budgets]] · [[data-processing-inequality]] · [[clarification-benchmarks]] · [[tacit-knowledge]] · [[constraint-as-information]] · [[clinician-veto]] · [[reducible-uncertainty-acquisition]]

[^s1]: hora-1996
[^s2]: kendall-2017
[^s3]: larocco-2026
[^s4]: matsnev-2026
[^s5]: suri-2026
[^s6]: arxiv-2511-22567 — "disagreement between the mixture components and aleatoric uncertainty as the spread of each individual component"
[^s7]: arxiv-2511-22567 — "Future work will focus on quantitative validation of the epistemic uncertainty estimates"
