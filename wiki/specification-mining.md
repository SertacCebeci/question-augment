---
description: "The one distillation procedure on stall 8 that consumes an **unlabelled** Ammons, Bodík & Larus (2002) coined the term for a pipeline that turns recorded runs of a program into a finite automaton d…"
aliases: ["specification mining", "mining specifications", "specification miner"]
sources: ["ammons-2002", "ammons-2003", "gold-1967"]
---
# Specification mining

> The one distillation procedure on stall 8 that consumes an **unlabelled**
> record and declares no [[possible-worlds|hypothesis space]] — it pays by substituting
> **frequency for correctness**, and by relocating the cost onto a human who
> must then debug the distillate.

## Mechanism

Ammons, Bodík & Larus (2002) coined the term for a pipeline that turns[^s1][^s2][^s3]
recorded runs of a program into a finite automaton describing the protocol
its API calls obey: tracer → flow-dependence annotator → scenario extractor →
automaton learner. The founding assumption, stated in the paper's abstract
and introduction, is that an executing program generally uses an API or ADT
correctly — often enough that its common behaviour reveals the protocol, even
when the program contains errors (ammons-2002). Nothing in the input is
labelled correct; **common behaviour is taken to be correct behaviour**.

Three declarations stand where a hypothesis language would be:

1. an expert-supplied table, written once per API, of which interaction
   attributes *define* an object and which *use* it — this is what the
   dependence annotator needs and what the paper names as future work to
   automate;
2. **scenario seeds** — the interactions around which scenarios are cut — and
   a bound on how many objects and neighbouring interactions a scenario may
   contain;
3. a **cutoff** for the corer.

Learning is two steps. An off-the-shelf probabilistic-automaton learner
generalises the standardised scenario strings; then the **corer** computes
each edge's *heat* — its likelihood of being traversed while generating a
string, obtained by inverting a matrix as a Markov-chain problem, explicitly
not its raw count — deletes every edge below the cutoff, drops the
probabilities, and returns an NFA that a human validates by inspection.

The paper's own framing of why it has no guarantee is the load-bearing part.
Finding an automaton that generates exactly the correct traces is unsolvable;
identifying the correct scenario set in the limit is undecidable, by Gold's (1967) result on language identification; and the surviving
probabilistic-approximation problem is not efficiently learnable under
reasonable distance metrics, with efficient solutions known only for acyclic
deterministic targets. What runs is a greedy learner with **no approximation
guarantee**, justified only by producing succinct output in practice.

## Why it matters

Stall 8 asks how a pile of answers becomes one artifact. [[version-space]]
answers *only if the answer space was declared first*. This is the same job
done without that declaration — and it shows the precondition does not
vanish, it changes type: from *the space of possible answers* to *an
equivalence relation on the record plus a price on rarity*.

Two consequences follow that version spaces cannot give. First, **noise never
halts anything**: a wrong answer becomes a low-heat edge the corer deletes,
where a version space would empty. That is also the danger — the same rule
deletes a rare *correct* interaction, and the procedure emits no signal that
it did. Second, **the cost is countable in human decisions**. Their X11
experiment ran an adjudication loop: each new trace that fails verification
sends the expert to decide whether it is a bug or evidence the specification
is too narrow. The expert did not have to inspect 4 of the 16 client
programs; corer and expert disagreed on 5 of the 27 states of the final
automaton. The follow-up (Ammons, Mandelin, Bodík & Larus 2003) states the
residue plainly — miners produce buggy specifications, so the distillate
itself must be debugged — and reports one case cut from 224 human decisions
to 28 by clustering the traces before inspection.

## Known as

| Name | Where | exact / close | Gloss |
|---|---|---|---|
| mining specifications | Ammons et al. 2002 | exact | the paper's title for the same procedure |
| specification miner | Ammons et al. 2002 | close | the artifact that runs the procedure; the two names are used interchangeably in both papers |
| likely invariant detection (Daikon) | Ernst et al., cited in Ammons et al. 2002 §7 | not this object | also learns from dynamic traces, but infers arithmetic relations holding at program points, not temporal and data dependences across API calls; the 2002 paper calls the two complementary and says they require radically different learning algorithms |
| grammar inference / PFSA learning | Ammons et al. 2002 §4.2 | not this object | a replaceable component of the pipeline, not a name for it |

## Transfer

| | Home field | Here |
|---|---|---|
| Record | execution traces of a program presumed mostly debugged | the transcript of question–answer pairs |
| Declared first | definer/user table, seeds, object bound, corer cutoff | an equivalence relation on answers and a price on rarity |
| Correctness signal | frequency across many runs | — no counterpart; see below |
| What survives | the design contract: a distillate is computable from an unlabelled record if the procedure declares what makes two records the same and a cutoff below which content is discarded, and if it treats a rejected record as *ambiguous* between a wrong answer and a too-narrow distillate, needing an adjudicator whose decisions are counted | |
| What does not | correctness-by-frequency, and everything resting on it: it needs many independent runs of a system already known to be mostly right, whereas one questioning session yields one record in which repetition measures the asker, not the world. The automaton form does not travel either — traces draw on a finite alphabet of API calls; free-text answers do not. | |

## Limits

- **The claim that this bears on stall 8 is the wiki's.** No cited source maps
  an answer to an interaction or a specification to a mined automaton; the
  import rests on treating a recorded reply as a traced interaction.
- "Needs no labels" is true of the traces only. The pipeline needs the
  expert's attribute table, the seeds, the scenario bound, the cutoff, and a
  human to validate the resulting automaton by inspection.
- No approximation guarantee exists for the learner actually used; the three
  impossibility results above are the paper's own account of why one is not
  available.
- The evidence is a single experiment on 16 X11 client programs, with an
  author acting as the expert; the 19% corer/expert disagreement is one
  measurement, not a rate.
- Noise tolerance here is a deletion rule, not a diagnosis. Unlike
  [[truth-maintenance-system]] there is no minimal inconsistent set to
  return, and unlike [[version-space]] no event announces that something was
  dropped.

## Related

[[version-space]] · [[backbone-of-a-formula]] · [[sufficient-statistic]] · [[truth-maintenance-system]] · [[agglomerative-information-bottleneck]] · [[qualitative-saturation]]

[^s1]: ammons-2002
[^s2]: ammons-2003
[^s3]: gold-1967
