---
description: "A 10-signal, 4-domain taxonomy — who wrote it, who published it, how it was vetted, how AI finds it — for scoring a cited source's authority."
aliases: ["Authority Signals Framework"]
sources: ["arxiv-2605-23921"]
---
# Authority Signals Framework

> A source's authority is not one number — it is who wrote it, who published it, how it was checked, and how findable it is, scored separately.

## Definition / Mechanism

The framework operationalizes "is this a credible source to cite" as
ten measurable signals grouped into four domains, each domain a
different question a reader — human or AI — could ask of a cited page
before trusting it:

1. **Who wrote it? (Author Credentials)** — one signal: author
   attribution level, coded 0 = none, 1 = name only, 2 = name with
   credentials.
2. **Who published it? (Institutional Affiliation)** — one signal:
   organization type, classified into seven categories (Medical
   Institution, Government Resource, Commercial Health Information,
   Professional Association & Advocacy, Encyclopedia/Reference,
   Peer-Reviewed Journal, News/Media).
3. **How was it vetted? (Quality Assurance)** — three signals:
   references cited (yes/no), medical review statement visible
   (yes/no), content recency (0 = before 2020 or not listed, 1 =
   2020–2023, 2 = 2024–2026).
4. **How does AI find it? (Digital Authority)** — five signals: page
   authority and domain authority (0–100, via Moz API), spam score
   (0–100), content length (0 = brief <500 words, 1 = moderate
   500–1,500, 2 = comprehensive >1,500), and schema markup (0 = none,
   1 = microdata, 2 = JSON-LD). "Understanding which sources AI systems
   prioritize requires asking four critical questions: 1. Who wrote
   it? (Author Credentials) 2. Who published it? (Institutional
   Affiliation) 3. How was it vetted? (Quality Assurance) 4. How does
   AI find it? (Digital Authority)"[^c1]

The framework does not collapse these into one score; it reports each
domain's signals separately and lets the pattern across an
organization type stand as the description, e.g. an institution can
score 0 on author credentials and quality assurance yet still be the
most-cited type in a corpus (see [[institutional-authority-halo]]).

## Why it matters

For `c4` — where a constraint's source comes from — this is a ready
operational checklist for auditing *what* a routing or citation
mechanism is actually keying on when it treats one source as more
authoritative than another, applicable to any system (an AI answerer,
a search ranker, a human reader) that must decide which source to
trust without checking the claim itself. It was built to run on scraped
HTML and public APIs (Moz), so it can be applied to a source corpus
before, or instead of, checking the correctness of what was cited. "It
does not ask whether Claude's citations are correct. It asks what
authority signals describe the sources Claude chooses in the first
place."[^c2]

## Limits

Domain-specific in its current form: the organization-type taxonomy
(Medical Institution, Government Resource, …) and the deployment
(health citations) are health-domain constructs; the four questions
generalize but the seven-category coding scheme would need
re-derivation for another domain. The framework measures signals
*present in* a cited source, not whether those signals caused the
source to be cited, nor whether the source's content is accurate —
"Whether those signals are what resulted in commercial health sources
being cited, or whether they are simply an association present among
those selected, is something this study does not settle."[^c3]
Three of the ten signals (page authority, domain authority, spam
score) depend on a third-party API (Moz) whose scoring method is not
under the framework's control.

## Related

- [[institutional-authority-halo]] — the pattern this framework's own
  application surfaces: institutional sources pass without the
  quality-assurance signals commercial sources need.
- [[typed-source-abstraction]] — models a source's type for routing;
  this framework instead scores a source's authority once chosen.
- [[novice-expert-problem]] — the asker's problem of judging a source
  without judging its content, which this framework operationalizes
  for one domain.
- [[scope-limitation]] — another framework keying a response to where
  it fell short, by origin rather than by authority signal.

[^c1]: arxiv-2605-23921 — "Understanding which sources AI systems prioritize requires asking four critical questions: 1. Who wrote it? (Author Credentials) 2. Who published it? (Institutional Affiliation) 3. How was it vetted? (Quality Assurance) 4. How does AI find it? (Digital Authority)"
[^c2]: arxiv-2605-23921 — "It does not ask whether Claude's citations are correct. It asks what authority signals describe the sources Claude chooses in the first place."
[^c3]: arxiv-2605-23921
