---
description: "One phrase, four ways of getting a schema-shaped reply. Only one of them Tam et al. (2024) hold the first three apart as separate experimental conditions on the same models and tasks."
aliases: ["structured output", "structured generation", "format restriction"]
sources: ["geng-2023", "geng-2025", "tam-2024", "willard-2023"]
---
# Structured output

> One phrase, four ways of getting a schema-shaped reply. Only one of them
> makes an out-of-schema reply impossible; for the other three the same
> guarantee is an empirical rate that has to be measured.

## The name and what it covers

Tam et al. (2024) hold the first three apart as separate experimental[^s1][^s2][^s3][^s4]
conditions on the same models and tasks. The fourth is added here, by analogy
with the task-specific finetuned baselines Geng et al. (2023) compare
against — they present those as accuracy baselines on information extraction,
entity disambiguation and constituency parsing, not as a structured-output
method with a measured out-of-schema rate.

| Object | What it does | Can an ill-formed reply come back? | Member note |
|---|---|---|---|
| **Constrained decoding** (also *grammar-constrained decoding*, *JSON mode* as vendors describe it) | masks the vocabulary at each decoding step so the prefix stays inside the grammar | **no** — the output is in $L(G)$ by construction (Geng et al. 2023) | [[constrained-decoding]] |
| **Format-restricting instruction** | puts the schema in the prompt; nothing enforces it | yes — Tam et al. (2024) report non-zero parse-failure rates for this condition | none yet |
| **NL-to-Format** | answer in free text, then a second call converts the text into the schema | yes, at the conversion step (Tam et al. 2024) | none yet |
| **Schema-conditioned finetuning** | trains the answerer to emit the format | yes — nothing enforces the schema at decode time; **this note's inference**, no source cited here measures the rate | none yet |

The measurable difference is the parse-failure rate, and for the first three it
is not a matter of degree: the first is zero by construction and the second and
third are empirical and non-zero in Tam et al.'s measurements. Tam et al. (2024)
also report those three conditions scoring differently on the same task with the
same model, so a result obtained under one does not transfer to another. The
fourth is placed on the same axis by argument — training is not enforcement —
and the rate that would put it there is unmeasured here.

## Known as

| Field | Name there | Relation |
|---|---|---|
| LLM evaluation (Tam et al. 2024) | format restriction | close — the umbrella for all four, used when the question is what the restriction costs |
| NLP systems (Willard & Louf 2023; Geng et al. 2025) | structured generation | close — the same umbrella, used when the question is how the restriction is enforced |
| Vendor APIs | JSON mode | **not this concept** — a product name Tam et al. classify as constrained decoding on the vendor's description; the implementations are closed, so the assignment is by claim, not by inspection |
| NLP (Geng et al. 2023) | grammar-constrained decoding, GCD | **not this concept** — names the first member only, and is the property of [[constrained-decoding]] |

## Why the split matters here

Stall 5 asks whether what came back is a constraint. The only member that
answers structurally — a reply always identifies a cell of the declared
partition — is constrained decoding. For the other three, "the answer is
JSON" is a claim about observed behaviour that has to be measured, and the
out-of-schema reply that [[question-as-partition]] calls a corrective is still
reachable. Treating them as one turns an empirical rate into a guarantee.

## Limits

- The split is Tam et al.'s three experimental conditions plus a fourth this
  note adds; no source states it as a taxonomy, and the boundaries blur — a
  finetuned model decoded under a mask is both the first and the fourth.
- This note's claim that the parse-failure rate is the *measurable* difference
  rests on the grammar being the schema the asker wanted. A mask enforces the
  grammar it was given, not the schema in the asker's head; a wrong grammar
  fails silently and at rate zero.
- The three members without notes are unwritten, not judged uninteresting.

## Related

[[constrained-decoding]] · [[format-restriction-effect]] · [[elicitation-protocols]] · [[question-as-partition]] · [[expected-future-grammaticality]]

[^s1]: geng-2023
[^s2]: geng-2025
[^s3]: tam-2024
[^s4]: willard-2023
