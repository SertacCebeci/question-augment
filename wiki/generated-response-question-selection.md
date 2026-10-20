---
description: "Pick the next question by sampling the respondent's predicted open-ended answers from a generative model and scoring their uncertainty, diversity or Fisher information, not a binary correctness."
aliases: ["generative computerized adaptive testing", "CodeGENCAT", "generative CAT", "response-simulation question selection"]
sources: ["arxiv-2602-20020"]
---
# Generated-response question selection

Classical adaptive testing scores each candidate question by the predicted probability of a correct answer; under 1PL IRT the information is largest near 0.5. The source argues this "compresses each student response into a binary" label and so discards why a response is wrong.[^c1] Generated-response selection keeps the loop (estimate knowledge, choose a question, observe, update) but changes what is scored: for each candidate, a generative model of the respondent, conditioned on the current knowledge estimate, samples N predicted open-ended answers, and the question is scored on those samples.[^c2]

## Mechanism (CodeGENCAT, programming education)

- Knowledge is a low-dimensional latent vector mapped to per-skill mastery levels; mastery enters an LLM prompt as an interpolated embedding between "TRUE" and "FALSE" tokens, and the LLM generates the student's code.[^c3]
- Training is supervised fine-tuning plus an alignment loss tying mean mastery on the question's skills to correctness. The authors report that SFT alone "suffers from mode collapse", ignoring the knowledge input, so a preference-optimization stage follows.[^c4]
- Three scores over the N sampled answers: uncertainty (mean predicted correctness near 0.5), diversity (low pairwise cosine similarity of code embeddings, read as the model being unsure how the student would answer), and Fisher information (trace of the information matrix, equal to the squared gradient norm of the sample log-likelihood with respect to the latent knowledge).[^c5][^c6] The Fisher variant is the [[fisher-information]] quantity taken over a latent knowledge vector rather than a scalar ability.
- After the real answer is observed, only the student's latent vector is updated by gradient descent; the model stays fixed.[^c7]

## What was measured

On two programming datasets (Java and Python), knowledge estimates were judged by how well the chosen questions let an IRT model predict held-out answers. The method beat 1PL IRT, BOBCAT, NCAT and LACAT, particularly early in the test.[^c8] The best of the three scores depends on dataset and stage; diversity did best at very short test lengths on one dataset.[^c9]

## Limits

- Evaluation is a proxy: true knowledge is unobservable, so accuracy of predicting held-out correctness stands in for it. Gains were largest in early steps and narrow as all methods converge.
- Only two programming datasets, one small backbone model, and 1PL IRT as the final predictor; whether this carries to non-code open-ended answers is untested here.
- Which score wins is not settled; the reason diversity helps early (estimate near the prior) is the authors' interpretation, not a tested mechanism.
- The generative model is itself trained on the student population, so selection inherits its biases; the sampling cost per candidate is not analysed in what I read.
- This is about choosing questions to estimate a respondent's state, not about the asker's own uncertainty; the transfer to an asker querying a user is my inference.

## Related

- [[fisher-information]] — the information score used by one variant
- [[next-best-question]] — the general selection problem this instantiates
- [[candidate-set-entropy-question-selection]] — another uncertainty-based scorer, over hypotheses rather than predicted answers
- [[particle-approximated-eig-selection]] — also scores questions via sampled simulated answers

[^c1]: arxiv-2602-20020 — "IRT compresses each student response into a binary"
[^c2]: arxiv-2602-20020 — "selects questions using predicted student code responses"
[^c3]: arxiv-2602-20020 — "This soft prompting approach enables the LLM to"
[^c4]: arxiv-2602-20020 — "from mode collapse, generating semantically identical responses for some questions regardless of the"
[^c5]: arxiv-2602-20020 — "This algorithm selects the question with the most semantically diverse set of generated responses."
[^c6]: arxiv-2602-20020 — "equivalent to the squared ℓ2 norm of the gradient."
[^c7]: arxiv-2602-20020 — "while keeping the GIRT"
[^c8]: arxiv-2602-20020 — "particularly during the early, most important phase of CAT (t from 1 to 7)"
[^c9]: arxiv-2602-20020 — "the best selection algorithm depends on both the dataset and"
