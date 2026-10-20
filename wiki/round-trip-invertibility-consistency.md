---
description: "Passing a forward task and its inverse separately does not show understanding; requiring the inverse to reconstruct the original input exactly exposes inconsistency that one-direction accuracy hides."
aliases: ["round-trip consistency", "bijection fidelity", "code invertibility test", "RoundTripCodeEval"]
sources: ["arxiv-2601-13398"]
---
# Round-trip invertibility consistency

A model that answers a question in one direction may not hold a coherent model of the thing asked about. Maveli, Vergari and Cohen test this on code: the model must predict an encoder's output and also a decoder's output, and the pair must close the loop, with the final reconstruction equal to the original input.[^c1]

## Mechanism

The test is built on lossless compression (four algorithms; RLE, LZW, arithmetic encoding, Huffman). Four tasks are scored: output prediction with the encoder, input prediction with the decoder, and the two "inversion" variants, where the model must construct the inverse of a function and apply it. The check is exact identity, not semantic equivalence: "lossless compression requires exact data identity."[^c2] This is deliberately stricter than natural-language round trips (code to description to code), which accept any behaviourally equivalent output.[^c3]

The argument for why this exposes more than forward accuracy: forward execution "can often be solved through surface-level pattern matching, memorisation, or statistical correlation", whereas inversion needs a consistent internal execution model.[^c4] The authors' reading is that a failure to close the loop shows forward correctness was fragile.[^c5]

Measured results: the abstract reports that models "frequently pass individual forward and backward tasks yet fail the combined round-trip", and that failures persist on simple bijections such as RLE.[^c6] Across models the ordering is consistent: output prediction highest, then output prediction with inversion, then input prediction, with input prediction with inversion lowest, which the authors say compounds errors.[^c7]

Two repairs were tried. Self-reflection (critique then revision) helps most on inversion tasks in the first round, then plateaus: "sharply diminishing returns", which the authors read as unaided self-critique being unable to fix systematic state-tracking or inversion errors.[^c8] Fine-tuning QwQ-32B on execution traces lifted forward tasks (RLE 80.0%, LZW 87.5%, AE 78.6% Pass@5) but inverse gains were uneven: AE inversion fell to 30.8% and Huffman encoding stayed at 0%.[^c9]

Why inversion is not trivial in general: any function A(x)=z can be wrapped as B(x)=(x,A(x)); inverting B is trivial, but inverting the checking function C(x,z) amounts to solving A.[^c10] So round-trip tests only fit problems where the inverse exists.

## Limits

- Scope is Python code on four compression algorithms with 250 inputs each; transfer to question-asking or answering is this wiki's inference, not tested. The analogy (a question and its recovered paraphrase as an encode/decode pair) loses exactness: natural language has no bijection, which is why exact identity cannot be required there.
- The interpretation (lack of "internal coherence", inability to "maintain and invert evolving algorithmic state") is the authors' hypothesis; the experiments show the gap, not its cause. They rule out one tokenizer as explanation by comparing models, but not other confounds.
- SFT used only 87-98 traces per algorithm and one model, so its failure may reflect small data.
- Self-reflection had no external execution feedback; the saturation may not hold with grounded feedback, as the authors themselves note.

## Related

- [[recovered-question-check]] — a conjectured natural-language analogue: recover the question a draft answers and compare with the received one

[^c1]: arxiv-2601-13398 — "evaluates round-trip consistency through execution-free, exact-match"
[^c2]: arxiv-2601-13398 — "lossless compression requires exact data identity."
[^c3]: arxiv-2601-13398 — "only require semantic equivalence"
[^c4]: arxiv-2601-13398 — "Forward execution can often be solved through"
[^c5]: arxiv-2601-13398 — "indicate that forward correctness was fragile"
[^c6]: arxiv-2601-13398 — "models frequently pass individual forward and backward tasks yet fail the combined round-trip,"
[^c7]: arxiv-2601-13398 — "consistent hierarchy: O/P Pred > O/P Pred-I > I/P Pred > I/P Pred-I."
[^c8]: arxiv-2601-13398 — "sharply diminishing returns"
[^c9]: arxiv-2601-13398 — "while AE collapses to 30.8% and Huffman encoding remains at 0%"
[^c10]: arxiv-2601-13398 — "Inverting B(x) into C(x, z) is algorithmically trivial"
