---
description: "A round trip through one's own implementation can pass while the output is wrong; checking outputs against a separate implementation exposes shared encoding and context mistakes."
aliases: ["interoperability check", "cross-implementation verification", "independent interoperability oracle"]
sources: ["arxiv-2512-12989", "arxiv-2512-10159", "arxiv-2511-21382"]
---
# Independent implementation check

A program can pass its own tests and still fail a second implementation of the same standard. In a migration from RSA to ML-DSA, the application signs, the application verifies, and the two agree; the fault appears only when a separate verifier reads the output. The paper's recorded example is a key format: the application wraps packed key bytes in PEM and reads them back with a matching loader. "Local signing and verification pass, but OpenSSL rejects the files because the required key structures are missing."[^c1] The mistake sits in a convention that both halves of the round trip share, so agreement between the halves cannot reveal it.

The mechanism is the independence of the other party. The checker "exchanges keys and signatures across implementations under a declared application contract"; it runs the application as a subprocess and imports none of its code.[^c2] It requires agreement in both directions under one contract: the candidate must verify the independent side's signatures, and the independent side must verify the candidate's. "Both directions, under the same contract" is the paper's own summary.[^c3] A context error that a self round trip cannot see becomes visible here, because the independent verifier applies the context the contract requires and the candidate's own code does not. The observable is acceptance and rejection, not signature bytes, since the scheme is randomized: "the relevant observations are successful key loading, acceptance of valid signatures, and rejection of invalid ones, rather than identical signature bytes."[^c4]

What it changed in the measurements: across the four local configurations, twelve final patches passed the local round trip and failed external requirements. For the Qwen3-Coder comparison alone, "the common local round trip would accept eight final patches that the contract-based evaluation rejects."[^c5] Which patches count as complete depends on whether the independent side is consulted.

The general point is about where agreement comes from. A closed loop through one implementation shows that its two halves share a convention, not that the convention is the one the standard requires. An outside implementation can disagree with a convention the producer never questioned. The paper states the division of labour directly: "Independent checks expose errors that local round trips miss, but diagnostics alone need not supply the knowledge or editing strategy needed for repair."[^c6] The check finds the error; it does not by itself repair it.

The same shape appears in model self-consistency. [[round-trip-invertibility-consistency]] shows that a forward and an inverse task can each pass while the combined loop fails; the independent check closes the loop through a second party instead of through the model's own inverse. Where judges share errors, a common residual makes agreement uninformative in the same way: [[accuracy-error-correlation-coupling]] and [[shared-error-pattern]] describe that failure among judges. The paper itself places an agent guided by independent implementations, Chai's agentic differential testing, as "closely related to our feedback setting."[^c7]

A numerical simulator can serve as the independent party when the output is a number. In a study of undergraduate circuit problems, the model's final answer was compared with the answer from an ngspice netlist that the model wrote from the same problem text. Where the circuit was read correctly the two answers match, and the match carries the check. Where the reading itself was wrong, both halves inherit it, and the check passes wrongly: the paper's example is a case where "they produced matching but incorrect solutions."[^c11] A mismatch is the useful outcome. In the first trial the simulator flagged 11 of the 12 wrong model answers, and the mismatches were sent to retries and then to a person, so that the proofreader was "required to review only 12 circuit diagrams and examine 5 + 17 = 22" solutions.[^c12][^c13] The flag is the check's output; it does not say which half was wrong.

Software test generation uses the same idea under the name differential testing. When the expected output is hard to write down, a second implementation or a second version of the program can stand in for it: "Differential testing supplies a pseudo-oracle when a comparison implementation or version is available."[^c14] The cost moves to interpreting disagreement. The review's warning is that "discrepancies require triage, and conclusions depend on the comparison target".[^c15] An independent check is only as informative as the party it checks against, so the question becomes how far the second implementation can be trusted, not only whether the two agree.

## Limits

- One external implementation. "OpenSSL is the only external implementation," so agreement with it is a single witness. Two implementations that share a misreading of the standard would still agree; this was not tested.[^c8]
- One task. "The study covers one Go file signer and one ML-DSA parameter set."[^c9] The check was built for this contract; how to build an independent oracle for an arbitrary task is not addressed.
- Passing is not conformance. "neither a local pass nor a full checker pass would establish FIPS conformance, side-channel resistance, or deployment safety."[^c10] The outcome is contract compliance, not exploitability.
- Access is not repair. The paper reports that an external diagnostic can be received and followed by edits that leave the failure unresolved; see [[agentic-iteration-gap-under-localized-verifier-feedback]] for the access-versus-delivery question.[^c6]
- Transfer to answering is my inference, not the paper's. Question answering has no byte-exact second implementation, so the exactness that makes this check strong here is absent. What may carry over is the structural point: a verifier that shares the answerer's conventions cannot expose a mistake those conventions hide.

## Related

- [[round-trip-invertibility-consistency]] — a closed loop within one model can pass in parts and fail combined; the independent check closes the loop through a separate party
- [[accuracy-error-correlation-coupling]] — correlated errors make agreement among checkers weaker evidence than their number suggests
- [[shared-error-pattern]] — the same failure among judge banks: errors shared by most judges
- [[agentic-iteration-gap-under-localized-verifier-feedback]] — localized feedback from a deterministic verifier lifts agent success; here the verifier's availability alone did not

[^c1]: arxiv-2512-12989 — "OpenSSL rejects the files because the required key structures are missing."
[^c2]: arxiv-2512-12989 — "exchanges keys and signatures across implementations under a declared application contract"
[^c3]: arxiv-2512-12989 — "Both directions, under the same contract"
[^c4]: arxiv-2512-12989 — "the relevant observations are successful key loading, acceptance of valid signatures, and rejection of invalid ones, rather than identical signature bytes"
[^c5]: arxiv-2512-12989 — "Thus, the common local round trip would accept eight final patches that the contract-based evaluation rejects."
[^c6]: arxiv-2512-12989 — "Independent checks expose errors that local round trips miss, but diagnostics alone need not supply the knowledge or editing strategy needed for repair."
[^c7]: arxiv-2512-12989 — "Its use of independent implementations to guide an agent is closely related to our feedback setting."
[^c8]: arxiv-2512-12989 — "OpenSSL is the only external implementation"
[^c9]: arxiv-2512-12989 — "The study covers one Go file signer and one ML-DSA parameter set."
[^c10]: arxiv-2512-12989 — "neither a local pass nor a full checker pass would establish FIPS conformance, side-channel resistance, or deployment safety"
[^c11]: arxiv-2512-10159 — "they produced matching but incorrect solutions"
[^c12]: arxiv-2512-10159 — "ngspice successfully flagged 11 of these cases by producing different"
[^c13]: arxiv-2512-10159 — "required to review only 12 circuit diagrams and examine 5 + 17 = 22"
[^c14]: arxiv-2511-21382 — "Differential testing supplies a pseudo-oracle when a comparison implementation or version is available."
[^c15]: arxiv-2511-21382 — "discrepancies require triage, and conclusions depend on the comparison target"
