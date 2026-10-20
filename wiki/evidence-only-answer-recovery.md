---
description: "A reference model, shown the question and the listed evidence but not the video, must reach the policy's answer; agreement rewards answers that the stated evidence actually supports."
aliases: ["consistency reward", "answer traceability", "evidence-only re-answering", "answer recoverability"]
sources: ["arxiv-2511-18463"]
---
# Evidence-only answer recovery

A model can write evidence and then give an answer that does not follow from it. The Video-DPL consistency term tests the link directly, by asking whether the answer can be recovered from the evidence alone. The paper measures "answer traceability" by "testing whether the final answer is recoverable from the extracted perception alone."[^c1] Concretely, the question and the perception list go to a reference model "without video input," and the reference model's answer is compared with the policy's final answer through a match function.[^c2]

The intuition the authors give is a sufficiency condition: "when the extracted perception is sufficient and factual, the same answer should be reachable from E(y) alone."[^c3] So the test reads the evidence as a sufficient premise. If the reference model cannot reach the policy's answer from the list, then the list is missing something or the answer is disconnected from it. The authors put it as: "consistency typically indicates missing perception or a disconnect between the perception and the answer."[^c4]

What the test measures is different from what it cannot measure. It does not look at the video, so it cannot tell whether the evidence is true. It looks only at whether the answer follows from the evidence as written. That is why the paper pairs it with a factuality reward: "Rah constrains perception factuality, while Rcons enforces evidence-grounded answering."[^c5] The two rewards cover different failures. A factuality judge sees false evidence but not an answer that ignores correct evidence; the recovery test sees the second but not the first. Where the answer is right and the visible reasoning stops supporting it, the failure is the one described as [[answer-evidence-gap]].

The paper reports the term's role in training rather than in isolation. Adding it "nearly eliminates out-of-format perception outputs," and the authors say it "improves the alignment between reasoning answers and video evidence".[^c6][^c7] The second claim is a result of the joint training, not of this term alone.

## Limits

- The reference model is not identified in the parts of the text I read. If it is weak, a correct answer can fail to match; if it has strong priors, it may recover the answer from its own knowledge rather than from the evidence. Neither case is tested in the text.
- The test is one-directional. It says the answer follows from the evidence, not that the evidence is true. Factual support needs the other reward, and a faithful answer built on a false list passes this test.
- The match function is task-dependent and its definition is not given in the parts read. For open-ended answers the match function probably carries much of the signal; that is my inference and was not measured.
- The paper does not run this consistency term alone. Its contribution is reported only together with the anti-hallucination reward, so its share of the gain is not separated.
- Only video question answering is tested. Whether an evidence list from text or images supports the same recovery test is not shown here.

## Related

- [[perception-logic-decoupling]] — the split that makes the evidence a separate list, so that this test has an object to read
- [[unit-averaged-grounding-reward]] — the factuality counterpart, which scores each listed unit against its clip
- [[answer-reasoning-consistency-reward]] — the lift-based consistency reward over a reasoning trace, scored against a gold answer; a different object and a different estimator
- [[process-outcome-consistency-verification]] — a verifier that rewards an answer only when its derivation agrees with it, aimed at lucky guesses in text reasoning
- [[answer-evidence-gap]] — the failure a traceability test is meant to catch, which the cache-coverage note describes as the final answer staying right while the visible reasoning stops supporting it

[^c1]: arxiv-2511-18463 — "answer is recoverable from the extracted perception alone"
[^c2]: arxiv-2511-18463 — "without video input to a reference"
[^c3]: arxiv-2511-18463 — "the same answer should be reachable from E(y) alone"
[^c4]: arxiv-2511-18463 — "consistency typically indicates missing perception or a disconnect between the"
[^c5]: arxiv-2511-18463 — "Rah constrains perception factuality, while Rcons enforces evidence-grounded answering"
[^c6]: arxiv-2511-18463 — "eliminates out-of-format perception outputs, enabling the anti-hallucination reward to function effectively"
[^c7]: arxiv-2511-18463 — "improves the alignment between reasoning answers and video evidence"
