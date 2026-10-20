---
description: "LLMs detect a causal flaw (77-91%) yet roughly half the time still endorse the claim; Dissonance Rate counts detected errors left uncorrected in the final answer."
aliases: ["dissonance rate", "detection is not correction", "uncorrected self-awareness"]
sources: ["arxiv-2602-08939", "arxiv-2604-13068", "doi-10-48550-arxiv-2609-38409", "doi-10-48550-arxiv-2608-14905"]
---
# Detection-Correction Gap

A model may correctly state that confounding or selection bias is present and still conclude that the causal claim is likely true. CausalT5k calls this the Detection-Correction Gap, and its Dissonance Rate "measures detected errors that remain uncorrected in the answer."[^c1] The metric needs trap labels plus the model's free-text justification, so that the diagnosis and the verdict can be compared.

Measured on the CausalL2 subset across five models: "All five models detect traps at 77–91%, yet roughly half of all cases fall into dissonance: the model names the flaw but fails to align its final answer with that diagnosis."[^c2] The authors read this as a systematic gap between declarative causal knowledge and procedural causal control across model families.[^c2]

The gap also appears inside the activations. Across seven models (117M to 7B; GPT-2, Pythia, Qwen-2.5), linear probes detect hallucination above chance in larger models, yet steering along the probe-derived direction gave "0% correction rate across all seven models", so the detected signal "is not a causal control point in hallucination generation under this intervention class."[^c3] Output-confidence baselines also beat the probes on detection AUC at every model above 410M parameters, so the probe's distinct value is temporal: it is readable "at position zero (before any output tokens are produced)".[^c4]

For answering well, the consequence is that a correct diagnosis in the text is not evidence that the answer acted on it; the check has to compare the two. It is what the "refuse" step of [[wise-refusal]] enforces.

A second instance of the same split comes from formal argumentation, outside causal inference. ArgGYM separates evaluating a formal state from producing an intervention that reaches one: "A model may be strong at evaluating a formal state while still being unreliable at constructive search over that formal system."[^c5] Its matched counter-argument conditions show the gap is not closed by offering a cheaper route: the paper observes that "Constructive success therefore depends not only on whether an effective intervention exists, but also on whether a model recognizes and exploits the available intervention affordances."[^c6] Recognising the state and acting on it are again separate capacities.

The same split appears in an audit of autonomous research agents. Across 800 end-to-end research trajectories, the most frequent failure pattern is "uncorrected self-awareness": the agent finds a critical flaw during its own self-review and then reports the conclusion unchanged.[^c7] The authors read the diagnosis as correct and the outcome as unchanged: "The judgment was correct and nothing followed from it."[^c8] Here the check on the answer is whether the report acted on a diagnosis the run had already written down.

## Limits

Evidence is one subset (CausalL2, a targeted set built to stress trap-level diagnosis) and five models of an older generation; the paper says such subsets do not estimate full-benchmark averages. Detection is judged from free text, so judge noise is possible. Why the gap arises is not established here. The probe-steering result covers one intervention class (steering along a probe direction), models up to 7B, and position-zero significance in only two of seven models; a different intervention might still correct. The research-agent case is a looser second instance: its counts come from an LLM agent-as-a-judge, and the authors report no per-pattern agreement for it.[^c9]

## Related

- [[wise-refusal]] — the criterion that closes the gap by requiring refusal after diagnosis
- [[recognition-refusal-dissociation]] — an internal-representation analogue of recognizing without acting
- [[reasoning-masked-sycophancy]] — another case where visible reasoning and the final answer part ways
- [[skepticism-trap]] — companion two-axis diagnostic from the same benchmark
- [[grounded-argument-acceptance]] — the formal-argumentation setting where the second instance above was measured
- [[local-correctness-without-global-composition]] — correct local verdicts that do not add up to a correct whole answer

[^c1]: arxiv-2602-08939 — "measures detected errors that remain uncorrected in the answer."
[^c2]: arxiv-2602-08939 — "yet roughly half of"
[^c3]: arxiv-2604-13068 — "activation steering along probe-derived hallucination directions yields 0% correction rate across all"
[^c4]: arxiv-2604-13068 — "probe signals are accessible at position zero (before any output tokens are produced)"
[^c5]: doi-10-48550-arxiv-2609-38409 — "A model may be strong at evaluating a formal state while still being unreliable at constructive search over that formal system"
[^c6]: doi-10-48550-arxiv-2609-38409 — "Constructive success therefore depends not only on whether an effective intervention exists, but also on whether a model recognizes"
[^c7]: doi-10-48550-arxiv-2608-14905 — "Uncorrected self-awareness (F.4) is the single most frequent pattern in the corpus"
[^c8]: doi-10-48550-arxiv-2608-14905 — "The judgment was correct and nothing followed from it."
[^c9]: doi-10-48550-arxiv-2608-14905 — "we do not report per-pattern or per-pillar agreement at this time"
