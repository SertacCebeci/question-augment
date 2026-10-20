---
description: "Uncited claims in a long report can be checked by inheriting the citations of the earlier sentences they depend on, so citation checking reaches claims that carry no marker."
aliases: ["back-tracking", "semantic back-tracking", "implicit-citation recovery", "citation inheritance", "implicit claim back-tracking"]
sources: ["arxiv-2512-17776"]
---
# Citation back-tracking

A long report makes many claims whose support was cited once, earlier, and then assumed. Citation checking reads only the marker on the sentence itself, so a claim with no marker is never tested, even when its source is one sentence back. The paper's premise is that "expert reports often contain implicit claims whose supporting citations appear in earlier sentences".[^c1] Its point is that such a claim is still checkable: "relying solely on citation markers may miss claims" that can be verified against external sources.[^c2]

The mechanism is a dependency pass. For a sentence, a model identifies the earlier sentences it semantically depends on, and "mechanism that recovers the citation set needed for verification" is the sentence's own citations plus the citations of those earlier sentences.[^c3] The verifier then runs against that set, so the sentence inherits the source of the sentence it leans on. "This enables verification by inheriting citations from previously referenced sentences" in the paper's words.[^c4]

Claims are typed before any retrieval. The paper sorts claims into six types, "we classify extracted claims into six types (A–F)", and applies external verification only to the verifiable ones: inline-cited claims (A), uncited claims whose support is elsewhere in the report (B and C), while the rest are "structural, internal, or otherwise non-verifiable".[^c5][^c6] The worked case is a sentence typed B: "L1.S2 (Type B) has no explicit citation but inherits [1] from L1.S1 through back-tracking".[^c7] A sentence with no recoverable source is type F, and it is not sent to external verification.

The inherited citation is a candidate, not a verdict. A claim counts as supported "only when the subsequent verification stage confirms that the candidate evidence actually supports it".[^c8] The paper says the pipeline tolerates wrong dependency guesses "because inherited citations serve only as candidate evidence".[^c9] The paper states that existing checkers do the opposite: they "verify only explicitly cited sentences, excluding claims without citation markers from verification".[^c10] The mechanism was validated, the paper says, against expert-annotated dependencies: "We empirically validate this mechanism against expert-annotated" dependencies in its §6.5 and appendix.[^c11]

## Limits

- The gain is in coverage of what is checked, not in the verdict on each claim. The verification stage that decides support is a separate step and is not improved by back-tracking.
- A wrong dependency sends the verifier to the wrong source. The paper's tolerance claim covers this only in the sense that the inherited citation is a candidate. My inference: a true claim whose real support lies elsewhere can come out "not supported" through a bad dependency.
- The accuracy of the dependency step is in a table outside the slices read here. This note reports the validation claim, not its figures.
- The sections read contain no run of back-tracking against explicit-citation-only checking on the same reports. The coverage gain rests on the design argument in those sections.
- The claims tested are in deep research reports across "50 report-generation tasks spanning"[^c12] domains. Whether the same dependency pass works on answers without an earlier sentence to lean on is not shown. A claim with no earlier source is type F and is simply not checked.

## Related

- [[claim-decomposed-retrieval-check]] — splits an answer into claims and checks each by web search; back-tracking decides which uncited claims get a source to be checked against, before any search runs.
- [[expert-evaluation-guidance]] — the rubric side of the same benchmark, which judges the report as a whole rather than claim by claim.
- [[expert-report-derived-atomic-rubrics]] — another way to grade long reports, by atomic rubrics taken from an expert article rather than by claim sources.

[^c1]: arxiv-2512-17776 — "expert reports often contain implicit claims whose supporting citations appear in earlier sentences"
[^c2]: arxiv-2512-17776 — "relying solely on citation markers may miss claims"
[^c3]: arxiv-2512-17776 — "mechanism that recovers the citation set needed for verification"
[^c4]: arxiv-2512-17776 — "This enables verification by inheriting citations from previously"
[^c5]: arxiv-2512-17776 — "we classify extracted claims into six types (A–F)"
[^c6]: arxiv-2512-17776 — "structural, internal, or otherwise non-verifiable"
[^c7]: arxiv-2512-17776 — "L1.S2 (Type B) has no explicit citation but inherits [1] from L1.S1 through back-tracking"
[^c8]: arxiv-2512-17776 — "verification stage confirms that the candidate evidence actually supports it"
[^c9]: arxiv-2512-17776 — "because inherited citations serve only as candidate evidence"
[^c10]: arxiv-2512-17776 — "checkers typically verify only explicitly cited sentences, excluding claims without citation markers from verification"
[^c11]: arxiv-2512-17776 — "We empirically validate this mechanism against expert-annotated"
[^c12]: arxiv-2512-17776 — "through 50 report-generation tasks spanning"
