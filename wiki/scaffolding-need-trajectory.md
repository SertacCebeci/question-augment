---
description: "In a 207-session corpus, the annotated rate at which a student needs tutor correction roughly doubles from the interview's opening to its diagnostic-closing phase."
aliases: []
sources: ["yang-2026"]
---
# Scaffolding-need trajectory

> How often a novice asker needs correction is not constant across one
> question sequence: expert annotation puts it at roughly one turn in six
> early on and one turn in three by the time the interview is closing in
> on a diagnosis.

## Definition / Mechanism

In the corpus behind Yang et al. (2026)'s gated-tutor trial
([[gated-socratic-scaffolding]]), three clinical experts annotated every
one of 2,350 student turns across 207 clinical-interview sessions (118
multi-agent learning sessions, 89 examination sessions) for whether the
turn needed tutor intervention, using a shared manual with four named
trigger reasons — see `premature-closure` (draft dropped) for one of them. Pooled across
the corpus, approximately 24.1% of student utterances required
instructional scaffolding.[^c1]

That rate was not flat across a session. Yang et al. report that it
increased from approximately 16.1% in the early phase of the consultation
to approximately 34.8% in the late phase.[^c2]

The judgment itself is only moderately reliable across the three experts —
agreement for whether a student utterance required scaffolding was
moderate, with a Fleiss' κ of 0.56 — clearly below the near-perfect
agreement the same experts reached on the more objective question of what
kind of utterance a turn was: agreement was highest for student dialog
intent, with a Fleiss' κ of 0.84, indicating near-perfect agreement.[^c3]

## Why it matters

What was measured is the pair of phase rates (c2). What the authors add
is an explanation they mark as a suggestion: that learners more often
required support when the encounter moved from initial information
gathering toward integration, diagnostic reasoning, and management
decisions. What this wiki infers, one step further, is a scheduling
consequence for a practitioner allocating a fixed intervention budget
across a question sequence: if the need for correction rises toward the
part of the sequence where an asker is converting gathered constraints
into one conclusion, then a uniformly-spaced or front-loaded review policy
checks least often exactly where the annotated need is highest.[^c4]

## Limits

- c2, the note's core figure, was `unverified` at first review because
  the locator could not match the sentence, which wraps across lines in
  the extract [?]; the quote is now the single extract line.
- The 16%/35% rates pool 118 tutored learning sessions (in which 115
  tutor messages were actually delivered) and 89 untutored examination
  sessions, and the paper gives no per-session-type breakdown; in the
  learning sessions the tutor's earlier prompts may have changed the
  turns annotated later, so the pooled curve need not be the novice's
  intrinsic trajectory.
- c4 is this wiki's inference, not the paper's: the paper reports phase
  rates and a suggested explanation; the scheduling consequence rests on
  the assumption that the annotated need is the quantity a review policy
  should track.
- One domain (acute abdominal presentations), one institution, one
  annotation manual; the 16%/35% figures are this corpus's rates, not a
  general law about interview phases.
- "Early" and "late" phase are the paper's own qualitative framing of
  within-session position, not a numerically defined boundary given in the
  text available to this wiki.
- Agreement on *whether* a turn needs help is only moderate (κ = 0.56); the
  trajectory is a trend across many annotated turns, not a precise,
  individually reliable per-turn signal.
- The corpus is human-student-to-AI-patient dialogue; whether the same
  temporal pattern holds against a human patient, under real time
  pressure, is untested here.

## Related

`premature-closure` (draft dropped) · [[gated-socratic-scaffolding]] · [[sprt]] · [[five-whys]]

[^c1]: yang-2026 — "The corpus contained 207 consultation sessions, including 118 multi-agent learning sessions and 89 examination sessions."
[^c2]: yang-2026 — "approximately 16.1% in the early phase of the consultation to approximately 34.8% in the late phase,"
[^c3]: yang-2026 — "Agreement for whether a student utterance required scaffolding was moderate, with a Fleiss’ κ of 0.56."
[^c4]: yang-2026 — "suggesting that learners more often required support when the encounter moved from initial information"
