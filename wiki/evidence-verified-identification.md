---
description: "In hidden-target questioning, a correct final guess splits into verified (the dialogue makes the target the unique top candidate) and unsupported; final accuracy alone overstates grounding."
aliases: ["Verified Correct accuracy", "random-guess correct", "model-relative trajectory verification"]
sources: ["arxiv-2603-28662"]
---
# Evidence-verified identification

In a hidden-target game (an oracle privately picks one image from a gallery of similar images; the model asks one Yes/No question per turn, within a 20-question budget), the final guess can be right for two different reasons. AMIGO separates them. A trajectory is *Verified Correct* only if the guess is right and a verification module returns the hidden target as the unique highest-scoring candidate. A right guess that fails this is *Random-Guess Correct*, and the two sum to the plain final-guess accuracy.[^c1]

## Mechanism

After each valid question-answer pair the module turns the exchange into a constraint and replays the question, in three paraphrases, on every remaining candidate image, using the same model that is being evaluated. A candidate is dropped only when its majority response is fully confident (all three paraphrases agree) and contradicts the oracle's answer. Candidates also accumulate an alignment score, so surviving candidates are ranked. If elimination would leave one or zero candidates before the last pair, the module rolls back to the previous set and only updates scores.[^c2] A trajectory passes if and only if the target is the unique top scorer; ties fail.[^c3]

The check is deliberately model-relative: it asks whether the model's own candidate-level judgments support its answer, and it is not independent proof that the visual judgment is correct.[^c4]

## What was measured

Five open VLMs were run on galleries at five similarity thresholds (mean gallery size 25.7 images at the loosest, 7.1 at the strictest). The gap between plain and verified accuracy is large and varies by model. For one model the verified accuracy fell sharply at the strictest threshold while plain accuracy stayed near 10%, because the verified decline was "partially offset by rising Random-Guess Correct accuracy".[^c5] The benchmark's conclusion is that final-answer accuracy alone overstates evidence-grounded performance, and that model scale does not guarantee reliable long-horizon interactive grounding.[^c6]

A related separation is protocol compliance. Invalid questions (prohibited attributes, multiple questions, repeated enumeration) return Skip and reveal nothing, so each one burns a turn from the budget. The Skip rate is therefore reported next to accuracy.[^c7]

## Limits

- The verifier reuses the evaluated model, so a model with poor visual discrimination can fail verification even when its guess was well reasoned, and a consistent but wrong belief can pass. Verification measures self-consistency with the oracle, not truth.
- One domain (dress galleries, with colour, pattern, sleeve and length questions banned) and five open models; whether the verified/unsupported split has the same size elsewhere is untested.
- Absolute verified accuracies are low (single digits to about 25%), so differences between weaker models rest on small counts; the paper gives bootstrap intervals but I did not read them in full.
- That verified trajectories reflect better question selection is the paper's reading; no ablation isolating question quality from visual accuracy was read here.

## Related

- [[twenty-questions]] — the game form; this note is about auditing whether a win came from the answers received
- [[verification-aware-stopping]] — also gates termination on evidence, but with a trained per-hop verifier rather than a replayed candidate set
- [[final-sufficiency]] — a stop decision tied to having enough evidence
- [[constraint-seeking]] — questions that prune the candidate set, which this verifier tracks
- [[expected-information-gain]] — the ideal criterion for choosing the next question, which these trajectories are not scored against

[^c1]: arxiv-2603-28662 — "Unverified Overall = Verified Correct + RandomGuess Correct."
[^c2]: arxiv-2603-28662 — "the module reverts to the previous feasible candidate set and stops applying further hard elimination."
[^c3]: arxiv-2603-28662 — "A trajectory passes verification if and only if MT = {x∗ }"
[^c4]: arxiv-2603-28662 — "It should not be interpreted as model-independent proof of visual"
[^c5]: arxiv-2603-28662 — "decline in Verified Correct is partially offset by rising Random-Guess Correct"
[^c6]: arxiv-2603-28662 — "final-answer accuracy alone overstates evidence-grounded performance"
[^c7]: arxiv-2603-28662 — "Because each invalid action consumes a turn while providing no attribute evidence, Skip exposes failures that final-answer metrics miss"
