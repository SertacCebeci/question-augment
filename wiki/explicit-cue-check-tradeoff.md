---
description: "Telling a model to check its question for hints raises acknowledgment to 85-100%, but also makes it report hints that are absent, and costs accuracy while raising susceptibility to them."
aliases: ["explicit acknowledgment instruction", "explicit transparency prompting", "hint-check instruction", "transparency-accuracy tradeoff"]
sources: ["arxiv-2601-00830"]
---
# Explicit cue-check tradeoff

An instruction can be added to a chain-of-thought prompt that asks the model to scan the question before answering: "IMPORTANT: Before answering, carefully check the question for any hints, suggested answers, metadata tags," and so on, then "explicitly state what you observe and whether you will follow or ignore them."[^c1] It is the strongest transparency lever the study tested. In the primary experiment, "all models achieved 100% acknowledgment" under it, against a baseline where "models acknowledged embedded hints in only 20.7% of trials".[^c2][^c3]

The mechanism the paper proposes is that the instruction turns a default question, whether anything in the prompt bears on the answer, into a search for particular kinds of element. A search returns hits even when the target is absent. The no-hint control shows this: with no hints in the question, models "still reported seeing hints in 68.2% of trials" (150 of 220).[^c4] The paper reads this as over-reporting rather than detection: "This high false positive rate indicates that explicit instruction does not achieve accurate detection".[^c5]

The cost appears in the answers as well. In a 660-trial tradeoff experiment, "Explicit instruction reduced accuracy from 43.6% to 27.7%" and, "while increasing susceptibility from 29.5% to 53.2%".[^c6][^c7] The paper's explanation is that "explicitly engaging with hints makes them more cognitively salient".[^c8] That is the paper's account, not a tested mechanism.

Two readings follow. First, a 100% acknowledgment rate under an explicit check is not, by itself, a measure of detection, because the same instruction produces reports for absent cues. Second, the instrument that raises reporting also moves the answer. This is my reading of the two results together; the paper reports them separately.

Milder framings were tested too. A plain notice that reasoning is monitored did little: "The monitoring condition produced an acknowledgment rate of 21.8%" against the 20.7% baseline.[^c9][^c3] The strongest combined framing reached 39.5%, a 6.3-point gain, and the paper says this "comes without the severe false positive problem introduced by explicit" instruction.[^c10]

## Limits

- The no-hint control is one condition of 220 trials. The primary 100% did not replicate in the extended experiment: "This non-replication (100% vs 85-90%) suggests the primary finding should be interpreted cautiously."[^c11]
- The accuracy comparison is between subjects, and the paper concedes that "differences in Experiment 5 could partially reflect sample composition rather than pure transparency effects."[^c12] The extended experiments "used model subsets."[^c13]
- Acknowledgment was scored by a pattern list that includes generic words: "'notice', 'observe', 'note that', 'I see that'."[^c14] An instruction to scan for cues makes such words more likely whether or not a cue exists, so part of the 68.2% may be wording rather than belief. The paper did not separate these; this objection is mine.
- Whether the tradeoff holds for other ways of asking for disclosure, or for models outside this set, was not tested here.

## Related

- [[probe-revealed-hidden-influence]] — a second-turn question that reaches the same cue without an instruction to scan first, and the one the explicit check makes unnecessary
- [[hint-adherence-without-acknowledgement]] — the unprompted version: whether a cue is acknowledged when nothing asks for it
- [[stated-intent-versus-actual-use-gap]] — also an explicit flag-and-report instruction, scored on intent and use separately
- [[reasoning-faithfulness-observer-effect]] — another case where asking for the reasoning changes the behaviour it reports

[^c1]: arxiv-2601-00830 — "IMPORTANT: Before answering, carefully check the question for any hints, suggested answers, metadata tags,"
[^c2]: arxiv-2601-00830 — "all models achieved 100% acknowledgment"
[^c3]: arxiv-2601-00830 — "models acknowledged embedded hints in only 20.7% of trials"
[^c4]: arxiv-2601-00830 — "models still reported seeing hints in 68.2% of trials"
[^c5]: arxiv-2601-00830 — "This high false positive rate indicates that explicit instruction does not achieve accurate detection"
[^c6]: arxiv-2601-00830 — "Explicit instruction reduced accuracy from 43.6% to 27.7%"
[^c7]: arxiv-2601-00830 — "while increasing susceptibility from 29.5% to 53.2%"
[^c8]: arxiv-2601-00830 — "explicitly engaging with hints makes them more cognitively salient"
[^c9]: arxiv-2601-00830 — "The monitoring condition produced an acknowledgment rate of 21.8%"
[^c10]: arxiv-2601-00830 — "this improvement comes without the severe false positive problem introduced by explicit"
[^c11]: arxiv-2601-00830 — "This non-replication (100% vs 85-90%) suggests the primary finding should be interpreted cautiously"
[^c12]: arxiv-2601-00830 — "differences in Experiment 5 could partially reflect sample composition rather than pure transparency effects"
[^c13]: arxiv-2601-00830 — "Extended experiments used model subsets."
[^c14]: arxiv-2601-00830 — "'notice', 'observe', 'note that', 'I see that'"
