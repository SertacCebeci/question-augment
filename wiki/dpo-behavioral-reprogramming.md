---
description: "A LoRA/DPO fine-tuning protocol that installs a high-frequency interrogative response pattern in an open-weight LLM, with measured rank, epoch and cross-lingual transfer bounds."
aliases: ["behavioral reprogramming", "cognitive plasticity", "Proactive Question Rate training", "DPO-induced Socratic persona"]
sources: ["malickova-2026"]
---
# DPO behavioral reprogramming

> Not ranking candidate questions but installing the habit of asking one:
> [[preference-optimization-for-questions|DPO]] applied to a narrow preference
> set can shift a model's terminal response from a statement to a question, and
> the shift only survives a floor on LoRA rank and a ceiling on epochs.

## Definition / Mechanism

Malíčková (2026) fine-tunes three open-weight chat models (Llama-3.1-8B,
Mistral-7B, Qwen3-14B) in two stages: supervised fine-tuning (SFT) on 1,458
conversational pairs, then DPO ($\beta = 0.15$) on 440 preference pairs
contrasting a "proactive, questioning" response against a "compliant,
passive" one. Success is measured by the **Question Rate (QR)**: the fraction
of generations whose terminal token is `?`.

A 405-job hyperparameter sweep over LoRA rank $r \in \{4,8,16,32\}$ found
$r=16$ (with $\alpha=32$) as the minimum capacity for the behavior to transfer
across languages: "we identified r = 16 ... as the critical multilingual
capacity threshold. A rank lower than 16 lacked the necessary subspace
dimensionality for cross-lingual transfer, while higher ranks induced rapid
overfitting on dominant syntactic structures."[^c1]

Training length is bounded on both sides: SFT generalization "diverges past
epoch three ... setting a strict mathematical boundary against memorization,"
and the DPO stage itself "was strictly capped at one epoch with a learning
rate of 5 × 10−5 and a Kullback-Leibler (KL) penalty coefficient of β = 0.15"
to avoid the same degradation.[^c2]

DPO, not SFT/LoRA alone, is what moves QR: LoRA-only adapters reached QR of
21.4% with ~95-word responses, while the DPO-aligned model reached 100%
short-response adherence (3.22 words/reply average) with category-specific QR
of 12–32% depending on the prompt's psychological category (e.g. suppressed
on "crisis" prompts, elevated on deflection/excuse-making prompts).[^c3]

## Why it matters

This is a protocol for installing *propensity to ask* directly in the
weights, distinct from ranking candidate questions by informativeness (see
[[preference-optimization-for-questions]]): the trained quantity here is
purely syntactic (does the turn end in `?`), not the axis the question
touches or its [[expected-information-gain|expected information gain]].

## Transfer

| | |
|---|---|
| **In its home field** | LoRA/DPO as a general parameter-efficient technique for shifting a model's output distribution toward a preferred response, independent of what the preference encodes. |
| **Here** | Applied to a preference pair set contrasting a terminal question against a terminal statement, to install a standing tendency to end a turn with a question. |
| **What survives** | That a small, curated preference set can decouple a categorical output *form* (statement vs. question) from a separately-controlled output *length*, and that this only takes hold above a LoRA-rank floor and within a short epoch window. |
| **What does not** | The numeric thresholds ($r=16$, one DPO epoch, $\beta=0.15$) are specific to this model family and 440-pair dataset; nothing here measures whether the induced questions are informative, on-axis, or answerable — only whether the turn ends in `?`. |

## Limits

- Single, non-peer-reviewed arXiv preprint (2026), one author, three base
  models; the wiki's own claim rests entirely on this one paper's reported
  numbers, `[?]` unverified beyond arXiv listing and abstract-level
  confirmation.
- Cross-lingual generalization from the source language (Slovak) is small-n
  and highly uneven: on a fixed 10-scenario-per-language evaluation,
  "Spanish (ES) demonstrated the highest structural retention, sustaining a
  proactive interrogation rate of 60.0% (6/10) ... German (DE) and Portuguese
  (PT) collapsed to a 0.0% inquiry rate (0/10)," while average response
  length stayed under 6 words in every language — the syntactic (brevity)
  constraint transferred everywhere the semantic (questioning) one did not.
  Ten scenarios per language cannot separate a true effect from evaluation
  noise.[^c4]
- QR is the paper's own metric and measures only whether a turn ends in a
  question mark; it says nothing about whether the question opens a useful
  axis or advances the conversation.
- The paper attributes cross-lingual failure to "tokenization fragmentation
  and the absence of explicit multi-lingual preference alignment," which is
  the authors' own explanation, not independently tested in this work.

## Related

[[preference-optimization-for-questions]] · [[expected-information-gain]] · [[socratic-method]]

[^c1]: malickova-2026 — "we identified r = 16 (with α = 32 and dropout 0.1) as the critical multilingual capacity threshold. A rank lower than 16 lacked the necessary subspace dimensionality for cross-lingual transfer, while higher ranks induced rapid overfitting on dominant syntactic structures."
[^c2]: malickova-2026 — "we prove that for low-resource fine-tuning, the generalization gap diverges past epoch three (reaching a validation loss of 0.919), setting a strict mathematical boundary against memorization."
[^c3]: malickova-2026 — "LoRA-only adapters [12] achieved an interrogative response rate (Question Rate, QR) of only 21.4%, generating overly explanatory responses averaging 95 words per turn"
[^c4]: malickova-2026 — "Spanish (ES) demonstrated the highest structural retention, sustaining a proactive interrogation rate of 60.0% (6/10), followed by English (EN) at 30.0% (3/10). However, syntactically distant languages like German (DE) and Portuguese (PT) collapsed to a 0.0% inquiry rate (0/10)."
