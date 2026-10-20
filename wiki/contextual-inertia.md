---
description: "LLMs in multi-turn dialogue copy their previous response regardless of whether it was right; most multi-turn errors trace to prior turns, and a single-turn-anchored reward reduces it."
aliases: ["multi-turn inertia", "persistence on previous reasoning traces"]
sources: ["arxiv-2603-04783"]
---
# Contextual inertia

Contextual inertia is the tendency of a model to rigidly adhere to its own earlier reasoning traces when a new instruction arrives, even when those traces are partially invalid or obsolete.[^c1] It is measured as the semantic similarity between the final answer and the preceding response, judged by GPT-4o.[^c2]

## The indiscriminate property

The key finding is that the intensity does not depend on whether the history was good. Histories that led to a correct final answer and histories that led to an incorrect one produce statistically indistinguishable intensity distributions.[^c3] So the model is not weighing the quality of what it said before: even a misleading or erroneous previous answer is propagated into later turns.[^c4]

## How much of the failure it explains

Among verified-incorrect multi-turn conversations, the authors had GPT-4o sort the root cause into misleading context, propagated error, or local reasoning failure. Over 70%-90% of errors traced to previous responses (the first two categories).[^c5] Conversations were chosen so that the full instruction given in one turn yields accuracy above 0.7, which isolates the failure from base-model weakness.[^c6] This reframes the usual explanations (context length, premature answering): the paper argues abstention or early clarification treats a symptom, and cannot help where the user is correcting an answer the model had to give (the "No, actually X is 5" case).[^c7]

## What reduces it

The proposed training (RLSTA) keeps only histories where single-turn accuracy on the merged instruction exceeds multi-turn accuracy, then adds to a verifier reward a length-normalized likelihood of the multi-turn answer under the base model conditioned on the full single-turn instruction.[^c8] The model's own single-turn ability is the anchor pulling the answer away from the history. The paper reports it beats standard fine-tuning and abstention-based methods and generalizes across domains.[^c9]

For asking and answering: a follow-up turn that corrects or adds information is answered worse not because the information is missing but because the model's own last answer is weighted as if it were reliable. Restating the full set of conditions in one turn removes the pull (my inference from the anchor design, not tested as a prompting intervention here).

## Limits

- The intensity metric and root-cause labels rely on GPT-4o judgments; their agreement with humans is not something I verified.
- Only the "indistinguishable distributions" evidence supports "indiscriminate"; no causal intervention on history quality was read.
- The anchor requires a verifier and a model that already solves the single-turn version; filtered cases exclude problems the model cannot solve at all.
- Tasks were synthetic sharded or refined math/code-style conversations, not open dialogue.

## Related

- [[multi-turn-reward-clarification-training]] — trains clarifying behavior in multi-turn RL; the abstention route this note argues is insufficient alone
- [[third-position-repair]] — repair of a prior turn in conversation, the human counterpart of correcting an earlier answer
- [[minimal-edit-belief-revision-benchmark]] — tests revising earlier beliefs after new information

[^c1]: arxiv-2603-04783 — "the inherent tendency of LLMs to rigidly adhere to previous reasoning traces when processing new instructions, even when those traces are partially invalid or obsolete"
[^c2]: arxiv-2603-04783 — "we define the intensity of contextual inertia ICI (mn , mn−1 ) as the semantic similarity between the model’s final answer mn and the preceding response mn−1"
[^c3]: arxiv-2603-04783 — "the intensity distributions conditioned on contrasting history qualities are statistically indistinguishable"
[^c4]: arxiv-2603-04783 — "even when mn−1 is misleading or erroneous, the model is compelled to propagate these traces into subsequent turns"
[^c5]: arxiv-2603-04783 — "over 70%–90% of multi-turn errors can be directly traced back to previous responses"
[^c6]: arxiv-2603-04783 — "yields high (> 0.7) accuracy"
[^c7]: arxiv-2603-04783 — "the model cannot abstain in early turns; it must fundamentally overcome its inertia for a correct answer"
[^c8]: arxiv-2603-04783 — "By calculating the length-normalized likelihood of the response under πθref (· | ifull )"
[^c9]: arxiv-2603-04783 — "RLSTA significantly outperforms standard fine-tuning and abstentionbased methods"
