---
description: "A gamma-contamination model replaces an empirical distribution by all measures keeping at least (1 minus gamma) of its mass, so choice sets widen to survive noisy protocols."
aliases: ["linear-vacuous model", "linear-vacuous mixture", "contamination model", "gamma-contamination"]
sources: ["arxiv-2512-05677"]
---
# Gamma-contamination model

A contamination model says the observed sample may be partly corrupted, and it
does so without naming the corruption. The paper builds its robustness on γ-contamination models, which it also
calls linear-vacuous models.[^c1] Within a set of probability measures on the
states, the model fixes the empirical distribution π̂ from the protocol and
admits every measure ξ with ξ ≥ (1 − γ)·π̂, read event by event, for γ in
[0, 1].[^c2] In words: ξ must keep at least a (1 − γ) share of the empirical
mass wherever the sample put it, and the remaining γ share may go anywhere.

This is a credal set in the imprecise-probability sense. At γ = 0 it collapses
to the empirical distribution, and at γ = 1 it admits every probability
measure. The paper says these models "originate in robust statistics"[^c9] and
names a classical member, the Imprecise Dirichlet Model: "A central example is
the Imprecise Dirichlet Model (Walley, 1996)".[^c3] For multinomial data that
model "admits a contamination-interpretation based on the" observed relative
frequencies.[^c10]

## Mechanism for choice

The model is attached to choice through a robust version of a choice function.
An empirical choice function gives one set of descriptions per protocol. Its
robust version is required to contain the original set, and to remain valid
for every disturbed sample drawn from a measure in the credal set. "In words,
Definition 8 views robustness as an outer expansion of the empirical choice
set."[^c4] The robust set keeps every description the empirical rule selects
and may add others. The added options are the price of robustness: a robust
choice is less decisive than the empirical one.

Credal sets also serve the paper's test, "as they allowed modeling contaminates
samples".[^c11] A modified test is then built to stay valid under a small
departure from the i.i.d. assumption, namely "slight deviations from its main
underlying assumption, namely the i.i.d. structure of the observed".[^c5]

## Limits

- The paper says the γ-model is an illustration: "this specific γ-contamination
  model shall primarily serve as an illustration".[^c6] Other contamination
  models are treated in its Section 6, and the choice among them is left open.
- The sections read here give no rule for choosing γ. The analyst sets it, and
  the output is only as robust as that setting. This is my reading of the parts
  read, not a result the paper reports.
- Contamination models cover noise in the sample, not a deterministic
  mechanism. The paper says that when the generation of states is suspected to
  be deterministic or adversarial, "our theory remains silent about these
  situations".[^c7]
- The test's power falls under strong departures from i.i.d.; the authors say
  it "will rapidly lose much of its power in such cases".[^c8]

## Related

- [[empirical-decision-problem]] — the protocol-based choice functions this model widens
- [[expected-utility]] — the rule under which the robust set is built for the EU-based choice
- [[credal-then-conformalize-interval-decomposition]] — credal sets used to show epistemic width, a different use of the same object

[^c1]: arxiv-2512-05677 — "we specifically build on γ-contamination models (or linear-vacuous models, see,"
[^c2]: arxiv-2512-05677
[^c3]: arxiv-2512-05677 — "A central example is the Imprecise Dirichlet Model (Walley, 1996)"
[^c9]: arxiv-2512-05677 — "They originate in robust statistics"
[^c10]: arxiv-2512-05677 — "admits a contamination-interpretation based on the"
[^c11]: arxiv-2512-05677 — "as they allowed modeling contaminates samples"
[^c4]: arxiv-2512-05677 — "In words, Definition 8 views robustness as an outer expansion of the empirical choice set"
[^c5]: arxiv-2512-05677 — "slight deviations from its main underlying assumption, namely the i.i.d. structure of the observed"
[^c6]: arxiv-2512-05677 — "this specific γ-contamination model shall primarily serve as an illustration"
[^c7]: arxiv-2512-05677 — "our theory remains silent about these situations"
[^c8]: arxiv-2512-05677 — "rapidly lose much of its power in such cases"
