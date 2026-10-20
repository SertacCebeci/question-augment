---
description: "A one-sentence certainty cue appended to an LLM rationale moved trust, decision confidence and advice adoption beyond rationale correctness; rationale presentation timing did not."
aliases: ["certainty framing of LLM rationales", "confidence cue persuasion", "rationale certainty cue effect"]
sources: ["arxiv-2603-07306"]
---
# Certainty framing shifts trust beyond rationale correctness

In a factual-verification study, participants saw an LLM's binary answer plus a step-by-step reasoning rationale. The experiment crossed rationale correctness (correct vs. a rationale with a controlled logical or factual flaw), certainty cue (none, certain, uncertain) and presentation format (instant, delayed, on-demand).[^c1] The cue was a single sentence added at the end of the rationale, for example a statement of confidence or of hesitation about the reasoning.[^c2]

**What moved.** Correctness and certainty were both main effects. Correct rationales and certainty cues raised trust, decision confidence and advice adoption; incorrect rationales and uncertainty cues lowered them.[^c3] For trust in the information, uncertain cues reduced trust relative to certain and to no cue, and correct rationales were trusted more than incorrect ones.[^c4] Certain cues raised trust in the LLM system over uncertain and no cues.[^c5]

**Beyond correctness.** The authors stress that the cue changed trust and decisions with the rationale content held fixed, so the effect is not just a proxy for the rationale being right.[^c6] Since the cue is a verbal sentence, not evidence, a confident tone on a flawed rationale can therefore buy trust it has not earned. The paper's summary is that the risk lies where weak reasoning is paired with strong certainty.[^c7]

**Presentation timing did not matter.** Revealing the rationale with the answer, after a short delay, or only on a Show/Hide button produced no significant differences.[^c8] So in this design the lever was what the rationale and its tone said, not when it appeared.

**How participants described use.** Open-ended answers said rationales were mostly used to audit the logic and calibrate trust, with trust dropping sharply when rationale and answer were inconsistent.[^c9] This is a self-report; it sits next to, not in place of, the measured cue effect.

For asking and answering: an answerer's stated certainty is a separate signal channel from its content, and a receiver's trust follows both. My inference, not measured here, is that a cue is only useful to the receiver if it covaries with the actual reliability of the answer.

## Limits

- Short online study: 68 Prolific participants, English-speaking, six trials each, CHI extended-abstract scale.[^c10]
- Binary factual claims from a fact-checking dataset; open, expert or multi-turn questions untested.
- Errors were inserted by hand into one step; naturally occurring reasoning errors may be more or less detectable.
- Only a one-sentence verbal cue was tested; numeric confidence, hedges inside the steps, or cues calibrated to true reliability were not compared.
- Adoption rates were high everywhere (about 0.84 to 0.96 in the descriptive table), leaving little range; effect sizes are modest.
- Whether the cue effect is calibration-improving or -harming was not measured against ground truth reliability of the cue.

## Related

- [[over-reliance-discrimination-failure]] — another study where confidence failed to flag wrong AI answers
- [[verbal-confidence-cached-retrieval]] — verbalised model confidence as an output signal
- [[perception-sensitive-confidence-reward]] — confidence expressions as they are perceived by receivers
- [[hint-adherence-without-acknowledgement]] — reasoning text not faithfully reflecting what drives answers

[^c1]: arxiv-2603-07306 — "Rationale Correctness: correct vs. incorrect; within-subjects) × 3 (Certainty"
[^c2]: arxiv-2603-07306 — "reasoning by adding a one-sentence cue at the end of the rationale."
[^c3]: arxiv-2603-07306 — "incorrect rationales and uncertainty cues reduced them. Notably,"
[^c4]: arxiv-2603-07306 — "showed that uncertain cues decreased trust relative to certain (𝑝 <"
[^c5]: arxiv-2603-07306 — "Certain cues increased trust in LLMs compared to"
[^c6]: arxiv-2603-07306 — "rationale content, indicating effects beyond correctness. In contrast, the presentation format showed no significant differences."
[^c7]: arxiv-2603-07306 — "when weak reasoning is paired with strong certainty"
[^c8]: arxiv-2603-07306 — "while presentation format had little impact, addressing our RQ."
[^c9]: arxiv-2603-07306 — "rationales mainly to audit and calibrate trust, despite trust dropping"
[^c10]: arxiv-2603-07306 — "We recruited 68"
