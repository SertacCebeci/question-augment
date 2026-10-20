---
description: "Code, specification, theorem and proof generated as linked artifacts can each pass a local check while drifting apart; the remedy tested is checks across the artifacts."
aliases: ["semantic drift", "cross-artifact drift", "multi-artifact consistency", "artifact drift in verified synthesis"]
sources: ["arxiv-2511-21104"]
---
# Coupled-artifact drift

Some verifiable outputs are not one object but several that must agree. In a proof assistant the answer is "executable code, specifications, theorem statements, and proof attempts," which "must remain mutually consistent."[^c1] The BRIDGE paper's name for the failure is semantic drift, and its claim is that treating the artifacts as independent makes it easy: "these artifacts independently makes semantic drift easy."[^c2]

The mechanism is that each artifact has its own local check, and the local checks do not see the links between artifacts. Code can pass its tests, a specification can typecheck, and a theorem can elaborate, while none of them states the property the code was meant to have. The paper gives the pattern in four cases: "a model can emit code that passes tests, a specification that typechecks but is vacuous, a theorem statement that looks correct but fails to capture the intended property."[^c2] Each piece is correct in its own terms. The mismatch is between the pieces.

The paper's response is to make the artifacts constrain each other rather than to check each one harder. It fixes an order, with code first, and uses "that implementation as a semantic anchor for specifications, theorem statements, and targeted proof attempts."[^c3] The later artifacts are then judged against the anchor. The effect is measured on the downstream artifacts: functional scaffolds "yield more Lean elaborating theorem statements" and more completed proofs aligned to the implementation.[^c4] Here "aligned" is the drift measure. A proof counts as drift-free when it is about the code the model wrote, and the paper's measures are of that kind: elaboration, plausibility, implementation relevance, and proof completion.

A consequence the paper states itself is that anchoring on the implementation can pull the proof toward the code rather than the task. "A completed proof can prove a statement that is too close to the implementation rather than the intended task."[^c5] So drift is not only the gap between artifacts. Too tight a link is also a failure, and the cross-artifact checks have to test for both. The code is an anchor that is not itself checked: "the intermediate program is a reasoning scaffold, not a certified source artifact."[^c6] (My inference: an error in the anchor carries into every artifact tied to it, and the paper's checks do not separate such a propagated error from a correct one.)

The concept is about a shared object across artifacts, not about any one of them. It is the reason the specification-side question of nonvacuity matters: a specification that is non-vacuous and discriminating is one of the artifacts whose agreement with the code can be tested.[^c7]

## Limits

The paper never defines a single drift quantity. Drift is read off several outcomes, each of which is a different check, and the text does not show that these outcomes move together beyond the reported tables. A reader who wants "drift" as one number will have to build it.

The paper also says what it does not do: "BRIDGE studies the front end of verified synthesis, not full semantic verification."[^c8] The evidence is about the front end, on mostly local algorithmic tasks, and the authors have "not yet tested BRIDGE on large formal libraries, rich stateful or effectful programs, long horizon proofs, or multi module verification."[^c9] The claim that cross-artifact checks reduce drift at scale is therefore not established.

The ordering is a finding for Lean in this paper, not a general rule. The authors write that "in Lean, we find an ordering that begins with code especially effective"[^c10], and they keep the three domains open to other orders. Whether code-first is best in other proof systems is untested here.

## Related

- [[specification-nonvacuity]] — the check that separates a specification with semantic bite from a vacuous one; one of the artifact-level tests that drift needs.
- [[declarative-formalization-style]] — another case where the intermediate program's form decides whether the formal output holds up; there the form is the solver's input rather than an anchor.
- [[generation-verification-gap]] — whether checking a proof is easier than producing one; a proof aligned to the implementation is a different target from a proof of the intended claim.
- [[verification-scope-granularity]] — checking a proof in narrow chunks catches errors a single read misses; a second way to make a linked check local enough to bite.

[^c1]: arxiv-2511-21104 — "must remain mutually consistent"
[^c2]: arxiv-2511-21104 — "these artifacts independently makes semantic drift easy"
[^c3]: arxiv-2511-21104 — "uses that implementation as a semantic anchor for specifications, theorem"
[^c4]: arxiv-2511-21104 — "Functional scaffolds yield more Lean elaborating theorem statements"
[^c5]: arxiv-2511-21104 — "a statement that is too close to the implementation rather than the intended task"
[^c6]: arxiv-2511-21104 — "program is a reasoning scaffold, not a certified source artifact"
[^c7]: arxiv-2511-21104 — "A specification that compiles is not necessarily meaningful."
[^c8]: arxiv-2511-21104 — "BRIDGE studies the front end of verified synthesis, not full semantic verification"
[^c9]: arxiv-2511-21104 — "rich stateful or effectful programs, long horizon proofs, or multi module verification"
[^c10]: arxiv-2511-21104 — "that begins with code especially effective"
