---
description: "VC-dimension is the largest point set a hypothesis class can shatter; Popper's dimension is one below the smallest set it cannot shatter, so the two diverge and capacity is not parameter count."
aliases: ["Popper dimension of a theory", "VC-dimension as degree of falsifiability", "shattering capacity"]
sources: ["corfield-2009"]
---
# VC-dimension versus Popper's dimension of a theory

Two measures of how much a class of hypotheses can be tested by data look alike and are not the same. A class that can fit any labelling of the data cannot be refuted by that data, and a question or answer built on such a class has said little.

## Mechanism

The VC-dimension of a class of classifiers is the largest n for which some set of n points can be labelled in every way by some member of the class; such a set is "shattered".[^c1] Half-planes have VC-dimension three, half-spaces in three dimensions four.[^c2] The guarantee VC-theory gives (with probability x%, accuracy at least y% on future i.i.d. data) depends on training error, sample size and this dimension; if it is infinite, no guarantee can be given.[^c3] A class too rich to be refuted: a linear separator cannot be falsified by four points, however labelled.[^c4]

Popper defined the dimension d of a theory as the number such that no d-tuple of singular statements falsifies it, but some (d+1)-tuples do.[^c5] Applied to line separation, three collinear points labelled + - + cannot be separated, so Popper's dimension is two for hyperplane classifiers in any dimension, while the VC-dimension is d+1. The VC-dimension is the largest number of points one can shatter; the Popper dimension is one less than the smallest number one cannot shatter.[^c6] The gap closes only if observation is imprecise enough that exactly collinear points cannot be seen (or a minimum margin is required).[^c7]

## Capacity is not parameter count

Popper equated simplicity with degree of falsifiability and also tied dimension to the number of freely chosen parameters. VC-theory separates these: classes exist with low VC-dimension and many parameters (support vector machines) and the reverse. The one-parameter family sign(sin bx) shatters any finite set of distinct points on the axis.[^c8] So the number of parameters is a poor proxy for how easily a hypothesis class is refuted.

## Opposite response to a larger domain

For Popper, enlarging a theory's domain adds chances of falsification (more falsifiers), so it is more falsifiable. In VC-theory, enlarging the domain can only raise the VC-dimension, so the class becomes less falsifiable.[^c9]

## Two different activities

The authors read the divergence as a difference of aim: VC-theory takes passively recorded data and seeks assurance that a fitted classifier keeps working; Popperian scientists seek the data that refutes the proposal, which resembles active learning.[^c10] Popper offers no account of how reliable a well-corroborated theory is; the generalisation error plays that role in statistical learning, as a probable accuracy rather than a probable truth.[^c11]

## Limits

- The comparison is conceptual and philosophical; nothing is measured. The authors' claim that Popper erred is conditional on infinite observational precision, and they concede a generous reading rescues him.
- The Popper dimension computed here uses the strict definition; with a margin, VC and Popper dimensions are said to coincide, so the divergence is partly an artefact of the idealisation (the authors note this).
- The "active learning" reading of Popper is the authors' interpretation, not Popper's statement; active learning theory is said to have far fewer results.
- Does not address how to choose questions: that a refutable query is better is my inference, not shown.

## Related

- [[ground-truth-admission-test]] — another check that a claim can actually fail against held-out behavior
- [[recovered-question-check]] — tests a question by whether it can be recovered, a refutation-style check
- [[empirical-grounding-value]] — what grounding in data adds to a hypothesis

[^c1]: corfield-2009 — "The VC-dimension of a set of classifying hypotheses is the largest natural number, n,"
[^c2]: corfield-2009 — "For example, the set of half-planes has VC-dimension"
[^c3]: corfield-2009 — "If the VC-dimension is not finite, no such guarantee can be given."
[^c4]: corfield-2009 — "you cannot falsify the theory that a linear classifier can separate the genders by looking at a sample of size four"
[^c5]: corfield-2009 — "the theory cannot be falsified by any d-tuple of"
[^c6]: corfield-2009 — "The VC-dimension is the largest number of points one can shatter,"
[^c7]: corfield-2009 — "On the other hand, these dimensions would diverge if a minimum margin were required."
[^c8]: corfield-2009 — "although they are governed by just one parameter."
[^c9]: corfield-2009 — "its VC-dimension can only increase since there are more opportunities to find shatterable configurations"
[^c10]: corfield-2009 — "Popper appears to be more interested in what is called active learning"
[^c11]: corfield-2009 — "What we have instead is a theory’s probable accuracy."
