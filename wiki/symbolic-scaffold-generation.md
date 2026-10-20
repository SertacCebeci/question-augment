---
description: "An LLM answer can be bounded by a symbolic model of the domain used as the admissible space of moves, not as retrieved text; the paper reports ratings, not enforcement."
aliases: ["TMK-constrained generation", "symbolic control layer", "active generative constraint", "symbolic-LLM hybrid generation"]
sources: ["arxiv-2511-20942"]
---
# Symbolic scaffold generation

The architecture splits an explanation into two layers. A symbolic layer holds a model of the skill, and a generative layer interprets that model and writes the answer. The system, Ivy, combines "symbolic Task-Method-Knowledge (TMK) models with a generative interpretation layer".[^c1] The symbolic model carries finite-state mechanisms with start, success and failure states, guarded transitions, goal hierarchies and concepts.[^c2] What matters is the role the model plays inside generation. The authors set their design against approaches that treat structure as static context, and describe their own use of the model as "symbolic representations as active generative constraints".[^c3]

The mechanism runs in four stages. A question is first tested for scope by embedding similarity against the model's top-level names. A question "is in-scope and proceeds to structured inference"; any other question goes to an unconstrained retrieval agent.[^c4] The system then retrieves the top-k entries of the model, with Mechanism entries preferred for how-questions, and synthesizes an answer from them. A later stage compresses the draft while keeping the structure. The authors' stated intent for the synthesis step is that the model fixes what may be said: "the logic cannot drift", because the model "defines the valid space of moves and justifications".[^c5]

The constraint, as the procedure is written, lives in the prompt and in the retrieved content, not in the decoder. Algorithm 1 asks the model to "answer using d and Q" and then to improve that answer against each further entry.[^c6] Nothing in the procedure rejects a sentence that breaks a guard after it is produced. My reading: this makes the mechanism closer to in-context conditioning than to the grammar masking in [[constrained-decoding]], which makes a non-member impossible by construction. The two differ in what is guaranteed. Here the guarantee is the authors' expectation that the model follows the structure they supply.

What was measured is ratings, not violations. Expert-judged correctness "was 0.65 for both Ivy+TMK-Basic and Ivy+TMKStructured",[^c7] so the formal state machine did not raise the share of fully correct answers over the looser model. The structured variant "traded some partials for more zeros".[^c8] The gain the paper reports is in the three inferential ratings, which are described in [[procedural-explanation-structure]]. The authors frame the design as a hypothesis: "We hypothesize that this four-stage design keeps the generative model expressive yet bounded."[^c9]

## Limits

- No count of violated transitions is reported. Whether the generated text actually follows the guards, state by state, is not measured; the claim that the logic "cannot drift" is the design's intent, not an observed rate.
- The domain expert who rated the responses built the model being rated: "a domain expert who constructed the TMK model".[^c10] The structured system is therefore not rated blind to its own design.
- The scope gate is a similarity threshold over top-level names. A question outside the names falls back to an unconstrained system, so the bound covers only the questions the model can match. My reading: a skill without a finite-state form, or a question phrased outside the model's vocabulary, is not tested.
- The model is hand-built for each skill. The authors state the next step is to automate it: "We will automate TMK-Structured construction using a".[^c11] Whether the bound survives automated construction is open.
- The domain examples are one puzzle with a small state space. Transfer to skills whose steps are not guarded transitions is not shown in the sections read.
- The generator was one small model, GPT-4o-mini, for all four systems. Whether a stronger model drifts less under the same scaffold is not tested.

## Related

- [[constrained-decoding]] — enforces a grammar at the decoder; this design relies on prompt conditioning, so the two differ in what they guarantee
- [[structured-output]] — constrains the form of a reply; here the constraint is on what the explanation may say
- [[answer-structure-specification]] — the asker declares the shape of the answer; here a domain model declares the admissible content

[^c1]: arxiv-2511-20942 — "symbolic Task-Method-Knowledge (TMK) models with a generative interpretation layer"
[^c2]: arxiv-2511-20942 — "if a guard fails, control routes to the Failure state"
[^c3]: arxiv-2511-20942 — "symbolic representations as active generative constraints"
[^c4]: arxiv-2511-20942 — "is in-scope and proceeds to structured inference"
[^c5]: arxiv-2511-20942 — "the logic cannot drift"
[^c6]: arxiv-2511-20942 — "Prompt M to answer using d and Q"
[^c7]: arxiv-2511-20942 — "was 0.65 for both Ivy+TMK-Basic and Ivy+TMKStructured"
[^c8]: arxiv-2511-20942 — "TMK-Structured traded some partials for more zeros"
[^c9]: arxiv-2511-20942 — "We hypothesize that this four-stage design keeps the generative model expressive yet bounded."
[^c10]: arxiv-2511-20942 — "a domain expert who constructed the TMK model"
[^c11]: arxiv-2511-20942 — "We will automate TMK-Structured construction using a"
