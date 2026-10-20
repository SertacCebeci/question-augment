---
description: "An agent asking a question is no longer a text behaviour but a protocol Two shipped agent runtimes carry the primitive, and they are the evidence that the class exists: **2025-06-18**,"
aliases: ["MCP elicitation", "human-in-the-loop interrupt"]
sources: ["anthropic-2025-mcp", "langchain-2026-interrupt", "hemming-2017"]
---
# Elicitation — asking at the protocol level

> An agent asking a question is no longer a text behaviour but a protocol
> primitive: a typed request that suspends execution until a constraint arrives.

## Who uses it, where

Two shipped agent runtimes carry the primitive, and they are the evidence that[^s1][^s2][^s3]
the class exists:

- **Anthropic's Model Context Protocol**, in the specification revision
  **2025-06-18**, which introduced `elicitation` as a client capability — the
  spec page says it is "newly introduced in this version".
- **LangChain's LangGraph**, whose `interrupt()` / `Command(resume=…)` pair is
  the documented human-in-the-loop mechanism (LangChain, *Interrupts*, documentation read 2026-09-10).

## MCP elicitation

In MCP (Anthropic, spec revision 2025-06-18), a server that cannot proceed
sends `elicitation/create` to the **client**, which puts it to the user:

```text
"I cannot continue without X"
   ↓
message + requestedSchema: JSON Schema  (date, amount, option, ...)
   ↓
the user fills it, the client returns it, the flow resumes
```

Three details of that revision are load-bearing:

- `requestedSchema` is a **restricted** subset of JSON Schema — flat objects,
  primitive properties only (string, number/integer, boolean, enum); nested
  structures and arrays of objects are deliberately excluded.
- The reply carries one of **three actions**: `accept` (with `content`),
  `decline` (explicit refusal), `cancel` (dismissed without choosing). Refusal
  is part of the protocol, not an error.
- Servers **MUST NOT** use elicitation to request sensitive information — the
  channel is scoped by policy, not only by schema.

## LangGraph interrupt

`interrupt()` inside a node pauses the graph, surfaces a JSON-serialisable
payload to the caller, and persists the state through the **checkpointer** under
a `thread_id`; the graph is resumed by invoking it again with
`Command(resume=…)`, whose value becomes the return value of the `interrupt()`
call (LangChain documentation). Asking as a state machine:

```text
RUNNING → NEEDS_INFO → ASKING → WAITING → UPDATE_BELIEFS → RUNNING
```

Two documented conditions: without a checkpointer and a stable `thread_id`
there is nothing to resume, and on resume the **whole node re-runs from its
start**, so any side effect before the `interrupt()` must be idempotent.

## Known as

| Field | Name there | Relation |
|---|---|---|
| MCP (Anthropic) | MCP elicitation / `elicitation/create` | close — one vendor instance of the class, with its own schema restrictions and its own three-action reply |
| LangGraph (LangChain) | human-in-the-loop interrupt | close — the same class realised as a durable pause, with no schema on the reply at all |
| Decision analysis, risk assessment | structured (expert) elicitation | **not this concept** — a methodology for extracting and combining experts' probability judgements (Hemming et al. 2017, IDEA protocol), i.e. a policy for *what* to ask and how to aggregate answers, not a transport for carrying a request |

The first two are instances, not synonyms: neither is `exact`, because a schema
restriction that MCP imposes has no counterpart in LangGraph, and a checkpointer
requirement that LangGraph imposes has no counterpart in MCP.

## Why the separation matters

**Question policy and transport must be separated.**

```text
Policy     what to ask, whom, when     →  the subject of this wiki
Transport  how the question travels    →  MCP / LangGraph / CLI
```

A questioning process should define the former and not depend on the latter.
Otherwise task-independence is lost. The three-action reply and the
checkpointer are transport facts; which slot of $W$ to open is not.

## The advantage of structured answers

Requesting an answer against a schema buys two things over free text:

1. The answer becomes **recordable as a constraint**
   ([[constraint-as-information]])
2. Empty "it depends" answers are **blocked at the schema level**

The second is a structural defence against the emptiest kind of answer — see
[[constraint-as-information]].

## Limits

- **A schema that blocks the empty answer records a constraint only when the
  answerer actually holds one.** Without an explicit no-opinion / out-of-schema
  branch, forcing the reply into the schema converts non-knowledge into a
  recorded constraint: [[survey-response-model]] measures this directly (Bishop
  et al. 1986, ~30% report an opinion on fictitious legislation; an explicit
  "no opinion" option removes most of it), and [[question-as-partition]]
  requires a channel for a reply that falls outside every cell. MCP's `decline`
  and `cancel` actions are a partial defence — they distinguish refusal from
  content — but neither carries *why*, and LangGraph's `resume` value has no
  such branch at all.
- Describes two specific protocols at named revisions (MCP 2025-06-18;
  LangGraph documentation as of 2026-09-10); both will change, and MCP's own
  spec warns the design may evolve.
- Schemas block "it depends" only when the answer space is enumerable. MCP's
  restriction to flat primitive properties makes this sharper: any question
  whose answer is a structure cannot be elicited in one round.
- Policy/transport separation is a design principle argued here, not a result
  either specification states.

## Related

[[compound-ai-systems]] · [[constraint-as-information]] · [[question-budgets]] · [[survey-response-model]] · [[question-as-partition]]

[^s1]: anthropic-2025-mcp
[^s2]: langchain-2026-interrupt
[^s3]: hemming-2017
