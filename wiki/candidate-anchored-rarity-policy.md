---
description: "A scoring rule for picking the next diagnostic question that combines current-disease rank, within-disease frequency, catalogue rarity, and a specificity boost."
aliases: ["CAR policy", "candidate-anchored rarity"]
sources: ["zaripova-2026"]
---
# Candidate-anchored rarity policy

> HPOQuest's rule for choosing the next follow-up question in sequential
> rare-disease diagnosis: score each eligible Human Phenotype Ontology term
> by how characteristic it is of the currently top-ranked diseases and how
> rare it is across the whole disease catalogue, not by expected [[entropy]]
> reduction alone.

## Mechanism

Starting from a small seed of confirmed phenotypes, HPOQuest maintains a
softmax disease posterior $\pi(d\mid C)$ over confirmed phenotypes $C$ and a
candidate question set $F_t$ constrained to the ontology neighbourhood of
what has been asked (children/siblings of confirmed terms, pruned subtrees
of denied ones). For each eligible term $h \in F_t$, the CAR policy scores
it by summing, over the $M$ currently top-ranked diseases, the product of
(1) that disease's current posterior weight, (2) how frequent $h$ is
within that disease's phenotype profile, (3) $h$'s rarity across the whole
catalogue ($-\log$ of the fraction of diseases carrying it), and (4) a
boost when $h$ is common within the disease but rare catalogue-wide.
Higher scores identify phenotypes that are both characteristic of the
current candidate diseases and discriminative across the disease
catalogue.[^c1]

Questions scoring above a fixed threshold are asked in descending order up
to a per-round and total budget; a yes or yes-branch response expands the
candidate set toward the confirmed term's descendants, a no removes the
term and its whole subtree, and asked/removed terms cannot be selected
again — so $F_t$ is not the full ontology at any step, only the current
frontier.

## Why it matters

The paper's own controlled ablation swaps only the ranking policy while
holding the acquisition loop, responses and diagnoser fixed: one-step
[[expected-information-gain|expected information gain]] (ranking candidates by expected entropy
reduction of the top-$M$ posterior) is a directly comparable baseline in
the same loop. On the MME cohort, CAR reaches 35.0% / 42.5% Recall@1/3
against plain EIG's 22.5% / 37.5%, and a reciprocal-rank fusion of CAR and
EIG (RRF) matches or exceeds both.[^c2]

Against no acquisition at all (diagnosing from the same three seed
phenotypes with an LLM or a full-profile-trained baseline), active
acquisition's overall effect is large: HPOQuest reports gains of up to 30
percentage points at Recall@1 and 45 points at Recall@5 on the hardest
cohort.[^c3]

## Limits

The comparison rests on a **deterministic, closed-world response
simulator**: a term absent from a patient's recorded positive-phenotype
set, with no recorded descendant, is scored as a firm "no" — real
clinicians can answer "unknown," which this design does not model. All
nine of CAR's hyperparameters ($\theta_s,\gamma,\lambda,\beta,\phi,\tau,
\theta_f,\theta_r,\theta_a$) are hand-set to one configuration and not
learned or swept per cohort; the ablation is against three named
alternatives (LLM-guided selection, EIG, RRF) in one domain (HPO-coded
rare-disease diagnosis with four RareBench cohorts), not a general claim
that catalogue-rarity weighting beats entropy reduction outside this
setting.

## Related

[[expected-information-gain]] · [[generalized-binary-search]] · [[value-of-information]] · Zaripova et al. (2026)

[^c1]: zaripova-2026 — "Higher scores identify phenotypes that are both characteristic of the current candidate diseases and discriminative across the disease catalogue."
[^c2]: zaripova-2026 — "We compare CAR with three acquisition policies under the same experimental setting."
[^c3]: zaripova-2026 — "HPOQuest substantially improves diagnosis from sparse initial phenotypes, with gains of up to 30% points at Recall@1 and 45% points at Recall@5."
