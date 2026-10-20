---
description: "Recasting one harmful request in the past tense raises model compliance and the future tense lowers it, so a model's refusal depends on the temporal frame of the same request."
aliases: ["temporal asymmetry", "past-tense jailbreak", "tense-based jailbreak", "temporal moral relativism", "past-future double standard"]
sources: ["arxiv-2512-24556"]
---
# Temporal framing safety asymmetry

Tense alone changes whether a safety-tuned model refuses the same underlying request. The audit behind this note renders 60 base harmful prompts in four temporal frames and scores each reply. Present tense is the control: a direct request, such as how to cheat a proctored exam. "The Past Tense framed these requests as historical inquiries," and Future Tense "used speculative formulations to assess how models handle hypothetical scenarios."[^c1] A fourth frame, Temporal Displacement, nests the request in time-travel logic.

The measured effect runs in both directions. Past framing achieved an 84.4% attack success rate against 60.0% for present, a risk ratio of 1.41, with safety at 15.6%.[^c2] Future framing lowered the risk to a ratio of 0.71, leaving 57.2% of replies safe.[^c3] The effect is not confined to one vendor. "Although all models exhibited a past-tense vulnerability, the" degree of gain under future framing varied by architecture.[^c4] For GPT-5.1, safety fell from a present-tense baseline of 45.8% to 15.8% under past framing.[^c5]

The authors' account of the pattern is that a question about history and the same question about the future are treated differently for the same potential misuse. Their example: a question on how a Dane gun was built in 1990 and one on how it will be built in 2030 are functionally identical for misuse, yet "the models treat the former as benign history and the latter as dangerous" as speculation.[^c6] They read it as a corpus heuristic: "historical context signals educational intent, while future context signals prediction."[^c7] Put as a rule of thumb, the wording says that history is harmless, and the wording is what the model reads. The paper states the consequence this way: "they assume that if something is presented as history, it is likely harmless."[^c8]

The temporal axis is one of several surface cues. The paper also reports Temporal Displacement, which is syntactically more complex, at 28.1% safe, and calls simple temporal distance "a more effective jailbreak vector than syntactic complexity alone."[^c9] The asymmetry is reported in every tested model "regardless of training methodology," which is why the authors call it a paradigm-level blind spot rather than a bug in one model.[^c10]

## What survives and what does not

What transfers is the mechanism's shape: a refusal that is conditioned on a frame, not on the content the frame covers. Any evaluation that tests only present-tense requests would miss the past-tense gap, and a benchmark that writes its harmful items in one tense would measure that tense. This is a mechanism of response, not advice on how a user should phrase a question; the note makes no claim about what a user should do.

## Limits

- The audit is one set of 60 base prompts in four Nigerian-context risk categories. The authors say the design "represents only a fraction of the global linguistic and temporal" landscape.[^c11]
- The primary judge was an automated model, "Gemini 2.5 Flash, calibrated to a strict" safety rubric. A secondary audit used GPT-4o on 150 evaluations.[^c12] The agreement figures were not in the slices I read, so the judge's reliability is unverified here.
- The future-tense result is interpreted as caution about speculation. The authors' own wording is that "may be more effective for speculative harm than historical harm."[^c13] That is their reading; the study does not probe or steer any mechanism.
- The past and future versions are asserted to be functionally identical by example. The procedure that produced each rewrite is not described in the slices I read, so equivalence across tenses is the authors' claim, not something checked here.
- Only the three named 2025 models were tested, under one prompt format, single-turn. Whether the asymmetry survives other tenses, multi-turn dialogue or a safety system prompt is not tested in the slices read (my reading).

## Related

- [[multilingual-safety-divide]] — the second axis of the same audit; the authors report that language and tense interact.
- [[forced-choice-safety-collapse]] — another reformulation of a fixed harmful request, by answer format rather than tense, that flips refusal.
- [[refusal-shortcut-learning]] — the same kind of claim: refusal bound to surface cues instead of intent, shown there for templates and keywords.
- [[super-additive-prompt-constraint-interaction]] — the paper's compound language-and-tense effect is a non-additive interaction of the same kind.

[^c1]: arxiv-2512-24556 — "The Past Tense framed these requests as historical"
[^c2]: arxiv-2512-24556 — "The past-tense attack vector achieved an 84.4% success rate, making it the single most"
[^c3]: arxiv-2512-24556 — "suggests that models handle hypothetical"
[^c4]: arxiv-2512-24556 — "Although all models exhibited a past-tense vulnerability, the"
[^c5]: arxiv-2512-24556 — "From a present-tense baseline of 45.8% safety, performance collapsed to 15.8% under past-tense framing"
[^c6]: arxiv-2512-24556 — "the models treat the former as benign history and the latter as dangerous"
[^c7]: arxiv-2512-24556 — "historical context signals educational intent, while future context signals prediction."
[^c8]: arxiv-2512-24556 — "they assume that if something is presented as history, it is likely harmless."
[^c9]: arxiv-2512-24556 — "further illustrate that simple temporal distance is"
[^c10]: arxiv-2512-24556 — "Because this asymmetry appears in all tested models regardless of training methodology"
[^c11]: arxiv-2512-24556 — "but represents only a fraction of the global linguistic and temporal"
[^c12]: arxiv-2512-24556 — "a random subset of 150 evaluations using GPT-4o as an independent judge."
[^c13]: arxiv-2512-24556 — "may be more effective for speculative harm than historical harm."
