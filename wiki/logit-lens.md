---
description: "Projecting an intermediate layer's hidden state through the output head yields a vocabulary distribution with no training, so the token a model leans toward before the last layer can be read."
aliases: ["logit lens", "unembedding projection of intermediate layers", "latent output decoding"]
sources: ["arxiv-2512-09555", "arxiv-2512-01909"]
---
# Logit lens

A decoder language model ends in an output head that maps the final hidden state to a score for every token in the vocabulary. The logit lens applies that same head to the hidden state of an earlier layer. Each layer then gives a readout of the tokens the network would emit if it stopped there. Nothing is trained for this: the readout uses the model's own head, so it asks what an intermediate state already points to, and it can do so layer by layer.[^c1]

In NLP the projection was used to map "weights and hidden states onto the language model’s vocabulary", as a way of seeing "the information flow within its internal layers".[^c2] Li et al. carry the same readout into blind image quality assessment, where the model's answer is a quality word and the readout asks which quality word each layer leans toward.[^c3]

Two choices carry the method across. The first is the layer. The authors decode "the outputs starting from the 30-th of 32 decoder layers", on the stated ground that "semantically meaningful information tends to emerge in the later layers".[^c4][^c5] The second is what is counted. At each decoded layer they look at the most probable next tokens, and over 300 samples classified as poor they "compute the token frequency distribution across intermediate layers".[^c6]

What the readout showed in that work. For one CSIQ image with a quality score of 0.416, the 30th-layer top token was “poor” while the output was “good” (Fig. 3 of the paper).[^c11] Across the sample, the one-stage model "demonstrates a sudden probability increase in the final layer", while the two-stage model "maintains a more stable probability distribution, allowing relevant tokens to emerge earlier in intermediate layers".[^c7][^c8] The abstract summarises this as a model that "often relies only on a limited set of candidate tokens".[^c9]

What survives the transfer. The readout compares a layer's state with the output vocabulary embeddings. It shows where that state lies in token space. By itself it does not show that the layer computed the answer, and that is the step the work takes when it reads a mid-layer leader as a source of instability. For a categorical output with a few candidates the readout is easy to read as a set of competing options. For free text the same readout would be a long, noisy distribution; the work does not test that case (my inference).

## Limits

- The lens is not validated in the work. No ground truth says what an intermediate state means, and no intervention checks that the 30th-layer top token drives the final output. The authors use the readout to observe a transition, not to test a cause.
- My inference: an intermediate state was never trained to be read through the final head, so its top tokens may reflect the head's geometry as much as the model's computation. The work does not test this.
- The layer range is the authors' choice, justified by a general remark about later layers, not by a sweep over layers.
- The quantitative part is a token-frequency distribution over 300 samples predicted as poor, from one backbone on one family of datasets. Fig. 3 is a single example. "Limited set of candidate tokens" summarises that distribution; it is not a separate measurement.
- A leader at a middle layer that loses at the output is not shown to be the correct answer. The authors treat the switch as a cause of "instability in final predictions"[^c10], but the readout alone does not say which of the two tokens is right.

## Related

- [[parametric-suppression]] — the same readout in knowledge conflicts, where the gold answer reaches rank 1 at mid-network and is lost by the output
- [[pre-committed-answer-before-cot]] — a trained linear probe reads the answer before the chain of thought; the logit lens needs no training and reads the model's own head at intermediate layers
- [[latent-debate]] — the same head-projection, read per layer as the True and False opinion of each hidden state, then weighed as supporting or attacking arguments.[^c12]

[^c1]: arxiv-2512-09555 — "To examine latent outputs, we utilize the language model’s head layer to predict the most probable next tokens based on the current state"
[^c2]: arxiv-2512-09555 — "researchers have employed projection techniques to map weights and hidden states onto the language model’s vocabulary, providing insights into the information flow within its internal layers"
[^c3]: arxiv-2512-09555 — "Inspired by this approach, we introduce a similar methodology to analyze the learning and inference mechanisms in our work"
[^c4]: arxiv-2512-09555 — "we decode the outputs starting from the 30-th of 32 decoder layers"
[^c5]: arxiv-2512-09555 — "semantically meaningful information tends to emerge in the later layers"
[^c6]: arxiv-2512-09555 — "compute the token frequency distribution across intermediate layers"
[^c7]: arxiv-2512-09555 — "which demonstrates a sudden probability increase in the final layer"
[^c8]: arxiv-2512-09555 — "maintains a more stable probability distribution, allowing relevant tokens to emerge earlier in intermediate layers"
[^c9]: arxiv-2512-09555 — "the language model often relies only on a limited set of candidate tokens"
[^c10]: arxiv-2512-09555 — "potentially leading to instability in final predictions"
[^c11]: arxiv-2512-09555 — "the most probable token is “poor” while the output token is “good”"
[^c12]: arxiv-2512-01909 — "and False, we can quantify the opinion of each latent"
