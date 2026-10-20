---
description: "The span a code request asks for, from one line to a whole class, sets difficulty: in M2 G-Eval, performance consistently falls from Line to Block/Function to Class."
aliases: ["multi-granularity code generation", "structural granularity of code tasks", "granularity-dependent difficulty", "M2 G-Eval granularity levels"]
sources: ["arxiv-2512-22628"]
---
# Requested-span granularity gradient

A code request can ask for a span of different size: one line, one block, one function, or a whole class. M2 G-Eval casts every such request in one form, as "filling a masked region of code"[^c3], with the surrounding in-file and cross-file context supplied and a granularity label fixing how large the masked region is. The benchmark then holds the model and the language roughly fixed and varies only that label. Across its evaluated models the ordering is consistent: "model performance consistently drops as we move from Line to Block/Function to Class."[^c1] The abstract puts it as "Line-level tasks easiest and Class-level most challenging."[^c4]

The span also interacts with the language. Full-granularity languages do better than partial-granularity ones at every level, and the gap is "smallest at the Line level, largest at the Class level."[^c5] The authors suggest the widening gap comes from partial-granularity languages being "limited by both weaker syntactic coverage and the difficulty of generating long, structured code."[^c6]

The reason the authors give for building this is that single-span evaluation hides the variation. Existing frameworks "adopt a single-granularity evaluation paradigm,"[^c2] which "obscures important variations in model capabilities across different code scopes."[^c7] The claim is that one span size yields one number for an ability that differs by span. For someone asking code questions, the size of what is requested is a difficulty variable of its own, separate from how hard the topic is. My inference, not the paper's: a request for a whole class asks the model to keep more structure consistent at once, so the same model can look capable at line level and weak at class level without any change in its knowledge of the language.

## Limits

- The gradient is the paper's own measurement on its own benchmark. The authors call the hierarchy "an apparent difficulty hierarchy,"[^c4] and the paper does not establish it as a property of code tasks in general.
- Span size is confounded with the scaffolding each level receives. The prompt template gives a skeleton only for function and class tasks: "Skeleon: Given when Function/Class level."[^c8] So the drop may reflect the extra structure supplied or the missing skeleton at line and block level, not span size alone. The work does not separate these. My inference.
- The result is an average over many models and 18 languages. The slices read do not show per-model orderings, so an individual model may not follow the aggregate pattern.
- Only code is tested. Whether the same ordering holds for prose requests, for example a one-sentence answer against a whole essay, is not shown here.
- The mechanism is not measured in the parts read. The authors suggest the cross-language gap reflects weaker syntactic coverage and the difficulty of long structured code,[^c6] but nothing read tests which features of a class task make it hard.

## Related

- [[evidence-scope-gradient]] — the same kind of gradient on the input side: there the scope of evidence a question must draw on, here the scope of output a request asks for.
- [[benchmark-target-scale]] — target program size separates models in reverse engineering; this note concerns the size of the requested output, a different axis.
- [[hierarchical-retrieval-interfaces]] — granularity chosen per step by a retrieval agent, where this note treats granularity as a fixed variable that sets difficulty.

[^c1]: arxiv-2512-22628 — "model performance consistently drops as we move from Line to Block/Function to Class"
[^c2]: arxiv-2512-22628 — "adopt a single-granularity evaluation paradigm"
[^c3]: arxiv-2512-22628 — "filling a masked region of code"
[^c4]: arxiv-2512-22628 — "an apparent difficulty hierarchy"
[^c5]: arxiv-2512-22628 — "smallest at the Line level, largest at the Class level"
[^c6]: arxiv-2512-22628 — "limited by both weaker syntactic coverage"
[^c7]: arxiv-2512-22628 — "in model capabilities across different code scopes"
[^c8]: arxiv-2512-22628 — "Skeleon: Given when Function/Class level"
