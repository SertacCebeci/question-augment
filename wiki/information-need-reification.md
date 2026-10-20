---
description: "An agent externalizes its current reading of an underspecified request as an explicit, executable, inspectable specification the user refines toward the true need, instead of asking."
aliases: ["relational reification", "active information need", "latent information need", "I+", "I*"]
sources: ["arxiv-2604-14422", "arxiv-2601-03618"]
---
# Information need reification

> Instead of asking the user what they meant, show them — as a concrete,
> runnable object — what the system already decided they meant, and let
> them edit that object until it is right.

## Definition / Mechanism

Balaka & Castro Fernandez (2026) split "the question"
into two objects: the **latent information need** $I^*$, "the fully
specified characterization of the data required to solve a task," and the
**active information need** $I^+$, "the user's current articulation of
$I^*$ at a particular point in time" — necessarily incomplete, since
"relevant variables, filters, or constraints may only become apparent
after inspecting the data."[^c1]

Their system, Pneuma-Seeker, does not resolve the gap between $I^+$ and
$I^*$ by asking a clarifying question. It resolves it by refusing to let
the agent's interpretation stay implicit: "the interpretation of user
intent should be externalized into a concrete, inspectable artifact
separate from execution." Rather than a prompt whose output is an
answer, the question becomes "a specification that must be progressively
refined," reified as a pair $(T, S)$ — a set of target relations $T$ and
a script $S$ over them. "The resulting set of relations functions as
a shared contract between user and system. … Through iterative
refinement of the relations, users can progressively converge from
$I^+$ to $I^*$."[^c6]

The distinguishing move is that the externalized object is not a
read-only display of the interpretation: it is the same artifact the
system executes to produce the answer. Inspecting it and computing with
it are the same act, so correcting a misread attribute (e.g. which
column "outstanding" means) is a refinement of $(T,S)$ that is
immediately re-materializable, not a message fed back into a dialogue
the system must re-interpret. A secondary, self-directed instance of the
same principle appears at the row level: rather than sampling table rows
into context and trusting the sample, the agent "may issue executable
queries … to probe retrieved tables, e.g., verifying value existence,
computing distributions, or inspecting structural properties," which
"encourages it to … verify assumptions before committing to
interpretations" — the agent checks the world instead of asking the user
or guessing.[^c5]

## Why it matters

Under the ordinary pipeline the paper contrasts itself with, "the
question is typically interpreted implicitly by the model, translated
into reasoning traces or executable code, and executed directly" — the
interpretation is never a first-class object, so a wrong reading is
invisible until the final answer is wrong. Reification makes the
interpretation itself the site of iteration: "such ambiguities would be
difficult to identify from the chat interface alone, but become apparent
through inspection of the schema and sample values." This is a
distinct answer to "should the agent ask" from a clarifying question:
it substitutes an editable execution artifact for a dialogue turn,
trading a question the agent must decide to ask (and phrase, and time)
for an artifact the user can always inspect.

## Limits

The mechanism is walked through on two hand-picked use cases from the
authors' own procurement collaboration, each with a wall-clock time
(2m24s; 1m41s then 3m27s after refinement) but no baseline, no comparison
against a clarification-dialogue agent, and no measurement of how often
or how fast users actually converge $I^+$ to $I^*$ — this is a demo
report, not an evaluation. The reification itself can mislead rather
than help: a semantic join used to repair a failed equality join "can
recover useful correspondences when explicit identifiers are absent,
[but] it may also introduce imperfect matches," and nothing in the
artifact flags which joined rows are such near-misses — the user must
still notice the discrepancy by inspection. The formal mechanism
(the reification protocol itself) is developed in a companion paper the
extract only cites, not in the text read here.

## Evidence from the original Pneuma project paper

The earlier CIDR paper defines the same pair ("The active information need is the user's working hypothesis about what data is needed, which evolves through interaction and exploration to approximate the latent one") and fixes the reified object as a table set plus SQL queries held as shared state that both user and a planner edit.[^c7] It also measures convergence, which the companion paper does not. Each benchmark question is treated as a latent need; an LLM-simulated expert starts from a broad prompt and refines it only from system outputs. Two metrics are used: the share of questions on which the simulated user converges, and median turns to convergence (capped at 15).[^c8] Systems that only return tables (full-text search, a table retriever) struggled to converge because the simulated user had to interpret the results itself; a RAG baseline matched the reified system on turns, but the reified system converged most often.[^c9] On answer accuracy the reified system beat the baselines, while the RAG baseline answered nothing correctly because the questions needed computation, not interpretation of retrieved context.[^c10] The design also caps consecutive autonomous actions (5) so the state cannot drift from the need before user feedback corrects it (my reading: a bound on unchecked interpretation).[^c11]

## Limits of that evidence

Users are an LLM (GPT-4o) told to behave vaguely and reach the target "only ... if the system's output correctly leads you there"; the authors call this "not a full substitute for real studies." Two datasets (12 and 20 questions), web search disabled. Latency is about 70 s per turn. Convergence is judged against a known target question, which real users lack.

## Related

[[interpretation-externalization]], [[levels-of-information-need]],
[[active-probing]], [[visibility-action-gap]]

[^c1]: arxiv-2604-14422 — "We therefore distinguish between two notions of information need. The latent information need I ∗ denotes the fully specified characterization of the data required to solve a task. In contrast, an active information need I + represents the user’s current articulation of I ∗ at a particular point in time."
[^c5]: arxiv-2604-14422 — "In addition to receiving row samples, the model may issue executable queries through DBService to probe retrieved tables, e.g., verifying value existence, computing distributions, or inspecting structural properties. This protocol enables targeted evidence extraction while maintaining scalability and directly supports correctness by allowing the system to resolve structural irregularities that sampling-based approaches may miss. Although the model could in principle perform such checks, explicitly modeling this capability as an action encourages it to, e.g., verify assumptions before committing to interpretations."
[^c7]: arxiv-2601-03618 — "The active information need is the user’s working hypothesis about what data is needed, which evolves through interaction and exploration to approximate the latent one."
[^c8]: arxiv-2601-03618 — "median turns to convergence, which is the median of the number of times LLM Sim has to prompt a system to achieve convergence (with an imposed limit of 15)."
[^c9]: arxiv-2601-03618 — "Pneuma-Seeker consistently achieves the highest percentage of convergence and similar median turns to convergence as LlamaIndex."
[^c10]: arxiv-2601-03618 — "LlamaIndex, on the other hand, does not answer any questions correctly because the questions require actual computation"
[^c11]: arxiv-2601-03618 — "This limit is intended to prevent (𝑇 , 𝑄) from moving away from the latent information need before user feedback can correct it"
[^c6]: arxiv-2604-14422 — "The resulting set of relations functions as a shared contract between user and system. Given this set of relations, the system identifies relevant tables and materializes the specified relations. Through iterative refinement of the relations, users can progressively converge from I + to I ∗ ."
