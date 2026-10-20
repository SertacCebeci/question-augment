---
description: "When a query's intent implies an answer the data cannot support, substitute a feasible, transparently-labeled computable proxy instead of hallucinating or refusing outright."
aliases: ["Proxy Instantiation"]
sources: ["arxiv-2604-17133"]
---
# Proxy instantiation

> An intent the data cannot answer is not a false premise to reject and not
> a gap to guess at — it is a request to be re-read into the nearest
> question the data can actually settle, with the substitution said aloud.

## Definition / Mechanism

**The problem (CGM-Agent, 2026).** In a question-answering
agent over continuous-glucose-monitor (CGM) time series, real-world user
queries routinely name an intent the underlying data cannot directly
establish. "Intent Ambiguity. Real-world queries often underspecify the
desired analysis." A subclass of these queries names a causal or
behavioral link the CGM stream alone cannot certify — *"Does splitting
insulin boluses help me lower my insulin intake?"*, *"What patterns do I
see around my menstrual cycle?"* — while still being groundable in an
adjacent, computable quantity.

**The mechanism.** A first layer (the Input Processor) classifies every
query into one of three feasibility classes before any computation runs:
directly answerable from CGM data, answerable via a proxy, or unanswerable.
"For questions that imply a causal link (e.g., impact of lifestyle) but
lack explicit logs, we employ Proxy Instantiation." The query is rewritten
from its causal or intent-level form $q$ into a time-windowed, feature-level
form $q'$ that the deterministic toolkit can execute — e.g. "patterns around
my menstrual cycle" becomes "plot my typical daily CGM blood glucose trends
for [Date A] to [Date B]". The rewrite is a *comparative or descriptive*
statistic standing in for the causal claim, never an estimate of the causal
claim itself: the agent reports "data-driven correlations (e.g., 'Glucose
was lower during your workout window') while acknowledging the lack of
definitive causation."[^c3] A distinct, disjoint class — genuinely unanswerable
queries (missing modality, sensor-hardware questions, forecasting, medical
consultation) — receives no proxy at all: "the Input Processor is trained to
generate an explanation e ... instead of attempting a hallucinated
calculation." Proxy instantiation is therefore the middle path between
answering-as-asked (impossible here) and refusing outright (available data
going unused): substitute, execute, and label the substitution in the
response rather than passing the causal framing through silently.

**What removing the read costs.** Ablating the Input Processor entirely —
feeding the raw ambiguous query straight to the tool-calling layer — costs
most of its accuracy in feature identification, not downstream reasoning:
"the significant decline in F1 ($\Delta=0.19$) reveals that the primary
bottleneck for raw LLMs is correctly identifying and aligning the required
feature parameters," while Value Accuracy on the queries it does solve
correctly drops far less ($\Delta=0.06$). The comprehension layer, not the
computation, is where an ambiguous intent is lost or kept.

## Why it matters

Most treatments of an unanswerable or ambiguous question offer only two
moves: answer (possibly by hallucinating the missing link) or abstain
(discard a query the data could partially serve). Proxy instantiation adds
a third, structured move that is specific to *intent*-level ambiguity
(as opposed to a false premise, which has no acceptable answer at all): read
the causal or vague request down to the strongest claim the data can
actually carry, execute that, and say explicitly which substitution was
made. This is a comprehension act, not a computation one — it happens before
any tool call, and the paper's ablation shows the accuracy cost of skipping
it lands almost entirely on correctly identifying what was asked, not on
executing it.

## Limits

The proxy set is hand-authored (a fixed table of causal-intent → feature
mappings) and evaluated only within one domain (CGM time series) and one
downstream toolkit; whether the substitution generalizes to intents outside
the curated table, or to other measurement modalities, is unverified. The
paper reports the mechanism's *product* (Table 13 of examples) rather than a
general procedure for deriving a proxy from an arbitrary infeasible intent,
and does not measure whether users judge the substituted answer as
satisfying their original intent, only that the substitute is computable and
labeled.[^c3]

## Related

- [[false-premise-question]]
- [[gated-answerability-rule]]
- [[interpretation-space]]
- [[levels-of-information-need]]

[^c3]: arxiv-2604-17133 — "while acknowledging the lack of definitive causation."
