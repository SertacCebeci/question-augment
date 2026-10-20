---
description: "A user preference is written as a targeted weight edit of a knowledge tuple; the edit survives dialogue turns where prompting decays, but plain rank-one edits fail on paraphrased and implicit queries."
aliases: ["Personalization Editing", "editing-based personalization", "knowledge editing for personalization"]
sources: ["doi-10-48550-arxiv-2512-13676"]
---
# Personalization as model editing

The paper treats a user preference as one fact in a model's knowledge base. Its framework, Personalization Editing, starts from a knowledge tuple: "Personalization Editing operates on a structure analogous to a knowledge tuple (s, r, o)".[^c1] The subject s is the topic of the preference (in the paper's example, "restaurants"), and the object o is the answer the model would give by default. Personalization replaces o with a target o* that reflects the user, while "Here, the user and predicate" are held fixed and only the response changes.[^c2]

The edit is a constrained update. The model should produce the target on the questions generated for that edit, and "the editing must maintain consistency on all inputs" outside that set, so that unrelated behaviour is not disturbed.[^c3]

## Why an edit, not a prompt or a fine-tune

The paper sets editing against two older routes. Fine-tuning is "expensive, and prone to catastrophic forgetting", and it needs domain data.[^c4] Prompting places the preference in the context, where in long prompts it "becomes diluted in long prompts, causing the models to become increasingly unreliable".[^c5] Editing is offered as the third option: a targeted update that "overrides the original model’s behavior while preserving unrelated behaviors".[^c6]

## How the edit is located and written

The editors come from knowledge editing. ROME is "Rank-one model editing that localizes factual associations in MLP" modules through causal intervention, and then makes a rank-one change to those weights.[^c7] The parameter-efficient baselines share one strategy: "first identify the most relevant layer, often a specific Feed-Forward Network layer, responsible for" the target knowledge, then update only that location.[^c8] Locating and writing a single layer is what makes the edit cheap, and it is also the choice the later sections test.

## What is measured

The main metric is Efficacy: the score "is equivalent to the success rate" on the edited questions.[^c9] A second score, Generalization, asks the same preference in other forms. It is the "accuracy on four types of Generalization Evaluation Questions": the explicit question, a paraphrase, an implicit question ("Indirect queries that rely" on prior knowledge), and a product recommendation.[^c10][^c11]

The reported pattern is uneven. ROME gets high efficacy on direct injection, and "While ROME exhibits strong efficacy on direct preference injection, it fails to generalize" to rephrased, implicit and recommendation-style queries.[^c12] Prompting is the reverse of persistence. Over ten turns, "prompting-based methods degrade rapidly, falling below 20% by the 8th turn, as" the models stop recalling the preference, and "models fail to recall preferences without repeated" reminders.[^c13][^c14] The authors read the edited weights as the reason the preference holds: "the injected personalization becomes persistent and less susceptible to forgetting across turns".[^c15] The efficiency claim is that the method has "greater computational efficiency than" fine-tuning.[^c16]

## Where the formalism comes from, and what does not transfer

The tuple and the locate-then-overwrite machinery come from knowledge editing, where an object is treated as the unique answer to a subject and relation. A preference does not behave like that: the same preference can surface as a direct question, a paraphrase, an implicit cue or a shopping request. What seems to survive the transfer is the editor and the success-and-locality accounting. What does not obviously survive is the assumption that one subject phrase picks out one fact. The paper's own answer to that gap is the cluster note, [[clustered-preference-representation]]. The last part of this paragraph is my reading, not the paper's claim.

## Limits

- The benchmark, UPQA, is a short-answer set built from attributes of Synthetic Persona Chat, so the preferences are authored, not drawn from real users.[^c17]
- Scoring is "we employ string match as the primary scoring" method, with an LLM judge as a fallback, and "Another limitation is the lack of human evaluation."[^c18][^c19]
- There is no RAG baseline, and the authors name this as a limitation: "absence of a RAG baseline, which we excluded". So "editing beats prompting" is shown against prompting only, not against retrieval (see [[knowledge-injection-mechanism-comparison]] for the retrieval-versus-parametric question).
- The paper says editing is "less straightforward to deploy than in-context prompting, especially in short multi-turn conversations".[^c20]
- The efficiency comparison is run on "a 200-sample subset of UPQA".[^c21] I did not check the table values, so the size of the efficiency advantage is not established here.
- The multi-turn persistence figure appears to show two models (Olmo2-7B and Qwen3-8B), by its panel labels. That is a small sample of models.
- The objective states the locality constraint, but the parts I read report efficacy and generalization, not a score for unrelated inputs.

## Related

- [[clustered-preference-representation]] — the paper's extension of this edit: a cluster of subjects and targets per preference, for rephrased and implicit questions
- [[redundant-multilayer-knowledge-editing]] — the same rank-one limitation seen in multi-hop questions: a single-layer edit fits one depth, and copies across layers trade specificity for reach
- [[knowledge-injection-mechanism-comparison]] — parametric versus retrieval injection of knowledge, the comparison this paper leaves out
- [[implicit-subject-resolution-injection]] — another intervention on the subject of a fact that the prompt does not name

[^c1]: doi-10-48550-arxiv-2512-13676 — "Personalization Editing operates on a structure analogous to a knowledge tuple (s, r, o)"
[^c2]: doi-10-48550-arxiv-2512-13676 — "Here, the user and predicate"
[^c3]: doi-10-48550-arxiv-2512-13676 — "the editing must maintain consistency on all inputs"
[^c4]: doi-10-48550-arxiv-2512-13676 — "expensive, and prone to catastrophic forgetting,"
[^c5]: doi-10-48550-arxiv-2512-13676 — "becomes diluted in long prompts, causing the models to become increasingly unreliable"
[^c6]: doi-10-48550-arxiv-2512-13676 — "update that overrides the original model’s behavior while preserving unrelated behaviors"
[^c7]: doi-10-48550-arxiv-2512-13676 — "Rank-one model editing that localizes factual associations in MLP"
[^c8]: doi-10-48550-arxiv-2512-13676 — "first identify the most relevant layer, often a specific Feed-Forward Network layer, responsible for"
[^c9]: doi-10-48550-arxiv-2512-13676 — "is equivalent to the success rate"
[^c10]: doi-10-48550-arxiv-2512-13676 — "Scores (%) are measured by accuracy on four types of Generalization Evaluation Questions"
[^c11]: doi-10-48550-arxiv-2512-13676 — "implicit_question: Indirect queries that rely"
[^c12]: doi-10-48550-arxiv-2512-13676 — "While ROME exhibits strong efficacy on direct preference injection, it fails to generalize"
[^c13]: doi-10-48550-arxiv-2512-13676 — "prompting-based methods degrade rapidly, falling below 20% by the 8th turn, as"
[^c14]: doi-10-48550-arxiv-2512-13676 — "models fail to recall preferences without repeated"
[^c15]: doi-10-48550-arxiv-2512-13676 — "the injected personalization becomes persistent and less susceptible to forgetting across turns"
[^c16]: doi-10-48550-arxiv-2512-13676 — "Personalization Editing achieves higher editing accuracy and greater computational efficiency than"
[^c17]: doi-10-48550-arxiv-2512-13676 — "We curated UPQA by extracting user-profile features from the Synthetic Persona Chat"
[^c18]: doi-10-48550-arxiv-2512-13676 — "we employ string match as the primary scoring"
[^c19]: doi-10-48550-arxiv-2512-13676 — "Another limitation is the lack of human evaluation."
[^c20]: doi-10-48550-arxiv-2512-13676 — "straightforward to deploy than in-context prompting, especially in short multi-turn conversations"
[^c21]: doi-10-48550-arxiv-2512-13676 — "on a 200-sample subset of UPQA"
