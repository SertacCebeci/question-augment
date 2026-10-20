---
description: "A correct answer buried in redundant, secondary or emotional material lowers the output's signal-to-noise; clinician-scored rubrics penalize that separately from inaccuracy."
aliases: ["information fat accumulation", "output redundancy penalty", "low signal-to-noise answer"]
sources: ["arxiv-2512-11544"]
---
# Information steatosis

A response can be right and still fail the person who asked. Shen et al. name the case *information steatosis*: the model gives the correct content but mixes it with a large amount of secondary material, emotional interference or irrelevant explanation, so the usable part of the answer is diluted.[^a1] The name is a metaphor borrowed from liver disease, and the paper places it inside a wider "AI-MASLD" frame. What is concrete is the scoring: redundancy is judged on its own rung, apart from whether the content is accurate.

The rubric makes this explicit. The twenty probes are scored on a 0–4 inverse scale by two clinicians working blind.[^a2] In the noise probes a mild version earns "1 point (Partial omission or mild redundancy)", a heavier one "3 points (Poor prioritization / severe omission / heavy redundancy)", and the top example reads "Answer may be accurate but is extremely wordy, burying core points."[^a3] A response can therefore be correct on the facts and still lose points on presentation. That separation is what makes the pattern a failure of its own rather than a synonym for error.

The mechanism the authors give is reader burden. Redundant content blurs the line between primary and secondary issues, which "compels clinicians to conduct secondary filtering".[^a4] GPT-4o is the main example: it "tended to generate redundant content", and this "pattern represented the most typical penalty scenario" for it, often scoring 2–3 points.[^a5]

The paper keeps this apart from fabrication. Its third mode is defined as "the model including symptoms or information in its output that" the patient never mentioned.[^a6] Steatosis adds too much true-or-neutral material; fabrication adds material that is not in the input (my reading of the two definitions). The two can co-occur in one answer, but they are scored as different failures.

The input-side neighbour is [[blind-execution]], where a rambling request is recovered better than a missing one while the agent then generates more output. Here the same surplus is seen from the reader's end. The two works do not measure each other, so the link is my inference. A related point, also mine: a grader with a [[llm-judge-biases]] tilt toward longer answers would score steatosis upward, so an evaluation that scores content but has no redundancy term will miss it.

## Limits

- Four models and twenty probes: "only four mainstream LLMs were evaluated".[^a7] The "typical penalty" claim rests on the authors' qualitative reading of high-risk probes, not on a counted frequency across the whole set.
- The probes are simulated narratives. "the inclusion of de-identified real patient records would" add ecological validity, and the paper did not use them.[^a8]
- The liver analogy is the authors' framing: "Just as the liver suffers functional impairment under metabolic stress induced by excessive lipid load".[^a9] What survives the transfer is the observation that an answer's usefulness falls when its content is not ranked. What does not survive is any claim of a shared mechanism; nothing in the text measures anything like lipid accumulation in a model.
- Redundancy was judged by clinicians against a rubric. The line between "moderate" and "heavy" redundancy is rater judgment. The text names an intraclass-correlation check; this note does not rely on its value.
- Only text was tested. Whether steatosis changes with images or speech is not established here.

## Related

- [[blind-execution]] — the input-side counterpart: rambling instructions are recovered better than missing ones, but the output grows.
- [[llm-judge-biases]] — a verbosity tilt in graders may reward the burial rather than penalize it (my inference, not tested in the paper).
- [[emotion-fact-separation]] — emotional interference is one of the secondary materials this paper counts as steatosis.

[^a1]: arxiv-2512-11544 — "the model outputting correct information while intermixing it with substantial secondary information, emotional interference, or irrelevant explanations"
[^a2]: arxiv-2512-11544 — "assessed via a double-blind, inverse rating scale by two independent clinicians"
[^a3]: arxiv-2512-11544 — "Answer may be accurate but is extremely wordy, burying core points."
[^a4]: arxiv-2512-11544 — "compels clinicians to conduct secondary filtering"
[^a5]: arxiv-2512-11544 — "This pattern represented the most typical penalty scenario for GPT-4o"
[^a6]: arxiv-2512-11544 — "the model including symptoms or information in its output that"
[^a7]: arxiv-2512-11544 — "only four mainstream LLMs were evaluated"
[^a8]: arxiv-2512-11544 — "the inclusion of de-identified real patient records would"
[^a9]: arxiv-2512-11544 — "Just as the liver suffers functional impairment under metabolic stress induced by excessive lipid load"
