---
description: "A system models every place a fact can come from — an LLM, the web, or the user — as a typed, queryable database, so a planner routes each sub-query to a source by cost and quality."
aliases: []
sources: ["arxiv-2604-15233"]
---
# Typed source abstraction

> The web, an LLM and the user are three databases with different query languages, not three special cases.

## Definition / Mechanism

The Data Intelligence Layer (DIL) generalizes "data source" past the[^s1]
traditional relational, document, graph and vector stores to include
three sources that a constraint-elicitation system usually treats as
qualitatively different from a database: an LLM, the open web, and the
user. "DIL explicitly models LLMs, the Web, and even the user as
structured, queryable sources, each with its own interface and
semantics" Aminnaseri et al. (2026). Concretely,
"DIL generalizes data sources to include: (1) LLMDB for commonsense
and world knowledge, (2) UserDB for capturing personal data and
context, (3) WebDB to capture on-demand extraction from web content.
Each source is modeled as a database system with its own native query
language (e.g. SQL, Cypher) as well as support for natural language
queries" A single request is decomposed at the field level and
each field is routed to whichever typed source answers it: in the
motivating example, "what are data scientist jobs?" maps to the jobs
relational database via NL2SQL, "which locations are considered Bay
Area?" maps to the LLM via NL2LLM, and "what jobs are suitable for
me?" maps to the user via NL2U, and the three structured outputs are
then joined by ordinary relational operators (`JOIN`, `IN`) into one
answer

Routing is not fixed at design time. A data registry catalogs every
available source's metadata, and a planner selects among them per
sub-query: "the planner leverages the data, model, and operator
registries to select operators and sources based on task, cost,
quality, and others" Treating the user as a source rather than a
one-off interrupt also gives the "ask" branch a persistence and a
staleness check that most human-in-the-loop mechanisms lack: "UserDB
may either leverage this information or initiate an interactive
session with the user to iteratively extract, clarify, and structure
relevant information, subsequently storing it for future use. UserDB
applies contextual judgment to assess the validity, freshness, and
relevance of stored data with respect to the current query, optionally
confirming with the user when uncertainty arises"

## Why it matters

Most of this wiki's routing mechanisms choose *among* one kind of
source — text index vs. image index, retrieve vs. ask — because the
asker's candidate sources are assumed to be answerable through one
interface. This framework instead makes the interface itself the thing
that varies: the LLM, the web and the user are given the *same*
standing (a schema, a native query language, structured output) so
that a query planner can compare and combine them the way a relational
optimizer compares join orders, rather than special-casing "ask the
user" as an escape hatch outside the query plan. The consequence for
where a constraint comes from is that the source is chosen by the same
task/cost/quality criterion the system uses for a database choice, and
the choice is a declarative, inspectable plan (a DAG of operators)
rather than an ad hoc branch in agent code.

## Limits

- This is a system-demonstration paper, not an evaluation of the
  routing policy: the planner is said to select "based on task, cost,
  quality, and others," but no experiment measures whether that
  selection is optimal, well-calibrated, or better than a fixed
  routing order — the criterion is asserted, not tested.
- The reported user study measures hackathon developers' experience
  building on the abstractions (onboarding, intuitiveness), not the
  quality of the sub-query decomposition or source choice the system
  makes at runtime; whether NL2SQL/NL2LLM/NL2U decomposition is correct
  or complete is unverified here.
- UserDB's freshness and confirmation judgment ("optionally confirming
  with the user when uncertainty arises") is described as contextual
  judgment without a stated decision rule; when it confirms versus
  silently reuses stored data is unspecified in the extract.

## Related

- [[groundedness-gated-tool-routing]] — also routes a sub-query to one of several source types by a learned criterion, but among retrieval modalities of one paper's own KB, not across a database/LLM/user split.
- [[trust-calibrated-supervisory-controller]] — routes among query, human-confirmed suggestion and autonomous fill by a cost-risk score, the closest existing analogue to treating "ask the user" as one ranked option among others.
- [[novice-expert-problem]] — the asker's problem of judging which source to trust when it cannot verify the answer itself; this framework instead lets a cost/quality criterion pick the source in the asker's place.
- [[constraint-as-information]] — the general claim that a constraint's origin does not change what it does; this framework is a concrete architecture where the origin (LLM, web, user) is tracked and still routed through one uniform interface.

[^s1]: arxiv-2604-15233
