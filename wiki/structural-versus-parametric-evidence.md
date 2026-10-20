---
description: "Deterministic operators over a document's structure lift LLM accuracy on questions whose answer is a structural fact, and add little where the answer needs knowledge the document lacks."
aliases: ["structural versus parametric evidence", "tool gain by evidence type", "structure-grounded versus knowledge-grounded answers"]
sources: ["arxiv-2601-11556", "arxiv-2512-05430"]
---
# Structural versus parametric evidence

A tool helps a language model answer a question only when the fact the answer rests on can be read off the object the tool operates on. In CSyMR-Bench that object is a symbolic music score, and the framework treats it as a structured document. Each analysis is an operator that returns a value from the notation. The authors describe the evidence unit as a specific musical feature "deterministically inferred from the raw notation", not a span that sits in the text.[^c1] The question type is set against standard retrieval: "Unlike standard text retrieval where answers often exist as explicit spans", the answer must be extracted from the structure and combined with other extractions.[^c2]

The measured result splits by category, not by overall difficulty. Tool augmentation "yields distinct gains on" the analysis-heavy categories, with "the largest improvements on analysis-heavy categories" reported in the abstract.[^c3][^c4] Against that, "improvements are negligible for" the metadata-driven categories, where the example is "metadata-driven categories (e.g., Genre Judgment)".[^c5] The authors' explanation is the boundary itself. The toolset is built "for explicit structural retrieval, which cannot" replace the knowledge the genre task needs, because that task requires "fully substitute for the implicit parametric knowledge required for" stylistic classification.[^c6]

The variable, then, is where the evidence lives, not how hard the question looks. Two kinds can be told apart here. Structural evidence is in the object: the windowed key-estimation operator the case study calls on, or a roman-numeral label, is a fact about the notation, and an operator can return it. Parametric evidence is in the reasoner: the conventions of a genre, what a waltz sounds like, the judgement of a practising musician. No operator over the notation holds that, so the model's own knowledge is the only source and the tool adds nothing. The case study shows the failure that follows when a structural question is answered from memory. The chain-of-thought baseline produces a plausible rationale that ends "fabricating non-existent pitches", while the tool path reads the key from the score and derives the function from it.[^c7][^c8]

For someone asking or answering, the consequence is a test before reaching for a tool. Ask whether the needed fact is a property of the given object that some operator can compute. If it is, the question is a candidate for grounding. If the fact is a convention or a judgement held outside the object, a tool run over the object will not supply it, and the answer stays exposed to the model's recall. The distinction is mine, drawn from the paper's category split; the paper does not name it or test it as a rule.

## Limits

The split is observed across categories, on a small set. Figure 1 labels three categories with 16, 14 and 16 items out of 126; reading those labels, a category gain of a few points is a handful of questions. The slices read report no significance test, so the sizes of the gains are not established beyond the paper's table.

Every method runs on one backbone: the prompting baselines and agent controllers "are implemented with GPT-4.1-mini as the backbone model".[^c9] Whether the split holds for other backbones is not tested in the text read.

The multiple-choice format is partly model-made: "plausible distractor options were synthesized using" GPT-4o-mini.[^c10] A question whose distractors were written to resemble the correct answer may favour a reasoner that checks the score against each option, and that is a property of the benchmark as much as of the tools.

The boundary is drawn in one domain. Nothing here shows that another structured object, a table or a program, separates structural from parametric evidence in the same way, or that a structural fact with no operator behind it would be recognised as one. The word "structural" is the paper's label for what its toolset reads, and it should not be read as a general criterion.

## Related

- [[tool-integrated-reasoning]] — the same loop of handing work to a tool, here applied to retrieval over a score; that note is about where computation runs, this one about which evidence a tool can supply at all.
- [[aggregation-extraction-gap]] — composing several extractions over one document is harder than a single extraction; CSyMR does not measure that gap, but its questions have the same composed shape inside one score.
- [[retrieval-gain-by-question-type]] — the same boundary for text retrieval: a fact the model lacks gains from a passage index, a reasoning step over text already given gains little. ArtistMus measures the split; it does not test a structured object, and the link between the two is my reading.

[^c1]: arxiv-2601-11556 — "deterministically inferred from the raw notation"
[^c2]: arxiv-2601-11556 — "Unlike standard text retrieval where answers often exist as explicit spans"
[^c3]: arxiv-2601-11556 — "tool augmentation yields distinct gains on"
[^c4]: arxiv-2601-11556 — "with the largest improvements on analysis-heavy categories"
[^c5]: arxiv-2601-11556 — "metadata-driven categories (e.g., Genre Judgment)"
[^c6]: arxiv-2601-11556 — "fully substitute for the implicit parametric knowledge required for"
[^c7]: arxiv-2601-11556 — "invokes a windowed key-estimation operator"
[^c8]: arxiv-2601-11556 — "fabricating non-existent pitches"
[^c9]: arxiv-2601-11556 — "are implemented with GPT-4.1-mini as the backbone model"
[^c10]: arxiv-2601-11556 — "plausible distractor options were synthesized using"
