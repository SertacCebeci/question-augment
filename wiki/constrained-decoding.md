---
description: "The asker writes the set of admissible answers as a formal grammar and the At each generation step an incremental parser computes which tokens keep the current prefix inside the prefix-language of …"
aliases: ["grammar-constrained decoding", "GCD", "guided generation", "constrained sampling"]
sources: ["beurer-kellner-2024", "geng-2023", "park-2024", "tam-2024", "willard-2023"]
---
# Constrained decoding

> The asker writes the set of admissible answers as a formal grammar and the
> decoder is forbidden to leave it: well-formedness stops being a property of
> the answerer and becomes a property of the channel.

## Definition / Mechanism

At each generation step an incremental parser computes which tokens keep the[^s1][^s2][^s3][^s4][^s5]
current prefix inside the prefix-language of the grammar $G$; the logits of
every other token are set to $-\infty$ and sampling proceeds on the
renormalised remainder. Because the grammar is prefix-closed, a completed
generation is in $L(G)$ by construction (Geng, Josifoski, Peyrard & West, EMNLP 2023).

Two properties of the construction are load-bearing for an asker.

- **The constraint can depend on the question.** Geng et al.'s
  *input-dependent grammars* let $G$ be built per input — the admissible
  answers can be exactly the live candidate set for this question, e.g. the
  entity catalogue rather than "a string". They report constrained LMs
  beating unconstrained ones and, on their tasks (information extraction,
  entity disambiguation, constituency parsing), task-specific finetuned
  models.
- **The mask is cheap if it is precomputed.** Willard & Louf (2023) reframe a
  regular constraint as a finite-state machine over the *vocabulary* and build
  an index from FSM state to allowed token ids, so the per-step cost stops
  scaling with the vocabulary scan; this is the construction behind the
  Outlines library.

## Known as

| Field | Name there | Relation |
|---|---|---|
| NLP (Geng et al. 2023) | grammar-constrained decoding, GCD | exact — the same masking construction, stated over context-free grammars |
| LLM serving (Willard & Louf 2023) | guided generation | exact — the same construction with the mask indexed by an FSM state |
| LLM evaluation (Tam et al. 2024) | JSON mode | close — a vendor product classified here by its description; what it masks is not published |
| Agent protocols (MCP, LangGraph) | elicitation with a `requestedSchema` | close — the same asker-declared answer set, but carried to the answerer as an instruction over a transport, so conformance is an observed rate rather than a construction ([[elicitation-protocols]]) |
| LLM systems | structured output, structured generation | **not this concept** — the umbrella over four different objects, held by [[structured-output]] |
| LLM systems (Tam et al. 2024) | format-restricting instruction | **not this concept** — the schema in the prompt with no enforcement; Tam et al. measure it as a condition of its own, so its parse-failure rate is empirical, not zero |

## Transfer

| | |
|---|---|
| **In its home field** | Formal language theory and parsing: a grammar defines a set of strings, membership is decidable, and a parser *rejects* a non-member after it has been produced. |
| **Here** | The grammar is the asker's declaration of the admissible answer set, applied prefix-wise during generation, so a non-member is never produced at all. |
| **What survives** | The membership guarantee ($\text{output} \in L(G)$) and prefix-closure, which is what makes incremental masking possible at all. |
| **What does not** | Anything about *which* member. Parsing ranks no string above another, and neither does the mask: the rate at which each member comes back is set by the grammar's shape rather than by the answerer ([[expected-future-grammaticality]]). The guarantee is also stated over characters, and only holds token-wise if the mask is computed on the model's own subword vocabulary — Beurer-Kellner, Fischer & Vechev (ICML 2024) show that methods which do not align the two "significantly impair task accuracy". |

## Why it matters

On stall 5 this is the only mechanism in the wiki that makes a reply outside
the question's partition *impossible* rather than unlikely. Two consequences
follow directly, and they point in opposite directions:

1. If the asker wants an answer recordable as a constraint, the grammar is the
   place to put the partition — not the prompt ([[structured-output]]), and not
   a schema handed over a transport. [[elicitation-protocols]] declares the
   same admissible answer set but sends it to the answerer as a
   `requestedSchema` with nothing in the channel enforcing it; there its claim
   that an empty answer is "blocked at the schema level" is a conformance rate
   to be measured, whereas here it is a property of the decoder.
2. Whatever the grammar omits cannot be said. The corrective that
   [[question-as-partition]] identifies as the only detector of a false
   presupposition, and the explicit no-opinion branch that
   [[survey-response-model]] shows is needed to keep pressure from
   manufacturing an opinion, are unreachable unless they are **members of the
   grammar**. A mask is a stronger version of the forced-choice instrument,
   not a defence against it.

## Limits

- The guarantee is over syntax. Membership in $L(G)$ is decidable; truth and
  relevance are not in the construction, so "the answer parsed" is not
  evidence that it is a constraint on the world. That reading of the
  mechanism is this wiki's, not a claim of the cited papers.
- The grammar must be written before the first answer, so the work moves from
  stall 5 back to stalls 1 and 3: an answer space that cannot be enumerated or
  parsed cannot be masked.
- The construction says nothing about accuracy. Whether forcing the format
  costs the answer anything is a separate, contested measurement
  ([[format-restriction-effect]]).
- Willard & Louf's efficiency claim is for regular constraints with a
  precomputed index; the precomputation is per grammar, so a per-question
  grammar pays it per question.
- The separation from [[elicitation-protocols]] is drawn from the two
  specifications' own descriptions of where enforcement sits; no source
  compares a mask and a transported schema on the same question.

## Related

[[structured-output]] · [[expected-future-grammaticality]] · [[format-restriction-effect]] · [[elicitation-protocols]] · [[question-as-partition]] · [[survey-response-model]]

[^s1]: beurer-kellner-2024
[^s2]: geng-2023
[^s3]: park-2024
[^s4]: tam-2024
[^s5]: willard-2023
