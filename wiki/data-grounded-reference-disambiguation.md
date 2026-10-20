---
description: "Before generation, a vague dataset reference in a prompt is replaced by the exact path matched from the data file's own structure; executable scripts rise while correct outputs barely move."
aliases: ["data-aware prompt disambiguation", "structure-grounded prompt disambiguation", "automated reference resolution against a data file"]
sources: ["arxiv-2511-21920"]
---
# Data-grounded reference disambiguation

A prompt that names a variable loosely ("the temperature data") leaves the generating model to guess where that variable sits in the file. The method closes the guess from the data's side rather than the user's. The system parses the HDF5 file to enumerate its dataset paths and attributes, splits the prompt into monograms and bigrams, and matches those tokens against the paths.[^c1] Matching runs in stages: exact and partial string matches first, then fuzzy Levenshtein matching. "Two thresholds are used: a strict threshold (87%) followed by a relaxed threshold (80%)" to tolerate variation.[^c1] The matched paths and attributes are then appended to the prompt "in a concise and non-intrusive format."[^c2] The user's wording stays; the file's structure is added to it, and nobody is asked a question.

The mechanism moves the resolution of a referent from a question to a lookup over a source the answerer can read. The authors state it is "model-agnostic and requires no changes to the LLM architecture."[^c3]

## What was measured

The comparison uses simple prompts and five open-source models, each run with and without the step. The authors report that grounding the references "made the generated code more robust to prompt underspecification."[^c4] The gain appears in how many scripts run at all. For output that is correct, it is small: "while script executability improved, the proportion of outputs that produced correct analytical or visualization results showed only marginal gains."[^c5] The authors' explanation is that the step "does not improve the specification of the" analytical task itself.[^c6]

The baseline failure is the motivation. Ambiguous prompts "often result in code that is incorrect, incomplete" on the authors' account.[^c7] The step targets the part of that failure that is about where data lives.

## Limits

- The prompts are synthetic. The simple prompts were produced by summarising detailed ones with an LLM, not by non-experts: the authors "used Llama3-70B to summarize the detailed versions into" shorter queries.[^c8]
- The matching thresholds (87% and 80%) are given as the authors' choice. The text read reports no sweep over them, so how sensitive the matches are is not shown.
- The executability gain is not evidence that the analysis is right. The paper's own figures show correctness nearly unchanged, so a script that now runs may still answer the wrong question.
- The method only helps where the prompt's referent is a name the file carries. Where no token matches any path, the step has nothing to append; the paper does not test that case. (My inference from the matching procedure.)
- The paper contrasts this with interactive clarification, saying such approaches "often rely on user interaction."[^c9] It does not compare the two empirically, so whether a lookup can stand in for a question is not shown here. The bound on evidence gathered without asking is treated in [[automated-clarification-proxy-bound]]; the present work does not test that bound.

## Related

- [[structural-versus-semantic-underspecification]] — the split between where a referent lives and what analysis is meant; this method reaches only the first
- [[ambiguity-driven-execution-probing]] — also resolves ambiguity without asking, but by executing probes against the database instead of matching paths in a file
- [[automated-clarification-proxy-bound]] — the ceiling on what evidence gathered without asking can recover about intent
- [[referent-match-set-ambiguity]] — types a referent by how many candidates match it; an empty match set is the case this step cannot resolve

[^c1]: arxiv-2511-21920 — "Two thresholds are used: a strict threshold (87%) followed by a relaxed threshold (80%)"
[^c2]: arxiv-2511-21920 — "in a concise and non-intrusive format"
[^c3]: arxiv-2511-21920 — "This method is model-agnostic and requires no changes"
[^c4]: arxiv-2511-21920 — "made the generated code more robust to prompt underspecification"
[^c5]: arxiv-2511-21920 — "while script executability improved, the proportion of outputs that produced correct analytical or visualization results showed only marginal gains"
[^c6]: arxiv-2511-21920 — "does not improve the specification of the"
[^c7]: arxiv-2511-21920 — "often result in code that is incorrect, incomplete"
[^c8]: arxiv-2511-21920 — "used Llama3-70B to summarize the detailed versions into"
[^c9]: arxiv-2511-21920 — "such approaches often rely on user interaction"
