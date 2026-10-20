---
description: "A judge's criteria can shift from one answer pair to the next under the same question; fixing one self-written rubric per question lowered both local and global inconsistency."
aliases: ["inconsistent judging criteria", "pair-dependent judging criteria"]
sources: ["arxiv-2512-16041"]
---
# Situational preference

A language-model judge that compares answers to one question should, on the rational-choice view the Sage suite adopts, hold one standard for "better" across all the comparisons. The paper names the failure where it does not "situational preference", defined as "inconsistent judging criteria encountering different answers under the same question".[^c1] The authors state the attribution plainly: "We attribute this to a new phenomenon called situational preference".[^c2]

The mechanism, as the paper argues it: a robust judge "should first model the question internally regardless of how the answers vary".[^c3] When the judge instead re-forms its standard for each pair, verdicts drawn from different pairs need not agree. Inside one pair the verdict can be stable and still conflict with a verdict on another pair. Across a full round-robin, that conflict shows up as local flips and as cycles in the global measure (see [[judge-transitivity-violation]]).

The test is an intervention. The judge first writes out its judging rubric for the question, and then uses that rubric for every pair. The rubric "is generated only once per question and serves as a fixed" standard,[^c4] so the criteria cannot change between comparisons. On the paper's aggregate, this reduces the inconsistency measures "by 16.1% and 11.0%" for IPI and TOV.[^c5] The authors conclude that "explicit judging rubrics can substantially mitigate this".[^c6] The abstract puts the same point as "rubrics or criteria can help the model judge consistently across answer pairs".[^c7]

The phenomenon is strongest where answers are close. All models in the study "show a marked degradation in performance from Sage-Easy to Sage-Hard", where the harder answers come from a single model.[^c8] This matches the reading that the judge's standard is not tested when the answers differ only in subtle ways.

## Limits

- The evidence for the phenomenon is one intervention. Writing a rubric also lengthens the prompt and adds a step, so a fall in inconsistency after the rubric is consistent with situational preference but does not isolate it from those other effects (my inference).
- The passages read give only aggregate reductions. Whether every model benefits, and by how much, is not shown in what was read.
- A rubric can be poor. Related work finds that self-generated rubrics help when good and push a verifier below rubric-free judging when misleading (see [[two-sided-rubric-influence]]). A rubric that lowers inconsistency is not thereby shown to lower error.
- The cause is located only in the output pattern. "Inconsistent judging criteria" is the authors' reading of the flips and cycles; no change inside the model was measured.
- The word "situational" is the authors' term. It is not the same concept as [[situational-relevance]], which concerns which past interactions help a user in retrieval.

## Related

- [[judge-transitivity-violation]] — the global measure where shifting criteria appear as cycles
- [[llm-judge-biases]] — position effects; the paper's local measure counts these together with run-to-run noise
- [[llm-judge-score-instability]] — the run-to-run noise that the same local measure also picks up
- [[two-sided-rubric-influence]] — rubrics can raise or lower a judge's accuracy depending on their quality
- [[criterion-collapse-in-evaluation]] — readers who merge separate criteria into one impression; a related failure of keeping criteria separate (my reading)

[^c1]: arxiv-2512-16041 — "i.e., inconsistent judging criteria encountering different answers under the same question"
[^c2]: arxiv-2512-16041 — "We attribute this to a new phenomenon called situational preference"
[^c3]: arxiv-2512-16041 — "question internally regardless of how the answers vary"
[^c4]: arxiv-2512-16041 — "this rubric is generated only once per question and serves as a fixed"
[^c5]: arxiv-2512-16041 — "reducing IPI and TOV scores by 16.1% and 11.0%"
[^c6]: arxiv-2512-16041 — "explicit judging rubrics can substantially mitigate this"
[^c7]: arxiv-2512-16041 — "rubrics or criteria can help the model judge consistently across answer pairs"
[^c8]: arxiv-2512-16041 — "all models show a marked degradation in performance from Sage-Easy to Sage-Hard"
