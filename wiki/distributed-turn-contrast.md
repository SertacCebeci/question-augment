---
description: "Preference pairs that differ only in the final turn give a reward model little signal about holistic multi-turn quality; pairs whose quality gap is spread across several turns supply it."
aliases: ["multi-turn preference contrast", "final-turn contrast limitation", "distributed multi-turn contrast", "multi-turn contrast signal"]
sources: ["arxiv-2512-24693"]
---
# Distributed multi-turn contrast

A preference pair is two conversations, one chosen and one rejected, and a reward model is trained to score the chosen one higher, typically under the [[bradley-terry-preference-model]] loss.[^c1] The loss is fixed; what varies is where the two conversations differ. The authors observe that widely used preference sets "often contain predominantly single-turn pairs or multi-turn pairs where the difference is confined to the final turn".[^c2] Their claim is that such pairs fail to teach the qualities that only show across a dialogue, such as coherence and consistency with earlier turns.

The mechanism they propose is a contrast whose quality gap is spread through the conversation rather than concentrated in one reply. The pair shares a prefix, then the two branches diverge in quality at several turns, so a judge who reads the whole exchange can see the difference at more than one point. In the authors' words the aim is pairs with "quality differences distributed across multiple turns, without human annotation".[^c3] The seed prefix is itself taken from existing data, because "the initial turns often represent valid, human-generated conversational trajectories", and only the later turns are regenerated on each branch.[^c4]

What was measured. A Gemma-2-9B-Instruct reward model trained on the Skywork preference set, with about 31k augmented pairs added to about 73k originals, was used to choose responses in a three-turn best-of-N dialogue. Gemini 1.5 Pro, shown both orders, preferred the conversations guided by the augmented model over those guided by the baseline: "the results consistently demonstrate that conversations guided by the MUSIC-Augmented RM are preferred over those guided by".[^c5] The gap generally widened as N went from 2 to 8. On RewardBench the augmented model stayed level or slightly higher in the chat, safety and reasoning categories, with overall accuracy 85.7 against 87.2.[^c6]

What the experiments do not separate. The only comparison is the augmented training set against the original set. The added pairs differ from the originals in two ways at once: they are multi-turn and they are distributed. I found no run that adds the same number of final-turn-only contrasts, so the gain cannot be credited to distribution over the plain volume of extra multi-turn data. That reading is my inference from the experiment list, not something the work states.

## Limits

- The insufficiency of final-turn pairs is motivated by the authors' reading of existing datasets. No experiment compares final-turn augmentation with distributed augmentation at matched size.
- Both the training pairs and the evaluation depend on an LLM. "these models may introduce their own biases or fail to capture the full" spectrum of human conversational judgment, as the authors themselves note.[^c7]
- Conversations were capped at five simulated turns and three evaluated turns, because of a 2048-token context. "The effectiveness of MUSIC for significantly longer conversations remains to be" explored.[^c8]
- One base model and one preference dataset. Results on other reward model families are not reported.
- The Reasoning category rose from 78.6 to 82.5. The authors offer transfer from multi-turn data as a hypothesis, and it is not tested.[^c9]

## Related

- [[controlled-degradation-contrast]] — how the distributed pairs are manufactured: one branch is generated under an instruction that degrades it at each turn
- [[bradley-terry-preference-model]] — the pairwise objective these pairs are trained under; it is unchanged here, only the pair structure differs
- [[process-reward-model-hackability]] — the step-level alternative. Process reward models score intermediate steps; the work treats conversational turns as the steps of an outcome-level score, where the quality signal is "implicit and distributed rather than discrete and verifiable"[^c10]
- [[reward-benchmark-downstream-correlation]] — a single-turn benchmark such as RewardBench can stay flat while multi-turn behaviour changes, which is why the work reports both

[^c1]: arxiv-2512-24693 — "human preferences under the Bradley-Terry (BT) model (Bradley and Terry, 1952):"
[^c2]: arxiv-2512-24693 — "the difference is confined to the final turn"
[^c3]: arxiv-2512-24693 — "quality differences distributed across multiple turns, without human annotation"
[^c4]: arxiv-2512-24693 — "the initial turns often represent valid, human-generated conversational trajectories"
[^c5]: arxiv-2512-24693 — "the results consistently demonstrate that conversations guided by the MUSIC-Augmented RM are preferred over those guided by"
[^c6]: arxiv-2512-24693
[^c7]: arxiv-2512-24693 — "these models may introduce their own biases or fail to capture the full"
[^c8]: arxiv-2512-24693 — "The effectiveness of MUSIC for significantly longer conversations remains to be"
[^c9]: arxiv-2512-24693 — "exposure to coherent, logically structured multi-turn dialogues during training may implicitly"
[^c10]: arxiv-2512-24693 — "implicit and distributed rather than discrete and"
