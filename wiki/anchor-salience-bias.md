---
description: "A question generator's choice of which document span to ask about is driven by local surface presentation, not only content, and this bias is exploitable by formatting and inserted artifacts."
aliases: ["anchor-salience bias"]
sources: ["alimaskina-2026"]
---
# Anchor-salience bias

> The region of a document a question-generating model chooses to ask about — its "anchor" — is not chosen from semantic content alone: headings, markup, tables and other surface cues pull it there, and an attacker or a messy document can exploit that pull.

## Definition / Mechanism
Alimaskina et al. (2026) call the source region a generator implicitly focuses on when writing an interaction its **anchor**: "When generating an interaction from a chunk, the model implicitly chooses a source region to focus on; we call this selected region an anchor." Measuring which surface features (section markers, headings, lists, tables, key-value fields, dates, dense numerical passages, citations, markup artifacts) co-occur with chosen anchors, they find that "Anchor selection is shaped not only by semantic content, but also by local presentation... the same content may become more question-worthy when it is visually or syntactically marked in the chunk."[^c1]

## Why it matters
This bias is directly manipulable. A formatting-only perturbation — prepending the banner "MOST IMPORTANT PASSAGE IN THIS EXCERPT" to an otherwise-unchanged low-salience paragraph — "increases the target hit rate from 25.2% to 36.3% (+11.0 pp), showing that local marking can redirect questions even when the paragraph content is unchanged."[^c2]

Combined with overlapping chunk sampling, the same mechanism lets a fixed, non-substantive artifact hijack generation at scale: inserting one parser-residue-like template repeatedly across a document, "Hit rates reach 77–94% on Cartridges, 55–85% on LongHealth, and 56–88% on QASPER for several seeds and generators," and exposure compounds with insertion count — "with 30 insertions, more than half of all sampled chunks already contain at least half of an inserted span in every corpus; with 50 insertions, exposure reaches 75.4–82.7%."[^c3]

For any question-selection rule that leans on a generator's own sense of salience (rather than a fixed, externally-specified target), this is a demonstrated channel by which presentation — not evidentiary value — decides what gets asked.

## Limits
The hijacking numbers depend on the specific inserted artifact (a fixed HTML-like, markup-heavy template), the chunk sampler used, and the six tested generator models (Qwen3-1.7B/4B/32B, Gemma3-12B/27B-IT, Llama3.1-8B-Instruct); a different artifact shape or sampler could shift the rate. The paper is a 2026 arXiv preprint, not yet peer reviewed.

## Related
[[question-generation-as-policy]] · [[expected-information-gain]] · [[surprisal]]

[^c1]: alimaskina-2026 — "When generating an interaction from a chunk, the model implicitly chooses a source region to focus on; we call this selected region an anchor."
[^c2]: alimaskina-2026 — "The banner increases the target hit rate from 25.2% to 36.3% (+11.0 pp), showing that local marking can redirect questions even when the paragraph content is unchanged."
[^c3]: alimaskina-2026
