---
description: "An LLM judges academic papers' abstracts and conclusions as making stronger claims than their discussion sections in most fields, so an answerer fed only the abstract inherits inflated confidence."
aliases: []
sources: ["arxiv-2605-27392"]
---
# Section hedging asymmetry

> A paper's abstract is not a compressed report of its own uncertainty.

## Definition / Mechanism

Thelwall (2026) has GPT-OSS 120B first name a paper's
main result from its full text, then separately rate, on a 1–10 scale, how
strongly that same result is claimed in the abstract, the discussion, and
the conclusion — run over several thousand articles each from eight MDPI
journals spanning humanities to formal sciences. Outside Humanities and
Social Science, the three ratings are not interchangeable: the discussion
section is judged the weakest-claiming section in nearly every journal,
while the strongest claim sits in the abstract or the conclusion.[^c1]

The asymmetry attaches to *where* in the paper a claim is read, not to the
claim's underlying evidence — the same identified "main result" is scored
three times and the score moves with the section. Because the abstract and
conclusion are exactly the sections an LLM without full-text access is
likely to ingest, the paper draws the transfer risk directly: an answerer
that summarises from abstracts alone reproduces the paper's most confident
phrasing of its finding and never sees the section where the authors stated
its actual evidential weight.[^c2]

## Why it matters

This is a source-mediation failure for commitment distinct from
miscalibration inside the answerer: the answerer's own uncertainty
machinery can be working correctly and it will still overclaim, because the
text handed to it is already confidence-inflated by which section of the
source document was retrieved. A retrieval or summarisation pipeline that
indexes abstracts — for cost, for copyright, or because that is all a
search API returns — has no internal signal that would expose this: the
abstract is fluently and locally well-hedged, just more confident than the
paper's own discussion of its result. The fix is not better confidence
elicitation from the answerer but a different choice of *which text*
constrains the answerer's expressed certainty.

## Limits

- One LLM (GPT-OSS 120B) judging strength on a bespoke 1–10 scale, with no
  human-rated ground truth for comparison; the paper states its results
  "may be different for other LLMs and journals."[^c3]
- Eight MDPI journals from a single publisher, English-language only, and
  MDPI's journals are topic- rather than field-focused, which weakens
  field-level generalisation.
- Humanities and Social Science show no asymmetry — the effect measured is
  field-dependent, not universal, and the paper flags the Humanities result
  itself as possibly an artefact of its small qualifying sample (193
  articles).
- The "main result" is identified once per article by the same LLM before
  all three ratings; an error in that identification step would propagate
  to every rating and is not independently checked. unverified.

## Related

[[hedged-mirage]] · [[calibration-training]] · [[expression-format-overconfidence-gap]] · [[abstention]]

[^c1]: arxiv-2605-27392 — "discussion in the main result is the lowest."
[^c2]: arxiv-2605-27392 — "cannot access full texts, then they may express the results with too much certainty."
[^c3]: arxiv-2605-27392 — "This study is limited to a single LLM, a small set of journals, and a single publisher."
