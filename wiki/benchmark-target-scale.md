---
description: "Target size sets a benchmark's difficulty apart from novelty: a clean-room 1.1k-line program was solved by every tested model, while one large program separated them."
aliases: ["program scale in benchmarks", "toy-program benchmark problem", "realistic target size"]
sources: ["doi-10-48550-arxiv-2608-11469"]
---
# Benchmark target scale

A benchmark's targets can be new to the model and still be too small to tell capable agents apart. In reverse engineering, scale is a second requirement, separate from novelty, and one ablation measured the two apart. Eight unhardened build settings were held fixed while only the target program varied.[^c1]

The small clean-room target was easy. A compressor of about 1.1k lines, written from scratch, "is fully solved by both models in every configuration for less" than about $1.60 and seven minutes.[^c2] Novelty alone did not make it hard: the authors conclude that "being clean-room provenance by itself does not make a target hard."[^c12]

The large target separated the models. RevCompress, which "combines original code with real world" scale,[^c3] gave "GPT-5.6-sol scores 5.62 and solves 7/8 configurations, versus 3.75 and" 3/8 for GPT-5.5.[^c4] The same ablation, read in the other direction, shows that size is not the only factor: a deployed encoder of about 200 modified lines, built largely from public code, was solved in every configuration, which the authors read as recognition standing in for analysis.[^c5]

The mechanism the authors offer is drawn from prior work rather than measured here: because program understanding is the task, "the combinatorial complexity of program behaviors grows exponentially with the scale," and so "capability measured on toy programs therefore does not extrapolate."[^c6] Earlier end-to-end RE benchmarks sit at the small end, for instance one with "48 small programs, averaging only 526.2 LoC per program."[^c7] The authors state the design rule directly: "Sufficient scale is necessary to accurately measure RE capabilities."[^c8]

## Limits

- The evidence is one ablation over three programs and one compression task family, under eight configurations. It is not a curve of difficulty against size; the benchmark's 16.9k-line average is a single point (my inference).
- Scale and provenance are confounded in the hard case. RevCompress has both original code and real-world scale, so the ablation cannot say which one made it separate the models.[^c4]
- Large size is not shown to be sufficient. The authors concede that their programs "do not cover the largest real-world software systems," and they name larger programs as the next direction.[^c9]
- The benchmark is small in count: "SRE-Bench is built from 19 programs. This is a small pool" in absolute terms, so the scale claim rests on few targets.[^c10]
- The difficulty of large programs is attributed to combinatorial growth by citing earlier work; this work does not measure that mechanism.

## Related

- [[post-cutoff-corpus-benchmark-isolation]] — isolation from pretraining addresses contamination; target scale is the separate requirement that the target also be large enough to measure something
- [[hop-depth-difficulty-with-entropy-check]] — another difficulty axis, set by reasoning depth rather than by program size
- [[symbol-name-anchoring]] — the same benchmark's finding that removing symbol names changes which agents succeed

[^c1]: doi-10-48550-arxiv-2608-11469 — "with eight unhardened build configurations fixed and varying only the target"
[^c2]: doi-10-48550-arxiv-2608-11469 — "is fully solved by both models in every configuration for less"
[^c3]: doi-10-48550-arxiv-2608-11469 — "which combines original code with real world"
[^c4]: doi-10-48550-arxiv-2608-11469 — "GPT-5.6-sol scores 5.62 and solves 7/8 configurations, versus 3.75 and"
[^c5]: doi-10-48550-arxiv-2608-11469 — "a large-scale program built largely from public code can be as easy"
[^c6]: doi-10-48550-arxiv-2608-11469 — "capability measured on toy programs therefore does not extrapolate"
[^c7]: doi-10-48550-arxiv-2608-11469 — "48 small programs, averaging only 526.2 LoC per program"
[^c8]: doi-10-48550-arxiv-2608-11469 — "Sufficient scale is necessary to accurately measure RE capabilities"
[^c9]: doi-10-48550-arxiv-2608-11469 — "We therefore view larger programs as an important direction for extending SRE-Bench"
[^c10]: doi-10-48550-arxiv-2608-11469 — "SRE-Bench is built from 19 programs. This is a small pool"
[^c12]: doi-10-48550-arxiv-2608-11469 — "being clean-room provenance by itself does not make a target hard"
