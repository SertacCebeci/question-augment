---
description: "The expressiveness of a token language is the set of meanings its tokens and grammar can encode; the paper argues that this set caps how much chain-of-thought a model can use."
aliases: ["expressive capacity of natural language tokens"]
sources: ["arxiv-2512-20954"]
---
# Language expressiveness

A language, in the paper's formalization, is a pair L = (G, V): a grammar G that says which token sequences are valid, and a vocabulary V of usable tokens. "The set of all meanings expressible (valid sequences) in language L" is written S_L, and the expressiveness of L is the cardinality of that set.[^l1] Because S_L is usually infinite, the cardinality cannot rank two languages by itself. The paper compares them by inclusion instead: "languages can still be meaningfully compared," and if one meaning set is a strict subset of another, the larger language is strictly more expressive.[^l2] Natural languages such as English and Chinese are not ranked against each other under this rule, since each carries meanings the other lacks. The amino-acid language is shown to sit far below them: a sentence such as "I am wrong" has "no meaningful expression" in the protein vocabulary.[^l3]

The reason this matters is chain-of-thought (CoT). The paper treats a model's hidden state as the latent language: information that the trained network can hold. CoT decodes parts of that hidden state into non-answer tokens drawn from the same vocabulary, which serve as memory and intermediate steps. The tokens "are discretized, verbalized, tokenized, or quantized forms of internal information" in the hidden state.[^l4] The paper's section heading states the consequence: "Language expressiveness determines CoT expressiveness."[^l5] If the vocabulary cannot name a reflection such as "I made a mistake," the hidden state's information about that mistake has nowhere to go. Direct answer generation has the same limit from the other side: "as the number of answer tokens is inherently constrained, thereby capping" the computation the model can express.[^l6] For amino-acid models the paper concludes that "the CoT expressiveness with Biological sequence models is practically 0."[^l7]

The formal layer carries over from formal language theory: a language is a grammar plus a vocabulary, and comparison is by inclusion of the sets of meanings. What the transfer does not supply is a measure of the meanings. The paper never counts the meanings an amino-acid sequence can carry, so "practically 0" is a statement about how the authors read the vocabulary, not a number. Their remedy is to enlarge the vocabulary with one reflection token, and they say the augmented set "significantly enhances the biological language expressiveness" — the test of the claim is therefore the reflection experiment in [[reflection-token-error-injection]], not the definition itself.[^l8]

## Limits

- The main text I read gives the definition and the argument; the formal results on Turing completeness and the computational power of CoT are in an appendix I did not read. The claim that the expressiveness ordering bounds reasoning rests on those results, which this note has not checked (my inference).
- The cardinality |S_L| is infinite for any language with unbounded sequences, so the single number the definition names carries no information. Only inclusion ranks languages, and it is often silent: two languages can be incomparable, as the paper says of English and Chinese (my inference from the definition).
- "Practically 0" is asserted for protein models. No measurement of expressiveness in a biological model appears in the text I read, and the paper does not separate expressiveness from the training data or the model size.
- The link from a larger vocabulary to better reasoning is shown only for one task, de novo peptide sequencing, with one added token. Whether the same holds for other token sets is untested here.

## Related

- [[reflection-token-error-injection]] — the paper's test of the claim: a reflection token added to the amino-acid vocabulary, after which the model is trained to correct its own tokens.
- [[two-stage-decision-sampling]] — the decision to revise an earlier output, which is the step a reflection token would have to express; the other note reads self-correction as a decision stage, not as wording.

[^l1]: arxiv-2512-20954 — "The set of all meanings expressible (valid sequences) in language L"
[^l2]: arxiv-2512-20954 — "languages can still be meaningfully compared"
[^l3]: arxiv-2512-20954 — "have no meaningful expression in Sprotein"
[^l4]: arxiv-2512-20954 — "they are discretized, verbalized, tokenized, or quantized forms of internal information"
[^l5]: arxiv-2512-20954 — "Language expressiveness determines CoT expressiveness"
[^l6]: arxiv-2512-20954 — "as the number of answer tokens is inherently constrained, thereby capping"
[^l7]: arxiv-2512-20954 — "the CoT expressiveness with Biological sequence models is practically 0"
[^l8]: arxiv-2512-20954 — "our augmented token set significantly enhances the biological"
