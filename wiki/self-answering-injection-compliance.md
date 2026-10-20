---
description: "The model that answers a self-generated question tends to obey instruction-like passages embedded in the source text, so a self-generated \"answer\" can be an attacker's constraint, not the document's."
aliases: ["injection compliance"]
sources: ["alimaskina-2026"]
---
# Self-answering injection compliance

> In a self-study QA pipeline the same untrusted chunk that supplies the question also supplies the answer; when that chunk contains an instruction-like passage, the answering model tends to obey it rather than merely report it — so the resulting "constraint" can come from the passage's author, not from the document's content.

## Definition / Mechanism
Alimaskina et al. (2026): "When answering, the model that produces the supervision tends to obey instruction-like passages embedded in the text. This compliance depends on the intent and surface form of the passage rather than its strictness, and is worst under task conflict, where larger models comply more often."[^c1]

## Why it matters
Because the answer becomes the training signal distilled into a downstream model or artifact, an answering-stage compliance failure does not stay local: it propagates as if it were a genuine constraint extracted from the document. The authors show it is reducible without changing the training loop: "filtering instruction-like spans before answering lowers mean injection compliance from 88% to 13% in our evaluation while retaining nearly all clean text."[^c2]

For a stall-5 question — is what came back actually a constraint from the source, or from something else entirely — this is a measured case where the answer's provenance is confounded: an untrusted passage can substitute its own instruction for the document's content, and ordinary fluency or format-following gives no signal that this happened.

## Limits
The 88%→13% figure is for one keyword–regex filtering defense against the paper's own tested instruction-like passages, on the same corpora and generator models used elsewhere in the study; it is not a general compliance rate for instruction injection in QA pipelines, and the mechanism behind why larger models comply more under task conflict is reported as an observation, not explained. The source is a 2026 arXiv preprint, not yet peer reviewed.

## Related
[[question-generation-as-policy]] · [[constraint-as-information]] · [[data-processing-inequality]]

[^c1]: alimaskina-2026 — "When answering, the model that produces the supervision tends to obey instruction-like passages embedded in the text. This compliance depends on the intent and surface form of the passage rather than its strictness, and is worst under task conflict, where larger models comply more often."
[^c2]: alimaskina-2026 — "filtering instruction-like spans before answering lowers mean injection compliance from 88% to 13% in our evaluation while retaining nearly all clean text."
