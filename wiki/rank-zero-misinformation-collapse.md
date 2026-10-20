---
description: "One plausible false article placed at search rank 0 collapses frontier agents' accuracy while tool use stays flat and confidence stays high, though truthful evidence is fully available."
aliases: ["adversarial search ranking vulnerability", "honeypot rank injection", "positional anchoring on top-ranked source"]
sources: ["arxiv-2603-00801"]
---
# Rank-zero misinformation collapse

The Synthetic Web benchmark builds procedurally generated mini-internets of thousands of hyperlinked articles with ground-truth credibility and fact labels. Questions are filtered so a strong model cannot answer them closed-book: any item GPT-5 answers correctly in at least 2 of 4 trials is removed.[^c1] The only intervention is a post-retrieval rank override: in adversarial mode one honeypot article, a plausible falsehood written for the query's topic, is injected at rank 0 of the first search response. Content is otherwise held constant, so the effect is causal.[^c2]

## What was measured

Accuracy collapses. GPT-5 falls from 65.1% to 18.2%, o3 from 48.4% to 16.7%, o1 from 39.0% to 8.4%, and GPT-4o from 27.2% to 3.8%.[^c3] The honeypot does not suppress other evidence; it is only presented first, and agents had no tool budget limit.[^c4]

Three behavioral signatures accompany the collapse:

- Flat search effort. GPT-5 averages 6.45 tool calls in the standard condition and 6.61 in the adversarial one, so a conflict does not trigger more searching.[^c5]
- Synthesis failure, not volume failure. Some failures come after 1–2 calls (premature commitment), others after very many (162 calls on one timeline question without correct ordering).[^c6] A rarer variant, "epistemic paralysis", acknowledges uncertainty yet declines to answer despite sufficient articles.[^c7]
- Miscalibration. Stated confidence stays high on wrong answers, and ECE and Brier score worsen under attack.[^c8]

Solvability check: humans using the same retriever scored 98% standard and 93% adversarial, which the authors read as showing that ordinary source criticism suffices.[^c9] The cues available are redundancy of true claims across independent articles versus single-source honeypot claims, fabricated uncorroborated citations, and provenance structure.[^c10]

## Hypothesis, not finding

The authors explicitly separate this: positional anchoring (treating rank as evidential strength) is proposed as the unifying mechanism, linked to "lost in the middle" effects, but attention was not measured and rank-position ablations were not run.[^c11] The measured facts are the four listed behaviors; the mechanism is conjecture.

## Implication for asking and answering (my inference)

An answerer that issues the first query and trusts the top result has no step that asks "does a second independent source agree?". The failure is one of not asking the corroboration question, not one of lacking evidence. This inference is mine; the paper only tests unmitigated agents.

## Limits

- Synthetic, LLM-generated (GPT-5) worlds; the authors call this complementary to, not a replacement for, real-web evaluation.[^c12]
- The human baseline is small and drawn from a single world.[^c13]
- No mitigation (corroboration prompts, calibration training, abstention rewards) was tested; they are listed as future directions.
- The same model family (GPT-5) generates the worlds and the contamination filter, which may shape which items survive.
- Only one injection position (rank 0) and one honeypot per query were tested, so how effect size varies with rank is unknown.

## Related

- [[parametric-knowledge-gates-retrieval-noise-damage]] — another account of when retrieved noise overrides what a model would otherwise answer
- [[benchmark-contamination-convergent-audit]] — contamination filtering, here done by closed-book probing
- [[over-reliance-discrimination-failure]] — reliance on a wrong source without discriminating its reliability
- [[uncertainty-band-corroboration-gate]] — corroboration as a gate, the step these agents skip

[^c1]: arxiv-2603-00801 — "remove any item the model answers correctly in ≥ 2 of 4 trials"
[^c2]: arxiv-2603-00801 — "our causal intervention is a post-retrieval rank override of one transient result"
[^c3]: arxiv-2603-00801 — "GPT-5 falls from 65.1% to 18.2% accuracy (−46.9 points), o3 from 48.4% to 16.7% (−31.7 points), o1 from 39.0% to"
[^c4]: arxiv-2603-00801 — "Models have full access to the rest of the search index, can issue multiple"
[^c5]: arxiv-2603-00801 — "(e.g., GPT-5: 6.45 calls) and adversarial (6.61 calls) conditions"
[^c6]: arxiv-2603-00801 — "The bottleneck is"
[^c7]: arxiv-2603-00801 — "models acknowledge uncertainty but still fail to act on available evidence as an example of epistemic paralysis"
[^c8]: arxiv-2603-00801 — "Calibration metrics (ECE, Brier score) degrade markedly in adversarial"
[^c9]: arxiv-2603-00801 — "Humans achieved 98% accuracy in the standard condition and 93% in the adversarial condition,"
[^c10]: arxiv-2603-00801 — "honeypot claims typically appear in a single source"
[^c11]: arxiv-2603-00801 — "but we caution that we have not"
[^c12]: arxiv-2603-00801 — "The synthetic setting is complementary"
[^c13]: arxiv-2603-00801 — "The human baseline used a small sample from a single world"
