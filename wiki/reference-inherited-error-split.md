---
description: "A tool-augmented answer's error against truth splits into a pipeline residual (answer minus tool output) and an inherited residual (tool output minus truth); measuring both locates the fault."
aliases: ["agent-vs-database residual", "pipeline fidelity residual", "residual decomposition of tool error"]
sources: ["arxiv-2512-11935"]
---
# Reference-inherited error split

A tool-augmented answer can be wrong for two different reasons, and they can be measured apart. The first is pipeline error: the value the model reports differs from the value its tool returned. The second is inherited error: the tool's value differs from the truth. The first belongs to the answerer; the second belongs to the reference the tool reads. In the AGAPI platform for materials prediction the paper writes three values, Vagent (the agent's report), Vdb (the database entry the tool retrieves) and Vexp (the experimental reference). The total error then decomposes as Vagent − Vexp = (Vagent − Vdb) + (Vdb − Vexp). The first term is "the agent-vs-database residual", which the paper reads as agentic pipeline fidelity; the second is the database-vs-experiment residual, which it reads as inherited DFT functional bias.[^r1]

The split answers a question an aggregate error hides: whether a tool-augmented score worse than the tool-free baseline is the agent's doing or the database's. The authors state the aim as separating "agent pipeline fidelity from inherited density functional theory" error.[^r2]

## What it found

The split gives different answers for different properties. Where the agent forwards the database entry, all error is inherited. The abstract reports that the agent "reproduces JARVIS-DFT entries to numerical precision" for bulk modulus and bandgap.[^r3] For bandgap, "the agent-vs-database residual is zero", so the 0.495 eV error against experiment is carried entirely by the database.[^r4] The paper gives the same reading for bulk modulus, where the 5.73 GPa error is inherited.[^r5]

For superconducting Tc (n = 13) the pipeline share is not zero. The agent sometimes replaces the retrieved DFT electron–phonon value with a value from its parametric memory.[^r6] The reported numbers are 3.38 K inherited, 3.56 K from the agent, 5.77 K total, and "both sources contribute comparably".[^r7] The paper reads the replacement as sometimes helpful: "that memorized value is often closer to" experiment than the DFT estimate, for canonical superconductors.[^r8] So the pipeline term can lower the error as well as raise it, and only the split shows which.

The inherited term depends on the functional stored in the database, not on the agent. With the agent held fixed, the bandgap error against experiment was 1.42 eV against OptB88vdW (n = 50), 0.48 eV against MBJ (n = 53) and 0.27 eV against HSE06 (n = 6). Switching the reference "from OptB88vdW to HSE06 reduces the experimental-reference error by" about a factor of five.[^r9]

What survives the transfer is the arithmetic and the requirement behind it. The pipeline term needs the tool's output recovered independently of the answer, and the inherited term needs a truth to compare against. Where no experimental reference exists, the inherited term cannot be computed and the split reduces to the pipeline term alone. That reduction is my inference, not something the paper tests.

## Limits

- The pipeline term is measured against the tool's own output. It measures whether the value was forwarded faithfully, not whether the value asked for was the right one. A faithful forward of the wrong question is a different failure, described by [[wrong-goal-execution]], and the split does not see it.
- The pipeline comparison covers only "on the subset of materials where Vagent could be" reliably extracted from the agent's natural-language reply.[^r10] The samples are small: bulk modulus n = 21, bandgap n = 54 (with the database value retrieved for 53), Tc n = 13. The Tc finding rests on 13 materials.
- The split locates error relative to one retrieved reference. It does not establish that the reference is the right one for the question. The functional comparison shows that this choice alone moved the inherited term by about a factor of five.
- The paper proposes using the split to decide when to call a tool. It says the agent "should invoke a database tool when the expected database-vs-experiment residual for the target" property is smaller than the expected parametric error, and it expects that "adaptive selection will outperform both always-use-tools" and never-use-tools strategies.[^r11] That is a proposal; the paper reports no test of it.
- The split needs an experimental reference for each material. Materials and properties without one get no inherited term, and the paper's comparison covers only the JARVIS-Leaderboard sets it chose.

## Related

- [[uncertainty-guided-retrieval-triggering]] — the decision made before the call: whether to consult a tool at all, rather than how far a returned value can be trusted
- [[version-dependent-judge-error]] — the same worry about a reference that is not ground truth, here in grading rather than in tool output
- [[wrong-goal-execution]] — a tool path can be forwarded faithfully and still answer the wrong question, which the split cannot detect

[^r1]: arxiv-2512-11935 — "the agent-vs-database residual"
[^r2]: arxiv-2512-11935 — "agent pipeline fidelity from inherited density functional theory"
[^r3]: arxiv-2512-11935 — "the agent reproduces JARVIS-DFT entries to numerical precision"
[^r4]: arxiv-2512-11935 — "the agent-vs-database residual is zero"
[^r5]: arxiv-2512-11935 — "so any error against experiment originates in the database"
[^r6]: arxiv-2512-11935 — "the agent sometimes replaces the retrieved DFT"
[^r7]: arxiv-2512-11935 — "both sources contribute comparably"
[^r8]: arxiv-2512-11935 — "that memorized value is often closer to"
[^r9]: arxiv-2512-11935 — "retrieved reference from OptB88vdW to HSE06 reduces the experimental-reference error by"
[^r10]: arxiv-2512-11935 — "on the subset of materials where Vagent could be"
[^r11]: arxiv-2512-11935 — "anticipate that adaptive selection will outperform both always-use-tools"
