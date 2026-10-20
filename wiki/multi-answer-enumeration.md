---
description: "Answering several readings of an ambiguous query at once is a third option beside asking and guessing, preferred when the words it adds cost less than the accuracy it gains."
aliases: ["multi-answer", "enumerated answer", "multi-interpretation answer", "answer-all-readings"]
sources: ["arxiv-2512-04068"]
---
# Multi-answer enumeration

An ambiguous question can be handled by asking which reading is meant, by answering
one reading, or by answering several at once. The third option, which this note calls
multi-answer enumeration, gives an answer that covers the candidate readings in one
turn. Berant and colleagues make it an explicit action of the assistant, next to
clarifying and answering. The assistant "can choose one of three actions," among them
"providing multiple interpretations."[^c1]

## Mechanism

Enumeration is a bet on words against accuracy. An answer that names two readings is
longer than a guess, and the length costs something under the reward. The paper gives
the comparison directly: "if a multi-answer adds m words to the final assistant answer
but improves expected accuracy by δ, it is preferable when β · m < δ."[^c2] Here β is
the price of a word, m the words the enumeration adds, and δ the gain in expected
accuracy. Enumeration wins over a guess when the words are cheap relative to what
coverage recovers, and the same comparison as the one for asking holds with the cost
of a turn replaced by the cost of words.

Figure 1 of the paper shows the three regimes as prices change. The assistant asks when
turns are cheap, and it "enumerates multiple interpretations when the cost of
generating a long response is low," and it guesses when both costs are high.[^c3] In
the enumerating case the answer "provides answers for two probable interpretations."[^c4]

The user side of the mechanism matters. When the assistant gives several answers, the
simulated user chooses "the relevant part of the multi-answer" using knowledge of
the interpretation it was assigned.[^c5] So the enumerated answer is useful when a
reader can pick the right part, which in the paper is done by the simulator.

## Transfer

The structure is an expected-value comparison of the kind used for choice under cost:
include an option when its marginal coverage beats its marginal price. What survives
is that comparison and the observation that coverage and length trade against each
other. What does not survive is the claim that enumeration is good in general. The
paper's reward is token F1 against one gold answer, and the cost of length is a single
linear price. A human reader does not pay a fixed price per word; a reader on a small
screen or in a voice interface pays something that depends on the medium. The
abstract names this case: "enumerating several possible interpretations can be
cumbersome on small screens or voice-based settings."[^c7]

The scoring problem has a precedent. [[recall-only-partial-credit]] notes that a
multi-answer item scored by overlap with the gold set is one-sided: it can reward
coverage bought with extra guesses. Here the F1 term does penalise extra words, but
only through the separate length price, so the precision side of enumeration is paid
for by β and nowhere else.

## Limits

The enumerated readings are only as good as the list of interpretations the dataset
supplies. For AmbigQA the authors report that "we found noisy annotations (annotated
interpretations that are not plausible)" and filtered the queries with a model.[^c6]
An enumeration built from a noisy list will name readings that no user intends.

The work does not show that enumeration beats the other two strategies on people. The
user is a language model, instructed not to answer from its own knowledge, and its
ability to pick the relevant part of an enumeration is assumed from instruction-following
checks the authors ran by hand. Whether a human reader would pick the right part, or
would be worn down by a long answer, is not measured.

The paper limits clarifying questions to one, so the combination of asking and
enumerating is tested in a narrow form. I did not read the results for the
clarify-then-enumerate constraint in full, so I cannot say how that combination
compares.

Finally, the enumerated answer is evaluated with F1 against one gold answer, which is
the only accuracy the paper measures. A response that is accurate in a different
reading than the gold one is scored as wrong, even if it is a fair reply.

## Related

- [[steerable-clarification-policy]] — the prices that decide whether enumeration or asking is chosen.
- [[recall-only-partial-credit]] — why an overlap score on a multi-answer item needs its precision beside it.
- [[interpretation-breadth-depth-asymmetry]] — LLM answerers spread over many readings, which is what unrestrained enumeration looks like.
- [[multi-answer-confidence-underestimation]] — the same multi-answer object seen from the confidence side: more correct answers can read as doubt.
- [[interpretation-space]] — the readings an enumeration covers, and the share it addresses.

[^c1]: arxiv-2512-04068 — "answering the query, or providing multiple interpretations"
[^c2]: arxiv-2512-04068 — "it is preferable when β · m < δ"
[^c3]: arxiv-2512-04068 — "enumerates multiple interpretations when the cost of generating a long response is low"
[^c4]: arxiv-2512-04068 — "provides answers for two probable interpretations"
[^c5]: arxiv-2512-04068 — "choose the relevant part of the multi-answer"
[^c6]: arxiv-2512-04068 — "we found noisy annotations"
[^c7]: arxiv-2512-04068 — "enumerating several possible interpretations can be cumbersome on small screens or voice-based settings"
