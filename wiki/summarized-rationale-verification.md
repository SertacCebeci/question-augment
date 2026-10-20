---
description: "A verifier checks a condensed, linear solution path distilled from a long chain of thought, not the raw trace, and names the first wrong step; the summary keeps step-by-step checking cheap."
aliases: ["summary-based process verification", "verification of summarized outcomes", "verification of a condensed solution path"]
sources: ["arxiv-2512-10756"]
---
# Summarized-rationale verification

A long chain of thought is verbose. A verifier that reads it whole pays for every redundant branch, and a verifier that reads only the final answer cannot see a flawed route to a correct result. The Outcome-based Process Verifier (OPV) work takes a middle path: a summarizer first rewrites the reasoning into a shorter object, and the verifier checks that object step by step. The summarizer "first summarizes verbose and meandering CoT trajectories into" concise, linear solution paths, keeping the key steps and pruning redundant explorations.[^c1] The paper treats this summary as a stand-in for the reasoning: "This summary serves as a faithful proxy of the underlying reasoning rationale".[^c2]

The verifier does not return one verdict for the whole. It "performs a step-by-step validation on this summary to identify the first erroneous step."[^c3] Its output is an index over the summary's steps, with -1 meaning a fully correct solution and a natural-language explanation alongside. The paper focuses on the first error because later steps "are built upon faulty premises and thus lack mathematical soundness."[^c4] The index is therefore a location, not a score, and it can be scored against annotated error positions.

## Why a summary rather than the raw trace

The claimed gain is efficiency with less interference: summarization "significantly reduces the complex, redundant reasoning structures in the input CoT, making OPV more efficient and less susceptible to interference from redundancy than vanilla" process verifiers.[^c5] The contrast is with two existing paradigms. An outcome-only verifier "assess[es] only the final answer against the ground truth, and overlook[s] the reliability of intermediate steps" in long chains.[^c6] A step-by-step verifier on the raw trace struggles with the trace's length and dependencies. The summarized route keeps step-level judgment and shortens the input.

## What the summary must contain

The summary is the whole mechanism, so its quality decides what the verifier can see. The authors first tried the model's own post-thinking summary and rejected it: such summaries were "inadequate, as they omitted crucial intermediate steps and".[^c7] They re-summarized the thinking content instead, "preserving all calculations, enumerations, and case analyses" and splitting steps uniformly.[^c8]

## What was measured

Applied to a public synthetic math set (AM-DeepSeek-R1-0528-Distilled), each entry was verified eight times and flagged when at least six runs reported an error. "Out of 674k math-related data entries checked, 53.7k were flagged as problematic by OPV."[^c9] On 50 sampled problems, human experts found the flags valid in most cases: "with 88% of the judgments being valid". The authors combine these into an estimate that about 7.0% of entries contain process errors.[^c10] For this application they used the vanilla summaries for cost, and the authors note the cost of that choice: "some answers might be incorrectly flagged due to inappropriate summarization."[^c11] Two of the 50 checked solutions were correct but flagged, because "their original summaries introduced logical gaps."[^c12]

In test-time use on AIME2025, the verifier scores several policy samples per problem. The abstract reports the accuracy of DeepSeek-R1-Distill-Qwen-32B "from 55.2% to 73.3% on AIME2025" as the compute budget scales.[^c13] Here the authors used the original summary part of each chain, not a re-summary, "to reduce compute budget and avoid introducing extra noise." So the gain reported at test time was obtained on the weaker summary.[^c14]

## Limits

- Mathematics only. The training pool and the held-out OPV-Bench are mathematical problems; no open-ended or non-mathematical task is tested in the text read.
- The summarizer is itself a model: "All sampled solutions are pre-summarized by DeepSeek-V3."[^c15] How much the verdict depends on the summarizer was not isolated. I searched the text read for an ablation comparing verification of the summary against verification of the raw chain and found none (my reading).
- The "faithful proxy" is asserted, not measured. A step the summarizer drops is invisible to the verifier, so a summary gap can hide an error or manufacture one; the paper's two-of-fifty case shows the second. Whether the first is common was not tested (my inference).
- The 7.0% estimate rests on 50 human-checked problems and a validity rate of 88%; no interval is given in the sections read.
- Expert labels come from a small annotator pool with explanations; agreement between annotators is not reported in the sections read.
- The claim is about verifying a model's reasoning for correct answers. It says nothing about whether a verdict on a summary improves the questions asked of a reasoner, or whether it transfers to answerers that were never trained on the summary format.

## Related

- [[process-outcome-consistency-verification]] — a different route to the same failure, a correct answer from a flawed derivation: there the verifier checks the whole derivation against its conclusion, here it checks a summarized path step by step
- [[cot-judge-detection-localization-gap]] — judges that flag a broken chain without naming the step; a first-error index is the output that avoids that gap
- [[process-reward-model-hackability]] — step-level scoring of reasoning and how a policy can exploit it
- [[rashomon-committee-querying]] — the same verifier's disagreement across repeated runs is used to choose which cases get expert labels

[^c1]: arxiv-2512-10756 — "OPV first summarizes verbose and meandering CoT trajectories into"
[^c2]: arxiv-2512-10756 — "This summary serves as a faithful proxy of the underlying reasoning rationale"
[^c3]: arxiv-2512-10756 — "on this summary to identify the first erroneous step."
[^c4]: arxiv-2512-10756 — "are built upon faulty premises and thus lack mathematical soundness."
[^c5]: arxiv-2512-10756 — "making OPV more efficient and less susceptible to interference from redundancy than vanilla"
[^c6]: arxiv-2512-10756 — "assess only the final answer against the ground truth, and overlook the reliability of intermediate steps in"
[^c7]: arxiv-2512-10756 — "as they omitted crucial intermediate steps and"
[^c8]: arxiv-2512-10756 — "preserving all calculations, enumerations, and case"
[^c9]: arxiv-2512-10756 — "53.7k were flagged as problematic by OPV"
[^c10]: arxiv-2512-10756 — "with 88% of the judgments being valid"
[^c11]: arxiv-2512-10756 — "some answers might be incorrectly flagged due to inappropriate summarization."
[^c12]: arxiv-2512-10756 — "their original summaries introduced logical gaps."
[^c13]: arxiv-2512-10756 — "the accuracy of DeepSeek-R1-Distill-Qwen-32B from 55.2% to 73.3% on AIME2025"
[^c14]: arxiv-2512-10756 — "the summary part of the original CoT here to reduce compute budget and avoid introducing extra noise"
[^c15]: arxiv-2512-10756 — "All sampled solutions are pre-summarized by DeepSeek-V3"
