---
description: "Routing exploration and proof to different models: in one IMO 2025 case GPT-5 found the answer but failed the proof, while Gemini proved a given answer, a confounded single case."
aliases: ["model orchestration", "multi-model orchestration", "model specialization", "phase-wise model routing"]
sources: ["arxiv-2512-19287", "arxiv-2512-04695"]
---
# Model orchestration

Model orchestration assigns different phases or subtasks of one problem to different models, chosen for each model's observed strength on that phase, instead of running a single model from start to finish. In the Vibe Reasoning case study the split was exploration to one model and rigorous proof to another. The authors put it as: "GPT5 excels at exploration while Gemini 3 Pro excels at rigorous proof."[^m1]

The observation behind the split comes from two traces. In a GPT-5-only run, "Answer discovery succeeded, but proof attempts failed repeatedly."[^m2] The authors also ran Gemini 3 Pro on the proof with the answer supplied: the trace is labelled "Gemini 3 Pro proof trace (given answer from GPT-5)", and it reached a complete proof using a Fooling Set approach.[^m3] In the other direction, when Gemini was asked for the answer directly, "it converged on the incorrect formula" (the paper's own phrasing is "When asked to find the answer directly, it converged").[^m4] Each model was therefore strong where the other was weak, which the paper summarizes as "Different models have complementary strengths; no single model excels at all phases."[^m5]

The switch itself is a human decision in the paper's account. "The decision to switch models reflects human judgment about when exploration should yield to rigorous proof," and the authors treat that judgment as meta-level, requiring no problem-specific knowledge.[^m6] What the principle carries over is the idea that the boundary between phases, here "answer found, now prove it", is the natural place to change the component doing the work. What does not carry over from this case is any claim about which model is better at which task in general; the paper's Table 3 rates capabilities only as "Strong", "Moderate" or "Weak", with no scores.

The paper also reports a cost. Its early exploratory trace shows "frequent context loss across model switches", so a switch is not free and has to be paired with persistent external notes.[^m7]

## Limits

The comparison is confounded. The Gemini proof was produced with the answer already in hand, so the success measures a proof task with a known target, not the same task the GPT-5 trace attempted. The paper's label "given answer from GPT-5" marks this, but the text does not run Gemini on the unassisted proof task in a way that isolates model strength from the supplied answer.

The evidence is two models on one problem from one set of authors. The paper itself says that "simple problems may not need model orchestration if a single model suffices."[^m8] Its claim that "Neither model alone could have achieved the complete solution" is a conclusion from these traces, not a measured result across tasks.[^m9]

Routing is done by hand. The paper says the human judgment about when and where to switch is what makes it work, and whether that judgment can be automated is left open. No automated router is tested here. A later work tests one: a small trained coordinator "learns to orchestrate a pool of external LLMs" and assigns each call a role, and it reports gains over single models on benchmarks, though not on a single problem.[^m10] See [[learned-model-coordinator]].

The capability table is qualitative and was drawn from this one case, so it describes two systems at one time, not their stable profiles.

## Related

- [[compound-ai-systems]] — the general idea of a system built from several components; model orchestration is one choice about which component does which phase.
- unreliable-self-evaluation — the paper's reason a second source of judgment helps: the same model cannot reliably check its own claims.

[^m1]: arxiv-2512-19287 — "GPT5 excels at exploration while Gemini 3 Pro excels at rigorous proof"
[^m2]: arxiv-2512-19287 — "Answer discovery succeeded, but proof attempts failed repeatedly"
[^m3]: arxiv-2512-19287 — "Gemini 3 Pro proof trace (given answer from GPT-5)"
[^m4]: arxiv-2512-19287 — "When asked to find the answer directly, it converged"
[^m5]: arxiv-2512-19287 — "Different models have complementary strengths; no single model excels at all phases"
[^m6]: arxiv-2512-19287 — "The decision to switch models reflects human judgment about when exploration should yield to rigorous proof"
[^m7]: arxiv-2512-19287 — "frequent context loss across model switches"
[^m8]: arxiv-2512-19287 — "not need model orchestration if a single model suffices"
[^m9]: arxiv-2512-19287 — "Neither model alone could have achieved the complete solution"
[^m10]: arxiv-2512-04695 — "that learns to orchestrate a pool of external LLMs"
