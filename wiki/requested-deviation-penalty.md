---
description: "A preference-trained image scorer ranks an output that follows an explicit request for an unappealing look below a conventional one, sometimes below chance on the instructed pair."
aliases: ["over-alignment", "reward-model penalty on instructed deviation", "anti-aesthetic penalty"]
sources: ["arxiv-2512-11883"]
---
# Requested-deviation penalty

A reward model is trained to rank outputs by general appeal. The question here is what it does when the prompt itself asks for an output that is not appealing: blur, clashing colour, a negative emotion, deliberate low quality. The paper calls this "wide-spectrum aesthetics", images "intentionally generated to deviate from dominant aesthetic conventions".[^c1] A scorer that reads the instruction correctly should prefer the image that carries it. The paper's finding is that many do not, and that the scorer prefers the conventional image even when the prompt names the deviation.

The test is a pair. For each base caption, an image is generated from the plain prompt and one from the anti-aesthetic prompt, and the scorer is asked which fits the anti-aesthetic prompt better. The control matters. Unaligned BLIP and CLIP pick the instructed image correctly, which the paper reads as showing "that complex prompt understanding is not the underlying issue but rather biased alignment".[^c2] The preference-trained scorers do worse. HPSv3 is "sometimes worse than random guessing".[^c3] My reading of the paper's Table 3 puts HPSv3 at accuracy 0.381 on this pair task, below the 0.5 of chance, against 0.913 for CLIP-L and 0.965 for BLIP-L. So the inversion is specific to the preference training, not to the scorer's architecture or its reading of language.

The same pattern shows up in a controlled edit. One happy image is edited into sad, angry and fearful versions with everything else held fixed. HPSv3 "consistently assigned higher scores to the positive emotion images",[^c4] and the paper summarises that the reward models "are very opinionated against negative emotions".[^c5] Real photographs show it too. Professionally anti-aesthetic AVA photographs are scored below clean AI images that were generated from clean captions, and the paper's Figure 6 says this holds "even when the prompt explicitly requests anti-aesthetic elements".[^c6] On a second check, HPSv3 "rates the clean image 5.90 points higher on average".[^c7] Real paintings from the LAPIS set are penalised in the same way, and the paper reads this as a choice rather than a failure to see: "Reward models could thus understand the content but choose to".[^c8] A BLIP score of 0.996 on the matched image-caption pairs, dropping to 0.086 when shuffled, supports that the scorer does see the content.[^c9]

The generators inherit the lean. Base models "can do reasonably well on anti-aesthetics generations",[^c10] while the strongly aesthetics-tuned DanceFlux produces the requested image "about 64% of the time" as often or less than the plain one.[^c11] On negative emotions it "consistently executed happy prompts but failed on most negative emotions".[^c12] The paper names the whole direction "reversed alignment": the system is aligned to an averaged preference and, through use, the user is aligned to that preference.[^c13] That second half is argued, not measured.

The mechanism, then, is a single prior that is trained into the scorer and then used to rank outputs against the very instruction it is asked to check. The prior does not need to be wrong about what people usually like. It only needs to outrank the explicit request, and in the measured cases it does.

## Limits

- The paper is a position paper. The terms "reversed alignment" and "aesthetic authoritarianism" are its argument; the measurements cover image pairs, emotion edits, real photographs and paintings, not the harm the authors describe.[^c13]
- Images only. The paper does not test text answers, and nothing in the read sections shows that a judge of answers behaves the same way (see the inference below).
- The judging model in the per-dimension test is a 4B model the authors fine-tuned: "we fine-tuned Qwen/Qwen3-VL-4B-Instruct on the VisionReward dataset".[^c14] The LLM ground truth for which image fits the prompt is validated by humans, but "only a filtering stage for the reward-model benchmark" for the reward-model pairs.[^c15]
- Sample size is small: "A random subset of 300 base prompts from COCO was selected".[^c16] The emotion test uses 120 prompts across four emotions.
- The concept is scoped to deliberate deviation: "This notion excludes unintended model errors and does not imply unsafe content".[^c17] Where a deviation is an actual error, the penalty is correct, and the paper does not claim otherwise.
- The paper's counter-position is that "a default experience pleasing the majority is a pragmatic design choice",[^c18] and it answers that only clarity is a technical flaw among its dimensions. That rebuttal is the authors', not tested against users.
- The anti-aesthetic label on real photographs comes from AVA category labels and an LLM-curated dataset, not from a rater reading each photograph.

My inference, not tested in the paper: a judge of answers that has a general-appeal prior could penalise an answer that obeys an unusual form the asker set, such as a deliberately terse or hostile reply. The paper gives no evidence on text, so this stays a conjecture.

## Related

- [[personal-rubric-reward-gap]] — the nearest measure: a reward model reaches only 75.94% when the difference is one user's rubric; here, on an explicit deviation, the general prior scores below chance. A weak judge is noise; an inverted one rewards the answer the asker did not want.
- [[default-tone-skew]] — the text-side counterpart of the positive lean: neutral replies lean polite, and the image scorer leans toward positive emotion.
- [[custom-instruction-adherence-audit]] — auditing whether a model keeps a user's custom instruction; the same instruction-following question, asked of a chat model rather than a scorer.

[^c1]: arxiv-2512-11883 — "generated to deviate from dominant aesthetic conventions"
[^c2]: arxiv-2512-11883 — "indicating that complex prompt understanding is not the underlying issue but rather biased alignment"
[^c3]: arxiv-2512-11883 — "sometimes worse than random guessing (HPSv3)"
[^c4]: arxiv-2512-11883 — "yet HPSv3 consistently assigned higher scores to the positive emotion images"
[^c5]: arxiv-2512-11883 — "reward models are very opinionated against negative emotions"
[^c6]: arxiv-2512-11883 — "even when the prompt explicitly requests anti-aesthetic elements"
[^c7]: arxiv-2512-11883 — "HPSv3 rates the clean image 5.90 points higher on average"
[^c8]: arxiv-2512-11883 — "Reward models could thus understand the content but choose to"
[^c9]: arxiv-2512-11883 — "got 0.996; shuffling captions and images dropped this to 0.086"
[^c10]: arxiv-2512-11883 — "Base models can do reasonably well on anti-aesthetics generations"
[^c11]: arxiv-2512-11883 — "about 64% of the time, Ia performs the same or worse"
[^c12]: arxiv-2512-11883 — "consistently executed happy prompts but failed on most negative emotions"
[^c13]: arxiv-2512-11883 — "We named this reversed alignment."
[^c14]: arxiv-2512-11883 — "Qwen/Qwen3-VL-4B-Instruct on the VisionReward"
[^c15]: arxiv-2512-11883 — "only a filtering stage for the reward-model benchmark"
[^c16]: arxiv-2512-11883 — "A random subset of 300 base prompts from COCO was selected"
[^c17]: arxiv-2512-11883 — "This notion excludes unintended model errors and does not imply unsafe content"
[^c18]: arxiv-2512-11883 — "a default experience pleasing the majority is a pragmatic design choice"
